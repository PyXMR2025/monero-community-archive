---
title: 'Bug using IPV6 '
source_url: https://github.com/monero-project/monero-gui/issues/2971
author: luisan00
assignees: []
labels: []
created_at: '2020-06-27T14:58:33+00:00'
updated_at: '2020-07-08T18:52:34+00:00'
type: issue
status: closed
closed_at: '2020-07-08T18:52:34+00:00'
---

# Original Description
### How to replicate it

#### Setup in the remote daemon is:
- daemon version: `monero-x86_64 linux-gnu-v0.16.0.0`
- IP address: `fc00:db9::1` 
```
# monerod.conf
public-node=1
rpc-use-ipv6=1
rpc-bind-ip=0.0.0.0                                         
rpc-bind-ipv6-address=::0                                     
rpc-restricted-bind-port=18089  
confirm-external-bind=1
```
#### In my computer:
- GUI version: `monero-x86_64 linux-gnu-v0.16.0.0`
- IP address: `fc00:db8::1`

#### Steps: 

- Run the GUI
- Click on `Remote Node` under `node` tab
- Set address to:  `[fc00:db9::1]`, port to: `18089` and click on `connect`

The connection seems successful, but the fields `address` and `port` are not showing the right info, so please look at the screen capture.

![image](https://user-images.githubusercontent.com/10358374/85338460-9e51f000-b4e2-11ea-8c57-d49df11adc1f.png)

**Note**: if we put the address without `[]`, the connection doesn't seem to be successful 
 


# Discussion History
# Action History
- Created by: luisan00 | 2020-06-27T14:58:33+00:00
- Closed at: 2020-07-08T18:52:34+00:00
