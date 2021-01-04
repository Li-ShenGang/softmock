from .Client import Proxy

class Mock:
    def __init__(self) -> None:
        self.params = {}
    def set(self, key, value):
        self.params[key] = value
    def start(self):
        if '--version' in self.params:
            version = 'soft-mock v' + self.params['--version']
            print(version)
            return version
        if '--host' in self.params:
            self.proxy = Proxy(self.params['--host'])
            self.proxy.run()
            return
        print('exec error 缺少参数--host')

        