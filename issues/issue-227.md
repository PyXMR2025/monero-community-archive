---
title: database build SIGABRT
source_url: https://github.com/monero-project/monero/issues/227
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-02-17T12:59:48+00:00'
updated_at: '2015-03-26T11:59:30+00:00'
type: issue
status: closed
closed_at: '2015-03-26T11:59:30+00:00'
---

# Original Description
Log Level 1 output:
http://pastebin.com/4AdUnESG

gdb tb:
http://pastebin.com/54zYH9rf

daemon was just sittin and doin its thing, also mining on 1 core. 

I woke up to a sigabrt.


# Discussion History
## Gingeropolous | 2015-02-17T13:50:22+00:00
tried to restart within gdb, didn't work. Then I couldn't restart because there were things running ... didn't copy the notification. Ended up killing the power (take THAT SSD!!!) in order to reboot it. 

After reboot, loaded fine. 


## fluffypony | 2015-03-26T11:59:30+00:00
Fixed in upstream


# Action History
- Created by: Gingeropolous | 2015-02-17T12:59:48+00:00
- Closed at: 2015-03-26T11:59:30+00:00
