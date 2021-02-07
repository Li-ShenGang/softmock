from .utils.version import version
from .utils.args import pattern
from .mock.mock import Mock


def launch(host):
    mock = Mock()
    mock.set('--host', host)
    mock.start()
