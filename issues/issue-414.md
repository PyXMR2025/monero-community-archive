---
title: GUI sporadic "monero-core" is not responding when sending
source_url: https://github.com/seraphis-migration/monero/issues/414
author: j-berman
assignees: []
labels: []
created_at: '2026-06-09T21:42:20+00:00'
updated_at: '2026-06-09T21:43:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Reported by u/FiatDemise in the stressnet channel.

Context:

```
FiatDemise: Hi, I often see a "monero-core" is not responding message when sending from one fcmp wallet to another. I click Wait and it continues fine. I am using the beta v2.0 linux x64 GUI on Ubuntu 24.04.4 LTS. My pc has a Ryzen 9 7900 and is pretty much idle when sending.
jberman: do you know if these are large txs spending a lot of inputs, or normal? Is this something that recently started happening or something you've seen consistently?
FiatDemise: Don't know where to look to see number of inputs. But I can tell you that both my sender and receiver wallets have under 50 transactions. I first noticed it occurring yesterday.
ofrnxmr@ofrnxmr:xmr.mx: Wre you sending full balance?
Does the issue still happen if sending an small amount smaller than your incoming transactions?
FiatDemise: nope, small amounts ranging from .001 to 1
ofrnxmr@ofrnxmr:xmr.mx: thats ehat you're sending, or what you received ?
FiatDemise: both
ofrnxmr@ofrnxmr:xmr.mx: If you have a bunch of 0.001 inputs, and are sending 1xmr, then it may be using a lot of inputs.

if you are sending 0.001, then it shouldnt be an issue
I'd switch to wallet-cli, increase log level to 2, and build the same transaction to see how long it takes & what the log shows during that time
jberman: you can also start the GUI via terminal and enable log level 2 in settings, wallet logs should print to terminal
because it's something just noticed yesterday, it may be related to the larger pool. Rucknium also noted increased RPC response times while the wallet was ingesting the pool
wallet RPC* response times
the refresh loop currently blocks while ingesting the larger pool, and could block other actions the GUI is expecting quicker returns on
```

# Discussion History
# Action History
- Created by: j-berman | 2026-06-09T21:42:20+00:00
