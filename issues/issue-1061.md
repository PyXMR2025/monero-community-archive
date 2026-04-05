---
title: 跟着一个病毒脚本来的这里了。。。
source_url: https://github.com/xmrig/xmrig/issues/1061
author: axzsd
assignees: []
labels:
- invalid
- av
created_at: '2019-07-16T02:10:38+00:00'
updated_at: '2025-06-16T05:30:13+00:00'
type: issue
status: closed
closed_at: '2019-07-20T16:36:37+00:00'
---

# Original Description
跟着一个病毒脚本来的这里了....

# Discussion History
## douyaolai | 2019-07-25T01:38:35+00:00
请问最后怎么处理的 ？

## axzsd | 2019-07-25T01:51:42+00:00
我的是 maven 仓库有漏洞，然后被入侵了，你看看是不是这个问题（https://blog.csdn.net/xstardust/article/details/88534938），杀掉可疑的进程，然后删除可疑的脚本。看到任务计划表里面有没得特殊的任务，有就关掉。然后补漏洞，如果是nexus oss的问题，那就升级

## douyaolai | 2019-07-25T03:04:57+00:00
![win-miner](https://user-images.githubusercontent.com/21256502/61842743-d95f3400-aecb-11e9-87d4-236312ac5416.png)

我这边的情况是，这个 xmrig 伪装成 system 进程，使用软件清除的时候，过后又出现。

## thisisvoa | 2019-12-12T09:13:17+00:00
我的14台服务器都中了这个病毒，现在是保守治疗，起来就杀一次，狗头

## axzsd | 2019-12-12T09:20:15+00:00
> 我的14台服务器都中了这个病毒，现在是保守治疗，起来就杀一次，狗头

我的服务器，这个脚本没有启动上来，被阿里云给拦截了

## liu-congcong | 2024-05-25T11:32:15+00:00
2024年，也中招了。
首先“感谢”作者开发了“xmrig”。
请作者闭源，增加相关的运行提示，以便于不了解xmrig的人可以更加容易发现他在运行。
木马的作者甚至修改了我的top、ls等等。

## CHINEONE | 2025-06-16T05:30:13+00:00
中了 腾讯管家杀死，等后续重新启用？

# Action History
- Created by: axzsd | 2019-07-16T02:10:38+00:00
- Closed at: 2019-07-20T16:36:37+00:00
