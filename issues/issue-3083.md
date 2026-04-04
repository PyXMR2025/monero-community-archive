---
title: restricted-rpc-bind-port and rpc-bind-port with user not compatible
source_url: https://github.com/monero-project/monero/issues/3083
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-01-08T04:51:27+00:00'
updated_at: '2024-08-24T14:19:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have the following config file

```
main12@main12-kvm:~$ cat /etc/monerod.conf 
confirm-external-bind=1
rpc-bind-ip=0.0.0.0
rpc-bind-port=18081
rpc-restricted-bind-port=18089
log-level=1
limit-rate=50000
start-mining=mining_address
fluffy-blocks=1
rpc-login=user:pass
```

and when I try to connect

```

main12@main12-kvm:~$ monerod --rpc-bind-port 18089 print_height
2018-01-08 04:48:32.009	    7ff608710740	ERROR	net.http	contrib/epee/include/net/http_client.h:421	Client has incorrect username/password for server requiring authentication
Error: Couldn't connect to daemon: 127.0.0.1:18089

```

So even though I have 18089 on the restricted port (but open), its still wanting me to provide login information. 

I expected it to function where the 18089 port is just passed through the user / pass stuff, and the anything that is not restricted would require the login.
  

# Discussion History
## Gingeropolous | 2018-01-08T04:53:08+00:00
So right now the only way to truly protect an RPC port that I could get info from is to use a port that hopefully won't be scanned. 

## moneromooo-monero | 2018-01-08T08:43:28+00:00
I don't get it. You set a user/password but want to not use it to login ? Why can't you just use that password ?

## Gingeropolous | 2018-01-08T12:56:31+00:00
I want to offer the remote node on 18089 to *anyone*, but I also want to be able to access it myself on 18081 with my user and login.

But with that above config file, I would need the user and login on 18089. 

## moneromooo-monero | 2018-01-08T13:56:54+00:00
Ah, makes sense. You want to access it from the outside (because if not, don't let the firewall allow that port) ?

## Gingeropolous | 2018-01-08T14:42:01+00:00
aaaah well yes , the firewall option would be logical...

but indeed, if I wanted to access it from the outside, then the current system wouldn't allow that... although I guess I could do some tunneling or something.....

## vtnerd | 2018-01-08T16:47:00+00:00
So you want to listen on 2 ports, one which is restricted, and the other which is not? And the login would apply to both?

## Gingeropolous | 2018-01-08T19:33:17+00:00
@vtnerd 

I want to listen on 2 ports, one which is restricted, and the other is not. The login is only applied to the one that is not restricted. 

## vtnerd | 2018-01-09T17:28:16+00:00
OK, so I thought of a solution that _hopefully_ won't wreck things too much:

`--rpc-restricted-bind-port 18009,user:pass --rpc-bind-port 500`

Basically, after a port in [0,655235] an optional "," is allowed for specifying user:pass. The least intrusive method I've come up with.

## vtnerd | 2018-01-09T17:29:09+00:00
Oh and this syntax would "override" the global settings.

## Gingeropolous | 2018-01-10T03:13:46+00:00
so, this would also be possible

```
--rpc-restricted-bind-port 18009 --rpc-bind-port 500,user:pass
```

because having a user pass on the restricted port is.... not necessary

## shermand100 | 2019-12-11T11:03:08+00:00
@moneromooo-monero 
Has there been any progress with this? I'm running into the same issue.

My usage:

Running monerod with

`./monerod --rpc-bind-ip=192.168.1.101 --rpc-bind-port=18082 --rpc-restricted-bind-port=18081 --confirm-external-bind --rpc-login=user:pass`

But monerod seems to require those rpc login credentials on both ports. Am I not using this correctly?

## moneromooo-monero | 2019-12-18T03:05:50+00:00
Not as far as I know.

## Gingeropolous | 2019-12-18T12:26:45+00:00
@shermand100 , im surprised this runs. isn't 18082 reserved for 0MQ?

## shermand100 | 2019-12-18T17:02:41+00:00
@Gingeropolous , Just ran it again to be sure but on a Raspberry Pi 3 running the latest Raspbian Buster:

`./monerod --rpc-bind-ip=192.168.1.105 --rpc-restricted-bind-port=18081 --rpc-bind-port=18082 --rpc-login=user:pass --confirm-external-bind  --rpc-ssl disabled`

Successfully runs the monero daemon.
However I'm having the same issue of both the `--rpc-restricted-bind-port=18081` and `--rpc-bind-port=18082` require rpc-login=user:pass to access info about the running node.

If it helps understand why I'm trying to do this, it's for the --rpc-restricted-bind-port to be public and use the new --rpc-payment-### options, whilst having an un-restricted internal port to feed node info to a user interface which restricted wont provide, print_cn, start/stop the node etc


Edit:
~~With the janky use of some if statements in my scripts I think I can work around this issue.~~

Edit 2:
Nope. Then I figured that by using a `--rpc-bind-port=18084` and `--rpc-restricted-bind-port=18081`  and NOT specifying any login credentials I could keep the un-restricted port behind my firewall. This works on a node without `--rpc-payment-###` options. However when I start with payment options enabled I get the error:

`E RPC payment enabled, but server is not restricted, anyone can adjust their balance to bypass payment`

## moneromooo-monero | 2019-12-21T17:54:16+00:00
Does https://github.com/monero-project/monero/pull/6260 help ?


## shermand100 | 2019-12-21T20:21:52+00:00
With reference to #6260, yes that could help.

To work I assume I would use `--rpc-bind-ip=0.0.0.0` to have both loopback and external connections.

Then `--rpc-restricted-bind-port=18081` and `--rpc-bind-port=18084` with added `--rpc-payment-allow-free-loopback`

Ths would only help if it prevents the  `E RPC payment enabled, but server is not restricted, anyone can adjust their balance to bypass payment` error


## moneromooo-monero | 2019-12-21T21:32:22+00:00
Specifying both --rpc-bind-port and --restricted-rpc-bind-port along side RPC payment and --rpc-payment-allow-free-loopback starts the daemon, no such error.

## shermand100 | 2019-12-22T00:00:04+00:00
Thanks, that's great that it gives me a work around for the project I'm working on. I think the title of this issue has been side stepped here but a working solution is still a working solution!

## omurad | 2021-01-04T02:14:00+00:00
Would love to see this implemented

## 0b100100 | 2021-12-05T17:29:31+00:00
How about automatically disabling the RPC login for the restricted bind port when `public-node=1` is in use?

## ahmafi | 2023-02-01T20:47:27+00:00
I would also like to see this. Using a user:pass on the restricted and public RPC node doesn't make sense. I want the user:pass only for myself on non-restricted port.

## thisIsNotTheFoxUrLookingFor | 2024-07-28T06:44:53+00:00
> I would also like to see this. Using a user:pass on the restricted and public RPC node doesn't make sense. I want the user:pass only for myself on non-restricted port.

Same for me, this is madness, set user:pass on full RPC, leave restricted RPC open for public to consume as it's (I assume) most used purpose

## thisIsNotTheFoxUrLookingFor | 2024-07-28T06:50:57+00:00
> OK, so I thought of a solution that _hopefully_ won't wreck things too much:
> 
> `--rpc-restricted-bind-port 18009,user:pass --rpc-bind-port 500`
> 
> Basically, after a port in [0,655235] an optional "," is allowed for specifying user:pass. The least intrusive method I've come up with.

Throws exception now, seems it is no longer allowed to do this, at least not from config file as `rpc-restricted-bind-port=18009,user:pass` monerod throws exception starting up when doing this

## thisIsNotTheFoxUrLookingFor | 2024-08-22T17:50:59+00:00
Curious, if we diable user:pass and expose public RPC but firewall the private (full) RPC to local network, if I assume a worst case scenario where my network is pwned and they start smashing my full RPC with no auth, what am I looking at as possible damage from that? There is no wallet functionality or any keys around my monerod, I am just connecting to it from wallet on other devices.

## omurad | 2024-08-23T01:49:30+00:00
Here's the [list of RPC commands](https://getmonero.dev/interacting/monerod.html#commands). It seems the worst that can happen is the attacker uses your node's CPU to mine for their wallet.

## thisIsNotTheFoxUrLookingFor | 2024-08-24T14:19:10+00:00
> Here's the [list of RPC commands](https://getmonero.dev/interacting/monerod.html#commands). It seems the worst that can happen is the attacker uses your node's CPU to mine for their wallet.

Looks like also they can faf with things like max in/out peers etc. but yah that's all stuff I can tolerate if it happens, cool.

# Action History
- Created by: Gingeropolous | 2018-01-08T04:51:27+00:00
