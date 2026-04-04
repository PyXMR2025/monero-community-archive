---
title: Minor UI Nicety - Password Dialog Lag When Sending
source_url: https://github.com/monero-project/monero-gui/issues/2281
author: Thunderosa
assignees: []
labels: []
created_at: '2019-07-15T18:27:14+00:00'
updated_at: '2021-04-13T23:47:09+00:00'
type: issue
status: closed
closed_at: '2021-04-13T23:47:09+00:00'
---

# Original Description
There's a small moment of doubt for the user when the password dialog pops when confirming the sending of transaction. The lag isn't super long, but it's long enough that a visual indication that it's processing would be a nice.

# Discussion History
## selsta | 2019-07-16T16:57:55+00:00
I don’t have this lag. Are you using a really slow / old machine?

## Thunderosa | 2019-07-16T18:01:45+00:00
No, but I do have a high latency connection. I went back to watch another transaction more closely, it's the very last prompt when sending that's the most noticeable...3-4 seconds, something like that.

## ghost | 2019-07-19T16:36:39+00:00
There are MANY of these lags everywhere in the GUI! (Sorry to say it.) Just try to go to the `Account` page: 2-3 seconds lag, cursor doesn't change, user doesn't know what's happening, user panics, clicks again. MANY, MANY of these situations everywhere! (Again, sorry to say it.) Or try to add a new account: For 5 seconds nothing happens (as if the user hasn't clicked at all), then the cursor changes to that spinning animation (like when the wallet is freezing) and 30 seconds later everything is fine and the new account has been created.

So I'd definitely believe Thunderosa's report ;)

## selsta | 2019-07-19T16:37:33+00:00
@Realchacal Are you using a Ledger ?

## ghost | 2019-07-19T16:38:47+00:00
@selsta Yes!



## selsta | 2019-07-19T16:41:45+00:00
Well, that’s why it’s laggy. The things you are describing are calculated on the Ledger, so it will always be slow. Things can be improved by making them async, but Ledger specific optimizations are low priority.

## ghost | 2019-07-19T16:48:03+00:00
@selsta Thanks, I didn't know. These things will scare off new users, though :(



## Thunderosa | 2019-07-23T14:20:34+00:00
I'll not speak for Realchacal, but I don't think either of us are saying that unavoidable lags be fixed, just that they be indicated so they don't feel like a freeze.

## ghost | 2019-07-23T14:26:13+00:00
That's exactly my opinion. Waiting time is more than ok (of course!), but not waiting time that looks like freezing. And I can understand that Ledger is low priority, but I wouldn't call fixing these freezings Ledger specific "optimizations".

## selsta | 2021-04-13T23:47:09+00:00
We reworked the transaction flow. Please open a new issue if you still experience this lag.

# Action History
- Created by: Thunderosa | 2019-07-15T18:27:14+00:00
- Closed at: 2021-04-13T23:47:09+00:00
