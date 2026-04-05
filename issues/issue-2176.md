---
title: Please provide a helm chart
source_url: https://github.com/xmrig/xmrig/issues/2176
author: vanthome
assignees: []
labels:
- wontfix
created_at: '2021-03-12T07:48:53+00:00'
updated_at: '2021-04-12T13:59:55+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:59:49+00:00'
---

# Original Description
Please provide a helm chart for xmrig, ideally with a diversity rule so that tow instances are not started on the same machine.

# Discussion History
## Lonnegan | 2021-03-12T08:07:47+00:00
Why not? I'm mining Monero with the CPU and Haven with the GPU. Therefore I have to start two instances of xmrig. 

## vanthome | 2021-03-12T09:00:26+00:00
Good point in that case it should be configurable. The point is, if I just start a certain number of replicas (let's say for just CPU mining), K8s will have no problem scheduling them on the same machine, which is ofc not desirable. there are primitives in K8s however to control this. It must just be exposed through the helm chart.

## SChernykh | 2021-03-12T09:13:10+00:00
XMRig doesn't provide Kubernetes container images in releases, so there is no point to ask anything related.

## vanthome | 2021-03-25T20:18:19+00:00
Good point but then they should do that, given that they are paid for this, I think it's fair to ask for it.

# Action History
- Created by: vanthome | 2021-03-12T07:48:53+00:00
- Closed at: 2021-04-12T13:59:49+00:00
