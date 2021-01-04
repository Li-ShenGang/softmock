from .utils.version import version
from .utils.args import pattern
from .mock.mock import Mock

def launch(args):
    _pattern = arg_pattern(args)
    mock = Mock()
    for k, v in _pattern.items():
        mock.set(k, v)
    mock.start()
    

def arg_pattern(args):
    """
    转换处理参数
    """
    result = {}
    for index, arg in enumerate(args):
        if arg.startswith('-'):
            value =  None if index == len(args) - 1 else None  if args[index+1].startswith('-') else args[index+1]
            result[pattern.get(arg) or arg] = value
    if '--version' in result:
        result['--version'] = version
    return result
    