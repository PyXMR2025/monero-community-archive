---
title: 'monerod for SunOS: compiled successfully, weirdness ensues'
source_url: https://github.com/monero-project/monero/issues/5805
author: kayront
assignees: []
labels: []
created_at: '2019-08-11T08:10:09+00:00'
updated_at: '2019-08-25T09:51:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[typescript.txt](https://github.com/monero-project/monero/files/3489665/typescript.txt)

Suspect this is related to #5804 ..

```
$ file bin/monerod 
bin/monerod:    ELF 64-bit LSB executable **AMD64** Version 1, dynamically linked, not stripped, no debugging information available
```

compare:

```
$ file /bin/prstat
/bin/prstat:    ELF 32-bit LSB executable **80386** Version 1, dynamically linked, not stripped, no debugging information available
```



# Discussion History
## hyc | 2019-08-18T12:23:30+00:00
I don't see what issue you're pointing out. You apparently compiled monerod for a 64bit architecture. What's the problem?

## kayront | 2019-08-25T09:51:21+00:00
The 32-vs-64 issue was an assumption on my part, I thought that perhaps SunOS does something odd with that seeing that my system binaries are 32 bit, on a 64 bit machine (unusual in other *nix).

But that is not the problem at all, third-party software from pkgsrc randomly inspected is all 64 bit binaries.

I have no idea what the problem might be, but it is clear from running the binary that something went horribly wrong at some point - see the typescript.

# Action History
- Created by: kayront | 2019-08-11T08:10:09+00:00
