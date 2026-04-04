---
title: monerod version command should get running daemon's version via RPC
source_url: https://github.com/monero-project/monero/issues/5994
author: ndorf
assignees: []
labels: []
created_at: '2019-10-16T19:40:41+00:00'
updated_at: '2019-12-12T19:36:40+00:00'
type: issue
status: closed
closed_at: '2019-12-12T19:36:40+00:00'
---

# Original Description
One would expect[1] the command `monerod version` (as opposed to the _option_ `monerod --version`) to get the running daemon's version via RPC. Instead, it simply prints the version from the binary that was invoked, just like the `--version` option:

```
$ ./release-v0.14/release/bin/monerod version
2019-10-16 19:27:46.202     I Monero 'Boron Butterfly' (v0.14.1.2-release)
2019-10-16 19:27:46.208  I Generating SSL certificate
Monero 'Boron Butterfly' (v0.14.1.2-release)
$ ./master/release/bin/monerod version
2019-10-16 19:28:04.548   I Monero 'Boron Butterfly' (v0.14.1.2-d66db18c0)
2019-10-16 19:28:04.553        I Generating SSL certificate
Monero 'Boron Butterfly' (v0.14.1.2-d66db18c0)
```

No attempt at RPC is made when the command is `version` (this would fail with any other command, e.g. `status`):

```
$ ./master/release/bin/monerod --rpc-bind-port=0 version
2019-10-16 19:33:05.577   I Monero 'Boron Butterfly' (v0.14.1.2-d66db18c0)
2019-10-16 19:33:05.583        I Generating SSL certificate
Monero 'Boron Butterfly' (v0.14.1.2-d66db18c0)
```

It doesn't seem that an RPC to support this exists -- [get_version](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_version) doesn't return a version string, but rather some opaque unsigned int. It seems reasonable to add one, though. Of course, it should be disabled for restricted RPC. Any objections?

[1]: `monerod --help` says `Usage: ./master/release/bin/monerod [options|settings] [daemon_command...]`. So, when invoking `monerod version`, `version` is the `daemon_command` argument, not an "option."

# Discussion History
## trasherdk | 2019-10-17T02:35:52+00:00
So when running different versions on main/stage/testnet, which one should return it's version?

## xiphon | 2019-10-17T03:15:50+00:00
> So when running different versions on main/stage/testnet, which one should return it's version?

* `./monerod --version`
should print `./monerod` version
* `./monerod version`
should print mainnet daemon version
* `./monerod version --testnet`
should print testnet daemon version


## trasherdk | 2019-10-17T08:39:21+00:00
Okay.

So, `./monerod --version` is `file version`
and `./monerod version` is `what is running`

Right?

## xiphon | 2019-10-17T12:50:20+00:00
Yep, should be that way

## moneromooo-monero | 2019-10-17T13:42:15+00:00
> It doesn't seem that an RPC to support this exists

get_info

## ndorf | 2019-10-23T16:17:37+00:00
> get_info

This one currently returns the same string "v0.14.1.2" for both master and release-v0.14. I assume it'd be okay to change it to the full version string (with -release or commit hash suffix)?

In any case, it seems that string (as reported by e.g. --version) isn't getting updated after an incremental build, but only a clean one. Looking into that.

## moneromooo-monero | 2019-10-23T17:48:01+00:00
I think I'd be OK with that as long as it stays restricted.

## hyc | 2019-10-23T19:30:19+00:00
> In any case, it seems that string (as reported by e.g. --version) isn't getting updated after an incremental build, but only a clean one. Looking into that.

You have to manually delete build/version.cpp; it is not getting rebuilt automatically. Getting cmake to cooperate on that has proved quite challenging.

# Action History
- Created by: ndorf | 2019-10-16T19:40:41+00:00
- Closed at: 2019-12-12T19:36:40+00:00
