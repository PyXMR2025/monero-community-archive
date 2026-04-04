---
title: 'moneronod '
source_url: https://github.com/monero-project/monero/issues/9658
author: XJIeb
assignees: []
labels:
- question
created_at: '2024-12-27T07:17:44+00:00'
updated_at: '2025-02-19T17:37:22+00:00'
type: issue
status: closed
closed_at: '2025-02-19T17:37:21+00:00'
---

# Original Description
Run moneronod with log level 3 
conf file
rpc-bind-ip=241.42.75.82 #(this is example ip from zerotier because i cant open ports)
rpc-bind-port=18081
confirm-external-bind=true
rpc-login=LOGIN:PASSWORD
log-level=3
db-sync-mode=fast
data-dir=M:\untitled

after this i bought ubuntu server to connect with rpc

this conf ubuntu
data-dir=/root/monero_data
rpc-bind-ip=281.42.491.761 #(this is example ip from zerotier because i cant open ports)
rpc-bind-port=18081
rpc-login=LOGIN:PASSWORD
confirm-external-bind=true
p2p-bind-ip=281.42.491.761
p2p-bind-port=18080
bootstrap-daemon-address=241.42.75.82:18081
bootstrap-daemon-login=LOGIN:PASSWORD
log-level=3
db-sync-mode=fast


Now i have node on Win if i want to check status it says 
2024-12-27 01:41:41.428 I Monero 'Fluorine Fermi' (v0.18.1.1-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081

same on ubuntu
telnet from ubuntu to win is succesful but if i wanna make curl http://281.42.491.761/get_info --user LOGIN:PASSWORD
it says
<html><head><title>Unauthorized Access</title></head><body><h1>401 Unauthorized</h1></body></html> 

for me will be cool to rpc connect with my windows node on log lvl 3

Mb i can make thsi from gui on windows not with moneronod on windows? 
but what flags or params i need>? 
maybe somebody can explain me 
![image](https://github.com/user-attachments/assets/67b79f2e-63c0-44ea-869e-3f322c45bfa3)

I wanna make 2 moneronod with log lvl 3 and 0.18.1.1 version 
1 ubuntu server and 1 windows my pc 



# Discussion History
## jeffro256 | 2024-12-27T19:55:21+00:00
> same on ubuntu
> telnet from ubuntu to win is succesful but if i wanna make curl http://281.42.491.761/get_info --user LOGIN:PASSWORD
> it says
> <title>Unauthorized Access</title>

If you want to use the `curl` command for password-protected Monero RPC, you need to pass the `--digest` flag. So your command would look like this: `curl http://281.42.491.761/get_info --user LOGIN:PASSWORD --digest`

> Error: Couldn't connect to daemon: 127.0.0.1:18081

127.0.0.1 is the "loopback" IP address, AKA the IP address that designates "this computer". All computers will reference themselves as 127.0.0.1, but you can't actually use that as an address if you want to connect to a *different* computer. If your node is on a different computer, you will need an actual address that isn't 127.0.0.1. 



## XJIeb | 2024-12-28T02:04:09+00:00
> > same on ubuntu
> > telnet from ubuntu to win is succesful but if i wanna make curl http://281.42.491.761/get_info --user LOGIN:PASSWORD
> > it says
> > <title>Unauthorized Access</title>
> 
> If you want to use the `curl` command for password-protected Monero RPC, you need to pass the `--digest` flag. So your command would look like this: `curl http://281.42.491.761/get_info --user LOGIN:PASSWORD --digest`
> 
> > Error: Couldn't connect to daemon: 127.0.0.1:18081
> 
> 127.0.0.1 is the "loopback" IP address, AKA the IP address that designates "this computer". All computers will reference themselves as 127.0.0.1, but you can't actually use that as an address if you want to connect to a _different_ computer. If your node is on a different computer, you will need an actual address that isn't 127.0.0.1.

`curl http://281.42.491.761/get_info --user LOGIN:PASSWORD --digest `
reply is empty BUT if

`curl http://281.42.491.761:18082/get_info --user LOGIN:PASSWORD --digest `
 reply  Failed to connect to 281.42.491.761 port 18082 after 32 ms: Connection refused

`curl http://281.42.491.761:18081/get_info --user LOGIN:PASSWORD --digest `
Unauthorized Access</title></head><body><h1>401 Unauthorized</h1></body></html>

AND FINALLY 
 `curl http://281.42.491.761:18080/get_info --user LOGIN:PASSWORD --digest `
 curl: (52) Empty reply from server 
 
 I`m waiting reply with some json that proof about my rpc connection between ubuntu and win 
 
 Now im waiting like 5 or 6 days about log lvl 3 sync 
 Do u know what flags or params i need to start monerod from GUI 
 because now my cmd on win run with `moneronod --config-file moneronod.conf` 
 and ubuntu same like windows conf are above. 
 My question is simple. I want to check what is % of my sync to lvl 3 now ?

## jeffro256 | 2025-01-05T08:00:30+00:00
Is this IP address a local IP address or a remote IP address? This feels like an invalid network setup after looking at it for a while. And are those the complete config files? Are you sure that the username/password combinations are correct? 

## jeffro256 | 2025-01-06T18:26:34+00:00
If you are still having troubles, I would recommend joining the #Monero-support room on the matrix.monero.social Matrix server. A live chat room to discuss this specific issue will probably be more fruitful than on GIthub. 

## selsta | 2025-02-19T17:37:21+00:00
Closing due to inactivity.

# Action History
- Created by: XJIeb | 2024-12-27T07:17:44+00:00
- Closed at: 2025-02-19T17:37:21+00:00
