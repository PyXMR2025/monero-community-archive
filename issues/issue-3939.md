---
title: Monero GUI Wallet not displaying balance
source_url: https://github.com/monero-project/monero-gui/issues/3939
author: RonnyBlack1978
assignees: []
labels: []
created_at: '2022-06-04T16:20:54+00:00'
updated_at: '2022-06-04T19:56:00+00:00'
type: issue
status: closed
closed_at: '2022-06-04T19:56:00+00:00'
---

# Original Description
I am a bit of a newbie to this.

Having checked other threads on here, I am running Windows 10 (64-bit - clean with no malware) and am using the Monero GUI Wallet (V.0.17.3.2). When using the wallet I disable my VPN and anti-virus software.

I have transferred Monero (XMR) from Binance to my GUI Wallet (advanced). The main address is correct and I can see the transaction on XMRchain.net. The GUI wallet displays as correctly syncing and connecting. However, the balance does not update.

I have tried:

Uninstalling and reinstalling the GUI Wallet. Changing the wallet restore height to an earlier number. Using several remote nodes that try to connect but unfortunately disconnect straight away. Changing the wallet file name (the one without an extension) to perform a refresh.

Nothing seems to work. The only thing that appears strange is that every time I check the log status it shows 0 (Out) and 0 (In) connections.

Does anyone have any suggestions? I would greatly appreciate some help.

Thanks.

# Discussion History
## selsta | 2022-06-04T16:38:02+00:00
https://github.com/monero-project/monero-gui/issues/3912#issuecomment-1119632082

Can you do these steps to set Advanced mode with a remote node?

Also can you post the transaction id of the transaction that is missing and can you go to Settings -> Info and post the output of "Wallet restore height".

## RonnyBlack1978 | 2022-06-04T17:53:26+00:00
Thanks for your response.

Advanced mode with remote node address: 88.198.199.23 and port: 18081 stays disconnected on the network status (bottom left) after 5 minutes.  I restarted the GUI wallet - same thing.

The transaction ID is: 433e52038b2bf96209da34d3a650eb61f18602a8ea74da718a6948273d4a220d

and the Wallet restore height: 2637979

Thanks.



## selsta | 2022-06-04T18:05:40+00:00
Is this transaction id that you posted the first transaction that you received?

Can you go to Settings -> Info and click on "(Change)" and then enter 2500000 and then ok twice?

Then wait for it to resync.

## RonnyBlack1978 | 2022-06-04T18:08:53+00:00
Yes, first transaction.

I have tried:

address: node.supportxmr.com
port: 18081

address: 78.47.80.55
port: 18081

address: node.community.rino.io
port: 18081

None of them connect.  It always displays Network Status as being disconnected in the bottom left corner.

## selsta | 2022-06-04T18:09:55+00:00
Did you change random settings around? E.g. Settings -> Interface did you enable socks5 proxy?

## RonnyBlack1978 | 2022-06-04T18:11:00+00:00
If I change to 2500000 but am disconnected on any of those remote nodes, will that change anything?

I will try now.

## RonnyBlack1978 | 2022-06-04T18:11:53+00:00
No changes made to any settings. Default installation with a new wallet created and advanced mode selected.

## selsta | 2022-06-04T18:14:49+00:00
You have to be connected to a node first before anything works. All these nodes are online so the issue is somewhere on your own end, we just have to figure it out.

## selsta | 2022-06-04T18:16:21+00:00
Can you open

88.198.199.23:18081/get_info

in your browser and see if it loads? It should display some JSON text.

## RonnyBlack1978 | 2022-06-04T18:17:44+00:00
Agreed.  

88.198.199.23:18081/get_info loads fine.

My internet is running fine and my VPN and anti-virus software are both definitely off.

## selsta | 2022-06-04T18:19:13+00:00
Settings -> Interface: the enable socks5 proxy setting has to be disabled.

Can you check for that?

## RonnyBlack1978 | 2022-06-04T18:20:31+00:00
Yes, that is disabled.

## selsta | 2022-06-04T18:21:14+00:00
What kind of anti virus and VPN are you using?

## RonnyBlack1978 | 2022-06-04T18:22:48+00:00
Bitdefender Total Security and NordVPN.  I have permanently disabled the Bitdefender AntiVirus Shield and completely quit NordVPN.

## RonnyBlack1978 | 2022-06-04T18:27:18+00:00
Hang on, just checked Bitdefender and the firewall is blocking the GUI Wallet.  Let me see if  I can connect to a remote node now.

## RonnyBlack1978 | 2022-06-04T18:30:41+00:00
I had disabled Bitdefender but didn't realise the firewall was still on.  It was blocking the Monero GUI Wallet.

Balance now updated!

Thank you very much for your help.

 I really appreciate it.

## selsta | 2022-06-04T19:56:00+00:00
Glad it's resolved. If the remote nodes makes issues in the future you can choose a different one from the linked comment.

# Action History
- Created by: RonnyBlack1978 | 2022-06-04T16:20:54+00:00
- Closed at: 2022-06-04T19:56:00+00:00
