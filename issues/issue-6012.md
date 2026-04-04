---
title: Version string is only updated on clean build, not incremental
source_url: https://github.com/monero-project/monero/issues/6012
author: ndorf
assignees: []
labels: []
created_at: '2019-10-23T17:59:23+00:00'
updated_at: '2019-10-24T23:39:16+00:00'
type: issue
status: closed
closed_at: '2019-10-24T23:39:16+00:00'
---

# Original Description
After a clean build, `monerod --version` shows the correct git commit hash it was built from. (This same version string is also logged during normal daemon startup.) However, after updating the source and rebuilding in the same directory, the new binary continues to report the old commit hash, from when the clean build was done.

```
% git status --ignored && git log -1
On branch master
Your branch is behind 'origin/master' by 36 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)
nothing to commit, working tree clean
commit 441ed9f2fef6a43708c115191c51ca16930ce95b
Merge: 6c0572398 515e9316b
Author: luigi1111 <luigi1111w@gmail.com>
Date:   Wed Oct 16 13:54:06 2019 -0500

    Merge pull request #5990
    
    515e931 functional_tests: fix transfer test - long payment ids are gone (moneromooo-monero)
% time make -j8
...
make -j8  3529.69s user 139.56s system 600% cpu 10:10.84 total
% ls -l build/**/bin/monerod 
-rwxr-x--- 1 ndorf ndorf 13623808 Oct 23 11:18 build/Linux/master/release/bin/monerod
% ./build/Linux/master/release/bin/monerod --version
Monero 'Boron Butterfly' (v0.14.1.2-441ed9f2f)
```

The clean build above prints the correct hash, 441ed9f2f. The incremental build below still prints the same one, but it should print 4233d8834:

```
% git pull
First, rewinding head to replay your work on top of it...
Fast-forwarded master to 4233d88341a074450c38064807ed348fe4691019.
% git submodule update --recursive
Submodule path 'external/randomx': checked out 'b53f0ed145c1a51df6ca0708a215089b76d0c056'
% git status --ignored && git log -1
On branch master
Your branch is up-to-date with 'origin/master'.
Ignored files:
  (use "git add -f <file>..." to include in what will be committed)

	build/

nothing to commit, working tree clean
commit 4233d88341a074450c38064807ed348fe4691019
Merge: bb2bcf352 abd376313
Author: luigi1111 <luigi1111w@gmail.com>
Date:   Tue Oct 22 10:54:46 2019 -0500

    Merge pull request #5973
    
    abd3763 cryptonote: fill in tx weight when syncing from pruned blocks (moneromooo-monero)
% time make -j8
...
make -j8  3410.07s user 129.51s system 613% cpu 9:37.02 total
% ls -l build/**/bin/monerod        
-rwxr-x--- 1 ndorf ndorf 13654712 Oct 23 11:33 build/Linux/master/release/bin/monerod
% ./build/Linux/master/release/bin/monerod --version
Monero 'Boron Butterfly' (v0.14.1.2-441ed9f2f)
```

In this example, all or almost all of the sources were rebuilt (9:37 vs 10:10 time), but the new executable is still printing the old version. After another clean build, it finally shows the correct one:

```
% git clean -xdf
Removing build/
% time make -j8
make -j8  3520.28s user 135.10s system 618% cpu 9:51.12 total
% ls -l build/**/bin/monerod 
-rwxr-x--- 1 who who 13650616 Oct 23 11:48 build/Linux/master/release/bin/monerod
% ./build/Linux/master/release/bin/monerod --version
Monero 'Boron Butterfly' (v0.14.1.2-4233d8834)
```

# Discussion History
## selsta | 2019-10-23T18:03:29+00:00
I’ve noticed the same behaviour.

## ndorf | 2019-10-23T20:25:19+00:00
It's done by [this custom CMake command](https://github.com/monero-project/monero/blob/4233d88341a074450c38064807ed348fe4691019/cmake/Version.cmake#L40), which won't be rerun unless version.cpp.in changes or version.cpp is deleted.

I think this should be fixable if the version string is stored in a CMake cache variable. The `configure_file` function will only rewrite the output if it changes. This seems to work in a toy example, at least. @hyc any thoughts?

## hyc | 2019-10-23T22:28:19+00:00
If you have a working patch, by all means, submit a PR.

## ndorf | 2019-10-23T22:51:26+00:00
I think it's fixed in #6015, feedback welcome.

## hyc | 2019-10-23T22:57:04+00:00
Keep the reference to #6012 in the description, so this issue will automatically get closed when that PR is merged.

## ndorf | 2019-10-23T23:47:23+00:00
That should be working now, it didn't seem to recognize the link until I moved it from the title to the first comment. It now says it will close this issue when you hover over the link.

# Action History
- Created by: ndorf | 2019-10-23T17:59:23+00:00
- Closed at: 2019-10-24T23:39:16+00:00
