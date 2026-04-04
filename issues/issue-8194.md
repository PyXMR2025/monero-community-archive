---
title: Syncing gets stuck around block >~2450000
source_url: https://github.com/monero-project/monero/issues/8194
author: tryphe
assignees: []
labels: []
created_at: '2022-02-27T03:29:12+00:00'
updated_at: '2024-07-31T23:21:49+00:00'
type: issue
status: closed
closed_at: '2024-07-31T23:21:49+00:00'
---

# Original Description
**Describe the problem**

Behavior: At some point after starting monerod, ranging from a few minutes to many hours, syncing "gets stuck". Whether synced or unsynced, blocks stop being added to the chain until monerod is restarted. The monerod process continues running and is responsive, however, and exits normally if given HUP etc.

The behavior repeatedly appears for me, in particular, starting around block >~2450000. Not any specific block, just random, but not at any point before ~2450000.  If monero is already synced, it takes longer for the behavior to appear, sometimes several hours longer.

There are plenty of connections and new connections being made during the behavior.
Monerod gives me two messages like this every few minutes, gives the correct number of total blocks, but is still stuck at the same block where the behavior appeared:
```
[random.ipv4.address:18080 OUT] Sync data returned a new top block candidate: 2459334 -> 2568414 [Your node is 109080 blocks (5.0 months) behind] 
SYNCHRONIZATION started 
```

Workaround: If I create a cron script to restart monerod every ~15 minutes, it eventually syncs.


**A few things about my node and what I've tried:**

I've been running monero for over 5 years with no syncing issues, until about a month ago.
Minimal setup Debian 10 VM with ntpd and monerod (Update: tried with a new Debian 11 machine and the same behavior occurs).
Syncing works fine until about 95%, or near block 2450000.
Removed the entire .bitmonero directory and synced from scratch several times with the same result.
Removed my config and am running with no arguments to reduce complexity, but get the same result.
Running on clearnet.
Using the blocklist at https://gui.xmr.pm/files/block.txt, but I tried without the blocklist and get the same result.
Using outbound connections only to try and sync currently to avoid possibility of attack.
Tried running with things like `--out-peers 25` or `--out-peers 50` but get the same result.
Running the latest master branch 9aab19f349433687c7aaf2c1cbc5751e5912c0aa but also tried with signed releases:
```
0.17.3.0
0.17.2.0
0.17.1.9
0.17.1.7
0.17.1.5
0.17.1.3
```
which experience the same behavior but do NOT show errors in the log.

**Update: I originally thought the syncing problem was related to these errors, but this is not the case. Will leave this section here**

Some errors/warnings that frequently occur:
```
ERROR   net     contrib/epee/include/net/abstract_tcp_server2.inl:777   Setting timer on a shut down object

ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1226    [3.230.147.95:18080 OUT] sent wrong NOTIFY_RESPONSE_GET_OBJECTS: block with id=cffef4cadcddc0a72007c8c07e1a5cce4bcd41b2e7fa1013aa70de02b96b1208 wasn't requested, dropping connection 

WARNING net.p2p src/p2p/net_node.inl:1173       [209.222.252.101:18180 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
```

There's also a loop that produces hundreds of these at once for the same peer:
```
2022-02-27 03:16:49.624 I [45.154.254.133:18080 OUT] [0] state: stopping adding blocks in state synchronizing
2022-02-27 03:16:49.624 I [45.154.254.133:18080 OUT] [0] state: resuming in state synchronizing
2022-02-27 03:16:49.625 I [45.154.254.133:18080 OUT] [0] state: will try to add blocks next in state synchronizing
2022-02-27 03:16:49.625 I [45.154.254.133:18080 OUT] [0] state: adding blocks in state synchronizing
2022-02-27 03:16:49.626 I [45.154.254.133:18080 OUT]  parent was requested, we'll get back to it
```

Here's a short run:
https://gist.githubusercontent.com/tryphe/0a09526e0c9aa1e6154b4e2b0c6e2e13/raw/a56cca8895370d6e91a27b5f4a4b887d4e064d2d/gistfile1.txt
(Note: I gave the hangup signal near 03:16:52.049 where it shuts down cleanly)

Any feedback is welcome and appreciated. Let me know if you need more information or if I can do anything to make debugging easier. Thank you.

# Discussion History
## selsta | 2022-02-27T03:32:22+00:00
> Syncing works fine until about 95%, or near block 2450000.

What exactly happens then? Does it stay stuck on the same block and stop syncing?

Does it start to ban other peers?

## tryphe | 2022-02-27T03:35:04+00:00
> > Syncing works fine until about 95%, or near block 2450000.
> 
> What exactly happens then?
> Does it start to ban other peers?

The errors and warnings stated above happen constantly (see gist for details) until I give the hangup signal around `03:16:52.049`. No blocks get added to the chain. It doesn't matter if I wait an hour, or 5 minutes, the log looks the same, so I gave a short log.

Indeed, peers are banned.

## tryphe | 2022-02-27T03:51:56+00:00
One thing I didn't mention, if I continually restart the daemon, it seems to sync a few chunks of 20 blocks upon start, but it only works for a minute or two until getting stuck like in the log.

It's obvious to me that there are some malicious nodes out there just handing me junk blocks. But could it really be an eclipse attack? It seems to me like adding more peers would reduce the chance quite a bit, but I'm not sure the problem here is just that. It seems like maybe a combination of a bug and malicious peers, but that's just speculation.

## selsta | 2022-02-27T03:56:25+00:00
Which log level is the log you posted?

> It's obvious to me that there are some malicious nodes out there just handing me junk blocks. But could it really be an eclipse attack?

You appear to have this issue for a month and no one else reported something similar so I don't think so, otherwise there would be more reports about similar issues.

It's probably either an issue with your setup or a bug that gets triggered in your setup, but looking at the logs I don't see anything obvious yet.

## tryphe | 2022-02-27T03:58:03+00:00
> Which log level is the log you posted?
> 
> > It's obvious to me that there are some malicious nodes out there just handing me junk blocks. But could it really be an eclipse attack?
> 
> You appear to have this issue for a month and no one else reported something similar so I don't think so, otherwise there would be more reports about similar issues.
> 
> It's probably either an issue with your setup or a bug that gets triggered in your setup, but looking at the logs I don't see anything obvious yet.

Log level 1. Let me know if you want a different log level.

## selsta | 2022-02-27T03:58:55+00:00
Can you post log level 2?

## tryphe | 2022-02-27T04:24:23+00:00
Thanks for your quick feedback. I use the same VM image for several coin daemons, and only Monero has syncing problems, but it's the only cryptonote coin I run. I can't really imagine a more generic setup, but after searching around, you're definitely right that no one seems to have this problem.

I'll make a clean VM and see how that does.

Log level 2: https://gist.githubusercontent.com/tryphe/2436c1e1a5ea21d7d3c678bd5567e396/raw/69d6a726a8fe45378bc0e6869cab1a5bbe11cceb/gistfile1.txt



## tryphe | 2022-02-27T04:43:37+00:00
I did a quick dist-upgrade to Debian 11 without rebuilding Monero and the problem seems to have resolved itself. Really strange. No problems now. Why it happens at 95% synced is beyond me. It doesn't happen at earlier blocks.

It seems that running Debian 10 and other non-new distros should be advised against. Debian 10 is "oldstable" which is still supported, so that's mildly concerning that people are probably using it still.

I'll post some new logs so they can be compared against the ones that failed.

## tryphe | 2022-02-27T05:00:41+00:00
Log level 2 after the problem was resolved by upgrading to Debian 11: https://gist.githubusercontent.com/tryphe/fac92713a0fab5aa6a75c6ae40905573/raw/c3262979e8e0f299b290bde46ac096c48cd6e144/gistfile1.txt

Thanks again for your feedback @selsta!

I can't spot anything in the log that's different. The warnings and errors look the same. It must be related to some buggy lower level library running on some Linux distributions.

Hopefully this might help someone that has a similar setup but this does not necessary qualify as a Monero issue. Maybe a check for some older library could be enforced, although frankly I have no idea which library it could be :stuck_out_tongue: 

## selsta | 2022-02-27T18:28:15+00:00
Does everything still work? It's unlikely that your OS version is related here.

## tryphe | 2022-02-28T23:03:09+00:00
@selsta yes. Ran dist-upgrade, did nothing else, and it's been synced ever since. I upgraded from Buster (Debian 10) which was up to date via apt, so there's a problem there.

## tryphe | 2022-03-01T22:08:40+00:00
It started doing it again today and now the node is behind. Will try and make a new machine. And again, none of my other coin daemons have this problem, so it's a monero problem. But it doesn't really make sense that i was able to sync ~100k blocks fine at a point where it was stuck, and then nothing.

## selsta | 2022-03-01T22:15:39+00:00
```
19:02 <+moneromooo> The first few blocks that are needed are requested from a peer that doesn't send them.
19:02 <+moneromooo> The timeout seems to be 25 seconds here.
19:04 <+moneromooo> The blocks then get requested from another peer, but that peer gets dropped after it sends a reply to another message. Possible state machine bug here.
19:31 <+moneromooo> There are two instances of possible large delays in networking. So, who knows.
```

That's what moneromooo saw from the logs. Now it still doesn't explain why there aren't more reports about this. I guess testing a different machine would be helpful.

## selsta | 2022-03-01T22:19:03+00:00
```
23:13 <hocuspocusoutoff> so... possibly not related at all since user's details dont match mine, but i had similar symptoms when i tried my first sync. i am hosting the blockchain on a NAS while daemon runs on my server. the NAS had some goofy-ass software that "indexed" things every time a change was made on disk. this basically caused the sync to grind to a halt somewhere around the same block height user is mentioning. once i was able to turn that
23:13 <hocuspocusoutoff> nonsense off, sync finished cleanly
```

Not sure if this is helpful for your setup but I thought I'd add it too.

## snex | 2022-03-01T23:44:41+00:00
Hi @selsta , I had a similar issue when trying to host the blockchain on my NAS. Turned out the problem was the NAS had some hidden service that "reindexed" its files every time *ANY* change was made on disk. This would lead monerod and this index service to compete for access to the file, which would grind the whole thing to a halt. Once I removed this NAS service, I was able to full sync from 0 in about 1.5 days total, with zero issues.

Could you possibly also have a similar service interfering with your blockchain file?

## tryphe | 2022-03-03T22:19:22+00:00
I was able to reproduce the bug with a new KVM instance with Debian 11 amd64 (vm software is up to date, host is up to date). Host is running other coin daemons with a similar setup. I tried to get a setup that is most similar to the one producing the bug.

Steps I took:
1. Install fresh Debian 11 netinst amd64. Ext4 partition, auto format, default options. Unchecked all debian features except xfce (Edit: after trying without xfce below, the bug seems unrelated to X, so choose which you prefer).
3. Configure static ip via `/etc/network/interfaces`
4. Remove crap: `apt remove network-manager network-manager-gnome light-locker xiccd pipewire colord system-config-printer gvfs gpg-agent tumbler at-spi2-core geoclue-2.0 policykit-1-gnome`
5. `apt autoremove`
6. Reboot and make sure no extra crap is running besides basic system processes and lightdm child processes.
7. Build Monero from source via instructions from README. In the OP I built via docker. This time I built without docker and still got the bug.
8. Execute `./monerod` and let it run. It will get stuck near block 2400000 to 2500000.

`$ gcc -v`:
`gcc version 10.2.1 20210110 (Debian 10.2.1-6)`

`$ uname -a`:
`Linux debian11 5.10.0-11-amd64 #1 SMP Debian 5.10.92-1 (2022-01-18) x86_64 GNU/Linux`

`$ ps -aux` (besides kernel processes) :
```
/sbin/init
/lib/systemd/systemd-journald
/lib/systemd/systemd-udevd
/usr/sbin/cron
/usr/bin/dbus-daemon
/usr/sbin/rsyslogd
/lib/systemd/systemd-logind
/usr/libexec/udisks2/udisksd
/usr/libexec/polkitd
/usr/sbin/lightdm
/usr/lib/xorg/Xorg
/sbin/agetty
/lib/systemd/systemd
(sd-pam)
xfce4-session
/usr/bin/dbus-daemon
/usr/bin/ssh-agent
/usr/lib/x86_64-linux-gnu/xfce4/xfconf/xfconfd
xfwm4
xfsettingsd
xfce4-panel
Thunar --daemon
xfdesktop
/usr/lib/x86_64-linux-gnu/xfce4/notifyd/xfce4-notifyd
/usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libsystray.so
/usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libnotification-plugin.so
/usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /usr/lib/x86_64-linux-gnu/xfce4/panel/plugins/libactions.so
xterm
bash
./monerod
/usr/libexec/dconf-service
```
It got all the way up to and stuck at block ~2508000 for hours, with many peers and lots of network traffic. Restarted the daemon, and it's syncing okay again for a few minutes. Same issue as in OP. We'll see how long until it gets stuck again.

I'll try to see if I can reproduce without x running (`sudo service lightdm stop` and switch to another tty)

## selsta | 2022-03-03T22:21:12+00:00
Is the blockchain stored inside the VM or on an external network drive?

## tryphe | 2022-03-03T22:26:21+00:00
> Is the blockchain stored inside the VM or on an external network drive?

> Could you possibly also have a similar service interfering with your blockchain file?

The blockchain is always stored locally and no processes are running that seem like they could interfere. Most processes have a fraction of a second of total cpu time used.

## tryphe | 2022-03-04T00:58:24+00:00
The steps taken above were an effort to try and reproduce the bug on a different VM but on an identical setup. The problem still occurred.

I've taken some additional steps to reduce the complexity and was able to reproduce the bug without X or related processes running ie. xfcond and I was still able to reproduce the bug.

`ss -t` gives me 13 outbound peers
`nload` tells me there is around 0.5-1mbps burst and <0.5 average traffic, as opposed to >5mbps average while syncing blocks successfully.

`ps aux` gives me (after I closed monerod):
```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.2  98204 10216 ?        Ss   17:30   0:04 /sbin/init
root           2  0.0  0.0      0     0 ?        S    17:30   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   17:30   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   17:30   0:00 [rcu_par_gp]
root           6  0.0  0.0      0     0 ?        I<   17:30   0:00 [kworker/0:0H-events_highpri]
root           8  0.0  0.0      0     0 ?        I<   17:30   0:00 [mm_percpu_wq]
root           9  0.0  0.0      0     0 ?        S    17:30   0:00 [rcu_tasks_rude_]
root          10  0.0  0.0      0     0 ?        S    17:30   0:00 [rcu_tasks_trace]
root          11  0.0  0.0      0     0 ?        S    17:30   0:00 [ksoftirqd/0]
root          12  0.1  0.0      0     0 ?        I    17:30   0:07 [rcu_sched]
root          13  0.0  0.0      0     0 ?        S    17:30   0:00 [migration/0]
root          14  0.0  0.0      0     0 ?        I    17:30   0:00 [kworker/0:1-mm_percpu_wq]
root          15  0.0  0.0      0     0 ?        S    17:30   0:00 [cpuhp/0]
root          16  0.0  0.0      0     0 ?        S    17:30   0:00 [cpuhp/1]
root          17  0.0  0.0      0     0 ?        S    17:30   0:00 [migration/1]
root          18  0.0  0.0      0     0 ?        S    17:30   0:00 [ksoftirqd/1]
root          20  0.0  0.0      0     0 ?        I<   17:30   0:00 [kworker/1:0H-events_highpri]
root          21  0.0  0.0      0     0 ?        S    17:30   0:00 [cpuhp/2]
root          22  0.0  0.0      0     0 ?        S    17:30   0:00 [migration/2]
root          23  0.0  0.0      0     0 ?        S    17:30   0:07 [ksoftirqd/2]
root          25  0.0  0.0      0     0 ?        I<   17:30   0:00 [kworker/2:0H-events_highpri]
root          26  0.0  0.0      0     0 ?        S    17:30   0:00 [cpuhp/3]
root          27  0.0  0.0      0     0 ?        S    17:30   0:00 [migration/3]
root          28  0.0  0.0      0     0 ?        S    17:30   0:00 [ksoftirqd/3]
root          30  0.0  0.0      0     0 ?        I<   17:30   0:00 [kworker/3:0H-events_highpri]
root          34  0.0  0.0      0     0 ?        S    17:30   0:00 [kdevtmpfs]
root          35  0.0  0.0      0     0 ?        I<   17:30   0:00 [netns]
root          36  0.0  0.0      0     0 ?        S    17:30   0:00 [kauditd]
root          37  0.0  0.0      0     0 ?        S    17:30   0:00 [khungtaskd]
root          38  0.0  0.0      0     0 ?        S    17:30   0:00 [oom_reaper]
root          39  0.0  0.0      0     0 ?        I<   17:30   0:00 [writeback]
root          40  0.0  0.0      0     0 ?        S    17:30   0:01 [kcompactd0]
root          41  0.0  0.0      0     0 ?        SN   17:30   0:00 [ksmd]
root          42  0.0  0.0      0     0 ?        SN   17:30   0:02 [khugepaged]
root          63  0.0  0.0      0     0 ?        I<   17:30   0:00 [kintegrityd]
root          64  0.0  0.0      0     0 ?        I<   17:30   0:00 [kblockd]
root          65  0.0  0.0      0     0 ?        I<   17:30   0:00 [blkcg_punt_bio]
root          66  0.0  0.0      0     0 ?        I<   17:30   0:00 [edac-poller]
root          67  0.0  0.0      0     0 ?        I<   17:30   0:00 [devfreq_wq]
root          68  0.1  0.0      0     0 ?        I<   17:30   0:15 [kworker/1:1H-kblockd]
root          69  0.0  0.0      0     0 ?        S    17:30   0:01 [kswapd0]
root          70  0.0  0.0      0     0 ?        I<   17:30   0:00 [kthrotld]
root          71  0.0  0.0      0     0 ?        I<   17:30   0:00 [acpi_thermal_pm]
root          72  0.5  0.0      0     0 ?        I<   17:30   0:40 [kworker/3:1H-kblockd]
root          73  0.0  0.0      0     0 ?        I<   17:30   0:00 [ipv6_addrconf]
root          82  0.0  0.0      0     0 ?        I<   17:30   0:00 [kstrp]
root          85  0.0  0.0      0     0 ?        I<   17:30   0:00 [zswap-shrink]
root          86  0.0  0.0      0     0 ?        I<   17:30   0:00 [kworker/u9:0]
root         135  0.0  0.0      0     0 ?        I<   17:30   0:00 [ata_sff]
root         136  0.0  0.0      0     0 ?        S    17:30   0:00 [scsi_eh_0]
root         137  0.0  0.0      0     0 ?        I<   17:30   0:00 [scsi_tmf_0]
root         138  0.0  0.0      0     0 ?        S    17:30   0:00 [scsi_eh_1]
root         139  0.0  0.0      0     0 ?        I<   17:30   0:00 [scsi_tmf_1]
root         144  0.0  0.0      0     0 ?        S    17:30   0:00 [scsi_eh_2]
root         145  0.0  0.0      0     0 ?        I<   17:30   0:00 [scsi_tmf_2]
root         147  0.0  0.0      0     0 ?        S    17:30   0:02 [irq/18-vmwgfx]
root         148  0.0  0.0      0     0 ?        I<   17:30   0:00 [ttm_swap]
root         149  0.0  0.0      0     0 ?        S    17:30   0:00 [card0-crtc0]
root         150  0.0  0.0      0     0 ?        S    17:30   0:00 [card0-crtc1]
root         151  0.0  0.0      0     0 ?        S    17:30   0:00 [card0-crtc2]
root         152  0.0  0.0      0     0 ?        S    17:30   0:00 [card0-crtc3]
root         153  0.0  0.0      0     0 ?        S    17:30   0:00 [card0-crtc4]
root         154  0.0  0.0      0     0 ?        S    17:30   0:00 [card0-crtc5]
root         155  0.0  0.0      0     0 ?        S    17:30   0:00 [card0-crtc6]
root         156  0.0  0.0      0     0 ?        S    17:30   0:00 [card0-crtc7]
root         157  0.1  0.0      0     0 ?        I<   17:30   0:11 [kworker/2:1H-kblockd]
root         160  0.0  0.0      0     0 ?        I    17:30   0:00 [kworker/2:2-cgroup_destroy]
root         161  0.1  0.0      0     0 ?        I<   17:30   0:11 [kworker/0:1H-kblockd]
root         190  0.0  0.0      0     0 ?        S    17:30   0:00 [jbd2/sda1-8]
root         191  0.0  0.0      0     0 ?        I<   17:30   0:00 [ext4-rsv-conver]
root         229  0.0  0.4  48332 17084 ?        Ss   17:30   0:00 /lib/systemd/systemd-journald
root         251  0.0  0.1  21916  5040 ?        Ss   17:30   0:00 /lib/systemd/systemd-udevd
root         294  0.0  0.0      0     0 ?        I<   17:30   0:00 [iprt-VBoxWQueue]
root         310  0.0  0.0      0     0 ?        I<   17:30   0:00 [cryptd]
root         414  0.0  0.0   6684  2648 ?        Ss   17:30   0:00 /usr/sbin/cron -f
message+     415  0.0  0.1   8208  4680 ?        Ss   17:30   0:01 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         422  0.0  0.0 220740  3956 ?        Ssl  17:30   0:00 /usr/sbin/rsyslogd -n -iNONE
root         424  0.0  0.1  21908  7144 ?        Ss   17:30   0:00 /lib/systemd/systemd-logind
root         425  0.0  0.2 390204 10536 ?        Ssl  17:30   0:00 /usr/libexec/udisks2/udisksd
root         438  0.1  0.0      0     0 ?        I    17:30   0:13 [kworker/0:3-events]
root         515  0.0  0.1 234236  7672 ?        Ssl  17:30   0:00 /usr/libexec/polkitd --no-debug
root         615  0.0  0.0   5784  1736 tty1     Ss+  17:30   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         930  0.0  0.0   6876  2856 tty5     Ss   17:33   0:00 /bin/login -p --
joe          936  0.0  0.2  15388  8792 ?        Ss   17:33   0:00 /lib/systemd/systemd --user
joe          937  0.0  0.0 100920  2652 ?        S    17:33   0:00 (sd-pam)
joe          943  0.0  0.1   8240  4848 tty5     S    17:33   0:00 -bash
root        1007  0.0  0.0   6864  3212 tty6     Ss   17:45   0:00 /bin/login -p --
root        1030  0.0  0.0      0     0 ?        I    18:21   0:03 [kworker/u8:0-ext4-rsv-conversion]
joe         1038  0.0  0.1   8112  4664 tty6     S+   18:28   0:00 -bash
root        1047  0.0  0.0      0     0 ?        I    18:33   0:00 [kworker/2:0-cgroup_destroy]
root        1048  0.0  0.0      0     0 ?        I    18:33   0:00 [kworker/3:2-events]
root        1078  0.0  0.0      0     0 ?        I    19:21   0:00 [kworker/1:1-mm_percpu_wq]
root        1080  0.0  0.0      0     0 ?        I    19:26   0:00 [kworker/1:0-mm_percpu_wq]
root        1081  0.0  0.0      0     0 ?        I    19:29   0:00 [kworker/1:3-ata_sff]
root        1084  0.0  0.0      0     0 ?        I    19:30   0:00 [kworker/u8:2-flush-8:0]
root        1087  0.0  0.0      0     0 ?        I    19:30   0:00 [kworker/3:0-events]
root        1089  0.0  0.0      0     0 ?        I    19:36   0:00 [kworker/1:2-mm_percpu_wq]
root        1095  0.0  0.0      0     0 ?        I    19:37   0:00 [kworker/0:0-cgroup_destroy]
joe         1189  0.3  0.1   7896  4352 ?        Ss   19:39   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root        1363  0.0  0.0      0     0 ?        I    19:39   0:00 [kworker/2:1-mm_percpu_wq]
root        1364  0.0  0.0      0     0 ?        I    19:40   0:00 [kworker/u8:1-events_unbound]
root        1373  0.0  0.0      0     0 ?        I    19:40   0:00 [kworker/u8:3]
joe         1379  0.0  0.0   9700  3336 tty5     R+   19:40   0:00 ps -aux
```
Logs during this run:
https://gist.githubusercontent.com/tryphe/cbfe7fd727180c5a3b93cfeb5dd298a4/raw/66b16c07a34d7470d7b69aea79b9d982a5690e01/gistfile1.txt

There is a reoccurring problem with `boost::wrapexcept<boost::bad_weak_ptr>` around the point of failure, but only after some other call in a thread has failed.


## tryphe | 2022-03-04T01:05:19+00:00
I'll build with `make debug` and report back with hopefully readable traces :)

## selsta | 2022-03-04T01:11:03+00:00
I'll try to sync up on a VPS and see if I can reproduce. Just to confirm, you used the master branch?

## tryphe | 2022-03-04T01:28:18+00:00
> I'll try to sync up on a VPS and see if I can reproduce. Just to confirm, you used the master branch?

Thanks. Indeed, head is at `d562deaaa950979b7a31a441a8f02a00013e26d6`

## tryphe | 2022-03-04T02:18:59+00:00
After 10 minutes of running I was able to reproduce the bug in debug mode. 7 blocks sync and then it gets stuck, lots of network chatter but no blocks being added. I gave the hangup signal after 10 minutes to keep the log smaller.

```
$ cat ~/.bitmonero/bitmonero.log | grep "Your node"
2022-03-04 01:58:25.247 [shortened for readability] Sync data returned a new top block candidate: 2512046 -> 2571962 [Your node is 59916 blocks (2.7 months) behind] 
2022-03-04 02:01:49.392 [shortened for readability] Sync data returned a new top block candidate: 2512053 -> 2571966 [Your node is 59913 blocks (2.7 months) behind] 
2022-03-04 02:03:42.697 [shortened for readability] Sync data returned a new top block candidate: 2512053 -> 2571968 [Your node is 59915 blocks (2.7 months) behind] 
2022-03-04 02:08:20.795 [shortened for readability] Sync data returned a new top block candidate: 2512053 -> 2571970 [Your node is 59917 blocks (2.7 months) behind] 
```

Log with --log-level 1: https://gist.githubusercontent.com/tryphe/bc38a41e752fd127d3092901e1178051/raw/c17ca0b278450c5d29d89014604eb9fe87861525/gistfile1.txt

Please let me know if there is anything else I can provide.

## tryphe | 2022-03-04T09:24:55+00:00
It looks like the errors are possibly unrelated to the syncing problem. I tried a handful of old release versions back as far as 0.17.1.3. I still experience the syncing problem but no runtime errors.

## selsta | 2022-03-08T03:47:42+00:00
I started the sync process on a fresh VPS now. Will update you if it syncs fine or if I gets stuck too.

## selsta | 2022-03-08T11:42:11+00:00
8 hours later, so far no issues

```
Synced 2505056/2575077 (97%, 70021 left)
```

## selsta | 2022-03-09T16:28:24+00:00
I unfortunately couldn't reproduce this on a fresh VPS with v0.17.3.0. Sync was without any issues.

## tryphe | 2022-03-09T23:00:39+00:00
I'm not really sure what the differences are between our machines.

While syncing past 95%, it takes me somewhere between 5 to 40 minutes to experience the stuck syncing problem.
While fully synced, it takes somewhere between 0 to 5 hours to experience the stuck syncing problem.

I'm on a residential connection so I have some packet loss. About 0.05% to 0.1%. Maybe that's the problem? I'll try and induce more packet loss to see if it makes the problem worse.

## selsta | 2022-03-09T23:19:14+00:00
Residential connection with minor packet loss should be fine.

The logs you posted did hint at some networking related issues, but it's not exactly clear yet.

## Regloom | 2022-03-17T12:11:56+00:00
I have exactly the same problem on my home pc running latest Arch linux kernel (5.16.14-arch1-1), monerod is launched inside docker container (as per https://sethforprivacy.com/guides/run-a-p2pool-node/). Absolutely the same behavior as described by  @tryphe. Will try to sync natively in arch with monero CLI. Overall network download speed according to "sync_info" seems to drop significantly to 3-60kB/s after 3-30mins of monerod container launch after 97% sync (block 2500000).

## selsta | 2022-03-17T12:14:15+00:00
@Regloom just to confirm, it gets completely stuck? or just slow sync?

## selsta | 2022-03-17T12:15:08+00:00
After block 2478000 there are no more checkpoints so sync will significantly slow down.

## Regloom | 2022-03-17T13:09:57+00:00
> 



> it gets completely stuck? or just slow sync?

It slows down first to very low speed and then it stucks (no new blocks within hours). Restarting monerod helps for a while and then again is slows down and stops syncing. Now trying to sync without docker in Arch itself.

## Regloom | 2022-03-17T17:09:42+00:00
> Now trying to sync without docker in Arch itself.

Same behaviour. Here is a [log 0 of monerod](https://pastebin.com/raw/JsKyTqWM).

## selsta | 2022-03-17T17:11:03+00:00
Can you also post sync_info output?

## Gingeropolous | 2022-03-17T18:42:18+00:00
have you tried adding specific peers? 

you can add a priority one with

`--add-priority-node` 176.9.0.187

or

`--add-exclusive-node` 176.9.0.187

that IP is that of xmrchain.net , so it *should* work. 

## selsta | 2022-03-17T18:43:41+00:00
Yea my idea was too to add a couple exclusive nodes to make sure it's not a malicious peer.

## Regloom | 2022-03-17T19:08:13+00:00
> have you tried adding specific peers?

Thanks for advice! I'll give it a try.

## selsta | 2022-03-17T19:09:39+00:00
Make sure to add both `--add-exclusive-node 88.198.199.23` and `--add-exclusive-node 176.9.0.187`, syncing from just one peer can be spotty. The other IP is mine.

## Regloom | 2022-03-17T19:54:10+00:00
> Can you also post sync_info output?

[Here](https://pastebin.com/raw/Dm5e8adg) you are.

## Regloom | 2022-03-17T20:17:12+00:00
> Make sure to add both `--add-exclusive-node 88.198.199.23` and `--add-exclusive-node 176.9.0.187`, syncing from just one peer can be spotty. The other IP is mine.

Executed monerod with `--add-exclusive-node=88.198.199.23:18081 --add-exclusive-node=176.9.0.187:18081`
Now it shows me that I'm fully synced:
`~/monero $ ./monero-x86_64-linux-gnu-v0.17.3.0/monerod status
2022-03-17 20:11:59.127	I Monero 'Oxygen Orion' (v0.17.3.0-release)
Height: 2507075/2507075 (100.0%) on mainnet, not mining, net hash 2.65 GH/s, v14, 0(out)+0(in) connections, uptime 0d 0h 8m 4s`
is it correct?

## selsta | 2022-03-17T20:19:49+00:00
That doesn't sound right.

Is it a node with restricted RPC?

## Regloom | 2022-03-17T20:28:21+00:00
> That doesn't sound right.
> 
> Is it a node with restricted RPC?

Well, I guess so. Here is my current [config](https://pastebin.com/raw/yA0np8R1). I've tried several other options (commented) but no luck.


## selsta | 2022-03-17T20:30:00+00:00
The first step would be to try to sync without any config at all, just a custom data dir if necessary. Also adding `--prune-blockchain` is fine if you don't have enough space for the full blockchain, but apart from that no config.

## Regloom | 2022-03-18T05:59:09+00:00
OK, here is [sync_info](https://pastebin.com/raw/0buJpRvQ) logs after night running:
**monerod --prune-blockchain --add-priority-node=88.198.199.23 --add-priority-node=176.9.0.187**
It stuck on Height: 2507351/2581844 (97.1%). 

I've also tried `--add-exclusive-node` and it blocked both nodes after 20 mins:

> 2022-03-18 06:04:56.330	I SYNCHRONIZATION started
> 2022-03-18 06:05:09.986	I Host 88.198.199.23 blocked.
> 2022-03-18 06:08:12.024	W monerod is now disconnected from the network
> 2022-03-18 06:08:12.978	I [176.9.0.187:18080 OUT] Sync data returned a new top block candidate: 2507361 -> 2582080 [Your node is 74719 blocks (3.4 months) behind] 
> 2022-03-18 06:08:12.978	I SYNCHRONIZATION started
> 2022-03-18 06:08:24.067	W monerod is now disconnected from the network
> 2022-03-18 06:08:24.747	I [176.9.0.187:18080 OUT] Sync data returned a new top block candidate: 2507371 -> 2582080 [Your node is 74709 blocks (3.4 months) behind] 
> 2022-03-18 06:08:24.747	I SYNCHRONIZATION started
> 2022-03-18 06:08:35.676	I Host 176.9.0.187 blocked.




## selsta | 2022-03-18T10:58:11+00:00
@Regloom can you also upload log level 2 logs? You don't have to add any priority nodes.

## Regloom | 2022-03-18T18:02:11+00:00
> can you also upload log level 2 logs?

Here you are, level 2 logs without priority nodes.
[bitmonero.log.zip](https://github.com/monero-project/monero/files/8306658/bitmonero.log.zip)

p.s. Also tried running from latest Debian Live image and got the same result. At least distro is not the cause. Can it be due to my hardware (e.g. AMD Athlon II X4 6400e CPU with no L3 cache and AES support)? 

## tryphe | 2022-03-18T21:54:26+00:00
Fwiw, I'm also running on an AMD FX 8300 series, but it's a different socket (AM3+ vs AM3 for Athlon II) and different die size (32nm vs 45nm for Athlon II).

## Regloom | 2022-03-19T08:17:10+00:00
> AMD FX 8300 series,

That might be somehow related. What's your motherboard? 

## tryphe | 2022-03-20T07:21:42+00:00
> > AMD FX 8300 series,
> 
> That might be somehow related. What's your motherboard?

I think it's this thing: ASUS TUF SABERTOOTH 990FX

AMD 990FX chipset.

I'll move the problematic VM to a newer Intel hypervisor to attempt to rule out any hardware issue. Will try to report back in a few days.

## Regloom | 2022-03-22T09:01:17+00:00
Just tried to perform full blockchain sync on a new SSD drive with no luck. Stuck on Height: 2501169/2585003 (96.8%) on mainnet. 

## selsta | 2022-03-22T22:35:41+00:00
> I'll move the problematic VM to a newer Intel hypervisor to attempt to rule out any hardware issue. Will try to report back in a few days.

Thanks. While I can't imagine the CPU being an issue, it still helps us isolate the sync bug.

## selsta | 2022-03-25T16:07:10+00:00
One more thing to test: Can you compile https://github.com/tevador/RandomX and then run the `./randomx-tests` binary to see if all tests pass without issues?

## Gingeropolous | 2022-03-25T18:48:53+00:00
for the record i just did a fresh sync on a 5900x on ubuntu 20 w/ 16gb ram. 

## Regloom | 2022-03-26T16:32:19+00:00
> One more thing to test: Can you compile https://github.com/tevador/RandomX and then run the `./randomx-tests` binary to see if all tests pass without issues?

Done, here is a clipped `./random-tests` output:

> 
> > [88] Hash test 2e (compiler)                  ... PASSED
> [89] Cache initialization: SSSE3              ... SKIPPED
> [90] Cache initialization: AVX2               ... SKIPPED
> [91] Hash batch test                          ... PASSED
> [92] Preserve rounding mode                   ... PASSED
> 
> All tests PASSED
> 2 tests were SKIPPED due to incompatible configuration (see above)

I've created a systemctl timer to restart monerod service every 30 mins as a workaround, at least it syncs somehow (slowly)

## moneromooo-monero | 2022-03-26T17:24:36+00:00
How long did that randomx test last ?

Also try running monerod with --prep-blocks-threads 1


## Regloom | 2022-03-26T18:41:21+00:00
> How long did that randomx test last ?
> 
> Also try running monerod with --prep-blocks-threads 1

It took less than a minute. Will do.

## moneromooo-monero | 2022-03-26T19:45:27+00:00
Check for any options for long term tests. It's possible your CPU starts going wonky once hot.


## Regloom | 2022-03-29T14:41:55+00:00
> Check for any options for long term tests. It's possible your CPU starts going wonky once hot.

Checked everything related to CPU (temp, freq) and it's OK. My blockchain synced to 100% in 3 days having "monerod" service restarted every 30 mins. Looks like a workaround for an issue.

## tryphe | 2022-04-12T05:33:02+00:00
Just a quick update

The VM on the AMD machine is synced but still exhibits the strange behavior usually every few hours, but sometimes takes longer, 20-30 hours.
The VM was cloned and has been running fine for 10 days on an i7 machine.
Same network for both machines, so it looks like it's not network related.


Although I didn't pop any blocks to see if it could sync from farther back on the i7 machine. But I'm assuming the cause of the behavior while synced and unsynced are identical because the behavior is the same.

I recently ran prime95 (random FFT) for a while on the AMD machine, so it's definitely stable. It never runs hotter than 30C. I ran the RandomX tests and everything does pass fine. It also runs other VMs and various software with no strange behavior. So I'm not really sure what's going on.

I think I have an old Athlon II X4 around here somewhere :D It's practically the same CPU on a slightly older socket and different chipset.

## tryphe | 2022-04-12T06:14:49+00:00
I updated the OP so it should be a bit more clear what the behavior is now.

## selsta | 2022-04-12T19:26:08+00:00
Can you run RandomX tests in a loop for 60 hours or so and see if it passes 100% of the time? That would be the most similar test to running monerod for a long time.

## Gingeropolous | 2022-04-18T04:33:37+00:00
I just completed a sync on a laptop made in 2007 with a  Intel(R) Core(TM)2 Duo CPU T8100  @ 2.10GHz with 2GB RAM and a 7200 rpm spinny HDD

## agowa | 2022-06-28T01:47:09+00:00
I ran into this issue too. I spent a few hours trying to debug it. Apparently, it crashes when trying to get the length of some string. I haven't found which one exactly it is, as when I try to debug it, but the strlen cal is way too often called for that to be feasible. Also, I tried to compile from the master branch, but that failed with a bunch of C++ errors in multiple libraries (cross-compiling for windows 64-bit from ubuntu). But back to the topic.

The error shows up as an "FILE SYSTEM LIMITATION" in procmon.
![image](https://user-images.githubusercontent.com/2544867/176068136-630a632b-15a3-4fe5-857b-ee7fa7967b7f.png)
![image](https://user-images.githubusercontent.com/2544867/176068177-7c946248-4112-4e99-a025-4062baf87966.png)
![image](https://user-images.githubusercontent.com/2544867/176068317-a2fa3d81-121c-49be-a1c8-345cd2c039f8.png)
![image](https://user-images.githubusercontent.com/2544867/176068395-c288693c-c99f-49ca-8c78-a740ff005b93.png)
![image](https://user-images.githubusercontent.com/2544867/176068937-19f704d3-b333-4410-898e-05cd9ac3a56d.png)
![image](https://user-images.githubusercontent.com/2544867/176069046-bb9b3c6e-d88f-474b-a1f3-3c2cc36c1fc5.png)
![image](https://user-images.githubusercontent.com/2544867/176069443-f9d6253f-3f13-409d-beef-b740c72b70b3.png)


## selsta | 2022-06-28T01:50:22+00:00
@agowa338 when did this issue start showing up? could it be a corrupted database?

## agowa | 2022-06-28T02:03:02+00:00
I dought that it's a corrupt database. After all it started syncing from noting yesterday.

## selsta | 2022-06-28T02:03:56+00:00
And it instantly crashes after startup?

## agowa | 2022-06-28T02:04:50+00:00
Not instantly, but immediately after the "SYNCHRONIZATION started" message. I tried to run it with increased loglevel, but even with 4 I couldn't see anything related to this (or I missed it, it was a lot of log output).

## selsta | 2022-06-28T02:09:06+00:00
I assume starting with `--db-salvage` doesn't help, but it's worth a try.

If it doesn't help I would move / delete the blockchain (data.lmdb) and try to sync from scratch again. The blockchain can corrupt when there is a power loss or when the external harddrive gets disconnected during sync.

You can also add `--db-sync-mode safe` which makes the sync process slower but it helps against corruption. This isn't necessary usually but Windows is a bit more error prone here.

## agowa | 2022-06-28T02:15:21+00:00
> If it doesn't help I would move / delete the blockchain (data.lmdb) and try to sync from scratch again. The blockchain can corrupt when there is a power loss or when the external harddrive gets disconnected during sync.

That wasn't the case. The computer was still running. All that happened was while the initial sync it already crashed at that position. And now every time I restart it crashes there again. And the harddisk is an NVME where also the OS is installed on, so it is probably also not that (no disk errors within the eventlog either). I can delete it and restart the sync, but as it was basically the initial sync, I have my doubts that it'll work the 2nd time...

![image](https://user-images.githubusercontent.com/2544867/176076540-000e6b77-f0a3-4798-a220-732ab2169641.png)
![image](https://user-images.githubusercontent.com/2544867/176076752-ab4746f8-551d-4047-9a09-77b8501aafb0.png)


## selsta | 2022-06-28T02:20:48+00:00
What you posted shows that there is an error when adding something to the database. Now I'm not really sure what "FILE SYSTEM LIMITATION" means exactly, but if it starts showing up a second time we can be sure that it's not a corrupted database.

@hyc any idea about ^ ?

## selsta | 2022-06-28T02:29:51+00:00
To clarify, with what you described (internal NVMe, no power loss) it's unlikely that your database is corrupted but it's the easiest first step to help us locate the issue.

## agowa | 2022-06-28T02:33:04+00:00
"FILE SYSTEM LIMITATION" is the result of the API call to SetEndOfFile https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-setendoffile which sets the physical size of a file (There is still about 156 GB free on that 1TB drive, so it's not an out of space issue either).

> To clarify, with what you described (internal NVMe, no power loss) it's unlikely that your database is corrupted but it's the easiest first step to help us locate the issue.

Ok, going to delete the database now. But it'll take about a day to sync. So that's why I didn't necessarily want to do it now while debugging.

## selsta | 2022-06-28T02:34:00+00:00
And do you know how to get an all threads backtrace on Windows? I'm unfortunately only familiar with gdb / lldb.

## agowa | 2022-06-28T02:37:45+00:00
Only in visual studio. Haven't done it in the x64dbg or windbg yet.

## agowa | 2022-06-28T02:45:55+00:00
Here you go, the horizontal lines separate threads:
![image](https://user-images.githubusercontent.com/2544867/176080697-b0181d23-578e-4ba4-a679-1cf5b42b16f5.png)
![image](https://user-images.githubusercontent.com/2544867/176080741-5a1567f8-58b6-4840-b0c0-0b840238e10d.png)
![image](https://user-images.githubusercontent.com/2544867/176080798-2d658425-0424-494f-8210-d7c3e383d104.png)


## selsta | 2022-06-28T02:53:15+00:00
This isn't readable unfortunately, seems to be either a stripped binary or some Windows specific thing.

## agowa | 2022-06-28T02:54:09+00:00
Those are the exact positions where the instruction pointer was currently pointing to. Sadly it doesn't show the function name. For that I have to click on each individual one and look a few lines up in the asembly...

## agowa | 2022-06-28T03:06:47+00:00
Apparently, that was my fault. I didn't download the symbols within x64dbg. This already looks a bit better (but I don't have a PDB file for monerod (it's not within the downloadable zip), so it cannot resolve these)
![image](https://user-images.githubusercontent.com/2544867/176083359-07335f6d-0031-44b6-bb36-401138dd3255.png)
![image](https://user-images.githubusercontent.com/2544867/176083408-f2451668-30ef-46b2-8382-475cc33fcffe.png)


## hyc | 2022-06-28T03:36:04+00:00
> What you posted shows that there is an error when adding something to the database. Now I'm not really sure what "FILE SYSTEM LIMITATION" means exactly, but if it starts showing up a second time we can be sure that it's not a corrupted database.
> 
> @hyc any idea about ^ ?

No idea how strlen() has anything to do with filesystem limitations. What is the size of the data.mdb file, and what kind of filesystem is in use on that partition?

## agowa | 2022-06-28T03:44:46+00:00
Filesystem NTFS
data.mdb size: 113 GB (122.395.095.040 bytes)

the strlen() is called once I hit "step over", so it's probably the exception handler within monerod I suppose (hard to tell without the PDB file).
![image](https://user-images.githubusercontent.com/2544867/176087435-b83c41bd-74dc-4169-a6ad-934cf0b57619.png)


## agowa | 2022-06-28T04:04:01+00:00
And when looking at the asm code of strlen we can see why it crashes. Somehow it ends up with a null pointer in RAX and tries to read from it. And reading from a null pointer aparently throws an access violation exception...
![image](https://user-images.githubusercontent.com/2544867/176089472-b40e30d0-0799-40d4-8a3f-93b765657acf.png)


## agowa | 2022-07-03T12:19:07+00:00
I deleted the database and let it resync again (this time with `--db-sync-mode safe`) and it worked.
I don't know why it failed at the first initial sync. But the 2nd initial sync worked.

## selsta | 2024-07-31T23:21:49+00:00
Closing as there were no other reports about this in a while and I suspect the issue was hardware related.

# Action History
- Created by: tryphe | 2022-02-27T03:29:12+00:00
- Closed at: 2024-07-31T23:21:49+00:00
