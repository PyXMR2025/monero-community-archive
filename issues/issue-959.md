---
title: Deamon Failed to Start
source_url: https://github.com/monero-project/monero-gui/issues/959
author: lh1008
assignees: []
labels: []
created_at: '2017-11-16T03:30:42+00:00'
updated_at: '2018-04-26T07:11:40+00:00'
type: issue
status: closed
closed_at: '2017-11-18T09:53:33+00:00'
---

# Original Description
Hi guys, 

I´m receiving this message. 
The monerod.exe starts, shows:
2017-11-16 02:47:39.250	2352	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.0.0-release)
2017-11-16 02:47:39.251	2352	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-11-16 02:47:39.251	2352	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-11-16 02:47:39.252	2352	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...

Then closes, with no reason.

From the wallet gui:
Deamons Failed to Start
Please check your wallet and daemon log for errors. You can also try to start monerod.exe manually.
![cap](https://user-images.githubusercontent.com/7443480/32871476-3186befe-ca4f-11e7-9492-cc24f3230ee8.PNG)

I had never experience any trouble with the deamon. Always used the monerod.exe(double click) and done. I have been using the deamon since December 2016 with no failure. This is the first time I´m experiencing any trouble. After no response of the deamon today was my first time opening the GUI first but recieved the error message. 

- I´m running Windows 7 Home Premium 64-bit
- Installed directly from [https://github.com/monero-project/monero-core/releases/tag/v0.11.1.0](url) Windows, 64-bit Current Version: 0.11.1.0 Helium Hydra. Always made the upgrades since december with no trouble. 
- `C:\ProgramData\bitmonero` Has this files:
`.daemon_lock`
`bitmonero.log`
`p2pstate.bin`
`p2pstate.bin.unportable`
`poolstate.bin`
`poolstate.bin.unportable`
- Localhost 18081
- data.mdb 33gb
- I´ve changed the deamon folder several times but never had any issues. Never changed any file name.
- It does not connect, just opens, first lines....connecting and then closes.
- Last connected, from `bitmonero.log`
2017-11-12 18:55:19.516	[P2P0]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521	[1;32mSYNCHRONIZED OK[0m
2017-11-12 19:20:30.942	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521	[1;32mSYNCHRONIZED OK[0m
2017-11-12 19:30:08.012	4588	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Stop signal sent
2017-11-12 19:30:08.013	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2017-11-12 19:30:08.121	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:78	Stopping core rpc server...
2017-11-12 19:30:08.121	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:145	Node stopped.
2017-11-12 19:30:08.121	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-11-12 19:30:08.121	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-11-12 19:30:08.669	[SRV_MAIN]	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-11-12 19:30:08.841	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-11-12 19:30:08.841	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully

- I don´t have any program knowledge. Made some windows "fixes" this weekend from [https://decentsecurity.com/holiday-tasks/](url), got to the point 13. Since then I didn´t use the deamon. Yesterday opened the deamon but didn´t notice it didn´t start, I was studying git. Today tried to open the deamon to send some funds but...Deamon Failed to Start.
- Rebooted several times but no start from deamon, it just won´t start. Same message again and again.  

Last 100 lines from `bitmonero.log` [https://paste.fedoraproject.org](url)
[https://paste.fedoraproject.org/paste/H7IO3tp0ZDJeXdUMN7Hx4g](url)

Got through issue [https://github.com/monero-project/monero-core/issues/890](url) to get forward in some instructions. Stopped in the last 100 lines from `bitmonero.log`, because I noticed my failure was different. 

I work all day so if I don´t give any answer please bear with me until I get home. Thanks! :)





# Discussion History
## medusadigital | 2017-11-16T13:53:06+00:00
please move your bitmonero.log away somehwere and try to start monerod.exe manually.

If it also fails to start, plase post full bitmonero.log (from start until it crashes)

## dEBRUYNE-1 | 2017-11-16T14:20:50+00:00
To clarify:

>It does not connect, just opens, first lines....connecting and then closes.

This happens when you open monerod.exe, i.e., just double clicking on monerod.exe?

-------------

In addition, did your system shut down unexpectedly when monerod.exe was running? 

## lh1008 | 2017-11-16T14:39:56+00:00
@dEBRUYNE-1 

> This happens when you open monerod.exe, i.e., just double clicking on monerod.exe?

Yes

> In addition, did your system shut down unexpectedly when monerod.exe was running?

Not that I have knowledge. Never had that experience. When I made some ["fixes"](https://decentsecurity.com/holiday-tasks/)(from decentsecurity.com; got till point 13) on windows this weekend, I never launched the monerod.exe.

## lh1008 | 2017-11-17T02:29:44+00:00
@medusadigital 

Removed the bitmonero.log and its ok. Didn´t crash.

![deamon](https://user-images.githubusercontent.com/7443480/32926313-9e609502-cb14-11e7-92f6-81711b092935.PNG)

Do I delete the old bitmonero.log?

I´m really grateful. Thank you. 



## lh1008 | 2017-11-18T09:53:33+00:00
Deamon is working as always, already used it to send funds.

Thanks guys 


## Chikwasman | 2018-04-21T10:54:25+00:00
This might sound cheap but gotta ask it, where can i locate the bitmoreno.log path on computer? its running on window 7 ultimate

## Diin3Alagaa | 2018-04-26T07:11:40+00:00
@Chikwasman its located in C:\ProgramData\bitmonero , Programdata folder is hidden so u have to manually open the folder

# Action History
- Created by: lh1008 | 2017-11-16T03:30:42+00:00
- Closed at: 2017-11-18T09:53:33+00:00
