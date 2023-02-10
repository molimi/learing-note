# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230209
# @Version: 1.0
# @Description: 更新数据

import pymysql

no = int(input("部门编号："))
name = input("部门名称：")
location = input("部门所在地：")

# 1.
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', passwd='Guest.618',
                       database='hrs', charset='utf8mb4')

try:
    #
    with conn.cursor() as cursor:
        #
        affected_rows = cursor.execute('update tb_dept set dname=%s, dloc=%s where dno=%s', 
                                       (name, location, no))
        if affected_rows == 1:
            print("更新部门信息成功！！！")
    conn.commit()
except pymysql.MySQLError as err:
    conn.rollback()
    print(type(err), err)
finally:
    conn.close()