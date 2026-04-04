---
title: Starting wallet rpc server
source_url: https://github.com/monero-project/monero/issues/1906
author: Joter271
assignees: []
labels: []
created_at: '2017-03-21T13:15:35+00:00'
updated_at: '2018-04-24T11:33:16+00:00'
type: issue
status: closed
closed_at: '2017-08-08T22:12:12+00:00'
---

# Original Description
Our monero-wallet-rpc.exe is stucked at "Starting wallet rpc server". It doesn't move over this step. We have increased verbosity level but can't get any useful log data. Version 10.1 works without any issues with same startup parameters. 

System: Windows Server 2012 R2
Version: Monero 10.2.1 64bit

![image](https://cloud.githubusercontent.com/assets/8576660/24148872/e94aa062-0e40-11e7-98c3-1cf6f7e0b43d.png)



# Discussion History
## amiuhle | 2017-03-21T14:12:02+00:00
Is the wallet synchronized?

If you open the wallet with `monero-wallet-cli`, you should see some more progress on synchronization, I think. I would open it with cli, let it sync completely, then exit and open the wallet with `monero-wallet-rpc` again.

## Joter271 | 2017-03-21T17:09:31+00:00
Now we have manually added some peers that someone suggested [here](http://monero.stackexchange.com/questions/3861/why-is-monerod-not-connecting-to-any-peers). It is now synced with network, but doesn't seem to start wallet rpc server... 


## amiuhle | 2017-03-21T18:21:47+00:00
Did you try with `--log-level 2` or `--log-level 4`? There's no log level 5, I don't know if that will just fall back to level 4 though.

Also you can try opening the wallet with `monero-wallet-cli`, wait for synchronization, then `exit` and try again with `monero-wallet-rpc`.

## Joter271 | 2017-03-21T18:23:14+00:00
Have tried with log level 4. Have restarted rpc.exe few times...


On Mar 21, 2017 19:21, "Timo Uhlmann" <notifications@github.com> wrote:

> Did you try with --log-level 2 or --log-level 4? There's no log level 5,
> I don't know if that will just fall back to level 4 though.
>
> Also you can try opening the wallet with monero-wallet-cli, wait for
> synchronization, then exit and try again with monero-wallet-rpc.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/1906#issuecomment-288172923>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AILelDJC_4yN5MdaHlCtgu9qJKKWkFELks5roBU_gaJpZM4MjyeP>
> .
>


## moneromooo-monero | 2017-03-21T19:23:40+00:00
Update to latest master, it's likely it's refreshing from the daemon, then pulling the (currently hefty) tx pool. The wallet now has a cache, so first load will still be slow, but subsequent ones will not be.

## Joter271 | 2017-03-21T19:54:23+00:00
I have managed to start RPC server, but now we have authentication issues. Previous RPC server didn't have any authentication, is there a way to disable it? We are connecting to RPC via secure VPN tunnel, so we can have it disabled... 

EDIT: `--disable-rpc-login `startup parameter helped. 

Thanks for help. 

## vtnerd | 2017-03-21T20:29:02+00:00
Yes, just remembered that @fluffypony told me to add logging to the server when it rejects requests. Its now on my whiteboard.

## moneromooo-monero | 2017-08-08T22:08:54+00:00
+resolved

## panpanliuBJ | 2018-03-13T03:45:07+00:00
It needs to sync block

![image](https://user-images.githubusercontent.com/12446331/37321588-f41715b6-26b3-11e8-80cd-26353bd63638.png)


## zeshanvirk | 2018-04-24T11:33:15+00:00
i'm having the same issue, how can i fix it?

# Action History
- Created by: Joter271 | 2017-03-21T13:15:35+00:00
- Closed at: 2017-08-08T22:12:12+00:00
