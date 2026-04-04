---
title: monerod frequently gets stuck syncing
source_url: https://github.com/monero-project/monero/issues/3713
author: ghost
assignees: []
labels: []
created_at: '2018-04-26T19:59:52+00:00'
updated_at: '2018-05-16T10:48:57+00:00'
type: issue
status: closed
closed_at: '2018-05-16T10:48:57+00:00'
---

# Original Description
Every couple of days it seems that monero daemon will stop retrieving new blocks and will be sitting at the same block height until the daemon is restarted.

# Discussion History
## moneromooo-monero | 2018-04-26T22:02:49+00:00
Once this happens, post the output of "sync_info" and "status".
Then set_log 1,net*:DEBUG
Then wait a bit and post the resulting log (fpaste.org or pastebin.mozilla.org or paste.debian.net).

## Onefox | 2018-04-26T22:41:35+00:00
I have the same Problem.
At some point i don't see the yellow block messages anymore after a deamon restart.
![image](https://user-images.githubusercontent.com/1709259/39335114-f4f4f432-49b1-11e8-849f-960e7100e6fa.png)
Here is the set_log output after that:
https://paste.fedoraproject.org/paste/Szh-FyNuY1zVWwNa6v6X9Q


I build master on a oDroid c2 arm, it worked with 0.11.1. os is Ubuntu 16.04.4 LTS
I tried lowering the block-sync-size flag to 10 or 1 this doesn't helped.

## moneromooo-monero | 2018-04-27T14:07:44+00:00
Once this happens, post the output of "sync_info" and "status".
And "diff" too.

## Onefox | 2018-04-27T14:14:15+00:00
@moneromooo-monero  what do you mean with diff?
The sync and status info can be seen on the screenshot right?

## moneromooo-monero | 2018-04-27T14:20:12+00:00
I meant the *output* of diff. But I've seen the screenshot now, and I don't need diff as the screenshot has enough info to answer my question. Do mention when there's a screenshot included, I don't see them so I have to go fish the URL, which I don't if I don't know there's a screenshot somewhere.


## moneromooo-monero | 2018-04-27T14:21:12+00:00
Actually, print_cn would also be helpful to see whch threads are in sync mode.

## Onefox | 2018-04-27T15:50:04+00:00
The other node had to be restaret.
But i have the same problem on a testnode:
here the print_cn:
> 
> print_cn
> Remote Host                   Peer id             Support Flags       Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)
> 
> INC 62.210.104.109:24790      fe74bb70413ebbe0    1                   675176(5)/10919174(5)         state_normal             270                 2           0             39        69
> INC 31.174.56.239:56178       14f02ca5ba6336be    1                   8449(43)/8145580(41)          state_normal             274                 0           0             29        290
> INC 54.38.82.8:54474          00a3043c706759d5    1                   147620(41)/56076(41)          state_normal             416                 0           2             0         0
> INC 183.89.212.241:59479      5ad01cd24433ff32    1                   365521(40)/387040(41)         state_normal             2994                0           0             0         0
> OUT 81.169.162.150:28080      b190ef88ec604c13    1                   2231639(11)/1486779(11)       state_normal             11808               0           0             0         0
> OUT 78.2.110.212:28080        be2e871ebd2d7790    1                   4534476(5)/1496132(5)         state_normal             11813               0           0             0         0
> INC 5.9.100.248:42738         5b4f28fe30cb7479    1                   7459792(2)/918355830(2)       state_normal             11874               0           0             75        104
> INC 118.193.19.166:60040      ef7ab19a70764599    1                   4535786(19)/1516063(19)       state_normal             11881               0           0             0         0
> OUT 212.53.140.36:28080       90a7396f8404834c    1                   4561732(32)/1503792(32)       state_normal             11915               0           2             0         0
> OUT 217.64.127.195:30996      bd0eece0e0b8e9d4    1                   4542993(30)/1423227(30)       state_normal             11915               0           0             0         0
> OUT 114.167.8.26:28080        82cbdd613c42042b    1                   5125600(10)/210593238(10)     state_normal             11713               0           0             17        34
> INC 104.1.221.229:64208       c61bc07ee954ebf8    1                   518595(13)/943483(13)         state_normal             7198                0           0             0         0
> OUT 198.199.122.75:28080      a3a408945b8762d8    1                   4560648(7)/1480831(7)         state_normal             11921               0           0             0         0
> INC 95.156.96.238:63544       ae103be4916dafd7    1                   415462(4)/63936952(4)         state_normal             2505                0           0             24        35
> OUT 5.9.150.112:28080         985ec51ddba0956f    1                   4538602(41)/1480004(41)       state_normal             11926               0           2             0         0
> OUT 42.98.225.123:28080       8335a45139206c22    1                   1210317(40)/1499963(41)       state_normal             11927               0           0             0         0
> 
![image](https://user-images.githubusercontent.com/1709259/39371593-6eb4d9f0-4a42-11e8-8e88-3561957ff1b8.png)
Here the sync_info:

> sync_info
> Height: 1090169, target: 1090666 (99.9544%)
> Downloading at 6 kB/s
> 17 peers
> 62.210.104.109:24790      fe74bb70413ebbe0  1090670  0 kB/s, 0 blocks / 0 MB queued
> 31.174.56.239:56178       14f02ca5ba6336be  832822  0 kB/s, 0 blocks / 0 MB queued
> 54.38.82.8:54474          00a3043c706759d5  1090169  0 kB/s, 0 blocks / 0 MB queued
> 183.89.212.241:59479      5ad01cd24433ff32  1090169  0 kB/s, 0 blocks / 0 MB queued
> 81.169.162.150:28080      b190ef88ec604c13  1090169  0 kB/s, 0 blocks / 0 MB queued
> 78.2.110.212:28080        be2e871ebd2d7790  1090169  0 kB/s, 0 blocks / 0 MB queued
> 5.9.100.248:42738         5b4f28fe30cb7479  1066771  0 kB/s, 0 blocks / 0 MB queued
> 96.248.81.93:55028        bb27eeefc7e93fca  1090166  0 kB/s, 0 blocks / 0 MB queued
> 118.193.19.166:60040      ef7ab19a70764599  1090169  0 kB/s, 0 blocks / 0 MB queued
> 212.53.140.36:28080       90a7396f8404834c  1090169  2 kB/s, 0 blocks / 0 MB queued
> 217.64.127.195:30996      bd0eece0e0b8e9d4  1090169  2 kB/s, 0 blocks / 0 MB queued
> 114.167.8.26:28080        82cbdd613c42042b  1057047  0 kB/s, 0 blocks / 0 MB queued
> 104.1.221.229:64208       c61bc07ee954ebf8  1090169  0 kB/s, 0 blocks / 0 MB queued
> 198.199.122.75:28080      a3a408945b8762d8  1090169  0 kB/s, 0 blocks / 0 MB queued
> 95.156.96.238:63544       ae103be4916dafd7  159792  0 kB/s, 0 blocks / 0 MB queued
> 5.9.150.112:28080         985ec51ddba0956f  1090169  2 kB/s, 0 blocks / 0 MB queued
> 42.98.225.123:28080       8335a45139206c22  1090169  0 kB/s, 0 blocks / 0 MB queued
> 0 spans, 0 MB
> 


status
Height: 1090169/1090666 (99.9%) on testnet, not mining, net hash 503 H/s, v8, up to date, 8(out)+8(in) connections, uptime 0d 3h 21m 42s

And here a log again:
https://paste.fedoraproject.org/paste/TnlowG7keP-a26oz4vij3A




## moneromooo-monero | 2018-04-27T17:28:11+00:00
And the diff output ?

## moneromooo-monero | 2018-04-27T17:29:55+00:00
Also I don't suppose to have a log of what that happened ?

## moneromooo-monero | 2018-04-27T18:36:46+00:00
This patch might help. Check for "Sync seems wedged, restarting" messages in the log, followed by sync restarting. It checks for 2 blocks, you may want to set this to, say, 10 for testing to make sure it's really wedged before this kicks in.

https://github.com/moneromooo-monero/bitmonero/tree/wrec

## ghost | 2018-04-28T18:10:15+00:00
https://paste.fedoraproject.org/paste/xP1NpedrQLnyTj98iuHfMA/raw

## moneromooo-monero | 2018-04-28T18:35:38+00:00
That one is likely fixed by https://github.com/monero-project/monero/pull/3719

## Onefox | 2018-04-29T13:20:42+00:00
I am on the wrec branch from your repo now, same problem here is the output:

here is the debug log:
https://paste.fedoraproject.org/paste/9H9RNr~qaeOjATTu26ObnQ

> print_cn:
> 
> PoW:    <0191fd03adafd864e60fb2848835b1b642ae8503b21f155930149b05aeb90100>
> difficulty:     25283
> 
> Remote Host                   Peer id             Support Flags       Recv/Sent (inactive,sec)      State                    Livetime(sec)       Down (kB/s) Down(now)     Up (kB/s) Up(now)
> 
> OUT 5.9.150.112:28080         985ec51ddba0956f    1                   268804(5)/88284(5)            state_normal             600                 0           2             0         0
> INC 89.27.78.102:35232        6cacf90fa989d31a    1                   230060(19)/11442857(5)        state_normal             1961                0           0             5         0
> INC 62.210.104.109:18044      fe74bb70413ebbe0    1                   4535692(1)/139309522(1)       state_synchronizing      6529                0           0             20        34
> INC 88.207.44.98:48796        be7b218ed61736df    1                   1020660(5)/1064949(5)         state_normal             7570                0           0             0         0
> INC 204.68.122.18:45650       a98264ab21275253    1                   1899304(8)/24719810(5)        state_normal             7713                0           0             3         3
> OUT 118.193.19.166:28080      ef7ab19a70764599    1                   4803263(1)/1726219(1)         state_normal             13019               0           2             0         0
> OUT 87.121.103.239:28080      e6deba72b975b1af    1                   750676(2)/89333743(2)         state_normal             3525                0           0             24        35
> OUT 42.98.225.123:28080       2ff5b2aefb7c6ce9    1                   1867107(4)/2167511(5)         state_normal             16392               0           0             0         0
> INC 78.2.107.57:47574         be2e871ebd2d7790    1                   4510491(5)/1659495(5)         state_normal             12337               0           2             0         0
> OUT 198.199.122.75:28080      a3a408945b8762d8    1                   6029999(4)/2167879(5)         state_normal             16350               0           2             0         0
> OUT 88.99.6.12:28080          f3e4933bc274da78    1                   6408081(5)/2235797(5)         state_normal             16769               0           2             0         0
> OUT 54.89.64.183:28080        0b8dd5e29751fb62    1                   2719297(20)/55332378(5)       state_normal             16396               0           0             3         0
> INC 5.9.100.248:51182         5b4f28fe30cb7479    1                   4938460(2)/690405313(2)       state_normal             7456                0           2             90        104
> INC 78.13.232.46:50747        2ba527af123621ac    1                   1850292(0)/23722658(2)        state_normal             6281                0           0             3         3
> OUT 54.38.82.8:28083          00a3043c706759d5    1                   6142150(5)/2193616(5)         state_normal             16769               0           2             0         0
> 


> status
> Height: 1091343/1092032 (99.9%) on testnet, not mining, net hash 426 H/s, v8, up to date, 8(out)+7(in) connections, uptime 0d 4h 37m 46s
> diff
> BH: 1091343, TH: d686366bcce0b1fb382d9d66c13fed1efa13a3f2141bca172ca2769e0dffbd06, DIFF: 51199, HR: 426 H/s
> sync_info
> Height: 1091343, target: 1092032 (99.9369%)
> Downloading at 7 kB/s
> 15 peers
> 5.9.150.112:28080         985ec51ddba0956f  1091343  2 kB/s, 0 blocks / 0 MB queued
> 89.27.78.102:35232        6cacf90fa989d31a  84095  0 kB/s, 0 blocks / 0 MB queued
> 62.210.104.109:18044      fe74bb70413ebbe0  1092032  0 kB/s, 0 blocks / 0 MB queued
> 88.207.44.98:48796        be7b218ed61736df  1091343  0 kB/s, 0 blocks / 0 MB queued
> 204.68.122.18:45650       a98264ab21275253  61398  0 kB/s, 0 blocks / 0 MB queued
> 118.193.19.166:28080      ef7ab19a70764599  1091343  2 kB/s, 0 blocks / 0 MB queued
> 87.121.103.239:28080      e6deba72b975b1af  1053709  0 kB/s, 0 blocks / 0 MB queued
> 42.98.225.123:28080       2ff5b2aefb7c6ce9  1091343  0 kB/s, 0 blocks / 0 MB queued
> 78.2.107.57:47574         be2e871ebd2d7790  1091343  2 kB/s, 0 blocks / 0 MB queued
> 198.199.122.75:28080      a3a408945b8762d8  1091343  0 kB/s, 0 blocks / 0 MB queued
> 88.99.6.12:28080          f3e4933bc274da78  1091343  0 kB/s, 0 blocks / 0 MB queued
> 54.89.64.183:28080        0b8dd5e29751fb62  750427  1 kB/s, 0 blocks / 0 MB queued
> 5.9.100.248:51182         5b4f28fe30cb7479  1066771  0 kB/s, 0 blocks / 0 MB queued
> 78.13.232.46:50747        2ba527af123621ac  56197  0 kB/s, 0 blocks / 0 MB queued
> 54.38.82.8:28083          00a3043c706759d5  1091343  0 kB/s, 0 blocks / 0 MB queued
> 1 spans, 0 MB
> 62.210.104.109:18044      20 (1091654 - 1091673)  -
> 

## moneromooo-monero | 2018-04-29T16:02:34+00:00
It doesn't seem stuck here.

## Onefox | 2018-04-29T18:45:44+00:00
mmh, now got the last blocks again and is back on 100% sync, I keep looking ;)

## moneromooo-monero | 2018-04-29T19:25:25+00:00
Did you get a log with "wedged" in ?

## Onefox | 2018-05-01T12:11:33+00:00
Here are the new logs, with many wedged logs.
https://paste.fedoraproject.org/paste/8yNGZEwnMzzwnY9aJY7xvA

There are also the sync_info status diff and print_cn in the bottom.

The daemon is now up to date. 

## moneromooo-monero | 2018-05-01T14:43:46+00:00
It seems like the wedged detection triggers on the "bad" chains. Unfortunate. But stoffu fixed what is probably the (or one of the) root cause in https://github.com/monero-project/monero/pull/3723

## Onefox | 2018-05-01T20:50:59+00:00
It still looks like I am up to date but still the wedged output is printed.
See attached screenshot.

![image](https://user-images.githubusercontent.com/1709259/39493118-f95579a0-4d91-11e8-8bcc-eb246e158423.png)


## iDunk5400 | 2018-05-02T22:24:21+00:00
It doesn't seem to be wedged there. It is just seeing a longer forked chain with lower cumulative difficulty. Someone started mining on testnet and got forked very early on after v7 or v8 hardforks, and now they are mining on their own chain. Don't let that forked chain confuse you, although it does produce massive amounts of alternative blocks.

## Onefox | 2018-05-02T23:11:34+00:00
The problem is while the daemon is showing "not sync", i cant use it with a wallet.... 
Is there any way around it?

## moneromooo-monero | 2018-05-03T08:22:27+00:00
Does it not become synced once it's discarded that branch ?

## Onefox | 2018-05-03T08:25:31+00:00
no its still in the stage since yesterday...
Height: 1094030/1094721 (99.9%) on testnet, not mining, net hash 409 H/s, v8, up to date, 8(out)+10(in) connections, uptime 2d 6h 6m 37s

## moneromooo-monero | 2018-05-04T10:50:51+00:00
And you definitely have stoffu's fix ?

## Onefox | 2018-05-06T16:32:25+00:00
after more testing this problem doesn't occurred anymore.
This could be closed

## moneromooo-monero | 2018-05-07T18:38:13+00:00
https://github.com/monero-project/monero/pull/3775 fixes a second sync failure problem.

## moneromooo-monero | 2018-05-08T20:00:58+00:00
And http://paste.debian.net/hidden/f8496e47/ fixes a third one.

## jwm1969 | 2018-05-11T14:10:28+00:00
I have this same issue every couple days; should we pull and compile master or the v12 tag?

## moneromooo-monero | 2018-05-11T17:36:55+00:00
None of the above. Use release-0.12.

## moneromooo-monero | 2018-05-16T10:26:41+00:00
All known sync bugs are now fixed and merged.

+resolved

# Action History
- Created by: ghost | 2018-04-26T19:59:52+00:00
- Closed at: 2018-05-16T10:48:57+00:00
