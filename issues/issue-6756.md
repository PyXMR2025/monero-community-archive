---
title: 'Request: Reproducible builds for NetBSD'
source_url: https://github.com/monero-project/monero/issues/6756
author: garlicgambit
assignees: []
labels: []
created_at: '2020-08-11T18:39:33+00:00'
updated_at: '2020-08-20T07:45:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
NetBSD is a [deterministically reproducible operating system](https://blog.netbsd.org/tnf/entry/netbsd_fully_reproducible_builds). It would be nice to have deterministically reproducible Monero binaries for it.  
  
Related: [reproducible builds issue](https://github.com/monero-project/monero/issues/6435) for OpenBSD.

# Discussion History
## thomasvaughan | 2020-08-13T11:53:22+00:00
The most efficient way to fulfil this Request might be to write a pkgsrc Makefile for Monero (a idea that's been mooted as being useful for Monero on SmartOS too  — https://github.com/monero-project/monero/issues/5802). The [pkgsrc manual](http://www.netbsd.org/docs/pkgsrc/) doesn't have a lot to say about reproducible packages, but you do have the option of setting the following in your mk.conf:

    PKGSRC_MKREPRO=yes
    ASLR=yes
    PKGSRC_MKPIE=yes

…apparently with consequences described as follows in [$PKGSRC ROOT/mk/defaults/mk.conf](http://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/mk/defaults/mk.conf):

    PKGSRC_MKREPRO?= no
    # If no, do not alter the build process. Otherwise, try to build reproducibly.
    # This allows packages built from the same tree and options to produce identical
    # results bit by bit.
    # This option should be combined with ASLR and PKGSRC_MKPIE to avoid predictable
    # address offsets for attackers attempting to exploit security vulnerabilities.
    # Possible: yes, no
    # Default: no
    #
    # Keywords: reproducible

For this to be truly reproducible, it presumably requires all dependency packages to also be built reproducibly (or does dynamic linking eliminate that requirement?).

I haven't tried writing a Monero pkgsrc Makefile myself, mostly out of laziness: it's doable, but the fiddly part is coaxing the pkgsrc Makefile into downloading all the right source files, including git submodules. Currently, Monero works on NetBSD x86_64, courtesy of a recent open PR that updates RandomX. Other hardware — unknown.

Writing a pkgsrc Makefile raises a few question. Who should host it (given the risks, mentioned by hyc in https://github.com/monero-project/monero/issues/2395#issuecomment-327765731, arising from encouragement of multiple independent binaries)? Should it follow the example set by other Monero packagers by creating rc scripts that allow monerod to run at system start-up under its own user account?

## hyc | 2020-08-13T16:21:15+00:00
If you want this to be included in the reproducible build process that everyone else uses, it needs to be buildable/cross-compilable from the gitian/depends framework. That ought to only require obtaining the NetBSD /usr/include and /usr/lib hierarchy, much like we did for FreeBSD.

## kayront | 2020-08-20T07:45:57+00:00
@thomasvaughan, not to go too oftopic here, but I tried compiling monero for SmartOS a long time ago, and it does not build at all (which is a shame).

I could provide a solaris zone accessible over tor for any developer who wants to have a go at it and can't easily find a solaris environment.

# Action History
- Created by: garlicgambit | 2020-08-11T18:39:33+00:00
