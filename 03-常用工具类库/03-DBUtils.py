import pymysql
from dbutils.pooled_db import PooledDB

# 数据库配置信息
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'abc123@2024',
    'database': 'test',
    'charset': 'utf8mb4'
}

# 创建数据库连接池
pool = PooledDB(
    creator=pymysql,    # 使用 pymysql 创建连接
    mincached=1,        # 初始化时，连接池中至少创建的空闲的连接，0表示不创建
    maxcached=5,        # 连接池中最多闲置的连接，0和None表示不限制
    maxconnections=20,  # 连接池允许的最大连接数，0和None表示不限制连接数
    blocking=True,      # 连接池中如果没有可用连接后，是否阻塞等待，True表示等待，False表示不等待然后报错
    maxshared=0,        # all connections are dedicated
    **db_config
)

def query_db(query, args=()):
    # 从连接池中获取一个连接
    conn = pool.connection()
    cursor = conn.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def execute_db(query, args=()):
    # 从连接池中获取一个连接
    conn = pool.connection()
    cursor = conn.cursor()
    effect_rows = cursor.execute(query, args)
    conn.commit()
    cursor.close()
    conn.close()
    return effect_rows

# 使用连接池查询数据库
rows = query_db("SELECT * FROM t_user")
for row in rows:
    print(row)

# 使用连接池执行数据库操作
effect_rows = execute_db("delete from t_user where name = %s and age = %s ", ('tony', 10))
print(effect_rows)