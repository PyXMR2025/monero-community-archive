---
title: 'Mac Ventura Build: Assertion Failed file CFData.c Line 235 '
source_url: https://github.com/xmrig/xmrig/issues/3185
author: walksonair
assignees: []
labels:
- bug
created_at: '2022-12-27T06:36:00+00:00'
updated_at: '2025-06-16T19:59:33+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:59:32+00:00'
---

# Original Description
**Describe the bug**
After build, unable to launch XMRIG. Getting following error:
`Assertion failed: (range.location + range.length <= dataLength), function __CFDataValidateRange, file CFData.c, line 235.`

**To Reproduce**
Build according to XMRIG website directions for intel Mac basic build

**Expected behavior**
Expected miner to begin mining with config.json parameters

**Required data**
```
 * ABOUT        XMRig/6.18.1 clang/14.0.0
 * LIBS         libuv/1.44.2 OpenSSL/3.0.7 hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz (1) 64-bit AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       27.8/64.0 GB (43%)
Assertion failed: (range.location + range.length <= dataLength), function __CFDataValidateRange, file CFData.c, line 235.
zsh: abort      ./xmrig
```

**Additional context**
Homebrew reports everything up to date.


# Discussion History
## SChernykh | 2022-12-27T10:50:06+00:00
Homebrew dependencies are sometimes broken, build using "Advanced build" instructions.

## walksonair | 2022-12-27T14:38:42+00:00
Installing XMRIG through homebrew works. Don't know why the basic build doesn't now. 

## Javihache | 2023-01-12T00:38:50+00:00
basic build doesn't work on MacOS Ventura. I can confirm.

## walksonair | 2023-01-12T01:29:27+00:00
Same issue with advanced build 🤷🏼‍♂️

## SChernykh | 2023-01-12T07:56:09+00:00
Try to build without hwloc: add `-DWITH_HWLOC=OFF` to cmake parameters.

## walksonair | 2023-01-18T04:14:18+00:00
Unsuccessful with `-DWITH_HWLOC=OFF`

## SChernykh | 2023-01-18T06:43:05+00:00
I was wrong about HWLoc. Compile with `-DWITH_DMI=OFF`. DMI reader is the only place in XMRig's code that uses CFData.

## Spudz76 | 2023-01-19T11:04:47+00:00
Seems like this change to the first line of `src/hw/dmi/dmi.cmake` would fix the problem (by automatically disabling DMI for Ventura or newer).
```
-if (WITH_DMI AND (XMRIG_OS_WIN OR XMRIG_OS_LINUX OR XMRIG_OS_FREEBSD OR (XMRIG_OS_MACOS AND NOT XMRIG_ARM)))
+if (WITH_DMI AND (XMRIG_OS_WIN OR XMRIG_OS_LINUX OR XMRIG_OS_FREEBSD OR (XMRIG_OS_MACOS AND NOT XMRIG_ARM AND NOT CMAKE_HOST_SYSTEM_VERSION VERSION_GREATER_EQUAL 22)))
```

## xmrig | 2023-01-19T15:10:57+00:00
Likely fixed in the dev branch, not yet verified on macOS Ventura.
Thank you.

## walksonair | 2023-01-21T16:41:08+00:00
I tried switching to the dev branch to pull and verify but it seems I may not have permissions for that. Let me know how you'd like me to help test.

## Spudz76 | 2023-01-21T17:18:48+00:00
Everyone has permission to pull dev.

## xmrig | 2023-01-22T09:42:59+00:00
@walksonair Usually just `git checkout dev` should be enough. Also I can confirm this issue is fixed.
Thank you.

## walksonair | 2023-01-24T17:09:23+00:00
Thanks. Was trying to use `git switch dev` and got that feedback..maybe I included a flag but nevertheless, I can confirm that I can build and run with the current DEV commit #3129 on Ventura.

Thanks for fixing this!

# Action History
- Created by: walksonair | 2022-12-27T06:36:00+00:00
- Closed at: 2025-06-16T19:59:32+00:00
