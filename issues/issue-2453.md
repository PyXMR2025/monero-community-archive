---
title: windows build creates extra libraries, crashes on execution
source_url: https://github.com/monero-project/monero/issues/2453
author: theshoeshiner
assignees: []
labels:
- invalid
created_at: '2017-09-16T10:52:32+00:00'
updated_at: '2017-10-05T08:48:21+00:00'
type: issue
status: closed
closed_at: '2017-10-05T08:48:21+00:00'
---

# Original Description
Im trying to build monero on windows. It compiles fine but creates 3 extra files in the release/bin directory:

libcrypto.a
libssl.a
libwinpthread-1.dll

When I run monerod it crashes with a generic "Application was unable to start correctly (0x000007b)" message. If I remove the .dlls the crash shows the message "libwinpthread-1 was missing from your computer".

What is going on locally that doesn't produce the exact build I got from https://getmonero.org/downloads/#windows

Edit: Looks like the latest download _does_ contain these extra libraries. My build is still crashing upon starting though.

# Discussion History
## gsovereignty | 2017-09-16T12:37:06+00:00
Are you using msys2?

There are usually dll files in the msys2 bin directory that you also need to copy to binary directory.


## theshoeshiner | 2017-09-16T12:57:40+00:00
Yea, I followed the directions for the windows build in the readme. 
The getmonero.org download (for v 0.10.3.1) contains the following files:

monero-blockchain-export.exe
monero-blockchain-import.exe
monero-utils-deserialize.exe
monero-wallet-cli.exe
monero-wallet-rpc.exe
monerod.exe

Is there a reason my build, from the same tag, isn't producing that exact set?

## gsovereignty | 2017-09-16T14:21:26+00:00
I'm not sure why, but I get the same result as you. I'm not sure how the official binaries are being built.

To verify that its just missing dll libraries causing it to fail you can try copying monerod.exe into the bin directory at the root of your msys2 folder. Anything it could possibly need should be in there so that should at least get it to run.

Apart from that, hopefully someone watching can elaborate on the build process thats being used for official releases.

## hyc | 2017-09-16T16:40:46+00:00
You should be using these instructions https://forum.getmonero.org/5/support/2510/building-monero-v0-9-2-on-win32 and you should be building v0.11 now, not v0.10.

## theshoeshiner | 2017-09-17T13:51:58+00:00
I followed those instructions and got the same result. It also still complains about the libwinpthread-1.dll library if I remove it.

My guess is that it's because those instructions are very old. Are there updated instructions somewhere that are specific to win64 and v11?

## theshoeshiner | 2017-09-17T22:58:07+00:00
Update: I went through the instructions again and followed them as-is with 0.10.3.1, using 32 bit everything, instead of trying to modify them for 64 bit. it compiled and runs fine. 

I'll keep working on getting the 64 bit build working. I probably just had some paths incorrect.

## moneromooo-monero | 2017-09-25T20:27:04+00:00
Do you still get the crash with current master ? Known crashes are now fixed.

## moneromooo-monero | 2017-10-05T08:45:34+00:00
Rereading, it looks like the crash was just due to a 32/64 bit configuration mixup, closing.

+invalid

# Action History
- Created by: theshoeshiner | 2017-09-16T10:52:32+00:00
- Closed at: 2017-10-05T08:48:21+00:00
