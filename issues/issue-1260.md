---
title: Option (--retries) not being honored when  Unknown/unsupported algorithm detected.
source_url: https://github.com/xmrig/xmrig/issues/1260
author: nssy
assignees: []
labels: []
created_at: '2019-11-04T16:29:26+00:00'
updated_at: '2019-12-22T19:28:59+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:28:59+00:00'
---

# Original Description
Hi,
Have notice that when algo is set and pool does not support that algo, xmrig keeps retrying indefinitely with the error. 
```
[2019-11-04 19:20:32.080] [mypool.com:5555] failed to parse field "seed_hash" required by RandomX
[2019-11-04 19:20:32.080] [mypool.com:5555] login error code: 7
```
This happens when only one pool is present.
example `xmrig -t 1 -a 'rx/0' -o mypool.com:5555 -u my_wallet -p x --retries=5`

The problem is that it displays this 5 times but continues trying to reconnect indefinitely in the background.
Is this the intended behavior with the `--retries=N`?
We run a small monero pool  and this has become noticeable after guys started updating for randomx (**xmrig 4.4.0-beta** in particular what was used) but set the wrong algo. 
So in the last couple of days we have been getting an unusually large amount of connections from just a couple of miners (_for this case xmrig 4.4.0-beta with algo wrongly set to rx/0_).
Of course this is human error caused by the miner but if they leave xmrig running this way, it continues to try to connect indefinitely eating up lots of tcp sockets on the pool without doing any actual work.
We were hoping that xmrig could **just honor the retries option (--retries=N)** and stop attempting to re-connect after the specified number of retries I.E if it encounters the above error, 
Or maybe just run in donate mode or something.

# Discussion History
## xmrig | 2019-11-05T15:48:08+00:00
`retries` is number of retries before miner try use another pool (failover strategy) if it will be finite miner never back to primary pool. For make retries less aggressive there is another option `--retry-pause`.

If you use own pool wrong algorithm is not a issue  https://xmrig.com/docs/extensions/algorithm-negotiation.

## nssy | 2019-11-06T08:23:36+00:00
Duly noted. 
Makes sense from your point of view.
Will try and explore other ways of mitigating this pool side.
Thanks for the reply.

# Action History
- Created by: nssy | 2019-11-04T16:29:26+00:00
- Closed at: 2019-12-22T19:28:59+00:00
