---
title: miniupnpc submodule conflicts with externally installed miniupnpc
source_url: https://github.com/monero-project/monero/issues/3862
author: ilovezfs
assignees: []
labels: []
created_at: '2018-05-25T14:24:07+00:00'
updated_at: '2018-10-26T09:37:42+00:00'
type: issue
status: closed
closed_at: '2018-10-26T09:37:42+00:00'
---

# Original Description
It seems that as of 0.12.1.0, even if an externally install miniupnpc is available, monero still tries to use the submodule.

This results in the build trying to install

lib/libminiupnpc.a

and

include/miniupnpc
include/miniupnpc/igd_desc_parse.h
include/miniupnpc/miniupnpc.h
include/miniupnpc/miniupnpc_declspec.h
include/miniupnpc/miniupnpctypes.h
include/miniupnpc/miniwget.h
include/miniupnpc/portlistingparse.h
include/miniupnpc/upnpcommands.h
include/miniupnpc/upnpdev.h
include/miniupnpc/upnperrors.h
include/miniupnpc/upnpreplyparse.h

which can conflict with the externally installed miniupnpc.

Some possibilities:
1) allow use of an externally installed miniupnpc as was the case in 0.12.0.0

or

2) if the externally installed miniupnpc isn't allowed, don't try to install the miniupnpc headers and static library (or at least not into the global include and lib directories)

Full build log: https://gist.github.com/ilovezfs/280f8a8b66c3d58d0264752c73cbde5c

# Discussion History
## anonimal | 2018-05-25T20:50:25+00:00
>even if an externally install miniupnpc is available, monero still tries to use the submodule.

Yes, that is intentional. See https://github.com/monero-project/monero/pull/3668#issuecomment-382683959  https://hackerone.com/reports/340012 https://github.com/miniupnp/miniupnp/issues/302#issuecomment-391803220

>if the externally installed miniupnpc isn't allowed, don't try to install the miniupnpc headers and static library (or at least not into the global include and lib directories)

We're still waiting on a resolution of https://github.com/monero-project/miniupnp/pull/3 and merging of https://github.com/monero-project/miniupnp/pull/4 and https://github.com/monero-project/miniupnp/pull/5. Ping @fluffypony.

## ilovezfs | 2018-05-25T23:56:51+00:00
>Yes, that is intentional.

OK, that's fine. Nonetheless, `make install` should not be trying to install a vendored static library or headers into the `CMAKE_INSTALL_PREFIX`.

## anonimal | 2018-05-26T01:49:48+00:00
>make install should not be trying to install a vendored static library or headers into the CMAKE_INSTALL_PREFIX

There is no install target in the monero Makefile. What your describing is fixed in https://github.com/monero-project/miniupnp/pull/3.

Future note: this issue should've been opened in the miniupnp repo.

## ilovezfs | 2018-05-26T01:51:48+00:00
@anonimal the install target is generated automatically by CMake. The `Makefile` itself should not be checked into source control.

## anonimal | 2018-05-26T01:59:22+00:00
>the install target is generated automatically by CMake

Yes but you're not describing a monero problem and this is the monero repo, so what is your point?

## ilovezfs | 2018-05-26T02:02:12+00:00
That saying "There is no install target in the monero Makefile" doesn't change the fact that you have CMake misconfigured and that https://github.com/monero-project/miniupnp/pull/3 or equivalent should be merged sooner rather than later.

## anonimal | 2018-05-26T02:18:02+00:00
>you have CMake misconfigured

Me? I'm the lead developer for miniupnp? This is an upstream issue, not mine nor monero's. You'd know that if you had half a brain to look at the git log.

Nothing is stopping you or brew from applying the patch. I have done it in the AUR https://aur.archlinux.org/cgit/aur.git/commit/?h=monero&id=67408013e2dcf401377912b870473ec8a6be2db6.

## ilovezfs | 2018-05-26T02:23:40+00:00
@anonimal as you can see I've already done the equivalent in https://github.com/Homebrew/homebrew-core/blob/master/Formula/monero.rb#L35-L38

>Me? I'm the lead developer for miniupnp? This is an upstream issue, not mine nor monero's. You'd know that if you had half a brain to look at the git log.

I mean that the configuration of monero shouldn't treat the vendored dependency as something to be installed, just as a build-time dependency. I'm not sure how that's an upstream issue.

>You'd know that if you had half a brain to look at the git log.

OK.

## moneromooo-monero | 2018-10-26T09:23:54+00:00
Is there still a problem here ? It looks like a patch was linked, and is now merged. The Monero makefile has no install target, as said above. If there is still a problem, please be specific about what is.

# Action History
- Created by: ilovezfs | 2018-05-25T14:24:07+00:00
- Closed at: 2018-10-26T09:37:42+00:00
