---
title: Building release-v0.11.1.0 doesn't produce the correct version
source_url: https://github.com/monero-project/monero-gui/issues/946
author: benma
assignees: []
labels:
- resolved
created_at: '2017-11-10T14:24:35+00:00'
updated_at: '2018-03-30T02:00:20+00:00'
type: issue
status: closed
closed_at: '2018-03-30T02:00:20+00:00'
---

# Original Description
I checked out `release-v0.11.1.0`, built the code using `build.sh`, and get this:

```sh
$ ./build/release/bin/monerod --version
Monero 'Helium Hydra' (v0.11.0.0-72b5f37f)
```

which is unexpected (.0 instead of .1).

The same from the downloaded binary from the release:

```sh
$ ./monerod --version
Monero 'Helium Hydra' (v0.11.1.0-release)
```

Building on linux 64 bit.

```sh
$ git describe
v0.11.1.0
```
In the monero submodule:

```sh
$ git describe
v0.10.3.1-950-gaf448d38
```

# Discussion History
## dEBRUYNE-1 | 2017-11-12T14:26:34+00:00
Try deleting `version/version.h` and then rebuild. 

## benma | 2017-11-12T22:24:20+00:00
That results in a number of compilation errors:

`fatal error: version.h: No such file or directory`

## dEBRUYNE-1 | 2017-11-13T13:19:19+00:00
Have you tried a fresh `git clone`?

## benma | 2017-11-13T13:22:45+00:00
I have. Same result. Does it work for you?

## Jaqueeee | 2017-11-13T19:13:34+00:00
I can't reproduce this either with release-v0.11.1.0 checked out. However, when building master branch I get the same output from `git describe` in monero submodule, which makes sense, since monero master branch still has 0.10.3.1 tag.

## sanderfoobar | 2018-03-30T01:49:08+00:00
+resolved

# Action History
- Created by: benma | 2017-11-10T14:24:35+00:00
- Closed at: 2018-03-30T02:00:20+00:00
