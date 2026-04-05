---
title: 各位大佬，这个 xmrig 怎样 在 android 下编译？
source_url: https://github.com/xmrig/xmrig/issues/1963
author: kungsoft
assignees: []
labels: []
created_at: '2020-12-03T15:35:53+00:00'
updated_at: '2021-04-12T14:33:35+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:33:35+00:00'
---

# Original Description
有国内的 挖矿爱好者吗？ kungsoft@qq.com 
Q我一下

# Discussion History
## kungsoft | 2020-12-05T07:13:05+00:00
没人回应，呜呜~

## FrankHB | 2020-12-21T09:50:08+00:00
Termux 下 proot 装个包够用的发行版。Arch Linux ARM 无压力。

## XZiar | 2021-01-03T02:49:46+00:00
termux下可以直接编译。
https://xmrig.com/docs/miner/build/ubuntu
按advanced build来。
不过安卓下libuv编译有点问题，`./build_deps.sh`完成后要单独去libuv目录下用cmake再编译一次，然后把生成的libuv_a.a替换script/deps/lib下的libuv.a。


# Action History
- Created by: kungsoft | 2020-12-03T15:35:53+00:00
- Closed at: 2021-04-12T14:33:35+00:00
