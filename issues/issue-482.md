---
title: Issues experienced building in Subgraph OS (based on Debian stretch) + fixes
source_url: https://github.com/monero-project/monero-gui/issues/482
author: dma
assignees: []
labels: []
created_at: '2017-02-20T00:13:11+00:00'
updated_at: '2017-02-20T03:22:17+00:00'
type: issue
status: closed
closed_at: '2017-02-20T03:22:17+00:00'
---

# Original Description
We're looking at packaging the Monero GUI wallet and monerod for [Subgraph OS](https://subgraph.com). As a first step, I've written a guide to building and running them in SGOS:

https://subgraph.com/sgos/documentation/monero/

I'd appreciate feedback on this guide!

During my experience I encountered a couple of issues that are documented in the guide along with workarounds. Here is the issue filing for both of them if you want to fix them here:

1. The '&' character in this [line](https://github.com/monero-project/monero-core/blob/master/translations/monero-core_de.ts#L500) produces a parsing failure during the localization step of the build, causing the build to fail. It's here;

https://github.com/monero-project/monero-core/blob/master/translations/monero-core_de.ts#L500

2. Building in Subgraph OS requires -ldl to be included in the list of libraries when monero-wallet-gui is linked. It's not there by default, resulting in an unresolved symbol from glibc and build failure. I added it to this section here (-ldl at the bottom of the list), and then the build completed successfully and produced a usable executable:

https://github.com/monero-project/monero-core/blob/master/monero-wallet-gui.pro#L90

Thanks.

# Discussion History
## danrmiller | 2017-02-20T01:50:43+00:00
Cool, I'll give your guide a try. The two issues you mention are fixed in Pull Requests #477 and #478 

## dma | 2017-02-20T03:22:16+00:00
Didn't see those, should have checked. Thanks!

# Action History
- Created by: dma | 2017-02-20T00:13:11+00:00
- Closed at: 2017-02-20T03:22:17+00:00
