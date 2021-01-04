# soft-mock

## 介绍

soft-mock 是一个融合了类似 charles 的代理功能，深耕前端 mock 方面。简化在前端开发过程中的 mock 复杂度。
soft-mock 的核心部分是使用 python3.7 来开发，接口文档部分是使用 react 开发

## 快速上手

#### 安装

- npm 用户：
  `npm i -g soft-mock`
- python3 用户：
  `pip install soft-mock`

#### 开始使用

根据自己的业务需要，监听对应的请求域名，例如：
`soft-mock -h www.baidu.com`
上面这行命令执行后会在浏览器打开一个网页，网页上是所有请求的 host 包含指定 host 的请求，你可以修改访问结果，在下次请求相同的 url 时，将会直接从本地进行返回。
