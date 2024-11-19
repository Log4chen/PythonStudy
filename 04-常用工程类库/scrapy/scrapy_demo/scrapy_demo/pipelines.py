# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
from dbutils.pooled_db import PooledDB


class PoemPipeline:
    pool = None

    def __init__(self):
        # 数据库配置信息
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'abc123@2024',
            'database': 'test',
            'charset': 'utf8mb4'
        }

        # 创建数据库连接池
        self.pool = PooledDB(
            creator=pymysql,  # 使用 pymysql 创建连接
            mincached=1,  # 初始化时，连接池中至少创建的空闲的连接，0表示不创建
            maxcached=5,  # 连接池中最多闲置的连接，0和None表示不限制
            maxconnections=20,  # 连接池允许的最大连接数，0和None表示不限制连接数
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待，True表示等待，False表示不等待然后报错
            maxshared=0,  # all connections are dedicated
            **db_config
        )
    def process_item(self, item, spider):
        sql = f'insert into poem value{item["title"], item["author"], item["dynasty"], item["content"]}'
        self.execute_db(sql)
        return item

    def execute_db(self, sql, args=()):
        # 从连接池中获取一个连接
        conn = self.pool.connection()
        cursor = conn.cursor()
        effect_rows = cursor.execute(sql, args)
        conn.commit()
        cursor.close()
        conn.close()
        return effect_rows