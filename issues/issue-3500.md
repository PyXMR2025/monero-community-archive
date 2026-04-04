---
title: unit_tests fails on 3 machines with v0.12.0.0
source_url: https://github.com/monero-project/monero/issues/3500
author: The-King-of-Toasters
assignees: []
labels:
- invalid
created_at: '2018-03-27T04:01:38+00:00'
updated_at: '2018-05-16T11:32:59+00:00'
type: issue
status: closed
closed_at: '2018-05-16T11:32:59+00:00'
---

# Original Description
I've tried compiling Lithium Luna on three different machines, and all of them fail the `unit_tests` test. This occurs on both release and debug versions.
The machines are:

- Thinkpad T420 (i7-2620M) running Arch Linux - Release only
- Random Prebuilt (i5-4440) running Ubuntu 16.04 - Release/Debug
- Personal Desktop (i7-3770k) running Arch Linux - Release/Debug

Each machine has all packages featured in README.md installed, except `libgtest-dev` on Ubuntu because of #3096.

I've uploaded each `unit_tests.log` to [my server](https://www.sgregoratto.me/monerologs/) for anyone to look at.

# Discussion History
## moneromooo-monero | 2018-03-27T10:15:36+00:00
Which one(s) is/are failing ? The logs don't seem to include that info. If it's just the DNS ones, then it's known.

## The-King-of-Toasters | 2018-03-27T14:51:57+00:00
I don't understand. The `unit_tests` test fails when invoking `make release-test` or `make debug-test`. This happens on all machines. 

Also, if its just DNS errors, does that mean everything else is fine?

## moneromooo-monero | 2018-03-27T14:55:50+00:00
When you run "make release-test" or similar, it just tells you if one or more failed, without the list. You have to run manually (build/tests/unit_tests/unit_tests) to see which ones fail. If it's just the DNS test(s) that fail(s), it doesn't necessarily mean everything else is fine, but it probably does :)

## moneromooo-monero | 2018-05-16T11:00:18+00:00
I'll assume it's the DNS test(s), as usual. If not, reopen and give the list of failing tests.

+invalid


# Action History
- Created by: The-King-of-Toasters | 2018-03-27T04:01:38+00:00
- Closed at: 2018-05-16T11:32:59+00:00
