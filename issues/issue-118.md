---
title: '"No active pools, stop mining" and other strange things'
source_url: https://github.com/xmrig/xmrig/issues/118
author: ght3d
assignees: []
labels: []
created_at: '2017-09-19T14:40:26+00:00'
updated_at: '2020-07-15T13:20:43+00:00'
type: issue
status: closed
closed_at: '2017-09-29T08:51:40+00:00'
---

# Original Description
Hey there, dear developer. 

A big fan of your miner here, pretty much the fastest and simplest to set up i've found for monero. 

The issue is that 1 day ago, suddenly xmrig started displaying the "No active pools, stop mining", the overall hashrate of the farm divided by 3 and slowed down, a lot of jobs were being accepted constantly, but only 2, sometimes 3 found shares where accepted by the pool. Then share accepting messages just stop appearing.  
Also "Connection reset by peer" started appearing, but nothing in my network configuration changed since i started mining. For 20 days straight, not a single invalid share, no errors, nothing, and now this.

I also tried to reroute all farms to and Xmrig-proxy installed on one of the machines in the same network. Errors are pretty much the same, no matter what pool is use or what xmrig flags i set, you can see them in the screenshots i provided.  

The other thing i did, to make sure it's not a network problem, is to install a 4g connection to the computer instead of using internet provided by the LAN. Same story on a 4g connection. First i thought the pool banned me for making a bunch of connections from  30 computers, but it's the same errors on all pools.

Tried to solve it by myself and last thing i wanted is to bother the developer with my noob problems.

Thank you for this wonderful miner!

![screenshot_1](https://user-images.githubusercontent.com/32014118/30598095-9361bc5c-9d61-11e7-8d79-47f1b66f572f.png)
![screenshot_2](https://user-images.githubusercontent.com/32014118/30598094-935ae864-9d61-11e7-9312-b3a164f9f5a5.jpg)
![screenshot_3](https://user-images.githubusercontent.com/32014118/30598096-93631c3c-9d61-11e7-86fc-660fdb2360fc.png)

# Discussion History
## ght3d | 2017-09-20T07:02:11+00:00
![screenshot_4](https://user-images.githubusercontent.com/32014118/30630749-8cfadc98-9dea-11e7-8af7-a387b30a4a5f.jpg)
Mined all night and had some other errors. The shares are being accepted but at an incredibly slow rate (only 125 for a whole night, which wasn't the case before). 

## ght3d | 2017-09-20T08:57:42+00:00
When trying to mine aeon it gives me this. A lot of people had same problem on forum with different mining software, but no explanation or solution was found:

![screenshot_1](https://user-images.githubusercontent.com/32014118/30635373-e40b6e70-9dfa-11e7-9fc7-5df5a1e7ea3e.jpg)


## LeozMaralz | 2017-09-20T17:29:22+00:00
> When trying to mine aeon it gives me this. A lot of people had same problem on forum with different mining software, but no explanation or solution was found

@ght3d Remove **stratum+tcp://** from the pool address and all should be fine.

## ght3d | 2017-09-20T20:03:02+00:00
@LeozMaralz same story with or without stratum+tcp:// . But thanks for suggestions

## calvintam236 | 2017-09-21T07:20:07+00:00
You are getting timed out. Looks like the pool is too far from your location (It's 500-1000ms in the screenshot). Try to lower the response time by using different region server/pool. Normally, I think it should less than 250ms.

## ght3d | 2017-09-21T08:09:59+00:00
@calvintam236 Didn't have the error for a month and ping couldn't suddenly change, connection settings stayed the same, also tried on a faster 4g connection and errors reproduced again. The errors appear on any pool, from any country, even if the ping is less than 100 ms. 

## calvintam236 | 2017-09-21T08:20:31+00:00
@ght3d Can you list out your OS, hardware spec, and `xmrig` version? Did you install/update any software on the rig recently?

## ght3d | 2017-09-21T08:45:50+00:00
@calvintam236 Double Xeon E5-2650 renderblades with 40mb L3 cache with Windows Server 2012 and a couple of single Xeon X5690 workstations with Windows 7. Latest XmRig 2.3.1 and no hardware/software changes in the last week whatsoever. Only one workstation got a new graphics card which i used successfully for mining for a week or so, but it's irrelevant as it doesn't affect other machines. All machines have the same issue, no matter their specs. In total there are 30 machines, all mining to the same wallet simultaneously. Tried Xmrig proxy and there are still timeout errors, machines keep connecting/disconnecting, share rate became pretty pathetic, almost a quarter of what it was before. 

## eXellenz | 2017-09-29T06:28:27+00:00
confirm. i have same problem.
thx 4 nice miner & nh support by gpu miner.
![cpu_i7](https://user-images.githubusercontent.com/32382806/31003439-c34509f0-a500-11e7-9f79-4f8902bfa059.jpg)


## ght3d | 2017-09-29T08:51:40+00:00
Well, after researching the problem for a week, and testing miners and network configurations, i found out that the network config was actually changed by the system admin. In order to protect the network from ddos attacks, the admin turned off any kind of DNS requests and the ICMP protocol which allows you to ping a machine. The miners couldn't ping servers because of this, so i made a http and socks5 proxy on a specific machine which reroutes traffic around the firewall. All the connection errors from the first screenshot dissapeared. I used XmrigProxy on said machine and sent all miners to this machine's address. Works great!

 For the other half of my farm i had to use another old miner , optimized for old machines which do not have the AES-NI instructions set and xmrig yields 10 times less speed on them then the old miner. Hopefully that miner had the option to set a proxy in the .bat file directly like "miner.exe -x http://proxy-address -o stratum+tcp://pool-address -u user -x password. These old miners, which do not use xmrig and xmrigproxy, mine directly to the pool through http proxy , but on the same wallet.  

Too bad that Xmrig doesn't support direct http proxies yet. 

@eXellenz - Work is accepted correctly, there are no connection issues or errors, you can easily ignore the "no active pools" error in your case. 

## joaopaulo164 | 2019-04-14T02:44:48+00:00
which old miner did you use? @ght3d 

## Spudz76 | 2019-04-15T16:54:02+00:00
Also high diff and low hashrate, some pools will hangup on you for no results in 90s or whatever.
You should be running a vardiff proxy to subdivide the enormous difficulty for your slow miners.

## jacksonkr | 2020-07-15T13:20:42+00:00
I noticed that one of my miners was not reporting and after looking into it I saw "No active pools, stop mining" in the terminal. While investigating what was going on the miner had reconnected itself and showed up as an active miner again on my supportxmr.com dashboard.

# Action History
- Created by: ght3d | 2017-09-19T14:40:26+00:00
- Closed at: 2017-09-29T08:51:40+00:00
