---
title: monerod exceeds available memory on shared host server
source_url: https://github.com/monero-project/monero/issues/4608
author: Engelberg
assignees: []
labels: []
created_at: '2018-10-16T02:05:27+00:00'
updated_at: '2018-10-17T01:47:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I've been running monerod on webfaction.com, a shared hosting service with 1gb RAM.

The problem is that whenever a wallet connects to monerod and starts syncing, monerod's memory usage exceeds 1gb and shortly thereafter, the VPS service kills the monerod process.  

I speculate that the problem stems from monerod's tendency to use all available RAM, and on a shared hosting service like webfaction, they set the hard limit on RAM higher than 1gb so in case you occasionally run over for a few seconds, it's not a problem -- to be kind, they only kill your process if you go over for an extended period of time.

The solution, I think, would be for monerod to offer a command-line option to constrain real memory usage to stay within a certain bound, sort of like Java's -Xmx option.  I've noticed this feature request on several monero-related forums over the years, but couldn't find a specific issue for it here in github.

# Discussion History
## hyc | 2018-10-16T14:25:02+00:00
Run the 32bit build, it won't use more than 1GB.

## Engelberg | 2018-10-17T01:47:59+00:00
When I run the 32-bit build, I get the error:
```/lib/ld-linux.so.2: bad ELF interpreter: No such file or directory```

Presumably, that's because it is a 64-bit OS and doesn't have installed the 32-bit C runtime libraries.  As a shared hosting service, I don't have the ability to install new libraries, so I think I would have to recompile the 32-bit build from source, downloading all runtime libraries and then statically linking to those runtime libraries.  Not impossible, but a more complicated solution than I was hoping for -- I'm not terribly familiar with linux build tools and C compilers.

For what it's worth, based on comments I saw on various forums while researching this issue, I get the impression there are other use cases than my own for wanting to limit the memory usage of the 64-bit monerod.



# Action History
- Created by: Engelberg | 2018-10-16T02:05:27+00:00
