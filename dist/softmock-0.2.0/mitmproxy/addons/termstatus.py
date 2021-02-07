from mitmproxy import ctx
from mitmproxy.utils import human

"""
    A tiny addon to print the proxy status to terminal. Eventually this could
    also print some stats on exit.
"""


class TermStatus:
    def running(self):
        if ctx.master.server.bound:
            ctx.log.info(
                "代理服务器监听端口在： http://{}".format(
                    human.format_address(ctx.master.server.address)
                )
            )
            ctx.log.info(
                "--------------------"
            )
