---
title: --background doesn't work on FreeBSD
source_url: https://github.com/xmrig/xmrig/issues/651
author: DeeeeLAN
assignees: []
labels: []
created_at: '2018-05-27T05:31:34+00:00'
updated_at: '2025-02-15T22:25:59+00:00'
type: issue
status: closed
closed_at: '2018-05-27T17:53:17+00:00'
---

# Original Description
Hi,

When I run my config without -B set, it works fine. When I set -B, xmrig never gets running. The log shows that it makes it up to the point of printing out the COMMANDS: line, but never prints the READY line after that. The web interface never loads either. 

# Discussion History
## lisergey | 2018-05-27T15:46:26+00:00
@avidmills you can use xmrig from ports
`/usr/ports/net-p2p/xmrig`
it is equipped with good startup script which allows to run xmrig in background in FreeBSD-way


## DeeeeLAN | 2018-05-27T16:52:23+00:00
I have installed xmring both from ports and from pkg, the startup script did not change behavior. I will do a more thorough check just to verify though.

Thanks,
Dillan
________________________________
From: lisergey <notifications@github.com>
Sent: Sunday, May 27, 2018 8:46:32 AM
To: xmrig/xmrig
Cc: avidmills; Mention
Subject: Re: [xmrig/xmrig] --background doesn't work on FreeBSD (#651)


@avidmills<https://github.com/avidmills> you can use xmrig from ports
/usr/ports/net-p2p/xmrig
it is equipped with good startup script which allows to run xmrig in background in FreeBSD-way

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/xmrig/xmrig/issues/651#issuecomment-392341277>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AMR86DVjtfEcVUWt4zZSPys8kBRuDT4kks5t2spYgaJpZM4UPJ4p>.


## lisergey | 2018-05-27T17:24:43+00:00
```
FreeBSD-11.1-p10# cat /usr/local/etc/xmrig/config.json
{
    "algo": "cryptonight",  // cryptonight (default) or cryptonight-lite
    "av": 3,                // algorithm variation, 0 auto select
    "background": false,    // true to run the miner in the background
    "colors": true,         // false to disable colored output    
    "cpu-affinity": null,   // set process affinity to CPU core(s), mask "0x3" for cores 0 and 1
    "cpu-priority": 0,      // set process priority (0 idle, 2 normal to 5 highest)
    "donate-level": 2,      // donate level, mininum 1%
    "log-file": "/var/log/xmrig.log",       // log all output to a file, example: "c:/some/path/xmrig.log"
    "max-cpu-usage": 75,    // maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.  
    "print-time": 180,      // print hashrate report every N seconds
    "retries": 2,           // number of times to retry before switch to backup server
    "retry-pause": 6,       // time to pause between retries
    "safe": true,           // true to safe adjust threads and av settings for current CPU
    "syslog": false,        // use system log for output messages
    "threads": 1,           // number of miner threads
    "pools": [
        {
            "url": "pool:3333", // URL of mining server
            "user": "",       // username for mining server
            "pass": "",         // password for mining server
            "keepalive": true,  // send keepalived for prevent timeout (need pool support)
            "nicehash": true,   // enable nicehash/xmrig-proxy support
            "variant": -1       // algorithm PoW variant
        }
    ],
    "api": {
        "port": 0,                             // port for the miner API https://github.com/xmrig/xmrig/wiki/API
        "access-token": null,                  // access token for API
        "worker-id": null                      // custom worker-id for API
    }
}
```
works fine.
This is old-style config, without per-thread options.
```
# pkg inf | grep xmrig
xmrig-2.6.2                    High performance Monero (XMR) CPU miner
```


## trasherdk | 2018-05-27T17:27:23+00:00
I am confused.
Is this a code issues thing, or a general newbie "please help me" thing?
Maybe a note about, directing general help/support/FAQ to stackoverflow,
while questions towards the code, goes here.
I don't understand questions like "why doesn't this software support XYZ coins" ?
Please educate me.

## DeeeeLAN | 2018-05-27T17:53:16+00:00
@lisergey you are right, when I previously tried running with the sysrc startup script, I also had background:true set, which broke it I think. Removing that now shows it working properly. 

Perhaps a note could be added to the freeBSD section of the wiki concerning using sysrc for background operation instead of the xmrig background flag.

## asmaek91 | 2025-02-15T22:25:58+00:00
u should put background true in config...
when config file is used the comand line options don t work!

# Action History
- Created by: DeeeeLAN | 2018-05-27T05:31:34+00:00
- Closed at: 2018-05-27T17:53:17+00:00
