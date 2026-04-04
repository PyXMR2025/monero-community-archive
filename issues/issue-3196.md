---
title: Can't connect to daemon after upgrade from v0.16 to v0.17
source_url: https://github.com/monero-project/monero-gui/issues/3196
author: jkellyinsf
assignees: []
labels: []
created_at: '2020-10-28T11:26:11+00:00'
updated_at: '2020-11-06T13:06:17+00:00'
type: issue
status: closed
closed_at: '2020-11-06T13:06:17+00:00'
---

# Original Description
I had a vanilla installation of v0.16.0.3 on Ubuntu 18.04 running a local node with no special monero config, no antivirus, hardware wallets, Tor, or proxy servers.  It was working fine a few weeks ago.  When I started it two days ago, the gui prompted me to upgrade.

I downloaded the tarball for v0.17.1.1, ran the daemon in its own shell, and once it was synched started the gui wallet. The gui opened my wallet and showed its balance but was never able to connect to the daemon, displaying "Wallet is connecting to daemon" for hours.  

I ran tcpdump and determined it never even sent any packets to localhost:18081, either when starting or when I ran `status` from the log screen.  The [gui log](https://github.com/monero-project/monero-gui/files/5451562/gui.log) didn't show any errors.  I also couldn't close the wallet or the app--the "closing wallet..." modal spins forever until I kill the process. It looks like there's still a thread running.

[dEBRUYNE_1](https://www.reddit.com/user/dEBRUYNE_1) and [selsta](https://www.reddit.com/user/selsta/) spent a day with me in a [reddit thread](https://www.reddit.com/r/monerosupport/comments/jishrv/wallet_gui_wont_connect_to_daemon/) suggesting perturbations.  Launching the daemon from within the gui didn't work, nor clearing the gui settings file.

I ran the v0.16 client against the v0.17 daemon and it connected fine, though it couldn't sync the wallet fully.  Something about v0.17 must be different, related either to my env or to the upgrade.












# Discussion History
## xiphon | 2020-10-28T12:27:09+00:00
According to the logs, it fails to run async background tasks (threads) `m_scheduler.run` -> `QtConcurrent::run`. What's weird is that it fails silently, though scheduler will print debug errors on failure.

Please attach `ulimit -all` output. Then try to increase stack size with `ulimit -s <PREVIOUS_STACK_SIZE_MULTIPLIED_BY_10>` and check if that helps, revert `ulimit -s` to the previous value after the test.


## jkellyinsf | 2020-10-28T12:57:50+00:00
I bumped the stack size to 81920, but that doesn't help.

```
~/.bitmonero$ ulimit -all
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 15526
max locked memory       (kbytes, -l) 16384
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 15526
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```


## xiphon | 2020-10-30T02:19:24+00:00
Reproduced the issue. Working on it.

# Action History
- Created by: jkellyinsf | 2020-10-28T11:26:11+00:00
- Closed at: 2020-11-06T13:06:17+00:00
