---
title: --nicehash What is the flag?
source_url: https://github.com/xmrig/xmrig/issues/37
author: RemezW
assignees: []
labels: []
created_at: '2017-07-11T13:05:17+00:00'
updated_at: '2017-07-19T23:58:12+00:00'
type: issue
status: closed
closed_at: '2017-07-19T23:58:12+00:00'
---

# Original Description
Hello! What is the flag for? 
What is the difference between:

> xmrig.exe -o stratum+tcp://cryptonight.eu.nicehash.com:3355 -u WALLET.1 -p x -k

and

> xmrig.exe -o stratum+tcp://cryptonight.eu.nicehash.com:3355 -u WALLET.1 -p x -k **--nicehash**

Do I need to use this flag if I use nicehash? Thank you.


# Discussion History
## xmrig | 2017-07-11T13:26:11+00:00
In that case no difference, because it detected from pool url (nicehash.com), explicitly specify `--nicehash` need only if detection by url may failed, for example connect by IP address or stratum proxy.

Nicehash have little difference in protocol, that need special handle, otherwise all shares will be invalid.
Also nicehash does not support `-k` option.
Thank you.

# Action History
- Created by: RemezW | 2017-07-11T13:05:17+00:00
- Closed at: 2017-07-19T23:58:12+00:00
