from pymysql import Connection

# 连接对象
conn = Connection(
    host="localhost",   # 主机名
    port=3306,          # 默认3306
    user='root',        # 账户
    password="123456"   # 密码
)

# 打印服务器信息
print(conn.get_server_info())

# 执行sql查询
# 先取得游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db('world')

# 使用execute来执行命令，此处创建表，
# 小提示，在pymysql中可不写;符号
# cursor.execute('create table test_pymysql(id int);')

# 查询student
# 通过fetchall()取得结果, 注意，返回的是元组<class 'tuple'>
cursor.execute('select * from student')
results: tuple = cursor.fetchall()
# print(results)  # ((100001, '栾淑静', 20, '女'), (100002, '鲜于梦琪', 55, '女'), ...)
for r in results:
    print(r)    # 打印单条

# 与文件读取一直，使用后关闭
conn.close()
