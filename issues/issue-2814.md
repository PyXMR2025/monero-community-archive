---
title: issue recovering wallet...
source_url: https://github.com/monero-project/monero-gui/issues/2814
author: alanhasgari
assignees: []
labels: []
created_at: '2020-03-27T22:18:00+00:00'
updated_at: '2020-03-27T23:18:59+00:00'
type: issue
status: closed
closed_at: '2020-03-27T23:13:44+00:00'
---

# Original Description
attempting to recover wallet with mnemonic and restore height... for some reason it will not accept my wallet name... my wallet name is 11 characters, and the box is red... when i enter the first 10 characters, the box becomes green, but that is not the full wallet name...

any ideas??

# Discussion History
## selsta | 2020-03-27T22:20:12+00:00
The wallet name already exists.

## alanhasgari | 2020-03-27T22:24:57+00:00
I'm trying to recover it... So, I'm suppose to enter a new name? I tried that and it gave me an error...

## selsta | 2020-03-27T22:32:00+00:00
Yes, you have to enter a new name. Which error?

## alanhasgari | 2020-03-27T23:07:28+00:00
Says electrum-style word list failed verification

## alanhasgari | 2020-03-27T23:13:44+00:00
After half a dozen tries, it finally went through... Never had this kind of problem with other wallets...

Thank you, selsta.

## selsta | 2020-03-27T23:17:04+00:00
electrum-style word list failed verification means that you didn’t enter the seed correctly.

## alanhasgari | 2020-03-27T23:18:59+00:00
It was a direct copy and paste... Inside not enter it incorrectly.

On Fri., Mar. 27, 2020, 7:17 p.m. selsta, <notifications@github.com> wrote:

> electrum-style word list failed verification means that you didn’t enter
> the seed correctly.
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/2814#issuecomment-605352726>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABHZ5PZZPG642OPUGH4DVZDRJUXXZANCNFSM4LVKLWEQ>
> .
>


# Action History
- Created by: alanhasgari | 2020-03-27T22:18:00+00:00
- Closed at: 2020-03-27T23:13:44+00:00
