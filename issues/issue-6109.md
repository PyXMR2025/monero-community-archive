---
title: v0.15 Binary Release Date?
source_url: https://github.com/monero-project/monero/issues/6109
author: Fenny
assignees: []
labels: []
created_at: '2019-11-08T11:30:34+00:00'
updated_at: '2019-11-11T07:57:29+00:00'
type: issue
status: closed
closed_at: '2019-11-11T07:57:29+00:00'
---

# Original Description
Building on linux keeps hanging on core_rpc_server.cpp.o for hours, I rather wait for the official binaries. 

When can we expect this to be released on the website?

# Discussion History
## moneromooo-monero | 2019-11-08T13:02:25+00:00
This file (and wallet2.cpp and chaingen_main.cpp) require a lot of resources. If it hangs on those, you likely need more RAM, as it's likely starting to swap, which cuts performance hard.


## dEBRUYNE-1 | 2019-11-08T14:13:14+00:00
@Fenny - Should be available soon. If you are particularly impatient, the direct download link is already available:

https://downloads.getmonero.org/cli/monero-linux-x64-v0.15.0.0.tar.bz2

Given that the binary was built deterministically, the hash should match the hashes posted by others in this thread:

https://www.reddit.com/r/Monero/comments/drj72w/cli_v01500_carbon_chamaeleon_has_been_tagged_you/

## trasherdk | 2019-11-08T19:02:26+00:00
I just had to try.
https://downloads.getmonero.org/gui/monero-gui-win-x64-v0.15.0.0.zip
Nothing there :^)

## dEBRUYNE-1 | 2019-11-08T20:30:12+00:00
@trasherdk - Only applies to the CLI. 

## dEBRUYNE-1 | 2019-11-11T07:51:06+00:00
CLI v0.15.0.0 release binaries are available now. 

## dEBRUYNE-1 | 2019-11-11T07:51:11+00:00
+resolved

# Action History
- Created by: Fenny | 2019-11-08T11:30:34+00:00
- Closed at: 2019-11-11T07:57:29+00:00
