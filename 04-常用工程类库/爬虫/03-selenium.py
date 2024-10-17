from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

'''
需要先安装对应浏览器的驱动，如chrome、edge
edge https://learn.microsoft.com/zh-cn/microsoft-edge/webdriver-chromium
phantomjs 可以在没有图形用户界面的情况下运行网页和浏览器脚本(phantomjs已停止维护)

'''
# 设置 Edge 无头模式选项
options = Options()
options.use_chromium = True
options.add_argument("--headless")  # 启用无头模式
options.add_argument("--window-size=1920,1080")  # 设置窗口大小

# 如果没有把driver路径添加到系统的环境变量中，需要指定driver路径
service = Service(executable_path='D:\Program Files\edgedriver_win64\msedgedriver.exe')

driver = webdriver.Edge(service=service, options=options)

driver.get('https://baidu.com')

time.sleep(3)

input = driver.find_element(by=By.ID, value='kw')
input.send_keys("hello")

button = driver.find_element(By.ID, 'su')
button.click()

html = driver.page_source

print(html)

driver.close()
