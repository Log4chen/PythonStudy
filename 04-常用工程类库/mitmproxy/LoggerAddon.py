import mitmproxy.http
from mitmproxy import ctx

class LoggerAddon():
    # 所有发出的请求数据包都会被这个方法所处理
    def request(self, flow: mitmproxy.http.HTTPFlow):
        request = flow.request
        ctx.log.info('request url %s' % request.url)

    # 所有服务器响应的数据包都会被这个方法处理
    def response(self, flow: mitmproxy.http.HTTPFlow):
        response = flow.response
        ctx.log.info('response status %s' % response.status_code)
        ctx.log.info('response content-type %s' % response.headers.get('content-type'))
        ctx.log.info('response content %s' % response.content.decode('utf-8'))
