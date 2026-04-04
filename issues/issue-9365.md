---
title: 'RPC Connection only over SSL, SSL - RPC, Check, '
source_url: https://github.com/monero-project/monero/issues/9365
author: jogii2p
assignees: []
labels:
- question
- low priority
- discussion
created_at: '2024-06-12T13:45:07+00:00'
updated_at: '2024-06-14T19:26:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hey,

I want to run my CakeWallet only over SSL to my own Node.
All works fine is seems, but:
To check that everything is working fine I have a few points:

1. Is the Options --rpc-ssl with command,
 ** enabled** -> Does this command rejects connections without ssl? Can I be sure that the connection is save with ssl?
Is there a way to use "Only" SSL for RPC connection? 
b: Where are the different between "enabled" and "auto" by dyfault? "Disabled" are clear.

2. Take the Option --rpc-ssl with the command enabled the certificate from the folder .bitmonero?
3. Is there a way to check the ssl connection?
4. If I create my own new public and private certificate with monero-gen-ssl-cert, is this a bug?, that the privat certificate is usually a .txt file? (the text file is fine, and includes the right certificates)
5. This happend if i don't set a file typ for the creating with monero-gen-ssl-cert, what kind of certificates are need, because in the .bitmonero folder the files are .crt and .key and not .pem? Does it metter? (It's work to create filename.pem) (I seems fine to work with all three .crt, .key and .pem)
6. The CakeWallet is't a real helper, because there is a point to set "Use SSL" but it does't matter if i set it or not there is no different, here i guess the CakeWallet is on Auto SSL.
7. Is there a way in the running monerod, to check the ssl?
8. Suggestin for the future, i guess that was definitley discuss a lot in the past, to force "Use Only SSL for RPC".

Thanks for all.

Used Monero Version 0.18.3.3
Linux Kernel: 6.9.3-1

References:
1. https://getmonero.dev/interacting/monerod.html

# Discussion History
## 0xFFFC0000 | 2024-06-14T07:33:41+00:00
Regarding your questions. 

> 1. Can I be sure that the connection is save with ssl?

I didn't understand this part. What do you mean by save with ssl?

> 2. Take the Option --rpc-ssl with the command enabled the certificate from the folder .bitmonero?

My apologies. I didn't quite understand this question. 

> 3. Is there a way to check the ssl connection?

You mean something like wireshark/tcpdump? One other way would be to set log level to 4, and look at the data transmitted during RPC requests and response. 

> 7. Is there a way in the running monerod, to check the SSL?

Same as the previous question. 

## jogii2p | 2024-06-14T12:17:52+00:00
 > 1. Can I be sure that the connection is save with ssl?

Here I meant whether there is a way to check and ensure that the SSL-RPC connection is fully functional?
This question is actually answered by the questions below.

> 2. Take the Option --rpc-ssl with the command enabled the certificate from the folder .bitmonero?

Which certificates does SSL use for an RPC connection and where are they usually stored in the system? Are they the certificates that I find under "/home/user/.bitmonero"? Because there are two here, "rpc_ssl.crt" and "rpc_ssl.key", are these the standard certificates used for an SSL-RPC connection? If I don't specify any others? 

> 3. Is there a way to check the ssl connection?

Yes here i meant wireshark/tcpdump or the log level 4.
In log level 4 I found:
>2024-06-14 11:33:45.351	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1496	New server for RPC connections, **SSL enabled**

Is this proof that SSL is being used? 

it seems that "--rpc-ssl enabled" allows a non ssl connection if SSL is switched off on the client (Cakewallet). A connection is nevertheless established here without SSL. (Cakewallet Option: SSL use off)
Is that right?
Is there a way to only accept an SSL connection and reject other RPC requests?

The background of my question is to make absolutely sure that my connection from Cakewallet (RPC-Client) to my Monero node (RPC-Server), which is protected with user and password, is also protected via SSL. I want to exclude my own mistakes here and also protect my username and password.
If no SSL connection is established, my transmitted data, transactions (edit-Here I know that the transaction is protected by monero standard) , username and password are visible in plain text, aren't they? 

 > 7. Is there a way in the running monerod, to check the ssl?

Here I meant a possible command to display the RPC clients and their connections to the Monero node, e.g. with "print_rpc" or similar. But I have now looked through all the documents and found nothing about this. I thought there was a possibility to display the RPC requests of the last hour or similar.

Next time I'll write more clearly :)

## selsta | 2024-06-14T19:17:11+00:00
I just did a test starting `monerod` with `--rpc-ssl enabled`, together with `monero-wallet-cli` and `--daemon-ssl disabled` I was not able to connect. If Cake Wallet is able to connect to SSL enabled daemon with SSL disabled then there might be a bug in Cake Wallet.

The `auto` settings means that the daemon allows SSL and non-SSL connections.

# Action History
- Created by: jogii2p | 2024-06-12T13:45:07+00:00
