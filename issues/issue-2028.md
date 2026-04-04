---
title: GUI with Linux not saving remote node
source_url: https://github.com/monero-project/monero-gui/issues/2028
author: roudaille
assignees: []
labels:
- resolved
created_at: '2019-03-21T20:42:26+00:00'
updated_at: '2019-03-22T11:48:31+00:00'
type: issue
status: closed
closed_at: '2019-03-22T11:45:38+00:00'
---

# Original Description
Hi,
with Linux, each time I start-gui.sh, I am starting from the beginning of the configuration of the wallet (created a new wallet from hardware):
- language selection
- mode selection
- open a wallet from file
- going to settings and specifying remote node

Hopefully the daemon and wallet remain sync when I set back everything.
One strange thing in info tab is the wallet creation height. I guess it is not related.

GUI version: v0.14.0.0 (Qt 5.7.0)
Embedded Monero version: v0.14.0.2
Wallet path: /home/X/Monero/wallets/X/X.keys
Wallet creation height: 0
Wallet log path: /home/X/.bitmonero/monero-wallet-gui.log
Wallet mode: Advanced mode

# Discussion History
## sanderfoobar | 2019-03-21T20:55:25+00:00
I'm trying to understand your issue, so far I can conclude:

1. Every time you start the GUI, you begin in the wizards
2. After opening your wallet and going to the node settings, it will **not** save the remote node in `/.config/monero-project/monero-core.conf` after clicking **connect**

Could you verify?

In addition; please paste output of: 

```bash
ls -al /.config/monero-project/monero-core.conf
```

And also:

```bash
grep  wallet_path ~/.config/monero-project/monero-core.conf
```

I'm trying to rule out the possibility that you might have incorrect permissions on your config file.

## dEBRUYNE-1 | 2019-03-21T20:56:21+00:00
@roudaille - Is this the first time you are using the GUI? Or did you use GUI v0.13.0.4 as well? 

## roudaille | 2019-03-21T22:04:06+00:00
> I'm trying to understand your issue, so far I can conclude:
> 
> 1. Every time you start the GUI, you begin in the wizards
> 2. After opening your wallet and going to the node settings, it will **not** save the remote node in `/.config/monero-project/monero-core.conf` after clicking **connect**
> 
> Could you verify?
> 
> In addition; please paste output of:
> 
> ```shell
> ls -al /.config/monero-project/monero-core.conf
> ```
> 
> And also:
> 
> ```shell
> grep  wallet_path ~/.config/monero-project/monero-core.conf
> ```
> 
> I'm trying to rule out the possibility that you might have incorrect permissions on your config file.

Hi xmrdsc,
I looked at the folders you mentioned and realized that in monero-core.conf there was root user.
I used to configure and launched the GUI with root before adding rules to udev.
There was .shared-ringdb folder which was root folder and not accessible when using a regular user.
I changed the permission and now the wallet is launching directly to the password pop up, keeping all the parameters.
Thank you.
But I still don't understand why I have Wallet creation height: 0.

## sanderfoobar | 2019-03-22T11:44:14+00:00
Thanks @roudaille that helps us out a ton. Glad it has been resolved by setting correct permissions.

 ```
chown user:user ~/.config/monero-project/monero-core.con
chown -R user:user ~/.shared-ringdb
chown -R user:user ~/.bitmonero
``` 

Where user is your system username, for anyone googling.

+resolved

# Action History
- Created by: roudaille | 2019-03-21T20:42:26+00:00
- Closed at: 2019-03-22T11:45:38+00:00
