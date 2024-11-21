```shell
pip install mitmproxy

# 启动代理，默认8080端口，web页面方式操作，web地址127.0.0.1:8081，类似fiddler
mitmweb [-s demo.py]
# 主要是以控制台的方式交互
mitmproxy [-s demo.py]
# 主要是以命令行的方式交互
mitmdump [-s demo.py]

# Chrome 以及 8080 端口代理运行
chrome.exe --proxy-server=127.0.0.1:8080 --ignore-certificate-errors
```






