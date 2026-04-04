---
title: monerod fails to start after install or on windows startup when installed as
  windows service
source_url: https://github.com/monero-project/monero/issues/8560
author: zubair72
assignees: []
labels:
- bug
- low priority
- reproduction needed
- more info needed
created_at: '2022-09-09T20:15:22+00:00'
updated_at: '2024-01-07T04:35:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Steps to reproduce error

 1.  Run windows elevated command
 2.  Switch to path where monerod.exe is located
 3.  Type monerod --install-service --data-dir DataLocation --other-command-line-options
 4.  After successful install service message appears try to start the service its fails to start
 5. If you mark the service to start at windows startup it does not start and and log error in windows system event

Note: Make sure before performing 5 steps monero-wallet-gui was not run and daemon was not started from monero-wallet-gui. If done so then issue does not appear.

Note 2: If monerod was run from elevated command prompt prior performing 5 steps issue does not appear again.

Summary: If monerod is run from monero-wallet-gui or from elevated command prompt at least once issue does not appear, as soon as you mark the service to start automatic, and restart windows you shall notice the service failed to start.

# Discussion History
## zubair72 | 2022-09-22T05:35:34+00:00
Anyone looking into this?

## selsta | 2022-10-02T19:47:21+00:00
Not yet, I'm not a Windows user myself, but I will ask someone who might look into it.

## rbrunner7 | 2022-10-03T18:12:28+00:00
I tried to reproduce any of the issues and failed completely. Or, in other words, for me everything worked flawlessly throughout.

After installing I had no problem to start the service. Setting the service to *Automatic* and restarting Windows worked, the Monero service started without any problems. GUI wallet could connect to the daemon running as a service. All the service-controlling options like `--start-service` or `--stop-service` worked, from an elevated command prompt.

I use Windows 10 Pro, 21H2. I tested with the 64bit Windows installer version of the GUI wallet, with the daemon at version v0.18.1.0-release. I have no AV software running beyond Windows standard defender.

I don't have a good idea how to proceed from here, only the almost trivial question: Do you have AV software running that could interfere? And if yes, did you already try to take it out of the picture i.e. pause it or at least define exceptions for the Monero software?

## zubair72 | 2022-10-05T17:18:13+00:00
I am using very same OS vesion Windows 10 Enterprise, 21H2 and daemon version v0.18.10 with no antivirus installed except widows standard protection and added the exclusion to folder where daemon is saved. Looks like I need to get a machine clean install and test.


## kcid123 | 2024-01-04T17:30:15+00:00
I have this exact issue right now and can provide images and video to support if anyone can help that'd be amazing.
![2024-01-04](https://github.com/monero-project/monero/assets/155665988/c7204bc8-1530-4610-b273-9c86a73a1fd8)


## 0xFFFC0000 | 2024-01-07T04:35:27+00:00
The picture you posted just says the executable file is missing. Nothing more. 

# Action History
- Created by: zubair72 | 2022-09-09T20:15:22+00:00
