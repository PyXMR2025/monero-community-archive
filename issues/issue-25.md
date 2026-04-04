---
title: Shell does not terminate automatically when monero-core is closed
source_url: https://github.com/monero-project/monero-gui/issues/25
author: medusadigital
assignees: []
labels: []
created_at: '2016-09-20T16:26:05+00:00'
updated_at: '2016-09-28T19:43:01+00:00'
type: issue
status: closed
closed_at: '2016-09-28T19:43:01+00:00'
---

# Original Description
if monero-core gets closed, shell doesnt terminate and stays showing the monero-core log, until exited the hard way with ctrl+q. this was different before if i remember correctly

--> Ubuntu 16.04 on mainnet together with pull request #23


# Discussion History
## radfish | 2016-09-21T02:31:16+00:00
Could you elaborate please? The shell you ran ./monero-core in? Why would it close when a process exits?


## medusadigital | 2016-09-21T22:35:21+00:00
im sorry maybe its the language. im not expecting the window i ran ./monero-core inside to close. 
but i expect the shell to return to normal usable state after gui gets closed. this doesnt happen anymore.

right now the shell i launched monero-core from looks like this after i closed the GUI:
![shellcloseist](https://cloud.githubusercontent.com/assets/17108301/18731441/32cc00f0-805c-11e6-95e6-d2be1d836b37.jpg)

But i would expect something like that (note i had to exit with ctrl+q here):
![shellclosesoll](https://cloud.githubusercontent.com/assets/17108301/18731446/41cea076-805c-11e6-8748-e6e5650af51f.jpg)

Nevertheless i didnt see the process running anymore, so the monero-core process gets killed correctly when closing the GUI it seems...part of why i somehow cant understand this behaviour. Its just the shell that keeps on showing the log i think.

i hope its clear now, definetely not so important, i just added everything that seemed strange.


## medusadigital | 2016-09-28T19:43:01+00:00
tested together with fresh monero-core build from /mbg033/monero-core, branch=develop on OS Ubuntu 16.04

works perfectly ---> closed


# Action History
- Created by: medusadigital | 2016-09-20T16:26:05+00:00
- Closed at: 2016-09-28T19:43:01+00:00
