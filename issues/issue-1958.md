---
title: Different addresses while using command <address> and <viewkey>
source_url: https://github.com/monero-project/monero/issues/1958
author: Lihaes
assignees: []
labels: []
created_at: '2017-04-04T16:27:10+00:00'
updated_at: '2017-04-04T20:55:33+00:00'
type: issue
status: closed
closed_at: '2017-04-04T20:55:32+00:00'
---

# Original Description
Hey, 
while I try to get familliared with the monero-wallet, I was wondering why `viewkey` returns as I considered my Kpriv + Kpup, but `address` gets me a key different and longer than the Kpup from `viewkeys.`

What is the differnence between this two?



# Discussion History
## moneromooo-monero | 2017-04-04T17:24:33+00:00
At the risk of missing the obvious, the address is an encoded version of both public keys. Are you just comparing the string representations of both ? If so, there's your problem. If you know what you're doing and they're really different, then please give more information (ie, how you compared).

## Lihaes | 2017-04-04T19:06:58+00:00
I just compared the string rep. of them. Is there a tutorial for the different keys and their representation(s)?
I found additional `spendkey` which is a further different key...


## moneromooo-monero | 2017-04-04T20:47:39+00:00
Keys are hexadecimal. The address is base58. Monero uses two keys, not one as Bitcoin.
You can ask such questions on monero.stackexchange.com (search first, it might already asked and answered). Please keep github for bug reports.


## moneromooo-monero | 2017-04-04T20:48:29+00:00
And please close that issue now, I can't :)

## Lihaes | 2017-04-04T20:55:32+00:00
Thanks!

# Action History
- Created by: Lihaes | 2017-04-04T16:27:10+00:00
- Closed at: 2017-04-04T20:55:32+00:00
