---
title: Updating advice
source_url: https://github.com/xmrig/xmrig/issues/3137
author: STUKguy
assignees: []
labels: []
created_at: '2022-10-16T18:28:01+00:00'
updated_at: '2022-10-17T02:06:41+00:00'
type: issue
status: closed
closed_at: '2022-10-17T02:06:41+00:00'
---

# Original Description
Hey,

Just a quick question, I'm assuming that cause i download the repository probably about 4 or 5 months ago that my repo would be out of date. the advice i need is, am i correct in thinking i need to download the repo again and then go into the build folder and run cmake .. & make again?

# Discussion History
## Spudz76 | 2022-10-16T18:44:57+00:00
```
git pull
```

And then you'll be up to date.

## STUKguy | 2022-10-16T21:24:33+00:00
> ```
> git pull
> ```
> 
> And then you'll be up to date.

root@wyse:/home/buzur/xmrig/build# git pull
hint: Pulling without specifying how to reconcile divergent branches is
hint: discouraged. You can squelch this message by running one of the following
hint: commands sometime before your next pull:
hint: 
hint:   git config pull.rebase false  # merge (the default strategy)
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint: 
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
remote: Enumerating objects: 586, done.
remote: Counting objects: 100% (470/470), done.
remote: Compressing objects: 100% (178/178), done.
remote: Total 586 (delta 313), reused 420 (delta 291), pack-reused 116
Receiving objects: 100% (586/586), 539.24 KiB | 3.85 MiB/s, done.
Resolving deltas: 100% (353/353), completed with 144 local objects.
From https://github.com/xmrig/xmrig
   4c57b60e..36afeec2  dev        -> origin/dev
   3ab07fe8..5e13d783  evo        -> origin/evo
   07d53fb7..4948a8c3  sync-base  -> origin/sync-base
Already up to date.

like that?


# Action History
- Created by: STUKguy | 2022-10-16T18:28:01+00:00
- Closed at: 2022-10-17T02:06:41+00:00
