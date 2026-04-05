---
title: Support for (Rpi4) ARM manjaro
source_url: https://github.com/xmrig/xmrig/issues/3112
author: girl313
assignees: []
labels: []
created_at: '2022-08-28T18:20:48+00:00'
updated_at: '2025-06-18T22:53:11+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:53:11+00:00'
---

# Original Description
Hi hi,

This is my first experience with mining coin.
I have: Manjaro ARM (rpi4) v22.08

I installed the wallet via: https://flathub.org/apps/details/org.getmonero.Monero
But I don't know how I should install and run the (xmrig) miner.

Which version and installation procedure should I choose ?

thanks  :-)

# Discussion History
## Spudz76 | 2022-09-01T02:25:19+00:00
Well considering there is no Linux arm64 [binary release](https://github.com/xmrig/xmrig/releases) currently (only macos-arm64 for M1's and such) then you'd follow the [advanced build instructions](https://xmrig.com/docs/miner/build/ubuntu) from some other distro of Linux, replacing step 1 with whatever Manjaro/Arch would call those packages.  I'd just skip step 1 and do 2, 3, and the first half of 4 and figure out what is missing to make `build_deps.sh` complete successfully.  Stuff like automake/cmake/libtool/git should still be called something real close to that in pacman, there might not be a convenience virtual package like `build_essential` which pulls in all the gcc and other compiler stuff.

Also you must be running a full, real, 64-bit install.  Many ARM distros are stupid and only have 32-bit even on a 64-bit CPU, or mix a 64-bit kernel with a 32-bit userspace which also doesn't work.  32-bit pure on an armv7 CPU sometimes works, but ends up slower than a tortoise walking backward while drunk.

## Spudz76 | 2022-09-01T02:30:57+00:00
Also of note, [an old post](https://archived.forum.manjaro.org/t/is-manjaro-arm-64-bit/45398/8) says Manjaro-ARM on Pi's are 32-bit kernel and I doubt anyone bothered to make it 64-bit since all you really need that for is mining (and it "can be" worse for everything else people use Pi's for, wastes memory, blah blah blah...)  There is a Rasbian pure-64-bit which definitely works, you might get 100H/s downhill with a tailwind.

# Action History
- Created by: girl313 | 2022-08-28T18:20:48+00:00
- Closed at: 2025-06-18T22:53:11+00:00
