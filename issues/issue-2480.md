---
title: Unable to start daemon
source_url: https://github.com/monero-project/monero/issues/2480
author: MattTwinkleToes
assignees: []
labels: []
created_at: '2017-09-19T15:13:15+00:00'
updated_at: '2018-05-08T06:31:22+00:00'
type: issue
status: closed
closed_at: '2017-09-22T09:54:25+00:00'
---

# Original Description
I am unable to start the daemon.

If i /opt/monero-gui-0.11.0.0 $ ./start-gui.sh, The gui opens and I am prompted for a password to unlock the wallet.

This succeeds but then the daemon fails to start.  Naturally, I am then unable to access my funds.

Is should add that I have successfully synchonised this wallet (took 10 hours) and been able to deposit some coins only once.  After wallet was closed and re-opened, this problem started.

```
./monerod 
2017-09-18 23:08:31.458	    7f7256275740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.0.0-release)
2017-09-18 23:08:31.458	    7f7256275740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-09-18 23:08:31.458	    7f7256275740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-09-18 23:08:31.458	    7f7256275740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
[1505776111] libunbound[2528:0] info: warning: unsupported algorithm for trust anchor . DS IN
[1505776111] libunbound[2528:0] warning: trust anchor . has no supported algorithms, the anchor is ignored (check if you need to upgrade unbound and openssl)
2017-09-18 23:08:33.208	    7f7256275740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-09-18 23:08:33.208	    7f7256275740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-09-18 23:08:33.208	    7f7256275740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-09-18 23:08:33.209	    7f7256275740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-09-18 23:08:33.209	    7f7256275740	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-09-18 23:08:33.210	    7f7256275740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /home/matt/.bitmonero/lmdb ...
2017-09-18 23:08:33.406	    7f7256275740	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:102	Failed to parse transaction from blob
2017-09-18 23:08:33.406	    7f7256275740	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1020	Failed to parse tx from txpool
2017-09-18 23:08:33.406	    7f7256275740	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:409	Failed to initialize memory pool
2017-09-18 23:08:33.406	    7f7256275740	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-09-18 23:08:33.406	    7f7256275740	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-09-18 23:08:33.406	    7f7256275740	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-09-18 23:08:33.416	    7f7256275740	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-09-18 23:08:33.416	    7f7256275740	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
 @moneromooo-monero
Contributor

```
It seems likely that the issue is this `"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"`

Why is there a \n at the end of the address?  Is it really trying to connect to that exact address?

```
"starting monerod /opt/monero-gui-0.11.0.0/monerod"
With command line arguments  ("--detach", "--check-updates", "disabled")
2017-09-19 15:09:26.197	    7f5d150de740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.0.0-release)
Forking to background...
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
```
Linux mint 18.2 x64
4.10.0-33 generic
monero-gui-0.11.0.0 64bit .deb

# Discussion History
## moneromooo-monero | 2017-09-19T16:08:11+00:00
<s>Should be fixed by https://github.com/monero-project/monero/pull/2481</s>  er, no I'm wrong here.

As the for \n, that's probably what's in the settings. Sounds like pasting something with had a \n in it.

## MattTwinkleToes | 2017-09-19T16:14:51+00:00
Thanks, the port settings were default but have since been removed to see if that helps but not change.

when #2481 is ready, what do i do?   will there be a new binary?

## moneromooo-monero | 2017-09-19T16:23:57+00:00
Can you paste on fpaste.org or pastebin.mozilla.org the results of these two commands, please:

./mdb_dump -s txpool_meta ~/.bitmonero/lmdb
./mdb_dump -s txpool_blob ~/.bitmonero/lmdb


## MattTwinkleToes | 2017-09-19T16:37:03+00:00
Sure, I had to install lmdb-utils first.

meta - https://paste.fedoraproject.org/paste/2seui6pbnX8BBlcUhl6hdQ

blob - https://paste.fedoraproject.org/paste/l~vulhdXK5TUdCMh2wHUIw

## moneromooo-monero | 2017-09-19T17:53:34+00:00
One of the txes is indeed corrupt looking. You'll have to drop the txpool in order to get back in working order:

mdb_drop -s txpool_meta ~/.bitmonero/lmdb
mdb_drop -s txpool_blob ~/.bitmonero/lmdb

mdb_drop source can be found at http://highlandsun.com/hyc/mdb_drop.c

Not sure why anything bad got written in the first place though. I'll continue looking.

## MattTwinkleToes | 2017-09-19T20:52:24+00:00
Hi moneroomoo-monero, can you elaborate a bit on this for me?  How do I drop the txpool?

Sorry but I am a bit of a noob with this.

## moneromooo-monero | 2017-09-20T08:48:22+00:00
By running the two commands in my previous comment. This drops the txpool. I'll probably add a --drop-txpool switch to monerod soon.

## MattTwinkleToes | 2017-09-20T08:49:48+00:00
Ok I ran them for yesterday and it still does not start.  Same error.

On 20 Sep 2017 10:48 am, "moneromooo-monero" <notifications@github.com>
wrote:

> By running the two commands in my previous comment. This drops the txpool.
> I'll probably add a --drop-txpool switch to monerod soon.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2480#issuecomment-330787551>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AUSpFqxYyVsZwxdZ_nIq_u56_SFc33xoks5skNFegaJpZM4Pcjv5>
> .
>


## moneromooo-monero | 2017-09-20T08:58:09+00:00
If you run them, then run the mdb_dump commands again, do the mdb_dump outputs come out empty (save for the headers/footers) ?

## MattTwinkleToes | 2017-09-20T13:23:51+00:00
My bad, i didnt notice the difference in the command you posted :)

I´ll figure out how to get mdb_dump working on mint 18.2 today (i hope)

On 20 September 2017 at 10:58, moneromooo-monero <notifications@github.com>
wrote:

> If you run them, then run the mdb_dump commands again, do the mdb_dump
> outputs come out empty (save for the headers/footers) ?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2480#issuecomment-330790072>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AUSpFqWvesZRbMhZd1pvLQR0O76ILddyks5skNOpgaJpZM4Pcjv5>
> .
>


## MattTwinkleToes | 2017-09-20T13:48:51+00:00
It wont compile for me and since iḿ not a developer, I dont really know why

gcc -o mdb_dump mdb_drop.c
/tmp/cch8RaqA.o: In function `main':
mdb_drop.c:(.text+0x196): undefined reference to `mdb_env_create'
mdb_drop.c:(.text+0x1a9): undefined reference to `mdb_strerror'
mdb_drop.c:(.text+0x1e3): undefined reference to `mdb_env_set_maxdbs'
mdb_drop.c:(.text+0x1fb): undefined reference to `mdb_env_open'
mdb_drop.c:(.text+0x20e): undefined reference to `mdb_strerror'
mdb_drop.c:(.text+0x24f): undefined reference to `mdb_txn_begin'
mdb_drop.c:(.text+0x262): undefined reference to `mdb_strerror'
mdb_drop.c:(.text+0x2a2): undefined reference to `mdb_dbi_open'
mdb_drop.c:(.text+0x2b5): undefined reference to `mdb_strerror'
mdb_drop.c:(.text+0x2ed): undefined reference to `mdb_drop'
mdb_drop.c:(.text+0x300): undefined reference to `mdb_strerror'
mdb_drop.c:(.text+0x32d): undefined reference to `mdb_txn_commit'
mdb_drop.c:(.text+0x340): undefined reference to `mdb_strerror'
mdb_drop.c:(.text+0x37e): undefined reference to `mdb_txn_abort'
mdb_drop.c:(.text+0x38a): undefined reference to `mdb_env_close'
collect2: error: ld returned 1 exit status
matt@otb3 ~/Desktop $ mdb_
mdb_copy  mdb_dump  mdb_load  mdb_stat

Is there another way to get this wallet up and running again so that I can
get my funds out of it?

I have the exact same issue on another linux mint machine that i tried to
recover the wallet on with seeds.

On 20 September 2017 at 15:23, Matt Fletcher <mat.fletcher@gmail.com> wrote:

> My bad, i didnt notice the difference in the command you posted :)
>
> I´ll figure out how to get mdb_dump working on mint 18.2 today (i hope)
>
> On 20 September 2017 at 10:58, moneromooo-monero <notifications@github.com
> > wrote:
>
>> If you run them, then run the mdb_dump commands again, do the mdb_dump
>> outputs come out empty (save for the headers/footers) ?
>>
>> —
>> You are receiving this because you authored the thread.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/monero-project/monero/issues/2480#issuecomment-330790072>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AUSpFqWvesZRbMhZd1pvLQR0O76ILddyks5skNOpgaJpZM4Pcjv5>
>> .
>>
>
>


## moneromooo-monero | 2017-09-20T13:51:41+00:00
Sorry: add /path/to/liblmdb.a -lpthread
ie: gcc mdb_drop.c /path/to/liblmdb.a -lpthread

And if you just want to use the wallet right now, add: --daemon-address node.moneroworld.com:18089

## MattTwinkleToes | 2017-09-20T13:56:15+00:00
where should i add it?

On 20 September 2017 at 15:51, moneromooo-monero <notifications@github.com>
wrote:

> Sorry: add /path/to/liblmdb.a -lpthread
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2480#issuecomment-330857986>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AUSpFtbOl1IHor2_c9gmpB92ffwE7-kRks5skRh6gaJpZM4Pcjv5>
> .
>


## moneromooo-monero | 2017-09-20T14:46:13+00:00
On the monero-wallet-cli command line.
And if you're using the GUI instead, you put node.moneroworld.com and 18089 in the settings page under the appropriate text widgets.

## moneromooo-monero | 2017-09-20T17:57:19+00:00
https://github.com/monero-project/monero/pull/2496 auto drops those bad txes on startup.

## moneromooo-monero | 2017-09-20T19:21:25+00:00
The code for writing tx blobs is fairly simple, and I can't see a reason why it'd write corrupt data. Did you get a crash before this happened ?

## MattTwinkleToes | 2017-09-20T20:24:59+00:00
No crash, perhaps my laptop going to hibernate or sleep may have been a
precursor but Im not sure.

I have the same behavior on another linux mint 18.2 box that i tried to
recover the wallet on.  exact same problem errors there.

On 20 September 2017 at 21:21, moneromooo-monero <notifications@github.com>
wrote:

> The code for writing tx blobs is fairly simple, and I can't see a reason
> why it'd write corrupt data. Did you get a crash before this happened ?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2480#issuecomment-330954216>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AUSpFi03TIAQEzMN_MEsQt0B2FI2kpYHks5skWW6gaJpZM4Pcjv5>
> .
>


## MattTwinkleToes | 2017-09-20T20:28:45+00:00
I still have not got his working yet either.  I was doing it all form the
gui, now i need to familiarise myself with the cli version.

My wallet name is matt monero wallet but when i enter that in it says it
cant find it and tries to create a new wallet.

On 20 September 2017 at 22:24, Matt Fletcher <mat.fletcher@gmail.com> wrote:

> No crash, perhaps my laptop going to hibernate or sleep may have been a
> precursor but Im not sure.
>
> I have the same behavior on another linux mint 18.2 box that i tried to
> recover the wallet on.  exact same problem errors there.
>
> On 20 September 2017 at 21:21, moneromooo-monero <notifications@github.com
> > wrote:
>
>> The code for writing tx blobs is fairly simple, and I can't see a reason
>> why it'd write corrupt data. Did you get a crash before this happened ?
>>
>> —
>> You are receiving this because you authored the thread.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/monero-project/monero/issues/2480#issuecomment-330954216>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AUSpFi03TIAQEzMN_MEsQt0B2FI2kpYHks5skWW6gaJpZM4Pcjv5>
>> .
>>
>
>


## MattTwinkleToes | 2017-09-20T20:29:54+00:00
matt\ monero\ wallet/ does not work either

On 20 September 2017 at 22:28, Matt Fletcher <mat.fletcher@gmail.com> wrote:

> I still have not got his working yet either.  I was doing it all form the
> gui, now i need to familiarise myself with the cli version.
>
> My wallet name is matt monero wallet but when i enter that in it says it
> cant find it and tries to create a new wallet.
>
> On 20 September 2017 at 22:24, Matt Fletcher <mat.fletcher@gmail.com>
> wrote:
>
>> No crash, perhaps my laptop going to hibernate or sleep may have been a
>> precursor but Im not sure.
>>
>> I have the same behavior on another linux mint 18.2 box that i tried to
>> recover the wallet on.  exact same problem errors there.
>>
>> On 20 September 2017 at 21:21, moneromooo-monero <
>> notifications@github.com> wrote:
>>
>>> The code for writing tx blobs is fairly simple, and I can't see a reason
>>> why it'd write corrupt data. Did you get a crash before this happened ?
>>>
>>> —
>>> You are receiving this because you authored the thread.
>>> Reply to this email directly, view it on GitHub
>>> <https://github.com/monero-project/monero/issues/2480#issuecomment-330954216>,
>>> or mute the thread
>>> <https://github.com/notifications/unsubscribe-auth/AUSpFi03TIAQEzMN_MEsQt0B2FI2kpYHks5skWW6gaJpZM4Pcjv5>
>>> .
>>>
>>
>>
>


## MattTwinkleToes | 2017-09-20T20:34:11+00:00
OK i tried to open it with the keys file but then it looks for a file that
does not exist

/opt/monero-gui-0.11.0.0 $ ./monero-wallet-cli --wallet-file matt monero
wallet.keys
Monero 'Helium Hydra' (v0.11.0.0-release)
Logging to ./monero-wallet-cli.log
Wallet password: *******************
Error: failed to load wallet: file not found "matt.keys"

I´m really out of my depth here, any ideas??

On 20 September 2017 at 22:29, Matt Fletcher <mat.fletcher@gmail.com> wrote:

> matt\ monero\ wallet/ does not work either
>
> On 20 September 2017 at 22:28, Matt Fletcher <mat.fletcher@gmail.com>
> wrote:
>
>> I still have not got his working yet either.  I was doing it all form the
>> gui, now i need to familiarise myself with the cli version.
>>
>> My wallet name is matt monero wallet but when i enter that in it says it
>> cant find it and tries to create a new wallet.
>>
>> On 20 September 2017 at 22:24, Matt Fletcher <mat.fletcher@gmail.com>
>> wrote:
>>
>>> No crash, perhaps my laptop going to hibernate or sleep may have been a
>>> precursor but Im not sure.
>>>
>>> I have the same behavior on another linux mint 18.2 box that i tried to
>>> recover the wallet on.  exact same problem errors there.
>>>
>>> On 20 September 2017 at 21:21, moneromooo-monero <
>>> notifications@github.com> wrote:
>>>
>>>> The code for writing tx blobs is fairly simple, and I can't see a
>>>> reason why it'd write corrupt data. Did you get a crash before this
>>>> happened ?
>>>>
>>>> —
>>>> You are receiving this because you authored the thread.
>>>> Reply to this email directly, view it on GitHub
>>>> <https://github.com/monero-project/monero/issues/2480#issuecomment-330954216>,
>>>> or mute the thread
>>>> <https://github.com/notifications/unsubscribe-auth/AUSpFi03TIAQEzMN_MEsQt0B2FI2kpYHks5skWW6gaJpZM4Pcjv5>
>>>> .
>>>>
>>>
>>>
>>
>


## moneromooo-monero | 2017-09-20T20:56:57+00:00
./monero-wallet-cli --wallet-file "matt monero wallet"

Assuming it's in the current directory. If not, give the path too.

## MattTwinkleToes | 2017-09-20T20:58:32+00:00
There is no matt.keys file in the directory

~/Monero/wallets/matt monero wallet $ ls -l
total 36
-rw-rw-r-- 1 matt matt 189 Sep 19 22:54 matt monero wallet
-rw-rw-r-- 1 matt matt  95 Sep 18 13:34 matt monero wallet.address.txt
-rw-rw-r-- 1 matt matt 864 Sep 18 13:34 matt monero wallet.keys

matt@otb3 /opt/monero-gui-0.11.0.0 $ ./monero-wallet-cli --wallet-file /home/matt/Monero/wallets/matt monero wallet.keys
Monero 'Helium Hydra' (v0.11.0.0-release)
Logging to ./monero-wallet-cli.log
Wallet password: *******************
Error: failed to load wallet: file not found "/home/matt/Monero/wallets/matt.keys"


## MattTwinkleToes | 2017-09-20T21:01:36+00:00
if i install the windows version on a windows VM, will I be able to restore this wallet with my seed words?

I really just want to get my coins out of that thing and find another way to store them at this point, it´s all a bit stressful not being able to access the funding you know?  There is a not insignificant amount of money in there.

## moneromooo-monero | 2017-09-20T21:20:02+00:00
That's because you didn't quote as in my example. And I did not put the .keys suffix in. Don't.
Otherwise you can restore from seed on any machine, yes.

## MattTwinkleToes | 2017-09-20T21:26:01+00:00
OK i got it to open the wallet with ./monero-wallet-cli --wallet-file /home/matt/Monero/wallets/matt\ monero\ wallet/matt\ monero\ wallet.keys

Now to try and get this bit to work from your earlier comment -add /path/to/liblmdb.a -lpthread

I do appreciate your help with this i promise

## moneromooo-monero | 2017-09-20T21:58:04+00:00
If you apply https://github.com/monero-project/monero/pull/2496, you don't need to run mdb_drop, as the patch will detect and drop those invalid txes on startup. Of course it's unfortunate we don't know how these came to be there in the first place...

## MattTwinkleToes | 2017-09-21T17:47:48+00:00
How would I go about applying 2496?, I installed from a .deb.  Is 2496 committed and in the main source now and should I just compile it?  

## moneromooo-monero | 2017-09-21T18:22:31+00:00
It was committed today indeed. So something like:

git clone https://github.com/monero-project/monero monero-fixed
cd monero-fixed
make

If it moans about missing stuff, install it (the list is the README).


## MattTwinkleToes | 2017-09-21T18:39:40+00:00
OK thanks, I will do that tonight.

## moneromooo-monero | 2017-09-22T09:47:17+00:00
+resolved

## danindiana | 2018-03-06T16:57:36+00:00
> git clone https://github.com/monero-project/monero monero-fixed
cd monero-fixed
make> 
Had the same issue with Linux 64 monero as OP. Initially cmake wouldn't work w/o errors but installing the additional libraries worked for me. 
OS: Ubuntu 16.04 xenial
 Kernel: x86_64 Linux 4.13.0-36-generic
 Uptime: 9h 26m
 Packages: 2937
 Shell: bash 4.3.48
 Resolution: 2560x1080
 DE: Unity 7.4.5
 WM: Compiz
 WM Theme: Radiance
Radiance [GTK2]
, Radiance [GTK3]
 Icon Theme: ubuntu-mono-light
 Font: Ubuntu 11
 CPU: AMD Ryzen 5 1600X Six-Core @ 3.6GHz
 GPU: GeForce GTX 1050
 RAM: 6052MiB / 16034MiB



## stevesbrain | 2018-05-08T06:31:22+00:00
@moneromooo-monero Just a heads up, I had this same issue after rsync'ing the .bitmonero folder between two hosts (on the same subnet), and trying to start. I re-rsync'd and tried again - same issue. I was able to use the mdb_drop software you linked, and this resolved the issue for me. Puts me ~3 days behind on sync apparently, but no big deal :) Thanks!

# Action History
- Created by: MattTwinkleToes | 2017-09-19T15:13:15+00:00
- Closed at: 2017-09-22T09:54:25+00:00
