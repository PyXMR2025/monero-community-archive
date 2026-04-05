---
title: 无法运行程序，连接被拒绝，log无颜色
source_url: https://github.com/xmrig/xmrig/issues/2992
author: chwncy
assignees: []
labels: []
created_at: '2022-03-25T02:00:10+00:00'
updated_at: '2022-03-25T05:06:41+00:00'
type: issue
status: closed
closed_at: '2022-03-25T05:06:41+00:00'
---

# Original Description

![1](https://user-images.githubusercontent.com/31879464/160039581-1ef37d0b-f7fe-47ee-899a-f82e98b573b6.png)

无法连接到pool.supportxmr.com:3333，但是又能ping得通，其他电脑没有问题，就这个不行，而且显示的log没有颜色，还望大佬帮忙解答一下，谢谢！

# Discussion History
## pdxwebdev | 2022-03-25T02:04:40+00:00
请确认你能够连接到3333端口的服务。Ping可能工作，但3333端口可能被封锁。

## chwncy | 2022-03-25T02:44:06+00:00
> 请确认你能够连接到3333端口的服务。Ping可能工作，但3333端口可能被封锁。

我用telnet测试了一下，只有80端口没有被封，然后我把端口改成80之后，就显示以下错误
![1](https://user-images.githubusercontent.com/31879464/160044329-5e62fb72-9337-4876-a244-8ccda04b9844.png)

## pdxwebdev | 2022-03-25T03:00:33+00:00
尝试使用3333端口进行telnet。XMRig不能解析从监听端口80的应用程序返回的输出。

## chwncy | 2022-03-25T03:35:29+00:00
> 尝试使用3333端口进行telnet。XMRig不能解析从监听端口80的应用程序返回的输出。

感谢，我尝试了其他端口，貌似均无法使用，感觉是运营商已封了该域名的所有端口，已放弃

## pdxwebdev | 2022-03-25T03:47:35+00:00
端口3333对我来说是有效的。我相信问题出在你的网络上。
![Screenshot from 2022-03-24 20-47-13](https://user-images.githubusercontent.com/490176/160050478-8ec1cf5f-5439-467a-ba0b-dde808a1ab32.png)


## chwncy | 2022-03-25T03:53:43+00:00
是的，应该是网络问题，我其他电脑是没有问题的

发自我的iPhone

在 2022年3月25日，11:47，pdxwebdev ***@***.***> 写道：

﻿

端口3333对我来说是有效的。我相信问题出在你的网络上。
[Screenshot from 2022-03-24 20-47-13]<https://user-images.githubusercontent.com/490176/160050478-8ec1cf5f-5439-467a-ba0b-dde808a1ab32.png>

—
Reply to this email directly, view it on GitHub<https://github.com/xmrig/xmrig/issues/2992#issuecomment-1078625266>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AHTHCKE7QIOXBAG6GIZMWXDVBUZOFANCNFSM5RS2FPEA>.
You are receiving this because you authored the thread.Message ID: ***@***.***>


# Action History
- Created by: chwncy | 2022-03-25T02:00:10+00:00
- Closed at: 2022-03-25T05:06:41+00:00
