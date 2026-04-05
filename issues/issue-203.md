---
title: cpu usage
source_url: https://github.com/xmrig/xmrig/issues/203
author: sametyuksel
assignees: []
labels:
- question
- NUMA
created_at: '2017-11-16T07:14:49+00:00'
updated_at: '2018-09-12T18:54:25+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:54:24+00:00'
---

# Original Description
hi

i cannot use all my cpus to hash more.
i have "Dual Intel Xeon X5650 2.66GHz HexaCore 24 cores".

Here what i tried on config.json;

cpu-affinity: null, cpu-priority: 5, max-cpu-usage: 100, threads: null (random 12 cores, 453 H/s)
cpu-affinity: 0xFFF, cpu-priority: 5, max-cpu-usage: 100, threads: null (first 12 cores, 450 H/s)
cpu-affinity: 0xFFF, cpu-priority: 5, max-cpu-usage: 100, threads: 24 (first 12 cores, 390 H/s)
cpu-affinity: 0xFFFFFF, cpu-priority: 5, max-cpu-usage: 100, threads: 24 (all 24 cores, 111 H/s)

what should i do to use all cores and get more hashrate.






# Discussion History
## xmrig | 2017-11-16T07:20:49+00:00
12 threads is optimal, because performance limited by CPU cache, not cores, each thread required 2 MB, so 24 / 2 = 12.

Option `max-cpu-usage` ignored if you manually specify threads and this option limited first by cache too.
Thank you.

## m1911 | 2017-11-17T09:48:53+00:00
I'm a double Xeon X5650.
Ubuntu 16.04 System.
It can only use one CPU.
@xmrig 

## sametyuksel | 2017-11-17T09:51:15+00:00
@m1911 how much hashpower do you have?

## m1911 | 2017-11-17T10:00:17+00:00
speed 2.5s/60s/15m 457.0 456.2 455.3 H/s max: 457.2 H/s
@xmrig 

## m1911 | 2017-11-17T19:31:11+00:00
@yyfong0918  My configuration
{
    "algo": "cryptonight",  // cryptonight (default) or cryptonight-lite
    "av": 0,                // algorithm variation, 0 auto select
    "background": false,    // true to run the miner in the background
    "colors": true,         // false to disable colored output    
    "cpu-affinity": 0x00003f,   // set process affinity to CPU core(s), mask "0x3" for cores 0 and 1
    "cpu-priority": 5,   // set process priority (0 idle, 2 normal to 5 highest)
    "donate-level": 1,      // donate level, mininum 1%
    "log-file": null,       // log all output to a file, example: "c:/some/path/xmrig.log"
    "max-cpu-usage": 80,    // maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.  
    "print-time": 60,       // print hashrate report every N seconds
    "retries": 5,           // number of times to retry before switch to backup server
    "retry-pause": 5,       // time to pause between retries
    "safe": false,          // true to safe adjust threads and av settings for current CPU
    "syslog": false,        // use system log for output messages
    "threads": null,        // number of miner threads
    "pools": [
        {
            "url": "xmr-us-east1.nanopool.org:14444", // URL of mining server
            "user": "",
            "pass": "x",                       // password for mining server
            "keepalive": true,                 // send keepalived for prevent timeout (need pool support)
            "nicehash": false                  // enable nicehash/xmrig-proxy support
        }
    ],
    "api": {
        "port": 0,                             // port for the miner API https://github.com/xmrig/xmrig/wiki/API
        "access-token": null,                  // access token for API
        "worker-id": null                      // custom worker-id for API
    }
}

But run an error.
/root/xmrig/build/config.json:300: Missing a comma or '}' after an object member.
No pool URL supplied. Exiting.

## sametyuksel | 2017-11-17T19:38:22+00:00
@yyfong0918 

"cpu-affinity": 0x00003f,
>>
"cpu-affinity": "0x00003f",

## sametyuksel | 2017-11-17T19:39:19+00:00
@yyfong0918 how do you open "turbo" on your processor?

## m1911 | 2017-11-17T19:41:54+00:00
@yyfong0918 Ubuntu 16.04 

## sametyuksel | 2017-11-17T19:54:24+00:00
in which pool? @yyfong0918 

## sametyuksel | 2017-11-17T20:02:13+00:00
@yyfong0918 where will you exchange it, i cant see it on poloniex?

## sametyuksel | 2017-11-17T20:11:11+00:00
would you please tell us your server's hashrate, not whattomine. @yyfong0918 
do you have this hashpower with cryptonight-lite?

## m1911 | 2017-11-17T20:11:24+00:00
@yyfong0918 Why does Ubuntu 16.04 run the error?

## sametyuksel | 2017-11-17T20:15:04+00:00
do you rent it?if yes how much? :) @yyfong0918 

## sametyuksel | 2017-11-17T20:21:05+00:00
wow its expensive.i bought it 39.99$.
if you would like to buy it annually its 29.99$

## sametyuksel | 2017-11-17T20:23:32+00:00
what you mean? did you buy it for this prices?

## sametyuksel | 2017-11-17T20:27:02+00:00
@yyfong0918 im very surprised.So you can rent it on miningrigrentals, you can earn more.

## sametyuksel | 2017-11-17T20:38:44+00:00
mrr is a different system.you can take a look.
you can rent your hashpower, not your server and with hours.

 @yyfong0918 

## sametyuksel | 2017-11-17T20:57:02+00:00
ok you said
you can earn; XMR = 12700 sato/day (480H/s) * 2 for KH 25400 sato/day.

also after you put your servers on the site, you have an option that, you can forward your hashpower to any mining pool when its not rented.

## sametyuksel | 2017-11-17T21:35:04+00:00
i can help you, if you have questions. @yyfong0918 

## sametyuksel | 2017-11-17T21:50:58+00:00
i cant see it, did you activate it?

## sametyuksel | 2017-11-18T00:09:54+00:00
i have two servers rented.
@yyfong0918 

## gtimeg77 | 2017-11-22T18:51:58+00:00
kind of same topic
limiting cpu on one machine works fine
same os/build it doesnt

## jdevsan | 2017-11-27T20:32:43+00:00
@sametyuksel where did u rent?


## sametyuksel | 2017-11-27T20:35:44+00:00
turnkeyinternet.net @pepecachivache 

## jdevsan | 2017-11-27T20:36:56+00:00
@sametyuksel what service do u recommend me to mine monero? with xmrig


## sametyuksel | 2017-11-27T20:39:14+00:00
im going to rent 25 of x5650 today or tomorrow and i will use xmrig on ubuntu 16.04.
If your provider let, overclock.

## jdevsan | 2017-11-27T20:40:28+00:00
@sametyuksel how u overclock it?

## sametyuksel | 2017-11-27T20:41:02+00:00
not me, ask to your provider.

## jdevsan | 2017-11-27T20:42:06+00:00
how is the way to ask them to overclock it?

## sametyuksel | 2017-11-27T20:43:09+00:00
open a support ticket and tell them to overclock on BIOS.

## jdevsan | 2017-11-27T20:44:37+00:00
you are earning  like 4 dolar each with 450 h per sec? excluding cost of hexacore server

## sametyuksel | 2017-11-27T20:46:53+00:00
yes @pepecachivache 

## jdevsan | 2017-11-27T20:51:18+00:00
u paid plan for one year no? and pool fee? what cripto are u mining?

## sametyuksel | 2017-11-27T20:52:45+00:00
im mining monero, 29.99 yearly is ok.But 39.99 is not unprofitable for just mining.

## jdevsan | 2017-11-27T21:00:52+00:00
@sametyuksel do you have a cellphone to talk? thanks

## sametyuksel | 2017-11-27T21:05:18+00:00
@pepecachivache im not available for call.you can mail me sametyuksel@gmail.com

## jdevsan | 2017-11-28T03:36:13+00:00
let me know when you are online!

2017-11-27 18:05 GMT-03:00 sametyuksel <notifications@github.com>:

> @pepecachivache <https://github.com/pepecachivache> im not available for
> call.you can mail me sametyuksel@gmail.com
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/203#issuecomment-347327643>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/ALKtYRH2XWDpTM7PR8-YEHeMUEhMO5XJks5s6yQSgaJpZM4QgDlz>
> .
>


## shrewdacumen | 2018-09-12T18:54:25+00:00
This happens on MacOS.
./xmrig -c some.file.json  --> produces an error if I removed config.json file.
cp some.file.json config.json
./xmrig --> run without problem.

xmrig does not recognize multi-cores on MacOS High Sierra.
Thus it runs sluggishly using 1-core only. (Intel i7 process felt useless with xmrig on MacOS)


# Action History
- Created by: sametyuksel | 2017-11-16T07:14:49+00:00
- Closed at: 2018-03-14T22:54:24+00:00
