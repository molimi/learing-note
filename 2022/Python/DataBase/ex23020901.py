# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230209
# @Version: 1.0
# @Description: 创建表格并插入数据

import pymysql

# 1. 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='guest', password='Guest.618',
                        database='hrs', charset='utf8mb4', 
                        autocommit=True)

# 2. 使用cursor()方法创建一个游标对象cursor
cursor = conn.cursor()

# 使用execute()方法执行SQL，如果表存在则删除
cursor.execute('drop table if exists tb_dept')
# 使用预处理语句创建表
sql = '''
-- 创建部门表
create table `tb_dept`
(
    `dno` int not null comment '编号',
    `dname` varchar(10) not null comment '名称',
    `dloc` varchar(20) not null comment '所在地',
    primary key (`dno`)
);
'''
# 执行SQL语句
cursor.execute(sql)

data = [(10, '会计部', '北京'),
        (20, '研发部', '成都'),
        (30, '销售部', '重庆'),
        (40, '运维部', '深圳')]

try:
    # 3. 通过游标对象向数据库服务器发出SQL语句，插入多条数据
    affected_rows = cursor.executemany("insert into tb_dept (dno, dname, dloc) values (%s, %s, %s)", data)
    # 提交数据
    if affected_rows == 4:
        print("数据添加成功！！！")
    # 4. 提交事务
    conn.commit()
except pymysql.MySQLError as err:
    # 5. 发生错误时回滚
    conn.rollback()
    print(type(err), err)
finally:
    # 6. 关闭数据库连接释放资源
    conn.close()