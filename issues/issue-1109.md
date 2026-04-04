---
title: monerod reporting "Output does not exist"
source_url: https://github.com/monero-project/monero/issues/1109
author: voidzero
assignees: []
labels:
- invalid
created_at: '2016-09-20T15:43:41+00:00'
updated_at: '2017-10-02T20:00:24+00:00'
type: issue
status: closed
closed_at: '2017-10-02T20:00:24+00:00'
---

# Original Description
During sync, I got the following message but don't understand what it means and if it is something problematic on my end:

<pre>[P2P1]Output does not exist! amount = 500000000000</pre>


This is monero compiled statically, on Gentoo, amd64, commit hash 53e18ca.


# Discussion History
## moneromooo-monero | 2016-09-20T16:44:38+00:00
Possibly an alt chain. It's unclear without more context.


## voidzero | 2016-09-20T17:02:57+00:00
Agreed. But is it possible to get more context a posteriori? I know that more verbose messages become visible when set_log is higher than 0, but in that case things like these will also be easier to pass by unnoticed, due to the amount of other output.

As an idea; maybe cases like these could be logged to a file when a user would specify something like, say, 'buglog' pointing to a filename? Another idea is to allow to set something like logfile_level=i, so that the console output level can be set separately from output that'd be written to a file. Hope this makes sense.


## moneromooo-monero | 2016-09-20T22:07:01+00:00
A change in logging will be done, and I expect it'll make it easier to find things.
However, such messages are expected if you're seeing an alt chain.


## radfish | 2016-09-21T02:25:43+00:00
@voidzero sorry for offtopic, do you happen to have a portage script for Gentoo to share?


## voidzero | 2016-09-21T12:07:35+00:00
@radfish no, I don't, because I usually run a stable system (the boost version is too low for monero, it needs to be keyworded (~amd64)) and I don't install monero from an ebuild.

To compile monero, I temporarily install some keyworded (~amd64) packages, which get the 'static-libs' use-flag (these packages are ldns, expat, gtest, unbound, boost). I also install doxygen and boost-build.

After this, I build static monero binaries (command make -j4 release-static).

And when all this this is done and my binaries are built, I reinstall the original versions of the packages I mentioned above.


## moneromooo-monero | 2017-10-02T19:32:36+00:00
No claim of anything not working beyond the message, and I believe some of them were expected back then. Closing.

+invalid

# Action History
- Created by: voidzero | 2016-09-20T15:43:41+00:00
- Closed at: 2017-10-02T20:00:24+00:00
