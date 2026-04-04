---
title: Always get stuck on the last 2 blocks - Monero Core win-x64-v0.17.1.5
source_url: https://github.com/monero-project/monero/issues/7050
author: gab81
assignees: []
labels: []
created_at: '2020-12-01T12:54:09+00:00'
updated_at: '2020-12-28T21:38:15+00:00'
type: issue
status: closed
closed_at: '2020-12-01T20:19:47+00:00'
---

# Original Description
hi,

apologies for reporting this again, but not sure it went to the right channel, this one should be it.

I synced my Monero Core a few times recently and it always get stuck on the last 2 blocks

When i load it the first time it finishes relatively quickly, says "Daemon Synchronized" and "all blocks synced" so both bars are orange, yet after a while it keeps going on and off between 1 block and 2 blocks, and stays on 2 blocks left for a while, it didn't happen to previous release as far as i can tell.

https://www.dropbox.com/s/ct6yf6t5kjly3ph/Mnr-stuck-2-blocks.png?dl=0

what's up? i have monero-gui-install-win-x64-v0.17.1.5

**Edit**: it finished, then back again to 1 block remaining and then 2 blocks again. so odd,

this is what i have in the log:

2020-12-01 11:43:42.160	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:368	[95.216.173.96:36630 INC] Sync data returned a new top block candidate: 2242596 -> 2242597 [Your node is 1 blocks (2.0 minutes) behind] 
2020-12-01 11:43:42.160	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:368	SYNCHRONIZATION started
2020-12-01 11:44:18.745	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1600	Synced 2242597/2242597
2020-12-01 11:44:18.746	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318	SYNCHRONIZED OK
2020-12-01 12:22:03.909	[P2P4]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318	SYNCHRONIZED OK
2020-12-01 12:23:20.281	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318	SYNCHRONIZED OK
2020-12-01 12:33:57.837	[P2P5]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318	SYNCHRONIZED OK
2020-12-01 12:40:20.779	[P2P2]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318	SYNCHRONIZED OK

and this is going over and over.. is that the intended behaviour?

many thanks

# Discussion History
## glv2 | 2020-12-01T13:36:34+00:00
I have the same thing on my node. It looks like a malicious node that I'm connected to is always indicating that its top block is 1 or 2 blocks ahead of the real top block.

You can try to start *monerod* with the ```--ban-list``` option to prevent the bad nodes from giving your node false information.
@selsta has a list of known bad nodes in https://gui.xmr.pm/files/block.txt, or you can make your own list.


## gab81 | 2020-12-01T13:49:01+00:00
hmhmhm that sounds strange, why would the app be connected to a malicious node? can it compromise things?

would like to hear the developers about this but thanks for the heads up!

## glv2 | 2020-12-01T14:08:33+00:00
It doesn't compromise Monero's privacy features (stealth addresses, ring signatures and masked amounts). 

You can read some info about these malicious node [here](https://www.reddit.com/r/Monero/comments/jrh7mv/psa_informational_thread_on_the_recently_observed/) and [here](https://www.reddit.com/r/Monero/comments/k3hoew/psa_if_you_run_a_public_remote_node_please/).


## gab81 | 2020-12-01T15:33:29+00:00
i ran the ban block command, just one question, does it "understand" the command if i have the blockchain on an external hard disk? it adds the ip to be banned successfully, but then he goes onto syncing from scratch..... 

so if i have the blockchain on D would this command work or i need to launch it with the blockchain location on D as well? hope it's clear what i mean, thank you!

## gab81 | 2020-12-01T15:37:12+00:00
ok i launched it with my real blockchain location, it got it to work ok, apparently 80+ blocks behind, let's see what happens now 👍 

## Pogodenhelder | 2020-12-01T16:26:22+00:00
i have the same problem on OSX with the wallet.
It stays at 2 blocks then goes to 1 block and then back to 2 blocks.

is there a way to fix this "problem"?

## dEBRUYNE-1 | 2020-12-01T18:26:07+00:00
The issue is caused by the malicious (misbehaving) nodes^1. It can be solved as follows.

**If you run your own local node (GUI)**

1. Download this file and place it in the same folder as `monerod` / `monero-wallet-gui`: https://gui.xmr.pm/files/block.txt

2. Go to the `Settings` page -> `Node` tab. 

3. Enter `--ban-list block.txt` in `daemon startup flags` box.

4. Restart the GUI (and daemon). 

**If you run your own local node (CLI)**

1. Download this file and place it in the same folder as `monerod` / `monero-wallet-cli`: https://gui.xmr.pm/files/block.txt

2. Add `--ban-list block.txt` as daemon (monerod) startup flag. 

3. Restart `monerod`

The issue will be investigated to provide a more permanent solution in an upcoming release. 

[1] See:

https://www.reddit.com/r/Monero/comments/jrh7mv/psa_informational_thread_on_the_recently_observed/

https://www.reddit.com/r/Monero/comments/jv8v2r/psa_if_you_run_a_public_remote_node_please/

## gab81 | 2020-12-01T18:38:02+00:00
> The issue is caused by the malicious (misbehaving) nodes^1. It can be solved as follows.
> 
> **If you run your own local node (GUI)**
> 
> 1. Download this file and place it in the same folder as `monerod` / `monero-wallet-gui`: https://gui.xmr.pm/files/block.txt
> 2. Go to the `Settings` page -> `Node` tab.
> 3. Enter `--ban-list block.txt` in `daemon startup flags` box.
> 4. Restart the GUI (and daemon).
> 
> **If you run your own local node (CLI)**
> 
> 1. Download this file and place it in the same folder as `monerod` / `monero-wallet-cli`: https://gui.xmr.pm/files/block.txt
> 2. Add `--ban-list block.txt` as daemon (monerod) startup flag.
> 3. Restart `monerod`
> 
> The issue will be investigated to provide a more permanent solution in an upcoming release.
> 
> [1] See:
> 
> https://www.reddit.com/r/Monero/comments/jrh7mv/psa_informational_thread_on_the_recently_observed/
> 
> https://www.reddit.com/r/Monero/comments/jv8v2r/psa_if_you_run_a_public_remote_node_please/

Thanks @dEBRUYNE-1 I can confirm, i've imported the ban list on command line mode, worked OK, then now launched the GUI and it's fully synchronized. 

So to the others @Pogodenhelder and @glv2 please try this too 👍 

The question is : is it gonna happen again? what about for other users that encounter this, perhaps the new release can bundle in the rogue IPs to be blocked already?


## selsta | 2020-12-01T18:41:28+00:00
> The question is : is it gonna happen again? what about for other users that encounter this, perhaps the new release can bundle in the rogue IPs to be blocked already?

We will add some mitigations to this annoying, but harmless attack in a future release. We will most likely not bundle a list of IP addresses.

## sumogr | 2020-12-01T18:41:38+00:00
report the IPs of the stupid f.ck to OVH for services abuse ffs

## gab81 | 2020-12-01T19:14:34+00:00
I talked too soon, after about 10-15 minutes stable with wallet synchronized, it's happening again, **back to "2 blocks remaining".**

then back to full again..... then back again to 2 blocks remaining :(

## selsta | 2020-12-01T19:15:46+00:00
How did you start the daemon when using in combination with the GUI?

## selsta | 2020-12-01T19:18:34+00:00
You always have to add the --ban-list flag when starting the daemon, not only once.

## selsta | 2020-12-01T19:59:17+00:00
@gab81 Please post the output of "sync_info" entered into Settings -> Log textbox.

## gab81 | 2020-12-01T20:17:05+00:00
> You always have to add the --ban-list flag when starting the daemon, not only once.

ahhhhhhhhhhhhhhhhhhhhhh that wasn't clear, ok will do - i did import the ban list via command line, then shut off then started GUI (without flag).

now i launched the GUI with the flag in there right away and it has been 45 mins. good now. thanks again

## selsta | 2020-12-01T20:18:25+00:00
@gab81 Glad you resolved it for now. If it starts to happen again, please download the latest version of https://gui.xmr.pm/files/block.txt and if happens again please post the output of "sync_info".

## gab81 | 2020-12-01T20:18:26+00:00
[01/12/2020 21:17] 2020-12-01 20:17:41.565 I Monero 'Oxygen Orion' (v0.17.1.5-release) 
Height: 2242858, target: 2242858 (100%) 

## gab81 | 2020-12-23T17:28:19+00:00
hi there,

there's an update to monero > monero-gui-install-win-x64-v0.17.1.7 . does that address the issue or you still have to launch with the banlist, etc? thank you

## selsta | 2020-12-28T21:36:38+00:00
Hi, this has been an ongoing attack with various variations of it, v0.17.1.7 does not resolve it.

## gab81 | 2020-12-28T21:38:15+00:00
ok thanks, still have the flag to filter in fact

# Action History
- Created by: gab81 | 2020-12-01T12:54:09+00:00
- Closed at: 2020-12-01T20:19:47+00:00
