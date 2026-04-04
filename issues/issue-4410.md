---
title: Was the monero testnet forked??
source_url: https://github.com/monero-project/monero/issues/4410
author: lhfly5201314
assignees: []
labels:
- invalid
created_at: '2018-09-21T02:08:22+00:00'
updated_at: '2018-09-25T23:24:52+00:00'
type: issue
status: closed
closed_at: '2018-09-25T23:24:52+00:00'
---

# Original Description
Hey,guys!What's wrong with the testnet?Is it forked again?
I found the block height is smaller than two days before,
Now,the block height is about 1063580,is 1160000+ two days before .
And the daemon gives some warnings:
### **peer claims higher version that we think (9 for 1063551 instead of 8) - we may be forked from the network and a software upgrade may be needed.**

Should I delete the old blockchain data and sync from the scratch?
I am using the version0.12.3.0 daemon.
Thanks!


# Discussion History
## Gingeropolous | 2018-09-21T03:34:20+00:00
yeah, delete and sync from scatch

## moneromooo-monero | 2018-09-21T08:45:23+00:00
You can also pop blocks till 1057000 with your current software, then pull master, and let the new version sync.

## lhfly5201314 | 2018-09-21T08:57:17+00:00
> yeah, delete and sync from scatch

Thanks,friend!

## lhfly5201314 | 2018-09-21T08:59:53+00:00
> You can also pop blocks till 1057000 with your current software, then pull master, and let the new version sync.

Hi,friend!You say "pull master",you mean  I should update my daemon version too?

## moneromooo-monero | 2018-09-21T09:28:10+00:00
Yes.

## moneromooo-monero | 2018-09-22T18:34:14+00:00
And it's going to need popping again very soon. Probably the last time short term.

## moneromooo-monero | 2018-09-25T23:23:28+00:00
Not a bug, so closing.

+invalid


# Action History
- Created by: lhfly5201314 | 2018-09-21T02:08:22+00:00
- Closed at: 2018-09-25T23:24:52+00:00
