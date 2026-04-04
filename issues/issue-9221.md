---
title: '`set priority` appears broken'
source_url: https://github.com/monero-project/monero/issues/9221
author: selsta
assignees: []
labels:
- bug
- wallet
created_at: '2024-03-08T03:07:39+00:00'
updated_at: '2024-03-09T01:27:08+00:00'
type: issue
status: closed
closed_at: '2024-03-09T01:27:08+00:00'
---

# Original Description
```
[wallet 431t1S]: set priority 2
Wallet password: 
[wallet 431t1S]: set
priority = 2 (normal)
[wallet 431t1S]: address
0  431t1SuHXJNE3U5GhqoGCw2t5XpAZRwyX2h3AfG5BKzkZuYWrVaEyyRdHGaXUMLhiCAc5mF5EaLN9cqie64a5PA3TXTiw3g  Primary address (used)
[wallet 431t1S]: transfer 431t1S 0.01
Wallet password: 
There is currently a 37 block backlog at that fee level. Is this okay?  (Y/Yes/N/No): n
Error: transaction cancelled.
```

# Discussion History
## SChernykh | 2024-03-08T07:20:47+00:00
It happens because of this line: https://github.com/monero-project/monero/blob/master/src/simplewallet/simplewallet.cpp#L6320
```
priority = m_wallet->adjust_priority(priority);
```
So #9219 should fix this

## SChernykh | 2024-03-08T07:25:54+00:00
After looking at the code a bit more, shouldn't this line assign to the default priority, not 0? https://github.com/monero-project/monero/blob/master/src/simplewallet/simplewallet.cpp#L6316
```
uint32 priority = 0;
```
should be

```
uint32 priority = m_wallet->get_default_priority();
```


## SChernykh | 2024-03-08T07:30:25+00:00
@selsta you can just add the one-line fix above to #9219

# Action History
- Created by: selsta | 2024-03-08T03:07:39+00:00
- Closed at: 2024-03-09T01:27:08+00:00
