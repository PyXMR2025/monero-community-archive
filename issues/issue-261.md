---
title: 'OSX: Existing monerod daemon not recoqnized'
source_url: https://github.com/monero-project/monero-gui/issues/261
author: rpcjacobs
assignees: []
labels: []
created_at: '2016-12-09T21:51:04+00:00'
updated_at: '2016-12-20T18:16:37+00:00'
type: issue
status: closed
closed_at: '2016-12-20T18:16:37+00:00'
---

# Original Description
Don't know if this is related to OSX-only (10.12), on which i'm testing the GUI on. But it seems the latest daemon implementation, does not automatically recognize an existing/running daemon. Honestly i'm not quite sure how the implementation is bound to work/thought out, but i was expecting it would find the running/existing daemon.

If i either setup a remote/foreign node-ip, or use a local ip, in both cases the local (running)daemon will not be _found_. I would expect, for example, it to disable the start daemon buttons and enable the stop daemon button and show the log for the running daemon `$HOME/.bitmonero/bitmonero.log` (if it exists) and/or load the existing `$HOME/.bitmonero/bitmonero.conf` (which might even include a non-default `log-file` configuration. A local/existing daemon could be detected with a simple `which` or likewise. Syncing my wallet with my local running daemon works and the daemon works as intended, so i'm sure it;s not related to the daemon.

On a side note, even starting a daemon from the GUI, does not work or does not show any log details. Simply does not work, although it does show the loading screen/pop-up. Tested when the local daemon was either running or stopped.

Maybe this report is early days for this latest addition, just thought to post my findings!

# Discussion History
## rpcjacobs | 2016-12-09T22:55:04+00:00
As noted by @Jaqueeee on irc, currently the daemon does not get built with monero-core, at leats not until #256 gets merged.

As per suggestion i've manually added the `monerod` to the gui `monero-core.app/Contents/MacOS`. Using a symbolic link from the build directory straight to the monero-core.app, which i first linked to my applications-folder, for easy access;  

`ln -s $HOME/monero-core/build/release/bin/monero-core.app /Applications/Monero-Core.app` 
`ln -s $HOME/monero/build/release/bin/monerod /Applications/Monero-Core.app/Contents/MacOS`

Hereafter, on starting the gui, a popup showed it had detected a (non-running) daemon. Starting it worked as intended now and logs get populated.



## moneromooo-monero | 2016-12-10T15:12:13+00:00
Is your running daemon using the same RPC version as the GUI you're running ? Look at the output of:
git grep RPC_VERSION
in both the tree you built the daemon in, and the monero subdirectory you built the GUI in.
If you did not built one of them, it's likely they're different RPC versions.

## Jaqueeee | 2016-12-19T19:17:01+00:00
Can this be closed @rpcjacobs ?

## rpcjacobs | 2016-12-20T18:16:22+00:00
Yes, for sure! It now works as intended!

# Action History
- Created by: rpcjacobs | 2016-12-09T21:51:04+00:00
- Closed at: 2016-12-20T18:16:37+00:00
