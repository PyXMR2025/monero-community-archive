---
title: Unlock time's dual interpretation causes conflict in Feb 2019 with recent code
  changes
source_url: https://github.com/monero-project/monero/issues/5734
author: who-biz
assignees: []
labels:
- invalid
created_at: '2019-07-05T00:17:04+00:00'
updated_at: '2019-07-29T02:46:34+00:00'
type: issue
status: closed
closed_at: '2019-07-09T09:41:52+00:00'
---

# Original Description
See below

# Discussion History
## who-biz | 2019-07-05T00:19:05+00:00
I commented this on the commit, but since no one seems quick to respond to that route of action -- here it is again, for ease of reference:

This change is problematic: https://github.com/monero-project/monero/commit/1387549e905fc206426d3099b069bd28df0aad71#diff-1f77146989e4bf145cab519a8adbd48aR215 

Since XMR uses .xz-style encoding (and 0x01 signals the termination of concatenated data), changing this looks like its going to make the timestamp for say, Feb. 20th or so, conflict with block 1,550,6xx (or wherever has a timestamp that reflects a (block height)*(10<sup>3</sup>))...

## moneromooo-monero | 2019-07-05T00:47:23+00:00
By "dual interpretation", do you mean the fact that's is a block number or timestamp based on value ?

Where do you think monero uses "xz-style encoding" ? It might, I've no idea what it does. But I'm not going on your wild goose chase this time. Varints (unlock time is a varint) are encoded with the high bit cleared at the end.

For the conflict, explain what you think the conflict is.


## moneromooo-monero | 2019-07-05T00:48:47+00:00
And I don't read email, so I don't get notifications. Comment in PRs if you found something or I won't see it unless by chance.

## who-biz | 2019-07-05T01:49:47+00:00
>By "dual interpretation", do you mean the fact that's is a block number or timestamp based on value ?

I mean the fact that the `unlock_time` in the block structure is a varint field. This field is interpreted as block height in some scenarios, and in others (in simplewallet for example if the field exceeds a value of 500000000) as a timestamp.  Usually, this is "whichever comes first" that dictates it. That's incredibly problematic in many areas.

>Where do you think monero uses "xz-style encoding" ? 

Within its variable length integers.  These aren't as the description in `varint.h` implies.  See here: https://github.com/monero-project/monero/issues/2340

Edit: I misspoke in saying the xz-style encoding is what makes the difference here. It’s the behavior above.

The conflict is that with the `ar.stream_good()` at the end of the `KV_SERIALIZE_END` macro, the varint interpretation changes.  Now, the timestamp of 1556000(000) for example, will be intrepreted the same as a block height of 1,556,000.

If we're at that block height, then the timestamp  is 1555839480 aka 2018-04-21 09:38:00 UTC.

1556000000 or 1555839480 . . . which comes first?

You can call it a wild goose chase, but I'd call it more like me making two responsible disclosures and you guys spitting in my face. Not to mention, breaking HackerOne's terms of service (in the first one at least).  It's cool, like I said -- I didn't come there to get paid. But don't get all high and mighty about it.

I might add, as I’ve said to you before... that the flaw behind the first disclosure then became your “ledger bug”. 

## jtgrassie | 2019-07-05T03:00:03+00:00
I maybe missing something here but `ar.stream().good();` is not *writing* the data, it's signaling whether the serialization happened ok or not. So it's not clear to me what you're trying to get at.

## who-biz | 2019-07-05T03:16:26+00:00
@jtgrassie Yep.  I know that, and so do both of you. https://github.com/monero-project/monero/commit/db2b9fba651670a9c8f86c316f36bc9d9dbb82cc#diff-5be7f4b15905c17dfe82ebe394ffa10e

Edit: Well, serializing the data is kinda re-writing it.  So apart from that -- sure. 

I didn't think changing the way things were *interpreted*, sounded like I was implying anything about writing the data.

## jtgrassie | 2019-07-05T03:26:09+00:00
Your are saying:

> The conflict is that with the ar.stream_good() at the end of the KV_SERIALIZE_END macro, the varint interpretation changes.

And what I'm getting at is that `ar.stream().good();` does not change any interpretation. `unlock_time` is a varint regardless if the data it is holding can be used as a block time or timestamp. It's still just a 64 bit int encoded as a varint. The serialization doesn't care.

## stoffu | 2019-07-05T03:37:23+00:00
@who-biz

> The conflict is that with the `ar.stream_good()` at the end of the `KV_SERIALIZE_END` macro, the varint interpretation changes. Now, the timestamp of 1556000(000) for example, will be intrepreted the same as a block height of 1,556,000.

1556000 and 1556000000 are distinctly varint encoded as `a0fc5e` and `80dafae505`, respectively. Unlock time less than `CRYPTONOTE_MAX_BLOCK_NUMBER (=500,000,000)` is regarded as the block height as specified in the protocol (`Blockchain::is_tx_spendtime_unlocked` in blockchain.cpp).

What you've been saying here doesn't make any sense to me.


## who-biz | 2019-07-05T03:42:55+00:00
It cares here: 
https://github.com/monero-project/monero/blob/master/src/serialization/binary_archive.h#L169-L175

And a few lines further down, here: 
```
  template <class T>
  void serialize_uint(T v)
  {
    for (size_t i = 0; i < sizeof(T); i++) {
      stream_.put((char)(v & 0xff));
      if (1 < sizeof(T)) v >>= 8;
    }
  }
```

## who-biz | 2019-07-05T03:46:35+00:00
> 1556000 and 1556000000 are distinctly varint encoded as a0fc5e and 80dafae505, respectively

@stoffu I agree.  The issue isn't their representation in hexidecimal.  It's the fact that the mask and shift doesn't happen,  if the stream doesn't signal the end of data with a terminating bit.

## jtgrassie | 2019-07-05T03:46:51+00:00
@who-biz 

> It cares here...

>   template <class T>
>   void serialize_uint(T v)
>   {...



No it doesn't. That is uint serialization not varint. `unlock_time` is defined as a varint field so that is how it's encoded/decoded. ref: https://github.com/monero-project/monero/blob/9d7107c870d88885f43a8fd65739b1b70a5af668/src/cryptonote_basic/cryptonote_basic.h#L175

## stoffu | 2019-07-05T03:49:08+00:00
@who-biz 

I see your argument as non-issue unless you come up with an example tx blob that actually breaks the system.

## who-biz | 2019-07-05T04:20:55+00:00
@stoffu With all due respect, thats a bit of a cop-out. 

Although, at this stage, it seems already done. Just thought I'd let ya know that I find it concerning. 

## stoffu | 2019-07-05T04:26:30+00:00
@who-biz 

It's not a cop-out, it's just you failing to identify what issue there might exist.

## moneromooo-monero | 2019-07-05T08:44:12+00:00
There *is* a slight change in interpretation, but you get to explain why it is exploitable.
AFAIK, before the change, a value of 0x00 would be read as 0, and a value of 0x80 would be read as 0. With the patch, the first one errors out. Off the top of my head, I did not actually test.
Something being off by a factor of 1000 somewhere seems implausible to me.
If your claim is different, then you do get to explain how exactly.


## who-biz | 2019-07-05T08:57:04+00:00
@stoffu Or perhaps the explanation as much for those who don't see binary every day. 

It does look like someone over at Boolberry may have figured this one out already.  Commits happened the same week as the ones in XMR.  Weird.

## moneromooo-monero | 2019-07-05T09:00:29+00:00
STOP being vague. Point to EXACT patches. Don't make us guess what you're saying, looking for patches somewhere with so little information. I will not waste time again unless information is given, not hinted at.

## who-biz | 2019-07-05T09:02:58+00:00
I'm not referring to patches. I'm referring to the number conflicts.  https://github.com/cryptozoidberg/boolberry/commit/449485220b05bc1927378a09cc7fdd8e10199ddb

## moneromooo-monero | 2019-07-05T09:05:26+00:00
OK, you said commits, not patches. Fine.
I don't see what that commit has to do with varints.
Again, please be specific.

## who-biz | 2019-07-05T09:34:38+00:00
things look strange to me with the unlock time changes. I just think that liberal interpretation of block structure in a field like that is not a good idea mixed with untested changes. 

Take for example the fact that if the fail bit gets set earlythat you could be truncating a timestamp into block height. 

## moneromooo-monero | 2019-07-05T09:40:45+00:00
Ah, so there is one bit of information here. You think that the fail bit can be set early. If this happens before it should, then yes, you can ready the wrong value. Can you point out where you think that can happen ?

## who-biz | 2019-07-06T07:46:53+00:00
I am not saying it’s exploitable. I am saying I think this looks like it will cause problems.

## HorribleGelatinousBlob | 2019-07-06T07:56:09+00:00
The question was

> Can you point out where you think that can happen ?

This issue should be closed as invalid if this simple piece of information can't be provided. To just say 

> ...this looks like it will cause problems.

Is not meaningful, helpful or useful in any way. This is an issue tracker for actual issues. Not code you "think" might cause a problem.

## HorribleGelatinousBlob | 2019-07-06T08:13:29+00:00
I should also add a link to a recent [reddit](https://www.reddit.com/r/CryptoMoonShots/comments/bvbuny/moneros_lacking_security_and_privacy_in_node/) post from the OP, where he claims that hashing a block with the same nonce twice would expose your private keys. A direct quote:

> security breaks completely and can reveal your private keys if you hash the same block twice with the same nonce.

Draw what conclusions you may regarding the reliability and knowledge of the person posting this issue

## who-biz | 2019-07-06T08:17:59+00:00
I invite that. Why don’t you reveal the rest of that post? It’s clear that I’m not talking about hashing *a block* there. Chacha20 is a stream cipher and yes it’s breaks when you’re encrypting a stream larger than 2<sup>70</sup> bytes. Nothing in code guards against that except a comment that says it’s “user’s responsibility” to stop there. 

But you’re detracting from the issue with skewed quotes that lack context . Can we stay on topic please instead of attempting to smear someone like me 

## who-biz | 2019-07-06T08:21:11+00:00
Feel free to close the issue but I think it warrants discussion. 

## HorribleGelatinousBlob | 2019-07-06T08:25:32+00:00
OK. back to topic. The link to the thread is there if anyone cares to read it. @moneromooo-monero asked for a specific example of how what you say can happen and the effect. he is talking about an actual code example, or an example transaction that will break the current code. speculation has no place here. either there is a valid issue which you can demonstrate or there is not. there is no need to further this discussion without that.

## who-biz | 2019-07-06T08:30:16+00:00
Since when does discussion have no place here? https://github.com/monero-project/monero/issues/4533 There are a lot of prior examples of the issue tracker being used for discussion of past present and future issues. 

## HorribleGelatinousBlob | 2019-07-06T09:19:11+00:00
The title of this issue does not state this is a discussion. it states there is an issue relating to the interpretation of timestamps in block lock times. now you are being asked to demonstrate that. why do you refuse to provide a demonstration? what is the point of discussing code that appears to work fine with no proof provided to the contrary? why do we need a discussion if everything is working as it should? And if it isn't, why won't you show us how it is not working properly. You are just wasting everyone's time.

## who-biz | 2019-07-06T21:37:36+00:00
This is an issue, in my opinion.  You don't agree.  At which point, the issue became a discussion...  It's first grade, Spongebob.


## who-biz | 2019-07-06T21:39:58+00:00
For starters, our window to examine would begin at the value of `1341379000` since the code has the genesis block set to that value, retroactively, for some reason.

## HorribleGelatinousBlob | 2019-07-07T00:11:18+00:00
the problem is "your opinion". Either it is an issue, or it isn't. Your feelings on the matter are irrelevant. So the request remains open. Provide an example of how the code is broken, or at least point to some code that is relevant to the discussion. you still have done neither and try to continue this conversation with nonsense. Just provide something solid we can discuss, otherwise the only reasonable conclusion is that you are trolling.

## stoffu | 2019-07-07T04:38:04+00:00
If the fail bit is read early and the block blob wasn't fully and correctly received, then the block will surely be rejected when validating the PoW.

@who-biz 
> I just think that liberal interpretation of block structure in a field like that is not a good idea mixed with untested changes.

What do you mean by "liberal interpretation"?

At this point your objective seems to be to draw attention and waste people's time.


## who-biz | 2019-07-07T04:47:04+00:00
@stoffu True for current blocks. Not true for blocks that fall in the compiled hashes area that were also `keeped_by_block`. These are in the past and assumed valid. Not to mention, if the timestamp seems like a valid block, or vice versa, that nothing in a sanity check would catch them as they appear valid. 

## HorribleGelatinousBlob | 2019-07-07T05:08:46+00:00
You have now been asked many times to simply provide a demonstration of how this dual purpose field may be interpreted incorrectly. @stoffu is correct. you are wasting everyones time. If you are so sure there is an issue, it should be trivial to demonstrate it. Yet you refuse repeated requests to provide a demonstration or even a reference to some code you deem problematic. No one is able to follow the vague description you are providing and you are not providing the requested information to discuss this further. This is simply a troll, where it appears you have a history of trolling Monero.



## iamamyth | 2019-07-07T09:18:13+00:00
> @stoffu True for current blocks. Not true for blocks that fall in the compiled hashes area that were also keeped_by_block. These are in the past and assumed valid.

No. Nice try, but no. If they're in the past, it should be easy for you to provide a demonstration.

> Not to mention, if the timestamp seems like a valid block, or vice versa, that nothing in a sanity check would catch them as they appear valid.

You mentioned it, and it's utter nonsense.

Let me simplify the conversation: You are talking to a toddler who has learned to type. You have assumed this individual is learned, on account of being able to type. At some juncture, you must realize, if you continue on this path, your entire project is doomed, because many individuals can produce words on a page, and, if you respond to all of them, you lose time in building software. Do as you will. 

## moneromooo-monero | 2019-07-07T15:47:14+00:00
It's going the way as previous reports. If it's about blocks within the compiled hash area, then you have to say it in the first place, or you are indeed wasting our time again. If there's a problem, explain it. Don't say there's a problem somewhere but withhold information such as the above and let us try to guess at the problem. Reporting a problem is not a game of blindfolded darts. So if you are trying to report a problem, as I assume you are since you are posting here, give all the details so we can assess the validity of your claim.


## HorribleGelatinousBlob | 2019-07-07T21:33:13+00:00
This issue seems to be based on opinions and speculation and not in reality. when you say that it's your opinion the code is liberally interpreting data, then you just have no idea what you're saying. Remember that this is the same person who declared on reddit that

> security breaks completely and can reveal your private keys if you hash the same block twice with the same nonce.

I think this tells us everything we need to know.

## who-biz | 2019-07-08T20:37:11+00:00
> If it's about blocks within the compiled hash area, then you have to say it in the first place, or you are indeed wasting our time again.

That is hardly what I’m doing. Stoffu mentioned a block failing validation for the PoW. I was merely making the point that we are talking about historical, checkpointed blocks. The PoW validation argument does not hold up when we are speaking about historicals. You can call it blindfolded darts, but I’m merely speaking to your counterpoints. I’ve been busy with 9 vulnerabilities you guys dropped at once... so my apologies. Give me a few minutes and I’ll post a full description of what I am getting at. 

## lobstachub | 2019-07-08T20:56:15+00:00
Don’t give this child any attention 

## who-biz | 2019-07-08T21:29:35+00:00
For a "non-issue" this is being defended pretty vehemently.  I really wasn't trying to be adversarial, and have been attacked by many of you. All of which, upon the sole basis of your opinion: that the issue I speak of is non-existent.

This sort of behavior results in problems like the ledger bug *impacting users* before a choice is made to do anything about it. Rather than a mature response, the report I filed on the same underlying issue (lack of accounting for R') was met with profanity, instead of a "gracious response" as your VRP states. As a result, I'm sure you nearly gave the three users that had the ledger issue a heart attack. But yes, lets write off more reporters to be "fucking trolling," as you so eloquently put it on HackerOne (against their ToS, btw).

Are there words I've said in the past that were incorrect? *Yes. Of course.* When we find out we're wrong, we learn and grow.  When a developer won't admit that, and doesn't amend their perspective, the network and users suffer instead.  Humans have been *wrong* more than anything else in history.  Myself included.  So chill out. 

**Back to the topic at hand...** (Y'all make one *exhausting* gaggle of naysayers)

Let's suppose we have a timestamp = `0x59FF01FF`.  That's during the 5th of November, 2017 UTC.  

Correct me if I'm wrong... haha, of course you will :-) ... But this timestamp, as well as any varint which terminates in `FF` needs an additional '0x01' afterward, to account for the 7-shift and our final bit. 

```
Hex:         0xFF          |      0x7FF     |      0x59FF01FF
Encoded:       0xFF01      |     0x7FF01  |      0x59FF01FF01
```

Remember, Remember our block structure, we have: 

```
     | tx version | unlock time |   vin    | tx type | input height | ...... and so on. 
```

Also, note from [CNS004](https://cryptonote.org/cns/cns004.txt) - 

      - version: Version defines the transaction parsing rules (i.e.
      transaction content) and is incremented by each transaction format
      update. **Parsing transactions with transaction_prefix of an unknown
      version is not safe because transaction content could be
      misinterpreted.** Currently only transactions of version 1 are
      defined.

Recall that this is the *same reason* we define a `count` after a specified tag within the `tx_extra` if the length of that field is not implicit within the context of the field itself.  When we have a dual context, this creates issues and we have plenty of design examples to look at, in order to know when and where this matters most.  Most of these reside in the prefix, along with unlock time. 

Let's hypothetically assume that someone decided to mine a block at height 511 (0x1ff). They've also decided that they wanted to wait until November 5th, 2017 to actually spend those outputs. 

```
              | tx version |     unlock time   |   vin    | tx type | input height |  
Or:                   0x01  |     0x59ff01ff     |  0x01  |   0xff      |    0x1ff
Encoded as:        0x01     |   0x59ff01ff01     |  0x01  |     0xff01    |    0x1ff01
```

Doesn't it look like things will get awfully confusing if we have a failbit truncate that `unlock _time` varint into the value `0x59ff` (now a block height of 23039) instead? 

Edit: Before the crowd gets going, I know that protobuf changes the representation of these hex values more than I'm illustrating.  This is for explanatory purposes only. 


## jtgrassie | 2019-07-08T22:29:38+00:00
> But this timestamp, as well as any varint which terminates in FF needs an additional '0x01' afterward, to account for the 7-shift and our final bit.

Incorrect. 

1. You have just demonstrated you do not know how to encode/decode a varint. (`0x59FF01FF` gets encoded to `0xFF83FCCF05` *not* `0x59FF01FF01`)
2. You have just demonstrated your complete lack of understanding regarding the stream failbit in that a tx that fails serialization (failbit gets set), the whole structure is invalid - it failed serialization.

Therefore you have still failed at explaining _any_ potential issue. 

> Before the crowd gets going, I know that protobuf changes the representation of these hex values more than I'm illustrating. This is for explanatory purposes only.

When you are trying to say there is a problem with encoding/decoding but then base your whole thesis on an incorrect illustration and assumption of how it works, proves beyond doubt, you have no merit debating this. 

## lobstachub | 2019-07-08T22:31:10+00:00
Don’t give this child any attention

## jtgrassie | 2019-07-08T22:31:40+00:00
Yes, you're right. I'm done.

## who-biz | 2019-07-08T22:32:59+00:00
See the bottom of my post.  I wrote it the way I did for comprehension for readers, outside of your developers.  Say, the issues I raised about ZeroMQ and MiniUPnP.... @jtgrassie didn't you PR some of those suggestions?  After going on and on about me on reddit?  Come on.  Address the relevance in concept.  A **very** simple fix would be to include a flag to denote if a transfer has an `unlock_time` or an `unlock_height`.  Alternatively, a counter for the number of significant figures to follow. 

## who-biz | 2019-07-08T22:40:13+00:00
If someone cares to elaborate on precisely how the ambiguity somehow does not matter, that would be a very sufficient response.  Supporting points for why a counter or a flag wouldn't be less error-prone would be great, too. 

## HorribleGelatinousBlob | 2019-07-08T22:58:08+00:00
no one is vehemently defending anything except to have an issue tracker free from idiocy. fake issues detract from real ones and it seems that once again you are claiming the sky is falling with no evidence except some childish scribbles. you clearly don't understand how the code works. you are not qualified to an opinion on whether or not there is an issue

## lobstachub | 2019-07-08T23:09:50+00:00
Don’t give this child any attention

## who-biz | 2019-07-08T23:40:28+00:00
Let me know when the grown-ups are back to chat. 

## HorribleGelatinousBlob | 2019-07-08T23:55:34+00:00
The grown ups have come, determined your "issue" to be a non-issue, determined that you do not know what you're talking about and now left again. 

You should probably go and work on your 9 vulnerabilities and come back when you have something different to go chasing shadows about.

## moneromooo-monero | 2019-07-09T09:35:54+00:00
Thanks for the examole at last. It is incorrect, you are simply misunderstanding how it works. Open a new bug IF you come up with an actual bug (test it first, since it seems all your reports are wrong).
I'll ignore the paragraphs of baiting.

+invalid

## who-biz | 2019-07-10T06:02:44+00:00
No one has explained how the ambiguity does not cause conflicts. If you’re going to claim that this is invalid, or that I am misunderstanding — shouldn’t there be a reason for such a conclusion? 

The basis that the encoded representation in my example does not end in `FF01` (Read left-to-right) doesn’t detract from the fact that any unlock time which does, would exhibit that behavior. 

Should I open a new issue for this, and exclude the `ar.stream_good()` catalyst? I mean, *ignoring the fact* that the eof bit could be set, and the good() check wouldn’t catch it. 


## who-biz | 2019-07-10T07:10:18+00:00
>You should probably go and work on your 9 vulnerabilities and come back when you have something different to go chasing shadows about.

Particularly tasteful way to say: “Go screw yourself and have fun cleaning up our mess.”

Seems that you have an inability for empathy except when you need it from others... Still, I hope this kind of conduct between developers comes to an end.  The atmosphere your group creates is absolutely toxic.

## HorribleGelatinousBlob | 2019-07-10T09:04:13+00:00
You said there was an issue, repeatedly. there is no issue. you have a history of fearmongering and fudding monero. Taking all this into consideration, go screw yourself seems appropriate

## HorribleGelatinousBlob | 2019-07-10T09:09:15+00:00
And I should also point out you are not "cleaning up our mess". Monero, nor any of the contributors involved in monero owe you anything. It is your responsibility to make sure your shitcoin is kept up to date if you don't want to be left out in the cold when vulnerabilities are disclosed

## who-biz | 2019-07-10T10:50:02+00:00
I have more history contributing to Monero than doing any sort of fear-mongering. Further, I’ve been cursed at, flamed, and slandered by you and others for doing what? Disclosing vulnerabilities properly in good faith? 

Do you guys do anything in good faith? I don’t sink to the levels you’re operating on.  

Edit: I don’t mean that to include people who have been reasonable. I’ll name selsta and SGP as two who have been rational, and gone further than simple efforts to mislead/dodge questions.

Answering my questions that pertain to this issue would be the preferred and productive road to take. 

Food for thought: nobody defends the truth this way.

## HorribleGelatinousBlob | 2019-07-10T11:15:23+00:00
what truth? you have been told you don't know what you're talking about. simple as that. the only truth here is that you have claimed an issue exists when it doesn't. You have not disclosed any vulnerabilities. people that do that don't get abused and cursed at. just you. that would tell most normal people that it is in fact you who is the problem. food for thought.

## who-biz | 2019-07-10T13:14:55+00:00
And no one has explained a rationale behind the *opinion* that this is not an issue. Wonder why. 

## lobstachub | 2019-07-10T13:20:12+00:00
because you’re an ignorant child who is babbling nonsense. 

your intentions is to bait into some nonsense. You are best left ignored 

## HorribleGelatinousBlob | 2019-07-11T07:43:22+00:00
How many times must you be told. your understanding of how a varint is serialized is wrong. There is nothing more to discuss. it is not an issue, because what you think is an issue is based on you misunderstanding how the code works. if you can demonstrate that there is a problem, reopen an issue and post an actual working proof of the issue. until then, there is nothing more to discuss

## who-biz | 2019-07-11T22:24:34+00:00
Lol. No one told me that. I told you in my post. 

Since we’re so hung up on variable length integers and my understanding, it’s safe to say that you guys all understand them very well. 

Maybe someone could tell me how block height is encoded in this field, then, too? Also a varint? :)

## lobstachub | 2019-07-11T22:26:27+00:00
Get a formal education 

## who-biz | 2019-07-11T22:28:46+00:00
@tchun Please stop the incessant typeface vomiting. Or use your actual account instead of a sock puppet for disparagement. You’re looking like a bytecoin sock puppet right now. 

## lobstachub | 2019-07-11T23:00:24+00:00
Child please. You’ve wasted enough people’s time. 

## HorribleGelatinousBlob | 2019-07-11T23:14:04+00:00
moneromoo said you don't understand

> Thanks for the examole at last. It is incorrect, you are simply misunderstanding how it works.

jtgrassie also said you don't understand

> You have just demonstrated your complete lack of understanding

I also am telling you you lack understanding. But it is not the responsibility of monero or it's contributors to educate shitfork plebs who demand answers. You now just sound like a child throwing a tantrum. I hope you do not expect to be taken seriously in the future.

## who-biz | 2019-07-12T21:20:15+00:00
Thanks, Mr. Parrot. No, you guys don't care to explain things like this because you prefer simply saying "you don't understand".  It's a cop-out.  Look at how much time you're spending doing this instead of eradicating any "misinformation" I may be accidentally spreading.  Instead, you prefer to avoid actually answering the questions, and proceed with ad hominem attacks which -- lets be honest -- are a sign of weakness.  This leaves one to wonder *why* we would not want to answer the questions, despite criticizing others for their lack of understanding.  

**So again:  I'll ask that you explain how timestamps within the `unlock_time` field are kept from conflicting with `block_height` values in interpretation. Specifically if an EOF is reached in the middle of that field's stream, or through conflict in the `varint` representation of a timestamp versus the `size_t` representation within block height.**

## hyc | 2019-07-12T23:17:16+00:00
@who-biz You clearly decoded the varints incorrectly. That's not an opinion, that's a fact. The obvious thing for you to do is go look up what the encoding rules of varints actually are. Not to keep haranguing everyone here to teach you how the code works.

## HorribleGelatinousBlob | 2019-07-13T00:50:04+00:00
why do we need to eradicate your misinformation? just stop talking rubbish. you have been told go go away and do your research. there are many resources on the internet that will show you how this is done. don't want us spending time telling you that you are wrong. fine. stop posting rubbish.

as for explaining how unlock times are differentiated from block heights. read the code and you will find the answers you seek

## who-biz | 2019-07-13T22:54:34+00:00
@hyc I'm agreeing with you that those encodings are incorrect.  It says so in my original post.  

But you know what, you guys are probably right! I've seen the error in my ways in asking direct questions. Clearly, no one here is reliable for disambiguating code or concepts.  I guess from the outside, this maybe looks like you guys are the wrong people to ask questions.  It's ok.  I will source my information from elsewhere. I recommend others do the same. 

## iamamyth | 2019-07-13T23:17:02+00:00
Next time, you might want to read the github index page:

```
Built for developers
GitHub is a development platform inspired by the way you work. From open source to business, you can host and review code, manage projects, and build software alongside 36 million developers.
```

It's not meant for teaching people how code works, or how to code; it is for facilitating actual project development.

## HorribleGelatinousBlob | 2019-07-13T23:17:47+00:00
This is what we have been saying. This is an issue tracker. This is not a classroom to answer questions you demand answers to. Finally you have decided to seek answers elsewhere, which is what we have all been saying for days. But the joy of open source code is that you can read the code and have your questions answered. Seems to me you just have not done that. So why would you expect anyone here to answer your questions, when from all appearances you appear to have put in none of your own effort. Seems all your effort is spent on arguing with people who don't really care about your opinion.

## who-biz | 2019-07-13T23:26:00+00:00
I still strongly feel this is an issue.  This wasn't an attempt to learn from you guys.  It was an attempt to alert you to an issue.  You instead, focused on a point that is irrelevant to the conceptual core of this issue. I agree, you all should be working to fix this, not questioning semantics in order to divert.

## HorribleGelatinousBlob | 2019-07-14T01:39:55+00:00
thus is getting silly now. what you feel doesn't matter. show an issue. people dismiss you cause you say there is an issue, yet demonstrate a lack of understanding of how the code works and ask people to explain it to you. that makes your feelings invalid. no one is going to investigate any feelings from someone who doesn't know how the code works. you are just wasting yours and everyone else's time. I should also point out the programming in general is not subject to feelings. either something works or it doesn't. to that end, there appears to be no issue with how the code works, otherwise you would be able to show how it doesn't work. constantly replying here saying you feel like something is wrong is just pointless for the reasons I just mentioned

## who-biz | 2019-07-14T02:42:19+00:00
@HorribleGelatinousBlob why are you even polluting this discussion? You’re not a contributor to Monero.

## lobstachub | 2019-07-14T02:54:54+00:00
Why are you still replying to this when it’s closed

## HorribleGelatinousBlob | 2019-07-14T03:46:24+00:00
babysitting the children is my contribution to monero.

## who-biz | 2019-07-14T06:39:12+00:00
Because the issue still persists. Its okay. I’ll open a new one, if that’s what we prefer. 

## HorribleGelatinousBlob | 2019-07-14T07:56:17+00:00
the issue was closed as invalid because you demonstrated a lack of understanding of how the code works and could not identify an issue. You are free to open another issue, however without clearly articulating the issue, it will end in the same way

## who-biz | 2019-07-14T08:00:34+00:00
I've a feeling it will end the same way, regardless :)

# Action History
- Created by: who-biz | 2019-07-05T00:17:04+00:00
- Closed at: 2019-07-09T09:41:52+00:00
