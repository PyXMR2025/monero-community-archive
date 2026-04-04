---
title: Transactions stuck at pending (Waiting for transaction to leave txpool)
source_url: https://github.com/monero-project/monero-gui/issues/2954
author: neponel
assignees: []
labels: []
created_at: '2020-06-15T10:53:53+00:00'
updated_at: '2020-06-15T12:25:32+00:00'
type: issue
status: closed
closed_at: '2020-06-15T12:25:32+00:00'
---

# Original Description
Hi all,

I'm new to this so would appreciate any help even if my question is dumb. 
A transaction of mine was stuck at pending. I've tried re-naming my {wallet} to {wallet}-old, and re-syncing, and sent another transaction. It's stuck again!
I think I'm using a remote node, on mac GUI client - the settings section of the client doesn't have a "log" tab too. 
What should I do? 

Thanks!!

# Discussion History
## selsta | 2020-06-15T10:57:57+00:00
Are you using simple mode? You can check the wallet mode in Settings -> Info. If yes, please click on the two arrows in the bottom left corner to connect to a new remote node and try again. It is possible that the node you connected to has problems.

## neponel | 2020-06-15T11:01:39+00:00
Thanks for your reply. I am indeed using simple mode. Already tried switching to a new node - it says "successfully connected to a new node" but it hasn't resolved the problem unfortunately.

## selsta | 2020-06-15T11:05:58+00:00
Ok, will take a look if there are problems with node switching.

In the meantime you can click on the exit icon in the top left corner, click on "Change wallet mode" -> Advanced mode, then open your wallet, go to Settings -> Node, select remote node and enter node.xmr.to port 18081

## neponel | 2020-06-15T12:13:10+00:00
Ok, so I swapped to Advanced mode and noticed that I in fact have a local node, not remote! The transaction is still pending...

## selsta | 2020-06-15T12:15:31+00:00
Did you select a remote node and entered node.xmr.to 18081?
<img width="1026" alt="Screenshot 2020-06-15 at 14 15 13" src="https://user-images.githubusercontent.com/7697454/84656217-a1f9db80-af12-11ea-9ff1-9828ba0a2f07.png">


## neponel | 2020-06-15T12:25:32+00:00
I have managed to resolve the issue using the advanced settings. Thanks a lot for your help!

# Action History
- Created by: neponel | 2020-06-15T10:53:53+00:00
- Closed at: 2020-06-15T12:25:32+00:00
