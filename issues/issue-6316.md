---
title: Usage question/problem
source_url: https://github.com/monero-project/monero/issues/6316
author: braindamagedjustnow
assignees: []
labels: []
created_at: '2020-02-06T06:57:43+00:00'
updated_at: '2020-04-01T09:53:26+00:00'
type: issue
status: closed
closed_at: '2020-04-01T09:53:26+00:00'
---

# Original Description
How is one supposed to use "--seed-node" command?
I've tried different ways and none seems to work.
I've tried with Windows 10 and 7. Monerod and GUI running as admin and not etc.
When I run the command from the GUI I usually get:

[2/5/2020 10:53 PM] 2020-02-06 06:52:54.203 I Monero 'Carbon Chamaeleon' (v0.15.0.1-release) 
2020-02-06 06:52:54.203 I Initializing cryptonote protocol... 
2020-02-06 06:52:54.203 I Cryptonote protocol initialized OK 
2020-02-06 06:52:54.203 I Initializing core... 
2020-02-06 06:52:54.203 I Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ... 
2020-02-06 06:52:54.998 I Loading checkpoints 
2020-02-06 06:53:01.107 I Core initialized OK 
2020-02-06 06:53:01.107 I Initializing p2p server... 
2020-02-06 06:53:02.371 F Error starting server: Failed to bind IPv4 (set to required) 
2020-02-06 06:53:02.371 I Deinitializing core... 
2020-02-06 06:53:02.391 I Stopping cryptonote protocol... 
2020-02-06 06:53:02.391 I Cryptonote protocol stopped successfully 
2020-02-06 06:53:02.391 E Exception in main! Failed to initialize p2p server.

# Discussion History
## dEBRUYNE-1 | 2020-02-09T10:16:51+00:00
Can you post the full exact command you are trying to utilize? 

## braindamagedjustnow | 2020-02-09T16:09:08+00:00
From the GUI I go to settings then on log I type:
--seed-node 192.168.1.1
I am using another IP of course.

I also tried it with the monerod.exe as a startup command 

## trasherdk | 2020-02-09T18:05:52+00:00
More often than not, the `Failed to bind IPv4` means something is using the port already.

## braindamagedjustnow | 2020-02-10T07:58:27+00:00
Well I also tried running it on a clean VM so it's confusing 

## trasherdk | 2020-02-10T09:12:33+00:00
Or trying to connect to a non existing or firewalled ip-address/port

## braindamagedjustnow | 2020-02-10T18:06:34+00:00
I've also tried with couple of IPs labeled as white which I get from "print_pl" 

## ndorf | 2020-02-11T01:24:10+00:00
--seed-node is an option, not a command. Without a command, you are attempting to start a second instance of the daemon, which fails because another one is already running and using the local ports.
 It should work if you stop the main daemon first, then run it with the option. In this mode it will exit after getting the peerlist, after which you can start the main daemon again.

## braindamagedjustnow | 2020-02-12T08:05:38+00:00
So from CMD running:
"monerod --data-dir D:\Monero\ --seed-node 192.168.1.1"

should do the job?



## trasherdk | 2020-02-12T12:14:58+00:00
You probably want `monerod --data-dir D:\Monero --seed-node 192.168.1.1`

## braindamagedjustnow | 2020-02-15T10:34:43+00:00
Well I still think something is wrong.
I delete p2pstate.bin and then I start the monerod with the following options:
monerod --data-dir D:\Monero --seed-node 192.168.1.1
I use IP labeled as white in print_pl
So I print the peers list with print_pl and save the output to a txt file.
Then I delete the p2pstate.bin again and start the same command with the same IP.
Then I print the peers list and save it to another text file.
Theoretically I should get the same peers list since I am getting in from same source but I am getting different lists? 

## moneromooo-monero | 2020-03-30T13:41:19+00:00
Why do you think the same source should give you the same list ?

## braindamagedjustnow | 2020-03-31T16:24:40+00:00
> 
> 
> Why do you think the same source should give you the same list ?

Theoretically I should get the same peers list since I am getting in from same source - isn't this correct? It's not like the node is making up some ips and sending them up. It has a list with known white and grey ips and it should send that list when asked. Or I am just missing something.  

## moneromooo-monero | 2020-03-31T17:17:57+00:00
This it not correct. You should expect a different list from the same peer.

## braindamagedjustnow | 2020-04-01T09:53:26+00:00
Well although I can't understand the logic behind this I guess I'll close the issue. Thank you moneromooo-monero!

# Action History
- Created by: braindamagedjustnow | 2020-02-06T06:57:43+00:00
- Closed at: 2020-04-01T09:53:26+00:00
