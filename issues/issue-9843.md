---
title: 'Failed to sign multisig tx: This signature was made with stale data: export
  fresh multisig data, which other participants must then use'
source_url: https://github.com/monero-project/monero/issues/9843
author: woodser
assignees: []
labels: []
created_at: '2025-03-17T10:50:21+00:00'
updated_at: '2025-09-08T21:20:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm observing a pattern with multisig wallets, where if importing multisig info fails the first time (e.g. `no connection to daemon`), then it succeeds the second time, then it'll cause an error when signing a multisig tx:

```
-35: Failed to sign multisig tx: This signature was made with stale data: export fresh multisig data, which other participants must then use
```


The issue might appear if there's an error syncing with the daemon here: https://github.com/monero-project/monero/blob/f90a267fa34bad095d7e8ba72ee78f2a63f37df6/src/wallet/wallet2.cpp#L14857

In that case I have to create the multisig tx anew, and then have the original peer complete the signing

Hoping someone might have an idea of what could cause this "stale data" error if `import_multisig_info` is called twice because the first request fails. Seems to be a bug of some kind.

# Discussion History
## rbrunner7 | 2025-03-23T15:56:04+00:00
I tried to reproduce. I used the CLI wallet with 2/2 multisig. To provoke an error when attempting `import_multisig_info` I stopped the daemon before executing the command.

In about 20 attempts I had the error only once or twice.

I suspect that there is some additional, not yet recognized condition that is necessary to trigger the error, beyond merely attempting the import first with an error and then repeating it.

The mechanism that detects "stale data" always was, and to this day is, more or less a complete mystery to me. Despite browsing multisig-related code in `wallet2.cpp` I don't have the slightest idea about the general approach behind that detection. There is talk about some "nonces" in comments, but no idea what they are, how they are calculated, and why they would allow to watch over correct execution of multisig steps.

That's not a good position to start an investigation ...

## woodser | 2025-03-24T15:28:35+00:00
A PR is open to fix this from @SNeedlewoods: https://github.com/monero-project/monero/pull/9863

## elibroftw | 2025-09-08T21:20:50+00:00
I encountered this today when using Haveno. I had turned off my VPN while a trade was open. I was the buyer as a maker. When the other party clicked payment confirmed I think something went wrong. 

# Action History
- Created by: woodser | 2025-03-17T10:50:21+00:00
