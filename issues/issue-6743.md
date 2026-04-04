---
title: xmr节点生成新的地址耗时5分钟
source_url: https://github.com/monero-project/monero/issues/6743
author: yzn5555
assignees: []
labels: []
created_at: '2020-08-05T09:13:40+00:00'
updated_at: '2022-02-19T04:18:33+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:18:33+00:00'
---

# Original Description
节点进入命令行执行address new 执行结果耗时较长，
服务是：4核 16G
但是在执行生成地址操作的时候发现cpu使用率在单核100%，总使用率最高25%，想问下服务器多个有使用多核的办法吗？


# Discussion History
## ghost | 2020-08-05T11:09:21+00:00
对于我来说，生成地址功能几乎是瞬间完成的，几乎不占用CPU。
服务器多个什么意思？多个核心吗？你如果没有手工设置  --max-concurrency ，钱包应该默认CPU多线程并行计算。

你用的什么操作系统还有确定CLI钱包占用的CPU？
 
 




## yzn5555 | 2020-08-05T12:07:46+00:00
我是用的是ubuntu1.18版本的 
操作步骤：1、使用monero-wallet-cli进入命令行    2、在命令行执行address new     执行完这个服务器cpu会突然暴增，但是4核服务器cpu使用率达到25%就无法增高了，通过top命令查看程序cpu使用率发现
![企业微信截图_15966181312171](https://user-images.githubusercontent.com/36029121/89411033-510aa480-d757-11ea-8941-17be16e8e98a.png)




# Action History
- Created by: yzn5555 | 2020-08-05T09:13:40+00:00
- Closed at: 2022-02-19T04:18:33+00:00
