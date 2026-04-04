---
title: '[vulnerability] Multisig view secret key disclosure'
source_url: https://github.com/monero-project/monero/issues/3389
author: naughtyfox
assignees: []
labels: []
created_at: '2018-03-12T13:21:53+00:00'
updated_at: '2018-03-15T14:21:34+00:00'
type: issue
status: closed
closed_at: '2018-03-13T09:30:08+00:00'
---

# Original Description
# Problem
I've been discovering monero multisignature implementation and figured out that initial keys exchange round is insecure. 

Since multisig view secret key is calculated as follows:
```
a = H(a1) + H(a2) + ... + H(an)
```
the eavesdropper (insecure connection, malicious multisig wallet service, etc) can restore view secret key just summing hashes.

# Proof-of-Concept
There is quick poc code (modified `monero-gen-trusted-multisig` utility): https://github.com/naughtyfox/monero/blob/view-key-disclosure/src/gen_multisig/gen_multisig.cpp#L133-L144 (you may build it and run by yourself)

Example output:
```
$ ./bin/monero-gen-trusted-multisig --filename-base=msig --scheme=2/3
This program generates a set of multisig wallets - use this simpler scheme only if all the participants trust each other

Monero 'Helium Hydra' (v0.11.1.0-master-e9f41e40)
Logging to ./bin/monero-gen-trusted-multisig.log
Generating 3 2/3 multisig wallets
Enter password for new multisig wallets: 
Confirm password: 
generating wallet msig-1
input view key: 3dfbfca02607bb3dece4d56e6476f5a3a1b56c010f296f3e5d7bc6964d136b00
input view key: 8aca9dd4276e64e8123557d0432ab1cf568e6fa52ec9e522aa0844363fbc4201
my view secret key: 0d306c058622c832c8e2a0fc90c40a4b04e439f1be1fd69b767965d6a6d80c09
generated view secret key: af9558f8c3e036a088f4d5c66050e5117d3ce35aff2faa8c32cf4ea7d1f49304

generating wallet msig-2
input view key: e8cfbd82756b177a89daa887b8af3e9e84f806b4c13d552b2b4b44da4425e602
input view key: 8aca9dd4276e64e8123557d0432ab1cf568e6fa52ec9e522aa0844363fbc4201
my view secret key: 31fac06b3a61b45c391c822ebe4cfd371471ed4e81e74df9c069b4d240a34d0e
generated view secret key: af9558f8c3e036a088f4d5c66050e5117d3ce35aff2faa8c32cf4ea7d1f49304

generating wallet msig-3
input view key: e8cfbd82756b177a89daa887b8af3e9e84f806b4c13d552b2b4b44da4425e602
input view key: 3dfbfca02607bb3dece4d56e6476f5a3a1b56c010f296f3e5d7bc6964d136b00
my view secret key: eee198786b09195362b6b4968df1b5082cb4ec36b71ffe50169610b9ccc0c301
generated view secret key: af9558f8c3e036a088f4d5c66050e5117d3ce35aff2faa8c32cf4ea7d1f49304

restoring keys
using key: 3dfbfca02607bb3dece4d56e6476f5a3a1b56c010f296f3e5d7bc6964d136b00
using key: 8aca9dd4276e64e8123557d0432ab1cf568e6fa52ec9e522aa0844363fbc4201
my key: e8cfbd82756b177a89daa887b8af3e9e84f806b4c13d552b2b4b44da4425e602
restored view secret key: af9558f8c3e036a088f4d5c66050e5117d3ce35aff2faa8c32cf4ea7d1f49304

using key: e8cfbd82756b177a89daa887b8af3e9e84f806b4c13d552b2b4b44da4425e602
using key: 8aca9dd4276e64e8123557d0432ab1cf568e6fa52ec9e522aa0844363fbc4201
my key: 3dfbfca02607bb3dece4d56e6476f5a3a1b56c010f296f3e5d7bc6964d136b00
restored view secret key: af9558f8c3e036a088f4d5c66050e5117d3ce35aff2faa8c32cf4ea7d1f49304

using key: e8cfbd82756b177a89daa887b8af3e9e84f806b4c13d552b2b4b44da4425e602
using key: 3dfbfca02607bb3dece4d56e6476f5a3a1b56c010f296f3e5d7bc6964d136b00
my key: 8aca9dd4276e64e8123557d0432ab1cf568e6fa52ec9e522aa0844363fbc4201
restored view secret key: af9558f8c3e036a088f4d5c66050e5117d3ce35aff2faa8c32cf4ea7d1f49304
```

Here you can see `restored view secret key` is `af9558f8c3e036a088f4d5c66050e5117d3ce35aff2faa8c32cf4ea7d1f49304` the same as each of wallets owns.

# Consequences
Knowing view secret and spend public keys `(a, B)` an attacker may see incoming money transfers to particular wallet which leads to lower privacy level.

# Proposed Solution
To make key exchange round secure monero needs to implement key exchange protocol such as `ECDH` for N participants (it may require additional key exchange rounds).


# Discussion History
## moneromooo-monero | 2018-03-12T17:21:15+00:00
There's a warning when running prepare_multisig telling you about it fwiw.
If you start assuming Eve knows the start secret keys, then yes, she can know that.
PK crypto could be used if the participants know each other ('s public keys). At the moment, just the generic one is done.

## Hueristic | 2018-03-12T17:22:27+00:00
Hit BP next please. :)

## naughtyfox | 2018-03-13T09:30:08+00:00
ok, i close this issue since it's assumed use case

## anonimal | 2018-03-14T19:02:36+00:00
@naughtyfox don't be a tool, use [responsible disclosure](https://github.com/monero-project/monero#vulnerability-response). If you don't, you won't eligible for bounty.

## naughtyfox | 2018-03-15T14:21:34+00:00
@anonimal thank you for advice. since it's pre-release concern i decided to post it here for some reason. hope to fit in the community soon

# Action History
- Created by: naughtyfox | 2018-03-12T13:21:53+00:00
- Closed at: 2018-03-13T09:30:08+00:00
