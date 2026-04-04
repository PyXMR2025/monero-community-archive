---
title: README.md step by step install instructions for ubuntu
source_url: https://github.com/monero-project/monero/issues/951
author: grummerd
assignees: []
labels: []
created_at: '2016-08-09T15:28:25+00:00'
updated_at: '2018-01-08T14:24:31+00:00'
type: issue
status: closed
closed_at: '2018-01-08T14:24:31+00:00'
---

# Original Description
This is a documentation request. Not going as far as asking the installer to check whether the dependencies are installed and if not install them

I'm thinking from a non-technical user's POV, it's frightening the technical knowledge bitmonero is expecting. The bar is set quite high, lets bring that down as much as possible. Baby steps

Plz include a step by step list of commands needed to install dependencies (for ubuntu)

sudo apt-get install [dependency 1]

sudo apt-get install [dependency 2]

sudo apt-get install [dependency 3]

Writing [dependency 1] or later,  [dependency 2] or later,  [dependency 3] or later is hard to follow and not user friendly. Did i install all the dependencies?! Who knows... 


# Discussion History
## anonimal | 2016-08-11T22:28:06+00:00
@grummerd would something like [Kovri's building instructions](https://github.com/monero-project/kovri/blob/master/doc/BUILDING.md) suffice?


## grummerd | 2016-08-13T07:35:07+00:00
First thanks for replying with a very useful link

Looking at the [bitmonero github readme.md install instructions](https://github.com/monero-project/bitmonero). Only. This is where the install instructions for bitmonero should live. Am i mistaken?? No where else. If installing kovri is a requirement then shouldn't ALL install instructions, including kovri, be on bitmonero page??

How to install / use monero should be crystal clear and simple. This issue is about documentation clarity (UX)
- Why am i installing kovri? Why would anyone be looking at kovri?
- From the bitmonero page, there is no prompt to use the kovri install instructions
- bitmonero has instructions for [torsocks](https://github.com/monero-project/bitmonero#using-tor), kovri i2p. Which one supposed to be configured? Both?!
- Why doesn't bitmonero mention [opening post in firewall](https://github.com/monero-project/kovri/blob/master/doc/BUILDING.md#step-4-open-your-natfirewall)?
- Which am i supposed to run [bitmonerod](https://github.com/monero-project/bitmonero#running-bitmonerod) or [kovri](https://github.com/monero-project/kovri/blob/master/doc/BUILDING.md#step-5-run-kovri)
- There is no discussion about whether or not to download the [blockchain](http://monero.cc/downloads/blockchain/linux/blockchain.bin) or let it sync from the beginning?

Are users supposed to hunt down pieces and patch them together?


## anonimal | 2016-08-14T09:01:18+00:00
@grummerd I only provided the link as an aesthetic example of how to build and install a piece of software; you do **not** have to install kovri to use bitmonero. I only wanted you to see the layout and design of the installation process.

I repeat: kovri building instructions have **nothing** to do with bitmonero at this point in time. Kovri is currently detached from bitmonero so, right now, think of it as its own piece of software _independent_ of bitmonero and you do **not** need kovri to run bitmonero.

I agree that [bitmonero's dependency guide](https://github.com/monero-project/bitmonero/blob/master/README.md#overview) needs work.


## grummerd | 2016-08-15T11:46:56+00:00
Misunderstood and unwittingly tried unsuccessfully to install kovri

Didn't get past the dependencies. Ran into the issue that kovri requires libcppnetlib-dev v0.12.0-final and the Ubuntu universal apt repository only has v0.11.2+dfsg1-2 Was unsuccessful at compiling/building libcppnetlib-dev v0.12.0-final

So guess i'll wait until ubuntu updates it's universal repository to install kovri

Time to dive into bitmonero. Hopefully have more luck


## grummerd | 2016-08-15T11:57:07+00:00
@anonimal Figure fixing the bitmonero biuld docs is something that can be tackled without a PhD in cryptography or indepth knowledge of C++ programming


## anonimal | 2016-08-15T12:14:25+00:00
@grummerd you don't have to install cpp-netlib as a dependency with your package manager; no where in the build instructions does it say to do that. Simply ensure that you have the dependencies listed in `Debian / Ubuntu` and then type `make dependencies`. If you still have trouble, please open a new issue in the kovri repository and I can help more there.

If no one else addresses this bitmonero build docs issue, I'll send a patch sometime soon.


## grummerd | 2016-08-15T12:17:59+00:00
Opened an issue
https://github.com/monero-project/kovri/issues/310


## moneroexamples | 2016-08-15T23:46:30+00:00
What about this:

https://github.com/moneroexamples/compile-monero-09-on-ubuntu-16-04


## grummerd | 2016-08-16T02:12:18+00:00
@anonimal I understand what you are saying now. The kovri documentation style is excellent. Quite easy to follow

@moneroexamples That's brilliant! Although outta this issue's scope, the development section could be used to help make Python3 wrappers, making bitmonero accessible to the Python3 development community

 [moneroexamples readme.md](https://github.com/moneroexamples/compile-monero-09-on-ubuntu-16-04/blob/master/README.md) should be linked at minimum to [monero readme.md](https://github.com/monero-project/bitmonero/blob/master/README.md). Then submit a pull request

Will definitely use this guide. If there are any suggestions, will send your way


## anonimal | 2016-08-16T04:08:25+00:00
> should be linked

The problem with cross-referencing documentation is that when one goes out of date, it's confusing to know which one is correct.  This is why we need to consolidate building documentation into the bitmonero repository and/or wiki.


## grummerd | 2016-08-17T07:27:29+00:00
@anonimal 
People shouldn't ever have to hunt thru Makefile and C++ code. Or guess which commands to use to install/build/use

Look forward to kovri being merged with bitmonero


## radfish | 2016-08-20T03:58:17+00:00
IMHO, the time would be better spent on simply packaging a .deb.

Current instructions are adequate for people who care to build the code from souce. For those users for who the instructions are not sufficient, the problem should be solved not by handholding through novel-sized tutorials but by packaging.


## grummerd | 2016-08-20T04:23:20+00:00
@radfish

docs first

deb later

Of course, you are right. Making it easier for ubuntu users is probably just not a priority. Also even with a deb still need to poke a hole into your router (open port) anyways, it's not too much to ask to install dependencies and issue a
./configure
sudo make
sudo make install


## dEBRUYNE-1 | 2018-01-08T13:04:51+00:00
+resolved

# Action History
- Created by: grummerd | 2016-08-09T15:28:25+00:00
- Closed at: 2018-01-08T14:24:31+00:00
