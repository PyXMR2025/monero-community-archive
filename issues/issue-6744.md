---
title: '[P2P8]  ERROR   default src/common/threadpool.cpp:118   wait should have been
  called before waiter dtor - waiting now'
source_url: https://github.com/monero-project/monero/issues/6744
author: lordSquigles
assignees: []
labels: []
created_at: '2020-08-05T14:16:49+00:00'
updated_at: '2020-10-15T22:39:07+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:39:07+00:00'
---

# Original Description
Every time, just before finishing syncing, I get this error, "[P2P8]  ERROR   default src/common/threadpool.cpp:118   wait should have been called before waiter dtor - waiting now." I have built and rebuilt the source, downloaded the build from the getmonero page and am yet to not get this error, which is preventing me from syncing.

Here is a Reddit thread where somebody experienced the same issue: https://www.reddit.com/r/monerosupport/comments/hm0sck/error_cli_01601_nitrogen_nebula_released/.

I am on Ubuntu 18.04.4, using monero 0.16 and am very stuck. Any help would be appreciated! Thanks.

# Discussion History
## moneromooo-monero | 2020-08-05T15:40:02+00:00
Can you detail the circumstances for how to get this ?

## lordSquigles | 2020-08-05T16:21:43+00:00
Sure. I am running monerod as a systemd service with torsocks. However, I don't think the issue is with torsocks, as I got the same error before using it. I've attached the monerod.service file, monerod.config file, and monerod.log file (pasted into text documents).



[monerod.config.txt](https://github.com/monero-project/monero/files/5029616/monerod.config.txt)

[monerod.service.txt](https://github.com/monero-project/monero/files/5029717/monerod.service.txt)

[monerod.log.txt](https://github.com/monero-project/monero/files/5029612/monerod.log.txt)



I am running Ubuntu (bionic beaver 18.04.4) on a VMware virtual machine and using the latest release of monero (nitrogen nebula 0.16). 

## lordSquigles | 2020-08-07T16:29:36+00:00
Any luck finding immediate issues? If there's any more information that you need, feel free to ask

## moneromooo-monero | 2020-08-08T10:08:03+00:00
I've not looked at it yet, sorry.

## moneromooo-monero | 2020-08-08T12:02:29+00:00
Can you try again, and once it's stuck:

gdb /path/to/monerod \`pidof monerod\`   (replace the path with the actual path)
thread apply all bt

And post the multi-page results.


## lordSquigles | 2020-08-08T22:24:54+00:00
Will do. Not at my computer at the moment. I will post the output later. Thanks

## lordSquigles | 2020-08-09T20:19:34+00:00
Here you go:

[gdb.txt](https://github.com/monero-project/monero/files/5048343/gdb.txt)


## moneromooo-monero | 2020-08-09T20:47:47+00:00
Do you see any exception in the log file thrown shortly before this ?

## lordSquigles | 2020-08-09T21:34:05+00:00
No. Log is the same as the one I sent you. Would you like me to log with a higher verbosity?

## moneromooo-monero | 2020-08-09T21:34:30+00:00
No, it would appear at default.

## lordSquigles | 2020-08-10T15:18:08+00:00
Log looks just like the one I posted earlier

## moneromooo-monero | 2020-08-10T17:59:48+00:00
I might have found it. Does the following patch fix it ?

```
diff --git a/src/ringct/rctSigs.cpp b/src/ringct/rctSigs.cpp
index 2e3e7007e..7a2bb39da 100644
--- a/src/ringct/rctSigs.cpp
+++ b/src/ringct/rctSigs.cpp
@@ -1056,6 +1056,7 @@ namespace rct {
         }
         if (!proofs.empty() && !verBulletproof(proofs))
         {
+          waiter.wait(&tpool);
           LOG_PRINT_L1("Aggregate range proof verified failed");
           return false;
         }
```

## lordSquigles | 2020-08-10T22:12:14+00:00
Sorry, I accidentally deleted the blockchain file. I will tell you if this worked when it is done syncing (or I get the same error). Thanks

## lordSquigles | 2020-08-11T16:54:19+00:00
I added the line of code, rebuilt everything, and unfortunately got the same error. Would you like me to sync from the start with the new code? Is there anything else I can do to help?

## moneromooo-monero | 2020-08-11T17:03:03+00:00
Don't sync from start, please try to keep the state as unchanged as you can. I guess I'm going to make a patch that logs everything about the threadpool and hope it'll shed some light on the bug.

## lordSquigles | 2020-08-11T17:29:22+00:00
Sounds good. 

## moneromooo-monero | 2020-08-11T17:53:36+00:00
https://paste.debian.net/hidden/aff321af/

This will spam stdout, hopefully it locks up fast for you.


## lordSquigles | 2020-08-11T20:53:24+00:00
Alright, I rebuilt with all the patches, and sent stdout to the file below:

[stdout.txt](https://github.com/monero-project/monero/files/5059416/stdout.txt)


## moneromooo-monero | 2020-08-11T21:03:51+00:00
Can you get me the same, but from the log file ? It's got extra thread info.

## lordSquigles | 2020-08-11T21:57:33+00:00
Sure. Here is the log file:

[monerod.log](https://github.com/monero-project/monero/files/5059648/monerod.log)


## moneromooo-monero | 2020-08-11T23:10:10+00:00
Please apply this patch on top of what you have already applied:

```
diff --git a/src/common/threadpool.cpp b/src/common/threadpool.cpp
index a1737778c..f1cf50ddf 100644
--- a/src/common/threadpool.cpp
+++ b/src/common/threadpool.cpp
@@ -166,7 +179,8 @@ void threadpool::run(bool flush) {
     lock.unlock();
     ++depth;
     is_leaf = e.leaf;
-    e.f();
+    try { e.f(); }
+    catch (const std::exception &e) { try { MERROR("Exception in threadpool job: " << e.what()); } catch (...) {} }
     --depth;
     is_leaf = false;
 
```

Then run again, and post the log file again.

## lordSquigles | 2020-08-12T00:59:41+00:00
Here you go:

[monero3.txt](https://github.com/monero-project/monero/files/5060099/monero3.txt)


## moneromooo-monero | 2020-08-12T01:32:34+00:00
Did it fix it ?

## lordSquigles | 2020-08-12T03:19:50+00:00
The error went away! But, now I have this one: "E Exception in threadpool job: mprotect failed."

## moneromooo-monero | 2020-08-12T11:17:00+00:00
Are you sure it's still breaking, and you waited a bit to see if it'd continue ?

## moneromooo-monero | 2020-08-12T11:28:41+00:00
Ah, I see. Try running with: MONERO_RANDOMX_UMASK=16

## lordSquigles | 2020-08-12T12:53:43+00:00
I added the, "--MONERO_RANDOMX_UMASK=16," flag. But, unfortunately still got the same error (mprotect failed). I will give it some time to see if its hanging there. Is there is any more detailed information you would like? 

## moneromooo-monero | 2020-08-12T13:02:58+00:00
It's an enviroment variable. Run like this;
MONERO_RANDOMX_UMASK=16 ./monerod --whatever

## lordSquigles | 2020-08-12T16:13:28+00:00
Silly me! I built another source, passing,"MONERO_RANDOMX_UMASK=16," as an environment variable, and with just the first and last patches (not the ones for more detailed stdout), so that I could get more focused logging. I seem to still get the, "E Exception in threadpool job: mprotect failed," error. Here is my log:

[monero4.txt](https://github.com/monero-project/monero/files/5064063/monero4.txt)

I noticed this exception:

2020-08-12 15:58:57.943	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error

Any idea of what might be causing this? Thanks a lot for your patience and the fantastic help.

## moneromooo-monero | 2020-08-12T17:02:33+00:00
What is your exact command line ?

## lordSquigles | 2020-08-12T18:46:57+00:00
I am running it as a systemd service:

[monerod.service1.txt](https://github.com/monero-project/monero/files/5064997/monerod.service1.txt)


## lordSquigles | 2020-08-12T19:19:37+00:00
Just realized it was the, "MemoryDenyWriteExecute=true," line in my systemd service file. Not an issue with monero. Apologies. Thanks alot for your amazing help. After applying the two patches, it syncs fine. Will these patches be implemented in a future version of monero, or is this issue uniquely mine?

## moneromooo-monero | 2020-08-12T20:24:06+00:00
They will be, though they would not fix the systemd stuff by themselves, they're still good to have.

## lordSquigles | 2020-08-12T21:44:36+00:00
Great. Again, thanks for the help. Really appreciated

## moneromooo-monero | 2020-08-12T23:44:12+00:00
https://github.com/monero-project/monero/pull/6757

# Action History
- Created by: lordSquigles | 2020-08-05T14:16:49+00:00
- Closed at: 2020-10-15T22:39:07+00:00
