---
title: Integrating XMRig into automated mining solutions
source_url: https://github.com/xmrig/xmrig/issues/1267
author: o2genum
assignees: []
labels: []
created_at: '2019-11-07T11:43:03+00:00'
updated_at: '2019-11-14T13:20:26+00:00'
type: issue
status: closed
closed_at: '2019-11-14T13:20:26+00:00'
---

# Original Description
I'm looking forward to integrating the XMRig into automated mining software, as a replacement for XMR-Stak, because the autoconf seems to be a bit better.

XMRig requires some changes for this to be possible, though. Here's what is necessary for easy integration into any kind.

<s>CLI args for selecting devices</s> DONE, thanks

### An API with per-device details

This is useful for displaying the per-device stats: hashrate, accepted/rejected shares (shares are useful as a coarse "health status" for quickly detecting misbehaving devices):

- <s>per-device hashrate</s> DONE
- per-device shares

```
"devices": [
{
"type": "CPU"
"name": "Intel Something",
"hashrate": 255,
"accepted_shares": 3,
"rejected_shares": 1
},
{
"type": "GPU",
"bus_id": "0000:02:00.0",
"name": "GIGABYTE GeForce GTX 1660 6GB",
"hashrate": 400,
"accepted_shares": 4,
"rejected_shares": 0
}
]
```

What do you think about these features? I would like to contribute a PR on this.

# Discussion History
## o2genum | 2019-11-14T13:20:15+00:00
Eveything except per-device shares is done in the latest release

# Action History
- Created by: o2genum | 2019-11-07T11:43:03+00:00
- Closed at: 2019-11-14T13:20:26+00:00
