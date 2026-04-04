---
title: incoming connection counts seems unrealistic and doesn't match system
source_url: https://github.com/monero-project/monero/issues/9817
author: Gingeropolous
assignees: []
labels: []
created_at: '2025-02-24T11:35:20+00:00'
updated_at: '2025-05-29T19:04:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
Height: 2969840/3354567 (88.5%) on mainnet, not mining, net hash 2.08 GH/s, v16, 12(out)+11172(in) connections, uptime 4d 7h 49m 27s

ss -tn | grep ":18080" | wc -l 
665
```

so the daemon reports 11k inc cnxns, but the system reports 665 on port 18080.  This is a seed node, so it doesn't have a in-peers limit set (just whatever the default is, which I think is unlimited?) Also has dns blocklist and the file

# Discussion History
## selsta | 2025-02-24T12:27:09+00:00
How quickly does it rise to such an amount when you restart? and also does this happen with `releae-v0.18` branch and v0.18.3.4`?

## Gingeropolous | 2025-02-24T20:45:18+00:00
this is with release-v0.18 , with 9740 pulled in (shouldn't matter tho), and its still synchronizing. 

this is the current output of status:

Height: 2993884/2993884 (100.0%) on mainnet, not mining, net hash 3.31 GH/s, v16, 10(out)+11653(in) connections, uptime 4d 17h 1m 29s

so about 500 was added in 10 hours. 

lemme restart and see how quickly it goes up. i'll also test with 18.3.4 

## Gingeropolous | 2025-02-24T21:08:43+00:00
release w/ 9740, 11 mins

Height: 2994324/3354892 (89.3%) on mainnet, not mining, net hash 2.90 GH/s, v16, 12(out)+30(in) connections, uptime 0d 0h 11m 22s

41 mins
Height: 2995604/3354906 (89.3%) on mainnet, not mining, net hash 3.19 GH/s, v16, 12(out)+98(in) connections, uptime 0d 0h 41m 51s

6.5 hours:
Height: 3011432/3355094 (89.8%) on mainnet, not mining, net hash 2.63 GH/s, v16, 12(out)+714(in) connections, uptime 0d 6h 36m 39s
ss -tn | grep ":18080" | wc -l 
249





## Gingeropolous | 2025-02-28T20:36:40+00:00
now after 3 days,

Height: 3118316/3357753 (92.9%) on mainnet, not mining, net hash 2.07 GH/s, v16, 7(out)+5998(in) connections, uptime 3d 23h 35m 35s


whereas, 

 ss -tn | grep ":18080" | wc -l 
641




## vtnerd | 2025-03-03T21:33:23+00:00
What os/distro? What is the Boost version in use?

## Gingeropolous | 2025-03-04T03:28:59+00:00
Description:	Ubuntu 22.04.5 LTS

#define BOOST_LIB_VERSION "1_74"



## hinto-janai | 2025-05-26T19:49:56+00:00
Also experiencing with:
- v0.18.4.0-c84cc6392
- Debian 12
- libboost-all-dev 1.74.0.3

`./monerod status`:
```
Height: 3420402/3420402 (100.0%) on mainnet, not mining, net hash 6.26 GH/s, v16, 1022(out)+132(in) connections, uptime 9d 4h 22m 34s
```

`monerod.conf`:
```
out-peers=1024
in-peers=1024
```

`ss -tn | awk '{print $5}' | grep ":18080" | wc -l`:
```
1014
```

## selsta | 2025-05-26T20:43:57+00:00
@hinto-janai I'm not sure if this is the same issue that ginger reported. 132 incoming connection is realistic. 5k-10k is unrealistic.

The fact that it doesn't fully match with the system has to be compared with different versions.

## vtnerd | 2025-05-27T00:57:43+00:00
Although uncommon, neither port has to be 18080 as well. 

## Gingeropolous | 2025-05-29T19:04:05+00:00
i wonder if this only occurs during initial blockchain download.

the node has syncd, and now the cnxns seem normal:

Height: 3422435/3422435 (100.0%) on mainnet, not mining, net hash 4.46 GH/s, v16, 12(out)+62(in) connections, uptime 93d 22h 5m 58s
Monero 'Fluorine Fermi' (v0.18.4.0-9e032c8f7)


# Action History
- Created by: Gingeropolous | 2025-02-24T11:35:20+00:00
