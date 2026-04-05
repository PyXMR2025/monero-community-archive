---
title: Up to 50% performance increase with software AES implementation (for CPU without
  AES-NI support)
source_url: https://github.com/xmrig/xmrig/issues/579
author: sergneo
assignees: []
labels: []
created_at: '2018-04-23T07:31:35+00:00'
updated_at: '2019-08-02T12:53:46+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:53:46+00:00'
---

# Original Description
https://github.com/Foudge/xmrig/releases

>  I have a bad news. I stopped mining with my CPU and stopped develop this project. I started the merge but it's not functionnal and need work and time to do all the necessary.

https://github.com/Foudge/xmrig/issues/1#issuecomment-383230732
The F3-F4 version for processors without AES performance is higher to 47%. Foudge rewrited soft-AES code (up to 50% perf increase !). The last time you included in your code is only part of the improvements.
the difference in hashrate between algorithms before and after hard fork is insignificant.
Here is a performance comparison:
Windows 7 x64 , ver. MSVC, pool Minergate.com
**Xeon E5440 (3.14GHz) (12M L2) av=4 th =4**
Xmrig 2.6.0-beta3 - 106 H/s (XMR v7)
Xmrig F4 - 126 H/s (XMO original CryptoNight)
a difference of 18%

**Quad Q8400 (6M L2) av=3 th =4**
Xmrig 2.6.0-beta3 - 82 H/s (XMR v7)
Xmrig F4 - 102 H/s (XMO original CryptoNight)
a difference of 24%

**Core2Duo E8500 (6M L2) av=4 th=2**
Xmrig 2.6.0-beta3 - 44 H/s (XMR v7)
Xmrig F4 - 64 H/s (XMO original CryptoNight)
a difference of 47%

as a result, on all processors the difference is exactly 20 hash, for such old processors is a significant increase in speed, especially when you have a fleet of 100-200 CPU

So here's a big request could you include its rewritten code for CPU without AES in your miner?
This particularly concerns the MSVC/assembly version. https://github.com/xmrig/xmrig/commit/8e5ff7aecc6a8778e7ea5d99e8e021587adcb11d
The basis Foudge took your version xmrig 2.4.4

@xmrig say you have the desire and opportunity to add?

here's another test:
Core2Quad Q9300 av=3 th=4

JCE Cryptonote CPU Miner - 94,85 h/s
XMRIG-F4 - 96,7 h/s
xmrig-2.6.0-beta3 - 78 h/s

Apparently your direct competitor jceminer used the same technologies that Foudge did. do not give up, make your miner is better 
> Devfees are:
>   3.0% when using at least one mining thread with non-AES architecture
>   3.0% when using 32-bits version
>   1.5% when using only 64-bits AES architecture

# Discussion History
## sergneo | 2018-04-26T17:15:10+00:00
@xmrig say you'll be able to add improvements or not?

## bobbieltd | 2018-04-26T17:55:52+00:00
+1

## 2010phenix | 2018-04-27T12:39:06+00:00
+1

PS i think before **2.6 stable** master revision, no any other solution and ideas be made.

# Action History
- Created by: sergneo | 2018-04-23T07:31:35+00:00
- Closed at: 2019-08-02T12:53:46+00:00
