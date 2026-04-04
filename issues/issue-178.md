---
title: 'Buildbot: onion updates + restarts'
source_url: https://github.com/monero-project/meta/issues/178
author: anonimal
assignees: []
labels: []
created_at: '2018-02-16T01:53:34+00:00'
updated_at: '2020-03-09T21:50:08+00:00'
type: issue
status: closed
closed_at: '2020-03-09T21:50:08+00:00'
---

# Original Description
I've only been able to consistently reach the following build machines:

- Linux32/64
- FreeBSD
- OS X 10.12
- Cubieboard2

The remaining build machines are unavailable:

- OS X 10.10
- OS X 10.11
- ARMv7
- ARMv8 (which is currently [offline](https://github.com/monero-project/meta/issues/177))
- DragonflyBSD
- OpenBSD

The Tor versions are also out of date, some very out of date.

# Discussion History
## danrmiller | 2018-02-16T05:21:10+00:00
I'll look at this tomorrow.

* You should be able to get to the armv7 machine over tor now, let me know on IRC if not.
* Do you need the osx 10.10 machine? I'm trying to get @fluffypony to replace it with a 10.13 box.

## anonimal | 2018-02-16T06:08:10+00:00
>I'll look at this tomorrow.

Thanks Dan.

>You should be able to get to the armv7 machine over tor now, let me know on IRC if not.

Awesome, works now, thanks.

>Do you need the osx 10.10 machine? I'm trying to get @fluffypony to replace it with a 10.13 box.

Not particularly, other than to keep the OS X builds in the green. I'm assuming any fixes I make to 10.11/10.12 should apply to 10.10. If not, and if we'll get [10.13](https://github.com/monero-project/meta/issues/153) soon, then I don't need access.

## danrmiller | 2018-02-16T16:00:58+00:00
@anonimal you should now be able to access the osx 10.11 box via tor as well.

## anonimal | 2018-05-12T09:05:28+00:00
Yes, thanks. I still can't connect to the BSDs though. Everything else that is online I can connect to.

## anonimal | 2018-06-01T05:46:03+00:00
@danrmiller Please, I need to do BSD development.

## anonimal | 2018-06-24T22:01:41+00:00
An updated list of the machines that I still cannot SSH into:

- ARMv8 (which is currently [offline](https://github.com/monero-project/meta/issues/177))
- macOS 10.12
- FreeBSD
- OpenBSD

# Action History
- Created by: anonimal | 2018-02-16T01:53:34+00:00
- Closed at: 2020-03-09T21:50:08+00:00
