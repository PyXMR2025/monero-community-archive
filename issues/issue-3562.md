---
title: 'Monerod: internal error: try to insert duplicate iterator in key_image set'
source_url: https://github.com/monero-project/monero/issues/3562
author: ordtrogen
assignees: []
labels: []
created_at: '2018-04-05T14:53:09+00:00'
updated_at: '2018-06-25T22:56:59+00:00'
type: issue
status: closed
closed_at: '2018-06-25T22:56:59+00:00'
---

# Original Description
Don't know how important this is but I'll report it anyway

Windows 10 - 64-bit
monerod --version returns "Monero 'Lithium Luna' (v0.12.0.0-master-release)"

![image](https://user-images.githubusercontent.com/15184875/38373451-96efca22-38f1-11e8-8fbb-7493db892d4b.png)


# Discussion History
## mochaccinuh | 2018-04-07T12:33:30+00:00
Same here on linux 64 v0.12.0.0-master-release. Got the error message shortly after I was synchronized with the network (2 minutes after).

## pat-sullivan | 2018-04-11T16:21:49+00:00
Same on mac as well. Right after the mapsize increase message

## rblaine95 | 2018-04-12T12:18:23+00:00
Just got this a couple minutes ago
![image](https://user-images.githubusercontent.com/4052340/38676804-7608f0fc-3e5c-11e8-9e5e-4264e5e80a80.png)




## ghost | 2018-04-15T08:19:05+00:00
Mint 18 
monero-v0.12.0.0

`2018-04-15 06:21:41.518	[P2P1]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:400	internal error: try to insert duplicate iterator in key_image set
2018-04-15 06:21:41.556	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:400	internal error: try to insert duplicate iterator in key_image set`

## mocadnet | 2018-04-18T06:54:02+00:00
same on here on Amazon Linux AMI

## d4m4ri | 2018-04-21T14:35:56+00:00
This error is reproducible by removing the entire blockchain (rm -r ~/.bitmonero/) and download the entire BC again. Once it's synchronised it will show these errors ("2018-04-xx xx:xx:xx.xxx [P2P5] ERROR txpool src/cryptonote_core/tx_pool.cpp:400 internal error: try to insert duplicate iterator in key_image set") a few times. The transfer command ("transfer") in CLI works fine. I assume it's a key/hash collision due to one/several duplicates in the DB/BC.

## OrvilleRed | 2018-04-24T04:42:44+00:00
Could these be the result of attacks from forked chains with prior key images?
https://www.coindesk.com/airdrop-attack-coming-monero-fork-condemned-as-privacy-threat/

## RichAyotte | 2018-05-17T18:36:19+00:00
Just adding a me too.

```
2018-05-17 18:26:44.111	[P2P8]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:400	internal error: try to insert duplicate iterator in key_image set
```
Seen on an updated Debian Sid with custom kernel.

```
$ uname -a
Linux cheetah 4.16.5-phenom #1 SMP PREEMPT Wed May 2 15:54:19 EDT 2018 x86_64 GNU/Linux
```

```
$ ./monerod 
2018-05-17 18:30:55.291	    7fea13d59bc0	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-release)
```

## moneromooo-monero | 2018-05-20T14:11:01+00:00
Believed fixed by https://github.com/monero-project/monero/pull/3828 (but it's hard to repro to make sure).

## johnalanwoods | 2018-06-07T18:12:50+00:00
Had this issue on 0.12.2: 

macOS High Sierra 10.13.5

    2018-06-07 18:10:30.988	[P2P3]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:400	internal error: try to insert duplicate iterator in key_image set


## moneromooo-monero | 2018-06-07T19:30:24+00:00
With #3828 ?

## johnalanwoods | 2018-06-07T19:42:23+00:00
Sorry my mistake, I mistook that #3828 was already in 0.12.2 - apologies.

## fenidik | 2018-06-19T12:23:49+00:00
Same. 0.12.2

## lh1008 | 2018-06-22T01:24:19+00:00
Hi, 

Same here(0.12.2) with aditional message of BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1596549.
Started syncing from scratch 2 weeks ago.

Linux Ubuntu 16.04 LTS

![errortxpool](https://user-images.githubusercontent.com/7443480/41753084-f77f409e-7590-11e8-8d51-ae57dffd59d4.png)



## moneromooo-monero | 2018-06-25T22:02:01+00:00
+resolved

# Action History
- Created by: ordtrogen | 2018-04-05T14:53:09+00:00
- Closed at: 2018-06-25T22:56:59+00:00
