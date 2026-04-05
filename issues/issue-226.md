---
title: SSL/TLS support
source_url: https://github.com/xmrig/xmrig/issues/226
author: zDEATHz
assignees: []
labels:
- enhancement
created_at: '2017-11-28T10:36:11+00:00'
updated_at: '2018-09-22T05:59:51+00:00'
type: issue
status: closed
closed_at: '2018-09-22T05:59:51+00:00'
---

# Original Description
Hello,

I am very glad to use your miner, thank you to your software!
Please, can you add a SSL/TLS support? It will be perfect.

Best regards,
E.V.

# Discussion History
## mxjoe | 2018-01-17T14:03:28+00:00
Is SSL/TLS support anywhere near? Currently I am using Claymore's solution but I would like to switch.

## moralrebuild | 2018-04-18T03:33:20+00:00
This is a must have feature for the sake of poor miners' security and privacy. XMRIG has nice self tuning capability but lacking TLS comparing with more popular alternative xmr-stak. 

## aleqx | 2018-04-22T01:39:37+00:00
Adding my vote. I just posted a new issue about this as I didn't find this one at first.

A lot of miners definitely want SSL and are already using SSL (via xmr-stak). Major pools support it, see supportxmr, hashvault, nanopool, etc ...

@xmrig, you'd be getting more income via the fee/donations if you added SSL. Many SSL miners who currently use xmr-stak because of SSL would switch to xmrig.

## ariadarkkkis | 2018-04-22T13:11:03+00:00
use xmrigCC with TLS support instead
Its only for CPU for now but I think the developer can fork GPU version with TlS and other awesome features.
@bendr0id
https://github.com/Bendr0id/xmrigCC

## aleqx | 2018-04-22T14:39:47+00:00
I took a look at xmrigCC and that is not an SSL client (doesn't support SSL). It seems it just sets up a local SSL proxy which connects to the SSL server, and then you connect xmrig to this local SSL proxy.

I can already do all that with stunnel + xmrig. That doesn't mean that xmrig supports SSL. A system admin can still sniff and mangle the packets xmrig sends to the loopback interface before they are SSL encrypted.

The request in this thread is for a true SSL support in the xmrig client, like xmr-stak, i.e. xmrig to be an actual SSL client. For that xmrig needs to use ssl calls (preferably with the SSL library statically compiled).

p.s. I do like the idea behind xmrigCC though, for remotely controlling xmrig instances, so thanks for the pointer :)

## Bendr0id | 2018-04-22T16:03:23+00:00
Hi alexq,

It seems that you either did not read carefully or misunderstood something. XMRigCC isn't and hasn't any proxy features. It is a full SSL/TLS client exactly like xmr-stak with an optional remote control feature. No local loopback device or tunneling is involved. It does end-to-end TLS for the whole communication with the pool.

The client uses Boost::asio which is statically linked against OpenSSL and adds a C++ Wrapper ontop of the OpenSSL calls. OpenSSL libs are part of my dependency package, or you compile it on your own.

My binaries already contain everything needed to use full TLS.

And also the optional remote control feature is full end-to-end encrypted when you enable it in the config.



## aleqx | 2018-04-22T18:53:05+00:00
@Bendr0id But that's not what your Howto is showing: https://github.com/Bendr0id/xmrigCC/wiki/tls ... unless I misread it.

It seems you need to first launch a server locally, which connects to the pool with SSL, and then you connect the miner to the local server unsecured. I want to connect the miner directly to the pool with SSL (not via any server/proxy).

What am I missing?

## Bendr0id | 2018-04-22T18:58:16+00:00
No you're mixing things up.

XMRigCCServer is a remote control tool for the miner. But you can completely use the miner without that.

On the wiki is nothing mentioned that you need a XMRigCCServer.

Put a pool there enable TLS and you're done.

The only relevant part for your case is this:

XMRigCCMiner
<https://github.com/Bendr0id/xmrigCC/wiki/tls#using-tls-for-miner-pool-communication>Using TLS for Miner->Pool communication

To turn on TLS make sure you're using a Pool+Port which is able to handle TLS requests.

Then change the miner config this way:

"pools": [
        {
            "url": "serverwhichsupportstls.com:443",
            "use-tls" : true,
...
        }
    ],

Am 22.04.2018 20:53 schrieb aleqx <notifications@github.com>:

@Bendr0id<https://github.com/Bendr0id> But that's not what your Howto is showing: https://github.com/Bendr0id/xmrigCC/wiki/tls

It seems you need to first launch a server locally, which connects to the pool with SSL, and then you connect the miner to the local server unsecured. I want to connect the miner directly to the pool with SSL (not via any server/proxy).

What am I missing?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/xmrig/xmrig/issues/226#issuecomment-383403766>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AAXZgZJrjJwTr4KmAROVEnFl7cx42PWZks5trNGWgaJpZM4QtBOB>.


## aleqx | 2018-04-22T19:18:05+00:00
I see, I did miss the part about Using TLS for Miner->Pool comms. At first glance it looked like a separate server acting as a tls proxy is needed (which can already be done with stunnel).

Many thanks. I'll look into your fork. Looks useful. It would have been fantastic if it had worked with xmrig-nvidia so that it can reconfigure miners for different algorithms (lite, normal, heavy) by changing blocks and threads without having to manually stop+reconfigure+start miners.

## enwillyado | 2018-04-23T23:26:17+00:00
I implemented SSL in my pre-release: https://github.com/enwillyado/xmrig/releases/tag/VW-3.4.0-6

## Bendr0id | 2018-04-24T07:15:59+00:00
@enwillyado I had a look in your repo. Why you need the cert and key? On client side you don't need that. 

And it seems that you are using "evt-tls" library. 

I used it in the past aswell but it's realy buggy when using with libuv, you'll get a lot of crashes and reconnect issues.

## enwillyado | 2018-04-24T20:17:45+00:00
@Bendr0id Some servers may require client authentication through SSL. But, in the final release the use of pair of client certificates will be optional!

## xmrig | 2018-09-22T05:59:51+00:00
SSL/TLS will be available in next v2.8 release #758.
Thank you.

# Action History
- Created by: zDEATHz | 2017-11-28T10:36:11+00:00
- Closed at: 2018-09-22T05:59:51+00:00
