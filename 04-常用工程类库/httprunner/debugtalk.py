import time
from datetime import datetime

'''
debugtalk.py 用于存放自定义的辅助函数和变量，以便在测试用例中被引用
'''
# 定义一些全局变量
API_KEY = "your_api_key"
USERNAME = "your_username"
PASSWORD = "your_password"

# 定义一个生成当前时间的函数
def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def sleep_seconds(secs) -> bool:
    time.sleep(secs)
    print(f'等待{secs}秒')
    return False