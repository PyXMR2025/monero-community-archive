---
title: Some command line flags (when loading daemon) don't work (or exist) once the
  daemon has started
source_url: https://github.com/monero-project/monero/issues/944
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-08-01T09:44:01+00:00'
updated_at: '2016-12-15T17:34:32+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:34:32+00:00'
---

# Original Description
Some variables that you can modulate with `--setting ARG` flags when you start bitmonerod can't be modified once the daemon starts (when you type things into the daemon or send it rpc stuff). I call this "live".  For instance, `out_peers` doesn't work when live even though its in the help menu of commands that should work. Also, `add-priority-node` doesn't exist, and there are a lot of other ones that are in the --help menu but not in the live help menu. 


# Discussion History
## moneromooo-monero | 2016-08-01T12:10:02+00:00
As designed. Restart the daemon if you want to do things like change port to bind to, etc.


## luigi1111 | 2016-08-10T14:46:45+00:00
I don't think `out_peers` is working as designed from the console. It returns "Error: Unsuccessful" for me.

But yes, not all launch commands are expected to work at the console. There's a reason the helps don't match.

Edit: Oh I see there's a separate issue for `out_peers`.


## moneromooo-monero | 2016-08-11T13:39:35+00:00
Yes, out_peers is an existing noop command at the moment.


# Action History
- Created by: Gingeropolous | 2016-08-01T09:44:01+00:00
- Closed at: 2016-12-15T17:34:32+00:00
