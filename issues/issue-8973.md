---
title: Latest release crashes on Orange Pi 3 LTS (Ubuntu)
source_url: https://github.com/monero-project/monero/issues/8973
author: tkalfaoglu
assignees: []
labels: []
created_at: '2023-08-15T15:39:40+00:00'
updated_at: '2023-09-21T17:15:10+00:00'
type: issue
status: closed
closed_at: '2023-09-21T17:15:10+00:00'
---

# Original Description
Hi the new version runs for 5 minutes and then crashes. I downloaded its binary because it takes > 12 hours to compile it on Orange Pi 3..  

# /usr/local/bin/monerod --restricted-rpc --block-sync-size 30 --confirm-external-bind --config-file /home/turgut/.bitmonero/monerod.conf 

2023-08-15 15:36:05.238 I +++++ BLOCK SUCCESSFULLY ADDED
2023-08-15 15:36:05.238 I id:   <602171bbcaebc215c0ba4043fc535faa813aa959faf052bb432dc2554d7e0aa4>
2023-08-15 15:36:05.238 I PoW:  <ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff>
2023-08-15 15:36:05.238 I HEIGHT 1325340, difficulty:   9539369511
2023-08-15 15:36:05.238 I block reward: 7.464053370603(7.386054570603 + 0.077998800000), coinbase_weight: 95, cumulative weight: 66391, 3(2/0)ms
2023-08-15 15:36:05.244 I Transaction added to pool: txid <cefa9358411b1ebaafc34dcd612955d889818a7e90e815cdccfdb85ce927b469> weight: 12924 fee/byte: 2.32126e+06
2023-08-15 15:36:05.245 I Transaction added to pool: txid <5835908a0f754026d53ebc172f5ff2246a61d66af337d6de33fba0d42f9e9446> weight: 12958 fee/byte: 2.31517e+06
2023-08-15 15:36:05.248 I Transaction added to pool: txid <601a2330cee8ac05b7c937d1ab1a16b5d8025cb531ecb7ad55d92b9c46dd9e52> weight: 70009 fee/byte: 1.16477e+06
2023-08-15 15:36:05.250 I Transaction added to pool: txid <16b5a599d49155d8bee55a051e7f15e5c283da10ffcd1c378efbe1e7aae67052> weight: 70010 fee/byte: 1.16475e+06
2023-08-15 15:36:05.252 I Transaction added to pool: txid <5cdebe69f6910065214796da732f66a60282aef1af686502cd33039d400e8516> weight: 76317 fee/byte: 1.16141e+06
2023-08-15 15:36:05.253 I Transaction added to pool: txid <285930cbc3a0589cbd643a431b931215695ae3ab522e6e950636b2a9915838a5> weight: 13256 fee/byte: 1.15898e+06
2023-08-15 15:36:05.254 I Transaction added to pool: txid <8a1fc26c4cdbb77537473d76f70b6eb48a583186ca514f45f2cc36611b2795af> weight: 51093 fee/byte: 1.15652e+06
malloc(): invalid size (unsorted)
Aborted

turgut@orangepi3-lts:~/.bitmonero$ ulimit
unlimited




# Discussion History
## selsta | 2023-08-15T22:54:24+00:00
Can you post the specs of your hardware? Which version did work for you previously?

Also which operating system do you have installed?

## selsta | 2023-09-21T17:15:10+00:00
Closing due to lack of reply. If you continue to have issues please comment or create a new issue.

# Action History
- Created by: tkalfaoglu | 2023-08-15T15:39:40+00:00
- Closed at: 2023-09-21T17:15:10+00:00
