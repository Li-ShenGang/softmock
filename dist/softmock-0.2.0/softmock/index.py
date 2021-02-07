from .utils.version import version
from .mock.mock import Mock


def launch(host):
    mock = Mock()
    mock.set('--host', host)
    mock.start()
