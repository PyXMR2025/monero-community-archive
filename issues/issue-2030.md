---
title: Nvidia fail
source_url: https://github.com/xmrig/xmrig/issues/2030
author: Loustick2
assignees: []
labels: []
created_at: '2021-01-09T09:36:16+00:00'
updated_at: '2021-04-12T14:24:44+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:24:44+00:00'
---

# Original Description
Hello,
I'm running xmrig 6.7.0 CUDA version with a Nvidia geforce 920M (latest driver installed).
I've installed the CUDA plugin and it is recognize and working fine for about few minutes.
After few minutes I get this message:

[https://ibb.co/PMfHjQ6](url)

I've read that this could be related with thread and block limitation, but despite many attempts to limit them in the config.json file, the thread and block limitations are never taken into account.

Does anyone have an idea on how to fix this? 


A clear and concise description of what the bug is.




Config.json file:

{
    
    "api": {
    "id": null,
    "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "cn/0": false,
        "cn-lite/0": false,
        "kawpow": false
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "NVIDIA",
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": true,
        "loader": "C:/Users/Nicolas/Desktop/xmrig cuda-6.7.0/xmrig-cuda.dll",
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false,
        "rx/0": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 15,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            },
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "donate.v2.xmrig.com:3333",
            "user": "YOUR_WALLET_ADDRESS",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false

}


 - OS: windows 10
 - For GPU related issues: information about GPUs and driver version.


I do thank you

Nicolas


# Discussion History
## Loustick2 | 2021-01-09T09:55:15+00:00
Sorry it seems the link is not working properly. The fail message is:

Nvidia thread #0 failed with error <cryptonight_extra_cpu_final>:440 "the launch timed out and was terminated"



## Spudz76 | 2021-01-15T23:10:31+00:00
Windows default TDR settings are too aggressive, set registry like in various howto's [like this one](https://www.pugetsystems.com/labs/hpc/Working-around-TDR-in-Windows-for-a-better-GPU-computing-experience-777/)

By the time you get TDR at defaults to quit freaking out, you'll have turned your threads and blocks down to useless levels, or maybe not even be able to turn it down enough depending on algo.  This is normal on "slower" cards which take "too long" to complete each work unit run.  Subdividing just adds overhead and kills hashrate and puts more traffic on the PCIe.  So disable TDR completely or extend the timeout until it stops false-triggering (then windows might still help you out by restarting the driver if it really does hang).

## Spudz76 | 2021-01-15T23:19:04+00:00
It's probably less that the Kepler core is slow at processing, but more that it's connected to DDR3 rather than GDDR5 so it is awaiting memory transfer more than awaiting GPU core time.  But same effect, takes too long to complete the work, and TDR kicks in.

Desktop GDDR5 Kepler cards may not trip TDR at the default settings.

CN-R and RandomX algos occasionally have to mutate (live-recompile through NVRTC) and it may only be taking too long when that occurs; therefore the running a while then triggering TDR when it takes a little longer at mutation.

RandomX is really slow on GPUs anyway, on purpose.

## Loustick2 | 2021-01-20T14:13:23+00:00
Thanks a lot for your feedback!
Tdr was indeed the issue, which is now fixed.
It is now running Nice...slow but Nice!
I know i do not have the correct material équipement...it is just an introduction to morning prior potentially invest.

Thanks Again,

Nicolas

## Loustick2 | 2021-01-20T14:14:05+00:00
*to mining*

# Action History
- Created by: Loustick2 | 2021-01-09T09:36:16+00:00
- Closed at: 2021-04-12T14:24:44+00:00
