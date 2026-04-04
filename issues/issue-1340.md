---
title: JSON-RPC protection
source_url: https://github.com/monero-project/monero/issues/1340
author: 3junit
assignees: []
labels: []
created_at: '2016-11-14T10:48:49+00:00'
updated_at: '2016-11-15T14:48:09+00:00'
type: issue
status: closed
closed_at: '2016-11-15T14:48:09+00:00'
---

# Original Description
Hello. I have multy wallet system that work with monero too via JSON-RPC. Monero work on separated server. There is any way to set up allow ip for rpc or not? Like in bitcoin. 

# Discussion History
## ghost | 2016-11-14T11:44:28+00:00
If you type monero --help in the console you'll see the command to bind to an RPC address:port


## 3junit | 2016-11-14T13:06:07+00:00
Well, thats is the problem. If i know this address:port i can do what i want! With simple curl! In bitcoin you have rpc user\password protection + allowip function for rpc. So you cant simply send curl and do commands.


## moneromooo-monero | 2016-11-15T11:57:41+00:00
There is no authentication nor encryption for RPC. If you want to do that, for now you need to tunnel through ssh.


## 3junit | 2016-11-15T14:48:09+00:00
Thank you, Will do tunnel via autossh 


# Action History
- Created by: 3junit | 2016-11-14T10:48:49+00:00
- Closed at: 2016-11-15T14:48:09+00:00
