---
title: monerod.exe failed to load ver win64
source_url: https://github.com/monero-project/monero-gui/issues/642
author: keatond
assignees: []
labels: []
created_at: '2017-03-29T22:39:07+00:00'
updated_at: '2017-03-30T13:34:10+00:00'
type: issue
status: closed
closed_at: '2017-03-30T13:34:10+00:00'
---

# Original Description
Good Evening Everyone,

I was told to come here to add an issue that I encountered within the win 64bit version of Beta 2. When you load the GUI application it says it is starting demon then will fail with the statement "Please check your wallet and daemon log for errors. You can also try to start monerod.exe manually.". 

After i click OK on the failed start message, the bottom left status message will say "Connected" and the process monerod.exe will be running within the Task Manager.  

When I go to the settings tab it will show that the daemon is not running. The "Start daemon" is bold and the "Stop daemon" is grey'd out.
[bitmonero.zip](https://github.com/monero-project/monero-core/files/880573/bitmonero.zip)



# Discussion History
## medusadigital | 2017-03-30T07:29:33+00:00
Hi, is it possible there is a space in the path where monerod.exe is stored? 

## ParsifalX | 2017-03-30T07:59:14+00:00
I had the same issue with @keatond where i could see monerod.exe running in the task manager even though GUI reported that the daemon failed to start.
I confirm that the issue was solved when i moved the folder to a path without spaces.

## keatond | 2017-03-30T10:58:45+00:00
Looks like you guys were correct. My folder was named "Monero GUI 2" and when changed to "MoneroGui2" everything loaded fine.

# Action History
- Created by: keatond | 2017-03-29T22:39:07+00:00
- Closed at: 2017-03-30T13:34:10+00:00
