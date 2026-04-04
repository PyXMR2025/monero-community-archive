---
title: monerod using tons of bandwidth after 100% synced blockchain
source_url: https://github.com/monero-project/monero/issues/3043
author: rex4539
assignees: []
labels:
- invalid
created_at: '2018-01-01T00:24:04+00:00'
updated_at: '2018-01-31T07:20:03+00:00'
type: issue
status: closed
closed_at: '2018-01-30T10:08:36+00:00'
---

# Original Description
Monero 'Helium Hydra' (v0.11.1.0-release)

Reproducibility: always

Steps:
Have monerod running with blockchain already 100% synced.

What happened:
monerod constantly uses tons of bandwidth.

Expected result:
monerod uses minimal bandwidth since the blockchain is already synced. There shouldn't be need for such massive use of bandwidth after the blockchain has synced.

Notes:
Looks like monerod uses some kind of P2P functionality to seed the blockchain to other nodes that have not yet synced to help propagate the blockchain. But why the need for such massive use of bandwidth? This forces me to shut down the daemon as soon as I quit the app. zcashd for example uses minimal bandwidth so I basically keep it running 24/7 without even noticing the bandwidth use.

# Discussion History
## moneromooo-monero | 2018-01-01T11:37:58+00:00
Run "set_log 0,net.cn:DEBUG" and post the log after running for, say, 5 minutes while this massive bandwidth use is going on.



## rex4539 | 2018-01-01T11:52:29+00:00
[bitmonero.log](https://github.com/monero-project/monero/files/1595891/bitmonero.log)


## moneromooo-monero | 2018-01-01T11:56:40+00:00
Looks like the daemon is far from synced. What do you think it is ?

## rex4539 | 2018-01-01T12:02:12+00:00
The daemon is definitely synced, according to the GUI status log.

`Height: 1477572/1477572 (100.0%) on mainnet, not mining, net hash 573.53 MH/s, v6, up to date, 10(out)+1(in) connections, uptime 0d 0h 1m 0s`

## moneromooo-monero | 2018-01-01T12:23:23+00:00
It looks like it's downloading from near the start of the chain, but not seeing these are blocks it already has. If it's not saying "ADDED AS ALTERNATIVE", however, it's blocks it already has, that's very odd. Can you send another log with this: `set_log 1,net.cn:DEBUG,*blockchain*:DEBUG,cn:DEBUG,txpool:DEBUG`

Also, the output of:

`mdb_stat -a ~/.bitmonero/lmdb`

mdb_stat should be in a lmdb package. If not, its source are in external/db_drivers/liblmdb

## rex4539 | 2018-01-01T12:41:24+00:00
ok, I know why the bitmonero.log showed different things.

I use MacOS and the GUI uses ~/Library/Application Support/Monero instead of ~/.bitmonero in Linux.

So running monerod directly from Terminal (instead of the GUI) somehow created a new ~/.bitmonero folder and started downloading from scratch...

I guess that's a separate bug perhaps. Running monerod on MacOS should always use the native MacOS folder ~/Library/Application Support

Hold on, will run monerod with --data-dir arg and post new log.

## moneromooo-monero | 2018-01-01T12:48:15+00:00
Looking at the source, it looks like monerod should also use ~/Library/Application Support when on mac. Please flie another bug for this, it'll have to be looked at by someone with a mac.

## rex4539 | 2018-01-01T13:14:19+00:00
In this session, monerod was constantly uploading to various IPs.

[bitmonero.log](https://github.com/monero-project/monero/files/1596042/bitmonero.log)


## rex4539 | 2018-01-01T13:17:05+00:00
Oops, forgot to enter the latest args you posted later. New logs coming up shortly.

## rex4539 | 2018-01-01T13:26:35+00:00
Log with `set_log 1,net.cn:DEBUG,*blockchain*:DEBUG,cn:DEBUG,txpool:DEBUG`

[bitmonero.log](https://github.com/monero-project/monero/files/1596052/bitmonero.log)


## rex4539 | 2018-01-01T13:34:41+00:00
Output of `mdb_stat -a ~/Library/Application Support/Monero/lmdb`

```
Status of Main DB
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 13
Status of block_heights
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1477608
Status of block_info
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1477608
Status of blocks
  Tree depth: 4
  Branch pages: 542
  Leaf pages: 121558
  Overflow pages: 34
  Entries: 1477608
Status of hf_versions
  Tree depth: 3
  Branch pages: 34
  Leaf pages: 7244
  Overflow pages: 0
  Entries: 1477608
Status of output_amounts
  Tree depth: 4
  Branch pages: 530
  Leaf pages: 80661
  Overflow pages: 0
  Entries: 25947286
Status of output_txs
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 25947286
Status of properties
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1
Status of spent_keys
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 22267827
Status of tx_indices
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 3684442
Status of tx_outputs
  Tree depth: 4
  Branch pages: 305
  Leaf pages: 68028
  Overflow pages: 2383
  Entries: 3684442
Status of txpool_blob
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 80
  Entries: 17
Status of txpool_meta
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 17
Status of txs
  Tree depth: 4
  Branch pages: 1096
  Leaf pages: 246254
  Overflow pages: 8236112
  Entries: 3684442
```

## moneromooo-monero | 2018-01-01T15:07:19+00:00
Uploading's fine/expected. Lots of new people starting off with monero. It doesn't seem to be doing this constantly though. If it's too much, you can limit upload rate with --limit-up N (IIRC N is kB/s). Same with --limit-down N.

The mdb_stat output looks good, but that is now expected since you found out why early blocks were being requested.


## rex4539 | 2018-01-01T15:20:49+00:00
Well, fine/expected is not good. I believe it needs to be changed.

I mean, it uses massive bandwidth and degrades my internet experience. Almost brings internet to a halt. And I'm on a reasonably fast connection.

![screen shot 2018-01-01 at 17 18 36](https://user-images.githubusercontent.com/227442/34468737-eb2344bc-ef17-11e7-8788-343ce2b5669d.png)


Is it a big deal to limit the bandwidth by default in the next GUI update?

I run the GUI and don't want to constantly use the command line.

Please? :)

## moneromooo-monero | 2018-01-01T15:29:48+00:00
The log did not show massive use though. Maybe that log was in a lull. You can specify whatever options you want for the daemon in the GUI, in the settings page I believe. Those should be persistent (if not, it's a bug). Automatically guessing what a good value is for the local connection is maybe doable, but that doesn't seem trivial to guess.


## rex4539 | 2018-01-01T15:55:03+00:00
Just as a reference for the next person looking to manually limit the rate in the GUI, the following commands are available.

```
  --limit-rate-up arg (=-1)             set limit-rate-up [kB/s]
  --limit-rate-down arg (=-1)           set limit-rate-down [kB/s]
  --limit-rate arg (=-1)                set limit-rate [kB/s]
```

## rex4539 | 2018-01-01T16:00:39+00:00
I hope some developer can pick this up and limit the bandwidth use.

## dEBRUYNE-1 | 2018-01-03T15:44:47+00:00
To add to @rex4539 comment, I wrote a guide for limiting bandwidth in the GUI:

https://monero.stackexchange.com/questions/6653/the-gui-uses-all-my-bandwidth-and-i-cant-browse-anymore-or-use-another-applicat
  

## moneromooo-monero | 2018-01-04T13:04:55+00:00
> I use MacOS and the GUI uses ~/Library/Application Support/Monero instead of ~/.bitmonero in Linux.

You didn't set it yourself, right ? This was the default ?

## rex4539 | 2018-01-04T13:11:53+00:00
Actually, I did set it myself back then it seems and forgot about it.

The standard macOS behavior for apps is to use ~/Library/Application Support instead of ~/ that is Unix behavior so I took it for granted.

Still, the fundamental issue exists. If a user changes the setting within the GUI and then run monerod from the command line, it will create ~/.bitmonero and start downloading the blockchain from scratch.

So my suggestion is to use a config file to store those kind of settings. So if a user changes the location in the GUI but then runs monerod from the command line, it will automatically pick up the location selected in the GUI.

## moneromooo-monero | 2018-01-30T09:53:01+00:00
I'll close as invalid, since it turned out to be normal, and there are options to limit network usage if that is wanted.

+invalid


## rex4539 | 2018-01-30T10:03:58+00:00
I would argue it's not "normal" to cripple someone's bandwidth :)

So I disagree with the "invalid" tag and would like to reopen the report until it is fixed (eg. bandwidth use is limited by default).

This is a valid report.

Sure, it's nice that we give the user the option to limit the bandwidth use but the main issue (and fact) is that monerod is using tons of bandwidth (and, mind you, after the blockchain has downloaded) and that could be limited by default (and then user could increase it in the command line argument, if desired).

My 0.000066 XMR

## SamsungGalaxyPlayer | 2018-01-31T07:20:03+00:00
@rex4539 I suggest opening a different issue to suggest default bandwidth limitations.

# Action History
- Created by: rex4539 | 2018-01-01T00:24:04+00:00
- Closed at: 2018-01-30T10:08:36+00:00
