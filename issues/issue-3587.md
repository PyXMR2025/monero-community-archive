---
title: Blockchain stops syncing
source_url: https://github.com/monero-project/monero-gui/issues/3587
author: t-anon
assignees: []
labels: []
created_at: '2021-06-23T04:38:42+00:00'
updated_at: '2023-01-18T06:11:08+00:00'
type: issue
status: closed
closed_at: '2023-01-18T06:11:07+00:00'
---

# Original Description
After initializing a new wallet, a couple of blocks sync and then sync stops.

```
GUI version: 0.17.2.2-937cb98 (Qt 5.12.8)
Embedded Monero version: 0.17.2.0-release
Wallet mode: Simple mode (bootstrap)OpenGL
```

# Discussion History
## selsta | 2021-06-23T04:40:03+00:00
Do you mean wallet scan or blockchain sync?

The lock is only visual so I doubt that it stops syncing.

## t-anon | 2021-06-23T04:52:10+00:00
Edited my post to reflect this. Looks like the syncing just... stops, after some time. Not sure what the cause is, could anyone help investigate?

## selsta | 2021-06-23T04:54:33+00:00
Does it continue if you wait?

## t-anon | 2021-06-23T04:57:03+00:00
No, it does not continue. I see there is a lot of network down, but the "Wallet Blocks Remaining" progress bar is stuck at ~124k in the GUI.

Running some commands:

```
>>> status
[6/23/21 12:54 AM] 2021-06-23 04:54:33.815 I Monero 'Oxygen Orion' (v0.17.2.0-release)
Height: 2389265/2389265 (100.0%) on mainnet, bootstrapping from REDACTED, local height: 1366064 (57.2%), not mining, net hash 2.47 GH/s, v14, 0(out)+0(in) connections
>>> status
[6/23/21 12:55 AM] 2021-06-23 04:55:39.541 I Monero 'Oxygen Orion' (v0.17.2.0-release)
Height: 2389265/2389265 (100.0%) on mainnet, bootstrapping from REDACTED, local height: 1370584 (57.4%), not mining, net hash 2.47 GH/s, v14, 0(out)+0(in) connections
```

It looks like there is progress but it's not reflected in the GUI.

## selsta | 2021-06-23T04:58:56+00:00
Does it continue if you click on the two arrow symbol in the top left corner?

## t-anon | 2021-06-23T05:00:55+00:00
I don't see such a symbol on the top left, but rather bottom right. I clicked it but nothing happened.

## selsta | 2021-07-02T01:12:57+00:00
Does this issue still happen?

## q7nm | 2021-07-12T16:47:56+00:00
> Does this issue still happen?

Yes

## selsta | 2021-07-13T22:21:50+00:00
@BigmenPixel0 Please open a separate issue with more details.

## q7nm | 2021-07-14T06:43:37+00:00
> @BigmenPixel0 Please open a separate issue with more details.

Now the problem is gone, but maybe the tor proxy was to blame for this?

## selsta | 2021-07-14T06:45:56+00:00
Possible, not clear.

## selsta | 2023-01-18T06:11:07+00:00
It seems that you were using simple mode (bootstrap) which can connect you to a bad remote node. If you continue to have issues I'd recommend to select advanced mode instead.

# Action History
- Created by: t-anon | 2021-06-23T04:38:42+00:00
- Closed at: 2023-01-18T06:11:07+00:00
