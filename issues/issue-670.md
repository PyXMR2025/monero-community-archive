---
title: Missing payment in show_transfers
source_url: https://github.com/monero-project/monero/issues/670
author: moneromooo-monero
assignees: []
labels:
- invalid
created_at: '2016-02-15T20:49:00+00:00'
updated_at: '2017-09-30T09:42:21+00:00'
type: issue
status: closed
closed_at: '2017-09-30T09:42:21+00:00'
---

# Original Description
From villabacho on BCT (https://bitcointalk.org/index.php?topic=583449.msg13886614#msg13886614):

Hi, I just noticed that the amounts reported by the two simplewallet commands

1) "show_transfers in"
2) "incoming_transfers"

do not sum up to the same value. The second one sums to the same value as what "balance" says (I didn't have any outgoing transfers from this wallet),
while the first one is missing one transaction with two outputs.

I'd like to use the first of the to commands as it nicely groups the outputs of each transaction and tells me the block height as well,
but if it misses transactions I'll have to stick with the second one for now.

Anything that I should know? Is the "show_transfers" command kind of experimental?

Thanks!


# Discussion History
## bigreddmachine | 2016-04-05T17:24:05+00:00
I saw this issue and thought I'd add a question:

Why two different methods anyway? I could understand if "incoming_transfers" was an alias to "show_transfers in" but it's not... they call two separate things. Are they simply not equivalent calls? In which case, what's the difference?


## moneromooo-monero | 2016-04-14T20:45:59+00:00
One enumerates the outputs, the other enumerates the per tx sums (for received), or something else for sent, can't recall just now. so incoming_transfers is authoritative, in case of discrepancy.


## luigi1111 | 2016-12-15T18:00:47+00:00
@moneromooo-monero Is this still relevant? :)

## moneromooo-monero | 2017-01-22T11:55:28+00:00
Well... Assuming it wasn't user error, I don't think anything was fixed there, so it'd probably still be relevant. Stuff changed though, so it could be something got fixed "by mistake" :) If you want to close this, I'm fine with it.

## moneromooo-monero | 2017-09-21T07:45:09+00:00
While trawling through the bug list, I'm now reminded that show_transfers will only show transfers when scanned with code after this patch was merged. This could very well be the reason for the difference.

## moneromooo-monero | 2017-09-30T09:29:02+00:00
That was most likely that. There was also a more recent bug with the "refresh from height" being subject to underflow, but this got added later. Since I never saw this and the code seems to preclude it, I'll call it invalid.

+invalid


# Action History
- Created by: moneromooo-monero | 2016-02-15T20:49:00+00:00
- Closed at: 2017-09-30T09:42:21+00:00
