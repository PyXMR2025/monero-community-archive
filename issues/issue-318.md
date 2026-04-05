---
title: Number of threads is 1
source_url: https://github.com/xmrig/xmrig/issues/318
author: quatranon
assignees: []
labels: []
created_at: '2018-01-05T11:12:33+00:00'
updated_at: '2018-01-05T14:16:45+00:00'
type: issue
status: closed
closed_at: '2018-01-05T14:16:45+00:00'
---

# Original Description
Please help me increase the number of CPU threads thus increase hashrate
![image](https://user-images.githubusercontent.com/35136675/34606931-4007373c-f237-11e7-9bbe-47fcbd419b24.png)
Thanks in advance @xmrig 
  

# Discussion History
## davidtavarez | 2018-01-05T12:51:48+00:00
When you run it without `-t, --threads=N` xmrig select automatically the number of threads. So you need to pass `-t X` where `X` is the number of threads that you want. 

## quatranon | 2018-01-05T12:58:23+00:00
{
    "algo": "cryptonight",  // cryptonight (default) or cryptonight-lite
    "av": 0,                // algorithm variation, 0 auto select
    "background": true,    // true to run the miner in the background
    "colors": true,         // false to disable colored output    
    "cpu-affinity": 0xFFFF,   // set process affinity to CPU core(s), mask "0x3" for cores 0 and 1
    "cpu-priority": null,   // set process priority (0 idle, 2 normal to 5 highest)
    "donate-level": 5,      // donate level, mininum 1%
    "log-file": null,       // log all output to a file, example: "c:/some/path/xmrig.log"
    "max-cpu-usage": 70,    // maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.  
    "print-time": 60,       // print hashrate report every N seconds
    "retries": 5,           // number of times to retry before switch to backup server
    "retry-pause": 5,       // time to pause between retries
    "safe": false,          // true to safe adjust threads and av settings for current CPU
    "threads": null,        // number of miner threads
    "pools": [
        {
            "url": "failover.xmrig.com:443",   // URL of mining server
            "user": "wallet",                        // username for mining server
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
Can you please tell which line is to be changed and how @davidtavarez ?
Thanks in advance.

## davidtavarez | 2018-01-05T13:05:39+00:00
`"threads": null, // number of miner threads`

replace null by the number of threads.

## quatranon | 2018-01-05T13:09:32+00:00
I tried that but still shows thread : 1 @davidtavarez 
![image](https://user-images.githubusercontent.com/35136675/34610535-9c3fc356-f247-11e7-9ab8-501af0a69567.png)
![image](https://user-images.githubusercontent.com/35136675/34610555-b096e80c-f247-11e7-872b-ccee954d924b.png)
Thanks in advance.

## Dhruv420 | 2018-01-05T13:20:13+00:00
@quatranon Save the config.json and try running the miner with admin privileges. 

## quatranon | 2018-01-05T13:22:15+00:00
Still no luck @Dhruv420 ....

## Dhruv420 | 2018-01-05T13:25:53+00:00
@quatranon 
Wait...according to your config the donate level is 5.But the terminal shows 0.From where did you download the miner?Try downloading from here(https://github.com/xmrig/xmrig/releases) and see if it works.
  

## quatranon | 2018-01-05T14:16:45+00:00
Thanks @davidtavarez  and @Dhruv420  for your help, the issue is solved now.

# Action History
- Created by: quatranon | 2018-01-05T11:12:33+00:00
- Closed at: 2018-01-05T14:16:45+00:00
