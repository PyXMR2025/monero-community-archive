---
title: What will be git clone for ubuntu
source_url: https://github.com/xmrig/xmrig/issues/1081
author: looplife55
assignees: []
labels:
- question
created_at: '2019-07-29T05:58:07+00:00'
updated_at: '2019-07-29T17:54:02+00:00'
type: issue
status: closed
closed_at: '2019-07-29T17:54:02+00:00'
---

# Original Description
I am try to install new update for wownero/wow by xmrig but it not showing 
Error which i am getting will cloning::
git clone https://github.com/xmrig/xmrig/releases/tag/v2.99.1-beta
Cloning into 'v2.99.1-beta'...
Cloning: command not found
root@jusval-3:~# fatal: https://github.com/xmrig/xmrig/releases/tag/v2.99.1-beta/info/refs not valid: is this a git repository?
fatal:: command not found

# Discussion History
## xmrig | 2019-07-29T06:06:34+00:00
Use:
`git clone https://github.com/xmrig/xmrig.git`
`git checkout beta`

In future if you already on beta branch, just `git pull`.
Thank you.

## looplife55 | 2019-07-29T06:16:31+00:00
BY using
git clone https://github.com/xmrig/xmrig.git
It cloning only old version. 
Plz bro guide me To mine wownero using your miner from 2 month i am mine monero.now i want to switch  to wownero(random/wow)
Btw, i never change donation level always giving 5% of my share. 😊

## xmrig | 2019-07-29T06:24:55+00:00
Second command `git checkout beta` do the thing.

## looplife55 | 2019-07-29T06:42:34+00:00
root@jusval-3:~# cd xmrig
root@jusval-3:~/xmrig# cd build
root@jusval-3:~/xmrig/build# git checkout beta
Already on 'beta'
Your branch is up to date with 'origin/beta'.
root@jusval-3:~/xmrig/build# ./xmrig -o loki.pool.mine2gether.com:3331 -u LCfrezxEYq1HHPj4tpinrqVCLMCMg2n4rfVQmsam5U3wWwrCX3eKEHAUM2phDhpgQqdGY8Jbuut11D6u6DUt5mXPQzCwGA7 -a rx/loki -k
unable to open "/root/xmrig/build/config.json".
No valid configuration found. Exiting.
root@jusval-3:~/xmrig/build#

## looplife55 | 2019-07-29T07:45:45+00:00
Waiting for reply want to setup my rig

## looplife55 | 2019-07-29T08:42:24+00:00
root@jusval-3:~/xmrig# git checkout beta
error: Your local changes to the following files would be overwritten by checkout:
        src/config.json
Please commit your changes or stash them before you switch branches.
Aborting
root@jusval-3:~/xmrig#

## looplife55 | 2019-07-29T13:41:15+00:00
Any method to updated xmrig to random/wow version in ubuntu wait for your answer 

## xmrig | 2019-07-29T14:18:00+00:00
git contains only source, you need make a binary from it via `cmake` and `make` as usual.

## looplife55 | 2019-07-29T17:53:58+00:00
Yup!! Solve

# Action History
- Created by: looplife55 | 2019-07-29T05:58:07+00:00
- Closed at: 2019-07-29T17:54:02+00:00
