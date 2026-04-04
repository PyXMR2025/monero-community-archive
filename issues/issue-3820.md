---
title: v7 sync stuck with --max-concurrency 1
source_url: https://github.com/monero-project/monero/issues/3820
author: GoodMirek
assignees: []
labels: []
created_at: '2018-05-17T09:36:24+00:00'
updated_at: '2018-07-17T14:48:39+00:00'
type: issue
status: closed
closed_at: '2018-07-17T14:48:39+00:00'
---

# Original Description
Affected version is 0.12.0 Lithium Luna. Not sure whether it happens with 0.11.1 Helium Hydra.
Excerpt from the log attached.
[bitmonero.log](https://github.com/monero-project/monero/files/2012571/bitmonero.log)

Monero is running on headless VM. Command line used to run monero:
```
monerod --detach --block-sync-size 1 --max-concurrency 1 --limit-rate 1000
```
After restarting the process synchronisation quickly catches up, but soon happens again.
Running on Linux Fedora Core 27.



# Discussion History
## moneromooo-monero | 2018-05-17T15:03:04+00:00
Do you have the fixes from release-0.12 ?

## GoodMirek | 2018-05-17T16:14:16+00:00
I am not sure what do you mean. I have the release 0.12.0 downloaded as a
tarball from getmonero.org

On Thu, May 17, 2018, 17:03 moneromooo-monero <notifications@github.com>
wrote:

> Do you have the fixes from release-0.12 ?

## moneromooo-monero | 2018-05-17T18:23:43+00:00
Is this:
- the 0.12.0.0 source
- the code from the release-0.12 branch
- something else

You want the second one.

## s-dz | 2018-05-18T00:18:26+00:00
I have same problem for launching new node with 0.12.0.0-master-release code. 

Around syncing block 15000-16000, there are frequently re-org error events in log: `Failed to switch to a lternative blockchain` or ` at insertion invalid by tx returned status existed`.

And also I found that success/failure depends on peer node, i.e. when connected to valid node it successfully re-orged, but failure with invalid node.

So to avoid try this:

1) pop some blocks from ldb by `monero-blockchain-import --pop-blocks (# of blocks to pop)`
2) then `monerod --add-exclusive-node (some IP address of node which have valid chain, you may find at getmonero.org or someplace)`

## moneromooo-monero | 2018-05-18T07:07:33+00:00
This manual popping should not be necessary anymore if you're using current release-0.12, the sync bugs are fixed there.

## stoffu | 2018-05-18T07:35:23+00:00
@moneromooo-monero 
> This manual popping should not be necessary anymore if you're using current release-0.12

PR #3753 which implements automatic block popping is not merged yet to the release-0.12 branch.

@shigakuiwabuchi 
The 0.12.0.0-master-release available from the official download contains sync bugs which are fixed in the current branch. In order to run the bugfixed version, you need to compile it yourself.


## GoodMirek | 2018-05-19T08:57:49+00:00
In my case, for which I originally created this issue, it seems almost sure that the issue is caused by command line option `--max-concurrency 1`.
I tried this option as I run monero node together with other cryptocurrency full nodes on the same VM  and need to limit its resource consumption.
I did not try to compile and run the latest master, so cannot say whether it is already fixed.

I cannot spend more time with this issue. Unless the maintainers of this project wants to keep this issue for reference, I will close it.

## moneromooo-monero | 2018-05-19T09:42:20+00:00
Please keep it open, and you can try again once 0.12.1.0 is released.

## moneromooo-monero | 2018-06-20T08:52:04+00:00
Is this still happening with 0.12.2.0 ?

## GoodMirek | 2018-06-20T09:06:36+00:00
Recently, the sync got stuck even without the --max-concurrency 1 with
0.12.2.0. Restart has helped and it is working well for two days already.
If that works well for at least one week, I will retest  --max-concurrency
1.

Mirek Svoboda | Skype: xsvobo10


## moneromooo-monero | 2018-06-20T09:44:38+00:00
Whether or not it's with --max-concurrency 1, get us a stack trace from gdb:

gdb /path/to/monerod \`pidof monerod\`
thread apply all bt

Then after quitting gdb, try those in case they will work:
status
sync_info
print_cn

and post their outputs too.

## moneromooo-monero | 2018-07-12T22:18:44+00:00
ping, did this happen again, and did you get the info above ?

## GoodMirek | 2018-07-17T14:48:39+00:00
I attempted to sync 3000 block lag, synced w/o issue on 0.12.3.
Command: `monerod --detach --block-sync-size 1 --max-concurrency 1 --limit-rate 1000`

# Action History
- Created by: GoodMirek | 2018-05-17T09:36:24+00:00
- Closed at: 2018-07-17T14:48:39+00:00
