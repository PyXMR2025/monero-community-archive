---
title: 'Regression in 2.15: CLI setting of threads does not work'
source_url: https://github.com/xmrig/xmrig/issues/1058
author: trickv
assignees: []
labels:
- bug
- need feedback
created_at: '2019-07-10T04:01:14+00:00'
updated_at: '2019-08-09T10:10:41+00:00'
type: issue
status: closed
closed_at: '2019-08-09T10:10:41+00:00'
---

# Original Description
I've noticed a slight regression in the 2.15 (and now 2.16) tags.  It seems that --threads (or -t) on the command-line is being ignored, while if I put all my configuration into config.json, it is honored.

I will try and pinpoint the changes in the git history if I can, but perhaps this is more obvious to a regular xmrig developer than it is to me.

```
[trick@here ~/src/xmrig-2.16.0-beta/build]$ ./xmrig  -o stratum+tcp://pool.supportxmr.com:5555 -u 49gJSVqMoq86665wytyNA3JSFCFwfsSecVfqib76cfH4AKHUYR9EC498WbjA55LmNRhJ7V7mQapJjRGkNEPF3ffZNiBaVPX --dry-run -t 1 
 * ABOUT        XMRig/2.16.0-beta gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1b 
 * CPU          Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz (1) x64 AES AVX2
 * CPU L2/L3    1.0 MB/6.0 MB
 * THREADS      3, cn, av=0, donate=5%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+tcp://pool.supportxmr.com:5555 variant auto
 * COMMANDS     hashrate, pause, resume
[2019-07-09 22:50:29.547] OK
```

```
[trick@here ~/src/xmrig-2.15.4-beta]$ ./xmrig  -o stratum+tcp://pool.supportxmr.com:5555 -u 49gJSVqMoq86665wytyNA3JSFCFwfsSecVfqib76cfH4AKHUYR9EC498WbjA55LmNRhJ7V7mQapJjRGkNEPF3ffZNiBaVPX --dry-run -t 1 
 * ABOUT        XMRig/2.15.4-beta gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1b 
 * CPU          Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz (1) x64 AES AVX2
 * CPU L2/L3    1.0 MB/6.0 MB
 * THREADS      3, cn, av=0, donate=5%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+tcp://pool.supportxmr.com:5555 variant auto
 * COMMANDS     hashrate, pause, resume
[2019-07-09 22:51:00.974] OK
```

```
[trick@here ~/src/xmrig-2.14.4/build]$ ./xmrig  -o stratum+tcp://pool.supportxmr.com:5555 -u 49gJSVqMoq86665wytyNA3JSFCFwfsSecVfqib76cfH4AKHUYR9EC498WbjA55LmNRhJ7V7mQapJjRGkNEPF3ffZNiBaVPX --dry-run -t 1 
 * ABOUT        XMRig/2.14.4 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1b microhttpd/0.9.62 
 * CPU          Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz (1) x64 AES AVX2
 * CPU L2/L3    1.0 MB/6.0 MB
 * THREADS      1, cryptonight, av=0, donate=5%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+tcp://pool.supportxmr.com:5555 variant auto
 * COMMANDS     hashrate, pause, resume
[2019-07-09 22:51:27] OK
```

Note the interpreted level of threads in each example above - the only one that gets it right is 2.14.4.

If I put threads into config.json on 2.15/2.16 it works as it should:
```
[trick@here ~/src/xmrig-2.15.4-beta/build]$ cat config.json
{
    "pools": [
        {
            "url": "stratum+tcp://pool.supportxmr.com:5555",
            "user": "49gJSVqMoq86665wytyNA3JSFCFwfsSecVfqib76cfH4AKHUYR9EC498WbjA55LmNRhJ7V7mQapJjRGkNEPF3ffZNiBaVPX",
            "pass": "x"
        }
    ],
    "threads": 1,
    "dry-run": true
}
[trick@here ~/src/xmrig-2.15.4-beta/build]$ ./xmrig 
 * ABOUT        XMRig/2.15.4-beta gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1b 
 * CPU          Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz (1) x64 AES AVX2
 * CPU L2/L3    1.0 MB/6.0 MB
 * THREADS      1, cn, av=0, donate=0%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+tcp://pool.supportxmr.com:5555 variant auto
 * COMMANDS     hashrate, pause, resume
[2019-07-09 22:59:51.921] OK
```

Hope this helps!

# Discussion History
## xmrig | 2019-08-02T11:39:52+00:00
In v2.99.x this issue should be fixed.
Thank you.

# Action History
- Created by: trickv | 2019-07-10T04:01:14+00:00
- Closed at: 2019-08-09T10:10:41+00:00
