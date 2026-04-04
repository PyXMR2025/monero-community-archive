---
title: '[Suggestion] Stop calling it StringCT'
source_url: https://github.com/monero-project/research-lab/issues/19
author: QuickBASIC
assignees: []
labels: []
created_at: '2017-10-01T06:46:49+00:00'
updated_at: '2017-10-30T14:56:00+00:00'
type: issue
status: closed
closed_at: '2017-10-30T14:56:00+00:00'
---

# Original Description
We all appreciate the work of Tim Ruffing, Sri Aravinda Krishnan Thyagarajan, Viktoria Ronge, and Dominique Schröder. I totally understand not wanting to use `RuffCT` as it doesn't give credit to the other researchers involved, but StringCT is a horrible alternative.

In English it has really bad connotations that we don't want to confuse new users with.

* you string things together (a string of pearls)
* a string is a series of events (a string of burglaries)
* a data type (a series of characters)
* denoting a particular sub-group of a sport team (1st string, 2nd String, etc)

Do we want to associate a cryptographic function with these ideas? Oh so the outputs are strung together/connected somehow? There's a string of events that make the cryptography work? The cryptography is being done with string data? There's some kind of cryptographic hierarchy in place? None of those things are strictly true, but the word `string` carries to much meaning to casually use it to credit the authors. RingCT itself is not named after it's author.

The authors will still receive credit and kudos from the Monero community even if their names are not used in this manner. 

I propose we use `RingCT 2.0` or `RingCT2` or `Enhanced RingCT` or `RingCT+` or `SL RingCT`, or any other name than this.

They're going to name it and call it whatever they choose, but as we hear more and more from the research lab and as we discussed it on Reddit the purple cat might already be out of the bag as we cement the name further in the minds of users and contributors.

# Discussion History
## anonimal | 2017-10-02T21:08:16+00:00
>RingCT 2.0
>RingCT2

If there is no scientific basis for using `string` (e.g., unlike string theory), then I agree.

## QuickBASIC | 2017-10-02T21:19:03+00:00
> If there is no scientific basis for using string (e.g., unlike string theory), then I agree.

It was an initialism created using characters from the researchers names to combat the use of RuffCT as they felt it was unfair to credit only only one author.

Dominique **S**chröder
Sri Aravinda Krishnan **T**hyagarajan
Tim **R**uffing
Viktoria **R**onge

`STRR-RingCT` became StringCT, which simply obfuscates what it is and does and adds nothing to understanding.



## anonimal | 2017-10-03T03:44:25+00:00
>STRR-RingCT became StringCT, which simply obfuscates what it is and does and adds nothing to understanding.

Yeah, that makes no sense at all. And what about the unlisted contributors? Should they be sought out to be included into the acronym?

Come on folks, we can do better than `StringCT`.

## sunday-afternoon | 2017-10-03T05:16:59+00:00
### VAST RingCT

Uses a letter from each contributor and highlights that a larger set is enabled.

## generalizethis | 2017-10-12T13:55:54+00:00
Is there a specific trait enhanced by this version of RingCT?

## QuickBASIC | 2017-10-12T14:06:50+00:00
@generalizethis 

I'm not a cryptographer or developer, but I believe it allows for more compact signatures at larger ring sizes.

With n being ring size:
RingCT ring signatures storage requirements are O(n).
RTRS RingCT ring signatures storage requirements are O(log n).

This means that a ring signature with a 1024 inputs will only be 2x the size of one with only 8 inputs, instead of 128x the size.

## acrelab | 2017-10-12T14:15:34+00:00
I'm a native English speaker and I'm not really convinced on the negative connotations of the word "string".

StringCT could be named after initials, could stand for `STrong Ring CT` or something.

If we wanna ditch `String` entirely then we could choose another word, or simply call it `RingCT2`.

```
StrongCT
RingCT2
2CT
RingECT (Ring Enhanced Confidential Transactions)
```

The core "ring" design hasn't changed and might be worth keeping in the name.

## fluffypony | 2017-10-12T14:18:42+00:00
I'd like to put forward some options:

- RingCT XT
- RingCT2x
- RingCT Classic
- RingCT ABC
- RingCT Unlimited

## QuickBASIC | 2017-10-12T14:21:05+00:00
> I'm a native English speaker and I'm not really convinced on the negative connotations of the word "string".

Sorry if I wasn't clear... I didn't use the word "negative", but I used the word "bad", but what I meant (and I feel I elaborated on) in the OP, is that the word "string" brings to mind different things than "ring" and it's still a ring and that leaves outsiders, newbies, etc wondering whats changed about the technology to change it from a "ring" to a "string"... and we're doing this just to credit the authors for their work.. I don't think the trade-off of possible confusion is worth it for the purpose of kudos.

> 
> I'd like to put forward some options:
> 
>     RingCT XT
>     RingCT2x
>     RingCT Classic
>     RingCT ABC
>     RingCT Unlimited
> 

@fluffypony maybe `RingCTGold` or `VertCT`? 😂😂😂

## hyc | 2017-10-12T14:47:39+00:00
We can keep the acronym: STRR RingCT. But I'd still pronounce it "stringCT" in spoken conversation. Maybe with a long rolled 'r' ...

## fluffypony | 2017-10-12T14:49:19+00:00
RingCT Cash

## QuickBASIC | 2017-10-12T14:57:33+00:00
> We can keep the acronym: STRR RingCT. But I'd still pronounce it "stringCT" in spoken conversation. Maybe with a long rolled 'r' ...

I think it's probably fine to call it `STRR RingCT` and pronounce it that way, but for all "official" (ha) documentation, research, communication we should retain the full text, so as to not to cause confusion.

What prompted me to create this issue was actually an update on Reddit where he actually used all three terms throughout. That's why I created the issue in the research-lab repo, because if anyone needs to be consistent about what it's being called, it's got to first be the researchers and developers, because they are going to set a de facto standard for what things are called.

## b-g-goodell | 2017-10-23T17:03:22+00:00
I'm simply going to call it RTRS RingCT in papers (this follows a common convention in pubs of using the initials of the first authors of a proposed scheme). Coding, on the other hand... I'll probably rename it RTRSRingCT or Log-RingCT or RingCT-25519. If someone wants to come up with a clever name and fork,  they can feel free.

## QuickBASIC | 2017-10-30T14:56:00+00:00
Doesn't seem to be any further discussion ongoing and the researchers seem resolved. I'm going to go ahead and close the issue... Thanks all.

# Action History
- Created by: QuickBASIC | 2017-10-01T06:46:49+00:00
- Closed at: 2017-10-30T14:56:00+00:00
