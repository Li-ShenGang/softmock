import sys
import platform
import os
import subprocess
from mitmproxy.tools.main import run as mitmproxy_run
from mitmproxy.tools import web, cmdline
import sqlite3
import click

# 导入addons
from .addons import Host

current_path = os.path.abspath(os.path.dirname(__file__))
database = os.path.join(current_path, "soft_mock.db")


class Proxy:
    def __init__(self, host):
        self.host = host
        self.conn = sqlite3.connect(database)
        self.network_list = ['Wi-Fi', 'Ethernet']
        cursor = self.conn.cursor()
        try:
            sql = "create table Mock1 (id varchar(100) primary key, detail TEXT, url TEXT, status Text)"
            cursor.execute(sql)
            sql = "create table Html (url varchar(100) primary key, filepath TEXT)"
            cursor.execute(sql)
        except:
            pass

    def set_browser_proxy(self):

        proxy = "localhost"
        port = 8080

        if platform.system() == 'Windows':
            self.set_windows(proxy, port)
        else:
            self.set_other_platform(proxy, port)

    def set_windows(self, proxy, port):
        import winreg
        INTERNET_SETTINGS = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_ALL_ACCESS)

        def set_key(name, value):
            _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
            winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)
        try:
            set_key('ProxyEnable', 1)
        except:
            click.secho(f'ProxyEnable设置失败，和可能需要手动设置代理', fg='yellow')
        # Bypass the proxy for localhost
        try:
            set_key('ProxyOverride', u'*.local;<local>')
        except:
            click.secho(f'ProxyOverride设置失败，和可能需要手动设置代理', fg='yellow')
        try:
            set_key('ProxyServer', f'{proxy}:{port}')
        except:
            click.secho(f'ProxyServer设置失败，和可能需要手动设置代理', fg='yellow')

    def close_windows(self):
        import winreg
        INTERNET_SETTINGS = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_ALL_ACCESS)

        def set_key(name, value):
            _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
            winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)
        try:
            set_key('ProxyEnable', 0)
            set_key('ProxyServer', f'')
        except:
            pass

    def set_other_platform(self, proxy, port):
        try:
            li = subprocess.getoutput(
                'networksetup -listallnetworkservices').split('\n')
            for net in li:
                if len([i for i in self.network_list if i in net]):
                    # 设置http代理
                    os.system(
                        f'networksetup -setwebproxy "{net}" {proxy} {port}')
                    # 设置https代理
                    os.system(
                        f'networksetup -setsecurewebproxy "{net}" {proxy} {port}')
        except:
            click.secho(f'auto-proxy 设置失败，和可能需要手动设置代理', fg='yellow')

    def close_other_platform(self):
        li = subprocess.getoutput(
            'networksetup -listallnetworkservices').split('\n')
        for net in li:
            if len([i for i in self.network_list if i in net]):
                # 关闭http代理
                os.system(f'networksetup -setwebproxystate "{net}" off')
                # 关闭https代理
                os.system(f'networksetup -setsecurewebproxystate "{net}" off')

    def browser_proxy_off(self):
        if platform.system() == 'Windows':
            self.close_windows()
        else:
            self.close_other_platform()

    def server_start(self):
        sys.argv = sys.argv[0:1]
        addons = [Host(self.host, self.conn)]  # 添加插件
        # 设置浏览器代理
        self.set_browser_proxy()
        mitmproxy_run(web.master.WebMaster, cmdline.mitmweb,
                      ['--host', self.host], extend_addons=addons)
        # 关闭浏览器代理
        self.browser_proxy_off()
        click.secho(f'softmock已安全关闭', fg='#71b83f')
        return None

    def run(self):
        print(f'开始记录host：{self.host}，网络请求')
        result = self.server_start()
        self.conn.close()
        sys.exit(result)
