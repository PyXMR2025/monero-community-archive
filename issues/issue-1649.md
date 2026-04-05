---
title: what's going on, falling hash?
source_url: https://github.com/xmrig/xmrig/issues/1649
author: klesilva
assignees: []
labels: []
created_at: '2020-04-19T11:00:19+00:00'
updated_at: '2020-04-19T19:02:19+00:00'
type: issue
status: closed
closed_at: '2020-04-19T19:02:18+00:00'
---

# Original Description
I'm mining normally, after 1 hour drastically drops the hash, when devfee hash starts back to normal, as soon as it ends it falls again and does not return to normal. Windows 10 Pro, R73800X 32GB DDR4 3600Mhz, CPU usage is normal. before I was using the R72700X and that didn't happen.



![Capturar](https://user-images.githubusercontent.com/40640747/79685971-06e6cd00-8213-11ea-8b92-c34f9830c88f.PNG)


# Discussion History
## trasherdk | 2020-04-19T13:51:31+00:00
Looks like you are mining `cn/r`.

## xmrig | 2020-04-19T14:22:28+00:00
Nicehash doesn't support algorithm negotiation, so you must specify `algo` option and must not use `coin` option, configuration should looks like `"algo": "rx/0", "coin": null,`.

Your current configuration worked fine in the past because only Monero used the `rx/0` algorithm, but now QRL also uses `rx/0` and people use nicehash to mine it. Using the `algo` option is the golden rule for nicehash, you can't control what coin mined.
Thank you.


## klesilva | 2020-04-19T17:23:35+00:00
I understand I will make the modification and see the problem again

## klesilva | 2020-04-19T19:02:18+00:00
@xmrig thanks for the help, more than 2 hours passed the problem did not occur again.

# Action History
- Created by: klesilva | 2020-04-19T11:00:19+00:00
- Closed at: 2020-04-19T19:02:18+00:00
