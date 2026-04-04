---
title: /sys/class/power_supply errors when smart mining on Fedora 25
source_url: https://github.com/monero-project/monero/issues/2614
author: shmacoshmuesday
assignees: []
labels: []
created_at: '2017-10-09T02:24:59+00:00'
updated_at: '2020-04-23T03:43:26+00:00'
type: issue
status: closed
closed_at: '2017-10-16T08:30:24+00:00'
---

# Original Description
On Fedora 25, x64, running version 11 GUI wallet and daemon, trying to smart mine. I do get hashes from it but apparently it's having trouble monitoring the power supply...? Here are the errors I'm getting. I believe I'm on the latest kernel or a very recent one. When I type status it shows that smart mining is working and giving me about 60 hashes/s.

2017-10-09 01:18:05.197	    7f2bff0fc700	ERROR	miner	src/cryptonote_basic/miner.cpp:940	couldn't query power status from /sys/class/power_supply
2017-10-09 01:18:05.197	    7f2bff0fc700	INFO 	global	src/cryptonote_basic/miner.cpp:650	idle percentage is 55%, miner percentage is 44%, ac power : 1
2017-10-09 01:18:15.199	    7f2bff0fc700	WARN 	miner	src/cryptonote_basic/miner.cpp:864	Unable to read from "/sys/class/power_supply/AC" to check if power supply present

# Discussion History
## glv2 | 2017-10-09T07:39:17+00:00
If you can compile and test the master branch, there is a patch in it that should fix that (commit 20256b7c0499b07c4f2ad45901bcde7d68893345).


## shmacoshmuesday | 2017-10-10T21:07:12+00:00
This will be my first time compiling if successful, will report back by end of week. Thank you!!

## shmacoshmuesday | 2017-10-14T13:28:30+00:00
I haven't been successful compiling (checked all dependencies, have a thread open on stackexchange asking for help, need to check on it). Just wanted to give a headsup. Thanks again

## shmacoshmuesday | 2017-10-15T12:48:10+00:00
Question for anyone that can answer: if I'm getting an error compiling from the master branch and I've verified my dependencies, should I open that as an issue here on github?

## moneromooo-monero | 2017-10-15T18:00:05+00:00
If you think it's a monero bug, yes.

## shmacoshmuesday | 2017-10-16T02:25:45+00:00
Thanks moneromoo. I found the answer to my latest issue and was able to compile from the master branch.

Happy to report I tested this issue and it appears to be resolved. 

I'm sure this isn't the best place but please point me to a better place to post such things if there is one. Is there a way that I/we can add a column for fedora on the dependency list? There are quite a few subtle (and not so subtle) differences in the dependencies required for fedora compared to what's listed on the project page. I'd be happy to do whatever needs done to accomplish that, I can provide the list of what I had to install to compile the latest on fedora.

## moneromooo-monero | 2017-10-16T08:20:33+00:00
They're in the README.md file, just add a column to the table starting on line 162, like there is for Ubuntu and Arch already.

+resolved

## shmacoshmuesday | 2017-10-16T21:33:02+00:00
Thanks (many times over of course) moneromoo
I'm a noob so may have more noob questions but I get what you're saying and I'll make that another project to mark off the list :)

## jaidetura55 | 2020-04-23T03:43:26+00:00
is it still mining or block mining


# Action History
- Created by: shmacoshmuesday | 2017-10-09T02:24:59+00:00
- Closed at: 2017-10-16T08:30:24+00:00
