"""
In mitmproxy, protocols are implemented as a set of layers, which are composed
on top each other. The first layer is usually the proxy mode, e.g. transparent
proxy or normal HTTP proxy. Next, various protocol layers are stacked on top of
each other - imagine WebSocket on top of an HTTP Upgrade request. An actual
mitmproxy connection may look as follows (outermost layer first):

    Transparent HTTP proxy, no TLS:
      - TransparentProxy
      - Http1Layer
      - HttpLayer

    Regular proxy, CONNECT request with WebSocket over SSL:
      - ReverseProxy
      - Http1Layer
      - HttpLayer
      - TLSLayer
      - WebSocketLayer (or TCPLayer)

Every layer acts as a read-only context for its inner layers (see
:py:class:`Layer`). To communicate with an outer layer, a layer can use
functions provided in the context. The next layer is always determined by a
call to :py:meth:`.next_layer() <mitmproxy.proxy.RootContext.next_layer>`,
which is provided by the root context.

Another subtle design goal of this architecture is that upstream connections
should be established as late as possible; this makes server replay without any
outgoing connections possible.
"""


from .base import Layer, ServerConnectionMixin
from .http import UpstreamConnectLayer
from .http import HttpLayer
from .http1 import Http1Layer
from .http2 import Http2Layer
from .websocket import WebSocketLayer
from .rawtcp import RawTCPLayer
from .tls import TlsLayer

__all__ = [
    "Layer", "ServerConnectionMixin",
    "TlsLayer",
    "UpstreamConnectLayer",
    "HttpLayer",
    "Http1Layer",
    "Http2Layer",
    "WebSocketLayer",
    "RawTCPLayer",
]
