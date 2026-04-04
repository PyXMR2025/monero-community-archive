---
title: gcc8 build still broken in v0.12.2.0
source_url: https://github.com/monero-project/monero/issues/3929
author: anonimal
assignees: []
labels: []
created_at: '2018-06-05T03:33:58+00:00'
updated_at: '2018-06-21T16:01:13+00:00'
type: issue
status: closed
closed_at: '2018-06-21T16:01:13+00:00'
---

# Original Description
Why hasn't this been applied yet? ae6a40dfd76f5fb024b48a83d900cf5e6d02db93

# Discussion History
## moneroexamples | 2018-06-06T08:41:51+00:00
On Arch? 

## anonimal | 2018-06-06T18:42:42+00:00
Yes. I've applied proper patches though. https://aur.archlinux.org/cgit/aur.git/log/?h=monero.

## moneroexamples | 2018-06-07T00:09:49+00:00
Can compile using the followng for the time being:

> make CXXFLAGS="-Wno-error=class-memaccess" CFLAGS="-Wno-error=class-memaccess"

## moneromooo-monero | 2018-06-21T08:47:21+00:00
AFAIK the last GCC 8 fix is now in master. Can you confirm (or anyone else with GCC 8) ?
If there's still more, run with -k to get ALL the errors.

## stoffu | 2018-06-21T15:13:23+00:00
Confirmed that everything builds fine with GCC 8.1.1 (on Manjaro 17).


## moneromooo-monero | 2018-06-21T15:56:57+00:00
Thanks

+resolved

# Action History
- Created by: anonimal | 2018-06-05T03:33:58+00:00
- Closed at: 2018-06-21T16:01:13+00:00
