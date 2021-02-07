# softmock

## 介绍

softmock 是一个录制接口的工具。基于 mitmproxy，并在此基础上对源码进行扩展和修改

## 快速上手

### 1.安装

```
pip install softmock
```

### 2.使用

#### 监听 host

```
softmock --host httpbin.org
```

这时会自动打开一个浏览器窗口，该窗口既是工作窗口

可以通过访问监听的链接查看拦截情况。在浏览器访问`http://httpbin.org/ip`

可以看到左侧列表监听到了

#### 修改数据

修改相应的内容，则下次请求次链接则返回修改后的内容

#### 监听 https 请求

默认情况下是不能正常监听`https`链接的，需要安装 ssl 证书

```
softmock
```

启动后，直接访问`http://mitm.it/`来下载对应的证书并信任
