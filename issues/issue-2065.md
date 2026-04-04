---
title: '[FEATURE REQUEST] Proving sending a payment without knowing the TX key (using
  input side of TX instead)'
source_url: https://github.com/monero-project/monero/issues/2065
author: JollyMort
assignees: []
labels: []
created_at: '2017-06-01T22:35:21+00:00'
updated_at: '2017-12-02T10:00:25+00:00'
type: issue
status: closed
closed_at: '2017-12-02T10:00:25+00:00'
---

# Original Description
So I was discussing with @luigi1111 regarding the new PR #1992 and an alternative idea to prove a payment was presented. Pasting the entire log below, but the gist of it is this:

1. Make a temporary TX with the same input ring as the original one you want to prove, but to some random address (the address doesn't matter, it's just to build a fully-compliant TX with the same input side as the one we're trying to prove)
2. Use the method from #1992 to reveal details of the temporary transaction
3. An auditor can compare the inputs of the temporary transaction with those of original, see that they're all matching, which proves that whomever built the temporary transaction also must have built the real one, and he will also know the amount from step 2.

Note: this can't prove the destination and it doesn't reveal the real output on the input side. It just proves making the original TX. Without knowing the original TX key, there's no way to link it to some address! Only if the recipient would assist the process and give ~~viewkey+address~~ TX shared secret to the auditor, could the link be established.

This is different from using the TX key, but it could be an useful fallback method in case the sender lost his TX key.

@stoffu since you coded up #1992 would you also be interested in this?

	jollymort [11:36 PM] 
	luigi1111 ok, anyways, when it gets merged i can update here: https://monero.stackexchange.com/a/3770/57

	[11:36] 
	but what do you think of the proposed method there as an alternative if the sender lost his `r`


	moneromooo APP [11:36 PM] 
	Well, Monero is kinda associated to Bytecoin ^_^

	jollymort [11:36 PM] 
	you could sign with the key-image on the input side to prove, yes?


	marmulak APP [11:36 PM] 
	yeah but monero is the redemption of cryptonote


	luigi1111 APP [11:37 PM] 
	yes

	[11:37] 
	though I wouldn't call it that

	jollymort [11:37 PM] 
	more like hostile takeover :smile:


	marmulak APP [11:38 PM] 
	;)

	[11:38] 
	crypto anarchists


	unknownids APP [11:38 PM] 
	fluffy is tft dont let them hold back the truth!


	moneromooo APP [11:38 PM] 
	Thank Fluffy Too


	luigi1111 APP [11:39 PM] 
	lol @jollymort

	[11:39] 
	I was responding to you

	jollymort [11:39 PM] 
	lol


	luigi1111 APP [11:39 PM] 
	you could sign with the output private key

	jollymort [11:39 PM] 
	the one getting spent?

	[11:39] 
	but then you'd reveal which one is it


	luigi1111 APP [11:39 PM] 
	yeah

	[11:40] 
	well

	jollymort [11:40 PM] 
	oooor!


	luigi1111 APP [11:40 PM] 
	you could do another ring sig

	jollymort [11:40 PM] 
	you could sign again with same ring signature!

	[11:40] 
	:smile:


	luigi1111 APP [11:40 PM] 
	just a new message

	jollymort [11:40 PM] 
	yup

	[11:40] 
	cool

	[11:40] 
	volounteers? :slightly_smiling_face:


	luigi1111 APP [11:40 PM] 
	you need a blockchain to verify, which kinda sucks

	jollymort [11:41 PM] 
	it's a fall-back method anyway

	[11:41] 
	for those who lost the cache


	luigi1111 APP [11:41 PM] 
	yeah

	[11:41] 
	you could also just sign against the key image

	[11:41] 
	no wait

	[11:41] 
	that would reveal index, nevermind

	jollymort [11:43 PM] 
	hmm, actually you'd just produce a random TX with the same input ring and reveal the r/R of THAT tx; that way the amount could be checked as well

	[11:43] 
	the TX can never be pushed to the blockchain because it'd be a double-spend

	[11:44] 
	that would let you reveal the details of the TX without even knowing the actual destination address

	[11:47] 
	or, to simplify: 1. make a temporary TX with the same input ring as the one you want to prove, but to some random address 2. use the method from #1992 to reveal details of the temporary transaction

	[11:49] 
	there's no way to prove you sent to a specific address if you lost the tx key, though


	luigi1111 APP [11:49 PM] 
	correct it's proving two different things

	jollymort [11:50 PM] 
	you can only prove it was you who made that TX, and prove the amount


	luigi1111 APP [11:50 PM] 
	who is the recipient vs who sent the funds

	jollymort [11:50 PM] 
	without recipient's viewkey+address, you can't make the link

	[11:50] 
	interesting stuff

	[11:50] 
	maybe stoffu would like to code another tool :slightly_smiling_face:

...

	moneromooo APP [12:40 AM] 
	What's the point in proving a payment was made if you don't prove it was made to the right destination ? You could have made it to yourself.

	jollymort [12:41 AM] 
	in a dispute, an auditor could ask the sender for this, and the recipient for the shared secret and establish the link

	[12:42] 
	or, the recipient could be proactive and immediately give the shared secret to the sender who could then use it to produce a full proofmoneromooo APP [12:40 AM] 

# Discussion History
## moneromooo-monero | 2017-06-04T09:50:11+00:00
You did not answer the question I asked though :)

If you want an arbitrator to arbitrate, you don't want to depend on a proof which needs honesty from *both* sides, or you don't know who's lying.

## JollyMort | 2017-06-04T11:34:58+00:00
Because there's no good answer. Point is, you can't do anything else if you lost the TX key :) If someone loses (or never records) the TX key, this would be the only remaining way to prove he was the one who made some specific TX. Maybe an use case is not apparent now, but it could be useful later on; or not. Just wanted to record it somewhere so it's not forgotten.

For example if you keep TX history disabled, and send to an exchange/shapeshift/xmr.to but forget the PID what can you do? You open a claim and tell them the TXID. If this is not enough to prove (it could be anyone making the claim, but what are the chances), you'd have to follow up with the proof which you could produce with the method above.

As a side note, this problem is a good example which shows the full strength of stealth addresses. Even if you know you sent to some entity, even you can't easily prove it, let alone some 3rd party trying to perform chain-analysis.

## stoffu | 2017-06-04T23:41:14+00:00
I came up with an idea of embedding the tx secret key `r` in the input ring signature itself, just like how an arbitrary message could be embedded into the range proof. Below is the recap of the ring signature scheme (where the ringsize is just one (reducing it to just the Schnorr scheme), but the same idea applies to ringsize>1):

```
[Generation]
k = random()
L = k*G
R = k*Hp(P)
c = Hs(Msg || L || R)
r = k - c*x
return (c, r)

[Verification]
L = c*P + r*G
R = c*I + r*Hp(P)
c' = Hs(Msg || L || R)
return c==c'
```

Here, the random scalar `k` can be "reconstructed" after the fact only by the sender knowing the secret key `x`:

    k = r + c*x

So, can't we just use `Hs(k)` as the tx secret key? Note that `k` itself can't be used as the tx secret key, because multiplying `G` to the both sides leads to

```
k*G = r*G + c*x*G
    = r*G + c*P
```

which means that anyone can easily tell which key is the real signer in the ring by comparing `r*G + c*P` with the tx pubkey `R = k*G`.

@luigi1111

## luigi1111 | 2017-06-05T01:01:44+00:00
@stoffu I think just going to a deterministic r is simpler and cleaner.

An actual scheme is not completely straightforward, but also shouldn't be too difficult, as we already have plenty of "one-time" data in every transaction that could conceivably be used as a seed.

## stoffu | 2017-06-05T02:08:19+00:00
@luigi1111 
Agreed. Is this something you (or someone else) may be working on sometime soon^TM? :)

## JollyMort | 2017-06-25T07:54:09+00:00
>@stoffu I think just going to a deterministic r is simpler and cleaner.

Wouldn't this undermine privacy in some cases? Sometimes we actually want to forget the **r**. If deterministic, and if someone's wallet private key would be compromised, apart from stealing all the funds, the culprit could also run all sent TX-es against some suspect address list and establish the links. But on the other hand, we could replace the wallet setting "Save TX key" with "Use deterministic TX key", and if set to False, go back to random and not saving it.

## iamsmooth | 2017-08-28T08:21:19+00:00
> it could be anyone making the claim, but what are the chances

On another cryptonote coin, one exchange has reported elsewhere that when a transaction is sent that visibly does not contain a payment ID, they routinely get multiple support requests claiming it.

That would be more difficult on Monero with RingCT though, since the imposters wouldn't know the amount.

## LordMajestros | 2017-08-28T08:41:23+00:00
Is this Aeon by any chance?

## iamsmooth | 2017-08-28T09:16:40+00:00
No, it was Bytecoin [link](https://bitcointalk.org/index.php?topic=512747.msg21161155#msg21161155), although I see now that the claim has been disputed. Anyway, its an obvious
way to try to scam some coins whether to not it has actually been happening.

## LordMajestros | 2017-08-28T09:17:22+00:00
I suppose there are people watching for those kinds of transactions. One more benefit of RingCT. Criminals are way too savvy.

## moneromooo-monero | 2017-12-02T09:15:01+00:00
+resolved

# Action History
- Created by: JollyMort | 2017-06-01T22:35:21+00:00
- Closed at: 2017-12-02T10:00:25+00:00
