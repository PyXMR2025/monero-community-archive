---
title: 'Feature Request:  JSON RPC call for the getrandom_outs.bin method using a
  JSON input'
source_url: https://github.com/monero-project/monero/issues/1363
author: medusadigital
assignees: []
labels: []
created_at: '2016-11-21T16:03:44+00:00'
updated_at: '2016-12-08T22:38:57+00:00'
type: issue
status: closed
closed_at: '2016-12-08T22:38:57+00:00'
---

# Original Description
Jaxx wants a JSON RPC call for the getrandom_outs.bin method using a JSON input. 

The daemon would be choosing the outputs istead of the wallet, which has an effect on users privacy.

more comments appreciated

# Discussion History
## AugustoL | 2016-11-21T16:09:51+00:00
How will this effect users privacy?

## tewinget | 2016-11-21T17:38:50+00:00
The daemon will know which output from each ring signature is the user's
because it chose the others.

This is dealt with by shifting the output selection to the client side, and
a JSON-RPC call is already written as needed for this in the upcoming zmq
rpc.

Will hasten my efforts.
On Nov 21, 2016 11:09 AM, "Augusto" notifications@github.com wrote:

How will this effect users privacy?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub
https://github.com/monero-project/monero/issues/1363#issuecomment-261982595,
or mute the thread
https://github.com/notifications/unsubscribe-auth/AE3k5rv5plCZslkoGBFKX2Fm9s7W-8W9ks5rAcJQgaJpZM4K4YA1
.


## AugustoL | 2016-11-21T17:50:29+00:00
Thanks @tewinget we are searching for random inputs on the client side using /getblocks and /gettransactions , I was wondering If we can did it using RPC to make the built of TX faster.

So as I understand the daemon knows if any of the outputs belongs to the user, right?, what if we had a randomOutputs rpc call that just return any random output (without checking ownership of outputs)? later on the client we can check if any of that outputs belongs to the suer, if not we can make the tx or ask for random outputs again.

## tewinget | 2016-11-21T17:54:57+00:00
I think you misunderstand.  Let's discuss it on IRC (#monero-dev on
freenode), as this discussion will quickly fall out of scope for this
feature request.
On Nov 21, 2016 12:50 PM, "Augusto" notifications@github.com wrote:

> Thanks @tewinget https://github.com/tewinget we are searching for
> random inputs on the client side using /getblocks and /gettransactions , I
> was wondering If we can did it using RPC to make the built of TX faster.
> 
> So as I understand the daemon knows if any of the outputs belongs to the
> user, right?, what if we had a randomOutputs rpc call that just return any
> random output (without checking ownership of outputs)? later on the client
> we can check if any of that outputs belongs to the suer, if not we can make
> the tx or ask for random outputs again.
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> https://github.com/monero-project/monero/issues/1363#issuecomment-262013864,
> or mute the thread
> https://github.com/notifications/unsubscribe-auth/AE3k5kWJptXJ8031SQJqVXeO8OxJCjsKks5rAdnngaJpZM4K4YA1
> .


## ghost | 2016-11-21T18:19:49+00:00
Really pleased to see these conversations starting :)

## moneromooo-monero | 2016-11-21T18:50:15+00:00
tewinget is correct.

Basically, if you use a daemon to ask "gimme N outputs of denomination X", then send a new tx to that daemon, and the daemon sees an input to that tx using the N outputs it sent earlier, plus another one, it can be sure that extra one is the real one.

The wallet now asks for specific outs, and, crucially, includes the one it intends to send. See the get_outs.bin call, which does that instead of the older getrandom_outs.bin.

## moneromooo-monero | 2016-11-21T18:55:33+00:00
> we are searching for random inputs on the client side using /getblocks and /gettransactions

Note that outputs are referenced by index, so in order to select random outputs, you need only know the number of outputs for a given denomination, say N, then pick P random numbers in [0,N). I'm not sure if you're doing something  more complicated here, but it kinda reads like it.

You get N by calling the histogram RPC. See an example in src/wallet/wallet2.cpp, get_outs (it does something a bit more funky to try to adapt to de facto distribution, but that can be ignored for a first implementation).

## AugustoL | 2016-11-21T19:55:45+00:00
@moneromooo-monero thanks for the detailed answer, let me dig again more deeply into the code to see again what we need.


## moneromooo-monero | 2016-11-22T20:02:48+00:00
I added a JSON based version of get_outs.bin, called get_outs.
This is to encourage doing the right thing. There will not be a text based version of getrandom_outs.bin.


## medusadigital | 2016-12-08T22:38:57+00:00
closing this for now. @AugustoL if youz have another request please open another ticket. 

# Action History
- Created by: medusadigital | 2016-11-21T16:03:44+00:00
- Closed at: 2016-12-08T22:38:57+00:00
