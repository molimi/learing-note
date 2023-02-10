程序运行时，数据都在内存中，程序终止时，需要将数据保存到磁盘上。为了便于程序保存和读取，并能直接通过条件快速查询到指定数据，数据库(Database)应运而生，本篇主要学习使用Python操作数据库，在 Python3 中，我们可以使用 `mysqlclient`或者 `pymysql`三方库来接入 MySQL 数据库并实现数据持久化操作。二者的用法完全相同，只是导入的模块名不一样。我们推荐大家使用纯 Python 的三方库 `pymysql`，因为它更容易安装成功。

## 1 数据库编程接口

项目开发中，数据库应用必不可少。数据库种类包括：SQLite，MySQL，Oracle，SQL Server等，其基本功能都是一样的。为了对数据库进行统一操作，大多数语言都提供了简单的、标准化的数据库接口(API)。在Python Database 2.0规范中，定义了Python数据库API接口的各个部分，如模块接口，连接对象，类型对象等等。

### 1.1 连接对象

数据库连接对象(Connection Object)主要提供获取数据库游标对象和提交、回滚事务的方法，以及关闭数据库连接。

**1．获取连接对象**

如何获取连接对象呢？这就需要使用`connect()`函数。该函数有多个参数，具体使用哪个参数，取决于使用的数据库类型。例如，需要访问Oracle数据库和MySQL数据库，则必须同时下载Oracle和MySQL数据库模块。这些模块在获取连接对象时，都需要使用`connect()`函数。

例如，使用PyMySql模块连接MySQL数据库，示例代码如下：
```python
conn = pymysql.connect(host='localhost', port=3306,
                        user='user', password='passwd',
                        database='test', charset='utf8mb4')
```
**2. 连接对象的方法**
`Connect()`函数返回连接对象。这个对象表示日前和数据库的会话，连接对象支持的方法如下表所示。
|  方法名  |  说明  |
|--|--|
| close() | 关闭数据库连接 |
|	commit()   |	提交事务|
|	rollback()  |	回滚事务|
|	cursor()  |	  获取游标对象，操作数据库，如执行DML操作，调用存储过程等  |

`commit()`方法用于提交事务，事务主要用于处理数据量大、复杂度高的数据。如果操作的是一系列的动作，比如张三给李四转账，有如下2个操作:
- 张三账户金额减少
- 李四账户金额增加
这时使用事务可以维护数据库的完整性，保证2个操作要么全部执行，要么全部不执行。

### 1.2 游标对象

游标对象(Cursor Object)代表数据库中的游标，用于指示抓取数据操作的上下文，主要提供执行SQL语句、调用存储过程、获取查询结果等方法。
如何获取游标对象呢?通过使用连接对象的cursor()方法，可以获取到游标对象。游标对象的属性如下所示:
- description：数据库列类型和值的描述信息。
- rowcount：回返结果的行数统计信息，如SELECT、UPDATE、CALLPROC等。

游标对象的方法如下表所示。

|  方法名  |  说明  |
|--|--|
|	`callproc(procname,[, parameters])`	|	调用存储过程，需要数据库支持	|
|	`close()`	|	关闭当前游标	|
|	`execute(operation[, parameters])`	|	执行数据库操作，SQL语句或者数据库命令	|
|	`executemany(operation, seq_of params)`	|	用于批量操作，如批量更新	|
|	`fetchone()`	|	获取查询结果集中的下一条记录	|
|	`fetchmany(size)`	|	获取指定数量的记录	|
|	`fetchall()`	|	获取结果集的所有记录	|
|	`nextset()`	|	跳至下一个可用的结果集	|
|	`arraysize`	|	指定使用`fetchmany()`获取的行致，默认为1	|
|	`setinputsizes(sizes)`	|	设置在调用`cxecutc*()`方法时分配的内存区域大小	|
|	`setoutputsize(sizes)`	|	设置列缓冲区大小，对大数据列(如 LONGS和 BLOBS)尤其有用	|

小结：
使用pymysql操作 MySQL 的步骤如下所示：
- 创建连接。MySQL服务器启动后，提供了基于TCP(传输控制协议)的网络服务。我们可以通过pymysql模块的connect函数连接 MySQL 服务器。在调用connect函数时，需要指定主机(host)、端口(port)、用户名(user)、口令(password)、数据库(database)、字符集(charset)等参数，该函数会返回一个Connection对象。
- 获取游标。连接 MySQL 服务器成功后，接下来要做的就是向数据库服务器发送 SQL 语句，MySQL 会执行接收到的 SQL 并将执行结果通过网络返回。要实现这项操作，需要先通过连接对象的cursor方法获取游标(Cursor)对象。
- 发出 SQL。通过游标对象的execute方法，我们可以向数据库发出 SQL 语句。
- 如果执行insert、delete或update操作，需要根据实际情况提交或回滚事务。因为创建连接时，默认开启了事务环境，在操作完成后，需要使用连接对象的commit或rollback方法，实现事务的提交或回滚，rollback方法通常会放在异常捕获代码块except中。如果执行select操作，需要通过游标对象抓取查询的结果，对应的方法有三个，分别是：fetchone、fetchmany和fetchall。其中fetchone方法会抓取到一条记录，并以元组或字典的方式返回；fetchmany和fetchall方法会抓取到多条记录，以嵌套元组或列表装字典的方式返回。
- 关闭连接。在完成持久化操作后，请不要忘记关闭连接，释放外部资源。我们通常会在finally代码块中使用连接对象的close方法来关闭连接。

### 2 代码实战

#### 2.1 创建表与插入数据
```python
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
    if affected_rows == 1:
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
```
说明：上面的`127.0.0.1`称为回环地址，它代表的是本机。下面的guest是我提前创建好的用户，该用户拥有对hrs数据库的insert、delete、update和select权限。不建议大家在项目中直接使用root超级管理员账号访问数据库，这样做实在是太危险了。我们可以使用下面的命令创建名为guest的用户并为其授权。
```mysql
create user 'guest'@'%' identified by 'Guest.618';
grant insert, delete, update, select, create, drop on `hrs`.* to 'guest'@'%';
```
如果要插入大量数据，建议使用游标对象的executemany方法做批处理（一个insert操作后面跟上多组数据）。游标对象的executemany方法第一个参数仍然是 SQL 语句，第二个参数可以是包含多组数据的列表或元组。

```python
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
```
### 2.2 删除数据
```python
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
```
说明：如果不希望每次 SQL 操作之后手动提交或回滚事务，可以connect函数中加一个名为autocommit的参数并将它的值设置为True，表示每次执行 SQL 成功后自动提交。但是我们建议大家手动提交或回滚，这样可以根据实际业务需要来构造事务环境。如果不愿意捕获异常并进行处理，可以在try代码块后直接跟finally块，省略except意味着发生异常时，代码会直接崩溃并将异常栈显示在终端中。

### 2.3 更新数据

```python
import pymysql

no = int(input("部门编号："))
name = input("部门名称：")
location = input("部门所在地：")

# 1. 创建连接(Connection)
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', passwd='Guest.618',
                       database='hrs', charset='utf8mb4')

try:
    # 2. 获取游标对象(Cursor)
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute('update tb_dept set dname=%s, dloc=%s where dno=%s', 
                                       (name, location, no))
        if affected_rows == 1:
            print("更新部门信息成功！！！")
    # 4. 回滚事务
    conn.commit()
except pymysql.MySQLError as err:
    conn.rollback()
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()
```


### 2.4 查询数据
```python
import pymysql


# 1. 创建连接(Connection)
conn = pymysql.connect(host='127.0.0.1', port=3306, 
                       user='guest', passwd='Guest.618', 
                       database='hrs', charset='utf8mb4',
                       autocommit=True)

try:
    # 2. 获取游标对象(Cursor)
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        cursor.execute('select dno, dname, dloc from tb_dept')
         # 4. 通过游标对象抓取数据
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
except pymysql.MySQLError as err:
    print(type(err), err)
finally:
    # 4. 关闭连接释放资源
    conn.close()    
```
上面的代码中，我们通过构造一个while循环实现了逐行抓取查询结果的操作。这种方式特别适合查询结果有非常多行的场景。因为如果使用fetchall一次性将所有记录抓取到一个嵌套元组中，会造成非常大的内存开销，这在很多场景下并不是一个好主意。

### 2.5 案例讲解
下面为大家讲解一个将数据库表数据导出到 Excel 文件的例子，我们需要先安装openpyxl三方库。

```sql
-- 创建员工表
create table `tb_emp`
(
`eno` int not null comment '员工编号',
`ename` varchar(20) not null comment '员工姓名',
`job` varchar(20) not null comment '员工职位',
`mgr` int comment '主管编号',
`sal` int not null comment '员工月薪',
`comm` int comment '每月补贴',
`dno` int not null comment '所在部门编号',
primary key (`eno`),
constraint `fk_emp_mgr` foreign key (`mgr`) references tb_emp (`eno`),
constraint `fk_emp_dno` foreign key (`dno`) references tb_dept (`dno`)
);

-- 插入14个员工
insert into `tb_emp` values 
    (7800, '张三丰', '总裁', null, 9000, 1200, 20),
    (2056, '乔峰', '分析师', 7800, 5000, 1500, 20),
    (3088, '李莫愁', '设计师', 2056, 3500, 800, 20),
    (3211, '张无忌', '程序员', 2056, 3200, null, 20),
    (3233, '丘处机', '程序员', 2056, 3400, null, 20),
    (3251, '张翠山', '程序员', 2056, 4000, null, 20),
    (5566, '宋远桥', '会计师', 7800, 4000, 1000, 10),
    (5234, '郭靖', '出纳', 5566, 2000, null, 10),
    (3344, '黄蓉', '销售主管', 7800, 3000, 800, 30),
    (1359, '胡一刀', '销售员', 3344, 1800, 200, 30),
    (4466, '苗人凤', '销售员', 3344, 2500, null, 30),
    (3244, '欧阳锋', '程序员', 3088, 3200, null, 20),
    (3577, '杨过', '会计', 5566, 2200, null, 10),
    (3588, '朱九真', '会计', 5566, 2500, null, 10);
```
接下来，我们通过下面的代码实现了将数据库hrs中所有员工的编号、姓名、职位、月薪、补贴和部门名称导出到一个 Excel 文件中。
```python
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
```