---
title: 'Daemon''s "output_histogram" command produces error: "Couldn''t connect to
  daemon"'
source_url: https://github.com/monero-project/monero/issues/1208
author: peanutsformonkeys
assignees: []
labels:
- wontfix
created_at: '2016-10-11T23:37:07+00:00'
updated_at: '2018-01-08T12:56:28+00:00'
type: issue
status: closed
closed_at: '2018-01-08T12:56:28+00:00'
---

# Original Description
After reading this [SE question](https://monero.stackexchange.com/questions/158/determining-the-number-of-available-outputs-by-denomination), I was trying the example command `monerod output_histogram 5 9`, but I always get the following error after a few minutes:

```
$ monerod output_histogram 5 9
Creating the logger system
Error: Couldn't connect to daemon
```

When I try to open a wallet after that, that initially seems to go fine, i.e. printing the address and the help banner, but then it appears to be blocked for a while, and shows the following message twice:

```
Error: Daemon uses a different RPC version that the wallet: http://localhost:18081. Either update one of them, or use --allow-mismatched-daemon-version.
Error: Daemon uses a different RPC version that the wallet: http://localhost:18081. Either update one of them, or use --allow-mismatched-daemon-version.
```

Waiting a bit longer then displays the wallet prompt. Typing `balance` works, pressumably from cache, as typing `refresh` just seems to hang forever (**update:** after 10 minutes or so, it gave up with the above daemon error). Similarly, issuing `monerod status` in another terminal also hangs, and eventually says `Error: Couldn't connect to daemon`. Killing the `monerod` daemon is the only option left.

It seems that the `output_histogram` command destabilizes the health of the daemon, at least on my system. I am on macOS (Mavericks) with 8 GB of RAM. Monero version 0.10.0.0.


# Discussion History
## moneromooo-monero | 2016-10-15T18:31:00+00:00
Hard disk or SSD ?

Works for me with a lot less RAM.


## peanutsformonkeys | 2016-10-16T01:15:01+00:00
It is a old Mac mini with a slow 5400 rpm drive.


## moneromooo-monero | 2016-10-16T09:05:49+00:00
Can you tell whether it's super busy with disk I/O ?
If you have top, that'd be the "wa" column near the top.


## peanutsformonkeys | 2016-10-16T12:40:48+00:00
I don't see this "wa" value in `top`. When I check `iostat` when starting `monerod output_histogram 5 9`, I don't think there's any significant uptick in disk I/O:

```
$ iostat 1
          disk0       cpu     load average
    KB/t tps  MB/s  us sy id   1m   5m   15m
   19.84  19  0.36  43  3 54  1.67 1.71 1.65
    4.00  75  0.29   3  2 95  1.67 1.71 1.65
    4.00  74  0.29   1  2 97  1.61 1.69 1.64
    4.00  80  0.31   2  2 96  1.61 1.69 1.64
    7.03 111  0.76   2  2 95  1.61 1.69 1.64
    4.26 106  0.44   1  2 97  1.61 1.69 1.64
    4.00  82  0.32   2  2 96  1.61 1.69 1.64
    4.00  79  0.31   1  2 98  1.57 1.68 1.64
    4.00  77  0.30   2  5 94  1.57 1.68 1.64
    7.19  72  0.51   2  3 95  1.57 1.68 1.64
    4.00  73  0.28   2  2 96  1.57 1.68 1.64
    4.00  76  0.30   2  2 97  1.57 1.68 1.64
    4.00  96  0.37   2  2 96  1.52 1.67 1.63
    4.00 125  0.49   2  2 96  1.52 1.67 1.63
    4.00 109  0.42   2  3 95  1.52 1.67 1.63
    4.00 106  0.41   2  2 96  1.52 1.67 1.63
    4.00  84  0.33   3  4 93  1.52 1.67 1.63
    4.00  74  0.29   2  3 95  1.48 1.66 1.63
    4.00  74  0.29   2  3 95  1.48 1.66 1.63
    4.00  73  0.28   2  3 95  1.48 1.66 1.63
```

However, this time, the wallet still seems to interact fine with the daemon, albeit more slowly. I can open it, refresh, and close. I guess I might have had another CPU intensive process active last time that made that part difficult. However, the `monerod output_histogram` command still fails after a while:

```
$ monerod output_histogram 5 9
Creating the logger system
Error: Couldn't connect to daemon
```

**Edit:** I still have to kill and restart the daemon after trying that command a few times.


## moneromooo-monero | 2016-10-22T16:35:40+00:00
Still works here. Run monerod with --log-level 2

Once you get the error, use gdb to get the stack trace of threads in the running daemon:

gdb monerod `pidof monerod`
thread apply all bt

And paste the output of this here (there will be several pages).


## peanutsformonkeys | 2016-10-22T18:45:19+00:00
Each attempt failed here, tried 3 times.

```
Mac-mini:~ user$ monerod output_histogram 5 9
Creating the logger system
Error: Couldn't connect to daemon
Mac-mini:~ user$ monerod output_histogram 5 9
Creating the logger system
Error: Couldn't connect to daemon
Mac-mini:~ user$ monerod output_histogram 5 9
Creating the logger system
Error: Couldn't connect to daemon
Mac-mini:~ user$ 
```

Then, started up `gdb`:

```
Mac-mini:~ user$ gdb monerod 55697
GNU gdb (GDB) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-apple-darwin13.4.0".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from monerod...
warning: Could not open OSO archive file "/usr/local/lib/libboost_chrono.a"

warning: Could not open OSO archive file "/usr/local/lib/libboost_date_time.a"

warning: Could not open OSO archive file "/usr/local/lib/libboost_filesystem.a"

warning: Could not open OSO archive file "/usr/local/lib/libboost_program_options.a"

warning: Could not open OSO archive file "/usr/local/lib/libboost_regex.a"

warning: Could not open OSO archive file "/usr/local/lib/libboost_serialization.a"

warning: Could not open OSO archive file "/usr/local/lib/libboost_system.a"

warning: Could not open OSO archive file "/usr/local/lib/libboost_thread-mt.a"
(no debugging symbols found)...done.
Attaching to program: /opt/monero.mac.x64.v0-10-0-0/monerod, process 55697
Unable to find Mach task port for process-id 55697: (os/kern) failure (0x5).
 (please check gdb is codesigned - see taskgated(8))
/Users/user/55697: No such file or directory.
(gdb) thread apply all bt
(gdb) quit
```

However, nothing happens after I typed `thread apply all bt`. Could this be because my `gdb` is installed via Homebrew? My Monero software is just the released binaries which I put in `/opt`. Maybe I should try all this on a more recent version of macOS.


## moneromooo-monero | 2016-10-30T11:48:01+00:00
That's because there's no process 55697 by the time you run gdb:
/Users/user/55697: No such file or directory.
So it tries to interpret this as a filename, which doesn't exist either.


## moneromooo-monero | 2017-10-19T16:10:52+00:00
This is probably because this is a very slow operation, and the client times out. This doesn't happen when called from the running daemon itself as it doesn't go through RPC. Not sure how to change that, and whether it's worth the work.

## dEBRUYNE-1 | 2018-01-08T12:52:54+00:00
+wontfix

# Action History
- Created by: peanutsformonkeys | 2016-10-11T23:37:07+00:00
- Closed at: 2018-01-08T12:56:28+00:00
