# soft-mock

## 介绍

soft-mock 是一个录制接口的工具
基于 mitmproxy，并在此基础上对源码进行扩展和修改

## 快速上手

1.安装

```
pip install softmock
```

2.安装 ssl 证书

- 首先设置浏览器的代理地址

```
softmock start
```

启动后看到代理地址，在浏览器高级设置中，将 http 代理地址设置为 localhost:8080

- 下载证书

然后访问 http://mitm.it/ 来下载对应的证书并安装

3.使用

```
softmock start --host baidu.com
```
