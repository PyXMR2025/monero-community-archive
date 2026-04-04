---
title: Monero Wallet Wont send coin with payment ID
source_url: https://github.com/monero-project/monero-gui/issues/1456
author: paulus333
assignees: []
labels:
- resolved
created_at: '2018-06-10T15:15:29+00:00'
updated_at: '2018-07-04T09:00:46+00:00'
type: issue
status: closed
closed_at: '2018-07-04T09:00:46+00:00'
---

# Original Description
Hi
So i had monero at bittrex and decided to keep safe in the monero-wallet-gui.
Everything seems fine it synchs, lets me know my monero coin but whenever i send a payment it does not go through.

I have sent to bittrex with and with out payment ID and to bitfinex with payment id but each time in wallet it states its been sent but it never comes through. Can somebody help please - attached payments
![screen shot 2018-06-10 at 16 07 19](https://user-images.githubusercontent.com/40145051/41203008-7a85f850-6cc9-11e8-83a6-ec727fa68244.png)


# Discussion History
## dEBRUYNE-1 | 2018-06-10T16:21:44+00:00
Could you post the full output of `Show status` (on the `Settings` page of the GUI)?

## paulus333 | 2018-06-10T16:29:12+00:00
Thanks for reply

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Error: Couldn't connect to daemon: 127.0.0.1:18081

Height: 1588171/1588171 (100.0%) on mainnet, not mining, net hash 572.64 MH/s, v6, update needed, 0(out)+0(in) connections, uptime 0d 0h 0m 3s

Height: 1592760/1592760 (100.0%) on mainnet, not mining, net hash 987.63 MH/s, v6, update needed, 9(out)+3(in) connections, uptime 0d 1h 22m 27s

Height: 1592760/1592760 (100.0%) on mainnet, not mining, net hash 987.63 MH/s, v6, update needed, 9(out)+3(in) connections, uptime 0d 1h 22m 30s


## paulus333 | 2018-06-10T16:30:25+00:00
Just sent

Thanks



> On 10 Jun 2018, at 17:21, dEBRUYNE-1 <notifications@github.com> wrote:
> 
> Could you post the full output of Show status (on the Settings page of the GUI)?
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/1456#issuecomment-396061745>, or mute the thread <https://github.com/notifications/unsubscribe-auth/AmSQmz8buij59gZQbUGori0PIbSQXxgLks5t7UebgaJpZM4UhwNo>.
> 



## pazos | 2018-06-10T18:11:25+00:00
@paulus333: You are in the dark side of monero :p. Current block is 1592113 right now and you're a few hundred blocks ahead, in the v6 chain. This means that you sent "monero" classic/original/zero to the exchange and not XMR.

Please read this, https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-11-to-cli-or-gui-v0-12-and-created-pe/

## dEBRUYNE-1 | 2018-06-11T08:55:35+00:00
@paulus333 - Which operating system are you using? Then I can give you specific steps on how to properly upgrade. 

## paulus333 | 2018-06-13T05:34:00+00:00
Hey

i am on mac book pro
2.2 GHz intel Core i7
10.13.4

Thanks

> On 11 Jun 2018, at 09:55, dEBRUYNE-1 <notifications@github.com> wrote:
> 
> @paulus333 <https://github.com/paulus333> - Which operating system are you using? Then I can give you specific steps on how to upgrade.
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/1456#issuecomment-396171228>, or mute the thread <https://github.com/notifications/unsubscribe-auth/AmSQm6Sl4REvijPQVtpuB6wPnpA9qbiiks5t7jCLgaJpZM4UhwNo>.
> 



## dEBRUYNE-1 | 2018-06-14T17:32:49+00:00
@paulus333 - First, make sure to close all Monero related software. Subsequently, please try these steps:

1. Download GUI v0.12.0.0 from [here](https://github.com/monero-project/monero-gui/releases/tag/v0.12.0.0). Direct link -> https://github.com/monero-project/monero-gui/releases/download/v0.12.0.0/monero-gui-mac-x64-v0.12.0.0.tar.bz2 

2. Extract the `.tar.bz2` file to a new folder / directory. 

3. Download *CLI* v0.12.2.0 from [here](https://github.com/monero-project/monero/releases/tag/v0.12.2.0). Direct link -> https://github.com/monero-project/monero/releases/download/v0.12.2.0/monero-mac-x64-v0.12.2.0.tar.bz2

4. Extract the `.tar.bz2` file to a new folder / directory. 

5. Open Finder and browse to the directory / folder v0.12.0.0 `monero-wallet-gui.app` is located.

6. Right click on `monero-wallet-gui.app` -> `Show contents` 

7. Now copy `monerod` v0.12.2.0 (from the CLI v0.12.2.0 directory / folder) to the v0.12.0.0 `monero-wallet-gui.app` -> `Show contents` directory / folder. 

8. Restart GUI v0.12.0.0 and let it start the daemon. The GUI should now be able to resolve the issue automatically. Make sure to give it ample time to do so though. 

## dEBRUYNE-1 | 2018-07-04T08:46:54+00:00
This particular issue is resolved in GUI v0.12.2.0: 

https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/

## dEBRUYNE-1 | 2018-07-04T08:46:58+00:00
+resolved

# Action History
- Created by: paulus333 | 2018-06-10T15:15:29+00:00
- Closed at: 2018-07-04T09:00:46+00:00
