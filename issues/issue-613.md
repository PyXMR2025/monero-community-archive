---
title: 'Latest xmrig v. 2.6.2: wrong output with system log'
source_url: https://github.com/xmrig/xmrig/issues/613
author: erotavlasme
assignees: []
labels: []
created_at: '2018-05-07T09:30:32+00:00'
updated_at: '2018-06-17T18:02:51+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:02:51+00:00'
---

# Original Description
Hi,
I found that with latest version v.2.6.2 by enabling the output via system.log, the output is wrong.
`[2018-05-07 11:30:01] [01;32m * [01;37mVERSIONS:     [01;36mXMRig/2.6.2[01;37m libuv/1.8.0 gcc/7.3.0
[2018-05-07 11:30:01] [01;32m * [01;37mCPU:          Intel(R) Core(TM) i7-3537U CPU @ 2.00GHz (1) [01;32mx64 [01;32mAES-NI
[2018-05-07 11:30:01] [01;32m * [01;37mCPU L2/L3:    0.5 MB/4.0 MB
[2018-05-07 11:30:01] [01;32m * [01;37mTHREADS:      [01;36m2[01;37m, cryptonight, av=0, donate=1%
[2018-05-07 11:30:01] [01;32m * [01;37mPOOL #1:      [01;36mpool.minexmr.com:80
[2018-05-07 11:30:01] [01;32m * [01;37mPOOL #2:      [01;36mpool.minexmr.com:443
[2018-05-07 11:30:01] [01;32m * [01;37mPOOL #3:      [01;36mxmr-eu1.nanopool.org:14444
[2018-05-07 11:30:01] [01;32m * [01;37mCOMMANDS:     [01;35mh[01;37mashrate, [01;35mp[01;37mause, [01;35mr[01;37mesume
[2018-05-07 11:30:01] [01;37muse pool [01;36mpool.minexmr.com:80 [01;30m94.130.206.79
[2018-05-07 11:30:01] [1;35mnew job[0m from [1;37mpool.minexmr.com:80[0m diff [1;37m35000[0m algo [1;37mcn/1[0m
[2018-05-07 11:30:01] [1;32mREADY (CPU)[0m threads [1;36m2(2)[0m huge pages [1;32m2/2 100%[0m memory [1;36m4.0 MB[0m`
I also found that some options (watch, rig-id, hw-aes) do not have any description [here](https://github.com/xmrig/xmrig).
Thank you

# Discussion History
## xmrig | 2018-05-07T19:24:34+00:00
Disable colors, `"colors": false,` it will solve this issue, previous versions was automatically disable colors, now it more flexible, sometimes colors more important than extra ANSI escape characters in log.

* `watch` enable file config watching, reload configuration when config file changed, same as proxy, this feature not fully implemented, don't use it now.
* `rig-id` rig identifier for pool-side statistics (needs pool support), also xmrig-proxy support it on both sides.
* `hw-aes` force enable/disable hardware aes support for [advanced threads mode](https://github.com/xmrig/xmrig/issues/563).




# Action History
- Created by: erotavlasme | 2018-05-07T09:30:32+00:00
- Closed at: 2018-06-17T18:02:51+00:00
