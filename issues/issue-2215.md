---
title: Problem with 24 threads processor and a low range of memory
source_url: https://github.com/xmrig/xmrig/issues/2215
author: agn-7
assignees: []
labels:
- question
created_at: '2021-03-28T11:55:24+00:00'
updated_at: '2021-04-12T13:46:53+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:46:53+00:00'
---

# Original Description
I have two VMs on two separate servers, and I don't have any problems with the first one. By the way, it has 8 threads and 8GB RAM. However, another one has 24 threads and 10GB RAM (I think it is insufficient). So when I run the `./xmrig` memory usage reaches to high and the machine gets stuck. It seems that, there is a direct correlation between the number of threads and given RAM capacity.
So my question is, is there any config to limit the number of threads or something?

Here's my cpu configuration section in `config.json`:

```
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": true,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "cn/0": false,
        "cn-lite/0": false
    },
```

---
I'm using *ubuntu server 18.04*

# Discussion History
## SChernykh | 2021-03-28T12:08:30+00:00
RandomX mining requires 2 GB RAM per NUMA node + only 2 MB memory per thread, so number of threads doesn't matter. I'm 99% sure that you have only 1 NUMA node there, so 10 GB should be enough. Check what else is running there and consuming all memory.

## agn-7 | 2021-03-28T21:00:44+00:00
> RandomX mining requires 2 GB RAM per NUMA node + only 2 MB memory per thread, so number of threads doesn't matter.

@SChernykh You are right. Acknowledging this I reduced `"max-threads-hint": 100,` from 100 to 75, and 6 threads are now free, but the memory usage is still over 10GB.

But the problem is the `xmrig` service uses this amount of memory (10.5GB!):

![xmrig-memory-usage](https://user-images.githubusercontent.com/14202344/112767868-50988400-902e-11eb-8c72-56c98e137b95.png)

However, in another machine, it is about 3GB:

![xmrig-memory-usage-lite](https://user-images.githubusercontent.com/14202344/112767873-5726fb80-902e-11eb-8588-abfe7508da41.png)



## xmrig | 2021-04-12T13:46:53+00:00
This is virtual memory usage, this does not mean the miner consumes 10GB.
Thank you.

# Action History
- Created by: agn-7 | 2021-03-28T11:55:24+00:00
- Closed at: 2021-04-12T13:46:53+00:00
