---
title: Daemon response did not include the requested real output
source_url: https://github.com/monero-project/monero-gui/issues/3709
author: oliverlj
assignees: []
labels: []
created_at: '2021-09-25T05:38:03+00:00'
updated_at: '2021-09-25T06:22:35+00:00'
type: issue
status: closed
closed_at: '2021-09-25T06:22:35+00:00'
---

# Original Description
I got this error message after upgrading form 0.17.2.2 to 0.17.2.3

This happens when I try to send a transaction

2021-09-25 05:31:32.443	E !real_out_found. THROW EXCEPTION: error::wallet_internal_error
2021-09-25 05:31:32.450	E Can't create transaction:  internal error: Daemon response did not include the requested real output
2021-09-25 05:31:32.450	W "Could not convert argument 0 at"
2021-09-25 05:31:32.450	W 	 "onTransactionCreated@qrc:/main.qml:825"
2021-09-25 05:31:32.450	W "Passing incompatible arguments to C++ functions from JavaScript is dangerous and deprecated."
2021-09-25 05:31:32.450	W "This will throw a JavaScript TypeError in future releases of Qt!"


# Discussion History
## selsta | 2021-09-25T05:40:39+00:00
Which wallet mode are you using? You can check on Settings -> Info

Also if this error shows up please immediately go to Settings -> Log, type "status" into the textbox and post the output here.

## oliverlj | 2021-09-25T05:49:54+00:00
Wallet mode: Advanced mode (Local node)

same daemon running for this issue

1 try to send from 0.17.2.3 => error
2 try to send from 0.17.2.2 => ok
3 try to send from 0.17.2.3 again => error

status : 
[25/09/2021 07:48] 2021-09-25 05:48:07.599 I Monero 'Oxygen Orion' (v0.17.2.3-release)
Height: 2456910/2456910 (100.0%) on mainnet, bootstrapping from 78.46.250.164:18089, local height: 2388690 (97.2%), not mining, net hash 2.62 GH/s, v14, 0(out)+0(in) connections


## selsta | 2021-09-25T05:52:14+00:00
Did you set a bootstrap node on `Settings -> Node`? If yes, what did you enter?

## oliverlj | 2021-09-25T05:57:13+00:00
![image](https://user-images.githubusercontent.com/1826498/134760318-ed5ec8c0-b8b5-4204-854f-1d715b5c92b2.png)


## selsta | 2021-09-25T06:00:03+00:00
You were connected to a malicious remote node that tried to weaken your privacy.

Please add `--enable-dns-blocklist` to `Daemon startup flags`.

Also change the `auto` to one of the remote nodes from here: https://monero.fail/ so that you don't connect to the malicious remote node anymore. Afterwards the issue should not show up anymore.

## oliverlj | 2021-09-25T06:22:35+00:00
ok this is working with this configuration. I can close this issue. And help anyone with this error later. Thanks for your time

# Action History
- Created by: oliverlj | 2021-09-25T05:38:03+00:00
- Closed at: 2021-09-25T06:22:35+00:00
