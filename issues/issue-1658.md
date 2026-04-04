---
title: monero-wallet-gui cannot be opened because of a problem. [Mac OS Mojave]
source_url: https://github.com/monero-project/monero-gui/issues/1658
author: tiosecurity
assignees: []
labels:
- resolved
created_at: '2018-10-16T02:34:37+00:00'
updated_at: '2018-11-02T12:45:48+00:00'
type: issue
status: closed
closed_at: '2018-10-18T12:45:23+00:00'
---

# Original Description
Monero wallet [GUI Beryllium Bullet v0.13.0.3](https://github.com/monero-project/monero-gui/releases)
Mac OS Mojave 
`Crashed Thread:        0
Exception Type:        EXC_CRASH (SIGABRT)
Exception Codes:       0x0000000000000000, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY
Termination Reason:    DYLD, [0x1] Library missing
Application Specific Information:
dyld: launch, loading dependent libraries
Dyld Error Message:
  Library not loaded: /usr/local/Cellar/openssl/1.0.2p/lib/libcrypto.1.0.0.dylib
  Referenced from: /Applications/monero-wallet-gui.app/Contents/Frameworks/libssl.1.0.0.dylib
  Reason: image not found   `
![monero-error](https://user-images.githubusercontent.com/8238880/46989237-ec6bf900-d12e-11e8-8aa6-d8c37f6f5bbb.png)


# Discussion History
## armybill461 | 2018-10-16T03:22:11+00:00
I got the same message, however I am able to run monorod and its currently updating the blockchain

## hoyanf | 2018-10-16T06:09:18+00:00
Dynamic Library Error

Dyld Error Message:
  Library not loaded: /usr/local/**Cellar**/openssl/1.0.2p/lib/libcrypto.1.0.0.dylib **<- missing**
  Referenced from: /Applications/monero-wallet-gui.app/Contents/Frameworks/libssl.1.0.0.dylib
  Reason: image not found

ls /usr/local/
bin		libexec		share	 etc		var

find /usr/ -name libcrypto.* -print
/usr//lib/libcrypto.42.dylib
/usr//lib/libcrypto.0.9.7.dylib
/usr//lib/libcrypto.41.dylib
/usr//lib/libcrypto.35.dylib
/usr//lib/libcrypto.dylib
/usr//lib/libcrypto.0.9.8.dylib


## selsta | 2018-10-16T12:06:12+00:00
Can someone test this out:

1. Install homebrew from https://brew.sh
2. Install `openssl` using `brew install openssl`

This would obviously be only a temporary fix until there are new binaries without this problem.

## Aquilae32 | 2018-10-16T13:09:34+00:00
Installing OpenSSL via Homebrew has allowed me to then open monero-wallet-gui.

## xyberpix | 2018-10-16T13:59:45+00:00
Okay, so a workaround is good, but I really don't feel the urge to install HomeBrew. Dev's any idea on when a fix is likely at all? BTW, thank you for all the great work.

## binarymind | 2018-10-16T14:00:37+00:00
openssl 1.0.2l -> 1.0.2p was indeed necessary for me

## dEBRUYNE-1 | 2018-10-16T14:56:08+00:00
@xyberpix - Stoffu is currently investigating the issue. Hopefully we can produce a new Mac OS X build soon that includes a fix. 

## xyberpix | 2018-10-16T14:56:58+00:00
@dEBRUYNE-1 Thanks man, appreciate the update.

## dEBRUYNE-1 | 2018-10-16T14:57:23+00:00
You're welcome. 

## Makazar | 2018-10-16T22:36:33+00:00
Trying to install HomeBrew ( by Restart-Utility-Terminal Pad) but it would not happen and getting the message: "Could not resolve host: raw.githubusercontent.com"

Any idea what I can do?

## selsta | 2018-10-16T22:50:02+00:00
@Makazar

The normal Terminal, not the Terminal in the Restart Utility.

## Makazar | 2018-10-16T23:03:44+00:00
@selsta 

Thanks. Have done but now it displays this message and would not let me type anything: "Press RETURN to continue or any other key to abort
==> /usr/bin/sudo /bin/chmod u+rwx /usr/local/bin
Password: "


## Makazar | 2018-10-16T23:25:23+00:00
Ok, figured out why. The password icon was displayed to signify that the password won't be shown when typing it. So I typed it in and the whole bunch of commands is downloading. Inept or what?😂

## Makazar | 2018-10-16T23:36:03+00:00

@selsta 

YES! Installation of Homebrew completed, then installed 'brew install openssl' and the wallet has just opened!
Thanks guys.

## tiosecurity | 2018-10-17T14:17:10+00:00
I confirm GUI Beryllium Bullet v0.13.0.3 is working fine with Mac OS Mojave now installing homebrew https://brew.sh and running:
`brew install openssl`
Open the wallet, done ✅

## erciccione | 2018-10-18T12:36:33+00:00
+resolved

## phik | 2018-10-19T06:22:48+00:00
Surely this isn't resolved yet?  We can't possibly expect the average person to install brew and openssl manually?  That's insane.

## selsta | 2018-10-19T07:13:31+00:00
We resolved this on the build machine, v0.13.0.4 has this fixed and should be out in the next days.

## umma08 | 2018-10-19T09:50:12+00:00
> We resolved this on the build machine, v0.13.0.4 has this fixed and should be out in the next days.

any update on this? will this also fix the issue on older versions of osX? i am on 10.11.4. 

thanks in advance!

## dEBRUYNE-1 | 2018-10-19T11:14:06+00:00
>will this also fix the issue on older versions of osX? i am on 10.11.4.

Yes and GUI v0.13.0.4 should be out soon. 

## Emzy | 2018-10-24T16:35:52+00:00
Quick workaround: 
`
$ sudo -i 

root# mkdir /usr/local/Cellar/openssl/1.0.2p/lib/ 

root# ln -s /Applications/monero-wallet-gui.app/Contents/Frameworks/libcrypto.1.0.0.dylib /usr/local/Cellar/openssl/1.0.2p/lib/

`

## ProBowie | 2018-10-28T10:38:21+00:00
I had both installed, but had to upgrade brew via: `brew upgrade`

## freddrums | 2018-11-02T06:54:27+00:00
Hello Iam trying to figure out how to install openssl. I am the avg person who has no idea how to do this. I have founs openssl in homebrew. Now trying to get the openssl to run on my mac. My mac says i need an app to run it. which app? any help to get thru would be amazing.
thanks!
Fred

## Aquilae32 | 2018-11-02T12:31:29+00:00
It is sufficient to have installed openSSL with Brew (“brew install openssl” in a terminal, supposing you have Brew already installed). The Monero GUI is the app that will automatically find it when opening. If it doesn’t, maybe openSSL is not in the PATH (the default directories where the system looks for a program).

(From Brew)
openssl is keg-only, which means it was not symlinked into /usr/local,
because Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries.

If you need to have openssl first in your PATH run:
  echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile



## selsta | 2018-11-02T12:40:31+00:00
This is fixed in the v0.13.0.4 binaries, openSSL is not required.
https://www.reddit.com/r/Monero/comments/9ti2on/gui_v01304_beryllium_bullet_released/

# Action History
- Created by: tiosecurity | 2018-10-16T02:34:37+00:00
- Closed at: 2018-10-18T12:45:23+00:00
