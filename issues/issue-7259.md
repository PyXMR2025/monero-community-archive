---
title: Segmentation error when syncing Armv8 Rock64
source_url: https://github.com/monero-project/monero/issues/7259
author: SomaticFanatic
assignees: []
labels: []
created_at: '2021-01-01T19:34:28+00:00'
updated_at: '2022-03-16T15:53:06+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:53:06+00:00'
---

# Original Description
Constant segmentation faults when syncing new node from scratch on RockPro64 Armv8 using binaries downloaded from GetMonero.org. Error happens perhaps every 10% synced, and not with any regularity. Sometimes can go 25% before erroring, sometimes just 3%. Happens both on pruned and non-pruned syncs.

`sudo ./monerod --restricted-rpc --ban-list block_tor.txt --prune-blockchain --log-level 2`

Note: I have to run monerod as sudo or else it says Permission denied.

Daemon log: https://pastebin.com/u1b0yHxf

Gdb: https://pastebin.com/TA7Hfe13

# Discussion History
## moneromooo-monero | 2021-01-01T20:22:21+00:00
Are you always using the same storage device ?

## SomaticFanatic | 2021-01-01T21:13:34+00:00
Yes

## moneromooo-monero | 2021-01-01T21:26:01+00:00
Use another.

## SomaticFanatic | 2021-01-01T22:27:45+00:00
I don’t understand. Right now I’m syncing via a SSD on the USB3 port. Are you saying I should try another drive or not use USB to SSD at all?

## SomaticFanatic | 2021-01-01T22:30:50+00:00
New GDB: https://pastebin.com/vn8hBbU7

## moneromooo-monero | 2021-01-02T13:10:43+00:00
Yes. A crash in cryptonote::BlockchainLMDB::compare_uint64 hints at a broken database, and a broken database several times in a row hints at hardware failiure.

## moneromooo-monero | 2021-01-02T13:11:46+00:00
The new stack looks more like memory corruption though.

## SomaticFanatic | 2021-01-02T14:08:49+00:00
> Yes. A crash in cryptonote::BlockchainLMDB::compare_uint64 hints at a broken database, and a broken database several times in a row hints at hardware failiure.

Should I try a different SSD or switching away from USD>SSD altogether and use the MicroSD card slot?

## moneromooo-monero | 2021-01-02T15:46:48+00:00
The microsd sounds like it's totally different hw so is best to try that.

## selsta | 2021-01-03T02:33:50+00:00
#7271 might be related

## komatom | 2021-01-04T11:25:00+00:00
Monerod recently closes itself without reasons on my node on Ubuntu 20.04, I though .8 point version would fix it, but apparently ti is not, it continues to do that.. just kills itself after an hour or so.

## SomaticFanatic | 2021-01-05T02:58:57+00:00
I moved to a different SSD and it still errored. I moved to a MicroSD and it errored. Perhaps memory corruption? I ordered a new Rock board so hopefully that fixes it. 

## selsta | 2021-01-05T04:11:18+00:00
@komatom See here: https://reddit.com/r/Monero/comments/ko3d1n/third_update_on_the_ongoing_network_attacks/

## selsta | 2021-01-05T19:50:08+00:00
@SomaticFanatic It seems to be a bug in our code.

## SomaticFanatic | 2021-01-19T13:48:02+00:00
@selsta Is the bug confirmed and is it fixed?

## selsta | 2021-01-19T14:14:06+00:00
@SomaticFanatic do you know how to compile a specific PR? #7309 might resolve your issue.

## SomaticFanatic | 2021-01-24T03:50:19+00:00
@selsta I do. Will compile and get back to this

## SomaticFanatic | 2021-01-25T17:49:01+00:00
@selsta Built from scratch. Sync from scratch. Seg fault. 

## selsta | 2021-01-25T17:49:46+00:00
Ok, that means 7309 is not related to your issue.

## selsta | 2021-01-25T17:58:34+00:00
@SomaticFanatic can you try compiling a debug build and then doing `thread apply all bt` in gdb?

## SomaticFanatic | 2021-01-26T20:38:21+00:00
@selsta I tried `make debug -d` and it freezes at 81%. I tried increasing swap file to 6GB and it doesn't matter. Still freezes at 81%: https://pastebin.com/mD9S5keW

## SomaticFanatic | 2021-01-27T01:06:25+00:00
If you want I can remove the -d flag for a less noisy output

## selsta | 2021-01-27T08:27:31+00:00
You can do

make -C path/to/build/directory daemon

to build only daemon.

Build will take a while so be patient. Build directory is where e.g. the bin folder is inside.

If this does not work gdb output from release + 7309 should be fine too.

## selsta | 2021-01-27T08:30:27+00:00
Also which distro are you using from here? https://wiki.pine64.org/wiki/ROCKPro64_Software_Release#Armbian

## SomaticFanatic | 2021-01-27T17:33:17+00:00
I’m definitely being patient. It would error at 81% after being left all night. I have to ^C it to stop it only if I catch it early enough. Otherwise it just is locked up at 81%. 

If I do make -C build/directory daemon it says 

make *** No rule to make target ‘daemon’. Stop. 

and quits. The distro I’m using is https://github.com/ayufan-rock64/linux-build/releases/tag/0.9.14 Ubuntu 18

I’ll make + 7309 instead

## SomaticFanatic | 2021-03-28T01:24:41+00:00
@selsta 7309 was merged. Built from current master, began sync from scratch, and it is still segfaulting. Should I post the gdb?

Edit: I’m running Bionic from here: https://github.com/ayufan-rock64/linux-build/releases/tag/0.9.14

## selsta | 2021-03-28T12:03:00+00:00
@SomaticFanatic Can you use https://paste.debian.net/hidden/c939360a/ to make a debug build and then try to reproduce the segfault under gdb?

## selsta | 2021-03-28T12:37:40+00:00
https://forum.pine64.org/showthread.php?tid=11209&pid=76615#pid76615

Could it be that the Rock64 is simply unstable during high load? Can you try reducing memory clock?

## selsta | 2022-02-19T00:57:31+00:00
ping @SomaticFanatic, did you check regarding memory clock? Otherwise I will close this issue.

# Action History
- Created by: SomaticFanatic | 2021-01-01T19:34:28+00:00
- Closed at: 2022-03-16T15:53:06+00:00
