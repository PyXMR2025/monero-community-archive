---
title: Tons of connections, monerod ignoring the cap
source_url: https://github.com/monero-project/monero/issues/8367
author: asheroto
assignees: []
labels: []
created_at: '2022-05-31T15:08:08+00:00'
updated_at: '2022-06-19T01:11:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,

As of the current version, 0.17.3.2, for some reason monerod is allowing way too many connections to port 18080. There were 118 connections before my server stopped responding to json_rpc requests. I have a cap set at 25 but for some reason monerod doesn't comply with it anymore. The previous version didn't have this issue, the only thing I've changed is the version number (the binary) with the latest.

Running on Debian 10

Thanks

# Discussion History
## selsta | 2022-05-31T15:10:30+00:00
What cap did you set at 25?

Also are these connections on port 18080 (P2P) or 18081 (RPC)? Is your port 18081 open?

## asheroto | 2022-05-31T17:35:57+00:00
```
out-peers=25
in-peers=25
```

18080 is the port with a ton of connections (P2P)

I have port 18089 open for RPC

## selsta | 2022-05-31T17:43:01+00:00
From what I can tell there is nothing relevant to your issue changed between v0.17.3.0 and v0.17.3.2. Maybe you simply didn't look for it with the old version?

Regarding json rpc being unresponsive, that is a separate issue that is related to SSL.

You can either set --rpc-ssl to disabled or you can compile with #7760

## asheroto | 2022-05-31T17:48:11+00:00
I UptimeRobot.com to monitor my server. It's basically an HTTP monitor that checks for connectivity every 5 minutes. What's weird is that I never received any "server down" / unresponsive events until upgrading to the latest version. Before this version my server had been running for around 3 months on the previous version without any events. Nowadays I'm getting an alert every few days. When I log on and check what's happening, there are over a hundred connections to port 18080, whereas before it never seemed to peak above the in/out-peers setting, but maybe that's different?

Anyway, the unresponsive issue seems to be correlated to the number of connections, as if the server can't handle all of them. If I restart the service everything is fine, and if there are even 50 connections it's fine, but it seems when it gets higher it can cause an unresponsive event.

Any ideas?

## selsta | 2022-05-31T20:07:48+00:00
What exactly is UptimeRobot.com checking? RPC availability?

## asheroto | 2022-06-01T02:18:04+00:00
Basically. It's just a free service that can check to see if a website (web server) is down, or ping checks, or port checks.

https://uptimerobot.com/website-monitoring/

To clarify, it can monitor HTTP/websites/web servers, however, I actually have this monitor set up to check port 18080 for connectivity every 5 minutes. So when the alert occurs, port 18080 is inaccessible. At that time, if I try to connect an XMR client (like the XMR GUI) to the node, the connection fails - port 18080 appears to be inaccessible. If I restart the monerod service, all is well again. The issue seems to occur when there are too many connections.

I reviewed the alerts just now. I've had the monitor set up since Feb 2022. There were some alerts in the past few months, but only every few weeks. I upgraded to the latest version of monerod about two weeks ago, and since then, I've had a connectivity issue/alert about every 3-5 days. Upon logging in, I'll find 100+ connections to port 18080.

UptimeRobot.com:
![image](https://user-images.githubusercontent.com/49938263/171313902-40555099-0803-42ca-be86-fa7368467137.png)

I changed the in-peers and out-peers to 24 earlier, and it's obeying at the moment:
![image](https://user-images.githubusercontent.com/49938263/171314670-a5eac986-c929-443b-bff2-775774f5997f.png)

But earlier, it was up at 50+

## asheroto | 2022-06-02T15:15:58+00:00
Oddly enough it's behaving the last few days, capping at 24 as expected. What's weird is that literally the only thing changed on the entire server was the in/out peers from 25 to 24, which I can't imagine would be the reason for its behavior now.... kinda odd. 

Wondering if there's some what in which the cap is ignored because of a bug?

## selsta | 2022-06-02T22:47:20+00:00
It's difficult to tell. I think there are different issues at play here. RPC being unresponsive is related to a bug fixed in #7760, as I wrote in my previous comment. An alternative to this patch is to run monerod with `--rpc-ssl disabled`.

The issue with more connections than set in the limit, I'm not sure. Maybe some connections didn't close correctly for some reason.

## asheroto | 2022-06-06T16:26:10+00:00
It sounds like that disables the SSL on RPC, right?

## selsta | 2022-06-07T08:57:59+00:00
Yes, because the current SSL code for RPC has bugs.

# Action History
- Created by: asheroto | 2022-05-31T15:08:08+00:00
