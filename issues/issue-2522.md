---
title: 'monerod_sync_ERROR '
source_url: https://github.com/monero-project/monero/issues/2522
author: dranogy
assignees: []
labels: []
created_at: '2017-09-24T14:41:59+00:00'
updated_at: '2022-03-16T15:29:47+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:29:47+00:00'
---

# Original Description
Dear Monero community, I am using Tails to run full monero nod and having issues with blockchain sync. I get the sync error allways at approximately block 407681 or 407686. I tried to change the USB storrage, tried to change the computer but still the same. 

I run the Tails with following:

sudo iptables -I OUTPUT 2 -p tcp -d 127.0.0.1 -m tcp --dport 18081 -j ACCEPT

DNS_PUBLIC=tcp TORSOCKS_ALLOW_INBOUND=1 torsocks ./monerod --p2p-bind-ip 127.0.0.1 --no-igd --rpc-bind-ip 127.0.0.1 --data-dir /media/amnesia/bitmonero

The sync error I get is following:

2017-09-24 14:08:24.910	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[94.23.4.63:18080 OUT]  Synced 407681/1406121
2017-09-24 14:08:26.485	[P2P4]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:72	Failed to commit a transaction to the db: Input/output error
2017-09-24 14:08:26.615	[P2P4]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3598	Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: Input/output error

Thank you

# Discussion History
## moneromooo-monero | 2017-09-24T15:05:33+00:00
<s>That looks like bad hardware. Check the disk, and prepare to buy a new one.</s> Hmm, you did say you changed computers. OK, that is very odd. EIO usually points to bad hardware... 

Talking to hyc, this could be due to not enough space, as the db resize doesn't acrtually check for space. Is the partition with the blockchain running out of space ?

## dranogy | 2017-09-26T09:07:46+00:00
hi moneromooo-monero, thank you for your support. I will be more precise. 

My setup/process I tried to run full monero client, is following: 
- dowloaded full CLI cient from an official website through proven Tails (full cli-GPG and hash check) - OK. 
- extracted the client in the Tails persistence named monero
- formated 2 USBs in Tails, one 32GB and 64GB. Named them bitmonero. I used them for blockchain storage. Both are Sandisk. Maybe this is an issue?
- I run monerod with commands, see above with --data-dir /media/amnesia/bitmonero on both USBs 3 times each, on 2 computers. The same network (can this be an issue?).
- my first computer is ThinkPadX200, 4GB RAM. Second computer I tried is Asus Zenbook UX305FA. Both can run Tails well. 
- can the IP [94.23.4.63:18080 OUT]  be a malicion IP? Should I try to block it?
I am stack with this and not happy. I elieve the Monero is the game changer and I need to join well and safe. 

My intention is for now, to just create an offline wallet with high sec level, to be able to send funds into. I runned full client on 32-bit version on my X200 with no issues before. 

Any help will be miuch appreciated guys. 

## moneromooo-monero | 2017-09-26T10:29:28+00:00
I'd run with strace to see if an I/O syscall is failing shortly before the error:

DNS_PUBLIC=tcp TORSOCKS_ALLOW_INBOUND=1 torsocks strace -o monerod.trace ./monerod --p2p-bind-ip 127.0.0.1 --no-igd --rpc-bind-ip 127.0.0.1 --data-dir /media/amnesia/bitmonero

Then check monerod.trace for errors (typically return values of -1).

The rest of what you say seem OK, assuming you had enough space left on those USB drives at the time of the error (which seems likely if they were empty to begin with).

## dranogy | 2017-09-27T12:31:25+00:00
Unfortunately in tails it tells me the trace is not available. Why do you think this issue appears, and what are the options to solve it? 

Do you have possibly any other options to create safely the offline wallet and be able to move xmr in case of need? I im definitely decided to run full monero client, but wouldnt like to lose time till it is solved. 

## moneromooo-monero | 2017-09-27T13:17:04+00:00
strace, not trace.

I do not know why you'd get I/O errors if the hardware's good. strace should help see whether they're really I/O errors (from the kernel) or not.

As for other options, you can use a remote node now (--daemon-address node.moneroworld.com:18089), until you can have your own local node.

## dranogy | 2017-09-27T13:43:59+00:00
I tried to run as you posted:
DNS_PUBLIC=tcp TORSOCKS_ALLOW_INBOUND=1 torsocks strace -o monerod.trace ./monerod --p2p-bind-ip 127.0.0.1 --no-igd --rpc-bind-ip 127.0.0.1 --data-dir /media/amnesia/bitmonero
and have got the "trace not available". Should it be -o monerod.strace instead of -o monerod.trace?

Can you be more specific with --daemon-address node.moneroworld.com:18089 please?  I am a bit noobish in that. 

Definitely I am decided to go for a full node, and will do whatever possible to make it run. If there is any assistance availale. Thank you!

## moneromooo-monero | 2017-09-27T22:14:59+00:00
The output filename doesn't matter. I guess "trace not available" might be a message from strace saying it can't trace a process. If you run just "strace", does it find the program ? If yes, then something in TAILS config seems to be preventing it from working. Some kind of kernel hardening, maybe.

For " --daemon-address node.moneroworld.com:18089", this is for running a wallet with a daemon run by someone else on the internet. This would be a temporary state until we can work out what's going on with those I/O errors. You pass that option on the monero-wallet-cli command line. If you use the GUI wallet instead, those go on the relevant text widgets in the settings page. If you prefer to wait to get the I/O errors fixed, then you can ignore that.

## dranogy | 2017-10-02T09:12:53+00:00
Sorry for the spoon feeding request, but could you elaborate the remote node function and running more please? 

My intention is to create an offline wallet through CLI, and be able to get, send monero and monitor my wallet. I understood that I can create and work with a monero wallet with the full monero client only if the blockchain is synced (right?), or use the remote node as proposed by you. 

Now for the remote node function:
- I right click in the folder with unpacked monero client, to open CLI (or just cd it)
- I enter the $ sudo iptables -I OUTPUT 2 -p tcp -d 127.0.0.1 -m tcp --dport 18081 -j ACCEPT
should I now proceed with the $ --daemon-address node.moneroworld.com:18089 ? 

I will try to start with the remote node and will closely watch the I/O error fixing to switch ASAP to the full client function. 

Thank you in advance for your support!

## moneromooo-monero | 2017-10-02T13:58:54+00:00
The "--daemon-address node.moneroworld.com:18089" is added at the end of the monerod command line. So using your original command:

DNS_PUBLIC=tcp TORSOCKS_ALLOW_INBOUND=1 torsocks ./monerod --p2p-bind-ip 127.0.0.1 --no-igd --rpc-bind-ip 127.0.0.1 --data-dir /media/amnesia/bitmonero --daemon-address node.moneroworld.com:18089



## dranogy | 2017-10-11T12:59:54+00:00
I tried the cli comand as stated but I get following error:

DNS_PUBLIC=tcp TORSOCKS_ALLOW_INBOUND=1 torsocks ./monerod --p2p-bind-ip 127.0.0.1 --no-igd --rpc-bind-ip 127.0.0.1 --data-dir /media/amnesia/bitmonero --daemon-address node.moneroworld.com:18089

Failed to parse arguments: unrecognised option '--daemon-address'

any ideas please?

## moneromooo-monero | 2017-10-11T13:03:03+00:00
er, yes, I was being an idiot, sorry. This goes on the monero-wallet-cli command line, not the monerod one.

## dranogy | 2017-10-11T17:49:26+00:00
no problem, how do I proceed than please? Where do I put the comands above, I used to run monero package through Tor only? Is it even necessary?

(it would be excelent if someone doesnt mind to extract the Linux, 64-bit (Command-Line Tools Only) or even the GUI  in the Tails and check it. Would be tremendous help for noobs like me)

## hyperreality | 2019-08-18T21:36:32+00:00
I just reproduced that the exact error monerod provides when the target data directory is on a drive that's out of space, is:

```
2019-08-18 21:31:56.105	W Failed to commit a transaction to the db: Input/output error
2019-08-18 21:31:56.105	E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: Input/output error
```
It seems plausible to me that @dranogy is hitting this error at the same block each time because the target drive only contains 32 GB of space.

@moneromooo-monero  Probably this can just be closed out because you already added a separate warning when free space is below 1 GB a month later https://github.com/monero-project/monero/commit/43f27c7d43ee5cae601e1fb0181cba2ccfd7baa6

## moneromooo-monero | 2019-08-27T15:38:29+00:00
Seems plausible, though a 64 GB card was used too, and that should be easily ample enough for 410k blocks. But maybe the bork happened much later in that case, and that was glossed over...


## selsta | 2022-03-16T15:29:47+00:00
No other report of this, closing due to inactivity.

# Action History
- Created by: dranogy | 2017-09-24T14:41:59+00:00
- Closed at: 2022-03-16T15:29:47+00:00
