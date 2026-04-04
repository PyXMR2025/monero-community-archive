---
title: The official binaries (v0.8.8.6) for Mac don't work on Mac OS X 10.9 (Mavericks)
source_url: https://github.com/monero-project/monero/issues/254
author: Jojatekok
assignees: []
labels: []
created_at: '2015-04-04T06:49:00+00:00'
updated_at: '2015-04-04T08:43:05+00:00'
type: issue
status: closed
closed_at: '2015-04-04T08:43:05+00:00'
---

# Original Description
I've been browsing through several websites, and it seems that the

```
-mmacosx-version-min [version]
```

compiler flag is suggested.


# Discussion History
## fluffypony | 2015-04-04T08:43:05+00:00
https://bitcointalk.org/index.php?topic=583449.msg10963108#msg10963108

> There's a bug introduced into the cmake in 0.8.8.6 that broke static builds. This is fixed in head. On OS X you can either wait for 0.8.8.7 RC1 to be tagged and released (after today's mega-merge it's just bug squashing and minor bits before blockchainDB gets merged in), or just use Homebrew to install the dependencies and follow the build instructions in the README (this is not as daunting as it sounds, especially if you ocassionalky use the command-line).

So nothing to do with additional compiler flags:)


# Action History
- Created by: Jojatekok | 2015-04-04T06:49:00+00:00
- Closed at: 2015-04-04T08:43:05+00:00
