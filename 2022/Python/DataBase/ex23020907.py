# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230209
# @Version: 1.0
# @Description: 数据导入到Excel中

import openpyxl
import pymysql

# 创建工作簿对象
workbook = openpyxl.Workbook()
# 获得默认的工作表
sheet = workbook.active
# 修改工作表的标题
sheet.title = '员工基本信息'
# 给工作表添加表头
sheet.append(('工号', '姓名', '职位', '月薪', '补贴', '部门'))
# 创建连接(Connection)
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', passwd='Guest.618',
                       database='hrs', charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        cursor.execute('select eno, ename, job, sal, coalesce(comm, 0), dname '
                       'from tb_emp natural join tb_dept')
        row = cursor.fetchone()
        while row:
            # 将数据逐行写入工作表中
            sheet.append(row)
            row = cursor.fetchone()

    # 保存工作簿
    workbook.save('hrs.xlsx')
except pymysql.MySQLError as err:
    print(err)
finally:
    cursor.close()
