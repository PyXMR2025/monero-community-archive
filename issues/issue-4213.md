---
title: Re-enumerating devices while monerod running with --data-dir on a USB drive
  causes the blockchain to become corrupt.
source_url: https://github.com/monero-project/monero/issues/4213
author: malixg
assignees: []
labels: []
created_at: '2018-08-02T16:18:16+00:00'
updated_at: '2022-04-08T15:08:42+00:00'
type: issue
status: closed
closed_at: '2022-04-08T15:08:42+00:00'
---

# Original Description
I am running monerod on Windows 10 x64. My C: drive SSD doesn't have room for the blockchain on it, so I run monerod with --data-dir parameter referencing an external USB hard drive. I have to re-enumerate devices often, and if I ever forget to exit monerod while it's running, before re-enumerating, the whole blockchain becomes corrupt and I have to re-synch from scratch. This has happened to me 4 times and it's very frustrating. Thanks

# Discussion History
## moneromooo-monero | 2018-08-02T16:28:07+00:00
Please define "re-enumerate devices".

## malixg | 2018-08-02T16:54:18+00:00
Go to Windows Device Manager, right click the root node (whatever your Computer Name is) and do Scan For Hardware Changes

## moneromooo-monero | 2018-08-02T17:37:00+00:00
So I guess this just umounts and mounts the filesystem again or something like that. Looks like a Windows filesystem layer bug then.

I'd say "don't run monero until you've finished tinkering with your hardware" and "report a bug to MS' bug tracker if they have one" :)


## dEBRUYNE-1 | 2018-08-03T10:34:44+00:00
@moneromooo-monero: Would the `--db-sync-mode=safe` flag guard against a corruption in this particular scenario? 

## moneromooo-monero | 2018-08-03T12:54:22+00:00
No idea, you'd have to try it and see, but I doubt it does given mmap is used in all cases (that said, it's windows, so maybe there is a difference there).

In any case, if Windows somehow allows writes without error when they corrupt the file, it's a Windows bug (unless LMDB writes directly to the device, but I doubt it does).


## selsta | 2022-04-08T15:08:42+00:00
There were no other reports about having to "re-enumerate devices", so I'll close this. If this continues to be an issue please comment and I can reopen.

# Action History
- Created by: malixg | 2018-08-02T16:18:16+00:00
- Closed at: 2022-04-08T15:08:42+00:00
