import pymysql

# 创建连接
conn = pymysql.connect(host='localhost', user='root', password='abc123@2024', port=3306, db='test', charset='utf8mb4',
                       autocommit=False)
# 创建游标
cursor = conn.cursor()

# 执行sql
# execute返回值为影响的行数
effect_rows = cursor.execute('insert into t_user(name, age, address) values("tony", 20, "南京"), ("kitty", 20, "北京")')
print(f'insert result: {effect_rows}')
# 提交
conn.commit()

# 查询数据
effect_rows = cursor.execute('select * from t_user')
print(f'select返回值为数据行数: {effect_rows}')
# 获取结果
dataList = cursor.fetchall()
print(f'dataList: {dataList}')

effect_rows = cursor.execute('delete from t_user')
print(f'影响行数：{cursor.rowcount}')
conn.rollback()

cursor.executemany('insert into t_user(name, age, address) values(%s, %s, %s)',
                   [('wilson', 20, '上海'), ('json', 20, '杭州'),])
conn.commit()

cursor.close()
conn.close()



