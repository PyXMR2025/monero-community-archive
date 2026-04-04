---
title: 'Error: Error mining to daemon: Found nonce, but daemon errored out with error
  -18: Stale payment, continuing'
source_url: https://github.com/monero-project/monero/issues/7041
author: lh1008
assignees: []
labels: []
created_at: '2020-11-23T15:14:18+00:00'
updated_at: '2025-12-28T22:40:29+00:00'
type: issue
status: closed
closed_at: '2025-12-28T22:40:29+00:00'
---

# Original Description
`Error: Error mining to daemon: Found nonce, but daemon errored out with error -18: Stale payment, continuing`

Hello everyone,

I have been using the RPC-pay wallet to use a RPC-pay node server and I encountered a bug I believe. These are the steps I did.

First, I stopped the wallet security closing timing.

`help set inactivity-lock-timeout 0`

and then, kept the same client ID to save the mining hashes.

`help set persistent-rpc-client-id 1`

When I first did it, nothing weird happened. There wasn't any lock timeout, everything was running smoothly, mining was great Then I `stop_mining_for_rpc` and closed the wallet. Re-opened it a day after and the wallet refreshes itself automatically using the previews hashes mined to the rpc-clien-id saved. It synchs properly and when it's finally synced this is what shows up:

![wallet_sytart](https://user-images.githubusercontent.com/7443480/99977914-44947100-2d73-11eb-912b-ce9ef4f6ab35.png)

If I type:

`rpc_payment_info` -> I start receiving the same error `Error: Error mining to daemon: Found nonce, but daemon errored out with error -18: Stale payment, continuing`. 

![error_info](https://user-images.githubusercontent.com/7443480/99977430-9f799880-2d72-11eb-987b-869d83c4889e.png)

f I type `start_mining_for_rpc`, it does the same. I receive the same errors message -> `Error: Error mining to daemon: Found nonce, but daemon errored out with error -18: Stale payment, continuing`

When I open the wallet this is what happens:

![error](https://user-images.githubusercontent.com/7443480/99976780-dd29f180-2d71-11eb-9db5-41c72b3ae584.png)

Let me know if you need anything from me so I can post it here. 

Thank you for your support.


# Discussion History
## lh1008 | 2020-11-25T13:25:04+00:00
An update in this. 

The error still shows up. So I tried to end the process (maybe that's not the way to do it), but anyway, I tried to disable the `persistent-rpc-client-id` by sending the 0. The command wasn't accepted (received) and the error still shows appearing. 
I also tried several times sending the `stop_mining_for_rpc` command but mining doesn't stop. It just keeps going and going.

I'll try to check the code, does anyone know which file I can check this out?

## lh1008 | 2020-11-26T17:34:32+00:00
Okay, another update on this.

I did a new wallet and well, what I expected, it happens again. 

So to conclude and be precise on what happens is:

- When a Monero user uses the monero-wallet-cli to run through a RPC-pay node it gets the error -> `Error: Error mining to daemon: Found nonce, but daemon errored out with error -18: Stale payment, continuing` by doing the following steps: 

1. Sync/refresh wallet the user starts mining for rpc -> `starts_mining_for_rpc`
2. Sets inactivity lock timeout to 0 -> `set inactivity-lock-timeout 0`
3. To save the client ID sets the persistent rpc client ID typing the command -> `set persistent-rpc-client-id 1`.
4. User stops mining -> `stop_mining_for_rpc`. 
5. `exit` wallet.

When the user re-opens the wallet, the wallet automatically refreshes with the persistent cliend ID using the hashes for payment  and then the error shows up by itself.

![error](https://user-images.githubusercontent.com/7443480/100379802-8b889d80-2fe3-11eb-9c93-7a29ec08fe49.png)


This is using Ubuntu 20.04.1 LTS (Focal Fossa) LTS.

:)

## lh1008 | 2020-12-02T15:54:20+00:00
Updated wallet to Monero Oxygen Orion v0.17.1.5 and the error is showing up with the `--log-level 2`.

![error](https://user-images.githubusercontent.com/7443480/100896542-b7e16580-348c-11eb-84b4-214515ab6a16.png)


## lh1008 | 2020-12-03T17:49:37+00:00
Hello everyone, this happened today

![error](https://user-images.githubusercontent.com/7443480/101067379-7b356d00-3565-11eb-8121-841d6891649d.png)

![error_1](https://user-images.githubusercontent.com/7443480/101066927-e7fc3780-3564-11eb-819c-8e275bbd92aa.png)

Pastebin

https://pastebin.pl/view/8dc197f6

## lh1008 | 2020-12-04T00:13:06+00:00
RPC Pay Log
[rpcPayserver.log](https://github.com/monero-project/monero/files/5639750/rpcPayserver.log)

Monero Wallet Cli Log
[monero-wallet-cli.log](https://github.com/monero-project/monero/files/5639789/monero-wallet-cli.log)



## lh1008 | 2020-12-06T17:45:13+00:00
RPC pay Server 2020-12-06-15-49 log timestamp

[rpcPayServer-2020-12-06-15-49.log](https://github.com/monero-project/monero/files/5649239/rpcPayServer-2020-12-06-15-49.log)





## lh1008 | 2020-12-06T17:45:55+00:00
Monero Wallet Cli 2020-12-06-15-49 timestamp

[monero-wallet-cli-2020-12-06-15-49.log](https://github.com/monero-project/monero/files/5649242/monero-wallet-cli-2020-12-06-15-49.log)


## moneromooo-monero | 2020-12-22T15:49:21+00:00
Did you get logs with the patch I gave you a couple weeks back ?

## lh1008 | 2020-12-22T20:09:49+00:00
Hey moneromooo, I patched and build (compiled). But the compiled version should have been replaced but it wasn't, I still had the latest version (0.17.1.7). I don't know how to find the replaced just compiled patch (it wasn't in the /bin folder). :/ I got stuck there. You told me I had to adapt the binaries to specify the paths and, that's where I got lost. 

I did patch it: `patch -p1 < FILENAME`. 
Then I compiled build again: `make`

## lh1008 | 2020-12-22T20:12:13+00:00
At the moment I complied I was running the v0.17.1.5 <- just to clarify, above I said I had the v0.17.1.7.

## moneromooo-monero | 2020-12-23T01:01:08+00:00
Should be in build/something/bin

Easiest is probably, after you built succesfully:

find build -name monerod -mmin -2

## lh1008 | 2020-12-29T17:30:12+00:00
Hey @moneromooo-monero,

Okay, so...I made a clean `git clone` of the Monero Project repository. Before building (`make`) I patched the code you gave me. Then I build `make` and, yes, the executables are stored in /build/something/bin.

Here are the logs:
[rpcPayServer.log](https://github.com/monero-project/monero/files/5751560/rpcPayServer.log)

[monero-wallet-cli.log](https://github.com/monero-project/monero/files/5751563/monero-wallet-cli.log)

I'm going to try creating a new wallet. 

## lh1008 | 2020-12-29T17:36:32+00:00
Oh, wait, I did `make` without `git checkout release-v0.17`. :facepalm: 



## lh1008 | 2020-12-29T20:53:21+00:00
Okay finally. I made a restore-deterministic-wallet and it refreshed the first ~5000 blocks from my local node and then it stopped. I connected it to the rpc-server and the error showed up. The code was built with the patch. 

[rpcPayServer.log](https://github.com/monero-project/monero/files/5752130/rpcPayServer.log)
 
[monero-wallet-cli.log](https://github.com/monero-project/monero/files/5752132/monero-wallet-cli.log)

![rpc_pay](https://user-images.githubusercontent.com/7443480/103313386-ed2a9600-49ed-11eb-9d9c-a63ace557abf.png)


## lh1008 | 2021-01-31T15:41:38+00:00
@moneromooo-monero I think I found what's the issue. The error is showing up when I set `set persistent-rpc-client-id 1`. This time I restored deterministic wallet, had a clean wallet, and only added the `set persistent-rpc-client-id 1` command. Closed the wallet, reopened the wallet and `started_mining_for_rpc` and the error shows up. It goes deeper, once the error starts showing up the wallet is mining but the RPC is not getting the hashes, so it doesn't sum up any credits:

![rpc_payment_info](https://user-images.githubusercontent.com/7443480/106389343-d7274100-63b0-11eb-8961-16ec5ef691c7.png)


## lh1008 | 2021-01-31T15:49:17+00:00
monero-wallet-cli.log

https://paste.debian.net/1183453/


## selsta | 2025-12-28T22:40:20+00:00
Closing as this issue has been removed from the wallet side.

# Action History
- Created by: lh1008 | 2020-11-23T15:14:18+00:00
- Closed at: 2025-12-28T22:40:29+00:00
