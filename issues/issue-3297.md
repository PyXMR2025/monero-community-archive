---
title: '[1/10/2021 4:24 PM] 2021-01-10 22:24:06.926 I Monero ''Oxygen Orion'' (v0.17.1.9-release)  Error:
  Couldn''t connect to daemon: 127.0.0.1:18081'
source_url: https://github.com/monero-project/monero-gui/issues/3297
author: RickyRiccardo1
assignees: []
labels: []
created_at: '2021-01-10T22:33:01+00:00'
updated_at: '2021-10-16T05:27:02+00:00'
type: issue
status: closed
closed_at: '2021-04-21T01:35:15+00:00'
---

# Original Description
Just installed Monero Gui wallet ('Oxygen Orion') tried to start daemon and received many "[1/10/2021 4:24 PM] 2021-01-10 22:24:06.926 I Monero 'Oxygen Orion' (v0.17.1.9-release) 
Error: Couldn't connect to daemon: 127.0.0.1:18081" errors

I then tried to start "monerod.exe" manually through the command line and then waited about 5 minutes for any glimpse of a "connection". During this 5 minutes the only thing that happened was the Network Status changed from "Disconnected" to "Connecting" (the status "Disconnected" lasted for about ten seconds whereas the "Connecting" status lasts for about one second). I'm new to Monero, and was advised to start a local node; any help would be greatly appreciated!

# Discussion History
## selsta | 2021-01-10T22:35:19+00:00
Do you use an anti virus / firewall?

Can you restart your computer, start monerod.exe, wait a minute and then start the GUI and report back if it connects?

## RickyRiccardo1 | 2021-01-10T23:02:50+00:00
I tried going through the windows cmd, didn't work. Then found monerod (application) in file explorer (Windows 10), tried to run it but it immediately closes.. so I assume it's a firewall issue. If that is, in fact, a correct assumption: do you have any recommended course of action?
   Thanks again

Edit: also tried Windows+R "monerod.exe" and recieved error message claiming that Windows couldn't find it.

## selsta | 2021-01-10T23:08:32+00:00
Can you open cmd.exe, drag and drop monerod.exe into it and then press enter and post the output here.

## RickyRiccardo1 | 2021-01-10T23:10:37+00:00
There was no output, it just tried to run the application "monerod" and then I got a message from Windows security saying "potentially unwanted app found"

Waited a few more minutes, tried again here we go: 
2021-01-10 23:18:42.998 I Monero 'Oxygen Orion' (v0.17.1.9-release)
2021-01-10 23:18:42.999 I Initializing cryptonote protocol...
2021-01-10 23:18:43.001 I Cryptonote protocol initialized OK
2021-01-10 23:18:43.002 I Initializing core...
2021-01-10 23:18:43.003 I Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2021-01-10 23:18:43.003 W Failed to open lmdb environment: Input/output error
2021-01-10 23:18:43.004 E Error opening database: Failed to open lmdb environment: Input/output error
2021-01-10 23:18:43.005 I Stopping cryptonote protocol...
2021-01-10 23:18:43.005 I Cryptonote protocol stopped successfully
2021-01-10 23:18:43.006 E Exception in main! Failed to initialize core


## selsta | 2021-01-10T23:39:58+00:00
This seems to be an issue with your anti virus. https://monero.stackexchange.com/questions/10798/my-antivirus-av-software-blocks-quarantines-the-monero-gui-wallet-is-there

## RickyRiccardo1 | 2021-01-10T23:50:22+00:00
okay, done! So now that that has been done.. do I just start up the gui and let it run?


## RickyRiccardo1 | 2021-01-11T00:19:43+00:00
Didn't work. Node wont start and the daemon can't connect.

## matthewjamesr | 2021-01-11T11:34:58+00:00
@RickyRiccardo1 In your anti-virus, add a folder-level exception for the following path (default data directory): `C:\ProgramData\bitmonero`. @ respond if that did not work.

## RickyRiccardo1 | 2021-01-16T03:00:54+00:00
Um, sorry to keep you waiting so long, other things had to be done I hope you understand. But, regarding your previous response, @matthewjamesr, the creating an exclusion did Not work; also I don't have the folder "ProgramData" but have other folders titled "Program Files x86" and "Program Files", another folder starting with P is "PerfLogs" but it's empty.... wondering if I could mass file-level exclude the contents of the monero folder? Edit: Mass file-level exlusion did not work..

## matthewjamesr | 2021-01-16T03:12:37+00:00
@RickyRiccardo1 you have to toggle Show Hidden Folders.

![image](https://user-images.githubusercontent.com/303321/104795764-17ed5a80-57f4-11eb-85f0-ca82c1c8fd25.png)


## silenci36 | 2021-04-05T12:05:19+00:00
**@matthewjamesr** I had the same problem and this worked for me. Thanks. Just had to exclude the folder from the antivirus in order to work.

## selsta | 2021-04-21T01:35:15+00:00
Closing, if you continue to have issues with your anti virus please ask on Reddit r/monerosupport

## dotnetspec | 2021-10-12T11:18:38+00:00
Hi,
I'm getting the same error (as per title) in logs on starting up my wallet with a local node.
```
System:    Kernel: 5.4.0-88-generic x86_64 bits: 64 compiler: gcc v: 9.3.0 Desktop: Cinnamon 4.8.6 
           wm: muffin dm: LightDM Distro: Linux Mint 20.1 Ulyssa base: Ubuntu 20.04 focal
 ```
Earlier today the daemon was connecting and updating the blockchain from same machine/network connection.
I am starting the daemon from within the wallet.
I moved the blockchain to a secondary drive on the laptop to create more space on the primary drive. I changed the blockchain location to match the new location in settings.
I have tried re-booting a couple of times, but the problem persists over last 3-4 hours.
I don't have a firewall enabled.
What else can I try? thanks ...

## selsta | 2021-10-12T15:11:27+00:00
@dotnetspec 

Seeing that message is fine in logs. It only means that the wallet tried to connect to the daemon before the daemon was fully started.

What other problems do you see apart from this message?

## dotnetspec | 2021-10-13T11:17:29+00:00
I'm getting:
```
Timed out, local node is not responding after 120 seconds.
Please check your wallet and daemon log for errors. You can also try to start monerod manually.
```
in the wallet.
Network status then reverts to 'Disconnected' (so this is the problem).
I don't know how to start monerod manually in Linux, however, I'm not confident that would resolve this anyway (?).
If I can, how should I start monerod manually?
Is there any other way for me to connect the daemon?

## selsta | 2021-10-13T17:01:02+00:00
@dotnetspec Can you try to set a different blockchain location folder? If your blockchain is corrupted the daemon will fail to start.

## dotnetspec | 2021-10-15T15:23:35+00:00
> @dotnetspec Can you try to set a different blockchain location folder? If your blockchain is corrupted the daemon will fail to start.

@selsta I tried a different folder. After many hours the blockchain had re-synced again. Looked good. I opened the wallet again today and same problem. Had to reset to the default directory (on the system drive) and copy the data.mdb back to it. Works now but I've wasted a few hours trying to use a different drive to the default system drive. Not a big problem, but was hoping it would be a bit easier to move. Thanks again for your help ...

## selsta | 2021-10-15T17:09:56+00:00
The problem with external hard drives is it's easy to unplug it during sync which can result in a corrupted blockchain. I guess that's happened here?

If you have having issues with your node you can simply use a remote node from https://monero.fail

## dotnetspec | 2021-10-16T05:17:39+00:00
I didn't unplug the external drive as it was syncing. I afterwards tried on a secondary internal drive and had the same problem ... so it's not a disconnection/corruption issue. When I moved the data.mbd to a non-system drive (either external or internal) I didn't move the monerod daemon to that drive as well ... should I have?

## selsta | 2021-10-16T05:27:02+00:00
monerod and the blockchain directory can be separate.

# Action History
- Created by: RickyRiccardo1 | 2021-01-10T22:33:01+00:00
- Closed at: 2021-04-21T01:35:15+00:00
