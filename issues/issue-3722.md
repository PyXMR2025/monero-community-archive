---
title: Monero GUI crashing on Mac
source_url: https://github.com/monero-project/monero-gui/issues/3722
author: b3K1ndRw1nd
assignees: []
labels: []
created_at: '2021-10-29T06:10:45+00:00'
updated_at: '2024-09-03T14:03:43+00:00'
type: issue
status: closed
closed_at: '2022-04-27T04:52:24+00:00'
---

# Original Description
Whenever I try to run the Monero GUI on my Mac Catalina Vers 10.15.7, it crashes with the following logs
[monero-logs.txt](https://github.com/monero-project/monero-gui/files/7439274/monero-logs.txt)


I have to do
```
export QMLSCENE_DEVICE=softwarecontext;
/Volumes/Macintosh HD/Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
``` 
to get it to run

# Discussion History
## selsta | 2021-10-29T12:31:27+00:00
What kind of Mac is this? The program doesn't crash in monero code.

## b3K1ndRw1nd | 2021-10-29T13:19:56+00:00
I have a 13-inch MacBook Pro Mid 2012

## b3K1ndRw1nd | 2021-10-29T13:20:58+00:00
I ran monero on this Macbook without issue for about 3 months now. This is the first time it won't launch.

## selsta | 2021-10-29T14:15:53+00:00
Did you update the application? If yes, can you try the previous version?

If it suddenly fails it's most likely not an issue on our side, seeing that no one else reported a similar issue.

## Frontrunner1488 | 2021-10-31T14:58:02+00:00
GUI crashing on startup after latest OS update.

## sMtzDczDq | 2021-11-01T14:47:13+00:00
The error I'm getting when starting it from terminal is this: W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth" No idea what it means. A quick google search points to Qt Framework

## selsta | 2021-11-01T17:35:11+00:00
@Frontrunner1488 which OS?

@sMtzDczDq same question, which OS, and since when do you have this issue? You only posted a warning which is unrelated.

## sMtzDczDq | 2021-11-01T17:47:29+00:00
@selsta macOS Catalina 10.15.7. I think it started after upgrading to 10.15.7 which according to my logs was October 26th. I tried the previous version of the gui but it has the same problem. I'm trying to get it running with a debugger attached. If I find anything I'll let you know.

## selsta | 2021-11-01T17:49:51+00:00
Can you update to macOS 11? It appears if 10.15.7 has a bug. The code doesn't crash inside monero code, so there isn't much we can do.

Unfortunately I don't have a machine on 10.15 to reproduce.

## Frontrunner1488 | 2021-11-01T18:03:33+00:00
@selsta Catalina, going to try to upgrade OS to Big Sur or Monterrey and see if that resolves the issue. 

## selsta | 2021-11-01T18:05:43+00:00
```
export QMLSCENE_DEVICE=softwarecontext;
/Volumes/Macintosh HD/Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
```

As a workaround it's possible to use the GUI with these commands on 10.15.7, as written in the original issue post.

## TonyD83 | 2021-11-04T11:25:55+00:00
I have the exact same issue on 10.15.7. Seems like it started after the recent security update. I tried searching the specific error. From what I can find this is due to the application trying to access a deprecated gpu driver? Can anyone confirm? 

Error:
Application Specific Signatures:
Graphics kernel error: 0xfffffffb

## selsta | 2021-11-04T13:48:38+00:00
@TonyD83 please see my comment here: https://github.com/monero-project/monero-gui/issues/3722#issuecomment-956460401

You either have to update your OS, or start in low graphics mode.

It's either a bug in Qt or in macOS, but seeing that it only shows up on this one macOS version I would assume it's due to a bug in macOS.

## mouldysandals | 2021-11-15T00:13:51+00:00
> ```
> export QMLSCENE_DEVICE=softwarecontext;
> /Volumes/Macintosh HD/Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
> ```
> 
> 
>      
>   
> 
> As a workaround it's possible to use the GUI with these commands on 10.15.7, as written in the original issue post.

Hi, it says no file or depository by that name but there 100% is, any advice? I'm running this in terminal, should it be console? Sorry for noob questions

## selsta | 2021-11-15T00:24:49+00:00
@mouldysandals

If you have the GUI inside the application folder try with Terminal:


```
QMLSCENE_DEVICE=softwarecontext /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
```

## TonyD83 | 2021-11-15T01:54:18+00:00
> @mouldysandals
> 
> If you have the GUI inside the application folder try with Terminal:
> 
> ```
> QMLSCENE_DEVICE=softwarecontext /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
> ```

This worked for me. Thanks!

## richelo | 2021-11-15T06:03:21+00:00
I am trying to run this for the first time on the M1 Mac Mini with MacOS 12.0.1.

I try and create a wallet, and at the set password screen it crashes. It always happens when I am retyping the password in the confirm field.

`Application Specific Information:
monero-wallet-gui(99047,0x2016cb600) malloc: Incorrect checksum for freed object 0x7fe6a370bcf8: probably modified after being freed.
Corrupt value: 0x4039642d0cfc4e3f
abort() called`

I tried running:

`QMLSCENE_DEVICE=softwarecontext /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui`

I get this in the terminal: 

`2021-11-15 05:57:13.797	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"`

I get a whole bunch of those and the application never starts.

## selsta | 2021-11-15T06:10:33+00:00
@richelo I can't reproduce this on my M1 MBP with 12.1 beta.

Can you open Console.app, copy paste the full crash report and upload it to paste.debian.net?

## richelo | 2021-11-15T06:24:28+00:00
@selsta do you want me to run the application from the console, or just run the app normally, and then grab the whole crash report?

Trying to run from the console never starts. It always just sits at `2021-11-15 06:24:04.243	W <Unknown File>: QML QQuickLayoutAttached: Binding loop detected for property "preferredWidth"`

## selsta | 2021-11-15T06:26:01+00:00
> or just run the app normally, and then grab the whole crash report?

Run the app normally and get a crash report.

## richelo | 2021-11-15T06:29:35+00:00
@selsta , here you go.
[MoneroGuiCrash.txt](https://github.com/monero-project/monero-gui/files/7536358/MoneroGuiCrash.txt)

## selsta | 2021-11-15T06:30:37+00:00
What kind of password did you enter? How many characters?

## richelo | 2021-11-15T06:33:35+00:00
10 Characters, 1 capital letter and a ! and a few numbers as well.

## selsta | 2021-11-15T06:34:59+00:00
Does it also crash if you enter e.g. 123 as your password? According to the crash log the issue is inside an external library for password strength.

## richelo | 2021-11-15T06:40:58+00:00
123 as password works with no issue.

I will play around a bit with passwords to see if I can set a secure one without the app crashing.

I do think it is something that needs to be investigated and fixed. It's not some insane password I am trying to use.

## selsta | 2021-11-15T06:59:19+00:00
Could you generate a password that makes it crash on your side so that I can reproduce and attempt to fix it?

## selsta | 2021-11-15T07:23:53+00:00
Might have found the issue: https://github.com/tsyrogit/zxcvbn-c/pull/11, opened a PR for it: https://github.com/monero-project/monero-gui/pull/3735

(To clarify, this should fix the issue in https://github.com/monero-project/monero-gui/issues/3722#issuecomment-968565551, not the crash on macOS 10.15.7)

## mouldysandals | 2021-11-15T15:11:49+00:00
> @mouldysandals
> 
> If you have the GUI inside the application folder try with Terminal:
> 
> ```
> QMLSCENE_DEVICE=softwarecontext /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
> ```

thank you so much selsta works perfectly

## mouldysandals | 2021-11-15T15:37:57+00:00
> @mouldysandals
> 
> If you have the GUI inside the application folder try with Terminal:
> 
> ```
> QMLSCENE_DEVICE=softwarecontext /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
> ```

hi sorry selsta, it's opening and 'working' it's showing me my funds, but it's stuck trying to connect to a remote node and i can't send the funds anywhere, on the terminal it just keeps saying daemon error - any advise? pls

## selsta | 2021-11-15T16:06:39+00:00
Can you go to Settings -> Info and check which "wallet mode" you are using?

## mouldysandals | 2021-11-15T16:37:53+00:00
> Can you go to Settings -> Info and check which "wallet mode" you are using?

Advanced mode (Remote node)

## mouldysandals | 2021-11-15T16:39:02+00:00
Oh wait, for some reason it's working now without me changing anything... weird, but no complaining! Thanks for your help anyway!

## selsta | 2021-11-15T16:44:28+00:00
@mouldysandals next time try a different remote node

## ALM0000 | 2023-01-16T11:47:26+00:00
hey @selsta 

I have a similar problem to @richelo but it crashes as soon as monero and the password field loads. 

**Info**

- Mac OS Monterey 12.5.1
- Monero V18.1.2

**Crash Report** 

- [Click here](https://paste.debian.net/hidden/e33b0c80)

Any ideas? 


## selsta | 2023-01-16T16:51:11+00:00
@ALM0000 does the same crash happen after creating a new wallet?

## ALM0000 | 2023-01-16T19:00:33+00:00
Hey @selsta 

Thanks for the quick reply. I can't even get to a wallet. As soon as I load the GUI wallet, it appears to enter password and then immediately crashes. 

I've also deleted my wallets but the same thing happens :(

## selsta | 2023-01-16T19:01:55+00:00
The crash report shows a triggered assert in operating system related code, I have never seen this before and unfortunately no idea. Can you try out Feather Wallet?

## epoberezkin | 2024-06-29T08:52:18+00:00
I have a similar issue with another hardware wallet, the log says 
Get public address exception: Call method failed
Cannot get a device address

GUI version: 0.18.3.3-release (Qt 5.15.13)
Embedded Monero version: 0.18.3.3-81d4db08e

## kupietools | 2024-08-23T07:02:27+00:00
I can't get this to work at all. A minute after I open it, Monero Wallet GUI consumes 100GB of virtual memory and then crashes. It's not generating anything under Crash Reports, but this is under Diagnostic Reports: https://pastebin.com/cFNeeWtT

Running `QMLSCENE_DEVICE=softwarecontext /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui` starts up the GUI app, but quickly freezes. Generated log has now sat for over 5 minutes with no new lines added to it and the app not starting: https://pastebin.com/CQp3swKK

Running MacOS Monterey 12.7.6, 16 GB ram. Monero-wallet-GUI 0.18.3.4.

## selsta | 2024-09-03T14:03:42+00:00
@kupietools this sounds like a bizarre issue, never have seen such a report before on macOS... do you have a different Mac where you can test this?

# Action History
- Created by: b3K1ndRw1nd | 2021-10-29T06:10:45+00:00
- Closed at: 2022-04-27T04:52:24+00:00
