---
title: Solo mining
source_url: https://github.com/xmrig/xmrig/issues/3189
author: sachinverma1
assignees: []
labels: []
created_at: '2023-01-05T11:49:59+00:00'
updated_at: '2025-06-18T22:49:04+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:49:04+00:00'
---

# Original Description
Hi.
Does this miner works or solo mining on node?

Thank you

# Discussion History
## SChernykh | 2023-01-05T12:45:29+00:00
https://github.com/xmrig/xmrig/blob/master/scripts/solo_mine_example.cmd

## sachinverma1 | 2023-01-05T12:50:52+00:00
Thank you fir your help.. Can you please help me with Monero.conf file
also... Where I can write my information.

On Thu, Jan 5, 2023, 6:15 PM SChernykh ***@***.***> wrote:

> https://github.com/xmrig/xmrig/blob/master/scripts/solo_mine_example.cmd
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3189#issuecomment-1372170478>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AHRZNL674SH3A43GMRC4TBDWQ267JANCNFSM6AAAAAATR3SHPI>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


## SChernykh | 2023-01-05T12:58:30+00:00
Just run `monerod` without parameters and XMRig on the same machine:
```
xmrig.exe -o 127.0.0.1:18081 -a rx/0 -u WALLET_ADDRESS --daemon
```

## sachinverma1 | 2023-01-05T12:59:53+00:00
OK.. Great... Thank you.

On Thu, Jan 5, 2023, 6:28 PM SChernykh ***@***.***> wrote:

> Just run monerod without parameters and XMRig on the same machine:
>
> xmrig.exe -o 127.0.0.1:18081 -a rx/0 -u WALLET_ADDRESS --daemon
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3189#issuecomment-1372184408>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AHRZNLZYAFF6WGNIKSOCN6TWQ3AQDANCNFSM6AAAAAATR3SHPI>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


## NeelChandra001 | 2023-12-02T00:22:44+00:00
Hi - I am using this command to run solo (xmrig.exe -o 127.0.0.1:18081 -a rx/0 -u WALLET_ADDRESS --daemon) I get error invalid wallet address - it is a coinbase wallet (which is still in use) - Can you help because I cannot make it to run solo ...

## Superfrenk | 2023-12-02T01:16:41+00:00
Hi.

If you have problem with setup your pool and wallet just go to this site
--> https://unmineable.com/support/article/how-to-setup-xmrig-for-cpu-mining

This site teach you to configurate your pool and wallet address.

Simple.

When you download XMRIGHT.rar or .exe I folder is .JSON  dokument --> this
dokument open in program visual studio or GitHub desk.

When you have oppened .json dokument here you can manage or change the pool
and wallet

Sending picture

Dňa so 2. 12. 2023, 1:23 NeelChandra001 ***@***.***>
napísal(a):

> Hi - I am using this command to run solo (xmrig.exe -o 127.0.0.1:18081 -a
> rx/0 -u WALLET_ADDRESS --daemon) I get error invalid wallet address - it is
> a coinbase wallet (which is still in use) - Can you help because I cannot
> make it to run solo ...
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3189#issuecomment-1836952972>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ASOA5F4EPANP56WJUU4KGLTYHJYHNAVCNFSM6AAAAAATR3SHPKVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQMZWHE2TEOJXGI>
> .
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


## sachinverma1 | 2023-12-02T02:38:27+00:00
Coinbase wallet address will not work for solo mining.

On Sat, 2 Dec, 2023, 6:46 am Marek Bárta, ***@***.***> wrote:

> Hi.
>
> If you have problem with setup your pool and wallet just go to this site
> -->
> https://unmineable.com/support/article/how-to-setup-xmrig-for-cpu-mining
>
> This site teach you to configurate your pool and wallet address.
>
> Simple.
>
> When you download XMRIGHT.rar or .exe I folder is .JSON dokument --> this
> dokument open in program visual studio or GitHub desk.
>
> When you have oppened .json dokument here you can manage or change the
> pool
> and wallet
>
> Sending picture
>
> Dňa so 2. 12. 2023, 1:23 NeelChandra001 ***@***.***>
> napísal(a):
>
> > Hi - I am using this command to run solo (xmrig.exe -o 127.0.0.1:18081
> -a
> > rx/0 -u WALLET_ADDRESS --daemon) I get error invalid wallet address - it
> is
> > a coinbase wallet (which is still in use) - Can you help because I
> cannot
> > make it to run solo ...
> >
> > —
> > Reply to this email directly, view it on GitHub
> > <https://github.com/xmrig/xmrig/issues/3189#issuecomment-1836952972>,
> or
> > unsubscribe
> > <
> https://github.com/notifications/unsubscribe-auth/ASOA5F4EPANP56WJUU4KGLTYHJYHNAVCNFSM6AAAAAATR3SHPKVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQMZWHE2TEOJXGI>
>
> > .
> > You are receiving this because you are subscribed to this thread.Message
> > ID: ***@***.***>
> >
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3189#issuecomment-1836977275>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AHRZNLZ2GQUCKXTLU3YBEATYHJ6QJAVCNFSM6AAAAAATR3SHPKVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQMZWHE3TOMRXGU>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


## SChernykh | 2023-12-02T08:11:41+00:00
@NeelChandra001 you have to use the wallet address starting with 4... for solo mining. Also, Coinbase doesn't even have Monero. Also, never download some random xmrig.rar from any websites - they can be malware. Download XMRig from https://github.com/xmrig/xmrig/releases/latest or from xmrig.com

# Action History
- Created by: sachinverma1 | 2023-01-05T11:49:59+00:00
- Closed at: 2025-06-18T22:49:04+00:00
