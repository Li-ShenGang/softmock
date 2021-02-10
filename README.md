# softmock

## 介绍

**softmock 是一个拦截 http/https 到本地的工具。**

**请求拦截到本地之后，可以进行修改、新增等操作，使下次请求直接返回到本地的数据。而不依赖远程服务器。**

_softmock 是从 抓包工具[mitmproxy](https://github.com/mitmproxy/mitmproxy) 经过修改，重构实现_

_前端地址：[softmock-template](https://github.com/web-trump/softmock-template)_

## 快速上手

### 1.安装准备

在使用之前请先使 python 的版本至少为 python3.8

[python 官网](https://python.org)

### 2.安装

```
pip install softmock
```

### 3.使用

#### 监听 host

```
softmock --host httpbin.org
```

这时会自动打开一个浏览器窗口，该窗口既是工作窗口

可以通过访问监听的链接查看拦截情况。在浏览器访问[http://httpbin.org/ip](http://httpbin.org/ip)

可以看到左侧列表监听到了

#### 修改数据

修改相应的内容，则下次请求次链接则返回修改后的内容

#### 监听 https 请求

默认情况下是不能正常监听`https`链接的，需要安装 ssl 证书

```
softmock
```

启动后，直接访问[http://mitm.it/](http://mitm.it/)来下载对应的证书并信任

### 4.其他命令

- `softmock -v` 查看版本
- `softmock --clear-all`清除数据库中所有的数据
- `softmock --help`查看帮助
