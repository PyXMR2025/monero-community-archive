---
title: '[Feature] wallet: add  ''donate <amount>'' command'
source_url: https://github.com/monero-project/monero/issues/1447
author: anonimal
assignees: []
labels: []
created_at: '2016-12-14T00:15:39+00:00'
updated_at: '2016-12-20T15:43:47+00:00'
type: issue
status: closed
closed_at: '2016-12-20T15:43:47+00:00'
---

# Original Description
```
@anonimal | Silly question, but how silly would it be to implement a 'donate <amount>' command which donates to a hardcoded monero fund address?
@anonimal | *the monero donation address
```

I'm curious to see how popular this idea is. An optional `sweep_all` like argument would be nice too.

# Discussion History
## ghost | 2016-12-14T09:23:09+00:00
I like it. If we could have a sunshine clause so it's only around for a year or two that might be better. 

## fluffypony | 2016-12-14T09:24:11+00:00
Or just pay it to donate.getmonero.org, and warn if it doesn't match the hardcoded one, no need to sunshine it:)

## luigi1111 | 2016-12-15T15:58:23+00:00
Added by #1451 

## anonimal | 2016-12-15T21:29:55+00:00
@luigi1111 can we reopen this since the command doesn't donate with cli wallet. Can anyone else confirm?

## luigi1111 | 2016-12-16T00:25:58+00:00
It does work.

## anonimal | 2016-12-16T01:45:32+00:00
Nope, not for everyone. Please see https://github.com/monero-project/monero/pull/1451#issuecomment-267496171.

## luigi1111 | 2016-12-16T15:09:47+00:00
OpenAlias not working over tor is a different issue, but fine. Please bring further discussion from PR #1451 back here.

## luigi1111 | 2016-12-16T15:21:02+00:00
https://github.com/luigi1111/bitmonero/commit/bfa23e4c4e6d9fbae3bef998dd98739d760a3008

That kinda lies to the user, but makes it look good.

## anonimal | 2016-12-16T18:44:45+00:00
Commented in https://github.com/luigi1111/bitmonero/commit/bfa23e4c4e6d9fbae3bef998dd98739d760a3008

## luigi1111 | 2016-12-16T22:01:08+00:00
I care very little about this functionality in general. I have significant doubts it'll actually facilitate meaningful donations over not having it (a button in a GUI, maybe that's different).

## anonimal | 2016-12-16T23:05:31+00:00
Is not every bit of XMR meaningful though? I think pushing all users to donate with cli or gui should be encouraged (gui button is a great idea too, btw). It comes at no cost to us. The easier the better too: is that not the basis (partly) of good sales strategy (don't make people wait or jump through hoops and don't give them time to change their mind)?

What if I simply PR'd the original hardcoded address and then we can close this issue?

## luigi1111 | 2016-12-16T23:51:20+00:00
> What if I simply PR'd the original hardcoded address and then we can close this issue?

Fine with me. :) Dunno what the others think.

# Action History
- Created by: anonimal | 2016-12-14T00:15:39+00:00
- Closed at: 2016-12-20T15:43:47+00:00
