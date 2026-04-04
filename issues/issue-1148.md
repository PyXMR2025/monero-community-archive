---
title: 'Unable to sync daemon: ARMv7 release binaries v0.10.0.0, Raspberry Pi 3 Rasbian'
source_url: https://github.com/monero-project/monero/issues/1148
author: bigreddmachine
assignees: []
labels: []
created_at: '2016-09-29T05:00:44+00:00'
updated_at: '2017-09-21T01:19:04+00:00'
type: issue
status: closed
closed_at: '2017-09-21T01:19:04+00:00'
---

# Original Description
I've been trying to set up a node on my Raspberry Pi 3 and have had no luck whatsoever.

Previously I had tried both building from source and using the pre-compiled binaries on Ubuntu MATE 16.04. I got it to compile, but after starting it just got stuck.

Today I decided to try using the binaries on Rasbian (Debian Jessie) and again could not get anywhere. 

I do not appear to be the only one having trouble... see this thread on /r/monero:
https://www.reddit.com/r/Monero/comments/54vlwa/monero_node_on_raspberry_pi2/

My log files in `~/.bitmonero/` were useless, but in the terminal I did see one thing of note. Here is the full copied text from the terminal from the time I started `monerod` (note that the binaries are in my PATH, hence why there's no `./` at the beginning of `monerod`.

Notice the `Segmentation fault` at the end.

```
pi@raspberrypi:~ $ monerod 
Creating the logger system
2016-Sep-28 22:43:15.745543 Initializing cryptonote protocol...
2016-Sep-28 22:43:15.745657 Cryptonote protocol initialized OK
2016-Sep-28 22:43:15.746092 Initializing p2p server...
2016-Sep-28 22:43:16.144966 Set limit-up to 2048 kB/s
2016-Sep-28 22:43:16.145281 Set limit-down to 8192 kB/s
2016-Sep-28 22:43:16.145430 Set limit-up to 2048 kB/s
2016-Sep-28 22:43:16.145650 Set limit-down to 8192 kB/s
2016-Sep-28 22:43:16.145987 Binding on 0.0.0.0:18080
2016-Sep-28 22:43:16.146299 Net service bound to 0.0.0.0:18080
2016-Sep-28 22:43:16.146364 Attempting to add IGD port mapping.
2016-Sep-28 22:43:17.175805 IGD was found but reported as not connected.
2016-Sep-28 22:43:17.176079 P2p server initialized OK
2016-Sep-28 22:43:17.176678 Initializing core rpc server...
2016-Sep-28 22:43:17.177131 Binding on 127.0.0.1:18081
2016-Sep-28 22:43:17.177700 Core rpc server initialized OK on port: 18081
2016-Sep-28 22:43:17.177863 Initializing core...
2016-Sep-28 22:43:17.179025 Loading blockchain from folder /home/pi/.bitmonero/lmdb ...
2016-Sep-28 22:43:17.179189 option: fast
2016-Sep-28 22:43:17.179311 option: async
2016-Sep-28 22:43:17.179431 option: 1000
2016-Sep-28 22:43:17.181201 Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2016-Sep-28 22:43:17.181735 The DB has no hard fork info, reparsing from start
2016-Sep-28 22:43:17.182057 Blockchain not loaded, generating genesis block.
2016-Sep-28 22:43:17.935189 Loading precomputed blocks: 1138751
2016-Sep-28 22:43:18.272357 Blockchain initialized. last block: 0, d1547.h23.m43.s17 time ago, current difficulty: 1
2016-Sep-28 22:43:19.169535 Core initialized OK
2016-Sep-28 22:43:19.169678 Starting core rpc server...
2016-Sep-28 22:43:19.169786 Run net_service loop( 2 threads)...
2016-Sep-28 22:43:19.170233 [SRV_MAIN]Core rpc server started ok
2016-Sep-28 22:43:19.170641 [SRV_MAIN]Starting p2p net loop...
2016-Sep-28 22:43:19.170809 [SRV_MAIN]Run net_service loop( 10 threads)...
2016-Sep-28 22:43:20.171505 [P2P1]
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level>" command*, where <level> is between 0 (no details) and 4 (very verbose).

Use "help" command to see the list of available commands.

Note: in case you need to interrupt the process, use "exit" command. Otherwise, the current progress won't be saved.
**********************************************************************
2016-Sep-28 22:43:21.155136 [P2P7][52.51.14.14:18080 OUT]Sync data returned unknown top block: 1 -> 1146254 [1146253 blocks (890 days) behind] 
SYNCHRONIZATION started
2016-Sep-28 22:43:21.317105 [P2P2]ERROR /DISTRIBUTION-BUILD/src/cryptonote_core/blockchain.cpp:1835 Ours and foreign blockchain have only genesis block in common... o.O
2016-Sep-28 22:43:21.589817 [P2P4][24.91.0.62:18080 OUT]Sync data returned unknown top block: 1 -> 1146254 [1146253 blocks (890 days) behind] 
SYNCHRONIZATION started
2016-Sep-28 22:43:21.672807 [P2P7]ERROR /DISTRIBUTION-BUILD/src/cryptonote_core/blockchain.cpp:1835 Ours and foreign blockchain have only genesis block in common... o.O
Segmentation fault

```


# Discussion History
## ghost | 2016-09-29T12:08:09+00:00
So the RPi 2 and 3 use different ARM processors, and the person on Reddit was saving the blockchain to the same small SD card that they were running the OS from. So I'm not sure these are the same issue.

RPi2 uses a 32-bit ARMv7  (Broadcom BCM2836, Cortex-A7)
RPi3 uses a 64-bit ARMv8 (Broadcom BCM2837, Cortex-A53)

Can I ask - did you compile from source or use the binaries? Can I recommend you try compiling from source, I put in some tests for various bits of ARMv7 and 8 functionality which may have been skipped by the static build from a different system.


## moneromooo-monero | 2016-09-29T13:47:08+00:00
Do you have a stack trace ?

Also, set_log 1 will me the log more useful.


## bigreddmachine | 2016-09-29T21:49:41+00:00
I deleted old logs and `~/.bitmonero` and tried syncing again fresh with --log-level 1

Here are logs: http://pastebin.com/hubVEvYR

How can I get a stack trace?


## bigreddmachine | 2016-09-29T21:53:05+00:00
@moneromooo-monero - sorry, I meant to ping you above.

---

@NanoAkron - RPi3 3 uses 32-bit mode and acts like ARMv7. There's no 64-bit kernel for it.

As I stated, I've tried both building from source and using the binaries. Here I used the binaries because 1) I wanted to try the new Raspbian release and Raspbian ships with Boost 1.55 not 1.58 afaik, and 2) when I tried both ways with Ubuntu MATE I got the same result.


## moneromooo-monero | 2016-09-30T20:01:41+00:00
Can you put logs on fpaste.org, please ? pastebin blocks Tor.

For a stack trace:
- ulimit -c unlimited
- run monerod, and make it crash
- gdb monerod core      # add path to monerod if not in ., and core might be named core.12345, put the right name there
- thread apply all bt

And copy the output of that last command to fpaste.org.


## moneromooo-monero | 2016-09-30T20:02:17+00:00
And running with --log-level 2 will help the log be more useful if you're going to re-run.


## bigreddmachine | 2016-10-02T19:19:08+00:00
Previosu logs here: https://paste.fedoraproject.org/441909/43591814/

---

Tried to re-sync from scratch with --log-level 2.

Logs here: https://paste.fedoraproject.org/441902/54358571/

---

Stack trace:

```
(gdb) thread apply all bt

Thread 18 (Thread 0x6baf6460 (LWP 1047)):
#0  0x76e42780 in __lll_lock_wait (futex=futex@entry=0x2b04c18, 
    private=<optimized out>)
    at ../ports/sysdeps/unix/sysv/linux/arm/nptl/lowlevellock.c:46
#1  0x76e3d3c4 in __GI___pthread_mutex_lock (mutex=0x2b04c18)
    at pthread_mutex_lock.c:114
#2  0x001f4a92 in cryptonote::Blockchain::have_block(crypto::hash const&) const
    ()
#3  0x00230438 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_chain_entry(int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&) ()
#4  0x00333ea6 in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.448] ()
#5  0x001c1d02 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()(gdb) thread apply all bt

Thread 18 (Thread 0x6baf6460 (LWP 1047)):
#0  0x76e42780 in __lll_lock_wait (futex=futex@entry=0x2b04c18, 
    private=<optimized out>)
    at ../ports/sysdeps/unix/sysv/linux/arm/nptl/lowlevellock.c:46
#1  0x76e3d3c4 in __GI___pthread_mutex_lock (mutex=0x2b04c18)
    at pthread_mutex_lock.c:114
#2  0x001f4a92 in cryptonote::Blockchain::have_block(crypto::hash const&) const
    ()
#3  0x00230438 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_chain_entry(int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&) ()
#4  0x00333ea6 in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.448] ()
#5  0x001c1d02 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
```


## radfish | 2016-10-04T05:31:54+00:00
Did you try with `--max-concurrency=1` argument on the command line?


## ghost | 2016-10-04T15:54:20+00:00
Can we set max-concurrency=1 to be the default unless overridden?


## moneromooo-monero | 2016-10-15T18:32:55+00:00
There should be pages of stack after that. The couple threads shown here aren't crashed, they're just waiting for the lock to be released so they can get to work.


## bigreddmachine | 2016-10-16T17:54:55+00:00
@radfish and @NanoAkron - I tried adding `--max-concurrency 1` and nothing different.

@moneromooo-monero - To be fair, my original issue never mentioned anything about a crash... I said it gets stuck. As in for hours and hours. Although the last few times it has a segmentation fault and terminates, so that could be considered a crash I suppose.

---

Is it possible the arm7 monerod build just doesn't work? This is an open question to any contributors, not just those in the discussion so far:

Has anyone successfully used monerod v0.10 on an arm7 device such as a Raspberry Pi 2 or 3, either by compiling from source or using the official binaries?


## ghost | 2016-10-17T21:27:23+00:00
I'm afraid I haven't. I got a Pi2 but soon switched to an Odroid C2 and am eyeing up the Pine 64.


## ghost | 2016-10-23T18:26:03+00:00
Hi @bigreddmachine, there have been a couple of changes since you posted your issue. Have any of these fixed things for you?


## bigreddmachine | 2016-10-28T21:22:16+00:00
@NanoAkron, the changes don't effect the release binaries, and afaik I can't compile on Raspbian because of the version of boost that's available (v1.55 I believe).

When I get a chance, I will try to set up a spare SD card with Ubuntu Mate and compile from head. Or, if you have the patience to walk me through what I might need to do, I could cross compile it on my ubuntu desktop and move it over.


## ghost | 2016-11-10T00:10:34+00:00
Hi @bigreddmachine I recently changed the README to include the recipe I used to build successfully on the RPi 2 - try it out and let us know here if it's worked


## radfish | 2016-11-18T23:12:07+00:00
@bigreddmachine You can create a chroot in your existing system with a more recent distribution with a more recent boost libs (like a more recent Ubuntu or Arch), build a static binary in the chroot, then copy the binary out of the chroot to the original system.


## moneromooo-monero | 2017-09-20T21:13:58+00:00
Is it better now ? 0.10.3.1 had busted cryptonight on armv7, which would cause a failure to sync.

## bigreddmachine | 2017-09-21T01:19:04+00:00
Can confirm, this now works out of the box on the Raspberry Pi, armv6 or armv7, both building on your own or grabbing the armv7 binaries.

Building on the Pi is also way easier now thanks to Raspbian upgrading from Jessie to Stretch. See #2502.

# Action History
- Created by: bigreddmachine | 2016-09-29T05:00:44+00:00
- Closed at: 2017-09-21T01:19:04+00:00
