---
title: defender reports xmrig-2.5.2-gcc-win64 is trojan Win32/Tiggre!plock
source_url: https://github.com/xmrig/xmrig/issues/511
author: wizdude
assignees: []
labels:
- av
created_at: '2018-04-06T23:30:41+00:00'
updated_at: '2018-11-05T13:21:16+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:21:16+00:00'
---

# Original Description
just upgraded to xmrig-2.5.2-gcc-win64 for the new monero PoW and defender has blocked it. 

reports it as being Win32/Tiggre!plock.

defender is happy with the previous xmrig-2.4.4-gcc-win64 that i've been running.

i've excluded the folder that it's in for the time being. virustotal detects the application as xmrig monero miner with no other threats detected.


# Discussion History
## JustHoldit | 2018-04-07T01:06:05+00:00
That's why I always run it in a linux Hyper-V VM on windows. I get a better hash rate, more stability and no Windows Defender.

## KenSharp | 2018-08-10T20:30:34+00:00
**Trojan:Win32/Fuery.B!cl** for `xmrig-2.6.4-msvc-win64.zip` in Windows Defender
**Trojan:Win32/Occamy.C** for `xmrig-2.6.4-gcc-win32.zip` in Windows Defender
**Trojan:Win32/Bluteal!rfn** for `xmrig-2.6.4-gcc-win64.zip` in Windows Defender
**Unix.Malware.Agent-6634015-0** for `xmrig-2.6.4-xenial-amd64.tar.gz` in ClamAV

`xmrig-2.6.4-gcc-win32.zip`, `xmrig-2.6.4-gcc-win64.zip` and `xmrig-2.6.4-msvc-win64.zip` are automatically blocked by Chrome/ium during download (possibly hinting at where Google get their definitions from).

And here's a fun read: [https://cloudblogs.microsoft.com/microsoftsecure/2018/07/26/attack-inception-compromised-supply-chain-within-a-supply-chain-poses-new-risks/](https://cloudblogs.microsoft.com/microsoftsecure/2018/07/26/attack-inception-compromised-supply-chain-within-a-supply-chain-poses-new-risks/)

The source code is _clean_ though!

# Action History
- Created by: wizdude | 2018-04-06T23:30:41+00:00
- Closed at: 2018-11-05T13:21:16+00:00
