---
title: Cannot start daemon
source_url: https://github.com/monero-project/monero/issues/3608
author: dmgmaker
assignees: []
labels: []
created_at: '2018-04-11T07:18:01+00:00'
updated_at: '2020-05-17T14:55:28+00:00'
type: issue
status: closed
closed_at: '2020-05-17T14:55:28+00:00'
---

# Original Description
[monero-wallet-gui.log](https://github.com/monero-project/monero/files/1897620/monero-wallet-gui.log)
I downloaded a new monero folder because i messed up with my last, i also deleted the old blockchain data to get all new. Now i try to start daemon with node.monerworld.com but after a time i get a message which says  daemon cannot connect, sometimes the programm collapses while starting daemon. I put the log in here too maybe someone can find out what is wrong. Thank you for any help.

# Discussion History
## moneromooo-monero | 2018-04-11T09:23:48+00:00
That's because the host is non existent. Try node.moneroworld.com.


## dmgmaker | 2018-04-12T04:59:17+00:00
i did node.moneroworld.com as host and as a port i tried 8880 then the daemon said it cant start. When i tried using port 18081 the programm collapsed.

## dmgmaker | 2018-04-12T05:02:56+00:00
But the most irritating thing is, that i cant open the gui anymore it takes hours to load but never finishes. i think i try to delete all folders i know from monero and try to reinstall it.

## dEBRUYNE-1 | 2018-04-12T09:54:35+00:00
`node.moneroworld.com` should be used with port `18089`

## dmgmaker | 2018-04-12T12:17:03+00:00
ok somehow i have another problem. I cant start my monero wallet at all. When i try to run the exe it crashes

## moneromooo-monero | 2018-04-12T13:08:27+00:00
Then please post a stack trace:

ulimit -c unlimited
echo core | sudo tee /proc/sys/kernel/core_pattern
Run monero-wallet-gui until it crashes
gdb /path/to/monero-wallet-gui /path/to/core
bt


## dmgmaker | 2018-04-12T13:27:53+00:00
> ulimit -c unlimited
echo core | sudo tee /proc/sys/kernel/core_pattern
Run monero-wallet-gui until it crashes
gdb /path/to/monero-wallet-gui /path/to/core
bt

> 
i dont really get what i need to do 

## moneromooo-monero | 2018-04-12T13:35:43+00:00
Are you on Linux, Mac, Windows, other ?

## dmgmaker | 2018-04-12T13:36:17+00:00
I am on Windows

## moneromooo-monero | 2018-04-12T13:37:19+00:00
Then if you know how to get a stack trace from a crash on windows, please do so. If you don't, then we're stuck.

## dmgmaker | 2018-04-12T13:40:24+00:00
yeah i dont know how to get that, but when u say i need it i will look it up and try to do it. Will post when i were successful


## moneromooo-monero | 2018-04-12T13:46:49+00:00
I'm told WinDbg is the tool for that, but I don't know how to use it.
I've added https://github.com/monero-project/monero/issues/3620 to get instructions added to the README for future use. If you find out how to use it before someone else does, maybe you could document the steps :)

## dmgmaker | 2018-04-12T14:30:41+00:00
Sadly i am a newbie with monero i cant even start the wallet exe and i just dont know why ^^ but ty for trying to help

## lashmi57 | 2018-04-26T15:14:40+00:00
I have the same problem, can't start deamon. on the main site it says:
**Download the new binaries from the official website or Github.**
then: Extract the new binaries to a new directory of your liking.
(a directory where..?? and you can't extract..but you can do a save as..!)
Then: Copy over the wallet files from the old directory (the one that contains the v0.11.0.0 or v0.11.1.0 binaries).
How can you expect the general population to take to this if you keep it techie, I've worked with
software guys over the years...they never get this..!! they write as they program and it might make
sense to them.....but for the non techies it doesn't work.!

## dEBRUYNE-1 | 2018-04-28T14:40:11+00:00
@lashmi57:

>I have the same problem, can't start deamon. on the main site it says:

Which operating system are you using?

>Download the new binaries from the official website or Github.

The binaries are the `.zip` file (Windows) or the `.tar.bz2` file (Mac OS X and Linux). 

>(a directory where..??

"To your liking" insinuates that it doesn't matter where you extract the binaries to. 

>but you can do a save as..!)

What do you mean here? The `.zip` file or `.tar.bz2` file first has to be saved, but subsequently has to be extracted to properly use the software. 

>Then: Copy over the wallet files from the old directory (the one that contains the v0.11.0.0 or v0.11.1.0 binaries).

This *merely* applies to the *CLI*. The wallet files are `<walllet-name>` (the file without extension), `<wallet-name>.keys`, and `<wallet-name>.address.txt`. 

>How can you expect the general population to take to this if you keep it techie, I've worked with
software guys over the years...they never get this..!! they write as they program and it might make
sense to them.....but for the non techies it doesn't work.!

It's a work in progress. 

## lashmi57 | 2018-05-01T16:33:34+00:00
@

Hi, just a quick note to say Thank you..!! Truly, Im still not sure how I got the wallet working...but after 3 days of pulling my hair out.
I came across a post of yours in in "Monero Beta" with the heading "I forgot to upgrade from GUI-v11 to Gui V12"
You gave instruction about popping blocks:-   ./monero-blockchain-import --pop-blocks 16500
Well I did this, nothing seem to happen I ran "monerod" it said the instruction stopped at an error location. I shut all the Monero processes and then started up Monero GUI.....It seemed to be frozen then it fired into life with "synchronizing wallet" zipping down from 12000 blocks to zero in about 5 minutes..!! My balance went up by the transaction that happened last week..!! I done a small transaction through shapeshift just to make sure it was working, yes..went through..!! 
So, thank you again, I'm off for a beer and a nervous breakdown..!!

## moneromooo-monero | 2020-05-17T14:55:28+00:00
Looks like this got resolved long ago, closing.

# Action History
- Created by: dmgmaker | 2018-04-11T07:18:01+00:00
- Closed at: 2020-05-17T14:55:28+00:00
