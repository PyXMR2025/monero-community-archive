---
title: Error building on Ubuntu 18.04
source_url: https://github.com/monero-project/monero/issues/3901
author: mkanakis
assignees: []
labels: []
created_at: '2018-06-01T18:46:46+00:00'
updated_at: '2018-09-17T19:12:18+00:00'
type: issue
status: closed
closed_at: '2018-09-17T19:12:18+00:00'
---

# Original Description
Hey, 

I am trying to build monero on Ubuntu 18.04 and I get the following error:

![virtualbox_ubuntu 18 04_01_06_2018_14_41_30](https://user-images.githubusercontent.com/7622185/40857890-d8d28606-65dc-11e8-9be3-ebdd5f7c5c57.png)

The dependencies are installed as supposed to.
Anyone else having this kind of problem?

Thanks.

# Discussion History
## moneroexamples | 2018-06-04T05:51:13+00:00
No problems for me.

What version are you compiling? Current monero master branch, or previous releases?

## daniel-levin | 2018-06-17T13:53:03+00:00
I suggest correcting the system clock first, to see if that makes any difference.
What about your version of gcc? 

Have you made sure to run ``git submodule update --init``?

## moneromooo-monero | 2018-09-14T14:32:28+00:00
It looks like a compiler problem.
If no answer is given soon to the questions above, I'll close as invalid since it works for others.


## mkanakis | 2018-09-17T19:12:18+00:00
Sorry for the late response.
Problem is solved, there was an incosistency with some of the dependencies and their versions.
Thanks.

# Action History
- Created by: mkanakis | 2018-06-01T18:46:46+00:00
- Closed at: 2018-09-17T19:12:18+00:00
