from .Client import Proxy
import click


class Mock:
    def __init__(self) -> None:
        self.params = {}

    def set(self, key, value):
        self.params[key] = value

    def start(self):
        if '--host' in self.params:
            self.proxy = Proxy(self.params['--host'])
            self.proxy.run()
            return
        click.secho('exec error 缺少参数--host', fg='red', )
