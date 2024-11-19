### scrapy命令
```shell
# start a new project
scrapy startproject project_name
# shell请求网页，用于调试和测试
scrapy shell url
# 启动爬虫，spider_name为scrapy.Spider子类中给name属性的赋值
scrapy crawl spider_name
# 将爬虫结果输出到文件
scrapy crawl gushiwen -o gushiwen.json
```

### 项目结构
#### spiders
用来存放我们写爬虫文件的地方

#### items.py
用来定义我们要存储数据的字段

#### middlewares.py 
就是中间件，在这里面可以做一些在爬虫过程中想干的事情，比如爬虫在响应的时候你可以做一些操作

#### pipelines.py
这是我们用来定义一些存储信息的文件，比如我们要连接 MySQL或者 MongoDB 就可以在这里定义

#### settings.py
这个文件用来定义我们的各种配置，比如配置请求头信息、输出字符编码等