---
title: balance not showing after transaction completed, ledger X, GUI
source_url: https://github.com/monero-project/monero-gui/issues/3610
author: nec1977
assignees: []
labels: []
created_at: '2021-07-05T03:51:05+00:00'
updated_at: '2021-07-08T20:40:49+00:00'
type: issue
status: closed
closed_at: '2021-07-08T18:06:29+00:00'
---

# Original Description
Hello, my deposit is not showing in my wallet. I've connected with my ledger X, did not export the keys, I'm using GUI bootstrap. All firmwares and versions are updated. Transaction is confirmed. Windows OS.  Thank you in advance for your help

# Discussion History
## dEBRUYNE-1 | 2021-07-05T11:09:37+00:00
What do the status bars in the left bottom report? 

## selsta | 2021-07-05T20:29:35+00:00
Also please post in Settings -> Info: `Wallet version` and `Wallet restore height`.

## nec1977 | 2021-07-06T05:06:47+00:00
Thank you so much for your replies. I have tried 3 times today to open the wallet and could not make it work properly. I will come back tomorrow. Could it have to do with a very slow procesor on my laptop? Opening and closing the aplication takes ages to load, when closing now it says "verifying local node" already for 30 minutes. After opening it was not really connecting properly and was not showing the same in progress bars as it was yesterday. Sorry didnt take notes of the actual texts hoping to be able to log in but didnt work in the end and now I'm very tired. Will try again tomorrow. Many thanks and good night 

## nec1977 | 2021-07-06T17:10:21+00:00
Status bars left bottom says "Waiting for daemon to sync" and "Daemon remaining blocks 2398950" all in grey, no progress.
GUI version 0.17.2.2-937cb98 (Qt 5.15.2)
Monero embeded version: 0.17.2.0-release
Restore Height 2377356
 

## selsta | 2021-07-06T23:44:56+00:00
I would recommend to connect to a remote node for now.

You can go to the main menu by clicking on the exit symbol in the top left corner.

Then click on "Change wallet mode" and select "Advanced mode". Afterwards open your wallet again, go to Settings -> Node, select "Remote node" and enter the following node:

address: `node.melo.tools`
port: `18081`

Then wait for your wallet to sync.

----------

Other remote node in case the above has issues:

address: `88.198.199.23`
port: `18081`

address: `78.47.80.55`
port: `18081`

address: `node.supportxmr.com`
port: `18081`

## nec1977 | 2021-07-08T04:00:01+00:00
Been trying for 3 hours to make this work, Im starting to think my computer is not powerful enough to run the wallet or something is not right, it gets stuck, nothing works. Tried with all nodes and no progress in bars whatsoever. 
My question now is: if I leave this as it is now, buy a new more powerful computer, and recover the wallet from there maybe in a month time, will my XMR be safe while on the blockchain but still not synced on my ledger? Sorry but Im still learning, many thanks

## selsta | 2021-07-08T04:00:53+00:00
Did you export your view key?

## nec1977 | 2021-07-08T15:45:25+00:00
no, I did not export the key

## selsta | 2021-07-08T15:46:01+00:00
You have to export the view key else it won't work.

## nec1977 | 2021-07-08T15:58:25+00:00
You mean confrim/aprove export key on my ledger? I read that in order to keep privacy it was better not to export? wouldnt it compromise my privacy or security if I export it?

## selsta | 2021-07-08T16:02:05+00:00
Your privacy would only get compromised if there is malware on your computer, but seeing that the malware could record your computer screen your privacy would get compromised anyway, even without exporting the view key.

It isn't possible without exporting the view key, the Ledger is too weak.

## nec1977 | 2021-07-08T16:21:00+00:00
Thank you so much for your kind help, I've read another thread where they said not to export the key and so I did. It worked perfectly now! Just for educational porpouses I would like to understand how this works, so when I export my view key, ledger is sending GUI a special password so the wallet can show my balance but it does not have anything to do with the seed or private key?

## selsta | 2021-07-08T18:06:29+00:00
The view key allows the GUI to scan for incoming transactions.

It is not possible to send any funds with the view key, that requires the spend key which stays on device.

Closing as the issue seems resolved.

## nec1977 | 2021-07-08T20:40:49+00:00
thank you so much for your help, have a nice weekend

# Action History
- Created by: nec1977 | 2021-07-05T03:51:05+00:00
- Closed at: 2021-07-08T18:06:29+00:00
