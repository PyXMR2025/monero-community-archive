---
title: Bug when recovering from seed
source_url: https://github.com/monero-project/monero/issues/6581
author: keffnet
assignees: []
labels: []
created_at: '2020-05-21T18:32:10+00:00'
updated_at: '2020-05-22T12:30:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When recovering a wallet from a seed it isn't clear if all the 25 words should be on the same row or if you can enter the words one by one. And if you do enter the words one by one then only 24 are accepted + an offset. See below,

Generating new wallet...
1 Specify Electrum seed:
2 Electrum seed continued:
3 Electrum seed continued:
4 Electrum seed continued:
5 Electrum seed continued:
6 Electrum seed continued:
7 Electrum seed continued:
8 Electrum seed continued:
9 Electrum seed continued:
10 Electrum seed continued:
11 Electrum seed continued:
12 Electrum seed continued:
13 Electrum seed continued:
14 Electrum seed continued:
15 Electrum seed continued:
16 Electrum seed continued:
17 Electrum seed continued:
18 Electrum seed continued:
19 Electrum seed continued:
20 Electrum seed continued:
21 Electrum seed continued:
22 Electrum seed continued:
23 Electrum seed continued:
24 Electrum seed continued:
25 Enter seed offset passphrase, empty if none:

--

I suggest either allowing only the seed to be entered on 1 line (and maybe show with one * per word) or just fix the bug and also allow multi line entering.

I prefer multi line since it could prompt you to correct a word if the word entered is not in the dictionary.

# Discussion History
## moneromooo-monero | 2020-05-21T18:58:48+00:00
You can do either one line for one word per line, either should be accepted.
Some seeds are 24 words, that's why it doesn't require a 25th if there is none. I suppose it could require an empty line in that case, but it seems complicating for no good reason.

## selsta | 2020-05-21T19:06:49+00:00
Did monero ever have 24 word seeds? AFAIK that’s only because dropping the checksum is also valid. I think the confusion was that @shyrwall thought the seed offset is the 25th word. But can’t think of a good solution here.

## moneromooo-monero | 2020-05-21T19:17:52+00:00
Well, yes, before the checksum got added :)

## keffnet | 2020-05-21T19:39:18+00:00
> You can do either one line for one word per line, either should be accepted.
> Some seeds are 24 words, that's why it doesn't require a 25th if there is none. I suppose it could require an empty line in that case, but it seems complicating for no good reason.

The problem is the 25 word seed doesn't work line by line :) Since it's expecting 24 words and then the 25th is the passphrase.

## keffnet | 2020-05-21T19:40:54+00:00
Or do you mean that if doing line by line the 25th word should not be entered at all? Because its a checksum? So the offset should just be empty.

If so I got it..

Unclear but I get it :D 

But still feels like a bug, Line by line could then just ask for 25 + offset. Where the 25th is the checksum. Same as one liner.

## iDunk5400 | 2020-05-21T20:51:47+00:00
It looks like `25` and `Enter seed offset passphrase, empty if none:` should be on separate lines.

## moneromooo-monero | 2020-05-21T20:57:01+00:00
I kinda skipped over the numbers mentally. I don't know where they're coming from, unless the output was manually altered to add them.

## iDunk5400 | 2020-05-21T21:01:17+00:00
Oh right, I didn't consider that.

## moneromooo-monero | 2020-05-21T21:28:34+00:00
For the record, since it's no obvious, the reason why it accepts several lines is because the seed is displayed on three lines, so it gets copy/pasted to a file for backup, so I expect it usually gets copy/pasted back as three lines.

## keffnet | 2020-05-22T03:40:33+00:00
> I kinda skipped over the numbers mentally. I don't know where they're coming from, unless the output was manually altered to add them.

Yes i just added the numbers manually so you could see the number of rows. 

## keffnet | 2020-05-22T05:24:40+00:00
If continuing the multiline input possibility this seems like a fix. Tested but not familiar enough with the code to know other impacts

[simplewallet.cpp.txt](https://github.com/monero-project/monero/files/4666206/simplewallet.cpp.txt)


## moneromooo-monero | 2020-05-22T11:09:53+00:00
Would that not prevent 24 word seed from being used ?

## moneromooo-monero | 2020-05-22T11:13:24+00:00
I checked, it would. But maybe one could add a check for an empty line, to say "I'm really done".
On the other hand, that 25th word is not needed in the first place, so I'm not sure it's worth the effort.

## keffnet | 2020-05-22T11:20:44+00:00
Ah.  Didnt even know there used to be 24 word seeds. 

I'm just thinking of it from a user aspect and most would have no idea the last one is a checksum and could be excluded. I sure didnt know and i would think i'm above the average joe :D

Just a suggestion to alleviate support request and/or thinking they lost the funds.

But up to you guys if its worth any change :)

## moneromooo-monero | 2020-05-22T12:30:53+00:00
OK. I think the "empty line stops" should work for both cases. You're the first ever to report that fwiw :)

# Action History
- Created by: keffnet | 2020-05-21T18:32:10+00:00
