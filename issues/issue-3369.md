---
title: Wallet fails to synchronize when using Monero-GUI over Tor
source_url: https://github.com/monero-project/monero-gui/issues/3369
author: ch9PcB
assignees: []
labels: []
created_at: '2021-03-28T06:11:19+00:00'
updated_at: '2021-04-04T08:40:42+00:00'
type: issue
status: closed
closed_at: '2021-04-04T08:40:42+00:00'
---

# Original Description
I am using Debian 10 (64bit) with Monero GUI v0.17.1.9

**Previously**

* _tor_ package in Debian repos was not installed because it was an outdated version
* _torsocks_ was installed using Debian repos
* _Monero GUI v0.17.1.9_ was used. In the GUI, I set the bootstrap address to 127.0.0.1 and the bootstrap port to 9150 (because I used the Tor Browser.)
* _Tor Browser_ was used

In the first terminal, I launched _Tor Browser_.

In the second terminal, I activated _torsocks_ by issuing the command:

`. torsocks on`

In the third terminal, I changed to the directory where Monero and the blockchain data were located and issued the command:

`DNS_PUBLIC=tcp://1.1.1.1 TORSOCKS_ALLOW_INBOUND=1 torsocks ./monerod --p2p-bind-ip 127.0.0.1 --no-igd --hide-my-port --ban-list block.txt --data-dir    /media/user/Backup/Monero`

In the same terminal, after the message about the daemon was synchronized and that the monero-cli could be launched appeared, I launched a fourth terminal.

In the fourth terminal, I launched _Monero GUI_ and there would be displayed near the bottom left corner:

```
Wallet is synchronized
Daemon is synchronized
```

**Now**

* I installed _tor_ package in Debian backports because it has the latest version which is 0.4.5.7
* _torsocks_ was installed using Debian repos
* _Monero GUI v0.17.1.9_ was used. In the GUI, I set the bootstrap address to 127.0.0.1 and the bootstrap port to 9050 (because I use the installed _tor_ package.)

In the first terminal, I activate _torsocks_ by issuing the command:

`. torsocks on`

In the second terminal, I change to the directory where Monero and its blockchain data are located and issued the following command:

`./monero-wallet-gui`

After the daemon has synchronized, I notice that the **wallet is not synchronized** (click the link below to view the screenshot).

https://ibb.co/Yp6GYrf

Moreover, in the second terminal, there are error messages:

```
WARNING: i965 does not fully support Gen11 yet.
Instability or lower performance might occur.
2021-03-28 01:56:27.315	I Monero 'Oxygen Orion' (v0.17.1.9-release)
Forking to background...
2021-03-28 01:57:15.878	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:57:15.882	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:57:15.882	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:57:16.073	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:57:16.073	E pull_blocks failed, try_count=3
2021-03-28 01:57:26.094	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:57:36.113	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:57:46.163	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:57:46.164	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:57:46.164	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:57:46.355	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:57:46.355	E pull_blocks failed, try_count=3
2021-03-28 01:57:56.374	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:58:06.394	E daemonBlockChainHeight: Failed to connect to daemon
2021-03-28 01:58:16.639	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:58:16.639	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:58:16.639	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:58:16.827	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:58:16.827	E pull_blocks failed, try_count=3
2021-03-28 01:58:26.842	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:58:36.858	E daemonBlockChainHeight: Failed to connect to daemon
2021-03-28 01:58:47.115	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:58:47.115	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:58:47.116	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:58:47.307	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:58:47.307	E pull_blocks failed, try_count=3
2021-03-28 01:58:57.323	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:59:07.340	E daemonBlockChainHeight: Failed to connect to daemon
2021-03-28 01:59:17.597	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:59:17.597	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:59:17.597	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:59:17.787	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-28 01:59:17.787	E pull_blocks failed, try_count=3
```

# Discussion History
## selsta | 2021-03-28T12:05:01+00:00
> I set the bootstrap address to 127.0.0.1 and the bootstrap port to 9050 

Any reason for setting bootstrap address and port?

## ch9PcB | 2021-03-28T20:27:12+00:00
> Any reason for setting bootstrap address and port?

As I am using Monero GUI over Tor, I assume that it is necessary or else Monero GUI will not be able to connect to the network. Is my assumption correct? (Your question tells me that I can leave the fields of bootstrap address and port empty......)



## selsta | 2021-03-30T02:27:30+00:00
If you run your own synced node there is no reason to use bootstrap settings. Remove them and try again.

## ch9PcB | 2021-03-31T21:33:42+00:00
> If you run your own synced node there is no reason to use bootstrap settings. Remove them and try again.

If I do as you suggested, the daemon will be synchronized using Tor, but the wallet will be synchronized over clearnet (that is, using my ISP's connection). Is my statement correct?


## selsta | 2021-03-31T21:35:17+00:00
Is your daemon running locally on the same machine / same network? If yes it will not go through your ISP.

## ch9PcB | 2021-04-04T08:40:35+00:00
> Is your daemon running locally on the same machine / same network? If yes it will not go through your ISP.

Yes, it does.

Thanks for your clarification. I wish your answer was in the [User Guides](https://www.getmonero.org/resources/user-guides/)


# Action History
- Created by: ch9PcB | 2021-03-28T06:11:19+00:00
- Closed at: 2021-04-04T08:40:42+00:00
