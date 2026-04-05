---
title: Mining turtlecoin on ubuntu
source_url: https://github.com/xmrig/xmrig/issues/1798
author: Therealjosephchrzempiec
assignees: []
labels: []
created_at: '2020-08-03T05:38:00+00:00'
updated_at: '2020-08-28T16:29:47+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:29:47+00:00'
---

# Original Description
Hello i haven't touched linux ubuntu in a long time and i wasn't good at it back then. But i now have 2 desktop computers with ubuntu on them and i would love to mine turtlecoin using Xmrig. I did install Xmrig not sure how to make it work with turtlecoin. I do have the pool address plus all the information. I just do not know how get it running. I looked all over online and it is unclear what to do next after install Xmrig for turtlecoin. Can someone please help me on the steps i need to do to get running?


Joseph

# Discussion History
## SChernykh | 2020-08-03T14:23:28+00:00
Just set `"algo" : "argon2/chukwa",` in config.json next to the pool URL. Turtlecoin uses this algorithm now.

## Therealjosephchrzempiec | 2020-08-03T16:30:23+00:00
Hello thank you for that. I have tried that and somehow i couldn't get it to run. Not sure what the problem is. So i ran this command in terminal ./xmrig -a cryptonight-lite  --api-worker-id i76700 -o trtl.pool.mine2gether.com:4445 -u mytrtl wallet  -p i76700 -k -t 5 and that seem to work. I was mining with no problem. However I'm trying to figure out how to run that on startup automatically afterbooting. Because a lot of time i wont be here.

Is there a way i can do that? When i checked online everything i found so far was a Py script on startup.


Joseph

## Lonnegan | 2020-08-04T08:17:31+00:00
Turtlecoin doesn't use "cryptonight-lite" anymore! They've forked to "cn-pico" in 2018 already and meanwhile to "argon2/chukwa". It may be, that mine2gether pool uses algo auto detection, so your wrong algo setting is been ignored by xmrig, but the command line you are using is definetly wrong!

But AFAIK...
https://xmrig.com/docs/algorithms
... xmrig supports argon2/chukwa only with CPU, not with GPU. But mining Argon2 with CPU is not very sensible. May be you have to use an other mining software to mine Turtlecoin with your GPU.

## ordtrogen | 2020-08-05T14:55:41+00:00
I started mining on Ubuntu 20 yesterday and use this section in config.json

    "pools": [
        {
            "algo": "argon2/chukwa",
            "url": "pool.semipool.com:22209",
            "user": "<myTRTLaddress>",
            "pass": "myaddress@gmail.com",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null
		}
    ]

## davenport651 | 2020-08-08T09:53:36+00:00
To make the miner autostart in Ubuntu, follow these instructions:  https://help.ubuntu.com/stable/ubuntu-help/startup-applications.html.en

The command you'll add will be something like:
`/usr/bin/xterm /home/$USER/xmrig -a argon2/chukwa --api-worker-id i76700 -o trtl.pool.mine2gether.com:4445 -u mytrtl wallet -p i76700 -k -t 5`

## Therealjosephchrzempiec | 2020-08-09T04:11:22+00:00
Hello i was able to cpu mine with no problem. Thank you. 

# Action History
- Created by: Therealjosephchrzempiec | 2020-08-03T05:38:00+00:00
- Closed at: 2020-08-28T16:29:47+00:00
