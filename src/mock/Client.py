import mitmproxy.http
import sys
from mitmproxy import ctx, http
from mitmproxy.tools.main import mitmweb, run as mitmproxy_run
from mitmproxy.tools import web, cmdline
from mitmproxy import options
import sqlite3
# 导入addons
from .addons import Host


class Proxy:
    def __init__(self, host):
        self.host = host
        self.conn = sqlite3.connect("soft_mock.db")
        cursor = self.conn.cursor()
        try:
            sql = "create table Mock (id varchar(100) primary key, detail TEXT, url TEXT)"
            cursor.execute(sql)
            sql = "create table Html (url varchar(100) primary key, filepath TEXT)"
            cursor.execute(sql)
        except:
            pass

    def server_start(self):
        sys.argv = sys.argv[0:1]
        addons = [Host(self.host, self.conn)]  # 添加插件
        mitmproxy_run(web.master.WebMaster, cmdline.mitmweb,
                      ['--host', self.host], extend_addons=addons)
        return None

    def run(self):
        print(f'开始记录host：{self.host}，网络请求')
        result = self.server_start()
        self.conn.close()
        sys.exit(result)
