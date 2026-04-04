---
title: Tweak messaging in headline paragraph?
source_url: https://github.com/monero-project/monero-site/issues/570
author: robby-d
assignees: []
labels: []
created_at: '2018-01-23T02:12:56+00:00'
updated_at: '2018-03-01T21:59:30+00:00'
type: issue
status: closed
closed_at: '2018-03-01T21:59:30+00:00'
---

# Original Description
I generally lurk on the reddits and slack, and I've noticed a bit of a shift with how many are thinking about Monero. Whereas before, its privacy and fungibility aspects were highly emphasized as standalone -- almost abstract -- properties, many seem to be coming around to the more holistic realization that these are required attributes of good digital money first and foremost. I think this is a great development, as an analogous relationship to the _better_ properties of paper cash (specifically, it's accessibility, privacy, bearer instrument nature and fungibility) massively helps people initially grok the value of Monero. In doing so, it may also help deflect the "bad boy" narrative that the press loves to drape all over Monero: that it's a coin used by hackers, drug dealers, and people who are generally up to no good, and that by extension, _you_, not being one of these kinds of people, _don't need it_.

So with all that said, I wanted to get peoples' opinions towards tweaking the first paragraph on the website. You can see the current content by going to [getmonero.org](https://getmonero.org) (it's the next to the right of the embedded video, at the top). I'd like to change it to something like this:

**Monero**
**(tagline:) True Money** _(from the comment [here](https://github.com/monero-project/meta/issues/146) with the highest likes...or, have no tagline)_

**Monero is cash for a connected world. It’s fast, private and secure. With Monero, you are your own bank. You can spend safely, knowing that others cannot see your balances or track your activity.**

Justifications:

* The updated text is shorter and more to the point. It immediately likens Monero to something that virtually everyone intrinsically understands and values: cash.
* With the advent of 0-conf spending with the Kasisto POS, mobile wallets, and monero's shorter blocktimes, I think we have enough justification to say it is "fast". People understand and -- as we've seen with all the interest for things like IOTA, XRB, etc -- _value_ fast.
* I carried over the "private" and "secure" for obvious reasons.
* I kept the bit on "you are your own bank" because it's important, is understandable and is what cash is all about (being a bearer instrument).
* I added "You can spend safely, knowing that others cannot see your balances or track your activity" as a replacement to some of the copy I removed (which I detail below). Beyond being more succinct, this sentence just "feels" better to me -- it's more positive and conveys a feeling of relief, without making me feel like I'm using monero to do something bad or because I'm a paranoid nutter. Being able to spend safely where random others cannot see your balances is something that everyone both values highly, as well as being something that other cryptos simply do not have. (I.e. new crypto users slowly realize that all their transaction activity is viewable by _anyone_...it's not like their checking account or cash wallet!) 
* I removed "Only you control and are responsible for your funds" because it was redundant with "you are your own bank", and the "responsible for your own funds" is heavy and scary, and doesn't really mean anything when you consider that Monero is just like any other cryptocurrency in that the user is responsible for the security of their private keys.
* I removed "It is open-source and accessible to all." because I think it doesn't need to be in this first paragraph: most public-chain cryptos are open source and thus accessible to all, and most general users do not strictly care about this up front. It's like advertising a car by saying "it has air conditioning".
* I removed "Your accounts and transactions are kept private from prying eyes." because it's redundant and no longer needed with the new content, and a bit paranoid/negative.

With these changes, privacy is still given the attention it deserves, but in a way that makes it sound less like we're all walking around in black hoodies trading drugs with one another. Thoughts?

EDIT: Changed "Monero is cash for the internet" to "Monero is cash for a connected world", at the suggestion of @cryptoizzy 

# Discussion History
## cryptoizzy | 2018-01-23T06:58:07+00:00
I love it. I still think the tag line True Money is tops  (I’ve wavered between that and sound money, but I can’t help but Think true is more elegant). And I do think having a tag is important - especially as this one is so powerful and succinct. 

 Also your comments/edits on copy are bang on. 
The only thing I would tweak would be calling it ‘for the internet’. We all know internet connectivity is what’s behind the tech, but I think for many it may sound like game-credits or something that can only be used when internet shopping (ie, not person-to-person). I’d suggest changing that one bit to ‘cash for a connected world.’ I feel like most people associate connectedness with telecoms/data so that link is still there, but a bit smoother somehow. 



## robby-d | 2018-01-23T14:51:07+00:00
@cryptoizzy thanks, and I like that suggestion. I updated the wording to match. (I'm good with either "cash for the internet" or "cash for a connected world" but like the latter a bit better.)

## andromedona | 2018-01-27T21:54:01+00:00
I like it. It's more concise, less paranoid and noobs will probably grasp the essence a few seconds faster which in this age of zero attention span can't be stressed enough. Good job.

## Gingeropolous | 2018-01-28T00:22:02+00:00
id love to work in the other aspects of monero as well.

Perhaps "unrestricted" - we have the dynamic blocksize, which permits main chain access no matter what, and there is also the egalitarian mining, meaning that all you need is software to participate in the coin distribution process. 

## Gingeropolous | 2018-01-28T00:23:13+00:00
It’s fast, private, secure, and unrestricted. 

## Chicken76 | 2018-01-28T14:18:56+00:00
I see a problem with this sentence: "It’s fast, private and secure." specifically with the word "fast".
It cannot be used in the headline, especially as the first adjective, for multiple reasons.

1. "Fast" is not a binary property, as in either it is or it isn't. For example, you can say an apple "is red", or "is in my hand", but you cannot say it "is big" without specifying what you are comparing it to. You cannot accept "big" by itself. If you do, I have some very big apples to sell you (and because they're very big I'm asking a lot for them), only for you to find out after the sale that they're only very big compared to black peppercorns. :)

2. As an alternative to fiat, is it a faster payment method? Well, it's certainly not faster than reaching in your pocket and handing out banknotes or coins. It's not faster than contactless credit/debit cards, or even regular swipe-and-enter-pin cards. What it may be faster than is bank account transfers, especially if they are across borders, but even then, it's not always the case if you consider point #4 below.

3. Sure, it's faster than bitcoin, especially the bitcoin of recent years, but compared to the altcoins, is it fast? The answer is no. There are quite a number of altcoins that have shorter blocktimes than Monero, and also require fewer confirmations for the funds to be spendable. We cannot state this as true: "Monero achieves the fastest currency transactions possible today".

4. We live in a world that prices goods and services in fiat and uses it for the vast majority of transactions, not cryptocurrencies. If you're selling oranges and accept Monero, you're not selling 0.1 XMR worth of oranges, you're selling 30 USD worth of oranges, regardless of the method of payment. If you received Monero, you need to wait for it to be spendable (enough confirmations), send it to an exchange, wait for your account there to be credited, trade it for fiat and then initiate a bank transfer to your account and wait for it to go through. Only then you can pay your supplier. All of this takes days. It’s not fast. Cash over the counter is a lot faster for on-the-spot transfers. As for transfers at a distance, if you need to convert to fiat, then it’s faster for me to hop onto a night flight, haul my ass across an ocean, jump into a cab at the airport and show up at your door to hand you the fiat money in the morning. That’s how slow transferring value with Monero can be.

5. Monero is an electronic way of transferring value. It uses computers spread across the globe to record and validate the transactions and these computers are communicating with each other using the Internet. This is what a newcomer to cryptocurrencies should be told first about Monero. But for a newcomer “computers” and “Internet” imply “fast”. If you have to explicitly specify “fast”, then this question will automatically pop up: “Wait, are there ways of using the interconnected computers of today that are slower than using archaic methods?”. You don’t want to be in the position to have to answer that.


TL,DR: “Fast” has no place in Monero’s headline because:
1. Fast compared to what?
2. It’s not true. It’s slower than the no.1 method of payment: fiat
3. Even among cryptocurrencies it’s not in the top 10 fastest
4. To spend anywhere you need to turn into fiat, and that’s not fast
5. We use computers, Internet and very advanced mathematics and we open with “fast”?

## robby-d | 2018-01-29T21:24:42+00:00
@Gingeropolous I get the whole thing about unrestricted. my concerns with that is that having 3 items flows the best, over 4 (which reads as a bit of a mouthful). Also, I think the rest of the text kind of implies unrestricted: "With Monero, you are your own bank. You can spend safely, knowing that others cannot see your balances or track your activity" -- i.e. I can spend freely, and I hold my own funds...can do whatever I want with them, essentially.

PS: Thank you for your commentary in the reddits, etc. I enjoy it.

## robby-d | 2018-01-29T22:44:15+00:00
@Chicken76 : Thanks for the comment. I can respond to your points one at a time:

1. Agreed

2. Sure, I would agree with this, but also say that really no distributed ledger system is faster than handing cash to someone next to you right now, so I’m not sure if it’s the most apt comparison.

3. Agreed here too, but by making a claim of “fast”, it doesn’t automatically mean “fastest”, and we are not claiming that. Bitcoin until recently had a claim of “fast” as well on their website. You might disagree with that (as in, 10 minute blocktimes are not very fast today), but when considering how long it takes to say move 2 million dollars from the US to Germany, it is fast (Bitcoin’s other issues aside).

4. In many cases this is the case — and you can shorten this process down considerably in some cases by using services like xmr.to — but this is something all cryptos but _perhaps_ the most liquid (BTC and ETH, specifically) experience. They are are of limited real world use. Until recently, Raiblocks (XRB) was accepted only at 1 or 2 backwoods exchanges, but it was still considered “fast”. So, if anything, we see that the definition of what “fast” means can vary from person to person. You may be considering speed in purchasing a physical good and comparing it to USD, while someone else may be considering just making a transaction across the network to someone else. 

5. I honestly don’t think 99.999% of users will go there…most of them are either not that insightful, and/or they understand that the word “fast” is being used in a relative fashion, in comparison to other electronic means of transmitting value.

I respect your opinion on this, but I am still thinking at this point that you could justify Monero as “fast” when you consider that 
1. when comparing on a DLT basis, as just one measurement, Monero has much shorter blocktimes to Bitcoin, which until recently labeled itself as "fast". Just as important, unlike Bitcoin and other cryptos, Monero has viable spending of unconfirmed transactions — this is a huge advantage that the “fast” monkier can aptly describe.

2. when comparing in a physical/USD sense, to most people, moving value where it takes even 10-20 minutes to fully settle the change out is still a super “fast” experience, when compared to standing in line at a bank and dealing with wire transfer hell. Maybe not such when handing a 20 dollar bill to someone, but the term has numerous senses/meanings. Sure, you have cashing out at the exchange to USD, but it’s not necessarily required in all cases, and has to do more with the regulations over the actual tech (without regs it would be much faster). I would venture that most people see this as a “govt is slow” thing, not as “the tech is slow” thing (they separate the govt/AML-KYC red tape aspects from the blockchain itself).

3. “fast” can be used to hint at accessibility as well — the project is rapidly improving in that area, with Monerujo, Cake Wallet, the upcoming MyMonero, and so on.

What I will do is submit the text as a PR. If the repo maintainer has an issue with “fast”, I am happy to remove it.

## robby-d | 2018-03-01T21:59:30+00:00
thank you to all. this change is now live on getmonero.org. Closing this issue.

# Action History
- Created by: robby-d | 2018-01-23T02:12:56+00:00
- Closed at: 2018-03-01T21:59:30+00:00
