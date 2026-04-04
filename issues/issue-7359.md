---
title: rpc_payments fails to start if running a regular RPC and restricted RPC on
  separate ports.
source_url: https://github.com/monero-project/monero/issues/7359
author: jnbarlow
assignees: []
labels: []
created_at: '2021-02-01T03:10:45+00:00'
updated_at: '2023-03-24T15:06:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I've spent a while playing the "what's different" game and narrowed it down to the following two scenarios.

If you start a server with no port assignments and `--restricted-rpc` (along with rpc payment flags), the `rpc_payments`  command shows stats and all is well.

However, if you start it with `--rpc-bind-port 18081 --rpc-restricted-bind-port 18089` and omit `--restricted-rpc`, the `rpc_payments` command yields `Error: Unsuccessful -- Payments not enabled`

It seems that `rpc_payments` needs a restricted server running for it to work, but doesn't know what to do when there is both a restricted and non-restricted server running out of the same daemon.

"Why would you run it that way?" you ask... Well, I can expose a restricted server to 18089 and hopefully get that sweet sweet rpc_payments money once that starts working, and keep a regular rpc running at 18081 so local network wallets can use it w/o having to pay (and allow me to pull stats off the rpc server.

# Discussion History
## moneromooo-monero | 2021-02-08T20:39:10+00:00
That's because the rpc_payments command is run on the default RPC port, which is not the one the RPC payment system is running. When using a restricted port and a non restricted port, there are two RPC servers running (unfortunately). This needs changing to have a single server listening on two ports (and restricting on one).

## jnbarlow | 2021-02-08T20:42:02+00:00
hmm..  with the current setup, do you think it would work if the restricted rpc ran on the default port and I moved the non-restricted port?

## moneromooo-monero | 2021-02-08T20:43:58+00:00
If you run rpc_payments as "monerod rpc_payments", then it should, as should "monerod --rpc-bind-port PORT rpc_payments". If running from the monerod console, I'm not quite sure.

## jnbarlow | 2021-02-08T20:50:39+00:00
hmm.. I'll give it a shot later tonight to see if I can have the restricted and non-restricted running with payments with the ports swapped... that's the one thing I didn't try.

I'll update the ticket with the results if it works or not.

## jnbarlow | 2021-02-08T21:57:58+00:00
yeah, swapping the ports doesn't help. It just doesn't know what to do with the two rpc servers running.

## reijerh | 2023-03-23T16:29:10+00:00
So... how are people using the `rpc_payments` command at the moment? The payment system is only useful for public nodes, but you obviously don't want it to be unrestricted. But if you make it unrestricted, you don't want it to be public.

So you'll have to use an unrestricted port as well, but now the `rpc_payments` command doesn't work...

This basically means you have to choose between managing your server via RPC _or_ running a public node?

What am I missing here?

(Sending a JSON request for `rpc_access_data` doesn't work either, since the restricted port will say it doesn't understand the command, and the unrestricted port will say payments are not enabled.)

## plowsof | 2023-03-24T00:46:43+00:00
@reijerh see #8724 (probably going to be removed: recent investigations showed that 'not many' nodes have it enabled. if use was widespread, 'evil' people would simply host free high quality nodes) 

however, there are use cases (which i personally like), such as https://repo.getmonero.org/selene/primo (it just never became popular)

## reijerh | 2023-03-24T15:06:51+00:00
Alright, thanks for the heads-up, and my sincere condolences to the original implementer. 🙃

# Action History
- Created by: jnbarlow | 2021-02-01T03:10:45+00:00
