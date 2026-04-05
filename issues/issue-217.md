---
title: 'DNS error: "unknown node or service"'
source_url: https://github.com/xmrig/xmrig/issues/217
author: fogoat
assignees:
- xmrig
labels:
- enhancement
created_at: '2017-11-23T04:54:44+00:00'
updated_at: '2022-01-03T13:05:10+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:56:50+00:00'
---

# Original Description
Ran into this error after I power cycled my router. Is there a way for xmrig to recover more gracefully when there is a DNS error?

```
[2017-11-22 20:01:22] speed 2.5s/60s/15m n/a n/a 151.0 H/s max: 152.7 H/s
[2017-11-22 20:01:25] [pool.xxxx.com:3333] DNS error: "unknown node or service"
[2017-11-22 20:01:31] [pool.xxxx.com:3333] DNS error: "unknown node or service"
[2017-11-22 20:01:36] [pool.xxxx.com:3333] DNS error: "unknown node or service"
```

# Discussion History
## gennadicho | 2017-11-23T10:24:13+00:00
Soo. May you write ip and domain into /etc/hosts directly? But is a dumb way. Just try to set up normal DNS-server on your router. Or you talking about xmrig not accepted dns-record on-the-air while it change?

## xmrig | 2017-11-23T14:41:14+00:00
Yep, unclear issue, something wrong with router? or the miner.
Need more details what DNS server used, buildin in router or some externals and other network tools is working or not, eg ping.

Also possible add feature to cache last successful ip address set and reuse it if get DNS errors.
Thank you.

## fogoat | 2017-11-27T17:28:47+00:00
Yes, I could put a hosts entry. It'd be nice if DNS fails, xmrig tries to renegotiate address again. I have wireless connection to router if it matters. DNS I use is whatever the router provides and not direct to a public DNS like 8.8.8.8 (Google Public DNS).

## fogoat | 2018-03-15T02:28:12+00:00
So any update to this? Will xmrig renegotiate connection again? I prefer your product over xmr-stak and donate 1% 

## xmrig | 2018-03-15T03:35:34+00:00
Probably will be added to v2.6.
Thank you.

## lucasff | 2019-12-14T13:30:04+00:00
I'm having this problem now :(

## CistelicanCatalin | 2020-07-02T08:16:28+00:00
Same problem

## HankFit247 | 2020-09-17T06:11:19+00:00
Starting to have this same issue on one of my miners, Windows 10 Pro XMRig v6.3.3.  

Happens after about 4-6 hours of mining.  Need to pay attention to the logs to get a better idea...

Changes I have made so far:
- I have both Google DNS Servers programmed into my miners IP Stack.  After a couple of days, I added my ISP (Comcast) to the stack for a total of 4 now.
- Better, not creating the DNS Error as often.  I was away at work for over 9 Hours today, and was still up and running.  Then about an hour later I got it.

- I just changed my DNS in my Router from "Get from ISP" to specifying them directly.

Network:
Netgear CAX80
Comcast over 300MB down

**Update:**  
Been running 24+ hours now without issue after adding the tertiary DNS entry in my router.  
I'm aware that most routers don't include this option.

## HankFit247 | 2020-09-20T22:07:09+00:00
Unfortuneatly this issue has returned.

SpeedTest.net to the RESCUE!!!
Downloaded "TCP Optimizer 4"
Run as Administrator

It recommended a number of changes to my IP Stack.
Reboot for changes to take effect.

https://www.speedguide.net/downloads.php

I saw a HUGE Improvement in Internet Threads even before the reboot!!!!


## HankFit247 | 2020-09-28T03:16:11+00:00
Issue has returned.  :(
v6.3.3

## HankFit247 | 2020-10-09T02:39:38+00:00
I found that Betterhash, which was also mining XMR via CPU on two of my Windows 10 Pro rigs was causing the issue.

Removed BETTER_TRASH lol, issue resolved!

## jishnunand | 2021-07-04T03:39:06+00:00
I am having this issue again :(

## pedroplanet | 2022-01-03T02:30:53+00:00
The same here,    xmrpool.eu:443 DNS error: "unknown node or service"
tried all the ports 3333 9999 etc

## SChernykh | 2022-01-03T09:52:15+00:00
> The same here, xmrpool.eu:443 DNS error: "unknown node or service" tried all the ports 3333 9999 etc

Try different DNS server (8.8.8.8 and 8.8.4.4 for example). Your ISP is most likely blocking xmrpool.eu.

## HankFit247 | 2022-01-03T13:02:50+00:00
Run as Administrator

## pedroplanet | 2022-01-03T13:05:10+00:00
> > The same here, xmrpool.eu:443 DNS error: "unknown node or service" tried all the ports 3333 9999 etc
> 
> Try different DNS server (8.8.8.8 and 8.8.4.4 for example). Your ISP is most likely blocking xmrpool.eu.

Yes, my ISP is blocking xmrpool. I've changed the DNS sever on the ISP router, now the blocked sites work on my browsers, but xmrig is still giving error.

# Action History
- Created by: fogoat | 2017-11-23T04:54:44+00:00
- Closed at: 2021-04-12T15:56:50+00:00
