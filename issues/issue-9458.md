---
title: 'Naming for the Implemention '
source_url: https://github.com/monero-project/monero/issues/9458
author: HardenedSteel
assignees: []
labels:
- low priority
- proposal
- discussion
created_at: '2024-08-27T07:49:24+00:00'
updated_at: '2024-10-01T08:10:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
We need to make disambiguation for the Monero C++ implementation. It causes confusion between the implementation(s) and the network.

This will also be useful when Cuprate is released.

So how we should refer to the Monero C++ implementation? Monerod? Monero Core? MoneroC++?

# Discussion History
## SyntheticBird45 | 2024-08-27T09:28:08+00:00
In general, the reference implementation of a cryptocurrency is called ***<Cryptocurrency> Core***. And *Core* generally include node + wallet. So I think there is no disambiguation:

Core software is the reference implementation of monero, which includes *monerod* (The monero daemon/node) and monero-wallet-cli/gui (The reference wallet implementation)

I wouldn't be worry about cuprate since the deamon will be named `cuprated`. get it? cuprate daemon. Hard to be confused.

## HardenedSteel | 2024-08-27T10:15:57+00:00
monerod is still confusing, Monero is the currency's name not the software implementation of Monero. These both should be disambiguated

Referring as Monero Core sounds good to me.

Look at this blog post; [Monero 0.18.3.4 'Fluorine Fermi' released](https://www.getmonero.org/2024/08/20/monero-0.18.3.4-released.html). Releasing Monero? How this is even possible? We should say Monero core 0.18.3.4 released and when cuprate releases in future we would say Cuprate x.x.x released.

Monero GUI and CLI also should be named but these are different issues.

# Action History
- Created by: HardenedSteel | 2024-08-27T07:49:24+00:00
