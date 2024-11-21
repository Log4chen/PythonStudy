from mitmproxy import ctx
import mitmproxy.http
import json

class ModifyRespAddon():
    # 所有发出的请求数据包都会被这个方法所处理
    def response(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log.info('ModifyRespAddon')
        response = flow.response
        content = response.content.decode('utf-8')
        json_dict = json.loads(content)
        json_dict['mitmproxy'] = 'mitmproxy攻击添加的内容'
        # 序列化时不要将非ASCII字符转换为ASCII转义序列
        resp = json.dumps(json_dict, ensure_ascii=False)
        response.set_text(resp)
