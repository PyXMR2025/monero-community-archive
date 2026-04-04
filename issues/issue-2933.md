---
title: Donate command needs sanity check
source_url: https://github.com/monero-project/monero/issues/2933
author: ghost
assignees: []
labels:
- enhancement
created_at: '2017-12-15T18:04:24+00:00'
updated_at: '2018-12-31T22:11:24+00:00'
type: issue
status: closed
closed_at: '2018-12-31T22:11:24+00:00'
---

# Original Description
I meant to type `help donate` to see it's description. Instead I typed `donate help`. The CLI then said `Donating help to donate.getmonero.org. Enter password:`

I know this isn't super important, but it might be a good idea to at least make sure it's a number.

# Discussion History
## ghost | 2017-12-15T18:06:53+00:00
Also, it might be fun to add a testnet address for use with --testnet flag. Like, the faucet address from https://dis.gratis/

## moneromooo-monero | 2017-12-15T18:12:13+00:00
Are you assuming it does not check, or did you check it does not check ?

## ghost | 2017-12-15T18:28:26+00:00
I'm assuming. I thought if I typed in a string of letters it would error something like "This is not a number". I can close this if there's already a check.

## moneromooo-monero | 2017-12-15T19:17:12+00:00
Well, IIRC this calls the transfer command, so I'm pretty sure it does check.
Now, that message is unfortunate, since it happens before the check, so maybe an extra one might be warranted, or the extra message removed. Anyway, that bug can stay since the message is wonky.

## ghost | 2017-12-17T18:01:24+00:00
> Also, it might be fun to add a testnet address for use with --testnet flag. Like, the faucet address from https://dis.gratis/

Same as #2848 

## dEBRUYNE-1 | 2018-01-08T12:46:17+00:00
+enhancement

# Action History
- Created by: ghost | 2017-12-15T18:04:24+00:00
- Closed at: 2018-12-31T22:11:24+00:00
