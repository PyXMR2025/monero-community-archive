---
title: 'C: is full how can I change it to another path?'
source_url: https://github.com/monero-project/monero/issues/2951
author: evil7
assignees: []
labels: []
created_at: '2017-12-18T00:42:00+00:00'
updated_at: '2017-12-18T05:32:55+00:00'
type: issue
status: closed
closed_at: '2017-12-18T05:00:35+00:00'
---

# Original Description
Thanks for this great object first.
I have 2 little problem here:
1. I running wallert-GUI on `win10 x64` when `monerod-wallert-gui.exe` when APP starting. It will auto set db file saved in path `C:\ProgramData\bitmonero`. No bad happened for running but now is the problem: My `C:\` is almost full now. How can I change to setting db's saving to another path? Or move it to other place?
1. At my macbook I used it with GUI but it not running well. It the `APP No Response` happened usual and I can only kill the pid and restart it. the bin file all in the APP can running well by used alone (I try used monero-cli and used bin file what inside APP that's all OK). How can I change GUI APP's config-file loading when APP start? Or some way to fix the APP's `fake died` problem?
I'll waiting for your answer and thx.

# Discussion History
## stoffu | 2017-12-18T04:21:19+00:00
First of all, GUI related questions should be addressed to the relevant repository: https://github.com/monero-project/monero-gui

For the point 1, you can move the entire bitmonero directory to an external disk etc, and specify a daemon flag `--data-dir=path/to/bitmonero` in the settings page before launching the daemon.

Not sure about the point 2.

## evil7 | 2017-12-18T04:31:41+00:00
Thx a lot. By the way an other one question. how can I change the daemon's listening from `127.0.0.1:18081` to `0.0.0.0:18081`. I want to change it server for my team or other people not just me at localhost. Same api or flag in setting? thank you again.

## evil7 | 2017-12-18T04:57:33+00:00
Thanks for your answer. I found the way fix next question. In log info:
```
2017-12-18 04:48:22.167 16356   INFO    global  contrib/epee/include/net/http_server_impl_base.h:70  Binding on 127.0.0.1:18081
2017-12-18 04:48:22.169 16356   INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-12-18 04:48:22.170 16356   INFO    global  src/daemon/core.h:73    Initializing core...
```
I'll try change the host from codes and re-make it. ✍️ 

## evil7 | 2017-12-18T05:00:34+00:00
Problems fixed. All clear.
thanks for your support.
Closed now.

## stoffu | 2017-12-18T05:28:24+00:00
You don't need to re-make it, you can use `--rpc-bind-ip 0.0.0.0` to allow external computers to access the daemon RPC. Note however that for security reasons you need to either configure the RPC login info via `--rpc-login username[:password]` or specify `--confirm-external-bind` so that no login is needed.

## evil7 | 2017-12-18T05:32:55+00:00
OK. I just will use it for my team now. thank you. XD

# Action History
- Created by: evil7 | 2017-12-18T00:42:00+00:00
- Closed at: 2017-12-18T05:00:35+00:00
