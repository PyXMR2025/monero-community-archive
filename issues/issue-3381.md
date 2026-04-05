---
title: Segmentation fault on v6.20.0 when API HTTP enabled
source_url: https://github.com/xmrig/xmrig/issues/3381
author: yueehndnx
assignees: []
labels: []
created_at: '2023-12-14T02:22:14+00:00'
updated_at: '2023-12-17T12:39:01+00:00'
type: issue
status: closed
closed_at: '2023-12-17T12:39:00+00:00'
---

# Original Description
Linux builds v6.20.0 when HTTP API enabled in JSON config caused to Segmentation fault when Ghostrider algo benchmark started
Reproduced on:

compact build from the repository
Works fine on the original XMRig. So the most obvious thing here is that there is a conflict with benchmarking

# Discussion History
## SChernykh | 2023-12-14T07:59:55+00:00
> Works fine on the original XMRig

You should probably report it to MoneroOcean, not here.

## yueehndnx | 2023-12-15T04:09:35+00:00
> > 在原始 XMRig 上运行良好
> 
> 您可能应该将其报告给 MoneroOcean，而不是在这里。

Getting this error in original xmrig

## SChernykh | 2023-12-15T21:30:15+00:00
> Works fine on the original XMRig

> Getting this error in original xmrig

You're contradicting yourself. Can you write how to trigger this error in the original XMRig?

# Action History
- Created by: yueehndnx | 2023-12-14T02:22:14+00:00
- Closed at: 2023-12-17T12:39:00+00:00
