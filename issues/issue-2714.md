---
title: Consider using an individual database file per block
source_url: https://github.com/monero-project/monero/issues/2714
author: heptathlon
assignees: []
labels:
- invalid
created_at: '2017-10-23T05:54:44+00:00'
updated_at: '2018-01-08T13:32:31+00:00'
type: issue
status: closed
closed_at: '2018-01-08T13:32:31+00:00'
---

# Original Description
Right now monero is using one big database blob file stored in `~/.bitmonero/lmdb/data.mdb`, currently sized at around 30GB. Please switch to using one file per (multiple) blocks like Bitcoin, Ethereum and a major part (if not all) other cryptocurrencies are currently doing. This has the advantage of being easier to backup and restore individual blocks (e.g. using a primitive backup program such as Apple Time Machine which backs up every different file as a whole and doesn't support incremental backups on a per file-delta level). Other tools are affected as well.

# Discussion History
## iamsmooth | 2017-10-23T06:28:45+00:00
As a workaround you might store the blockchain database in a [sparse bundle disk image](https://en.wikipedia.org/wiki/Sparse_image#Sparse_bundle_disk_images)

Or just exclude it from Time Machine altogether. You can always restore it from the net, or keep a copy of the .bin file locally.

## ghost | 2017-10-24T13:17:04+00:00
@heptathlon I once asked this same question, and our database guru and inventor of LMDB explained that this is actually a far better structure. I know it's a bit annoying, but for the sake of efficiency I'm willing to put up with it. 

Please just exclude it from your backup

## emesik | 2017-12-09T02:02:52+00:00
Another important problem is that a 30GB file cannot be stored on a FAT filesystem, which is very popular on USB sticks and external drives.

That's a serious issue when someone wants to use an offline computer to serve as cold wallet.

## hyc | 2017-12-09T03:19:44+00:00
This entire ticket is ridiculously stupid. Bitcoin and ethereum use multifile databases and they self-corrupt if you look at them funny. It is physically impossible to prevent a multifile database from self-corrupting.

At this point, SDcards and USBsticks with 64GB or more are using exFAT, and there's no problem. This ticket is utterly garbage.

## Gingeropolous | 2017-12-09T04:33:06+00:00
> This entire ticket is ridiculously stupid.

I just want to celebrate this comment. 

## dEBRUYNE-1 | 2018-01-08T13:20:46+00:00
+invalid

# Action History
- Created by: heptathlon | 2017-10-23T05:54:44+00:00
- Closed at: 2018-01-08T13:32:31+00:00
