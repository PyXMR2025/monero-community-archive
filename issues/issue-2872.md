---
title: if 1st --tls pool fails, all non tls backup pools fail too. there is no --notls
  param to use for backup pools.
source_url: https://github.com/xmrig/xmrig/issues/2872
author: sfhdfshdfh
assignees: []
labels: []
created_at: '2022-01-17T15:47:24+00:00'
updated_at: '2022-01-19T13:20:23+00:00'
type: issue
status: closed
closed_at: '2022-01-19T13:20:23+00:00'
---

# Original Description
**Describe the bug**
when using --tls for first pool it expects all backup pools to be tls too, as a result, when 1st one fails the next ones fail too(for not being tls), there is no param such as --notls or --tls=0 to disable it for nontls backup pools individually. 
lack of params to disable tls for every single pool defined in batch file.

**To Reproduce**
i need something like this to work.
xmrig.exe -o tlspool.com:445 -u wallet --TLS -p x   -o backup-pool.com:80 -u wallet --NoTLS -p x ... and next tls & non tls backup pools

or just make xmrig try the pool without tls settings if there is no --tls specified for it. make --tls mandatory for every single pool and backup pools defined in the bat file to use tls mode.


**Expected behavior**

**Required data**

**Additional context**


# Discussion History
## SChernykh | 2022-01-17T18:36:17+00:00
You can setup every pool in any way you want in config.json. Don't try to use command line for advanced setups.

## APT-ZERO | 2022-01-18T09:09:43+00:00
@SChernykh 
so my idea #2564 was not that bad

## SChernykh | 2022-01-18T09:15:20+00:00
No, it's a bad idea. Command line length is not enough for this on some systems. Embedded config is supported if you compile XMRig yourself.

# Action History
- Created by: sfhdfshdfh | 2022-01-17T15:47:24+00:00
- Closed at: 2022-01-19T13:20:23+00:00
