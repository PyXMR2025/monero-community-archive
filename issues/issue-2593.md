---
title: Compiling with -DBUILD_GUI_DEPS=ON disables building monero-wallet-rpc binary
source_url: https://github.com/monero-project/monero/issues/2593
author: emesik
assignees: []
labels: []
created_at: '2017-10-07T01:05:45+00:00'
updated_at: '2017-11-15T17:40:26+00:00'
type: issue
status: closed
closed_at: '2017-11-15T17:40:26+00:00'
---

# Original Description
When compiled with `-DBUILD_GUI_DEPS=ON` the `monero-wallet-rpc` binary is missing, it never gets built.

This looks like a bug. Or perhaps there's some non-intuitive reason behind such behavior?

# Discussion History
## moneromooo-monero | 2017-10-07T07:54:28+00:00
The GUI does not need that binary.

## emesik | 2017-10-07T13:50:48+00:00
OK, but my understanding of `-DBUILD_GUI_DEPS=ON` is that I'll get those deps in addition to everything else. When I turn something _ON_, it doesn't make me expect that I automatically turn something _OFF_, unless warned explicitly.

So, how would look a config for _"build everything possible"_? I'd like to use both GUI and RPC.

## moneromooo-monero | 2017-10-07T14:37:08+00:00
You'll have to ask jaquee. AFAIK, this setting is meant to build only what the GUI needs, since it's used automatically as part of the GUI build process. It is maybe confusing wording though, that is true.

## emesik | 2017-10-07T17:39:04+00:00
@Jaqueeee seems to be offline recently, but perhaps he could have a look :) I'm not familiar with cmake and don't want to mess it up.

## radfish | 2017-10-07T20:54:23+00:00
Remove the if statement on line 85 in src/wallet/CMakeLists.txt
I agree, turning something on should not turn other stuff off. If no objections, either of us can PR that.

If somebody really objects to having the gui build do the extra work of building that binary.... then I would add another flag variable for BUILD_WALLET_RPC and set its default to NOT BUILD_GUI_DEPS.

## moneromooo-monero | 2017-10-07T21:20:58+00:00
I would object to having this change, unless the change keeps the ability to build just what the GUI wallets needs.

## emesik | 2017-10-07T21:42:05+00:00
@radfish your idea from second paragraph sounds interesting, but perhaps it's better to avoid all non-mandatory interaction of switches? It's not intuitive and may still cause confusion. Let's keep it simple.

So, I'd see the defaults as `BUILD_WALLET_RPC=ON` and `BUILD_GUI_DEPS=OFF`.

If someone wants to build GUI deps only, they'd have to turn the RPC flag off. Otherwise they'll just build additional binary. This is not harmful although could be annoying on resource-thin platforms. But those usually build only CLI anyway.

What do you guys think about it?

## moneromooo-monero | 2017-10-07T21:48:00+00:00
I'm thinking the best may be to actually have the GUI build process make libwallet.so (or whatever target it is). This gets rid of this cmake level configuration, the main makefile targets don't include it, anyone who wants it can make this target, and anyone can make both binaries and lib. It'd need jaquee to tell us whether that'd work with the GUI build process.

## radfish | 2017-10-07T22:11:51+00:00
Please, let's not remove the library target from cmake because that makes packaging hell.

The .sh script that tries to build GUI by downloading and building the daemon source is not used for package builds of the Qt GUI. For packages of Qt GUI (and whatever else may come in the future), the process is clean and standard: the GUI package depends on the package that provides the library, the latter package is built separately, as one of two packages built from a spllit source package of this repo. That's how it's already packaged for Arch, and the only road to a Debian package.

Since overloading BUILD_GUI_DEPS is confusing, let's just add a flag (with simple defaults). EDIT: or two flags: one for RPC and one for wallet merged lib, and have BUILD_GUI_DEPS set those two flags accordingly, this way avoiding any change to the CLI api. Those who prefer the .sh script build system, can go ahead and use it. Nothing changes for them.

## moneromooo-monero | 2017-10-07T22:18:52+00:00
Since I know not much about packaging, I'll leave it to people who know to decide. However, a configuration option for just the RPC wallet seems wrong, unless there's one per tool (ie, daemon, cli wallet, etc).

## iDunk5400 | 2017-10-08T23:39:29+00:00
I had excluded `monero-wallet-rpc` from building with `-DBUILD_GUI_DEPS=ON` because it failed linking on some systems when `-DUSE_LTO=ON` used to be the default. Now that LTO is off by default, excluding `monero-wallet-rpc` from building may not be necessary any more.

## moneromooo-monero | 2017-10-09T08:16:19+00:00
I had thought this was to avoid wasting time building stuff we don't need. If that is not the case, then I'm fine with building all. But then the wallet API code is built in "normal" builds too, so the only thing that's extra is the "merged" library, right ? In that case, what is the use of BUILD_GUI_DEPS (or was it always a bodge to bypass LTO issues) ?

## moneromooo-monero | 2017-11-15T17:34:44+00:00
+resolved

# Action History
- Created by: emesik | 2017-10-07T01:05:45+00:00
- Closed at: 2017-11-15T17:40:26+00:00
