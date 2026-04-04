---
title: '[v13] Ledger wallet doesn’t open sometimes (libhidapi)'
source_url: https://github.com/monero-project/monero/issues/4534
author: selsta
assignees: []
labels: []
created_at: '2018-10-08T20:13:09+00:00'
updated_at: '2018-10-25T00:01:37+00:00'
type: issue
status: closed
closed_at: '2018-10-20T19:08:52+00:00'
---

# Original Description
This issue is quite minor, simply opening the wallet again fixes the issue. It has happened a couple of times now so I’ve created an issue to document it.

```
selsta@mbpR ~/d/m/b/D/l/r/bin> ./monero-wallet-cli --wallet-file ledger
2018-10-08 20:09:40,705 INFO  [default] Page size: 4096
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Beryllium Bullet' (v0.13.0.1-rc-ac567452)
Logging to ./monero-wallet-cli.log
Wallet password: 
Error: failed to load wallet: Wrong sequence_idx
```

/cc @cslashm 

# Discussion History
## cslashm | 2018-10-09T05:59:16+00:00
Minor  but Srange. I will try to have a look quickly at that.

Le lun. 8 oct. 2018 à 22:13, selsta <notifications@github.com> a écrit :

> This issue is is quite minor, simply opening the wallet again fixes the
> issue.
>
> selsta@mbpR ~/d/m/b/D/l/r/bin> ./monero-wallet-cli --wallet-file ledger
> 2018-10-08 20:09:40,705 INFO  [default] Page size: 4096
> This is the command line monero wallet. It needs to connect to a monero
> daemon to work correctly.
> WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.
>
> Monero 'Beryllium Bullet' (v0.13.0.1-rc-ac567452)
> Logging to ./monero-wallet-cli.log
> Wallet password:
> Error: failed to load wallet: Wrong sequence_idx
>
> /cc @cslashm <https://github.com/cslashm>
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/4534>, or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AFOX8y0Ua4K5KiWXBz5dPPBuDW-lfXv8ks5ui7HwgaJpZM4XNmX1>
> .
>


## Zarkoob | 2018-10-10T22:55:21+00:00
@selsta and @cslashm I can get the ledger working in v0.13.0.2-release however I noticed a strange quirk that's similar to the send issue: 

If you start the CLI wallet with the typical command and let it prompt you for your wallet password everything works fine. However if you start the wallet with a password file/arg in the command you will get an error sometimes as:
 `Error: failed to load wallet: Wrong sequence_idx`

It's only 50% of the time like the issue with sending. But at least this way you can jump into the wallet really fast and test if the issue is still here vs having to send something. 

It's almost as if we need another type of delay?



## apxs94 | 2018-10-14T11:19:23+00:00
+1 on this issue, same description as above

Right now it happened 3x in a row when trying to open the wallet file for Ledger. 4th attempt, without changing anything, the wallet opened.

Also on macOS.

## philkode | 2018-10-14T23:04:03+00:00
+1 except this is happening on a fresh CLI build of v0.13.0.2 on Windows too. Seems to be happening 100% of the time when trying to create new or access existing Ledger wallet (which worked fine on v0.12). Basically means Ledger isn't usable on Windows as of v0.13.0.2 (on my machine at least, subsequent posts indicate it is working for others but also that I am not alone with this issue).

## cslashm | 2018-10-15T09:05:33+00:00
I look at that today.

## cslashm | 2018-10-15T14:41:57+00:00
I'm not able to reproduce the probleme neither under win7 nor under linux

It would be useful if someone can make USB log with http://www.usblyzer.com. (filtering the long on the device  VID:PID == 2c97:0001) 


## usmarine2141 | 2018-10-15T17:23:47+00:00
I have same issue. Unable to open wallet on my ledger nano S

Win 10

Errors the wallet cli generates


2018-10-15 17:13:21.366	3156	INFO logging	contrib/epee/src/mlog.cpp:242	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-15 17:14:32.291	3580	INFO logging	contrib/epee/src/mlog.cpp:242	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO

## usmarine2141 | 2018-10-15T17:42:49+00:00
@cslashm 

Here is the USBLYZER capture

[ledger usblyzer.zip](https://github.com/monero-project/monero/files/2479894/ledger.usblyzer.zip)


## philkode | 2018-10-15T17:47:28+00:00
Here's another USBLYZER capture
[ledger.zip](https://github.com/monero-project/monero/files/2479917/ledger.zip)

## cslashm | 2018-10-16T06:49:36+00:00
@usmarine2141, @philkode  thanks. We saw somthing strange that we do not explain for now.

Is it possible for you to do the same log, but with log level4 on monero cli and provide me the both log ulz and monero. 

## iDunk5400 | 2018-10-16T09:11:35+00:00
> 
> 
> I have same issue. Unable to open wallet on my ledger nano S
> 
> Win 10
> 
> Errors the wallet cli generates
> 
> 2018-10-15 17:13:21.366 3156 INFO logging contrib/epee/src/mlog.cpp:242 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
> 2018-10-15 17:14:32.291 3580 INFO logging contrib/epee/src/mlog.cpp:242 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO

There are no errors there.
![screenshot_2018-10-16 v13 macos ledger wallet doesn t open sometimes libhidapi issue 4534 monero-project monero](https://user-images.githubusercontent.com/20195079/47006290-df063d00-d135-11e8-8e5b-14debbf99208.png)


## iDunk5400 | 2018-10-16T09:47:21+00:00
> Basically means Ledger isn't usable on Windows as of v0.13.0.2.

Works fine for me on Windows 10. Make sure you've installed the [required dependency](https://github.com/monero-project/monero/pull/4203) before building.

## DrCryptoKey | 2018-10-16T11:37:43+00:00
I'm on Windows 10 (Home v1809) using the new 0.13.0.3 GUI I get "Couldn't open wallet: wrong sequence_idx" when opening my Ledger Wallet, same error when doing it with the CLI 0.13.0.2. 
In the GUI, if I select to create a new wallet I get the error message "failed to generate new wallet: Wrong sequence_idx". The ledger worked fine with GUI 0.12.3.
Things I tried;
1) Unplugging and plugging it back.
2) Different USB cables and ports.
3) Removed the Monero app from the device and re-installing it.

Without the Ledger, just opening a local non-ledger wallet or creating a new one works fine.

With error level=4 I get the following in the log:
https://pastebin.com/23KkmGz9

## DrCryptoKey | 2018-10-16T12:19:57+00:00
Update: I just tried the Ledger (with the same USB cable) on a different computer (Windows 10 Pro 1809) and I was able to get past the option to create a new wallet without the error message appearing. So that means it's not a problem with the Ledger or the cable.

## cslashm | 2018-10-16T12:55:01+00:00
@DrCryptoKey thanks for the precision.

It confirm there is some random/race probleme under windows/mac during init. (making me crasy)
To investigate more I need both log level 4 from cli and usblyser log and from as many failing machine.

On failing machine, you can also test that: 
- plug the NanoS, 
- wait 30sec, 
- launch the monero app
- wait 30sec, 
- launch client

retry with 1 minute in case of failure



## DrCryptoKey | 2018-10-16T13:08:01+00:00


> On failing machine, you can also test that:
> 
> * plug the NanoS,
> * wait 30sec,
> * launch the monero app
> * wait 30sec,
> * launch client
> 
> retry with 1 minute in case of failure

Even with 1 minute pauses, the problem persists. My logs are supplied a few posts up, I can't quite figure out how to use usblyser, perhaps a more detailed explanation on what to do with it would be helpful? Thanks for assisting. 


## MrC0D3 | 2018-10-16T14:37:49+00:00
This seems to work for me (not a fix, workaround, only tried a few times with monero-wallet-cli)

- If Ledger is connected via USB, first disconnect the USB connection
- Navigate to where your wallet file is stored
- Start monero-wallet-cli, load the wallet file, but do not enter password to open wallet
- Connect Ledger via USB, enter PIN code, launch Monero App
- Go back to monero-wallet-cli, now enter wallet password

This seems to have worked for me a few times.

## iDunk5400 | 2018-10-16T16:49:07+00:00
Do you have USB 2 ports on your PC ? If you do, try using those. On my Linux boxes, for example, I can only use my Nano S in my front panel USB 2 ports. It won't work in USB 3 ports. On my Windows box, where I only have USB 3 ports, It works on some ports (chipset provided USB 3), and does not on others (ASMedia add-on chip).

## doserFu | 2018-10-16T17:07:56+00:00
Same issue with ledger, tried all the walkarounds, not working.

Error: failed to load wallet: Wrong sequence_idx

## selsta | 2018-10-16T17:09:50+00:00
@doserFu

Which OS are you using?

## doserFu | 2018-10-16T17:10:11+00:00
@selsta 

Sorry, Windows10

## philkode | 2018-10-16T21:14:30+00:00
@cslashm here's another USBLYZER dump including CLI wallet log-level 4, on Windows 10 (built with all appropriate dependencies)

[monero capture.zip](https://github.com/monero-project/monero/files/2484928/monero.capture.zip)

@MrC0D3 unfortunately that trick didn't seem to work for me...

@iDunk5400 
> 
> 
> > Basically means Ledger isn't usable on Windows as of v0.13.0.2.
> 
> Works fine for me on Windows 10. Make sure you've installed the [required dependency](https://github.com/monero-project/monero/pull/4203) before building.

Yeah I followed the instructions verbatim from the Github readme and the prerequisite steps seem to install all dependencies. I should clarify my post to indicate that it seems that for some machines, Ledger isn't working on the latest CLI. Glad to hear it's not universal though - hopefully we can figure out the root cause.

Update: this issue also seems to be occuring with the latest released v0.13.0.3 binaries, for what it's worth.

## marcelrv | 2018-10-16T21:21:49+00:00
same here... windows 10, ledger latest 1.4.2 firmware
Monero released v0.13.0.3 binaries

however, it is not sometimes, but sofar always

## ghost | 2018-10-16T22:54:39+00:00
Fresh install of Windows 10 + Monero 13.0.3 and Ledger Nano S 1.4.2 and I'm getting the wrong sequence idx issue as well. Tried several different USB ports and I still have the same issue.

## iDunk5400 | 2018-10-17T00:46:16+00:00
Does it work if you start the wallet with `--hw-device Ledger` ?

## smurfguy12 | 2018-10-17T00:52:20+00:00
Yeah can't get this to work at all. I usually use the GUI wallet. Tried starting in CLI but I have to use input args due to wallet location. Could using args be an issue?

## repetenz | 2018-10-17T01:13:43+00:00
I too am having the same issue, wrong sequence_idx, latest binary GUI 13.0.3 and Ledger Nano S. Tried all the approaches above, but have not been able to access my wallet thus far. Verified the GUI binary archive.

Edit: Non ledger wallets are fine.
Edit2: Windows 10, latest windows updates, ledger fw 1.4.2.

## xiphon | 2018-10-17T02:14:33+00:00
Could someone::
1. Apply the first patch, compile and test
2. Then apply the second patch, compile and test

PS: Would be great to see Usblyzer logs.

```diff
diff --git a/src/device/device_ledger.cpp b/src/device/device_ledger.cpp
index a1778496..461225ea 100644
--- a/src/device/device_ledger.cpp
+++ b/src/device/device_ledger.cpp
@@ -276,7 +276,7 @@ namespace hw {
     int device_ledger::set_command_header_noopt(unsigned char ins, unsigned char p1, unsigned char p2) {
       int offset = set_command_header(ins, p1, p2);
       //options
-      this->buffer_send[offset++] = 0;
+      this->buffer_send[offset] = 0;
       this->buffer_send[4] = offset - 5;
       return offset;
     }
```

```diff
diff --git a/src/device/device_io_hid.cpp b/src/device/device_io_hid.cpp
index 562aca8b..6fd90cb0 100644
--- a/src/device/device_io_hid.cpp
+++ b/src/device/device_io_hid.cpp
@@ -184,8 +186,9 @@ namespace hw {
       out[offset_out++] = ((sequence_idx >> 8) & 0xff);
       out[offset_out++] = (sequence_idx & 0xff);
       sequence_idx++;
-      out[offset_out++] = ((command_len >> 8) & 0xff);
-      out[offset_out++] = (command_len & 0xff);
+      unsigned int total_len = static_cast<unsigned int>(command_len) + offset_out;
+      out[offset_out++] = ((total_len >> 8) & 0xff);
+      out[offset_out++] = (total_len & 0xff);
       block_size = (command_len > this->packet_size - 7 ? this->packet_size - 7 : command_len);
       ASSERT_X(out_len >= block_size,  "out_len too short: "+std::to_string(out_len));
       out_len -= block_size;
```

## cslashm | 2018-10-17T06:58:51+00:00
hmm I do no agree with the previous patch, If I correctly re-read the code:
 - set_command_header will build `00 ins p1 p2 lc=00` and return offset=5 (next byte offset, actual length)
 - no incrementing offset will set buffer[4] = 0, and lead into `00 ins p1 p2 lc=00 payload=00`

`lc` is in fact 1, one byte data payload the option



## deathd0tcom | 2018-10-17T15:55:15+00:00
having the same issue myself (https://monero.stackexchange.com/questions/10366/v0-13-0-2-monero-wallet-cli-error-failed-to-load-wallet-wrong-sequence-idx-l) 
 
using ledger fw 1.4.2 & Windows 10 I keep getting the same error after entering my Wallet password:

Error: failed to load wallet: Wrong sequence_idx

Tried some of the recommended fixes from this thread like waiting 30 seconds-1 minute between plugging into USB & running Monero App. I also tried not plugging in the Ledger Nano S until I get prompted for the password, and then after plugging it in, entering PIN & opening the Monero App I enter the wallet password, but still get the same 'Wrong sequence_idx' error.

Any & all help appreciated!!!



## cslashm | 2018-10-17T16:05:00+00:00
For any test, keep in mind that the application on NanoS SHALL BE launched BEFORE the monero desktop client.

## mferrari43 | 2018-10-17T16:38:30+00:00
> For any test, keep in mind that the application on NanoS SHALL BE launched BEFORE the monero desktop client.

just tried this, i'm on windows 10 and it's not working for me as well :(

## doserFu | 2018-10-17T17:50:31+00:00
i have tried in different win10 machines and the same happens...! 

## Makazar | 2018-10-17T18:03:52+00:00
Spent all day pissing about with this. macOS High Sierra + Monero 13.0.3 and Ledger Nano S 1.4.2 and I'm getting the **Couldn't open wallet:wrong sequence idx** or **Couldn't open wallet: std::bad_alloc** both alternating as they please. Tried several different USB ports and I still have the same issue.

## iDunk5400 | 2018-10-17T21:36:16+00:00
To those affected, can you try `git revert bd7b800` and see if that makes any difference ?

## Makazar | 2018-10-17T21:39:13+00:00
@iDunk5400 - Can you please explain what to do with 'git revert bd7b800' in more detail? Happy to try.


## ghost | 2018-10-17T21:42:15+00:00
He means for someone to recompile 13.03 without that change


## smurfguy12 | 2018-10-17T22:03:13+00:00
I suggest if you kept your old version 12 client to move funds elsewhere before tomorrow. That is what I am doing.

## Makazar | 2018-10-17T22:05:18+00:00
@smurfguy12 - Unfortunately I do not have the 12 GUI any longer. Not sure if it can be emailed if someone still has it?

## ghost | 2018-10-17T22:06:15+00:00
Send to where? Mine are on a Ledger Nano S. I think once the bugs are fixed we'll be good to go. It's not like the Monero is disappearing off of the Ledger.

## smurfguy12 | 2018-10-17T22:12:17+00:00
It's not disappearing, but it's going to be a hell of a lot harder to access your money once this fork happens. 

## iDunk5400 | 2018-10-17T22:18:02+00:00
[v0.12.3.0 GUI is not that hard to find](https://github.com/monero-project/monero-gui/releases/tag/v0.12.3.0) if you want to transfer from your device until this is fixed.

## arguser | 2018-10-18T00:23:15+00:00
@smurfguy12 what if we access the Ledger Wallet trough monerujo? Would that make sense? I still don't understand why it would be harder to access the money after the fork.

## smurfguy12 | 2018-10-18T02:33:42+00:00
@arguser Not gonna lie. Did not know about monerujo. Pretty cool. Convinced me to finally get an OTG cable. 

## Makazar | 2018-10-18T06:18:26+00:00
**@iDunk5400**  Thanks for that bud. Just installed it and now even v0.12.3.0 wouldn't open the wallet (macOS High Sierra). Think I'll just have to wait it out 'till the workable v0.13 gets released.

## 37thChamber | 2018-10-18T14:15:35+00:00
Also receiving this error when using the GUI with a Nano S on Win 10.  

## ghost | 2018-10-18T14:27:30+00:00
Im having the same issue on Win 10. I upgraded to the newest build recently and this error popped up :(
I have tried cleaning all files that XMR created on my PC but still same issue :(

## Rev-b | 2018-10-18T15:32:02+00:00
"Error: failed to load wallet: Wrong sequence_idx" also here with a Ledger Nano S. 
Windows 10, both with GUI and CLI.

## cslashm | 2018-10-18T15:41:30+00:00
pending fix incoming : #4643

## binarymind | 2018-10-18T19:01:11+00:00
maybe stupid but I was not able to launch with the connection to the ledger (I had the error src/device/device_io_hid.cpp:97 Unable to open device 1:11415) until I did run the start--gui.sh in sudo. If it helps anyone...

## althea16 | 2018-10-18T21:28:51+00:00
I am having the same problem with gui v0.13.0.3.
"Couldn't open wallet: Wrong sequence_idx"
I am hoping some specific instructions will surface on how to fix this. I'm very confused...and worried. But glad that I found this thread, at least. 
Does anyone how to proceed?

## selsta | 2018-10-18T21:33:38+00:00
@althea16 The problem will be fixed with v0.13.0.4, which should come out in the next days.

## althea16 | 2018-10-18T21:35:32+00:00
> 
> 
> @althea16 The problem will be fixed with v0.13.0.4, which should come out in the next days.

@selsta Thank you!

## moneromooo-monero | 2018-10-20T18:57:37+00:00
Believed fixed now.

+resolved

## Zarkoob | 2018-10-21T04:40:27+00:00
I've checked out the latest commits and built. My Monerod / wallet CLI version now shows 

`Monero 'Beryllium Bullet' (v0.13.0.3-4ad6b662)`

I do think the fix for these changes are incorporated but I'm still getting
`Error: failed to load wallet: Wrong sequence_idx`

@selsta have you been able to check this?

## deathd0tcom | 2018-10-21T12:28:13+00:00
I'm still unable to utilize the Ledger, was wondering why it was being reported as 'resolved' when the issue persists on v0.13.0.3. Hoping v0.13.0.4 comes out soon w/ fix, or someone can explain why this is being described as resolved when people are still getting the error, many of us 100% of the time, not "sometimes" as described above.

## selsta | 2018-10-21T12:30:13+00:00
This is a dev issue tracker. If something is resolved in the code, it is resolved here.

## althea16 | 2018-10-21T14:50:46+00:00
I still have the same issue:
"Couldn't open wallet: Wrong sequence_idx" using the available gui v0.13.0.3.
Why is this marked resolved?

## xiphon | 2018-10-21T14:54:51+00:00
@Zarkoob are you sure you checked out the latest `master` branch? Could you provide `git log -n 1` output?

## ghost | 2018-10-21T15:02:08+00:00
I checked the commits and I don't see any committed code that affects the ledger nano s issue discussed here. I compiled as of a day ago and I still face the same issue. Could you reference the correct commit so that I can review the code?

https://github.com/monero-project/monero-gui/commits/master

## iDunk5400 | 2018-10-21T15:03:29+00:00
@althea16 It is marked as resolved because a fix has been merged.
As @selsta mentioned, this is a dev issue tracker, not a user support forum.

## iDunk5400 | 2018-10-21T15:06:08+00:00
#4642 has been merged to `master`, #4643 has been merged to `release-v0.13`.

## ghost | 2018-10-21T15:19:42+00:00
Okay ... so we have to include the updated Monero codebase when recompiling Monero GUI. Got it.

## althea16 | 2018-10-21T15:26:57+00:00
> 
> 
> #4642 has been merged to `master`, #4643 has been merged to `release-v0.13`.

Thank you. So if I delete my current V0.13.0 and reinstall then it should work?

## iDunk5400 | 2018-10-21T15:30:13+00:00
@jefferson-1 If you're building Monero GUI from release-v0.13 branch, try replacing as yet non-existent `v0.13.0.4` tag with `release-v0.13` branch [here](https://github.com/monero-project/monero-gui/blob/release-v0.13/get_libwallet_api.sh#L20).

@althea16 You have to compile from source to get the fix until the new binaries are released.

/Edit: typos.

## ghost | 2018-10-21T15:30:30+00:00
@althea16 

Here is the process that you should follow.

1. Delete current monero install...sure.
2. Git Clone the Monero and Monero GUI release branches
3. Compile using the instructions provided in the Readme
4. Update this thread with your testing results...

or...

You can wait until someone releases an official update.

## althea16 | 2018-10-21T15:36:02+00:00
@jefferson-1 Thank you. I'm guessing I should just wait until an official release. That should probably come soon, right? It would be bad for a project to leave non-techies without access..?

## ghost | 2018-10-21T15:45:05+00:00
@althea16 Yes...the unpaid workers and contributors of Monero are working at it. I'm sure that it will happen. Given that they have released prior updates as quickly as possible...I'm sure that they will release this update soon.

If you want it sooner, compile it yourself as I am doing.

## iDunk5400 | 2018-10-21T16:02:06+00:00
Nightly builds of current master are [here](https://build.getmonero.org/downloads/monero-2287fb9f-win64.tar.gz) for Win64 and [here](https://build.getmonero.org/downloads/monero-2287fb9f-osx-10.13.tar.gz) for OSX.

## iDunk5400 | 2018-10-21T19:30:39+00:00
That is a different error. You may want to delete or move your wallet cache file elsewhere and try again.

/Edit: this message was in response to a user who subsequently deleted his/her comment.

## selsta | 2018-10-21T21:19:19+00:00
Can Windows/macOS users who have troubles opening the Ledger wallet test the nightly linked by @iDunk5400 above? Does it fix the issue?

## Zarkoob | 2018-10-22T00:29:59+00:00
I still have the following error:
`Error: failed to load wallet: Wrong sequence_idx`

I've tried using 

```
(v0.13.0.0-master-2287fb9f)
(v0.13.0.3-4ad6b662)
```

Both have the same error.

macOS Mojave v10.14

## DrCryptoKey | 2018-10-22T07:23:14+00:00
I can confirm that the latest CLI nightly (I used the Win64 link that @iDunk5400 posted above) works fine and fixed the issue. Thank you everyone for finding the bug and fixing it so quickly!

## Zarkoob | 2018-10-22T14:12:47+00:00
@DrCryptoKey can you try opening and closing the wallet like 20 times in a row?

Some times I can get it to work 10 times in a row oddly. 

Since my windows machines have the issue I wonder if you ran into a string of “good luck”? 

## xiphon | 2018-10-22T14:52:23+00:00
@Zarkoob please run master binaries (`v0.13.0.0-master-2287fb9f` would be fine) and provide the `monero-wallet-cli` logs with `--log-level 4`

## Zarkoob | 2018-10-23T02:04:54+00:00
[monero-wallet-cli.log](https://github.com/monero-project/monero/files/2504147/monero-wallet-cli.log)

@xiphon thank you for taking the time for this! 

## xiphon | 2018-10-23T02:23:48+00:00
According to the logs the binary doesn't contain #4642 fix

## xiphon | 2018-10-23T03:53:45+00:00
Finally localized Mac-related problem (thanks to @Zarkoob for IRC log-gathering session)

**OS**
macOS Mojave v10.14

**Issue**
We are invoking `hid_open_path` to open a device.
And there is no way to select a desired device with HIDAPI if both devices have the same OS-specific device path, Using `hid_open` won't work either, it is implemented through `hid_open_path` as well.

**Workaround**
* Building Monero with `depends` might resolve the issue.
* Updating hidapi library might resolve the issue.

**Log**

```
2018-10-23 02:49:34.902	     0x11929f5c0	DEBUG	device.io	src/device/device_io_hid.cpp:83	Looking for HID Device with interface_number 0 or usage_page 65440
2018-10-23 02:49:34.902	     0x11929f5c0	DEBUG	device.io	src/device/device_io_hid.cpp:92	SKIPPED  HID Device path USB_2c97_0001_14200000 interface_number -1 usage_page 61904
2018-10-23 02:49:34.902	     0x11929f5c0	DEBUG	device.io	src/device/device_io_hid.cpp:92	SELECTED HID Device path USB_2c97_0001_14200000 interface_number -1 usage_page 65440
```

## selsta | 2018-10-23T14:57:19+00:00
Thanks @xiphon 

I debugged with @Zarkoob and using the latest master version seems to have fixed the issue. (At least it didn’t occur after opening the wallet 25 times in a row.)

## dEBRUYNE-1 | 2018-10-23T16:00:56+00:00
If @selsta is unable to reopen this issue, I guess we can move to #4706. 

## scaramanzia | 2018-10-24T04:17:33+00:00
I had the same error. "Error: failed to load wallet: Wrong sequence_idx"
My solution was to go to "USB Configuration" then "Bluetooth and other devices" In "Other devices" "Ledger S" Remove device.
Then it worked.

Sorry for my English,
I do not know if the problem had already been solved.
Greetings.

## 37thChamber | 2018-10-24T17:10:57+00:00
> 
> 
> I had the same error. "Error: failed to load wallet: Wrong sequence_idx"
> My solution was to go to "USB Configuration" then "Bluetooth and other devices" In "Other devices" "Ledger S" Remove device.
> Then it worked.
> 
> Sorry for my English,
> I do not know if the problem had already been solved.
> Greetings.

This actually worked!  Thank you!

## mferrari43 | 2018-10-25T00:01:37+00:00
> I had the same error. "Error: failed to load wallet: Wrong sequence_idx"
> My solution was to go to "USB Configuration" then "Bluetooth and other devices" In "Other devices" "Ledger S" Remove device.
> Then it worked.
> 
> Sorry for my English,
> I do not know if the problem had already been solved.
> Greetings.

i came here to say this worked for me as well :)

# Action History
- Created by: selsta | 2018-10-08T20:13:09+00:00
- Closed at: 2018-10-20T19:08:52+00:00
