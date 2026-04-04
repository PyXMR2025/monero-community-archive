---
title: can't start daemon
source_url: https://github.com/monero-project/monero/issues/6530
author: alexstaj
assignees: []
labels: []
created_at: '2020-05-13T22:59:08+00:00'
updated_at: '2020-05-14T23:15:18+00:00'
type: issue
status: closed
closed_at: '2020-05-14T23:15:18+00:00'
---

# Original Description
ran:

```
MacOS % ./monerod --testnet
2020-05-13 22:36:59.660	I Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)
2020-05-13 22:36:59.660	I Initializing cryptonote protocol...
2020-05-13 22:36:59.660	I Cryptonote protocol initialized OK
2020-05-13 22:36:59.660	I Initializing core...
2020-05-13 22:36:59.660	I Loading blockchain from folder /Users/tha/.bitmonero/testnet/lmdb ...
2020-05-13 22:36:59.662	W Failed to open lmdb environment: No space left on device
2020-05-13 22:36:59.662	E Error opening database: Failed to open lmdb environment: No space left on device
2020-05-13 22:36:59.663	I Stopping cryptonote protocol...
2020-05-13 22:36:59.663	I Cryptonote protocol stopped successfully
2020-05-13 22:36:59.663	E Exception in main! Failed to initialize core
```

log file says:
```
2020-05-13 22:36:59.659	     0x10c6efdc0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-05-13 22:36:59.660	     0x10c6efdc0	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)
2020-05-13 22:36:59.660	     0x10c6efdc0	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2020-05-13 22:36:59.660	     0x10c6efdc0	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2020-05-13 22:36:59.660	     0x10c6efdc0	INFO	global	src/daemon/core.h:63	Initializing core...
2020-05-13 22:36:59.660	     0x10c6efdc0	INFO	global	src/cryptonote_core/cryptonote_core.cpp:506	Loading blockchain from folder /Users/tha/.bitmonero/testnet/lmdb ...
2020-05-13 22:36:59.662	     0x10c6efdc0	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to open lmdb environment: No space left on device
2020-05-13 22:36:59.662	     0x10c6efdc0	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:607	Error opening database: Failed to open lmdb environment: No space left on device
2020-05-13 22:36:59.663	     0x10c6efdc0	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2020-05-13 22:36:59.663	     0x10c6efdc0	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2020-05-13 22:36:59.663	     0x10c6efdc0	ERROR	daemon	src/daemon/main.cpp:339	Exception in main! Failed to initialize core

```

# Discussion History
## selsta | 2020-05-13T23:04:15+00:00
> No space left on device


## alexstaj | 2020-05-13T23:08:54+00:00
yes but my drive has 1.45TB free.  I believe there is some error with lmdb not operating properly on MacOS  10.15.4 formatted with an APFS drive perhaps?

## selsta | 2020-05-13T23:10:21+00:00
APFS should work fine. I use it myself.

Is it the main drive? Is it an external hard disk / network share?

## alexstaj | 2020-05-13T23:11:01+00:00
main drive and I even gave terminal and monero-wallet-gui.app full disk access in the security and privacy preference pane.

## moneromooo-monero | 2020-05-14T13:39:52+00:00
liblmdb reuses ENOSPC when opening the db, so it might not be actual no space left. Try this:

```
diff --git a/external/db_drivers/liblmdb/mdb.c b/external/db_drivers/liblmdb/mdb.c
index ba1315401..4c41eff0e 100644
--- a/external/db_drivers/liblmdb/mdb.c
+++ b/external/db_drivers/liblmdb/mdb.c
@@ -4166,7 +4166,10 @@ mdb_env_init_meta(MDB_env *env, MDB_meta *meta)
        else if ((unsigned) len == psize * NUM_METAS)
                rc = MDB_SUCCESS;
        else
+       {
+               printf("rc: %s\n", strerror(rc));
                rc = ENOSPC;
+       }
        free(p);
        return rc;
 }
```


If this is where it's coming from, this should tell us what the actual error is.

## alexstaj | 2020-05-14T19:46:28+00:00
so I did 
```
git clone --recursive https://github.com/monero-project/monero
```

then I went into /monero/external/db_drivers/liblmdb/mdb.c

and added
```
        printf("rc: %s\n", strerror(rc));
```
in a new line just before
```
		rc = ENOSPC;
```
that was previously at line 4169.

I then ran

```
make
```
which compiled the master.

After running 
```
monerod --testnet
```

I still get the same error and the log file still looks the same.

So either my change did not get implemented or it did not print the error.

Your help is most appreciatd.

Thanks

## selsta | 2020-05-14T19:49:31+00:00
Did you add the `{}` around the else? Only adding printf is not enough. Also did you open the correct binary? It is `build/Darwin/master/release/bin/monerod`

## alexstaj | 2020-05-14T19:57:14+00:00
yes. here is line 4163 to 4175 in my edited file and yes I ran the newly built file at the same location you mention.
```
	DO_PWRITE(rc, env->me_fd, p, psize * NUM_METAS, len, 0);
	if (!rc)
		rc = ErrCode();
	else if ((unsigned) len == psize * NUM_METAS)
		rc = MDB_SUCCESS;
	else
    {
        printf("rc: %s\n", strerror(rc));
		rc = ENOSPC;
    }
    free(p);
	return rc;
}
```

## moneromooo-monero | 2020-05-14T22:17:56+00:00
Then it's likely really a ENOSPC from the OS.
You can run with strace, eg:
strace -o monerod.out ./monerod --testnet
Also:
df -h /Users/tha/.bitmonero/testnet/lmdb

## alexstaj | 2020-05-14T22:24:37+00:00
can you tell me how to do this with dtrace as MacOS does not have strace

## moneromooo-monero | 2020-05-14T22:25:27+00:00
No. Duckduckgo can likely find out.

## alexstaj | 2020-05-14T22:41:36+00:00
I was able to run dtruss instead.  let me know if anything catches your eye. thanks!

```
tha@thas-Mac-mini bin % sudo dtruss ./monerod --testnet 
dtrace: system integrity protection is on, some features will not be available

SYSCALL(args) 		 = return
open("/dev/dtracehelper\0", 0x2, 0xFFFFFFFFE386C040)		 = 3 0
ioctl(0x3, 0x80086804, 0x7FFEE386BF50)		 = 0 0
close(0x3)		 = 0 0
mprotect(0x10D376000, 0x1000, 0x1)		 = 0 0
mprotect(0x10D396000, 0x1000, 0x1)		 = 0 0
mprotect(0x10D3DF000, 0x5000, 0x1)		 = 0 0
mprotect(0x10F978000, 0x12000, 0x1)		 = 0 0
mprotect(0x10F756000, 0xF000, 0x1)		 = 0 0
mprotect(0x10D4DD000, 0x4000, 0x1)		 = 0 0
mprotect(0x10D5B0000, 0x6000, 0x1)		 = 0 0
mprotect(0x10D633000, 0x1000, 0x1)		 = 0 0
mprotect(0x10D683000, 0x1000, 0x1)		 = 0 0
mprotect(0x10D6BF000, 0x2000, 0x1)		 = 0 0
mprotect(0x10D6DE000, 0x1000, 0x1)		 = 0 0
mprotect(0x10DA8D000, 0x29000, 0x1)		 = 0 0
mprotect(0x10D8C9000, 0x8000, 0x1)		 = 0 0
mprotect(0x10FA1E000, 0x1000, 0x1)		 = 0 0
mprotect(0x10D789000, 0x4000, 0x1)		 = 0 0
mprotect(0x10D7A4000, 0x1000, 0x1)		 = 0 0
mprotect(0x10D7DD000, 0x2000, 0x1)		 = 0 0
mprotect(0x10D85B000, 0x2000, 0x1)		 = 0 0
mprotect(0x10CDDD000, 0x27000, 0x1)		 = 0 0
access("/AppleInternal/XBS/.isChrooted\0", 0x0, 0x0)		 = -1 2
bsdthread_register(0x7FFF6911AB7C, 0x7FFF6911AB68, 0x2000)		 = 1073742047 0
sysctlbyname(kern.bootargs, 0xD, 0x7FFEE386AAC0, 0x7FFEE386AAB0, 0x0)		 = 0 0
ioctl(0x2, 0x4004667A, 0x7FFEE386AD34)		 = 0 0
mprotect(0x10FA2E000, 0x1000, 0x0)		 = 0 0
mprotect(0x10FA38000, 0x1000, 0x0)		 = 0 0
mprotect(0x10FA39000, 0x1000, 0x0)		 = 0 0
mprotect(0x10FA43000, 0x1000, 0x0)		 = 0 0
mprotect(0x10FA44000, 0x1000, 0x0)		 = 0 0
mprotect(0x10FA4E000, 0x1000, 0x0)		 = 0 0
mprotect(0x10D37F000, 0x90, 0x1)		 = 0 0
mprotect(0x10D370000, 0x1000, 0x1)		 = 0 0
mprotect(0x10D37F000, 0x90, 0x3)		 = 0 0
mprotect(0x10D37F000, 0x90, 0x1)		 = 0 0
issetugid(0x0, 0x0, 0x0)		 = 0 0
getentropy(0x7FFEE3869D80, 0x20, 0x0)		 = 0 0
getentropy(0x7FFEE3869DD0, 0x40, 0x0)		 = 0 0
getpid(0x0, 0x0, 0x0)		 = 13976 0
stat64("/AppleInternal\0", 0x7FFEE386AF30, 0x0)		 = -1 2
csops_audittoken(0x3698, 0x7, 0x7FFEE386AA80)		 = -1 22
proc_info(0x2, 0x3698, 0xD)		 = 64 0
csops_audittoken(0x3698, 0x7, 0x7FFEE386A300)		 = -1 22
geteuid(0x0, 0x0, 0x0)		 = 0 0
getuid(0x0, 0x0, 0x0)		 = 0 0
dtrace: error on enabled probe ID 2210 (ID 572: syscall::sysctl:return): invalid kernel access in action #10 at DIF offset 28
gettid(0x7FFEE3869B50, 0x7FFEE3869B54, 0x0)		 = -1 3
geteuid(0x0, 0x0, 0x0)		 = 0 0
getegid(0x0, 0x0, 0x0)		 = 0 0
csops(0x3698, 0x0, 0x7FFEE386A8AC)		 = 0 0
gettid(0x7FFEE3869B20, 0x7FFEE3869B24, 0x0)		 = -1 3
geteuid(0x0, 0x0, 0x0)		 = 0 0
getegid(0x0, 0x0, 0x0)		 = 0 0
open_nocancel(".\0", 0x0, 0x1)		 = 3 0
fstat64(0x3, 0x7FFEE386A9D0, 0x0)		 = 0 0
fcntl_nocancel(0x3, 0x32, 0x7FFEE386ABF0)		 = 0 0
close_nocancel(0x3)		 = 0 0
stat64("/Users/tha/tools/monero/build/Darwin/master/release/bin\0", 0x7FFEE386A940, 0x0)		 = 0 0
open_nocancel(".\0", 0x0, 0x1)		 = 3 0
fstat64(0x3, 0x7FFEE386A9D0, 0x0)		 = 0 0
fcntl_nocancel(0x3, 0x32, 0x7FFEE386ABF0)		 = 0 0
close_nocancel(0x3)		 = 0 0
stat64("/Users/tha/tools/monero/build/Darwin/master/release/bin\0", 0x7FFEE386A940, 0x0)		 = 0 0
open_nocancel(".\0", 0x0, 0x1)		 = 3 0
fstat64(0x3, 0x7FFEE386A9D0, 0x0)		 = 0 0
fcntl_nocancel(0x3, 0x32, 0x7FFEE386ABF0)		 = 0 0
close_nocancel(0x3)		 = 0 0
stat64("/Users/tha/tools/monero/build/Darwin/master/release/bin\0", 0x7FFEE386A940, 0x0)		 = 0 0
open_nocancel(".\0", 0x0, 0x1)		 = 3 0
fstat64(0x3, 0x7FFEE386A9D0, 0x0)		 = 0 0
fcntl_nocancel(0x3, 0x32, 0x7FFEE386ABF0)		 = 0 0
close_nocancel(0x3)		 = 0 0
stat64("/Users/tha/tools/monero/build/Darwin/master/release/bin\0", 0x7FFEE386A940, 0x0)		 = 0 0
dtrace: error on enabled probe ID 2210 (ID 572: syscall::sysctl:return): invalid kernel access in action #10 at DIF offset 28
mlock(0x10CE6D000, 0x1000, 0x0)		 = 0 0
open("/dev/urandom\0", 0x1020000, 0xFFFFFFFFE386CC18)		 = 3 0
dtrace: error on enabled probe ID 2186 (ID 174: syscall::read:return): invalid kernel access in action #12 at DIF offset 68
close(0x3)		 = 0 0
sysctlbyname(hw.ncpu, 0x7, 0x7FFEE386B104, 0x7FFEE386B0F8, 0x0)		 = 0 0
2020-05-14 22:39:29.930	I Monero 'Carbon Chamaeleon' (v0.15.0.0-77a008f71)
2020-05-14 22:39:29.930	I Initializing cryptonote protocol...
2020-05-14 22:39:29.930	I Cryptonote protocol initialized OK
2020-05-14 22:39:29.931	I Initializing core...
2020-05-14 22:39:29.931	I Loading blockchain from folder /Users/tha/.bitmonero/testnet/lmdb ...
2020-05-14 22:39:29.933	W Failed to open lmdb environment: No space left on device
2020-05-14 22:39:29.933	E Error opening database: Failed to open lmdb environment: No space left on device
2020-05-14 22:39:29.933	I Stopping cryptonote protocol...
2020-05-14 22:39:29.933	I Cryptonote protocol stopped successfully
2020-05-14 22:39:29.933	E Exception in main! Failed to initialize core
issetugid(0x0, 0x0, 0x0)		 = 0 0
open_nocancel("/var/db/timezone/zoneinfo/UTC\0", 0x0, 0xE)		 = 3 0
fstat64(0x3, 0x7FFEE386B378, 0x0)		 = 0 0
dtrace: error on enabled probe ID 2187 (ID 960: syscall::read_nocancel:return): invalid kernel access in action #12 at DIF offset 68
close_nocancel(0x3)		 = 0 0
issetugid(0x0, 0x0, 0x0)		 = 0 0
open_nocancel("/var/db/timezone/zoneinfo/posixrules\0", 0x0, 0x0)		 = 3 0
fstat64(0x3, 0x7FFEE386B1B8, 0x0)		 = 0 0
dtrace: error on enabled probe ID 2187 (ID 960: syscall::read_nocancel:return): invalid kernel access in action #12 at DIF offset 68
close_nocancel(0x3)		 = 0 0
shm_open(0x7FFF6910F280, 0x0, 0x0)		 = 3 0
mmap(0x0, 0x1000, 0x1, 0x1, 0x3, 0x0)		 = 0x10D381000 0
close_nocancel(0x3)		 = 0 0
getuid(0x0, 0x0, 0x0)		 = 0 0
geteuid(0x0, 0x0, 0x0)		 = 0 0
getgid(0x0, 0x0, 0x0)		 = 0 0
getegid(0x0, 0x0, 0x0)		 = 0 0
getrlimit(0x1008, 0x7FFEE386BEB0, 0x0)		 = 0 0
open_nocancel("/usr/local/etc/openssl@1.1/openssl.cnf\0", 0x0, 0x1B6)		 = 3 0
fstat64(0x3, 0x7FFEE386BCE8, 0x0)		 = 0 0
dtrace: error on enabled probe ID 2187 (ID 960: syscall::read_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2187 (ID 960: syscall::read_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2187 (ID 960: syscall::read_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2187 (ID 960: syscall::read_nocancel:return): invalid kernel access in action #12 at DIF offset 68
close_nocancel(0x3)		 = 0 0
socketpair(0x1, 0x1, 0x0)		 = 0 0
fcntl(0x3, 0x3, 0x0)		 = 2 0
fcntl(0x3, 0x4, 0x6)		 = 0 0
fcntl(0x4, 0x3, 0x0)		 = 2 0
fcntl(0x4, 0x4, 0x6)		 = 0 0
socketpair(0x1, 0x1, 0x0)		 = 0 0
fcntl(0x5, 0x3, 0x0)		 = 2 0
fcntl(0x5, 0x4, 0x6)		 = 0 0
fcntl(0x6, 0x3, 0x0)		 = 2 0
fcntl(0x6, 0x4, 0x6)		 = 0 0
close(0x3)		 = 0 0
close(0x4)		 = 0 0
close(0x5)		 = 0 0
close(0x6)		 = 0 0
open_nocancel(".\0", 0x0, 0x1)		 = 3 0
fstat64(0x3, 0x7FFEE386B800, 0x0)		 = 0 0
fcntl_nocancel(0x3, 0x32, 0x7FFEE386BA20)		 = 0 0
close_nocancel(0x3)		 = 0 0
stat64("/Users/tha/tools/monero/build/Darwin/master/release/bin\0", 0x7FFEE386B770, 0x0)		 = 0 0
open_nocancel(".\0", 0x0, 0x1)		 = 3 0
fstat64(0x3, 0x7FFEE386B800, 0x0)		 = 0 0
fcntl_nocancel(0x3, 0x32, 0x7FFEE386BA20)		 = 0 0
close_nocancel(0x3)		 = 0 0
stat64("/Users/tha/tools/monero/build/Darwin/master/release/bin\0", 0x7FFEE386B770, 0x0)		 = 0 0
open_nocancel(".\0", 0x0, 0x1)		 = 3 0
fstat64(0x3, 0x7FFEE386B800, 0x0)		 = 0 0
fcntl_nocancel(0x3, 0x32, 0x7FFEE386BA20)		 = 0 0
close_nocancel(0x3)		 = 0 0
stat64("/Users/tha/tools/monero/build/Darwin/master/release/bin\0", 0x7FFEE386B770, 0x0)		 = 0 0
open_nocancel(".\0", 0x0, 0x1)		 = 3 0
fstat64(0x3, 0x7FFEE386B800, 0x0)		 = 0 0
fcntl_nocancel(0x3, 0x32, 0x7FFEE386BA20)		 = 0 0
close_nocancel(0x3)		 = 0 0
stat64("/Users/tha/tools/monero/build/Darwin/master/release/bin\0", 0x7FFEE386B770, 0x0)		 = 0 0
open_nocancel(".\0", 0x0, 0x1)		 = 3 0
fstat64(0x3, 0x7FFEE386BA20, 0x0)		 = 0 0
fcntl_nocancel(0x3, 0x32, 0x7FFEE386BC40)		 = 0 0
close_nocancel(0x3)		 = 0 0
stat64("/Users/tha/tools/monero/build/Darwin/master/release/bin\0", 0x7FFEE386B990, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/bitmonero.conf\0", 0x7FFEE386C1B0, 0x0)		 = -1 2
open_nocancel(".\0", 0x0, 0x1)		 = 3 0
fstat64(0x3, 0x7FFEE386BC30, 0x0)		 = 0 0
fcntl_nocancel(0x3, 0x32, 0x7FFEE386BE50)		 = 0 0
close_nocancel(0x3)		 = 0 0
stat64("/Users/tha/tools/monero/build/Darwin/master/release/bin\0", 0x7FFEE386BBA0, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = -1 2
mkdir("/Users/\0", 0x1FB, 0x0)		 = -1 17
mkdir("/Users/tha/\0", 0x1FB, 0x0)		 = -1 17
mkdir("/Users/tha/.bitmonero/\0", 0x1FB, 0x0)		 = -1 17
mkdir("/Users/tha/.bitmonero/testnet/\0", 0x1FB, 0x0)		 = 0 0
open_nocancel("/Users/tha/.bitmonero/testnet/bitmonero.log\0", 0x209, 0x1B6)		 = 3 0
lseek(0x3, 0x0, 0x2)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x1)		 = 0 0
fstat64(0x3, 0x7FFEE386B9F8, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BC50, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
lseek(0x3, 0x0, 0x0)		 = 0 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x0, 0x1)		 = 294 0
lseek(0x3, 0x126, 0x0)		 = 294 0
stat64("/Users/tha/.bitmonero/testnet\0", 0x7FFEE386C0B0, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
lseek(0x3, 0x126, 0x0)		 = 294 0
lseek(0x3, 0x126, 0x0)		 = 294 0
lseek(0x3, 0x126, 0x0)		 = 294 0
lseek(0x3, 0x126, 0x0)		 = 294 0
lseek(0x3, 0x126, 0x0)		 = 294 0
lseek(0x3, 0x126, 0x0)		 = 294 0
lseek(0x3, 0x126, 0x0)		 = 294 0
lseek(0x3, 0x126, 0x0)		 = 294 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x0, 0x1)		 = 420 0
lseek(0x3, 0x1A4, 0x0)		 = 420 0
fstat64(0x1, 0x7FFEE386BB38, 0x0)		 = 0 0
ioctl(0x1, 0x4004667A, 0x7FFEE386BB84)		 = 0 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x1A4, 0x0)		 = 420 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x0, 0x1)		 = 534 0
lseek(0x3, 0x216, 0x0)		 = 534 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x216, 0x0)		 = 534 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x0, 0x1)		 = 647 0
lseek(0x3, 0x287, 0x0)		 = 647 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x287, 0x0)		 = 647 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x0, 0x1)		 = 742 0
lseek(0x3, 0x2E6, 0x0)		 = 742 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
stat64("/Users/tha/.bitmonero/testnet\0", 0x7FFEE386BC10, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/blockchain.bin\0", 0x7FFEE386BC10, 0x0)		 = -1 2
lseek(0x3, 0x2E6, 0x0)		 = 742 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x0, 0x1)		 = 909 0
lseek(0x3, 0x38D, 0x0)		 = 909 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
stat64("/Users/tha/.bitmonero/testnet/lmdb\0", 0x7FFEE386B990, 0x0)		 = -1 2
stat64("/Users/tha/.bitmonero/testnet/lmdb\0", 0x7FFEE386B980, 0x0)		 = -1 2
stat64("/Users/tha/.bitmonero/testnet\0", 0x7FFEE386B980, 0x0)		 = 0 0
mkdir("/Users/tha/.bitmonero/testnet/lmdb\0", 0x1FF, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/data.mdb\0", 0x7FFEE386B990, 0x0)		 = -1 2
stat64("/Users/tha/.bitmonero/testnet/lock.mdb\0", 0x7FFEE386B990, 0x0)		 = -1 2
open("/Users/tha/.bitmonero/testnet/lmdb/lock.mdb\0", 0x1000202, 0x1A4)		 = 4 0
fcntl(0x4, 0x8, 0x7FFEE386B810)		 = 0 0
lseek(0x4, 0x0, 0x2)		 = 0 0
ftruncate(0x4, 0x2000, 0x0)		 = 0 0
mmap(0x0, 0x2000, 0x3, 0x1, 0x4, 0x0)		 = 0x10D382000 0
stat64("/Users/tha/.bitmonero/testnet/lmdb/lock.mdb\0", 0x7FFEE386B7A8, 0x0)		 = 0 0
semget(0x4D047EE1, 0x2, 0x3A4)		 = -1 28
madvise(0x7FC570330000, 0x200000, 0x7)		 = 0 0
madvise(0x7FC570330000, 0x200000, 0x7)		 = 0 0
munmap(0x10D382000, 0x2000)		 = 0 0
close(0x4)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B280, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B280, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B280, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B280, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B280, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B280, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B280, 0x0)		 = 0 0
lseek(0x3, 0x38D, 0x0)		 = 909 0
lseek(0x3, 0x38D, 0x0)		 = 909 0
lseek(0x3, 0x38D, 0x0)		 = 909 0
lseek(0x3, 0x38D, 0x0)		 = 909 0
lseek(0x3, 0x38D, 0x0)		 = 909 0
lseek(0x3, 0x38D, 0x0)		 = 909 0
lseek(0x3, 0x38D, 0x0)		 = 909 0
lseek(0x3, 0x38D, 0x0)		 = 909 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x0, 0x1)		 = 1072 0
lseek(0x3, 0x430, 0x0)		 = 1072 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B5B0, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B5B0, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B5B0, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B5B0, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B5B0, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B5B0, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386B5B0, 0x0)		 = 0 0
lseek(0x3, 0x430, 0x0)		 = 1072 0
lseek(0x3, 0x430, 0x0)		 = 1072 0
lseek(0x3, 0x430, 0x0)		 = 1072 0
lseek(0x3, 0x430, 0x0)		 = 1072 0
lseek(0x3, 0x430, 0x0)		 = 1072 0
lseek(0x3, 0x430, 0x0)		 = 1072 0
lseek(0x3, 0x430, 0x0)		 = 1072 0
lseek(0x3, 0x430, 0x0)		 = 1072 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x0, 0x1)		 = 1247 0
lseek(0x3, 0x4DF, 0x0)		 = 1247 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
madvise(0x7FC5700A0000, 0x188000, 0x7)		 = 0 0
lseek(0x3, 0x4DF, 0x0)		 = 1247 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x0, 0x1)		 = 1357 0
lseek(0x3, 0x54D, 0x0)		 = 1357 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x54D, 0x0)		 = 1357 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x0, 0x1)		 = 1476 0
lseek(0x3, 0x5C4, 0x0)		 = 1476 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
stat64("/Users/tha/.bitmonero/testnet/\0", 0x7FFEE386BB50, 0x0)		 = 0 0
lseek(0x3, 0x5C4, 0x0)		 = 1476 0
lseek(0x3, 0x5C4, 0x0)		 = 1476 0
lseek(0x3, 0x5C4, 0x0)		 = 1476 0
lseek(0x3, 0x5C4, 0x0)		 = 1476 0
lseek(0x3, 0x5C4, 0x0)		 = 1476 0
lseek(0x3, 0x5C4, 0x0)		 = 1476 0
lseek(0x3, 0x5C4, 0x0)		 = 1476 0
lseek(0x3, 0x5C4, 0x0)		 = 1476 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
lseek(0x3, 0x0, 0x1)		 = 1599 0
lseek(0x3, 0x63F, 0x0)		 = 1599 0
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
dtrace: error on enabled probe ID 2185 (ID 962: syscall::write_nocancel:return): invalid kernel access in action #12 at DIF offset 68
stat64("/usr/lib/libstdc++.6.dylib\0", 0x7FFEE386B5D0, 0x0)		 = 0 0
stat64("/\0", 0x7FFEE3869AF0, 0x0)		 = 0 0
getattrlist("/usr\0", 0x1181CE8B8, 0x7FFEE386B440)		 = 0 0
getattrlist("/usr/lib\0", 0x1181CE8B8, 0x7FFEE386B440)		 = 0 0
getattrlist("/usr/lib/libstdc++.6.dylib\0", 0x1181CE8B8, 0x7FFEE386B440)		 = 0 0
readlink("/usr/lib/libstdc++.6.dylib\0", 0x7FFEE386A840, 0x400)		 = 21 0
getattrlist("/usr/lib/libstdc++.6.0.9.dylib\0", 0x1181CE8B8, 0x7FFEE386B440)		 = 0 0
munlock(0x10CE6D000, 0x1000, 0x0)		 = 0 0

```

## selsta | 2020-05-14T22:43:16+00:00
Also can you post the output of `df -h /Users/tha/.bitmonero/testnet/lmdb`?

## alexstaj | 2020-05-14T22:44:52+00:00
here it is:
```
tha@thas-Mac-mini bin % df -h /Users/tha/.bitmonero/testnet/lmdb
Filesystem     Size   Used  Avail Capacity iused       ifree %iused  Mounted on
/dev/disk1s1  1.8Ti  509Gi  1.3Ti    28%  983391 19538045369    0%   /System/Volumes/Data
```

## alexstaj | 2020-05-14T22:45:45+00:00
the only thing in the lmdb folder is lock.mdb and its 8kb in size.

## moneromooo-monero | 2020-05-14T22:58:36+00:00
Looks like you're hitting:

       ENOSPC A semaphore set has to be created but the system limit for the maximum number of semaphore sets (SEMMNI), or the system wide maximum number  of  sema‐
              phores (SEMMNS), would be exceeded.

No idea how to look this up and/or change it on Mac.

## moneromooo-monero | 2020-05-14T23:11:10+00:00
"ipcs -l" might show current limits if you have that.

## alexstaj | 2020-05-14T23:15:18+00:00
thanks for your hard work.  it appears that the issue was that I hadn't restarted my computer since installing monero.

after a simple restart everything is now working and I am able to run my own local node!!

thanks again for all your help!

# Action History
- Created by: alexstaj | 2020-05-13T22:59:08+00:00
- Closed at: 2020-05-14T23:15:18+00:00
