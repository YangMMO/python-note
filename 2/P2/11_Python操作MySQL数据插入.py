from pymysql import Connection

connect = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True         # 自动确认
)

connect.select_db('world')
cursor = connect.cursor()

cursor.execute('insert into student values(100012, "jacky", 33, "男")')

# 手动确认insert的数据
# connect.commit()

connect.close()
