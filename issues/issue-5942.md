---
title: enforce 10 block age for spending of outputs
source_url: https://github.com/monero-project/monero/issues/5942
author: who-biz
assignees: []
labels:
- invalid
created_at: '2019-09-29T01:24:01+00:00'
updated_at: '2019-10-03T17:39:31+00:00'
type: issue
status: closed
closed_at: '2019-09-30T21:33:36+00:00'
---

# Original Description
The changes in https://github.com/monero-project/monero/commit/a444f06e53b218cc8bd091e5283828beb3e7d9af don't actually do anything to prevent this from happening on the protocol or blockchain side of things.  

My suggestion is using a hardcoded constant rather than the `CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE` and `HF_VERSION_ENFORCE_MIN_AGE` macros for this value.

# Discussion History
## xiphon | 2019-09-29T01:38:54+00:00
> The changes in [a444f06](https://github.com/monero-project/monero/commit/a444f06e53b218cc8bd091e5283828beb3e7d9af) don't actually do anything to prevent this from happening on the protocol or blockchain side of things.

It actually does. Could you elaborate what issue you are referring to?

## who-biz | 2019-09-29T03:00:57+00:00
@xiphon if you change `CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE` to `0` and `HF_VERSION_ENFORCE_MIN_AGE` to `14` in `src/cryptonote_config.h` (or some number higher than the next fork), transactions can still go through, it appears. 

## who-biz | 2019-09-29T03:03:57+00:00
Unless there is a hardcoded check added, that is dependent on values that aren’t macros... I believe this will still be the case. 

## xiphon | 2019-09-29T11:47:14+00:00
> @xiphon if you change `CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE` to `0` and `HF_VERSION_ENFORCE_MIN_AGE` to `14` in `src/cryptonote_config.h` (or some number higher than the next fork), transactions can still go through, it appears.

This won't affect the blockchain and Monero network anyhow. Other nodes won't accept such a tx.

> Unless there is a hardcoded check added, that is dependent on values that aren’t macros... I believe this will still be the case.

The check is hardcoded already.
Compiler treats `CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE` and `HF_VERSION_ENFORCE_MIN_AGE` macroses exactly the same way it treats `0` and `14` numeric values.

## moneromooo-monero | 2019-09-29T11:48:11+00:00
I'll leave this open for a bit in case someone points out an actual bug, and close it later if not.

## who-biz | 2019-09-29T13:57:55+00:00
@xiphon if you say so.  Although, we know that didn't stop a custom value from being considered valid in the past. But hey, your house ... your decisions.

## HorribleGelatinousBlob | 2019-09-29T22:15:00+00:00
I believe you have not read the code properly. It also seems you do not understand that macro and a constant are the same thing. I find it quite amusing that you fail to understand the most basic of programming concepts, yet try to lecture people about code you do not comprehend. Good thing you closed this, lest more people see you embarrass yourself

## who-biz | 2019-09-30T00:51:32+00:00
Oh, for once... put a sock in it @HorribleGelatinousBlob. No body is embarrassing themselves except for you. Your fixation on embarrassment also would imply fairly low self esteem on your part.

From what I can gather, macros seem to behave differently in C++ when we’re talking about distributed networks. It seems they are always interpreted locally? Something odd happening there.

I believe this is why the last pre-compile constant had no effect on consensus, and why I don’t believe this one will do any better. The best route would be using modern C++ keywords, if everyone is really hell-bent on sticking with the current constant management system. 

## HorribleGelatinousBlob | 2019-09-30T12:31:06+00:00
The compiler simply substitutes a macro with the constant it defines. Nothing you say makes sense. We don't need to worry about "what you can gather". This is well defined and well known behavior. Do a bit of actual research instead of wasting time making assumptions about what you think is happening. Every coder here knows how macros work. What you think is happening is irrelevant and makes you look like a fool. 

## who-biz | 2019-09-30T14:13:47+00:00
@HorribleGelatinousBlob, maybe you can explain why a spendable age of zero is currently considered valid by consensus then?

If you can find a better reason for that behavior despite the “hardcoded constant” in the current release, I’m all ears. 

Test this for yourself. And come back with an account that actually contributes to Monero. Or are we using sock puppets for fear of being associated with our words?

Edit: Also, to your point about "reading code": I'm much less concerned with how code reads, than how it works.

## HorribleGelatinousBlob | 2019-09-30T20:38:52+00:00
You're funny. worried about how code works when you don't read it or understand how macros work. Changes OpenSSL version in depends... calls himself a monero contributor. You've contributed more useless conversation than code. Spent too long with your head in the munny pot

## moneromooo-monero | 2019-09-30T21:29:01+00:00
No bug AFAICT and this is just pointless bickering now.

+invalid

## who-biz | 2019-10-01T02:19:42+00:00
> No bug AFAICT and this is just pointless bickering now.

I was under the impression that code not functioning as intended `is` a bug.  Unless of course, the intent is for that spendable age caveat to be meaningless? I suggest you test changing those values for yourself.

## who-biz | 2019-10-01T02:22:03+00:00
Oh, and the only reason this was reduced to pointless bickering is because no one addressed the issue. Closing an issue without addressing it seems dishonest, and unethical.

## hooftly | 2019-10-01T02:32:11+00:00
doesn't the network need to fork to version 12 first before this becomes part of consensus?  Or did you try this on Testnet?

## who-biz | 2019-10-01T02:38:18+00:00
>doesn't the network need to fork to version 12 first before this becomes part of consensus? Or did you try this on Testnet?

Testnet. I'm actively testing version 11 on BLUR currently.  Ported the changes in question.  That aside, I think we can gather that this wouldn't work if it didn't work last time...

Why repeat strategies that failed?  I've also written code for Qwertycoin & UltraNote (running live on both in production) that utilizes the macro irregularity, productively.

## hooftly | 2019-10-01T02:40:10+00:00
what does blur and dpow have to do with this?  I dont understand...  


## who-biz | 2019-10-01T02:41:40+00:00
Edited.  It means that I tested the same irregularity, and verified what I am claiming as a behavior of macros, on three separate codebases.  It is common to C++. Not just monero.


## HorribleGelatinousBlob | 2019-10-01T02:46:20+00:00
You know what they say...When everyone says you're wrong, then you're wrong. Post an actual issue with some actual evidence of a bug if you want to be taken seriously. Saying macros don't work in C++ is just going to (rightfully) get you laughed out of the room

## hooftly | 2019-10-01T02:46:40+00:00
can you provide an example from those bases explaining what you mean then?  im sure if you can articulate what the issue is and can show an example of it behaving as you claim people will listen?

## who-biz | 2019-10-01T02:49:17+00:00
https://github.com/qwertycoin-org/qwertycoin/pull/87

## who-biz | 2019-10-01T02:51:05+00:00
Implemented the same functionality in UltraNote.  The `PROJECT_VERSION` macro is evaluated locally for peers.  That code wouldn't work, without changing the code they were running too, if it wasn't. But it worked without changing a thing on their end.

Compile and test that code, if you don't believe me. Reading code won't help shift your understanding, if your understanding is incorrect.  Mine was too, until I tried it. That is, assuming this `is a bug`

## HorribleGelatinousBlob | 2019-10-01T10:10:57+00:00
i have already explained this to you. macros are not "evaluated". That implies some runtime logic. do some research. if i type "C++ macros" into google, this is the first result
[https://gcc.gnu.org/onlinedocs/cpp/Macros.html](https://gcc.gnu.org/onlinedocs/cpp/Macros.html)
This is basic level programming. What's more, 3 seconds on google will tell you why you are incorrect in your assessment. There is an old saying where i come from, maybe it will help you moving forward.

> Better to keep your mouth shut and be thought a fool, than to open it and remove all doubt.

## who-biz | 2019-10-02T16:10:00+00:00
Will 3 seconds on Google tell me that the dynamic linking in protocol potentially exposes information? (which is what we are talking about here... a node's version being exposed).  Not to mention possibly causing the issues with `SPENDABLE_AGE` too, which is the REAL issue here.

Or can we just have a real developer address this, instead of sockpuppets?  Seeming more disingenuous by the second, guys. Disappointing.

Edit: Oof, sorry.  Its the external linkage leaves version exposed.  Easy to confuse with all the `const char* const` going on in those files, coupled with the macros :)

## who-biz | 2019-10-02T16:14:46+00:00
A simple enough solution would be changing the constant management system to use C++ declarations, rather than C-style macros.  There's really no reason to use them for many of these. Oh, and actually compiling `cryptonote_protocol` into a static library, uniform to the rest of code. That library being compiled as a plugin makes this seem strangely coincidental.

So if it’s not a bug, say so. Then it’s intentional design. If it’s a bug, fix it.  I'll even volunteer to PR it.

## HorribleGelatinousBlob | 2019-10-02T21:59:29+00:00
 > Or can we just have a real developer address this, instead of sockpuppets? Seeming more disingenuous by the second, guys. Disappointing.

Yeah. can't do that. Everyone has just decided you have no idea what you're talking about and now refuses to engage with you seeing how you are clearly an idiot. I am also done here. You just have no idea what you're saying. want static linking, you can do that easily.  Do you also not realise that most of the code is written in C? Clearly not. Just go away, because no one cares about what you have to say here or anywhere else.

## who-biz | 2019-10-02T22:10:08+00:00
lol

## who-biz | 2019-10-02T22:12:29+00:00
Offer still stands to PR it :) Let me know if y’all change your mind. My changes work properly on the code I have the go-ahead to change without all of this shadowy and questionable behavior 

## who-biz | 2019-10-03T03:05:13+00:00
By the way, it’s absolutely disgusting that you guys don’t reject this kind of conduct in public discussions of your code.

## HorribleGelatinousBlob | 2019-10-03T09:42:21+00:00
Allow me to post here and excerpt from IRC


hyc
I vote we ban who-biz and clowns like him https://github.com/monero-project/monero/issues/5942

anyone who claims with a straight face that programs should use hardcoded constants instead of preprocessor macros needs to have their keyboard taken away from them
 
asymptotically
>From what I can gather, macros seem to behave differently in C++ when we’re talking about distributed networks. It seems they are always interpreted locally? Something odd happening there.
>The best route would be using modern C++ keywords
if you're writing a P2P application, you need to use constexpr and not define!!!
 
hyc
blah blah blah
 
hyc
this discussion is so mind-numbingly stupid I can't believe the participants are serious
 
ErCiccione
a ban sound excessive. Just invite them to not comment again, if they do, let's lock the issue.
 
dEBRUYNE
hyc: He has been great at wasting other's time
 
sech1
that was a funny read
who-biz is on that point of a Dunning-Kruger curve where he thinks he knows everything

As I said. No one cares what you think. But feel free to PR whatever you feel is important. It is an open source project and PR's will be evaluated based on their merit. 

# Action History
- Created by: who-biz | 2019-09-29T01:24:01+00:00
- Closed at: 2019-09-30T21:33:36+00:00
