---
title: create cmake and make should fallback to system packages for projects in /external
source_url: https://github.com/monero-project/monero/issues/9561
author: solomoncyj
assignees: []
labels:
- invalid
created_at: '2024-11-10T11:04:29+00:00'
updated_at: '2024-11-11T16:56:35+00:00'
type: issue
status: closed
closed_at: '2024-11-11T16:48:45+00:00'
---

# Original Description
In packaging, this will stop conflicts with system packages. moreover, some distrols, eg fedora, do not allow us to use static libs and or vendor 3rd party libs

# Discussion History
## hyc | 2024-11-10T15:44:58+00:00
None of the code in external/ is packaged or installed on its own, so that all seems irrelevant. liblmdb and randomx in external/ certainly cannot rely on a system package anyway.

## solomoncyj | 2024-11-10T16:26:16+00:00
ye s, but for packages like trezor-common, rapid json,  and other submodule execpt for supercop are already in package managers

## solomoncyj | 2024-11-11T08:25:22+00:00
> None of the code in external/ is packaged or installed on its own, so that all seems irrelevant. liblmdb and randomx in external/ certainly cannot rely on a system package anyway.

why cant they?
[randomx](https://packages.fedoraproject.org/pkgs/randomx/randomx/index.html)
[lmdb](https://packages.fedoraproject.org/pkgs/lmdb/lmdb/index.html)

## solomoncyj | 2024-11-11T09:29:36+00:00
please prefer `find_package` (if it's a normally CMake installed package) and only conditionally `add_subdirectory(external)`. 

## hyc | 2024-11-11T16:48:45+00:00
No. The issue you're reporting doesn't exist. There are no components of external/ that are installed, therefore there cannot be any conflicts with distro package managers. This ticket is invalid.

## hyc | 2024-11-11T16:56:13+00:00
> > None of the code in external/ is packaged or installed on its own, so that all seems irrelevant. liblmdb and randomx in external/ certainly cannot rely on a system package anyway.
> 
> why cant they? [randomx](https://packages.fedoraproject.org/pkgs/randomx/randomx/index.html) [lmdb](https://packages.fedoraproject.org/pkgs/lmdb/lmdb/index.html)

Monero builds LMDB with non-default compile options. Distro packages are not compatible.
RandomX is consensus-critical, you would have to be stupid or insane to trust someone else's build of it.

All of the components in external/ are at known specific versions. This is a requirement for both reliability and reproducibility.

# Action History
- Created by: solomoncyj | 2024-11-10T11:04:29+00:00
- Closed at: 2024-11-11T16:48:45+00:00
