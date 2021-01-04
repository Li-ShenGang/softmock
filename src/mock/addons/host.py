import mitmproxy.http
from mitmproxy import ctx
from functools import wraps


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
        self.sentry(flow)

    def sentry(self, flow):
        return

    @exclude_host
    def response(self, flow: mitmproxy.http.HTTPFlow):
        text = flow.response.get_text()
        flow.response.set_text('this_a_page')
