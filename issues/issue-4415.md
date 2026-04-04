---
title: 'Error starting server: bind: Cannot assign requested address'
source_url: https://github.com/monero-project/monero/issues/4415
author: dawiepoolman
assignees: []
labels: []
created_at: '2018-09-22T12:37:07+00:00'
updated_at: '2018-09-22T14:02:39+00:00'
type: issue
status: closed
closed_at: '2018-09-22T14:02:39+00:00'
---

# Original Description
Hi guys

w.r.t setup guide [here](https://pinode.weebly.com/monero-node-for-pi-3-or-armv7-devices-no-lcd-display.html)

I am trying to launch monerod for the first time on my RPi3B+ and binding my laptop over ssh to port 4008 with cmd:

./monero-v0.12.3.0/monerod --rpc-bind-ip=192.168.1.22 --rpc-bind-port=4008 --confirm-external-bind

I get error:

FATAL net contrib/epee/include/net/abstract_tcp_server2.inl:849 Error starting server: bind: Cannot assign requested address

Any ideas why my laptop from where I ssh into the pi cant seem to get its IP assigned?  Any port fwd required on my router (sounds unlikely on the LAN)?

Thx


# Discussion History
## moneromooo-monero | 2018-09-22T12:59:10+00:00
Are you sure 192.168.1.22 is the IP assigned to a local interface you are allowed to bind to ?
Does "ifconfig" confirm ?


## dawiepoolman | 2018-09-22T13:07:28+00:00
Hi moneromoo
Indeed it does:
![image](https://user-images.githubusercontent.com/2351212/45917517-2ff97d00-be79-11e8-96ee-631fbfab40c8.png)



## moneromooo-monero | 2018-09-22T13:14:47+00:00
Can you bind any other daemon to that IP address from the same user account ?

## dawiepoolman | 2018-09-22T13:23:05+00:00
Interesting question.
Since it is a brand new RPi3 setup, the answer is no/idk.  How would I test such an alternative without maybe installing a shitcoin :P ?
 
I do have another separate RPi3 with a btc-lnd node running though. Not sure that is of relevance though since it is a separate setup.

## moneromooo-monero | 2018-09-22T13:29:39+00:00
You'd install something like a small http server that your distro knows about for instance, and hope they have a way to bind to a specific address.

## dawiepoolman | 2018-09-22T13:36:46+00:00
Ty, while I try and Google like the noob I am to this, herewith a full screenshot of the error just to make sure I am not missing anything else that might be obvious:
![image](https://user-images.githubusercontent.com/2351212/45917792-1fe39c80-be7d-11e8-9ac0-f23ab645e5d4.png)


## moneromooo-monero | 2018-09-22T13:47:10+00:00
Try: nc -l 192.168.1.22 4008

## dawiepoolman | 2018-09-22T13:48:52+00:00
nc: Cannot assign requested address

## iDunk5400 | 2018-09-22T13:49:48+00:00
I might be missing something here, but why are you trying to bind monerod on your Pi to your Windows laptop address ?

## dawiepoolman | 2018-09-22T13:52:52+00:00
I preferably want the gui (and wallet) to live client side on my laptop like the installation instructions in the op post

## iDunk5400 | 2018-09-22T13:54:01+00:00
But you need to bind monerod on your Pi to your Pi IP, not your Windows laptop IP.

## dawiepoolman | 2018-09-22T13:59:19+00:00
Thank you!
It works now.  I guess the guide was ambiguous when it said:

 To run the node for the first time type

                             ./monero-v0.12.3.0/monerod --rpc-bind-ip=192.168.XX.XX --rpc-bind-port=4008 --confirm-external-bind

​**Where XX.XX is the IP address you have been using to SSH to the Pi.   

## iDunk5400 | 2018-09-22T14:00:55+00:00
Yes, not the source address you're sshing from, but the destination address you're sshing to :)

## dawiepoolman | 2018-09-22T14:02:39+00:00
Facepalm.  Makes sense now ty.  Sorry for posting this drama.
So I learn every day.  You guys were super responsive.
Thx again.  Amazing community.  

# Action History
- Created by: dawiepoolman | 2018-09-22T12:37:07+00:00
- Closed at: 2018-09-22T14:02:39+00:00
