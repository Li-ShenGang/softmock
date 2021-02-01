from mitmproxy.net.http import response
import mitmproxy.http
import sqlite3
import json
from mitmproxy import ctx
from urllib import parse
from functools import wraps

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
            return fn(self, flow) if self.host in flow.request.host else None

        return wrapper

    @exclude_host
    def request(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log.info("访问" + self.host)
        url = flow.request.scheme + '://' + \
            flow.request.host + flow.request.path.split('?')[0]
        db = sqlite3.connect("soft_mock.db")
        cursor = db.cursor()
        sql = f"select * from Mock1 where url='{url}' and status='1'"
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
            flow.response = mitmproxy.http.HTTPResponse.make(
                response['status_code'],  # (optional) status code
                response['html'],  # (optional) content
                headers  # (optional) headers
            )

        cursor.close()
        db.close()

    @exclude_host
    def response(self, flow: mitmproxy.http.HTTPFlow):
        pass
        # text = flow.response.get_text()
        # flow.response.set_text('this_a_page')
