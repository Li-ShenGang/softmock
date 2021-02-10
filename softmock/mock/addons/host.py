import sqlite3
import json
import base64
from mitmproxy import ctx
import mitmproxy
from urllib import parse
from functools import wraps
from softmock.mock.Client import database

null = None
false = False
undefined = None


class Host:
    def __init__(self, host, conn) -> None:
        self.host = host

    def exclude_host(fn):
        """
        排除不满足host条件的请求
        """
        @wraps(fn)
        def wrapper(self, flow):
            return fn(self, flow) if ctx.options.host in flow.request.host else None

        return wrapper

    # @exclude_host
    # def http_connect(self, flow: mitmproxy.http.HTTPFlow):
    #     '''
    #     在应用层，dns查询之前
    #     '''
    #     print(flow.server_conn.__dict__)

    @exclude_host
    def request(self, flow: mitmproxy.http.HTTPFlow):
        '''
        网络层
        dns查询之后
        '''
        url = flow.request.scheme + '://' + \
            flow.request.host + \
            flow.request.path.split('?')[0] + ' ' + flow.request.method
        db = sqlite3.connect(database)
        cursor = db.cursor()
        sql = f"select * from Mock1 where url='{url}' and status='1'"
        print(f'拦截{url}到本地')
        result = cursor.execute(sql)
        js = [i for i in cursor.execute(sql)]
        if len(js) > 0:
            result = json.loads(parse.unquote(js[0][1]))
            # flow.response = result['data']['response']
            response = result['data'].get('response', None)
            if not response:
                return None
            headers = {}
            try:
                for header in response['headers']:
                    headers[header[0]] = header[1]
            except:
                pass
            content_type = headers.get(
                'content-type', None) or headers.get('Content-Type', None)
            html = response['html']
            if 'image' in content_type or 'video' in content_type:
                html = base64.b64decode(html.encode())
            flow.response = mitmproxy.http.HTTPResponse.make(
                response['status_code'] or 200,  # (optional) status code
                html,  # (optional) content
                headers  # (optional) headers
            )

        cursor.close()
        db.close()

    def sentry():
        pass

    @exclude_host
    def response(self, flow: mitmproxy.http.HTTPFlow):
        pass
        # text = flow.response.get_text()
        # flow.response.set_text('this_a_page')
