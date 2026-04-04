---
title: Monero GUI on Win 10 64 needs computer reboot after opening then closing the
  application to reopen again.
source_url: https://github.com/monero-project/monero-gui/issues/1355
author: Simplexletalis
assignees: []
labels: []
created_at: '2018-04-25T13:41:49+00:00'
updated_at: '2018-04-26T23:43:17+00:00'
type: issue
status: closed
closed_at: '2018-04-26T19:41:13+00:00'
---

# Original Description
Could not find a similar issue on this, so thought I'd open a new one.

After opennig the Monero wallet and using it, then closing and trying to re-open the GUI, the application crashes right away. A reboot solves the problem and the wallet can open again until being closed.

My tests were on Windows 10 x64. 

# Discussion History
## Simplexletalis | 2018-04-25T14:23:17+00:00
Event 1000, practically useless information but it's what shows in Event viewer when this occurs. This is on 12.0 directly from getmonero.

```
Faulting application name: monero-wallet-gui.exe, version: 0.0.0.0, time stamp: 0x5ac38fb4
Faulting module name: unknown, version: 0.0.0.0, time stamp: 0x00000000
Exception code: 0xc0000005
Fault offset: 0x0000000000000000
Faulting process id: 0x1de4
```

## pazos | 2018-04-25T14:43:45+00:00
@Simplexletalis: thanks for reporting. Since windows qt applications don't print anything on console could you please try installing https://docs.microsoft.com/es-es/sysinternals/downloads/debugview and running the program while the debugger is open? both on normal operation and when the app crashes

## Simplexletalis | 2018-04-25T17:33:31+00:00
```

> 	
> 00000050	87.81632996	[10320] app startd	
> 00000051	87.81814575	[10320] available width:  1690	
> 00000052	87.81819916	[10320] available height:  914	
> 00000053	87.81823730	[10320] devicePixelRatio:  1	
> 00000054	87.81824493	[10320] screen height:  1690	
> 00000055	87.81826782	[10320] screen width:  944	
> 00000056	87.81829071	[10320] screen logical dpi:  96	
> 00000057	87.81834412	[10320] screen Physical dpi:  95.9709	
> 00000058	87.81835175	[10320] screen calculated ratio:  0.749772	
> 00000059	88.11286926	[10320] qml: check next false	
> 00000060	88.11291504	[10320] qml: Checking seed	
> 00000061	88.13558197	[10320] qml: check next false	
> 00000062	88.13561249	[10320] qml: Checking seed	
> 00000063	88.13607025	[10320] qml: check next false	
> 00000064	88.14299011	[10320] qml: check next false	
> 00000065	88.48274994	[10320] libpng warning: iCCP: known incorrect sRGB profile	
> 00000066	88.86764526	[10320] libpng warning: iCCP: known incorrect sRGB profile	
> 00000067	88.99408722	[10320] qml: transfer page loaded	
> 00000068	88.99610901	[10320] qml: PrivacyLevel changed:0	
> 00000069	88.99614716	[10320] qml: mixin count: 6	
> 00000070	89.09759521	[11752] Lizard Mode: Priviledged process	
> 00000071	89.12969971	[10320] qml: qrScannerEnabled disabled	
> 00000072	89.13199615	[10320] file:///C:/Program Files/Monero/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"	
> 00000073	89.13233185	[10320] Checking for updates	
> 00000074	89.18630219	[11752] Lizard Mode: Reverting to default M/KB Configuration	
> 00000075	94.27275085	[11752] Lizard Mode: Unpriviledged process	
> 00000076	94.27291107	[11752] Lizard Mode: Restoring app mapping	
> 

```

## Simplexletalis | 2018-04-25T17:52:23+00:00
Ran as administrator.

## gene-telligent | 2018-04-25T21:09:37+00:00
Weird question -- are you using a Steam Controller as your primary input? A nonstandard input like that might cause some issues with Qt.

## Simplexletalis | 2018-04-25T21:27:32+00:00
I have a corsair scimitar mouse, IBM Model M keyboard and a corsair void wireless headset. Those are the only devices connected to my PC.

## Simplexletalis | 2018-04-26T17:37:28+00:00
I need to test further but I think this might have something to do with remote desktop being used to access the PC and opening the wallet.

## pazos | 2018-04-26T19:24:58+00:00
@Simplexletalis: I find nothing wrong in the gui process you attached (10320). As you can see there is another process running which seems a bit fishy to me. If you installed a trusted(by you) 3rd party software like Steam and it is running in the background it can be polling for non standard inputs to trigger certain events. If you didn't install and run Steam it *could* be a keylogger.

I am lucky enough to don't have to deal with Windows 10 and I'm not a big Windows fan either. So I might to be wrong.

> Ran as administrator

You shouldn't run the gui as an administrator.


> I think this might have something to do with remote desktop being used to access the PC and opening the wallet.

In that case the software shouldn't run at all (unless started with start-low-graphics-mode.bat)

You could check for the file monero-wallet-gui.log in the same folder as the binary to see if it contains some errors.

## Simplexletalis | 2018-04-26T19:41:13+00:00
Starting the normal wallet-gui would still fail after closing everything else.

Started it with the low graphics bat in as non administrative and it works.

# Action History
- Created by: Simplexletalis | 2018-04-25T13:41:49+00:00
- Closed at: 2018-04-26T19:41:13+00:00
