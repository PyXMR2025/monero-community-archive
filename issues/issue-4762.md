---
title: 'gitian: syntax error in gitian-build.py'
source_url: https://github.com/monero-project/monero/issues/4762
author: moneromooo-monero
assignees: []
labels: []
created_at: '2018-10-30T18:07:43+00:00'
updated_at: '2018-12-13T01:49:08+00:00'
type: issue
status: closed
closed_at: '2018-12-13T01:49:08+00:00'
---

# Original Description
Line 168: 
args.commit = (''  if args.commit else) + args.version

There used to be a "else 'v'", but was recently removed.

If it's still supposed to be here, it's weird to cut off the tag's first character and assume it's a 'v'. There might be a good reason ?

# Discussion History
## stoffu | 2018-11-05T06:57:59+00:00
I think
```python
args.commit = ('' if args.commit else 'v') + args.version
```
is correct. As explained in contrib/gitian/README.md, the script is called like this
```
./gitian-build.py --detach-sign --no-commit --build stoffu 0.13.0.4
```
for building tags, or like this
```
./gitian-build.py --detach-sign --no-commit --build --commit stoffu 7e2483e1d565f85efbe0b0ae03ba47acd8ef085d
```
for building commits. When `--commit` is not specified, `args.version` is expected to hold the version tag minus the first `v` character, e.g. `13.0.4.0`, making the final command invoked by the script as `git checkout v13.0.4.0`.

Paging @TheCharlatan 

## moneromooo-monero | 2018-11-05T09:37:41+00:00
That's the original version before it got changed. However, giving a non-commit name without the first character does seem wtf (I'd be really curious to know what reason there could be).


## moneromooo-monero | 2018-12-13T01:15:25+00:00
+resolved

# Action History
- Created by: moneromooo-monero | 2018-10-30T18:07:43+00:00
- Closed at: 2018-12-13T01:49:08+00:00
