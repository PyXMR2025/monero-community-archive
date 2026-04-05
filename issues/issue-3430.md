---
title: After terminating xmrig (ran as superuser) RAM does not get freed.
source_url: https://github.com/xmrig/xmrig/issues/3430
author: d4f5409d
assignees: []
labels: []
created_at: '2024-02-26T15:08:52+00:00'
updated_at: '2024-04-23T17:26:37+00:00'
type: issue
status: closed
closed_at: '2024-04-23T17:26:37+00:00'
---

# Original Description
**Describe the bug**
After closing the program the RAM does not get cleared and it stays as allocated. Note this only happens if you start the program multiple times in a session.

**To Reproduce**
Open xmrig as superuser.
Close with CTRL+C
Reopen it.
Close again.
Experience the error.

**Expected behavior**
Free the RAM that is not used by anymore by the program.

**Required data**
 - Can't provide sorry
 - Default
 - OS: Linux > Ubuntu > ZorinOS
 - Not GPU related

**Additional context**
Nothing.


# Discussion History
## SChernykh | 2024-02-26T20:49:10+00:00
Any modern operating system, including Linux, frees all memory and resources after an application terminates. If it doesn't, then it's a bug in Linux, or (more likely) you just misinterpret something.

## d4f5409d | 2024-02-27T07:41:54+00:00
Maybe, but I am not sure. I'll leave the issue open to help others find it.

## Fjodor42 | 2024-02-27T09:49:35+00:00
@d4f5409d: Coould you perhaps psot the results of the following?

1. Output from `free` before running
2. Output after stopping
3. Output after running again
4. Output after stopping

In other words, it would be nice to know how you determine that the RAM stays allocated, and I have seen others, in other contexts, be confused by the output of `free` in particular, which is why as ask for that output specifically, but if you determine the problem to exists by other means, please include that as well.

## d4f5409d | 2024-02-27T13:29:19+00:00
Of course, give me a few minutes.

## d4f5409d | 2024-02-27T13:40:54+00:00
Looks like it does not get freed after first closure either.

### Before
```
               total        used        free      shared  buff/cache   available
Mem:         7956344     1514644      913304       49528     5528396     6119716
Swap:              0           0           0
```

### After 1st closure
```
              total        used        free      shared  buff/cache   available
Mem:         7956344     4206132      523476       52252     3226736     3435576
Swap:              0           0           0
```

### After 2nd start and while running the program
```
              total        used        free      shared  buff/cache   available
Mem:         7956344     4208960      517444       52256     3229940     3432756
Swap:              0           0           0
```

### After 2nd closure
```
               total        used        free      shared  buff/cache   available
Mem:         7956344     4249944      468040       52272     3238360     3391772
Swap:              0           0           0
```

*Note that I have disabled swap and it does not correlate with the issue. The issue is independent of it.*

## d4f5409d | 2024-02-27T13:45:50+00:00
After running the system monitor as root, it can not detect any source of heavy RAM use by any process, either. So RAM gets eaten up in the wild, and I don't even know what process causes this issue. After reboot, everything is fine again. Maybe this is a bug in the kernel?

## Fjodor42 | 2024-02-27T16:43:32+00:00
How long after system startup did you run this?

Would it be possible to start the machine, let it run for 10-15 minutes before starting xmrig, then do similar readings?

A reading while the first run is in effect would also be nice.

## d4f5409d | 2024-02-29T14:29:26+00:00
> How long after system startup did you run this?
> 
> Would it be possible to start the machine, let it run for 10-15 minutes before starting xmrig, then do similar readings?
> 
> A reading while the first run is in effect would also be nice.

I am pretty sure it does not affect what time I launch it.

## Fjodor42 | 2024-02-29T15:22:38+00:00
That is under the assumption that it is xmrig that is leaking in a way that should be well-nigh impossible.

I would like to see whether something is started up on the machine that may eat the RAM.

Before, during and after a run, `ps auxk pmem` would probably also be some good output to show at least some of the last lines of.

## d4f5409d | 2024-03-01T20:05:40+00:00
Before:

```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           2  0.0  0.0      0     0 ?        S    20:51   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   20:51   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   20:51   0:00 [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   20:51   0:00 [slub_flushwq
root           6  0.0  0.0      0     0 ?        I<   20:51   0:00 [netns]
root           7  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/0:0-
root           8  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/0:0H
root           9  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/0:1-
root          10  0.7  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:0
root          11  0.0  0.0      0     0 ?        I<   20:51   0:00 [mm_percpu_wq
root          12  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_tasks_kt
root          13  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_tasks_ru
root          14  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_tasks_tr
root          15  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/0]
root          16  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_preempt]
root          17  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/0]
root          18  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          19  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/0]
root          20  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/1]
root          21  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          22  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/1]
root          23  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/1]
root          24  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/1:0-
root          25  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/1:0H
root          26  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/2]
root          27  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          28  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/2]
root          29  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/2]
root          30  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/2:0-
root          31  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/2:0H
root          32  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/3]
root          33  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          34  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/3]
root          35  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/3]
root          36  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:0-
root          37  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/3:0H
root          38  0.0  0.0      0     0 ?        S    20:51   0:00 [kdevtmpfs]
root          39  0.0  0.0      0     0 ?        I<   20:51   0:00 [inet_frag_wq
root          40  0.7  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:1
root          41  0.0  0.0      0     0 ?        S    20:51   0:00 [kauditd]
root          42  0.0  0.0      0     0 ?        S    20:51   0:00 [khungtaskd]
root          43  0.0  0.0      0     0 ?        S    20:51   0:00 [oom_reaper]
root          44  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/u8:2
root          45  0.0  0.0      0     0 ?        I<   20:51   0:00 [writeback]
root          46  0.0  0.0      0     0 ?        S    20:51   0:00 [kcompactd0]
root          47  0.0  0.0      0     0 ?        SN   20:51   0:00 [ksmd]
root          48  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/1:1-
root          49  0.0  0.0      0     0 ?        SN   20:51   0:00 [khugepaged]
root          50  0.0  0.0      0     0 ?        I<   20:51   0:00 [kintegrityd]
root          51  0.0  0.0      0     0 ?        I<   20:51   0:00 [kblockd]
root          52  0.0  0.0      0     0 ?        I<   20:51   0:00 [blkcg_punt_b
root          53  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/2:1-
root          54  0.0  0.0      0     0 ?        I<   20:51   0:00 [tpm_dev_wq]
root          55  0.0  0.0      0     0 ?        I<   20:51   0:00 [ata_sff]
root          56  0.0  0.0      0     0 ?        I<   20:51   0:00 [md]
root          57  0.0  0.0      0     0 ?        I<   20:51   0:00 [md_bitmap]
root          58  0.0  0.0      0     0 ?        I<   20:51   0:00 [edac-poller]
root          59  0.0  0.0      0     0 ?        I<   20:51   0:00 [devfreq_wq]
root          60  0.0  0.0      0     0 ?        S    20:51   0:00 [watchdogd]
root          61  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/2:1H
root          62  0.0  0.0      0     0 ?        S    20:51   0:00 [ksgxd]
root          63  0.1  0.0      0     0 ?        S    20:51   0:00 [kswapd0]
root          64  0.0  0.0      0     0 ?        S    20:51   0:00 [ecryptfs-kth
root          65  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:1-
root          66  0.0  0.0      0     0 ?        I<   20:51   0:00 [kthrotld]
root          67  0.0  0.0      0     0 ?        I<   20:51   0:00 [acpi_thermal
root          68  0.0  0.0      0     0 ?        I<   20:51   0:00 [mld]
root          69  0.0  0.0      0     0 ?        I<   20:51   0:00 [ipv6_addrcon
root          71  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/1:2-
root          77  0.0  0.0      0     0 ?        I<   20:51   0:00 [kstrp]
root          79  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/u9:0
root          83  0.0  0.0      0     0 ?        I<   20:51   0:00 [charger_mana
root         105  0.1  0.0      0     0 ?        I<   20:51   0:00 [kworker/1:1H
root         117  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/0:1H
root         118  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/3:1H
root         120  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/2:2-
root         135  0.0  0.0      0     0 ?        I<   20:51   0:00 [cryptd]
root         136  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_0]
root         137  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_0]
root         138  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_1]
root         139  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_1]
root         140  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_2]
root         141  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_2]
root         142  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_3]
root         143  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_3]
root         144  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_4]
root         145  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_4]
root         146  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_5]
root         147  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_5]
root         148  0.4  0.0      0     0 ?        I    20:51   0:00 [kworker/u8:3
root         149  0.6  0.0      0     0 ?        I    20:51   0:00 [kworker/u8:4
root         150  0.6  0.0      0     0 ?        I    20:51   0:00 [kworker/u8:5
root         151  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/u8:6
root         152  0.6  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:7
root         153  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:2-
root         154  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:3-
root         157  0.0  0.0      0     0 ?        I<   20:51   0:00 [uas]
root         158  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_6]
root         159  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_6]
root         160  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/0:2H
root         164  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/0:2-
root         327  0.0  0.0      0     0 ?        I<   20:52   0:00 [kdmflush/252
root         332  0.0  0.0      0     0 ?        I<   20:52   0:00 [kcryptd_io/2
root         333  0.0  0.0      0     0 ?        I<   20:52   0:00 [kcryptd/252:
root         334  0.0  0.0      0     0 ?        S    20:52   0:00 [dmcrypt_writ
root         339  0.0  0.0      0     0 ?        I<   20:52   0:00 [kdmflush/252
root         340  0.0  0.0      0     0 ?        I<   20:52   0:00 [kdmflush/252
root         374  0.0  0.0      0     0 ?        S    20:52   0:00 [jbd2/dm-1-8]
root         375  0.0  0.0      0     0 ?        I<   20:52   0:00 [ext4-rsv-con
root         464  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/0:3-
root         524  0.0  0.0      0     0 ?        S    20:52   0:00 [irq/127-mei_
root         625  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/1:3-
root         644  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/2:3-
root         645  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/2:4-
root         678  0.0  0.0      0     0 ?        I<   20:52   0:00 [kworker/0:3H
root         691  0.0  0.0      0     0 ?        S    20:52   0:00 [nv_queue]
root         692  0.0  0.0      0     0 ?        S    20:52   0:00 [nv_queue]
root         693  0.0  0.0      0     0 ?        S    20:52   0:00 [nv_open_q]
root         724  0.0  0.0      0     0 ?        S    20:52   0:00 [jbd2/sdc2-8]
root         725  0.0  0.0      0     0 ?        I<   20:52   0:00 [ext4-rsv-con
root         798  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia-modes
root         799  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia-modes
root         806  0.1  0.0      0     0 ?        S    20:52   0:00 [irq/129-nvid
root         807  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia]
root         808  0.1  0.0      0     0 ?        S    20:52   0:00 [nv_queue]
root         961  0.0  0.0      0     0 ?        S    20:52   0:00 [UVM global q
root         962  0.0  0.0      0     0 ?        S    20:52   0:00 [UVM deferred
root         963  0.0  0.0      0     0 ?        S    20:52   0:00 [UVM Tools Ev
root        1430  0.0  0.0      0     0 ?        I<   20:52   0:00 [iprt-VBoxWQu
root        1431  0.0  0.0      0     0 ?        S    20:52   0:00 [iprt-VBoxTsc
root        2462  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia-drm/t
user        3089  0.0  0.0      0     0 ?        Z    20:52   0:00 [zypak-sandbo
root        5281  0.0  0.0      0     0 ?        S    20:53   0:00 [nvidia-drm/t
root        5334  0.0  0.0      0     0 ?        S    20:53   0:00 [nvidia-drm/t
user        3044  0.0  0.0   4108   660 ?        Ss   20:52   0:00 server --sh -
root        1246  0.0  0.0  10084  1032 ?        S    20:52   0:00 /usr/sbin/dns
user        3050  0.0  0.0   2960  1152 ?        S    20:52   0:00 /usr/libexec/
user        5149  0.0  0.0   2956  1152 ?        S    20:53   0:00 /usr/libexec/
user        3195  0.0  0.0   2872  1284 ?        S    20:52   0:00 /usr/libexec/
avahi        885  0.0  0.0   7496  1420 ?        S    20:52   0:00 avahi-daemon:
user        3047  0.0  0.0   2872  1536 ?        S    20:52   0:00 /usr/libexec/
user        5146  0.0  0.0   2872  1536 ?        S    20:53   0:00 /usr/libexec/
user        2602  0.0  0.0   2892  1664 ?        Ss   20:52   0:00 sh -c /usr/bi
user        3092  0.0  0.0   5652  1664 ?        S    20:52   0:00 cat
user        3093  0.0  0.0   5652  1664 ?        S    20:52   0:00 cat
user        3095  0.0  0.0   2872  1664 ?        Ss   20:52   0:00 /usr/libexec/
user        2664  0.0  0.0   2872  1792 ?        S    20:52   0:00 /usr/libexec/
root        2770  0.0  0.0   2796  1920 ?        Ss   20:52   0:00 fusermount3 -
root         823  0.0  0.0   2816  2048 ?        Ss   20:52   0:00 /usr/sbin/acp
root         890  0.0  0.0  12232  2108 ?        Ss   20:52   0:00 /sbin/mount.n
nvidia-+     979  0.0  0.0   5468  2176 ?        Ss   20:52   0:00 /usr/bin/nvid
kernoops    1420  0.0  0.0  13088  2188 ?        Ss   20:52   0:00 /usr/sbin/ker
kernoops    1412  0.0  0.0  13088  2212 ?        Ss   20:52   0:00 /usr/sbin/ker
libvirt+    1245  0.0  0.0  10112  2568 ?        S    20:52   0:00 /usr/sbin/dns
root         864  0.0  0.0  12388  2688 ?        Ss   20:52   0:00 /usr/sbin/cro
user        5119  0.0  0.0  86928  3200 ?        SLs  20:53   0:00 /usr/bin/gpg-
rtkit       1319  0.0  0.0 154004  3328 ?        SNsl 20:52   0:00 /usr/libexec/
user        5991  0.0  0.0  15992  3840 pts/0    R+   20:54   0:00 ps auxk pmem
avahi        825  0.0  0.0   7760  3968 ?        Ss   20:52   0:00 avahi-daemon:
root         835  0.0  0.0  82768  3968 ?        Ssl  20:52   0:00 /usr/sbin/irq
user        2400  0.0  0.0   8616  4608 ?        S    20:52   0:00 /usr/bin/dbus
root        1099  0.0  0.0   6772  4696 ?        Ss   20:52   0:00 /usr/sbin/apa
www-data    1102  0.0  0.0 1932688 4700 ?        Sl   20:52   0:00 /usr/sbin/apa
www-data    1103  0.0  0.0 1932688 4700 ?        Sl   20:52   0:00 /usr/sbin/apa
root        2022  0.0  0.0  41232  4876 ?        Ss   20:52   0:00 /usr/lib/post
user        5546  0.0  0.0  14172  5248 pts/0    Ss   20:53   0:00 bash
user        2408  0.0  0.0  94800  5376 ?        Ssl  20:52   0:00 /usr/libexec/
user        2291  0.0  0.0 165504  6016 tty2     Ssl+ 20:52   0:00 /usr/libexec/
user        5147  0.0  0.0 165536  6016 ?        Sl   20:53   0:00 /usr/libexec/
user        2269  0.0  0.0 170592  6072 ?        S    20:52   0:00 (sd-pam)
user        2556  0.0  0.0 157104  6144 ?        Ssl  20:52   0:00 /usr/libexec/
user        3048  0.0  0.0 165668  6144 ?        Sl   20:52   0:00 /usr/libexec/
syslog       839  0.0  0.0 222456  6272 ?        Ssl  20:52   0:00 /usr/sbin/rsy
user        2276  0.0  0.0  42460  6272 ?        S<sl 20:52   0:00 /usr/bin/pipe
user        2285  0.4  0.0  10160  6272 ?        Ss   20:52   0:00 /usr/bin/dbus
user        2478  0.0  0.0 239300  6400 ?        Ssl  20:52   0:00 /usr/libexec/
user        2277  0.0  0.0  26352  6528 ?        Ssl  20:52   0:00 /usr/bin/pipe
user        2621  0.0  0.0 239416  6528 ?        Ssl  20:52   0:00 /usr/libexec/
root         875  0.0  0.0 239408  6656 ?        Ssl  20:52   0:00 /usr/libexec/
root         881  0.0  0.0  16504  6656 ?        Ss   20:52   0:00 /sbin/wpa_sup
user        2426  0.0  0.0 380892  6656 ?        Sl   20:52   0:00 /usr/libexec/
user        2513  0.0  0.0 239528  6656 ?        Ssl  20:52   0:00 /usr/libexec/
systemd+     793  0.0  0.0  14836  6784 ?        Ss   20:52   0:00 /lib/systemd/
user        2521  0.0  0.0 239732  6784 ?        Ssl  20:52   0:00 /usr/libexec/
root         467  0.1  0.0  27064  7040 ?        Ss   20:52   0:00 /lib/systemd/
root         877  0.0  0.0  14952  7040 ?        Ss   20:52   0:00 /lib/systemd/
user        2620  0.0  0.0 460984  7040 ?        Ssl  20:52   0:00 /usr/libexec/
user        3040  0.0  0.0 239860  7040 ?        Ssl  20:52   0:00 /usr/libexec/
user        2517  0.0  0.0 240616  7168 ?        Ssl  20:52   0:00 /usr/libexec/
user        2603  0.0  0.0 313728  7168 ?        Ssl  20:52   0:00 /usr/libexec/
postfix     4918  0.0  0.0  41620  7168 ?        S    20:52   0:00 pickup -l -t 
postfix     4920  0.0  0.0  41664  7168 ?        S    20:52   0:00 qmgr -l -t un
message+     828  0.5  0.0  11352  7296 ?        Ss   20:52   0:00 @dbus-daemon 
user        2765  0.0  0.0 466304  7424 ?        Ssl  20:52   0:00 /usr/libexec/
user        2855  0.0  0.0 167076  7552 ?        Ssl  20:52   0:00 /usr/libexec/
systemd+     804  0.0  0.0  89720  7680 ?        Ssl  20:52   0:00 /lib/systemd/
user        2708  0.0  0.0 240380  7680 ?        Sl   20:52   0:00 /usr/libexec/
user        2813  0.0  0.0 166628  7680 ?        Sl   20:52   0:00 /usr/libexec/
user        2677  0.0  0.0 240508  7808 ?        Sl   20:52   0:00 /usr/libexec/
user        2867  0.0  0.0  46960  7808 ?        Ss   20:52   0:00 /usr/lib/blue
root         838  0.0  0.0 243212  7884 ?        Ssl  20:52   0:00 /usr/libexec/
user        2675  0.0  0.0 232268  7936 ?        Sl   20:52   0:00 /usr/libexec/
root         850  0.0  0.1 243160  7992 ?        Ssl  20:52   0:00 /usr/libexec/
root         876  0.0  0.1  48256  8032 ?        Ss   20:52   0:00 /lib/systemd/
user        2418  0.0  0.1 243744  8064 ?        Ssl  20:52   0:00 /usr/libexec/
user        2508  0.0  0.1 318308  8192 ?        Ssl  20:52   0:00 /usr/libexec/
user        2609  0.0  0.1 315232  8192 ?        Ssl  20:52   0:00 /usr/libexec/
user        3677  0.0  0.1 317472  8192 ?        Sl   20:52   0:00 /usr/libexec/
user        2583  0.0  0.1 162812  8320 ?        Sl   20:52   0:00 /usr/libexec/
user        2394  0.0  0.1 309712  8448 ?        Ssl  20:52   0:00 /usr/libexec/
user        2624  0.0  0.1 315608  8704 ?        Ssl  20:52   0:00 /usr/libexec/
root        2044  0.0  0.1 245380  8960 ?        Ssl  20:52   0:00 /usr/libexec/
root        1059  0.0  0.1 244408  9088 ?        Ssl  20:52   0:00 /usr/sbin/gdm
user        2960  0.0  0.1 317924  9216 ?        Sl   20:52   0:00 /usr/libexec/
nm-open+    4800  0.1  0.1  13596  9344 ?        S    20:52   0:00 /usr/sbin/ope
root        4750  0.0  0.1 173412  9984 ?        Sl   20:52   0:00 /usr/lib/Netw
user        2625  0.0  0.1 322648 10112 ?        Ssl  20:52   0:00 /usr/libexec/
user        2282  0.1  0.1 246052 10200 ?        SLl  20:52   0:00 /usr/bin/gnom
root         878  0.0  0.1 131484 10240 ?        Ssl  20:52   0:00 /usr/sbin/the
user        2268  0.3  0.1  18060 10368 ?        Ss   20:52   0:00 /lib/systemd/
root        2261  0.0  0.1 173812 11008 ?        Sl   20:52   0:00 gdm-session-w
user        2502  0.0  0.1 393064 11264 ?        Ssl  20:52   0:00 /usr/libexec/
user        2622  0.0  0.1 469244 11264 ?        Ssl  20:52   0:00 /usr/libexec/
user        2619  0.0  0.1 253072 11648 ?        Ssl  20:52   0:00 /usr/libexec/
root           1  0.7  0.1 166956 11988 ?        Ss   20:51   0:01 /sbin/init sp
user        2608  0.1  0.1 318252 12016 ?        Sl   20:52   0:00 /usr/bin/ibus
root        1388  0.0  0.1 172676 12032 ?        Ssl  20:52   0:00 /usr/sbin/cup
root        1032  0.0  0.1 317964 12512 ?        Ssl  20:52   0:00 /usr/sbin/Mod
root         837  0.8  0.1 247152 12700 ?        Ssl  20:52   0:01 /usr/libexec/
systemd+     803  0.0  0.1  25464 13568 ?        Ss   20:52   0:00 /lib/systemd/
colord      1058  0.0  0.1 248604 13684 ?        Ssl  20:52   0:00 /usr/libexec/
root         997  0.0  0.1  76016 13696 ?        Ss   20:52   0:00 /usr/sbin/cup
user        2665  0.0  0.1 192600 14592 ?        Sl   20:52   0:00 touchegg
user        2761  0.0  0.1 627024 14592 ?        Ssl  20:52   0:00 /usr/libexec/
root         879  0.0  0.1 332528 15232 ?        Ssl  20:52   0:00 /usr/bin/touc
user        2694  0.0  0.1 345484 15232 ?        Sl   20:52   0:00 /usr/libexec/
user        2306  0.0  0.1 226112 15872 tty2     Sl+  20:52   0:00 /usr/libexec/
user        2532  0.0  0.1 415296 15872 ?        Sl   20:52   0:00 /usr/libexec/
user        2607  0.0  0.2 378772 16640 ?        Ssl  20:52   0:00 /usr/libexec/
root         880  0.1  0.2 393836 16956 ?        Ssl  20:52   0:00 /usr/libexec/
user        3066  0.0  0.2 296952 17280 ?        Ssl  20:52   0:00 /usr/libexec/
user        2428  0.0  0.2 662708 18816 ?        Ssl  20:52   0:00 /usr/libexec/
root         829  0.2  0.2 264960 19232 ?        Ssl  20:52   0:00 /usr/sbin/Net
root         836  0.0  0.2  43920 21228 ?        Ss   20:52   0:00 /usr/bin/pyth
root        1001  0.0  0.2 120944 23680 ?        Ssl  20:52   0:00 /usr/bin/pyth
user        2705  0.0  0.2 195836 23776 ?        Sl   20:52   0:00 /usr/libexec/
user        2631  0.0  0.3 343564 23876 ?        Ssl  20:52   0:00 /usr/libexec/
user        2614  0.0  0.3 343284 23956 ?        Ssl  20:52   0:00 /usr/libexec/
user        2618  0.0  0.3 453196 26940 ?        Ssl  20:52   0:00 /usr/libexec/
user        2581  0.0  0.3 2517412 27072 ?       Sl   20:52   0:00 /usr/bin/gjs 
user        2278  0.0  0.3 1755436 27208 ?       S<sl 20:52   0:00 /usr/bin/puls
user        2797  0.0  0.3 2591132 27428 ?       Sl   20:52   0:00 /usr/bin/gjs 
user        2605  0.1  0.3 612828 28084 ?        Ssl  20:52   0:00 /usr/libexec/
user        2617  0.0  0.3 719536 28728 ?        Ssl  20:52   0:00 /usr/libexec/
user        2679  0.8  0.3 274716 28916 ?        Sl   20:52   0:00 /usr/libexec/
user        2866  0.0  0.3 348108 29104 ?        Ssl  20:52   0:00 /usr/libexec/
user        2632  0.0  0.3 349568 30796 ?        Ssl  20:52   0:00 /usr/libexec/
root        2893  0.3  0.4 397132 32800 ?        Ssl  20:52   0:00 /usr/libexec/
root         429  0.2  0.4  57280 33664 ?        S<s  20:52   0:00 /lib/systemd/
user        5705  0.1  0.4 497756 33704 ?        Sl   20:53   0:00 update-notifi
user        5285  0.0  0.4 200360 36736 ?        Sl   20:53   0:00 /home/user/.v
user        2525  0.0  0.4 571828 37504 ?        Sl   20:52   0:00 /usr/libexec/
root        2059  4.2  0.5 376352 41940 ?        Ssl  20:52   0:05 /usr/libexec/
user        2812  1.5  0.5 788544 43988 ?        SNsl 20:52   0:01 /usr/libexec/
root         998  0.2  0.5 1655560 46808 ?       Ssl  20:52   0:00 /usr/sbin/lib
user        2695  0.2  0.6 375248 50504 ?        Sl   20:52   0:00 /usr/bin/pyth
user        3087  0.0  0.6 33797260 50560 ?      S    20:52   0:00 /app/Signal/s
user        3204  0.0  0.6 33799900 52352 ?      S    20:52   0:00 /app/Signal/s
user        2495  0.1  0.6 531136 54528 ?        Ssl  20:52   0:00 /usr/libexec/
user        2480  0.0  0.6 741512 54656 ?        Sl   20:52   0:00 /usr/libexec/
user        2542  0.1  0.7 973268 56064 ?        Ssl  20:52   0:00 /usr/libexec/
user        2564  0.1  0.7 898988 58752 ?        Ssl  20:52   0:00 /usr/libexec/
user        4515  0.1  0.7 33933840 58872 ?      Sl   20:52   0:00 /app/Signal/s
user        5522  0.8  0.7 898168 61152 ?        Ssl  20:53   0:00 /usr/libexec/
user        4525  0.0  0.8 33846888 65536 ?      Sl   20:52   0:00 /app/Signal/s
user        5012  0.2  0.8 906776 66864 ?        Sl   20:53   0:00 /usr/bin/gnom
user        2773  0.2  0.8 627112 67484 ?        Ssl  20:52   0:00 /usr/libexec/
user        5388  0.0  0.8 2358172 68352 ?       Sl   20:53   0:00 /home/user/.v
user        5477  0.0  0.8 2358172 68352 ?       Sl   20:53   0:00 /home/user/.v
user        5393  0.0  0.8 2358172 68608 ?       Sl   20:53   0:00 /home/user/.v
user        2293  1.6  0.9 25402296 76140 tty2   Sl+  20:52   0:01 /usr/lib/xorg
user        2900  0.6  0.9 3289936 76584 ?       Sl   20:52   0:00 gjs /usr/shar
user        5301  1.5  0.9 382016 78940 ?        Sl   20:53   0:01 /home/user/.v
user        2721  0.2  1.0 764484 79924 ?        Sl   20:52   0:00 /usr/libexec/
user        5305  0.3  1.1 2373240 95208 ?       Sl   20:53   0:00 /home/user/.v
user        5386  0.2  1.2 2374200 99404 ?       Sl   20:53   0:00 /home/user/.v
user        5344 10.8  1.8 19504176 148528 ?     Sl   20:53   0:07 /home/user/.v
user        2663 11.0  2.3 1144832 186828 ?      Sl   20:52   0:11 /usr/bin/gnom
user        3057  2.7  2.9 1182405136 233236 ?   SLl  20:52   0:02 /app/Signal/s
user        2731  6.5  3.3 1324300 265088 ?      Sl   20:52   0:07 /usr/bin/pyth
user        4628  3.4  4.2 1186410004 335896 ?   Sl   20:52   0:03 /app/Signal/s
user        5193  6.8  4.5 2975312 360360 ?      Sl   20:53   0:04 ./firefox.rea
user        2452  6.2  4.5 4424784 365148 ?      SLsl 20:52   0:06 /usr/bin/gnom
```

During:
```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           2  0.0  0.0      0     0 ?        S    20:51   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   20:51   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   20:51   0:00 [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   20:51   0:00 [slub_flushwq
root           6  0.0  0.0      0     0 ?        I<   20:51   0:00 [netns]
root           7  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/0:0-
root           8  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/0:0H
root           9  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/0:1-
root          10  0.4  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:0
root          11  0.0  0.0      0     0 ?        I<   20:51   0:00 [mm_percpu_wq
root          12  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_tasks_kt
root          13  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_tasks_ru
root          14  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_tasks_tr
root          15  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/0]
root          16  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_preempt]
root          17  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/0]
root          18  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          19  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/0]
root          20  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/1]
root          21  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          22  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/1]
root          23  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/1]
root          24  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/1:0-
root          25  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/1:0H
root          26  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/2]
root          27  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          28  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/2]
root          29  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/2]
root          30  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/2:0-
root          31  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/2:0H
root          32  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/3]
root          33  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          34  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/3]
root          35  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/3]
root          36  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:0-
root          37  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/3:0H
root          38  0.0  0.0      0     0 ?        S    20:51   0:00 [kdevtmpfs]
root          39  0.0  0.0      0     0 ?        I<   20:51   0:00 [inet_frag_wq
root          40  0.4  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:1
root          41  0.0  0.0      0     0 ?        S    20:51   0:00 [kauditd]
root          42  0.0  0.0      0     0 ?        S    20:51   0:00 [khungtaskd]
root          43  0.0  0.0      0     0 ?        S    20:51   0:00 [oom_reaper]
root          44  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/u8:2
root          45  0.0  0.0      0     0 ?        I<   20:51   0:00 [writeback]
root          46  0.0  0.0      0     0 ?        S    20:51   0:00 [kcompactd0]
root          47  0.0  0.0      0     0 ?        SN   20:51   0:00 [ksmd]
root          48  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/1:1-
root          49  0.0  0.0      0     0 ?        SN   20:51   0:00 [khugepaged]
root          50  0.0  0.0      0     0 ?        I<   20:51   0:00 [kintegrityd]
root          51  0.0  0.0      0     0 ?        I<   20:51   0:00 [kblockd]
root          52  0.0  0.0      0     0 ?        I<   20:51   0:00 [blkcg_punt_b
root          53  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/2:1-
root          54  0.0  0.0      0     0 ?        I<   20:51   0:00 [tpm_dev_wq]
root          55  0.0  0.0      0     0 ?        I<   20:51   0:00 [ata_sff]
root          56  0.0  0.0      0     0 ?        I<   20:51   0:00 [md]
root          57  0.0  0.0      0     0 ?        I<   20:51   0:00 [md_bitmap]
root          58  0.0  0.0      0     0 ?        I<   20:51   0:00 [edac-poller]
root          59  0.0  0.0      0     0 ?        I<   20:51   0:00 [devfreq_wq]
root          60  0.0  0.0      0     0 ?        S    20:51   0:00 [watchdogd]
root          61  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/2:1H
root          62  0.0  0.0      0     0 ?        S    20:51   0:00 [ksgxd]
root          63  0.2  0.0      0     0 ?        S    20:51   0:00 [kswapd0]
root          64  0.0  0.0      0     0 ?        S    20:51   0:00 [ecryptfs-kth
root          65  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:1-
root          66  0.0  0.0      0     0 ?        I<   20:51   0:00 [kthrotld]
root          67  0.0  0.0      0     0 ?        I<   20:51   0:00 [acpi_thermal
root          68  0.0  0.0      0     0 ?        I<   20:51   0:00 [mld]
root          69  0.0  0.0      0     0 ?        I<   20:51   0:00 [ipv6_addrcon
root          71  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/1:2-
root          77  0.0  0.0      0     0 ?        I<   20:51   0:00 [kstrp]
root          79  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/u9:0
root          83  0.0  0.0      0     0 ?        I<   20:51   0:00 [charger_mana
root         105  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/1:1H
root         117  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/0:1H
root         118  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/3:1H
root         120  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/2:2-
root         135  0.0  0.0      0     0 ?        I<   20:51   0:00 [cryptd]
root         136  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_0]
root         137  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_0]
root         138  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_1]
root         139  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_1]
root         140  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_2]
root         141  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_2]
root         142  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_3]
root         143  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_3]
root         144  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_4]
root         145  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_4]
root         146  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_5]
root         147  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_5]
root         148  0.2  0.0      0     0 ?        I    20:51   0:00 [kworker/u8:3
root         149  0.3  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:4
root         150  0.3  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:5
root         151  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/u8:6
root         152  0.3  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:7
root         153  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:2-
root         154  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:3-
root         157  0.0  0.0      0     0 ?        I<   20:51   0:00 [uas]
root         158  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_6]
root         159  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_6]
root         160  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/0:2H
root         164  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/0:2-
root         327  0.0  0.0      0     0 ?        I<   20:52   0:00 [kdmflush/252
root         332  0.0  0.0      0     0 ?        I<   20:52   0:00 [kcryptd_io/2
root         333  0.0  0.0      0     0 ?        I<   20:52   0:00 [kcryptd/252:
root         334  0.0  0.0      0     0 ?        S    20:52   0:00 [dmcrypt_writ
root         339  0.0  0.0      0     0 ?        I<   20:52   0:00 [kdmflush/252
root         340  0.0  0.0      0     0 ?        I<   20:52   0:00 [kdmflush/252
root         374  0.0  0.0      0     0 ?        S    20:52   0:00 [jbd2/dm-1-8]
root         375  0.0  0.0      0     0 ?        I<   20:52   0:00 [ext4-rsv-con
root         464  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/0:3-
root         524  0.0  0.0      0     0 ?        S    20:52   0:00 [irq/127-mei_
root         625  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/1:3-
root         644  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/2:3-
root         645  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/2:4-
root         678  0.0  0.0      0     0 ?        I<   20:52   0:00 [kworker/0:3H
root         691  0.0  0.0      0     0 ?        S    20:52   0:00 [nv_queue]
root         692  0.0  0.0      0     0 ?        S    20:52   0:00 [nv_queue]
root         693  0.0  0.0      0     0 ?        S    20:52   0:00 [nv_open_q]
root         724  0.0  0.0      0     0 ?        S    20:52   0:00 [jbd2/sdc2-8]
root         725  0.0  0.0      0     0 ?        I<   20:52   0:00 [ext4-rsv-con
root         798  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia-modes
root         799  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia-modes
root         806  0.1  0.0      0     0 ?        S    20:52   0:00 [irq/129-nvid
root         807  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia]
root         808  0.0  0.0      0     0 ?        S    20:52   0:00 [nv_queue]
root         961  0.0  0.0      0     0 ?        S    20:52   0:00 [UVM global q
root         962  0.0  0.0      0     0 ?        S    20:52   0:00 [UVM deferred
root         963  0.0  0.0      0     0 ?        S    20:52   0:00 [UVM Tools Ev
root        1430  0.0  0.0      0     0 ?        I<   20:52   0:00 [iprt-VBoxWQu
root        1431  0.0  0.0      0     0 ?        S    20:52   0:00 [iprt-VBoxTsc
root        2462  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia-drm/t
user        3089  0.0  0.0      0     0 ?        Z    20:52   0:00 [zypak-sandbo
root        5281  0.0  0.0      0     0 ?        S    20:53   0:00 [nvidia-drm/t
root        5334  0.0  0.0      0     0 ?        S    20:53   0:00 [nvidia-drm/t
user        3044  0.0  0.0   4108   660 ?        Ss   20:52   0:00 server --sh -
root        1246  0.0  0.0  10084  1032 ?        S    20:52   0:00 /usr/sbin/dns
user        3050  0.0  0.0   2960  1152 ?        S    20:52   0:00 /usr/libexec/
user        5149  0.0  0.0   2956  1152 ?        S    20:53   0:00 /usr/libexec/
user        3195  0.0  0.0   2872  1284 ?        S    20:52   0:00 /usr/libexec/
avahi        885  0.0  0.0   7496  1420 ?        S    20:52   0:00 avahi-daemon:
user        3047  0.0  0.0   2872  1536 ?        S    20:52   0:00 /usr/libexec/
user        5146  0.0  0.0   2872  1536 ?        S    20:53   0:00 /usr/libexec/
user        2602  0.0  0.0   2892  1664 ?        Ss   20:52   0:00 sh -c /usr/bi
user        3092  0.0  0.0   5652  1664 ?        S    20:52   0:00 cat
user        3093  0.0  0.0   5652  1664 ?        S    20:52   0:00 cat
user        3095  0.0  0.0   2872  1664 ?        Ss   20:52   0:00 /usr/libexec/
user        2664  0.0  0.0   2872  1792 ?        S    20:52   0:00 /usr/libexec/
root        2770  0.0  0.0   2796  1920 ?        Ss   20:52   0:00 fusermount3 -
root         823  0.0  0.0   2816  2048 ?        Ss   20:52   0:00 /usr/sbin/acp
root         890  0.0  0.0  12232  2108 ?        Ss   20:52   0:00 /sbin/mount.n
nvidia-+     979  0.0  0.0   5468  2176 ?        Ss   20:52   0:00 /usr/bin/nvid
kernoops    1420  0.0  0.0  13088  2188 ?        Ss   20:52   0:00 /usr/sbin/ker
kernoops    1412  0.0  0.0  13088  2212 ?        Ss   20:52   0:00 /usr/sbin/ker
root        6113  0.0  0.0  17508  2468 pts/1    Ss   20:55   0:00 sudo xmrig
libvirt+    1245  0.0  0.0  10112  2568 ?        S    20:52   0:00 /usr/sbin/dns
root         864  0.0  0.0  12388  2688 ?        Ss   20:52   0:00 /usr/sbin/cro
user        5119  0.0  0.0  86928  3072 ?        SLs  20:53   0:00 /usr/bin/gpg-
rtkit       1319  0.0  0.0 154004  3200 ?        SNsl 20:52   0:00 /usr/libexec/
user        6151  0.0  0.0  15992  3840 pts/2    R+   20:56   0:00 ps auxk pmem
avahi        825  0.0  0.0   7760  3968 ?        Ss   20:52   0:00 avahi-daemon:
root         835  0.0  0.0  82768  3968 ?        Ssl  20:52   0:00 /usr/sbin/irq
user        2400  0.0  0.0   8616  4608 ?        S    20:52   0:00 /usr/bin/dbus
root        1099  0.0  0.0   6772  4696 ?        Ss   20:52   0:00 /usr/sbin/apa
www-data    1102  0.0  0.0 1932688 4700 ?        Sl   20:52   0:00 /usr/sbin/apa
www-data    1103  0.0  0.0 1932688 4700 ?        Sl   20:52   0:00 /usr/sbin/apa
root        2022  0.0  0.0  41232  4876 ?        Ss   20:52   0:00 /usr/lib/post
user        5546  0.0  0.0  14172  5120 pts/0    Ss   20:53   0:00 bash
user        2408  0.0  0.0  94800  5376 ?        Ssl  20:52   0:00 /usr/libexec/
user        6142  0.0  0.0  14172  5376 pts/2    Ss   20:56   0:00 bash
user        2276  0.0  0.0  42460  5888 ?        S<sl 20:52   0:00 /usr/bin/pipe
user        2291  0.0  0.0 165504  6016 tty2     Ssl+ 20:52   0:00 /usr/libexec/
user        5147  0.0  0.0 165536  6016 ?        Sl   20:53   0:00 /usr/libexec/
user        2269  0.0  0.0 170592  6072 ?        S    20:52   0:00 (sd-pam)
syslog       839  0.0  0.0 222456  6144 ?        Ssl  20:52   0:00 /usr/sbin/rsy
user        2277  0.0  0.0  26352  6144 ?        Ssl  20:52   0:00 /usr/bin/pipe
user        3048  0.0  0.0 165668  6144 ?        Sl   20:52   0:00 /usr/libexec/
root        6112  0.0  0.0  17508  6144 pts/0    S+   20:55   0:00 sudo xmrig
systemd+     793  0.0  0.0  14836  6272 ?        Ss   20:52   0:00 /lib/systemd/
user        2285  0.2  0.0  10160  6272 ?        Ss   20:52   0:00 /usr/bin/dbus
root         881  0.0  0.0  16504  6400 ?        Ss   20:52   0:00 /sbin/wpa_sup
user        2478  0.0  0.0 239300  6400 ?        Ssl  20:52   0:00 /usr/libexec/
root         877  0.0  0.0  14952  6528 ?        Ss   20:52   0:00 /lib/systemd/
user        2621  0.0  0.0 239416  6528 ?        Ssl  20:52   0:00 /usr/libexec/
root         467  0.1  0.0  27064  6656 ?        Ss   20:52   0:00 /lib/systemd/
root         875  0.0  0.0 239408  6656 ?        Ssl  20:52   0:00 /usr/libexec/
user        2426  0.0  0.0 380892  6656 ?        Sl   20:52   0:00 /usr/libexec/
user        2513  0.0  0.0 239528  6656 ?        Ssl  20:52   0:00 /usr/libexec/
user        2556  0.0  0.0 157628  6656 ?        Ssl  20:52   0:00 /usr/libexec/
user        2521  0.0  0.0 239732  6784 ?        Ssl  20:52   0:00 /usr/libexec/
user        2620  0.0  0.0 460984  7040 ?        Ssl  20:52   0:00 /usr/libexec/
user        3040  0.0  0.0 239860  7040 ?        Ssl  20:52   0:00 /usr/libexec/
systemd+     804  0.0  0.0  89720  7168 ?        Ssl  20:52   0:00 /lib/systemd/
user        2517  0.0  0.0 240616  7168 ?        Ssl  20:52   0:00 /usr/libexec/
user        2603  0.0  0.0 313728  7168 ?        Ssl  20:52   0:00 /usr/libexec/
postfix     4918  0.0  0.0  41620  7168 ?        S    20:52   0:00 pickup -l -t 
postfix     4920  0.0  0.0  41664  7168 ?        S    20:52   0:00 qmgr -l -t un
message+     828  0.2  0.0  11352  7296 ?        Ss   20:52   0:00 @dbus-daemon 
user        2867  0.0  0.0  46960  7296 ?        Ss   20:52   0:00 /usr/lib/blue
user        2765  0.0  0.0 466304  7552 ?        Ssl  20:52   0:00 /usr/libexec/
root         876  0.0  0.0  48256  7648 ?        Ss   20:52   0:00 /lib/systemd/
user        2708  0.0  0.0 240380  7680 ?        Sl   20:52   0:00 /usr/libexec/
user        2855  0.0  0.0 167244  7680 ?        Ssl  20:52   0:00 /usr/libexec/
root         838  0.0  0.0 243212  7756 ?        Ssl  20:52   0:00 /usr/libexec/
user        2677  0.0  0.0 240508  7808 ?        Sl   20:52   0:00 /usr/libexec/
user        2813  0.0  0.0 166628  7808 ?        Sl   20:52   0:00 /usr/libexec/
user        2508  0.0  0.0 318308  7936 ?        Ssl  20:52   0:00 /usr/libexec/
user        2675  0.0  0.0 232268  7936 ?        Sl   20:52   0:00 /usr/libexec/
root         850  0.0  0.1 243160  7992 ?        Ssl  20:52   0:00 /usr/libexec/
user        2418  0.0  0.1 243744  8064 ?        Ssl  20:52   0:00 /usr/libexec/
user        3677  0.0  0.1 317472  8192 ?        Sl   20:52   0:00 /usr/libexec/
nm-open+    4800  0.0  0.1  13596  8192 ?        S    20:52   0:00 /usr/sbin/ope
user        2583  0.0  0.1 162812  8320 ?        Sl   20:52   0:00 /usr/libexec/
user        2394  0.0  0.1 309712  8448 ?        Ssl  20:52   0:00 /usr/libexec/
root        2044  0.0  0.1 245380  8704 ?        Ssl  20:52   0:00 /usr/libexec/
user        2624  0.0  0.1 315608  8704 ?        Ssl  20:52   0:00 /usr/libexec/
root        1059  0.0  0.1 244408  8960 ?        Ssl  20:52   0:00 /usr/sbin/gdm
user        2609  0.0  0.1 316240  9088 ?        Ssl  20:52   0:00 /usr/libexec/
user        2960  0.0  0.1 317924  9088 ?        Sl   20:52   0:00 /usr/libexec/
user        2268  0.1  0.1  18060  9600 ?        Ss   20:52   0:00 /lib/systemd/
root        4750  0.0  0.1 173412  9728 ?        Sl   20:52   0:00 /usr/lib/Netw
user        2282  0.0  0.1 246052 10072 ?        SLl  20:52   0:00 /usr/bin/gnom
user        2625  0.0  0.1 322648 10112 ?        Ssl  20:52   0:00 /usr/libexec/
root         878  0.0  0.1 131484 10240 ?        Ssl  20:52   0:00 /usr/sbin/the
root        2261  0.0  0.1 173812 10880 ?        Sl   20:52   0:00 gdm-session-w
user        2622  0.0  0.1 469244 11008 ?        Ssl  20:52   0:00 /usr/libexec/
user        2502  0.0  0.1 393056 11264 ?        Ssl  20:52   0:00 /usr/libexec/
root           1  0.4  0.1 166956 11348 ?        Ss   20:51   0:01 /sbin/init sp
user        2619  0.0  0.1 253072 11520 ?        Ssl  20:52   0:00 /usr/libexec/
root        1388  0.0  0.1 172676 11776 ?        Ssl  20:52   0:00 /usr/sbin/cup
user        5995  0.0  0.1 431436 11776 ?        Sl   20:54   0:00 /usr/libexec/
user        2608  0.1  0.1 318252 12016 ?        Sl   20:52   0:00 /usr/bin/ibus
root        1032  0.0  0.1 317964 12512 ?        Ssl  20:52   0:00 /usr/sbin/Mod
root         837  0.4  0.1 247152 12572 ?        Ssl  20:52   0:01 /usr/libexec/
systemd+     803  0.0  0.1  25464 12928 ?        Ss   20:52   0:00 /lib/systemd/
root         997  0.0  0.1  76016 13568 ?        Ss   20:52   0:00 /usr/sbin/cup
colord      1058  0.0  0.1 248604 13684 ?        Ssl  20:52   0:00 /usr/libexec/
user        2761  0.0  0.1 627024 14080 ?        Ssl  20:52   0:00 /usr/libexec/
user        2665  0.0  0.1 192600 14464 ?        Sl   20:52   0:00 touchegg
root        6114  286  0.1 3070384 14592 pts/1   Sl+  20:55   2:00 xmrig
user        2694  0.0  0.1 345484 15104 ?        Sl   20:52   0:00 /usr/libexec/
root         879  0.0  0.1 332528 15232 ?        Ssl  20:52   0:00 /usr/bin/touc
root         880  0.0  0.1 393836 15292 ?        Ssl  20:52   0:00 /usr/libexec/
user        2532  0.0  0.1 415296 15744 ?        Sl   20:52   0:00 /usr/libexec/
user        2306  0.0  0.1 226112 15872 tty2     Sl+  20:52   0:00 /usr/libexec/
user        3066  0.0  0.2 296952 16256 ?        Ssl  20:52   0:00 /usr/libexec/
user        2607  0.0  0.2 378772 16640 ?        Ssl  20:52   0:00 /usr/libexec/
user        2428  0.0  0.2 662708 18688 ?        Ssl  20:52   0:00 /usr/libexec/
root         829  0.1  0.2 264960 18720 ?        Ssl  20:52   0:00 /usr/sbin/Net
root         836  0.0  0.2  43920 20972 ?        Ss   20:52   0:00 /usr/bin/pyth
user        2705  0.0  0.2 195836 23648 ?        Sl   20:52   0:00 /usr/libexec/
root        1001  0.0  0.2 120944 23680 ?        Ssl  20:52   0:00 /usr/bin/pyth
user        2631  0.0  0.3 343564 23876 ?        Ssl  20:52   0:00 /usr/libexec/
user        2614  0.0  0.3 343284 23956 ?        Ssl  20:52   0:00 /usr/libexec/
user        2618  0.0  0.3 453196 26940 ?        Ssl  20:52   0:00 /usr/libexec/
user        2581  0.0  0.3 2517412 27072 ?       Sl   20:52   0:00 /usr/bin/gjs 
user        2797  0.0  0.3 2591132 27428 ?       Sl   20:52   0:00 /usr/bin/gjs 
user        2278  0.0  0.3 2017224 27464 ?       S<sl 20:52   0:00 /usr/bin/puls
user        2605  0.0  0.3 612828 28084 ?        Ssl  20:52   0:00 /usr/libexec/
user        2617  0.0  0.3 719536 28728 ?        Ssl  20:52   0:00 /usr/libexec/
user        2866  0.0  0.3 348108 28848 ?        Ssl  20:52   0:00 /usr/libexec/
user        2679  0.4  0.3 274716 28916 ?        Sl   20:52   0:00 /usr/libexec/
root         429  0.1  0.3  57280 29824 ?        S<s  20:52   0:00 /lib/systemd/
root         998  0.1  0.3 1655560 30808 ?       Ssl  20:52   0:00 /usr/sbin/lib
user        2632  0.0  0.3 349568 30924 ?        Ssl  20:52   0:00 /usr/libexec/
root        2893  0.1  0.4 397132 32160 ?        Ssl  20:52   0:00 /usr/libexec/
user        2812  0.9  0.4 788544 33508 ?        SNsl 20:52   0:01 /usr/libexec/
user        5705  0.0  0.4 497756 33704 ?        Sl   20:53   0:00 update-notifi
user        5285  0.0  0.4 200360 33792 ?        Sl   20:53   0:00 /home/user/.v
user        2525  0.0  0.4 571828 37120 ?        Sl   20:52   0:00 /usr/libexec/
root        2059  2.3  0.5 376352 40404 ?        Ssl  20:52   0:05 /usr/libexec/
user        2695  0.1  0.6 375248 50120 ?        Sl   20:52   0:00 /usr/bin/pyth
user        3087  0.0  0.6 33797260 50432 ?      S    20:52   0:00 /app/Signal/s
user        3204  0.0  0.6 33799900 52224 ?      S    20:52   0:00 /app/Signal/s
user        2495  0.0  0.6 531136 52480 ?        Ssl  20:52   0:00 /usr/libexec/
user        2480  0.0  0.6 741512 52992 ?        Sl   20:52   0:00 /usr/libexec/
user        2542  0.0  0.6 973268 53504 ?        Ssl  20:52   0:00 /usr/libexec/
user        2564  0.0  0.7 898988 56960 ?        Ssl  20:52   0:00 /usr/libexec/
user        4515  0.0  0.7 33933840 60152 ?      Sl   20:52   0:00 /app/Signal/s
user        5522  0.8  0.7 899980 62148 ?        Ssl  20:53   0:01 /usr/libexec/
user        5477  0.0  0.7 2358172 62720 ?       Sl   20:53   0:00 /home/user/.v
user        5388  0.0  0.7 2358172 62848 ?       Sl   20:53   0:00 /home/user/.v
user        5393  0.0  0.7 2358172 63104 ?       Sl   20:53   0:00 /home/user/.v
user        5301  0.6  0.7 382016 63196 ?        Sl   20:53   0:01 /home/user/.v
user        5012  0.1  0.8 906776 65072 ?        Sl   20:53   0:00 /usr/bin/gnom
user        4525  0.0  0.8 33846888 65408 ?      Sl   20:52   0:00 /app/Signal/s
user        2773  0.1  0.8 627248 67484 ?        Ssl  20:52   0:00 /usr/libexec/
user        2721  0.1  0.9 764484 78132 ?        Sl   20:52   0:00 /usr/libexec/
user        2293  1.6  0.9 25404452 78136 tty2   Sl+  20:52   0:03 /usr/lib/xorg
user        5305  0.1  1.0 2373240 87092 ?       Sl   20:53   0:00 /home/user/.v
user        2900  0.7  1.1 3635552 87624 ?       Sl   20:52   0:01 gjs /usr/shar
user        5386  0.0  1.1 2374200 92196 ?       Sl   20:53   0:00 /home/user/.v
user        5344  4.6  2.0 19495984 159168 ?     Sl   20:53   0:08 /home/user/.v
user        2663  5.6  2.2 1145196 175180 ?      Sl   20:52   0:11 /usr/bin/gnom
user        3057  1.3  2.9 1182405136 233876 ?   SLl  20:52   0:02 /app/Signal/s
user        2731  3.3  3.3 1324300 262656 ?      Sl   20:52   0:07 /usr/bin/pyth
user        5193  2.8  3.8 2973264 307528 ?      Sl   20:53   0:05 ./firefox.rea
user        4628  1.7  4.2 1186401808 336084 ?   Sl   20:52   0:03 /app/Signal/s
user        2452  4.2  4.5 4440488 359920 ?      SLsl 20:52   0:09 /usr/bin/gnom

```

After:
```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           2  0.0  0.0      0     0 ?        S    20:51   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   20:51   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   20:51   0:00 [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   20:51   0:00 [slub_flushwq
root           6  0.0  0.0      0     0 ?        I<   20:51   0:00 [netns]
root           7  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/0:0-
root           8  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/0:0H
root           9  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/0:1-
root          10  0.4  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:0
root          11  0.0  0.0      0     0 ?        I<   20:51   0:00 [mm_percpu_wq
root          12  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_tasks_kt
root          13  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_tasks_ru
root          14  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_tasks_tr
root          15  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/0]
root          16  0.0  0.0      0     0 ?        I    20:51   0:00 [rcu_preempt]
root          17  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/0]
root          18  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          19  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/0]
root          20  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/1]
root          21  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          22  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/1]
root          23  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/1]
root          24  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/1:0-
root          25  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/1:0H
root          26  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/2]
root          27  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          28  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/2]
root          29  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/2]
root          30  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/2:0-
root          31  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/2:0H
root          32  0.0  0.0      0     0 ?        S    20:51   0:00 [cpuhp/3]
root          33  0.0  0.0      0     0 ?        S    20:51   0:00 [idle_inject/
root          34  0.0  0.0      0     0 ?        S    20:51   0:00 [migration/3]
root          35  0.0  0.0      0     0 ?        S    20:51   0:00 [ksoftirqd/3]
root          36  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:0-
root          37  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/3:0H
root          38  0.0  0.0      0     0 ?        S    20:51   0:00 [kdevtmpfs]
root          39  0.0  0.0      0     0 ?        I<   20:51   0:00 [inet_frag_wq
root          40  0.4  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:1
root          41  0.0  0.0      0     0 ?        S    20:51   0:00 [kauditd]
root          42  0.0  0.0      0     0 ?        S    20:51   0:00 [khungtaskd]
root          43  0.0  0.0      0     0 ?        S    20:51   0:00 [oom_reaper]
root          44  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/u8:2
root          45  0.0  0.0      0     0 ?        I<   20:51   0:00 [writeback]
root          46  0.0  0.0      0     0 ?        S    20:51   0:00 [kcompactd0]
root          47  0.0  0.0      0     0 ?        SN   20:51   0:00 [ksmd]
root          48  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/1:1-
root          49  0.0  0.0      0     0 ?        SN   20:51   0:00 [khugepaged]
root          50  0.0  0.0      0     0 ?        I<   20:51   0:00 [kintegrityd]
root          51  0.0  0.0      0     0 ?        I<   20:51   0:00 [kblockd]
root          52  0.0  0.0      0     0 ?        I<   20:51   0:00 [blkcg_punt_b
root          53  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/2:1-
root          54  0.0  0.0      0     0 ?        I<   20:51   0:00 [tpm_dev_wq]
root          55  0.0  0.0      0     0 ?        I<   20:51   0:00 [ata_sff]
root          56  0.0  0.0      0     0 ?        I<   20:51   0:00 [md]
root          57  0.0  0.0      0     0 ?        I<   20:51   0:00 [md_bitmap]
root          58  0.0  0.0      0     0 ?        I<   20:51   0:00 [edac-poller]
root          59  0.0  0.0      0     0 ?        I<   20:51   0:00 [devfreq_wq]
root          60  0.0  0.0      0     0 ?        S    20:51   0:00 [watchdogd]
root          61  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/2:1H
root          62  0.0  0.0      0     0 ?        S    20:51   0:00 [ksgxd]
root          63  0.1  0.0      0     0 ?        S    20:51   0:00 [kswapd0]
root          64  0.0  0.0      0     0 ?        S    20:51   0:00 [ecryptfs-kth
root          65  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:1-
root          66  0.0  0.0      0     0 ?        I<   20:51   0:00 [kthrotld]
root          67  0.0  0.0      0     0 ?        I<   20:51   0:00 [acpi_thermal
root          68  0.0  0.0      0     0 ?        I<   20:51   0:00 [mld]
root          69  0.0  0.0      0     0 ?        I<   20:51   0:00 [ipv6_addrcon
root          71  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/1:2-
root          77  0.0  0.0      0     0 ?        I<   20:51   0:00 [kstrp]
root          79  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/u9:0
root          83  0.0  0.0      0     0 ?        I<   20:51   0:00 [charger_mana
root         105  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/1:1H
root         117  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/0:1H
root         118  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/3:1H
root         120  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/2:2-
root         135  0.0  0.0      0     0 ?        I<   20:51   0:00 [cryptd]
root         136  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_0]
root         137  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_0]
root         138  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_1]
root         139  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_1]
root         140  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_2]
root         141  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_2]
root         142  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_3]
root         143  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_3]
root         144  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_4]
root         145  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_4]
root         146  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_5]
root         147  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_5]
root         148  0.2  0.0      0     0 ?        I    20:51   0:00 [kworker/u8:3
root         149  0.3  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:4
root         150  0.3  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:5
root         151  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/u8:6
root         152  0.3  0.0      0     0 ?        I    20:51   0:01 [kworker/u8:7
root         153  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:2-
root         154  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/3:3-
root         157  0.0  0.0      0     0 ?        I<   20:51   0:00 [uas]
root         158  0.0  0.0      0     0 ?        S    20:51   0:00 [scsi_eh_6]
root         159  0.0  0.0      0     0 ?        I<   20:51   0:00 [scsi_tmf_6]
root         160  0.0  0.0      0     0 ?        I<   20:51   0:00 [kworker/0:2H
root         164  0.0  0.0      0     0 ?        I    20:51   0:00 [kworker/0:2-
root         327  0.0  0.0      0     0 ?        I<   20:52   0:00 [kdmflush/252
root         332  0.0  0.0      0     0 ?        I<   20:52   0:00 [kcryptd_io/2
root         333  0.0  0.0      0     0 ?        I<   20:52   0:00 [kcryptd/252:
root         334  0.0  0.0      0     0 ?        S    20:52   0:00 [dmcrypt_writ
root         339  0.0  0.0      0     0 ?        I<   20:52   0:00 [kdmflush/252
root         340  0.0  0.0      0     0 ?        I<   20:52   0:00 [kdmflush/252
root         374  0.0  0.0      0     0 ?        S    20:52   0:00 [jbd2/dm-1-8]
root         375  0.0  0.0      0     0 ?        I<   20:52   0:00 [ext4-rsv-con
root         464  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/0:3-
root         524  0.0  0.0      0     0 ?        S    20:52   0:00 [irq/127-mei_
root         625  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/1:3-
root         644  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/2:3-
root         645  0.0  0.0      0     0 ?        I    20:52   0:00 [kworker/2:4-
root         678  0.0  0.0      0     0 ?        I<   20:52   0:00 [kworker/0:3H
root         691  0.0  0.0      0     0 ?        S    20:52   0:00 [nv_queue]
root         692  0.0  0.0      0     0 ?        S    20:52   0:00 [nv_queue]
root         693  0.0  0.0      0     0 ?        S    20:52   0:00 [nv_open_q]
root         724  0.0  0.0      0     0 ?        S    20:52   0:00 [jbd2/sdc2-8]
root         725  0.0  0.0      0     0 ?        I<   20:52   0:00 [ext4-rsv-con
root         798  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia-modes
root         799  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia-modes
root         806  0.1  0.0      0     0 ?        S    20:52   0:00 [irq/129-nvid
root         807  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia]
root         808  0.0  0.0      0     0 ?        S    20:52   0:00 [nv_queue]
root         961  0.0  0.0      0     0 ?        S    20:52   0:00 [UVM global q
root         962  0.0  0.0      0     0 ?        S    20:52   0:00 [UVM deferred
root         963  0.0  0.0      0     0 ?        S    20:52   0:00 [UVM Tools Ev
root        1430  0.0  0.0      0     0 ?        I<   20:52   0:00 [iprt-VBoxWQu
root        1431  0.0  0.0      0     0 ?        S    20:52   0:00 [iprt-VBoxTsc
root        2462  0.0  0.0      0     0 ?        S    20:52   0:00 [nvidia-drm/t
user        3089  0.0  0.0      0     0 ?        Z    20:52   0:00 [zypak-sandbo
root        5281  0.0  0.0      0     0 ?        S    20:53   0:00 [nvidia-drm/t
root        5334  0.0  0.0      0     0 ?        S    20:53   0:00 [nvidia-drm/t
user        3044  0.0  0.0   4108   660 ?        Ss   20:52   0:00 server --sh -
root        1246  0.0  0.0  10084  1032 ?        S    20:52   0:00 /usr/sbin/dns
user        3050  0.0  0.0   2960  1152 ?        S    20:52   0:00 /usr/libexec/
user        5149  0.0  0.0   2956  1152 ?        S    20:53   0:00 /usr/libexec/
user        3195  0.0  0.0   2872  1284 ?        S    20:52   0:00 /usr/libexec/
avahi        885  0.0  0.0   7496  1420 ?        S    20:52   0:00 avahi-daemon:
user        3047  0.0  0.0   2872  1536 ?        S    20:52   0:00 /usr/libexec/
user        5146  0.0  0.0   2872  1536 ?        S    20:53   0:00 /usr/libexec/
user        2602  0.0  0.0   2892  1664 ?        Ss   20:52   0:00 sh -c /usr/bi
user        3092  0.0  0.0   5652  1664 ?        S    20:52   0:00 cat
user        3093  0.0  0.0   5652  1664 ?        S    20:52   0:00 cat
user        3095  0.0  0.0   2872  1664 ?        Ss   20:52   0:00 /usr/libexec/
user        2664  0.0  0.0   2872  1792 ?        S    20:52   0:00 /usr/libexec/
root        2770  0.0  0.0   2796  1920 ?        Ss   20:52   0:00 fusermount3 -
root         823  0.0  0.0   2816  2048 ?        Ss   20:52   0:00 /usr/sbin/acp
root         890  0.0  0.0  12232  2108 ?        Ss   20:52   0:00 /sbin/mount.n
nvidia-+     979  0.0  0.0   5468  2176 ?        Ss   20:52   0:00 /usr/bin/nvid
kernoops    1420  0.0  0.0  13088  2188 ?        Ss   20:52   0:00 /usr/sbin/ker
kernoops    1412  0.0  0.0  13088  2212 ?        Ss   20:52   0:00 /usr/sbin/ker
libvirt+    1245  0.0  0.0  10112  2568 ?        S    20:52   0:00 /usr/sbin/dns
root         864  0.0  0.0  12388  2688 ?        Ss   20:52   0:00 /usr/sbin/cro
user        5119  0.0  0.0  86928  3072 ?        SLs  20:53   0:00 /usr/bin/gpg-
rtkit       1319  0.0  0.0 154004  3200 ?        SNsl 20:52   0:00 /usr/libexec/
user        6204  0.0  0.0  15992  3840 pts/2    R+   20:57   0:00 ps auxk pmem
avahi        825  0.0  0.0   7760  3968 ?        Ss   20:52   0:00 avahi-daemon:
root         835  0.0  0.0  82768  3968 ?        Ssl  20:52   0:00 /usr/sbin/irq
user        2400  0.0  0.0   8616  4608 ?        S    20:52   0:00 /usr/bin/dbus
root        1099  0.0  0.0   6772  4696 ?        Ss   20:52   0:00 /usr/sbin/apa
www-data    1102  0.0  0.0 1932688 4700 ?        Sl   20:52   0:00 /usr/sbin/apa
www-data    1103  0.0  0.0 1932688 4700 ?        Sl   20:52   0:00 /usr/sbin/apa
root        2022  0.0  0.0  41232  4876 ?        Ss   20:52   0:00 /usr/lib/post
user        5546  0.0  0.0  14172  5120 pts/0    Ss+  20:53   0:00 bash
user        2408  0.0  0.0  94800  5376 ?        Ssl  20:52   0:00 /usr/libexec/
user        6142  0.0  0.0  14172  5376 pts/2    Ss   20:56   0:00 bash
user        2276  0.0  0.0  42460  5888 ?        S<sl 20:52   0:00 /usr/bin/pipe
user        2291  0.0  0.0 165504  6016 tty2     Ssl+ 20:52   0:00 /usr/libexec/
user        5147  0.0  0.0 165536  6016 ?        Sl   20:53   0:00 /usr/libexec/
user        2269  0.0  0.0 170592  6072 ?        S    20:52   0:00 (sd-pam)
syslog       839  0.0  0.0 222456  6144 ?        Ssl  20:52   0:00 /usr/sbin/rsy
user        2277  0.0  0.0  26352  6144 ?        Ssl  20:52   0:00 /usr/bin/pipe
user        3048  0.0  0.0 165668  6144 ?        Sl   20:52   0:00 /usr/libexec/
systemd+     793  0.0  0.0  14836  6272 ?        Ss   20:52   0:00 /lib/systemd/
user        2285  0.2  0.0  10160  6272 ?        Ss   20:52   0:00 /usr/bin/dbus
root         881  0.0  0.0  16504  6400 ?        Ss   20:52   0:00 /sbin/wpa_sup
user        2478  0.0  0.0 239300  6400 ?        Ssl  20:52   0:00 /usr/libexec/
root         877  0.0  0.0  14952  6528 ?        Ss   20:52   0:00 /lib/systemd/
user        2621  0.0  0.0 239416  6528 ?        Ssl  20:52   0:00 /usr/libexec/
root         467  0.0  0.0  27064  6656 ?        Ss   20:52   0:00 /lib/systemd/
root         875  0.0  0.0 239408  6656 ?        Ssl  20:52   0:00 /usr/libexec/
user        2426  0.0  0.0 380892  6656 ?        Sl   20:52   0:00 /usr/libexec/
user        2513  0.0  0.0 239528  6656 ?        Ssl  20:52   0:00 /usr/libexec/
user        2556  0.0  0.0 157628  6656 ?        Ssl  20:52   0:00 /usr/libexec/
user        2521  0.0  0.0 239732  6784 ?        Ssl  20:52   0:00 /usr/libexec/
user        2620  0.0  0.0 460984  7040 ?        Ssl  20:52   0:00 /usr/libexec/
user        3040  0.0  0.0 239860  7040 ?        Ssl  20:52   0:00 /usr/libexec/
systemd+     804  0.0  0.0  89720  7168 ?        Ssl  20:52   0:00 /lib/systemd/
user        2517  0.0  0.0 240616  7168 ?        Ssl  20:52   0:00 /usr/libexec/
user        2603  0.0  0.0 313728  7168 ?        Ssl  20:52   0:00 /usr/libexec/
postfix     4918  0.0  0.0  41620  7168 ?        S    20:52   0:00 pickup -l -t 
postfix     4920  0.0  0.0  41664  7168 ?        S    20:52   0:00 qmgr -l -t un
message+     828  0.2  0.0  11352  7296 ?        Ss   20:52   0:00 @dbus-daemon 
user        2867  0.0  0.0  46960  7296 ?        Ss   20:52   0:00 /usr/lib/blue
user        2765  0.0  0.0 466304  7552 ?        Ssl  20:52   0:00 /usr/libexec/
root         876  0.0  0.0  48256  7648 ?        Ss   20:52   0:00 /lib/systemd/
user        2708  0.0  0.0 240380  7680 ?        Sl   20:52   0:00 /usr/libexec/
user        2855  0.0  0.0 167244  7680 ?        Ssl  20:52   0:00 /usr/libexec/
root         838  0.0  0.0 243212  7756 ?        Ssl  20:52   0:00 /usr/libexec/
user        2677  0.0  0.0 240508  7808 ?        Sl   20:52   0:00 /usr/libexec/
user        2813  0.0  0.0 166628  7808 ?        Sl   20:52   0:00 /usr/libexec/
user        2508  0.0  0.0 318308  7936 ?        Ssl  20:52   0:00 /usr/libexec/
user        2675  0.0  0.0 232268  7936 ?        Sl   20:52   0:00 /usr/libexec/
root         850  0.0  0.1 243160  7992 ?        Ssl  20:52   0:00 /usr/libexec/
user        2418  0.0  0.1 243744  8064 ?        Ssl  20:52   0:00 /usr/libexec/
user        3677  0.0  0.1 317472  8192 ?        Sl   20:52   0:00 /usr/libexec/
nm-open+    4800  0.0  0.1  13596  8192 ?        S    20:52   0:00 /usr/sbin/ope
user        2583  0.0  0.1 162812  8320 ?        Sl   20:52   0:00 /usr/libexec/
user        2394  0.0  0.1 309712  8448 ?        Ssl  20:52   0:00 /usr/libexec/
root        2044  0.0  0.1 245380  8704 ?        Ssl  20:52   0:00 /usr/libexec/
user        2624  0.0  0.1 315608  8704 ?        Ssl  20:52   0:00 /usr/libexec/
root        1059  0.0  0.1 244408  8960 ?        Ssl  20:52   0:00 /usr/sbin/gdm
user        2609  0.0  0.1 316240  9088 ?        Ssl  20:52   0:00 /usr/libexec/
user        2960  0.0  0.1 317924  9088 ?        Sl   20:52   0:00 /usr/libexec/
user        2268  0.1  0.1  18060  9600 ?        Ss   20:52   0:00 /lib/systemd/
root        4750  0.0  0.1 173412  9728 ?        Sl   20:52   0:00 /usr/lib/Netw
user        2282  0.0  0.1 246052 10072 ?        SLl  20:52   0:00 /usr/bin/gnom
user        2625  0.0  0.1 322648 10112 ?        Ssl  20:52   0:00 /usr/libexec/
root         878  0.0  0.1 131484 10240 ?        Ssl  20:52   0:00 /usr/sbin/the
root        2261  0.0  0.1 173812 10880 ?        Sl   20:52   0:00 gdm-session-w
user        2622  0.0  0.1 469244 11008 ?        Ssl  20:52   0:00 /usr/libexec/
user        2502  0.0  0.1 393056 11264 ?        Ssl  20:52   0:00 /usr/libexec/
root           1  0.3  0.1 166956 11348 ?        Ss   20:51   0:01 /sbin/init sp
user        2619  0.0  0.1 253072 11520 ?        Ssl  20:52   0:00 /usr/libexec/
root        1388  0.0  0.1 172676 11776 ?        Ssl  20:52   0:00 /usr/sbin/cup
user        2608  0.1  0.1 318252 12016 ?        Sl   20:52   0:00 /usr/bin/ibus
root        1032  0.0  0.1 317964 12512 ?        Ssl  20:52   0:00 /usr/sbin/Mod
root         837  0.4  0.1 247152 12572 ?        Ssl  20:52   0:01 /usr/libexec/
systemd+     803  0.0  0.1  25464 12928 ?        Ss   20:52   0:00 /lib/systemd/
root         997  0.0  0.1  76016 13568 ?        Ss   20:52   0:00 /usr/sbin/cup
colord      1058  0.0  0.1 248604 13684 ?        Ssl  20:52   0:00 /usr/libexec/
user        2761  0.0  0.1 627024 14080 ?        Ssl  20:52   0:00 /usr/libexec/
user        2665  0.0  0.1 192600 14464 ?        Sl   20:52   0:00 touchegg
user        2694  0.0  0.1 345484 15104 ?        Sl   20:52   0:00 /usr/libexec/
root         879  0.1  0.1 332528 15232 ?        Ssl  20:52   0:00 /usr/bin/touc
root         880  0.0  0.1 393836 15292 ?        Ssl  20:52   0:00 /usr/libexec/
user        2532  0.0  0.1 415296 15744 ?        Sl   20:52   0:00 /usr/libexec/
user        2306  0.0  0.1 226112 15872 tty2     Sl+  20:52   0:00 /usr/libexec/
user        3066  0.0  0.2 296952 16256 ?        Ssl  20:52   0:00 /usr/libexec/
user        2607  0.0  0.2 378772 16640 ?        Ssl  20:52   0:00 /usr/libexec/
user        2428  0.0  0.2 662708 18688 ?        Ssl  20:52   0:00 /usr/libexec/
root         829  0.1  0.2 264960 18720 ?        Ssl  20:52   0:00 /usr/sbin/Net
root         836  0.0  0.2  43920 20972 ?        Ss   20:52   0:00 /usr/bin/pyth
user        2705  0.0  0.2 195836 23648 ?        Sl   20:52   0:00 /usr/libexec/
root        1001  0.0  0.2 120944 23680 ?        Ssl  20:52   0:00 /usr/bin/pyth
user        2631  0.0  0.3 343564 23876 ?        Ssl  20:52   0:00 /usr/libexec/
user        2614  0.0  0.3 343284 23956 ?        Ssl  20:52   0:00 /usr/libexec/
user        2618  0.0  0.3 453196 26940 ?        Ssl  20:52   0:00 /usr/libexec/
user        2581  0.0  0.3 2517412 27072 ?       Sl   20:52   0:00 /usr/bin/gjs 
user        2797  0.0  0.3 2591132 27428 ?       Sl   20:52   0:00 /usr/bin/gjs 
user        2278  0.0  0.3 2017224 27464 ?       S<sl 20:52   0:00 /usr/bin/puls
user        2605  0.0  0.3 612828 28084 ?        Ssl  20:52   0:00 /usr/libexec/
user        2617  0.0  0.3 719536 28728 ?        Ssl  20:52   0:00 /usr/libexec/
user        2866  0.0  0.3 348108 28848 ?        Ssl  20:52   0:00 /usr/libexec/
user        2679  0.3  0.3 274716 28916 ?        Sl   20:52   0:00 /usr/libexec/
root         429  0.1  0.3  57280 29952 ?        S<s  20:52   0:00 /lib/systemd/
root         998  0.1  0.3 1655560 30808 ?       Ssl  20:52   0:00 /usr/sbin/lib
user        2632  0.0  0.3 349568 30924 ?        Ssl  20:52   0:00 /usr/libexec/
root        2893  0.1  0.4 397132 32160 ?        Ssl  20:52   0:00 /usr/libexec/
user        5705  0.0  0.4 497756 33704 ?        Sl   20:53   0:00 update-notifi
user        5285  0.0  0.4 200360 33792 ?        Sl   20:53   0:00 /home/user/.v
user        2525  0.0  0.4 571828 37120 ?        Sl   20:52   0:00 /usr/libexec/
root        2059  1.9  0.5 376352 40404 ?        Ssl  20:52   0:05 /usr/libexec/
user        2812  0.7  0.5 788544 40932 ?        SNsl 20:52   0:02 /usr/libexec/
user        2695  0.0  0.6 375248 50120 ?        Sl   20:52   0:00 /usr/bin/pyth
user        3087  0.0  0.6 33797260 50432 ?      S    20:52   0:00 /app/Signal/s
user        3204  0.0  0.6 33799900 52224 ?      S    20:52   0:00 /app/Signal/s
user        2495  0.0  0.6 531136 52480 ?        Ssl  20:52   0:00 /usr/libexec/
user        2480  0.0  0.6 741512 52992 ?        Sl   20:52   0:00 /usr/libexec/
user        2542  0.0  0.6 973268 53504 ?        Ssl  20:52   0:00 /usr/libexec/
user        2564  0.0  0.7 898988 56960 ?        Ssl  20:52   0:00 /usr/libexec/
user        4515  0.0  0.7 33934096 60152 ?      Sl   20:52   0:00 /app/Signal/s
user        5477  0.0  0.7 2358172 62720 ?       Sl   20:53   0:00 /home/user/.v
user        5388  0.0  0.7 2358172 62848 ?       Sl   20:53   0:00 /home/user/.v
user        5522  1.1  0.7 900460 63044 ?        Ssl  20:53   0:02 /usr/libexec/
user        5393  0.0  0.7 2358172 63104 ?       Sl   20:53   0:00 /home/user/.v
user        5301  0.4  0.7 382016 63196 ?        Sl   20:53   0:01 /home/user/.v
user        5012  0.0  0.8 906776 65072 ?        Sl   20:53   0:00 /usr/bin/gnom
user        4525  0.0  0.8 33846888 65408 ?      Sl   20:52   0:00 /app/Signal/s
user        2773  0.1  0.8 627248 67484 ?        Ssl  20:52   0:00 /usr/libexec/
user        2721  0.0  0.9 764484 78132 ?        Sl   20:52   0:00 /usr/libexec/
user        2293  1.7  0.9 25404452 78136 tty2   Sl+  20:52   0:04 /usr/lib/xorg
user        5305  0.1  1.0 2373240 87092 ?       Sl   20:53   0:00 /home/user/.v
user        2900  0.7  1.1 3635552 87716 ?       Sl   20:52   0:01 gjs /usr/shar
user        5386  0.0  1.1 2374200 92196 ?       Sl   20:53   0:00 /home/user/.v
user        5344  3.6  1.9 19495984 153484 ?     Sl   20:53   0:08 /home/user/.v
user        2663  4.6  2.2 1145196 175180 ?      Sl   20:52   0:11 /usr/bin/gnom
user        3057  1.1  2.9 1182405136 233876 ?   SLl  20:52   0:02 /app/Signal/s
user        2731  2.7  3.3 1324300 262784 ?      Sl   20:52   0:07 /usr/bin/pyth
user        5193  2.3  3.8 2973264 306576 ?      Sl   20:53   0:05 ./firefox.rea
user        4628  1.4  4.2 1186402064 336892 ?   Sl   20:52   0:03 /app/Signal/s
user        2452  4.0  4.5 4440488 360260 ?      SLsl 20:52   0:10 /usr/bin/gnom

```

## koitsu | 2024-03-02T02:52:24+00:00
Let's look at RSS/RES (i.e. `pmem`) and add up all the results shown, for before, during, and after.  We can do this with `awk` easily. 

In the below example, we add up all the RSS/RES columns, as well as keep track of process count (in case there is a huge jump in RSS/RES we can possibly correlate it to new processes, though requires investigation on a per-process basis to determine).  Output is space-delimited RSS/RES total, and process count.  We exclude the USER header row.
```
$ cat before | awk '!/^USER/ { r+=$6; i++ } END { print r " " i }'
4802272 293
$ cat during | awk '!/^USER/ { r+=$6; i++ } END { print r " " i }'
4688776 298
$ cat after | awk '!/^USER/ { r+=$6; i++ } END { print r " " i }'
4656976 294
```
RSS/RES actually **decreased**: 4802272-4656976=145296 KBytes (~145MBytes)

What isn't taken into account here is VIRT/VSZ, which is very hard to calculate usage of because it's virtual process size and includes memory marked as shareable across processes (see: dynamically linked libraries).  Unlike with RSS/RES, you can't just add up all the VIRT columns and get a number that will indicate bloat.  Extracting from multiple processes truly "how much VIRT is used" is extremely complicated.  However, we can get an idea if the process counts fluctuating also correlate with VIRT adjustments, which may let us know what process *could* be doing something.  Let's try it.

```
$ cat before | awk '!/^USER/ { v+=$5; i++ } END { print v " " i }'
2617906348 293
$ cat during | awk '!/^USER/ { v+=$5; i++ } END { print v " " i }'
2622068188 298
$ cat after | awk '!/^USER/ { v+=$5; i++ } END { print v " " i }'
2618532344 294
```
VIRT stays roughly the same (a decrease is shown): 2618532344-2617906348=625996 KBytes

What you are trying to find is roughly a 4249944-1514644=2735300 KBytes (~2.7GBytes) difference.  Those numbers come from your earlier `free` output, looking at `used` column.

Your memory bloat is therefore in kernel space, **not** user space.  Whether or not it's a kernel bug is undetermined at this point, but I would suggest trying stock Ubuntu 22.04 or 20.04 and not some weird fork.  (If you are compiling/building your own kernel, then I will bow out of this conversation.)

Debug kernel memory usage is more complicated, but there are tools for this.  Let's start with some generic ones that are not complicated.  Do the same procedure you have been doing, but for the following commands and put into separate files:

* `sudo vmstat -s`
* `sudo vmstat -m`

Please do that and let's see what we can figure out.  The latter command will also give me some idea of what types of drivers/stuff you have on your system.

Now let's talk about your problem report.

Your report intentionally omits relevant data -- in particular, whether or not you are GPU mining, and regardless of GPU vs. CPU (or both), what algorithm you're using along with your relevant XMRig invocation flags and/or config.json.  I'd like to see those.  Please edit out any personal data (ex. wallet addresses) by replacing them with XXXs.

Why this matters:

If GPU mining: GPUs do their own Happy Fun Stuff(tm) with both on-board and system memory, depending on what it is that's being done.  There is always a possibility that the XMRig CUDA plugin does something a little odd and NVIDIA drivers don't do the right thing.  Don't kid yourself thinking NVIDIA (or AMD!) has flawless drivers.  I can't really help you troubleshoot GPU driver issues, but the vmstat data might help narrow it down.

If **only** CPU mining: then there is something very uncomfortable going on.  If this is the case, I would like to reproduce this problem myself if possible, so please disclose pool and algorithm as I have multiple bare-metal Ubuntu-based systems (of varying kernel versions) that I can analyse.

## d4f5409d | 2024-03-02T08:53:29+00:00
I'll print out the logs later, now I can tell you that I didn't use any GPU mining, because of my opinion it's unstable. I use Zorin OS, not some random weird fork and I do not compile my kernel for myself, so this shouldn't happened the first place. I am pretty sure to stick with it, because I like it better than stock Ubuntu. I'll contact the developers to check up on this issue. Maybe I can tell you another useful information: the 1GB pages not everytime have 100% efficiency as I mean I have to restart over and over again to get 100%, because I sometimes only get 11% or 89% or not at all, 0% when I start xmrig.

## koitsu | 2024-03-02T09:44:14+00:00
Please provide what I asked for in the last paragraph of my above comment.  You omitted it originally, and you're omitting it again.  I'm not even going to get into a discussion about 1GB page efficiency until you provide that information.  Pool/algo information, as well as your XMRig configuration (both command-line invocation flags and the config.json) are needed to even begin this discussion.

Any fork of Ubuntu is "weird", and the fork maintainers are likely going to tell you "we use Ubuntu, so, uh, talk to Canonical or the LKML".  Hint: I'm a UNIX sysadmin who has been practising over 30 years, was a FreeBSD committer and project member for several years, etc..  I've been around a long while and know exactly how these things will pan out.  Stick with running mainstream stuff if possible.  I would seriously consider installing stock Ubuntu on a USB stick along with your XMRig config/setup and see if the same problem happens then.  Whole process would take 30 minutes at most.  That way you can determine if it's a Zorin OS thing or not.

## d4f5409d | 2024-03-03T20:38:11+00:00
@koitsu Can you provide your public PGP key please? I've got the files you asked for.

## koitsu | 2024-03-03T22:00:34+00:00
I have a PGP key but I don't see why that's applicable here.  This is an open-source project where bugs/issues should be discussed openly -- XMRig maintainer should be able to look at these, as well as any other person of interest.  There is nothing secretive about XMRig invocations or config.json contents (other than XXX'ing out your wallet address, passwords, or other identifying info).  If you are using a private (non-public) pool, then giving me the pool details aren't going to help anyway since I want to be able to reproduce this problem and I wouldn't have access to said pool.  I regret commenting at all if time vampiring and paranoia are going to be present.

## d4f5409d | 2024-03-03T22:15:56+00:00
I regret asking a person to appreciate my privacy who calls me paranoid just because I care about it. Anyways, can not disclose the pool then, we should move on.

http://0.vern.cc/IV.zip

## d4f5409d | 2024-03-07T16:04:22+00:00
After receiving an update to Zorin OS today, ram finally gets freed every time, **but not all of it**. There is a small percent of it that still remains allocated and it adds up after I start and close and start xmrig over and over again. However, the allocated remains do not seem to go above a certain amount.

## d4f5409d | 2024-04-23T17:26:37+00:00
After compiling and switching to v6.21.3, **the issue seems to almost completely disappear** at first glance. What I still see is, there are small chunks of RAM, that after multiple terminations still don't get freed, and those add up, but the chart tells everything. 

### Very good job guys, thank you!
![Képernyőkép ekkor: 2024-04-23 19-20-43](https://github.com/xmrig/xmrig/assets/76624594/29bffedc-cb84-46d6-9aad-5eb9570f37d0)


# Action History
- Created by: d4f5409d | 2024-02-26T15:08:52+00:00
- Closed at: 2024-04-23T17:26:37+00:00
