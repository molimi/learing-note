# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230209
# @Version: 1.0
# @Description: 删除数据

import pymysql

dno = int(input("部门编号："))

# 1. 创建连接(Connection)
conn = pymysql.connect(host='127.0.0.1', port=3306, 
                       user='guest', passwd='Guest.618', 
                       database='hrs', charset='utf8mb4',
                       autocommit=True)

try:
    # 2. 获取游标对象(Cursor)
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute('delete from tb_dept where dno=%s', (dno, ))
        if affected_rows == 1:
            print("删除部门成功！！！")
finally:
    # 4. 关闭连接释放资源
    conn.close()        