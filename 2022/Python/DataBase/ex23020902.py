# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230209
# @Version: 1.0
# @Description: 增加数据

import pymysql

# 1. 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='guest', password='Guest.618',
                        database='hrs', charset='utf8mb4', 
                        autocommit=True, cursorclass=pymysql.cursors.DictCursor)

no = int(input("部门编号："))
name = input("部门名称：")
location = input("部门所在地：")

try:
    # 2. 使用cursor()方法创建一个游标对象cursor
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
                                            'insert into `tb_dept` values (%s, %s, %s)', 
                                            (no, name, location)
            )
        if affected_rows == 1:
            print("新增部门成功！！！")
    # 4. 提交事务(transaction)
    conn.commit()
except pymysql.MySQLError as err:
    # 5. 回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    # 6. 关闭连接释放资源
    conn.close()