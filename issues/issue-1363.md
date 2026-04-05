---
title: v5.1.0 Linux "nice" command doesn't work.
source_url: https://github.com/xmrig/xmrig/issues/1363
author: DM168168
assignees: []
labels:
- bug
created_at: '2019-12-02T01:15:13+00:00'
updated_at: '2019-12-04T10:33:42+00:00'
type: issue
status: closed
closed_at: '2019-12-04T10:33:42+00:00'
---

# Original Description
Hi 
The V5.1.0 is pretty good for RandomX, but I could not use "nice" command to control process priority anymore when I upgrade to V5.1.0.
Please help me to figure out this problem.

※The V5.0.1 & V5.0.0 is workable about "nice" command.
![not_work](https://user-images.githubusercontent.com/40748523/69924047-360ad500-14e4-11ea-8127-5c9a2bd7a35a.jpg)
![workable](https://user-images.githubusercontent.com/40748523/69924048-360ad500-14e4-11ea-9911-5c41f378f2e9.jpg)



# Discussion History
## xmrig | 2019-12-02T01:45:32+00:00
Actually it strange nothing related to this changed, I just checked and `nice -n 19` works fine. Also there option `"priority": 0,` in `cpu` object, it works like `nice -n 19` for mining threads, but not change  niceness of main thread.
Thank you.

## DM168168 | 2019-12-02T02:54:34+00:00
Hi Sir
Thanks for your quickly reponse.
I have tried the option " priority": 0, but top command show nice values are "-15".
Do you have any recommendations? I would like to nice value is "-19" show on top command.

![nice_issue2](https://user-images.githubusercontent.com/40748523/69927252-5a6dae00-14f2-11ea-9bde-51eef24d6a71.jpg)
![nice_issue](https://user-images.githubusercontent.com/40748523/69927339-a02a7680-14f2-11ea-9cc5-0c3173776c25.jpg)



## xmrig | 2019-12-03T11:32:21+00:00
Fixed in dev branch, if priority not set in config `"priority": null,` miner not will not change any priority by self.
If priority set in config main miner thread will always use higher priority than mining threads.
Thank you.

## xmrig | 2019-12-04T10:33:42+00:00
Fix included into v5.1.1 release https://github.com/xmrig/xmrig/releases/tag/v5.1.1
Thank you.

# Action History
- Created by: DM168168 | 2019-12-02T01:15:13+00:00
- Closed at: 2019-12-04T10:33:42+00:00
