---
title: 'Suggestion: "delinking" option for specific UTXO'
source_url: https://github.com/monero-project/monero/issues/1990
author: dnaleor
assignees: []
labels:
- enhancement
created_at: '2017-04-17T21:45:42+00:00'
updated_at: '2019-05-05T01:05:11+00:00'
type: issue
status: closed
closed_at: '2019-05-05T01:05:11+00:00'
---

# Original Description
The heuristic II attack described in this recent paper (https://drive.google.com/file/d/0B7e8g-wJId8md3FYUGF0TlB5NjQ/view) can largely be solved by either using a "one time address" that is being developped, but there is also another option which doesn't require additional addresses and may be more feasible in certain situations.

I am guessing some people think that sending some XMR to themselves "mixes" their coins a bit more, but this paper shows (and I also said this on IRC and reddit a few times) that it's actually worse for your privacy because you can potentially link the 2 newly created txo's (amount and change) together later on.

This is my proposal to solve this "issue". [imho it's not really an issue, it's just wrong user behaviour]

Say you receive coins and you want to do a "delinking" before you spend the coins. When you receive the transaction, the GUI shows a "delink" button that creates a RingCT transaction with this one input (and a bunch of decoys) and spends the amount completely (in one txo) to the wallet. In the CLI a new command could be something like this: 

`delink ringsize txid`

of course, just one output will be suspicious, so a zero-ringct txo as "change" will also be created. That way, it's impossible to know if you've send those coins to yourself or just spend them. [and IIRC, this is already implemented. if there is only one output, a second 0-output is added automatically]
The Heuristic II "issue" won't happen because the wallet will not select the zero-ringct txo as an input for a transaction.

PS: this is not perfect though, because researches will point out that if the change never is spent, it can be "guessed" that this was a delinking transaction. But it's also possible that a RingCT transaction will sometimes chose this zero-ringct txo as an input, so at least there is a possibility for obfuscation. I just add this, because researchers will otherwise point it out as a "flaw" ;)

---

Additionally maybe a warning can be shown in the GUI (and maybe also the CLI) if you are about to create 2 (or more) new txo's that will be send to your own wallet. Also a warning can be displayed if you are about to spend 2 utxo's that stem from the same transaction.


# Discussion History
## dternyak | 2017-04-18T03:26:59+00:00
Interesting proposal. 

I didn't see an explanation on why efforts aren't efforts better spent on "one time addresses/subaddresses".

Wouldn't it make more sense to kill two birds with one stone and create less link-ability in the real world (e.g. shapeshift knowing where they sent funds, even if the blockchain doesn't) as well as on the blockchain (based on various heuristic analysis) by focusing work on one time addresses?. 



## dnaleor | 2017-04-18T03:31:19+00:00
I support the subaddress / disposable address / one time address proposals :)
But this proposal can be complementary. It's adding an additional layer of protection.

edit: and it's easy to implement, and will solve the attack vector (well, it can't be enforced, so solving it completely is impossible, but users wouldn't be tempted to do the wrong thing)

## dnaleor | 2017-04-18T03:55:51+00:00
actually this suggestion solves a slightly different issue compared to disposable addresses:

disposable addresses hide the wallet address mainly, while the delinking would give the user plausible deniability on whether he has spent his coins or not. 

## iamsmooth | 2017-04-18T03:57:33+00:00
Well as you know Heuristic II is just a non-issue with RingCT. Since you will normally never receive a RingCT transaction with multiple outputs there is nothing to solve here. And if you did the wallet avoids using them both in the same transaction when possible (this wasn't previously the case, and it was possible less often in the past anyway, because so much more of your value would be received in multi-output transactions).

However, there is a case where someone could maliciously send you multiple outputs, so a method to delink in that case would be useful, and maybe it should even be done (or suggested) by the wallet by default.


## dnaleor | 2017-04-19T11:10:22+00:00
Maybe we could block the wallet from sending ringct transactions with 2 txo's to the same address? It can't be blocked at protocol level due to stealth addresses, but we can make it very hard for the end user.

(very hard, i.e. you would need to change the wallet code yourself and compile yourself)

## iamsmooth | 2017-04-19T21:10:56+00:00
It apparently is done deliberately by pools and exchanges who want to break up their outputs so payments can be made with locking less change. Possibly with other improvements to the wallet the need to do this can be reduced (though not entirely eliminated, at least for exchanges, because they can always receive arbitrarily large outputs as deposits). Also, maybe exchanges need to do this when withdrawing from cold storage? I don't know the details here but it is a tricky issue for sure.

## dnaleor | 2017-04-20T10:40:55+00:00
hmm, ok. So they actively use it. Not a mistake by users. Not easily solvable as we can't block it through consensus. 

## moneromooo-monero | 2017-04-22T08:32:51+00:00
If you send multiple outputs to your wallet, they should then be used in a single tx only if the amount to send can't be otherwise satisfied. See pop_best_value_from in src/wallet/wallet2.cpp.

## kewde | 2017-05-16T20:18:56+00:00
"However, there is a case where someone could maliciously send you multiple outputs, so a method to delink in that case would be useful, and maybe it should even be done (or suggested) by the wallet by default."

Any transaction which contains multiple outputs that go to the same sender should be tagged as malicious and should be locked in some way such that they aren't spend as inputs. A special config flag and a few debug messages should do the trick for exchanges.

"Well as you know Heuristic II is just a non-issue with RingCT. "
That's actually not completely true. Inversion the attack vector still renders it useful to some extent. If two outputs of one source transaction are generally _never combined_ to be a real spend (because one is change/zero), then any transaction using those two inputs must have used it as _atleast_ one mixin. 

```
+-------+---------+---------+--------+
| REAL  | MIXIN1  | MIXIN2  | MIXIN3 |
+-------+---------+---------+--------+
| tx1:0 | _tx2:0_ | tx3:1   | tx10:1 |
| tx6:1 | _tx2:1_ | tx4:1   | tx9:1  |
| tx7:1 | tx11:1  | tx5:1   | tx8:1  |
+-------+---------+---------+--------+
```

Here, we know that mixin 1 has the highest probability of not real because they share two inputs of tx2.

Or even worser, if you're terribly unlucky could do the following, where both mixin 1 and 2 are corrupt:
```
+-------+---------+---------+--------+
| REAL  | MIXIN1  | MIXIN2  | MIXIN3 |
+-------+---------+---------+--------+
| tx1:0 | _tx2:0_ | _tx4:1_ | tx10:1 |
| tx6:1 | _tx2:1_ | _tx4:0_ | tx9:1  |
| tx7:1 | tx11:1  | tx5:1   | tx8:1  |
+-------+---------+---------+--------+
```

The chances of picking the same transaction are _currently_ very slim, but a skewed distribution curve may interfere with that in the future. I propose you calculate the probability that you pick the same transaction as mixin, and if that value is too high then add a mechanism that prevents two mixins to come from the same transaction. (This does however affect people who make custom transactions)

Also @dnaleor,
"I am guessing some people think that sending some XMR to themselves "mixes" their coins a bit more, but this paper shows (and I also said this on IRC and reddit a few times) that it's actually worse for your privacy because you can potentially link the 2 newly created txo's (amount and change) together later on."

You might actually be right there, one of the txo's would be non-zero. The wallet does not detect that you're sending it to yourself hence creates a non-zero change output. Given that this user behavior persists it can create a chain of toxic outputs.





 

## iamsmooth | 2017-05-17T06:15:13+00:00
@kewde The mixins are independent across rows. So while it is unlikely that mixin1 is the real output for _both_ the first and second rows, this is only a very, very weak bias. It could still be the real output for one or neither.

Nevertheless I agree with your general point about inverting the attack vector. (Applies in some other cases as well.)

## kewde | 2017-05-17T12:27:00+00:00
@iamsmooth 
Ahhh well I was under the impression that there was a constraint on the columns? 
In other words: I assumed you have to know all the private keys of a single column to sign a RingCT TX.

Are you saying that the following situation can occur?
Sketching your scenario below in table format.
```
+---------+---------+---------+--------+
| MIXIN1  |    A    |    B    | MIXIN3 |
+---------+---------+---------+--------+
|  tx1:0  | _tx2:0_ |  tx4:1  | tx10:1 |
|  tx6:1  | tx12:1  | _tx3:1_ | tx9:1  |
+---------+---------+---------+--------+
```
Where both column A and B contain an input.

I think you may have misunderstood the situation I tried to sketch. 
A bit of explanation on the terminology, tx2:0 => output 0 from transaction 2.

I'm under the impression that there is a constraint on the columns.
https://github.com/monero-project/monero/blob/master/src/ringct/rctSigs.cpp#L116
Only _one_ secret index is passed to MLSAG_Gen.
On line 120 that index is checked if it is smaller than the amount of columns then it asserts to an error which makes me believe that one columns contains all the real keys. 

If there was no constraint on the columns, wouldn't there have to be multiple index numbers?

Edit, the quote above the function also seems to confirm this:
>    // Gen creates a signature which proves that for some column in the keymatrix "pk"
>    //   the signer knows a secret key for each row in that column

**EDIT: see comment below, the above scenario where column A and B contain real inputs is valid. The above mentioned MLSAG_Gen is called on each row independently**

----

So if you do come across a destination transaction which has a column that uses two inputs from one source transaction, then you can discard that column and mark it as a mixin with near 100% certainty. 

We know one of this columns must contain all of senders real inputs. There is no normal situation where two outputs of a transaction go to the same receiver. One of them is either change or 0, hence the column containing them will never be the real spends. 
```
+-------+---------+---------+--------+
| REAL  | MIXIN1  | MIXIN2  | MIXIN3 |
+-------+---------+---------+--------+
| tx1:0 | _tx2:0_ | tx3:1   | tx10:1 |
| tx6:1 | _tx2:1_ | tx4:1   | tx9:1  |
| tx7:1 | tx11:1  | tx5:1   | tx8:1  |
+-------+---------+---------+--------+
```

On a note, this explanation doesn't relate much to the original topic, but goes deeper into the inverse of the heuristic II attack.
 


## moneromooo-monero | 2017-05-17T19:57:02+00:00
I'm hazy with what you are saying right now, but the code you point to is called once per input when there are several inputs in a tx. The original rct code did what you say (and this is what is described in the paper), however Shen introduced another variant (the so-called "simple" version) where the same-index constraint does not apply.

## kewde | 2017-05-23T00:19:42+00:00
@moneromooo-monero Ahh, I wasn't aware of that. I took some time to look properly digest the code and it all makes sense now.

I don't know if the official reasons for this approach are documented anywhere, but removing the same column constraint is a pretty darn good idea. If it weren't like that then an attacker with one output as mixin would know that the whole column is not being spent. That's a lot of 'collateral damage', smart move for using the simple method. 

Recap for fellow readers;
The following situation is perfectly possible:
```
+---------+---------+---------+--------+
| MIXIN1  |    A    |    B    | MIXIN3 |
+---------+---------+---------+--------+
|  tx1:0  | _tx2:0_ |  tx4:1  | tx10:1 |
|  tx6:1  | tx12:1  | _tx3:1_ | tx9:1  |
+---------+---------+---------+--------+
```
Where both column A and B contain the real inputs being spent.

## moneromooo-monero | 2017-05-24T21:17:22+00:00
The reason was because this constraint would allow deducing things on other rings, as you said. The "same column" version is left in because it makes slightly smaller txes when there's a single input, so it gets used in those cases. Now, I kinda regret leaving it in, since it seems not that much gain for more code.

## dEBRUYNE-1 | 2018-01-08T12:45:19+00:00
+enhancement

## dnaleor | 2019-05-03T22:45:51+00:00
I would like to bump this post again.

Basically I think that an option to churn (I called it "delinking" 2 years ago) a certain TXO seems a good idea, regardless of what the MRL comes up with.

I can't see any disadvantages to have this in monero core. It could be integrated in the CLI with a command 

`churn txid`

In the GUI it could be integrated with a simple button in the transaction histiry, making it very intuitive to churn a certain TXO.

if there are disadvantages, please share your concerns. 

edit: I know there is a workaround to do this already in the CLI:
If you receive an transaction in a certain subaddress, you can sweep that specific address. But... If you receive more transactions at the same subaddress, there is no way to specify the txo that needs churning.

## iamsmooth | 2019-05-04T03:56:39+00:00
If you want to churn a single output, then you can't specify it by transaction id since as noted above in this thread there are situations when a single transaction contains multiple outputs (indeed this is specifically one situation when you might want to do this sort of churn).

## iamsmooth | 2019-05-04T03:59:18+00:00
BTW, there is already something called sweep_single in the wallet which I believe does this, right?


## dEBRUYNE-1 | 2019-05-04T06:10:10+00:00
@iamsmooth - That's correct as far as I know. It allows the user to sweep a single output. 

## dnaleor | 2019-05-04T09:17:42+00:00
ok, great, didn't know that.
So in theory we could have a "churn" button in the GUI? 

## SamsungGalaxyPlayer | 2019-05-04T15:42:29+00:00
Yes, there is sweep_single which seems to be exactly what you describe here.

There could be churn options in the GUI, but it currently doesn't have a way of showing the different outputs.

## dnaleor | 2019-05-04T15:48:21+00:00

> There could be churn options in the GUI, but it currently doesn't have a way of showing the different outputs.

The most intuitive place to have this is on the transaction history page. Just next to an incoming transaction, a "churn button" could be added.


## SamsungGalaxyPlayer | 2019-05-04T17:04:40+00:00
@dnaleor we would need a UI to convey sweeap_all or sweep_single, which will probably take a bit of work. Ideally it would also show outputs received from specific subaddresses to churn per-subaddress.

However, I would consider this specific issue closed since the feature is implemented in the CLI. Open a new issue in here for per-subaddress sweep, and in gui for the gui support.

## dnaleor | 2019-05-05T01:04:57+00:00
> @dnaleor we would need a UI to convey sweeap_all or sweep_single, which will probably take a bit of work. Ideally it would also show outputs received from specific subaddresses to churn per-subaddress.

I like you idea I heard today on the coffee chat for output management, but what I proposed here is just a "churn button" in the transaction history page.
By defenition, you receive txo's. So it would probably be doable to just add a button in the GUI that uses sweep_single in the background. 

That being said, yes, we can close this. 

# Action History
- Created by: dnaleor | 2017-04-17T21:45:42+00:00
- Closed at: 2019-05-05T01:05:11+00:00
