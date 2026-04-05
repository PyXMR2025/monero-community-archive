---
title: xmrig-6.12.2-macos-arm64 has cn/0 disabled like linux?
source_url: https://github.com/xmrig/xmrig/issues/2443
author: juanpc2018
assignees: []
labels: []
created_at: '2021-06-14T13:59:22+00:00'
updated_at: '2021-06-14T16:53:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
xmrig-6.12.2-macos-arm64 has cn/0 disabled like linux?

I had to download less than v3.0 to use cn/0 in linux x86_64

Cn/0 is dissabled and imposible to activate,
Xmrig A.i. rewrites .json disabling cn/0

Is thete a way to compile v2.x in M1 ?

# Discussion History
## SChernykh | 2021-06-14T14:09:36+00:00
cn/0 is an ASIC mined algorithm, so it's disabled by default. You can manually remove `"cn/0": false,` from config.json to enable it.

## juanpc2018 | 2021-06-14T14:58:42+00:00
i know .json has a false / true  cn/0
but does Not work,
A.I. rewrites back to false.
when mining, complains it´s disabled, and refuses to mine & activate.
the code is broken or was removed.

i know cn/0 is ASIC,
but... 
hypothetical situation:
a meteorite strikes the only ASIC factory
or... a Large solar Flare,
or... ASIC miners are banned by All Govs. World Wide, manufacturing, shipping, and use becomes illegal.
having an ASIC miner = Jail.
or... price of XYZ coin becomes too high... $1million dollar each XYZ coin.

from the ASIC manufacturer POV, 
Has No logic to sell ASIC miners,
is much more profitable Not to sell ASIC miners,
does Not sell replacement parts,
does Not sell New ASIC miners.

has total control of the coin.
totally centralized manufacturing.

that´s Not the original idea of Satoshi Nakamoto 
that goes against a Decentralized environment.


the same idea, "is Not fast enough = pointless"
was the reason why BTC developers REMOVED CPU wallet mining since v0.10 from Bitcoin Wallet,
CPU wallet mining was slow? yes, but allowed to send with 0-fee while mining was true.

like a waterfall / chian reaction, 
99% of BTC mutations removed also the code, LiteCoin, DOGEcoin, etc...

the result? 
BTC has the highest miner fees.
https://bitinfocharts.com/comparison/transactionfees-btc-eth-ltc-bch-xrp-bsv-etc-xmr-doge-btg.html#log&1y

No 0-Fee? disincentive / discourage people from making small transactions 
= small BTC owners lose more %, only people with large transactions are Not affected by high miner fee.

No 0-Fee discourage / disincentive having a Node Wallet.
No Node Wallet? = Vulnerable to 51% attack.
https://bitnodes.io/

is Not about FAST
it´s about Fail Safe 
it´s about a Decentralized environment.
a Centralized environment is doom, 
goes against all original ideas of Satoshi Nakamoto.

it´s a chain reaction.
a Tower of Cards,

"don´t put all eggs in 1 basket." also apply for miners.

## SChernykh | 2021-06-14T15:26:24+00:00
Correction: use the same values for `cn/0` as you have for `cn` in the generated config.json, for example:
```
        "cn/0": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
        ],
```
This way it works.

## Spudz76 | 2021-06-14T16:53:19+00:00
Or, `"cn/0": "cn",` is what I use

# Action History
- Created by: juanpc2018 | 2021-06-14T13:59:22+00:00
