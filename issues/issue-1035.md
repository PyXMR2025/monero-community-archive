---
title: Bitmonero stuck after many json request
source_url: https://github.com/monero-project/monero/issues/1035
author: AJIekceu4
assignees: []
labels: []
created_at: '2016-09-02T19:00:38+00:00'
updated_at: '2016-12-15T20:30:34+00:00'
type: issue
status: closed
closed_at: '2016-12-15T20:30:34+00:00'
---

# Original Description
Hello all. My server running 3 bitmonero instance with different ports: 13666,23666,33666.
13666 and 23666 is Monero 'Hydrogen Helix' (v0.9.4.0-04906e6) version from **02.09.2016**
33666 is Monero 'Hydrogen Helix' (v0.9.4.0-unknown) old version from **06.04.2016**

I make json request to all 3 bitmonero via script (node js) every 50ms (20 times per second). And after some time 13666 and 23666 stop working (for some time). At this time - no error in console, but bitmonero did not answer to json request. Script and bitmonero connected via 127.0.0.1 (via internet problem also exist, already test it). I test it on 2 different servers with Ubuntu 16-04 and Ubuntu 14-04 (both have HDD in RAID 1) and problem exist on both.

Log from bitmonero when problem exist:
http://pastebin.com/raw/N473m6E1

Also i noticed that this bug appears at the same time on both 13666 and 23666 (they started in different time > 1 hours). You can see it on screenshots:

![13666](https://cloud.githubusercontent.com/assets/16595267/18215072/34ac485c-7158-11e6-8d87-fe81b4108fd3.jpg)
![23666](https://cloud.githubusercontent.com/assets/16595267/18215074/34ad585a-7158-11e6-8d70-51510b6627a4.jpg)
![33666](https://cloud.githubusercontent.com/assets/16595267/18215073/34acfffe-7158-11e6-8140-64706bf10948.jpg)

If i manually use curl when bitmonero stuck:
`curl -X POST http://127.0.0.1:13666/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getlastblockheader"}' -H 'Content-Type: application/json'`

And **after 60 seconds** get answer:
`curl: (7) Failed to connect to 127.0.0.1 port 13666: Connection timed out`

Problem exist if i run only 1 bitmonero instance on server (v0.9.4.0-04906e6). 
First time i notice this problem after i compile some previous release (from 03.05.2016 i think). **Anyway it was version in which blockchain mdb converted to new format (or something like this, because it promt info about convert)**. 


# Discussion History
## AJIekceu4 | 2016-09-03T10:53:23+00:00
Also i check 3 libboost version:  1.58.0.1, 1.55.0, 1.61.0 and problem exist on all 3 in my system ;(


## moneromooo-monero | 2016-09-18T13:28:22+00:00
When this happens, can you gdb into monerod to find out what it's doing ?

gdb /path/to/monerod `pidof monerod`
thread apply all bt

And paste here the result of the last line.


## AJIekceu4 | 2016-09-19T10:40:29+00:00
https://paste.fedoraproject.org/430939/47428156/raw/


## AJIekceu4 | 2016-09-19T18:44:18+00:00
After applying this patch:
https://github.com/moneromooo-monero/bitmonero/tree/cache-block-template

Problem is gone away. Test 3 monerod instance with 50ms delay and >6 hours online and no problem detected.


## ghost | 2016-12-05T00:22:11+00:00
Hi @AJIekceu4 is this problem still present with a clean installation of monero v0.10? If not, could you close this ticket?

## AJIekceu4 | 2016-12-05T07:31:03+00:00
Hello, today i compiled current version Monero 'Wolfram Warptangent' (v0.10.0.0-45bb393) from github.
And in this version this problem still persist. Very huge cpu utilization and sometimes it is not responding to json request.

## ghost | 2016-12-15T15:59:37+00:00
Hi again @AJIekceu4 - is this an issue with the latest 0.10.1 with the most recent JSON correction?

## AJIekceu4 | 2016-12-15T20:30:34+00:00
Hello. In Monero 'Wolfram Warptangent' (v0.10.1.0-29735c8)
1 problem still persist (very high CPU load), another problem (not responding to json request) - seems ok. I tested about 90 minutes and don't see any problem with json request, but cpu usage is very huge ;)
So i close this issue, because main problem is solved.

# Action History
- Created by: AJIekceu4 | 2016-09-02T19:00:38+00:00
- Closed at: 2016-12-15T20:30:34+00:00
