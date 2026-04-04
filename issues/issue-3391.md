---
title: Warn about transactions using same decoys for all inputs ?
source_url: https://github.com/monero-project/monero/issues/3391
author: MoroccanMalinois
assignees: []
labels: []
created_at: '2018-03-13T06:02:05+00:00'
updated_at: '2018-03-14T17:18:46+00:00'
type: issue
status: closed
closed_at: '2018-03-14T17:18:46+00:00'
---

# Original Description
Found `311` transactions using the exact same `5` fake rct outs for all inputs. That's statistically impossible, which makes them easily traceable. So i wonder if the wallet should warn about these kind of transactions, i.e. composed of multiple rct inputs and using a _mostly_ overlapping set of decoys. 

Example of transactions:
- [27c9ea7c09ce5812664dfd118835f814a32ad984bb53f2b8040b895e3df8d0e9](https://xmrchain.net/search?value=27c9ea7c09ce5812664dfd118835f814a32ad984bb53f2b8040b895e3df8d0e9)
- [8772d5d909ee0bbc8fd1b5367904f66bbc1ee3b9304b23076d7c942b485536d7](https://xmrchain.net/search?value=8772d5d909ee0bbc8fd1b5367904f66bbc1ee3b9304b23076d7c942b485536d7)
- [a18c6c0a76585945d4f36ab0e1b3c982fd64098aa67be1dd791da999fac70455](https://xmrchain.net/search?value=a18c6c0a76585945d4f36ab0e1b3c982fd64098aa67be1dd791da999fac70455)

Now, just for the fun, here is the last part of the distribution of inputs referencing, which shows how much these `5` txo stands out (total 4902154 RCT outputs as of block < 1525000)

Number of time referenced |  Number of outputs
-----------------------------------|--------------------------
17|49
18|13
19|2
20|2
2301|1
2302|1
2305|3

Here is the distribution of these `311` transactions over time
![untitled](https://user-images.githubusercontent.com/22608168/37322231-29d21d62-2674-11e8-8987-24a3e1327cfe.png)

(Too stupid for a malicious activity, i vote for a bug in a new "service" :) )
 

# Discussion History
## moneromooo-monero | 2018-03-13T09:40:49+00:00
If it's some other code doing this, what would we do in the wallet which doesn't create those ?

Anyway, if you feel like adding the code you used to the new monero-blockchain-blackball tool, that'd be nice :)

## MoroccanMalinois | 2018-03-13T23:39:40+00:00
> If it's some other code doing this, what would we do in the wallet which doesn't create those ?

I thought, maybe, we should print a warning for the receiver. Just felt like i'd like to know if i was the receiver of one of these tx (TBH, i checked and i'm not :) ), but maybe it's too much work for a negligible case.

> if you feel like adding the code you used to the new monero-blockchain-blackball tool

Sorry mooo, i'm using a method, inb4, that could be fairly qualified as idiotic in this context :). For my job, i'm benchmarking "big data" frameworks & back-ends & blablabla , just doing it on Monero and Bitcoin's data instead of some dummy data. So, it's really just a bunch of ugly SQL queries on an export of the blockchain inserted in some back-end (or not, can use a simple CSV), using [Apache Zeppelin](https://zeppelin.apache.org/) as front-end

## moneromooo-monero | 2018-03-14T10:28:01+00:00
The wallet would have to track all rings. Possible, but it'd take... a lot of memory. Maybe 200 MB currenly to store the compressed rings so you can lookup when you receive a new tx. Or ask the daemon each time, but that leaks which tx is yours.

## MoroccanMalinois | 2018-03-14T17:18:46+00:00
Not worth the troubles. Closing

# Action History
- Created by: MoroccanMalinois | 2018-03-13T06:02:05+00:00
- Closed at: 2018-03-14T17:18:46+00:00
