---
title: '[PROPOSAL] Encode restore height as 26th word of the mnemonic seed'
source_url: https://github.com/monero-project/monero/issues/6639
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2020-06-10T13:36:39+00:00'
updated_at: '2022-11-02T05:49:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The restore height is currently a value that has to be entered manually for wallets that are restored from either the keys or the mnemonic seed. The wallet will essentially ignore blocks (only pulling block hashes) before the restore height and start scanning (looking for transactions that belong to the wallet) from the restore height block. 

User experience is degraded if the user accidentally sets a restore height that is too 'high' (i.e. after the first transaction to the wallet), as the wallet will 'miss' certain or all transactions, thereby causing an improper balance (as well as transaction history) to be displayed. 

In order to improve user experience, we could encode an approximate restore height as additional word of the mnemonic seed. The restore height would then be set automatically upon restoring the wallet, thereby ensuring users will not inadvertently set an erroneous restore height. 

I personally do not see many drawbacks of this proposal. Guides will have to be updated to reflect the new format and users need to be informed. Users further, initially, may be slightly confused due to two different seed formats being present. However, I think ultimately the proposal is net beneficial to user experience. 

# Discussion History
## fluffypony | 2020-06-10T13:42:53+00:00
My suggestion is to encode it as follows: the position of the word in the wordlist * 21915 = starting block height. 21915 blocks is about a month's worth of blocks (half a month when the block time was 1 minute), so it gives us a good 135 years worth of coverage.

## SChernykh | 2020-06-11T08:11:14+00:00
This is too obscure, just use `Jun/2020` or something like this instead of a 26th word in the seed.

## rbrunner7 | 2020-06-11T08:29:32+00:00
As discussed on IRC, summarizing it here for broader publicity and discussion:

I am in full favor of adding one seed word to encode restore height.

But if we touch the seed system and add a "new" kind of seed encoding the restore height, I vote for taking the chance and add two more worthwhile changes at the same time. (Changing anything with seeds will be a larger endeavor,  and IMHO it would be a strategic mistake to come back to this with "new new" seeds a year later or so).

The "checksum" as implemented with the checksum word being simply a copy of one of the other words is very weak i.e. it does not catch a lot of errors. This can stay a single checksum word, but it should be calculated using a much more robust algorithm going over **all** words of the seed.

Furthermore, one more word should get added as the first word of the seed, encoding a seed version. The words used for the version should be **different** from all other seed words so you can reliably detect whether the first word given is such a version word or not.

This will enable a very robust UX. You can for example generate useful error messages if somebody enters only the first 25 words of a "new" seed for whatever reason, be it conviction that "more than 25 words are wrong", or input forms just not allowing for more words because not yet reworked / upgraded for "new" seeds.

Seed versions would also allow for adjustments in the word list, for whatever crazy reasons that may pop up, like some words becoming "politically incorrect", or more or less banned outright e.g. for Chinese seeds.

IMHO we should stick with words for both version and restore height encoding. Why? Because if it is anything else people will recognize it as something special and because of this some people may not treat them with the same care as the other words and e.g. simply not enter them, based on false assumptions like "I thought that's not part of the seed proper".

Maybe we should even go as far as avoiding that the exactly same word gets added as the version word to each and every Monero "new" seeds, possibly for years, because again people might get confused whether that seemingly constant world really belongs to the seed and is really necessary. People also could fear that Monero seeds are weaker than other coins' seed because of a word being constant.

This could be solved by using only the first letter of the word as the version and e.g. randomly chose from several words starting with that letter.


## nim4 | 2020-06-11T08:44:53+00:00
Maybe instead of adding a new word we can use first letter of each word to encode the timestamp in days(upper case=1, lower case=0).

For example using (unix timestamp / (60 * 60 * 24))

`general nomad tail jargon nodes lion scrub juicy palace puffin shipped rift vampire maze axes deity viewpoint timber textbook opened awesome gang object odds object`

will be 

`general nomad tail jargon nodes lion scrub juicy palace puffin Shipped rift vampire maze Axes Deity Viewpoint Timber Textbook Opened Awesome Gang object odds object`

## fluffypony | 2020-06-11T08:54:27+00:00
@nim4 clever idea, but having helped people who have inherited wallets from a deceased spouse you can bet that case sensitivity never factored into it.

## fluffypony | 2020-06-11T09:05:01+00:00
Regarding the seed version, why do we want to pick a word that isn't on the wordlist? We could just pick a random word, and use the same offset in other wordlists, which means no additional translation work.

I've also tossed around the idea of using a single word for both the version and the block height offset chunk. We could, for instance, use the first 3 bits for the version and last 7 bits for the offset (128 possible offsets, so maybe group it per year). Alternatively, if we really want to eek as much out of it as possible, we could divide the wordlist into 5 groups (so maximum of 5 different versions for this format), and then use the offset in each group, which would give us 325 words per group, so we each offset would be ~3.5 months.

## SChernykh | 2020-06-11T09:05:18+00:00
Another idea would be to use 27 word seed. `1626^27 ~ 1.008 * 2^288`, so we have 256+32=288 bits of storage there. Additional 32 bits could be used for 16-bit checksum (CRC-16 or similar), and 16-bit restore height with 5000 blocks (1 week) precision.

## knaccc | 2020-06-11T09:05:24+00:00
1. How much of this UX improvement could come from simply asking a wallet to scan backwards instead of forwards?

2. More of a stray thought than a proposal: the first 24 words of the base 1626 seed encode 256.01 bits of information, but a seed only needs to be 252 bits. So we have 3 bits extra there. It's fast and easy to brute force seed selection such that the seed mod (135*12) = restore block height / 21915. Since we have 3 bits extra already, this brute force only loses us 8 bits of entropy on the seed. It's already questionable as to how important it is for Monero to have a 256-bit seed instead of a hashed 128-bit seed.


## rbrunner7 | 2020-06-11T09:10:54+00:00
> Regarding the seed version, why do we want to pick a word that isn't on the wordlist?

Because it has many advantages to be able to reliably recognize the word as a version word, or in reverse see that the first given word is **not** a version for sure. This allows to detect all kinds of possible confusions, wrongly entered seeds, cut-off seeds etc.

I think especially with something as critical and sensitive as seeds we want our UX (and the transition from "old" seeds to "new" seeds) to be as robust as possible.


## sumogr | 2020-06-11T09:44:43+00:00
How on earth will the cli know the top height if i just want to generate a cold wallet without a daemon running . The above discussion requires an already connected cli wallet to an already fully synced daemon (maybe get the date from the system's timestamp? wouldnt that be dangerous?)

## rbrunner7 | 2020-06-11T10:01:42+00:00
> How on earth will the cli know the top height if i just want to generate a cold wallet without a daemon running . The above discussion requires an already connected cli wallet to an already fully synced daemon (maybe get the date from the system's timestamp? wouldnt that be dangerous?)

You are right, I forgot to mention this from the IRC discussion: There are various situations where restore height is not known. Beside your cold-wallet example, programs generating random seeds offline come to mind.

0 must therefore be a valid value for the encoded restore height, with a meaning of "restore height unknown". This can then be used e.g. to prompt for the restore height when restoring.

## trasherdk | 2020-06-11T10:59:06+00:00
Does the restore height have to be part of the check-summed seed?
Couldn't it just be a 32 bit hexadecimal number appended as 26st. word?
If it's there, it's the restore height. If not, ask.

## fluffypony | 2020-06-11T11:03:47+00:00
@trasherdk a single word is only 10 bits of entropy, so can't encode the actual restore height, but yes - this proposal is about adding an additional word for the restore height, plus a 27th word for versioning.

## trasherdk | 2020-06-11T11:23:04+00:00
The 25 word seed is pretty much set in stone for all eternity, unless you are willing to abandon all those paper-wallets out there, hidden in madrases or something. Right?

## fluffypony | 2020-06-11T11:30:57+00:00
@trasherdk I don't understand how this affects paper wallets? It's not like the old seed format would no longer be supported, there'd just be a new, default seed format. We already did this with the old English and new English wordlists, the old English wordlist still exists and you can restore an old paper wallet any time you want.

## rbrunner7 | 2020-06-11T11:41:37+00:00
> The 25 word seed is pretty much set in stone for all eternity, unless you are willing to abandon all those paper-wallets out there, hidden in madrases or something. Right?

Yes. There will be "new" seeds and "old" seeds with us forever. That's one reason why I am so vocal in favor of a system that is able to distinguish in a crystal-clear way between both sorts.

The first 25 words of a "new" seed should better **not** be a valid "old" seed for a system that, for whatever reason, never learned about "new" seeds. New version words outside the current word lists would nicely take care of this, because they make "new" seeds flat-out invalid for an "old" system. You won't be able to do something that only looks like a correct restore with the first 25 words of a "new" seed on an old system.


## fluffypony | 2020-06-11T11:51:36+00:00
@rbrunner7 it's already 2 words longer than the "old" seeds, so I don't think we need to worry about validity. Also if we move the checksum to the end, and make it a checksum valid for the whole of the new seed (and not just the key portion), then it'll fail checksum validation on an older wallet anyway.

I would like to keep the discussion going around versioning, as I've not yet heard an argument for an out-of-band word that makes sense to me, or even an argument for putting the version in an entire word instead of using the extra bits we gain from adding 1 word for both versioning AND initial block offset chunk.

## trasherdk | 2020-06-11T11:52:26+00:00
Okay, so far. Is there any reason the 26st. word cant be `00205263` for Height 2118243 ?

## knaccc | 2020-06-11T12:00:09+00:00
> Okay, so far. Is there any reason the 26st. word cant be `00205263` for Height 2118243 ?

Excellent point. Or as @asymptotically508 wrote on reddit, "I just write the date on the same paper as the seed.".

## rbrunner7 | 2020-06-11T12:00:36+00:00
> I would like to keep the discussion going around versioning

Fair enough.

Just for completeness sake: The GUI wallet currently does not insist on the 25th / checksum word, it also accept the "naked" 24 words. Not sure about the CLI wallet.

## rbrunner7 | 2020-06-11T12:06:32+00:00
> Excellent point. Or as @asymptotically508 wrote on reddit, "I just write the date on the same paper as the seed.".

Sure, but this assumes that people know about restore heights and their importance in the first place. Count the people on the Monero subreddit that don't and e.g. fail to correctly restore a wallet. (If they knew, and just did not know the correct restore height, they could easily go back far enough to be safe. It seems they often don't.)

Which is an important part of the motivation to touch the seed system and integrate the restore height, to do away with such problems as best as possible.

## knaccc | 2020-06-11T12:13:44+00:00
@rbrunner7 I agree, writing the date down and getting it wrong later can create problems.

I'll therefore revert to proposing the much more foolproof solution of changing nothing with the seed and just making the wallet scan from the current block backwards.

## rbrunner7 | 2020-06-11T12:16:13+00:00
> just making the wallet scan from the current block backwards.

Maybe I stupidly overlook something, but I have no idea how you would know when to stop scanning. How can you be sure my first transaction is not in block #1?

## knaccc | 2020-06-11T12:17:47+00:00
> > just making the wallet scan from the current block backwards.
> 
> Maybe I stupidly overlook something, but I have no idea how you would know when to stop scanning. How can you be sure my first transaction is not in block #1?

What does it matter whether the wallet still has to scan the entire blockchain? If this is about UX, all that matters is that we show people what looks like their balance as quickly as possible. 

If Monero has an [Eternal September](https://en.wikipedia.org/wiki/Eternal_September) then this solves the waiting problem for most.

## rbrunner7 | 2020-06-11T12:22:46+00:00
> What does it matter whether the wallet still has to scan the entire blockchain? If this is about UX, all that matters is that we show people what looks like their balance as quickly as possible.

Interesting approach which I might be able to agree with, if it were not for the weak checksum problem and the advantages that some sort of versioning brings as additional arguments to improve seeds.

## fluffypony | 2020-06-11T12:22:49+00:00
> Okay, so far. Is there any reason the 26st. word cant be `00205263` for Height 2118243 ?

Yes, that's not a word, and can't be encoded into many physical wallets (eg. Cryptosteel).

## knaccc | 2020-06-11T13:36:39+00:00
> Interesting approach which I might be able to agree with, if it were not for the weak checksum problem and the advantages that some sort of versioning brings as additional arguments to improve seeds.

I agree your proposal is better, if we were starting from scratch. I just don't think that due appreciation has been given to the confusion that will be caused when all of the documentation and tutorials and paper wallets suddenly have to start talking about 25 vs 26 word seeds.

## rbrunner7 | 2020-06-11T13:52:13+00:00
> I just don't think that due appreciation has been given to the confusion

A difficult assessment for sure. I hope for many people voicing their opinions here and on the Monero subreddit. I think Monero might have it easier here than many other coins because users were subjected to frequent changes anyway so far, with all our hardforks ...

## sumogr | 2020-06-11T14:12:22+00:00
Humbly and just to give  my two pennies worth
```
void simple_wallet::print_seed(const epee::wipeable_string &seed)
{
  auto timenow =  chrono::system_clock::to_time_t(chrono::system_clock::now()); 
  success_msg_writer(true) << "\n" << "Seeds generated at: " << ctime(&timenow) << "\n"; 
  success_msg_writer(true) << "\n" << boost::format(tr("NOTE: the following %s can be used to recover access to your wallet. "
    "Write them down and store them somewhere safe and secure. Please do not store them in "
    "your email or on file storage services outside of your immediate control.\n"
    "When restoring from seeds please use the date above to avoid needlessly scanning the entire chain.\n")) % (m_wallet->multisig() ? tr("string") : tr("25 words")); 
```

No extra word, no confusion, monero has already too many seed words compared to btc clones. 

## fluffypony | 2020-06-11T14:25:46+00:00
I don't buy the "let's not add extra words" story - 25, 26, or 27 words makes no difference to the end user. I also don't think that trying to force the user to write down a Unix timestamp is useful either, as that genuinely *is* an additional piece of out-of-band data that users will not always be able to write down (eg. if they use a CryptoSteel), nor can we communicate to them easily what "needlessly scanning the entire chain" actually means.

I would encourage people to have a non-technical friend try use the Monero GUI, and you'll quickly see how frightening mnemonic seeds are already. If we can make them easier to use then that's a win. And to be sure, abstracting any complexity around figuring out what seed it is will be abstracted away from the user, just like we don't ask them to specify the seed language before entering it in. They just type in their seed, and the wallet will figure out everything else.

## ghost | 2020-06-11T14:27:48+00:00
The restore height if added should also be made part of the checksum since the goal is to improve the experience for the new users, if the restore height is entered incorrectly it may lead to the user not having access to certain funds if they doesn't notice. Extending the seed will likely not be backwards compatible with all wallets anyway. Old mnemonic phrases can easily be supported in newer wallet versions. If someone generates a mnemonic seed in newer software the likelihood of them then later entering that seed in older software is low.  Also on the UI side not to confuse the user the software can simply ask for a "mnemonic seed" / "mnemonic phrase" without mentioning the amount of words it contains. If deemed necessary the UI could mention the different possible word counts in a tooltip: "NOTE: The mnemonic phrase is a list of 13, 24, 25 or 26 words".

On another note, we should use something like a digital pin board for the different approaches / proposals where people can add pros and cons to each so that there can be a debate that's simpler to follow. 

## rbrunner7 | 2020-06-11T14:29:39+00:00
> The restore height if added should also be made part of the checksum

Fully agree. Plus the version if we come around to add one. In effect, checksum goes over everything.

## fluffypony | 2020-06-11T14:30:27+00:00
> > The restore height if added should also be made part of the checksum
> 
> Fully agree. Plus the version if we come around to add one. In effect, checksum goes over everything.

Agreed, sarang had some ideas about that as well.

## knaccc | 2020-06-11T14:58:34+00:00
> I don't buy the "let's not add extra words" story - 25, 26, or 27 words makes no difference to the end user.

Here is an example of where it makes a difference:

One of the easiest ways to mess up is to miss out a word when writing down a seed.

Paper wallets are therefore very useful, because they provide exactly 25 boxes. Someone will notice immediately if they've missed out a word and not filled in all of the boxes.

Think of how many people will download a paper wallet that has not been updated to allow for 26 words, and accidentally skip a word because there are only 25 boxes.

Also think of the confusion when they have a 26 word seed and the paper wallet doesn't have enough boxes.

Note that I'm not making a stand against the proposal. I'm just saying that in my opinion, it doesn't seem like an earth-shatteringly great improvement to me, compared with just scanning backwards.

## fluffypony | 2020-06-11T15:04:45+00:00
@knaccc paper wallets can be redesigned to add an extra box or two, surely? Seems like a pretty easy fix that would accompany a major change to the seed structure.

## knaccc | 2020-06-11T15:05:39+00:00
> @knaccc paper wallets can be redesigned to add an extra box or two, surely? Seems like a pretty easy fix that would accompany a major change to the seed structure.

I'm sure they can be. I'm just pessimistic about the percentage of paper wallet designs out there that people will be bothered to update.

## fluffypony | 2020-06-11T15:05:57+00:00
Regarding scanning backwards: it's not terrible, but it does assume you've synced up first before you can start scanning. On a scan-forwarder scenario you could / should be able to sync up and scan at the same time.

## fluffypony | 2020-06-11T15:08:17+00:00
> I'm sure they can be. I'm just pessimistic about the percentage of paper wallet designs out there that people will be bothered to update.

That's a fair argument; besides the Monero.how paper wallet are there any other designs?

## knaccc | 2020-06-11T15:08:23+00:00
> but it does assume you've synced up first before you can start scanning

Are you suggesting it's acceptable from a security perspective to start downloading and verifying the blockchain mid-way, instead of from the beginning? At first glance, that does not seem wise.

Edit: I see now that's not what you're suggesting.

If you have not synced up the entire blockchain yet, there is nothing to stop you scanning backwards from wherever you are up to so far. In fact, that will be normal, because a new block may appear while you are backwards-scanning.

## rbrunner7 | 2020-06-11T15:09:26+00:00
> Also think of the confusion when they have a 26 word seed and the paper wallet doesn't have enough boxes.

I think perspective changes many things. I already quipped a few times on the Monero subreddit that our ancestors will see this and that or remember this and that on the 100th anniversary of the Monero genesis block in the year 2114. And this is not only joking: Monero, if really successful, will stay for decades. So I propose to plan for this. And a very, very robust seed system is part of that. And any succession period a small blipp in Monero's history.

## knaccc | 2020-06-11T15:23:21+00:00
> besides the Monero.how paper wallet are there any other designs?

Having searched, other than that one, the only other popular one I could find is this : https://www.themonera.art/2018/01/30/printable-monero-paper-wallet-pack-1/

Paper wallets maybe not the biggest problem then. It'd be more to do with the number of references on the web to "25 word seeds", and whether that would cause confusion or not.

I'm just being conservative by nature. I've seen how confused and worried people get about little things like "I'm scared to use the first 4... address in my wallet because I heard subaddresses provide more privacy".


## selsta | 2020-06-11T15:29:12+00:00
We added the restore height a while back to the wallet creation screen though I can’t say how much this helped with support requests.

<img width="1026" alt="Screenshot 2020-06-11 at 17 14 12" src="https://user-images.githubusercontent.com/7697454/84405576-9eabda80-ac08-11ea-9960-e6e1d93a92c5.png">

Also one thing to consider: Hardware wallets will always need a restore height because they don’t display a seed.

## knaccc | 2020-06-11T15:34:52+00:00
> We added the restore height a while back to the wallet creation screen though I can’t say how much this helped with support requests

I assume though that simply scanning backwards would have had the same effect.

## selsta | 2020-06-11T15:35:42+00:00
> I assume though that simply scanning backwards would have had the same effect.

Can you explain a bit more? Scanning backwards for how long?

## Cactii1 | 2020-06-11T15:36:37+00:00
> I assume though that simply scanning backwards would have had the same effect.

The wallet would still have to scan to block 0 as it doesn't know wallet creation date.


## knaccc | 2020-06-11T15:38:52+00:00
> Can you explain a bit more? Scanning backwards for how long?

You would always go backwards all the way back to zero. The point is though, you start to show people that things are working much more quickly, since most users will have txs near the end of the blockchain and not near the beginning. So you still go back all the way to zero, but that's now all in the background and all of the anxiety that their wallet balance may not appear will be gone.

## rbrunner7 | 2020-06-11T15:47:26+00:00
> all of the anxiety that their wallet balance may not appear will be gone.

A nice touch of this idea. A little minus point: It's possible it will show as negative over some scan time.

Note that we still can switch to scanning backwards, even with seeds that contain the proper blockheight.

## tobtoht | 2020-06-11T15:55:13+00:00
3 issues on the topic of seeds:

- Writing down a 24+ word seed every time you create a new wallet is bad UX.

We should look to decrease this number, not increase it. Does the average user even need 256 bits of security considering that the birthday problem is a complete nonissue if you factor in the time it takes to scan for outputs? It doesn't appear to be an issue on Bitcoin, and they have transparent balances.

Long seeds ruin the flow of disposable wallets with temporary paper backups because it's a pain to write the seed down every time. Long seeds also increase the likelihood of mistakes / missing words / bad ordering when copying.

Can we make the MyMonero-style seed the default for GUI users? Or at least have it as an option?

- Waiting for a wallet to scan irrelevant blocks (especially when bandwidth is limited) is bad UX.

Scanning the blockchain from height 0 over Tor can take hours, if not up to a day. For many users and for many different reasons running a local node is not got going to happen. To mitigate network-level metadata leakage syncing the wallet over Tor should be a supported use-case. Having the wallet sync backwards to block 0 will greatly decrease the practicality of this.

- Not having the full balance display after syncing a wallet is bad UX.

I like philogoly's idea to encode the restore height in the checksum word. Round it down to the nearest xK blocks or month, whatever fits. This way the concept of the restore height is abstracted away. Users no longer have to think about it. Wallets no longer have to explain the concept. Unnecessary syncing time is cut down by a substantial amount. Just enter your seed and you will always restore your wallet the same way every time.

## sumogr | 2020-06-11T16:54:23+00:00
> I don't buy the "let's not add extra words" story - 25, 26, or 27 words makes no difference to the end user. I also don't think that trying to force the user to write down a Unix timestamp is useful either, as that genuinely _is_ an additional piece of out-of-band data that users will not always be able to write down (eg. if they use a CryptoSteel), nor can we communicate to them easily what "needlessly scanning the entire chain" actually means.
> 
> I would encourage people to have a non-technical friend try use the Monero GUI, and you'll quickly see how frightening mnemonic seeds are already. If we can make them easier to use then that's a win. And to be sure, abstracting any complexity around figuring out what seed it is will be abstracted away from the user, just like we don't ask them to specify the seed language before entering it in. They just type in their seed, and the wallet will figure out everything else.

the advantage of monero compared to mimblewimble coins (whose tech i admire), while both serving the same purpose, is its comparative ease of use compared to the hell a mimblewimble coin user has to go through to get acquainted with their cli. Monero users had to suffer many changes during the past few years. Restoring from seeds happens once or twice during a user's "lifetime", a user restoring casually the same wallet is already acquainted with it and knows where to restore it from. There will be two kind of legacy seeds after this is applied. I think it will not make a difference in user experience (for example someone who knows how to setup tor and run monerod over socks knows for sure which height to restore his wallet from to avoid waiting for hours). Anyway :P 

## fluffypony | 2020-06-11T17:13:34+00:00
@sumogr I manned the MyMonero support email for a few years. Users restore more often than you think, and struggle way more than you'd expect. Most users do NOT know what they're doing.

## knaccc | 2020-06-11T17:15:44+00:00
I'm now in favor of the proposal, having thought about it more.

I just did a wallet restore with restore height=0, using the node.supportxmr.com remote node.

It took 1 hour 30 mins, and required a download from the remote node of 6.5 GB.

Since remote nodes provide by far the fastest way to get people up and running, this proposal would cut down the bandwidth requirements for remote nodes by 90% assuming the "eternal september" I referred to earlier. That's too great an advantage for me to ignore.

## fluffypony | 2020-06-11T17:20:56+00:00
@knaccc welcome to the pro-26th-word club :)

## ghost | 2020-06-11T20:00:49+00:00
> I like philogoly's idea to encode the restore height in the checksum word. Round it down to the nearest xK blocks or month, whatever fits. This way the concept of the restore height is abstracted away. 

@tobtoht I was only suggesting that the restore height also be checksummed not that it somehow be combined with the checksum word. If you were to combine the restore height with the checksum somehow let's say by XOR it would basically make the checksum useless since it would only lead to a corrupted restore height if any word is wrong. If that's what you were suggesting.

I have a radical idea for mnemonic seeds: while Monero doesn't have an easy way to store arbitrary data on the blockchain like other cryptocurrencies it could still be done by storing data in payment ids. Instead of the mnemonic phrase storing the entire private spend key with additional information such as a version and restore height it stores the decryption key and location of the private view key on the blockchain, this would require far fewer words but the cost would be users would have to pay a small fee in Monero to store the data. In the future if things were to be added one could encrypt that data as well for the newer wallet versions but the mnemonic seed phrase would have the exact same length.



## Cactii1 | 2020-06-11T20:11:57+00:00
How would that work if you don't have access to the wallet that allows you to decrypt the encrypted Payment ID ?

## fluffypony | 2020-06-11T20:12:26+00:00
@philogy apart from breaking the principle of "every transaction should appear indistinguishable" you also have the problem of having to scan the whole blockchain to find that transaction with your encrypted data, thus negating its value:-P

## ghost | 2020-06-11T20:32:27+00:00
@fluffypony good point. I was also suggesting that you'd also store the location in the blockchain in the mnemonic phrase:
> stores the decryption key and location of the private view key on the blockchain

> How would that work if you don't have access to the wallet that allows you to decrypt the encrypted Payment ID ?

Can't you publicly see payment ids anyway?

## ghost | 2020-06-11T20:37:25+00:00
Also the data would be encrypted before being stored in a payment ID so wouldn't the transactions still be indistinguishable?

## tevador | 2020-06-11T21:01:57+00:00
If we are going to change the mnemonic seed format, we should consider replacing the 256-bit Ed25519 scalar with a 128-bit seed (that can be passed to a KDF to get the private key). The elliptic curve provides only 128-bit level of security anyways, so there are not many reasons to have 256 bits of entropy in the mnemonic seed.

The electrum wordlist has 2048 words (11 bits/word), so we could have a **14-word** seed and encode:
* 4-bit version
* 11-bit restore height
* 128-bit private key seed
* 11-bit checksum

11-bit restore height is good for 170 years with a 1-month resolution.

## knaccc | 2020-06-11T21:07:31+00:00
> The elliptic curve provides only 128-bit level of security anyways

@tevador I asked about the necessity of 256-bit keys here: https://bitcoin.stackexchange.com/questions/72612/bip32-recommends-a-256-bit-seed-why-do-most-bitcoin-wallets-only-use-a-128-bit

(see the comment by Pieter Wuille)

It's not as satisfying an answer as I would like, but it was enough to convince me to err on the side of 252 bit keys.

## tevador | 2020-06-11T21:29:27+00:00
@knaccc I read the stackexchange comments and didn't find a convincing reason to use more than 128 bits of entropy. The Pollard's Rho algorithm can calculate the private key from the public key in `O(√n)` time and `O(1)` space. It's absolutely a real attack [[1](http://koclab.cs.ucsb.edu/teaching/ecc/project/2015Projects/Blumenfeld-Paper.pdf)], not just theoretical as Pieter Wuille's comment suggests.

With a 128-bit seed, there would be 2 possible attacks, both requiring the order of 2<sup>128</sup> steps. The KDF could be chosen in such way that the constant for the seed search attack is larger than the constant for the Pollar's Rho search, thereby not having any negative impact on the security of the private key.

## rbrunner7 | 2020-06-12T04:41:49+00:00
> If we are going to change the mnemonic seed format, we should consider replacing the 256-bit Ed25519 scalar with a 128-bit seed (that can be passed to a KDF to get the private key).

Just to fully understand: Would this mean that you can't ask an "old" wallet for a "new" short seed? If yes, I would count this as a point against it because it could make the transition harder.

## knaccc | 2020-06-12T06:43:20+00:00
@tevador Just to be clear: are you disagreeing with Pieter, and saying that the Pollard's Rho attack does NOT require significantly more memory/CPU resources than a straight 2^128 exhaustive search?

## tobtoht | 2020-06-12T06:56:24+00:00
>The electrum wordlist has 2048 words (11 bits/word), so we could have a 14-word seed

I would love to to see this. Questions that stem from confusion about the restore height make up a decent chunk of the Monero-related support work I do, even though I make an effort to explain what it is in the guides I write. I also often see complaints about the length of the current mnemonic seed, because it is cumbersome to write down and verify 25 words. 

For comparison: a Monero seed took me 2m 05s to write down and verify. A 12 word Electrum seed only 40 seconds. For two reasons: obviously length, and the fact that the Electrum word list contains easier English words. Compare the two and see for yourself: [monero](https://github.com/monero-project/monero/blob/master/src/mnemonics/english.h), [electrum](https://github.com/spesmilo/electrum/blob/master/electrum/wordlist/english.txt).

A shorter seed with embedded restore height would help in reducing the number of support queries related to seeds and is a great improvement in UX.

## tevador | 2020-06-12T07:04:31+00:00
@rbrunner7 That's correct. The only way to "convert" an old seed to the new one would be to send all funds to the new address. It's a disadvantage, but I think it's more than compensated by the big UX improvement of a much shorter seed. We would need to support the old style seed anyways.

@knaccc I don't think Pieter was referring to the Pollard's Rho attack. There are other ways to compute discrete logarithms which require more memory. Pollard's Rho has `O(1)` space complexity (see the paper I linked above).

My point was that by choosing an appropriate KDF, the 2<sup>128</sup> exhaustive search could be made more expensive than simply breaking the public key. In the Pollard's Rho algorithm, each step requires a point addition and a cheap hash function call, which together take under 1 ms. The KDF could be made to take e.g. 1 second per seed, which would make the exhaustive search on average 1000x more costly.

## knaccc | 2020-06-12T07:31:08+00:00
@tevador Ah, interesting, I didn't realize you were suggesting key stretching. That sounds appealing.

Talking of Pieter Wuille, there is an interesting [talk](https://www.youtube.com/watch?v=NqiN9VFE4CU) he gave about how CRC-32 is appropriate for single bit errors, but that Bose–Chaudhuri–Hocquenghem codes are appropriate for symbol errors. 

## tevador | 2020-06-12T07:57:43+00:00
> CRC-32 is appropriate for single bit errors, but that Bose–Chaudhuri–Hocquenghem codes are appropriate for symbol errors

I've been also thinking about this. These codes only work in <code>GF(q<sup>n</sup>)</code>, where `q` is a prime, so they wouldn't work with the 1626-word list, but would work with the the 2048-word electrum list. We could then use the much simpler Reed-Solomon codes because our seed is shorter than the alphabet size (Bech32 couldn't use Reed-Solomon because it only works for up to 31 symbols when using base32).

There would be these two options:
* 1-word checksum (11-bits), allowing any 1-word error to be detected.
* 2-word checksum (22-bits), allowing any 2-word error to be detected and a 1-word error to be corrected (e.g. if one word is unreadable or omitted).

The second option is probably unnecessary.

## rbrunner7 | 2020-06-12T08:15:49+00:00
> The electrum wordlist has 2048 words (11 bits/word), so we could have a **14-word** seed

For what it's worth our friends over at Ryo Currency switched to 14 word seeds about 2 years ago, see e.g. [this announcement](https://www.reddit.com/r/ryocurrency/comments/8vi6es/ryo_currency_free_radical_v020_release/), "with a proper CRC-12 checksum".

I was not able to find the corresponding code for this on their GitHub to check whether they went beyond switching the number of words and a better checksum algorithm, like we discuss here with version and height info encoded as well.

## tevador | 2020-06-12T08:45:24+00:00
@rbrunner7 Interesting coincidence. I checked the [source code](https://github.com/ryo-currency/ryo-currency/blob/3f809a3cb51d85e9c70fdf9820962c7f26e133fb/src/mnemonics/electrum-words.cpp#L273) and they don't seem to encode a version or restore height in their 14-word seed. 

This is how they use the 154 bits in their mnemonic seed:
* 128-bit private key seed
* 12-bit CRC
* 1 bit: long/short address flag
* 13 bits wasted

I'd call it suboptimal.

## tobtoht | 2020-06-12T09:53:40+00:00
>1 bit: long/short address flag

If we are going to switch to a different mnemonic seed format we should reserve one or two bits for this as well. I know this is a discussion for a different time, but Monero's long addresses are another major UX hurdle because of how poorly they are displayed in just about every user interface, especially on mobile and on websites. Ideally the address should fit on a mobile screen without linebreaks. Having spare bits available in the new seed format would decrease the friction to implement such scheme at a later point in time.

## tevador | 2020-06-13T20:00:34+00:00
Proof of concept: https://github.com/tevador/monero-seed

## rbrunner7 | 2020-06-14T05:46:21+00:00
[Reddit discussion thread](https://old.reddit.com/r/Monero/comments/h8ekuk/proof_of_concept_14word_mnemonic_seed_for_monero/) specifically for @tevador 's proof-of-concept.

Probably also notewhorthy that the [earlier Reddit thread](https://old.reddit.com/r/Monero/comments/h0uofc/proposal_encode_restore_height_as_26th_word_of/) about the proposal to add a checksum in general got only few downvotes and few posts speaking out against changing the seed scheme.

## SChernykh | 2020-06-14T07:54:33+00:00
@tevador I'll duplicate my reddit post here: are you sure hardware wallets can handle 256 MB Argon2id to restore the wallet?

## tevador | 2020-06-14T08:30:45+00:00
I checked the specs of Ledger Nano S and it seems to have only 10 KiB of RAM. In that case, the KDF would have to be downgraded to something like PBKDF2 with around 1000-5000 iterations, which should be suitable for hardware wallets. I think 1000 hashes should already exceed the costs of an EC point addition, which should make the Pollard's Rho search easier than brute force attack on the seed.

## rbrunner7 | 2020-06-14T10:57:01+00:00
I am a little unsure how hardware wallets would enter the picture here. Would this be for restoring directly on a hardware wallet using a Monero seed?

## ghost | 2020-06-14T11:04:28+00:00
Can we just use bip-39 and add an extra 11-bit integer, a word, either before or after the checksum? I know it might look stupid, but will it not work? I know you need two keys, but the second can be derived from the first no?

It's way easier for others who try to work with your software, if you can keep it close to a standard.

Last time I tried to implement your seed conversion algorithm was a failure, just speaking from my own experience.

## fluffypony | 2020-06-14T11:30:51+00:00
@fuwa0529 we already derive both keys from a seed.

## knaccc | 2020-06-14T14:26:09+00:00
Note that if we switch to the electrum wordlist, then when entering a seed, we'll need to enter the first 4 characters of each word to uniquely identify it.

The existing Monero wordlist only requires 3 characters of each word to be entered.

I understand that this is unavoidable so that the wordlist can be a power of 2 for Reed Solomon. So this comment is just an observation that the number of characters that need to be entered to restore a wallet will only drop from 75 to 56.

## rbrunner7 | 2020-06-14T14:54:42+00:00
> The existing Monero wordlist only requires 3 characters of each word to be entered.

For English 3 characters are enough. The other "European" languages need 4 characters already now :)

## sedited | 2020-06-14T16:43:53+00:00
@tevador nice proof of concept! To weigh in quickly on the KDF memory issue: The hardware wallets at the moment anyway don't make use of the monero entropy to key scheme. They derive their keys from within a BIP32 key that in return is derived from some BIP39 entropy. However even Scrypt is too memory intensive for hardware wallets, so using PBKDF2 with a high amount of rounds is probably the best solution on low memory devices currently. 

The new monero seed system could make proper use of the version byte and use it for encoding the type of KDF used by enumerating for example Argon, Scrypt and PBKDF2. Then a future low memory device could still generate a valid monero seed.

## SChernykh | 2020-06-14T16:45:02+00:00
> I am a little unsure how hardware wallets would enter the picture here. Would this be for restoring directly on a hardware wallet using a Monero seed?

Both restoring wallet from a seed and generating new wallet (new random seed) require calculating private key from the seed. If it's 256MB Argon2id then hardware wallets will have problems.

## knaccc | 2020-06-14T19:20:16+00:00
> However even Scrypt is too memory intensive for hardware wallets

If it's true that Hs(128-bit seed) provides a security level that is equivalent to a 252-bit seed, then why not either skip the key stretching, or just do 1024 rounds of keccak to add 10 bits of key stretching, and leave it at that?

## ghost | 2020-06-14T19:31:53+00:00
With keccak 256, you probably only need one round.

https://en.wikipedia.org/wiki/HMAC#Design_principles

## tevador | 2020-06-14T20:25:59+00:00
FYI, I changed Argon2id to PBKDF2 with 4096 iterations in my PoC. Should be fine even for low-end hardware.

> If it's true that Hs(128-bit seed) provides a security level that is equivalent to a 252-bit seed

They are equivalent except for a constant factor. I still recommend to use some key stretching since it's cheap and can make a bruteforce attack much slower.

## sedited | 2020-06-14T21:03:52+00:00
Another feature that I would like to at least have discussed is ciphering the entropy similar to what [aezeed](https://github.com/Casa/lnd/tree/master/aezeed) does (though not necessarily using the aez cipher). This way a user can choose a single additional password that is required in combination with the words. If the user exposes the password he can safely change it and subsequently the words without changing the underlying entropy and keys. I am not sure if that is desirable though, since it is mutually exclusive with BIP39 style '25th word' seed phrases.

## tevador | 2020-06-15T20:33:36+00:00
I made some improvements to my PoC:

* embedded network type (mainnet/stagenet/testnet) to prevent accidental misuse of the seed on a different network
* built-in way to make seeds incompatible between different coins, e.g. a seed for Aeon cannot be accidentally used to restore a Monero wallet; this can become important if other coins adopt the same seed format
* 3 reserved bits instead of 2
* removed explicit version field (version is implicit from reserved values)

One of the reserved bits could be used in the future to support some form of seed encryption as suggested by @TheCharlatan.

https://github.com/tevador/monero-seed

## rbrunner7 | 2020-06-16T06:03:56+00:00
Nailing the seed to a particular coin is done in a clever way, definitely an improvement.

> version is implicit from reserved values

I am not sure how you mean that. If finally you will give meaning to all 3 of these now-reserved bits, they can all be either 0 or 1. How would you reliably read a version out of this? And I note that already now we have at least candidate uses for all 3 of those bits, thus probably not a good idea to start to use the first one as a version bit - and "loose" it that way - sometime in the near future.

Encoding the network type is certainly a good idea, but I am really not sure whether it's worth to sacrifice an explicit version for this. It will be probably mostly devs and experienced people that will deal with stagenet and testnet wallets which will also know what they do. And restoring a wallet with the same keys on a different network might come handy for testing purposes. (Not impossible of course if you build in some "override" mechanism when restoring the seed on another network, but still.)

## tevador | 2020-06-16T16:58:36+00:00
> Encoding the network type is certainly a good idea, but I am really not sure whether it's worth to sacrifice an explicit version for this. It will be probably mostly devs and experienced people that will deal with stagenet and testnet wallets which will also know what they do.

You may be right. In that case, we could mark all 5 bits as reserved.

> I am not sure how you mean that. If finally you will give meaning to all 3 of these now-reserved bits, they can all be either 0 or 1. How would you reliably read a version out of this? And I note that already now we have at least candidate uses for all 3 of those bits, thus probably not a good idea to start to use the first one as a version bit - and "loose" it that way - sometime in the near future.

We have just 5 bits to use for versioning/features. That's 32 possible values. If we used e.g. 2 bits as an explicit "version" field, we would instantly waste 8 out of the 32 possible values because the 3 reserved bits have no meaning when version = `00`.

A better option is to use all 5 bits as a "version" field and assign functionality to each of the 32 versions.

IMO, an even better solution is to forgo the explicit version field and use just 5 "reserved" bits. This can work under the following two conditions:

1. Reserved bits are required to be `0`. The software should return an error otherwise.
2. When defining a new feature bit, `0` should be the previous behavior.
 
Example:

In the second version of the seed format, we decide to introduce 3 additional key derivation functions (KDFs), e.g. bcrypt, and 2 variants of Argon2. We can allocate 2 feature bits for this as follows:

* `00` = the original KDF (PBKDF2-HMAC-SHA256)
* `01` = bcrypt
* `10` = Argon2 variant 1
* `11` = Argon2 variant 2

The remaining 3 bits stay reserved and must be set to `000`.

As you can see, this update doesn't cause any issues:

* v1 wallet receiving a v2 seed with Argon2 KDF will return an error (as per condition 1 above) instead of restoring the wrong key
* v1 seed will work in v2 wallets because `00` is the original KDF from the first version (as per condition 2 above)

## rbrunner7 | 2020-06-16T17:57:23+00:00
> IMO, an even better solution is to forgo the explicit version field and use just 5 "reserved" bits.

After reading and thinking a bit this seems the best approach to me. No version, not explicit nor implicit, just feature bits, and there are 5 of those because 5 bits are left and not more.

Those feature bits come of course first, so we could change the whole "layout" of the seed, e.g. by defining a feature bit where a value of 1 means a better checksum is present that needs a few bits more, say 13 instead of 11, and we would get the 2 additional bits needed for that from making the restore height more coarse, reducing it from 10 bits to 8 bits.

And about that network story: If it becomes a real problem we could still use one of the feature bits where a value of 1 means "not usable for mainnet" or "not a mainnet seed" to guard against the most problematic case.

## Adreik | 2020-06-19T00:26:54+00:00
If introducing a new seed system anyway, why not also introduce a 49/50 word seed standard and have the private view key generated non-deterministically if using that seed type?

## fluffypony | 2020-06-19T05:32:18+00:00
@Adreik there's no real benefit from that, it's not like you can practically crack the spend key if you have the view key. Plus you can always generate the two keys non-deterministically right now using the CLI wallet, and back them up however you want. Someone is welcome to write a Javascript mnemonic encoder for such a task for the 2 people that will use it.

## knaccc | 2020-06-23T02:05:36+00:00
@tevador It occurred to me that it would be useful if when a user creates a couple of new wallet seeds, those new seeds are likely to have different first words. This will make them easier to distinguish from each other, and also has the side effect of not falsely creating the impression that Monero seeds are supposed to always start with a particular word. 

## knaccc | 2020-06-23T02:10:52+00:00
@tevador I've just created a [javascript implementation](https://github.com/knaccc/monero-seed-js) of your code. The [test file](https://github.com/knaccc/monero-seed-js/blob/master/test/test.js) shows how to use it. Run `node test/test` to run the tests.

I'm unable to parse your example test mnemonic though, so there must be a small difference between our implementations. It could be because we are using different Reed Solomon implementations.

According to your implementations, are these supposed to be valid RS encodings?
`0,0,0,0,0,0,0,0,0,0,0,0,0,0` and `0,1,2,3,4,5,6,7,8,9,10,11,12,52`

A quick way to test the RS JS implementation I'm using is to run this code:
```
const reedSolomon = require('reedsolomon');
const reedSolomonEncoder = new reedSolomon.ReedSolomonEncoder(new reedSolomon.GenericGF(2053, 2048, 1));
const mnemonicWordsLen = 14;
const mnemonicErrorCorrectionWordsLen = 1;
function reedSolomonEncode(unflaggedDataInt32Array) {
  let r = unflaggedDataInt32Array.slice();
  reedSolomonEncoder.encode(r, mnemonicErrorCorrectionWordsLen);
  return r;
}
var a = new Uint8Array(mnemonicWordsLen);
console.log(reedSolomonEncode(a)+'');
for(let i=0; i<a.length-1; i++) a[i] = i;
console.log(reedSolomonEncode(a)+'');
```

When you're applying the coin flag, you're doing that to the second mnemonic word, right?


## rbrunner7 | 2020-06-23T05:53:26+00:00
> @tevador It occurred to me that it would be useful if when a user creates a couple of new wallet seeds, those new seeds are likely to have different first words.

You mean if a program gets an order to produce 10 seeds, has produced 9 already, and then goes on to produce the 10th one, it would throw away candidates that are too similar to any of the previous ones and keep generating randomly until it get a really "different" seed?

Right now I can't see how, for single seeds produced independently, you can do better than just using a good source of randomness and hope for different first words.

## tevador | 2020-06-23T05:56:12+00:00
@knaccc 

> It occurred to me that it would be useful if when a user creates a couple of new wallet seeds, those new seeds are likely to have different first words

If you test my implementation, you will see that the first word changes for different seeds. That's because the first word is actually the checksum. The second word encodes the flags and the high bits of the wallet birthday, so it will stay mostly the same for seeds created in the same year.

My implementation orders the coefficients in ascending order, i.e. the constant term is first, then the linear term etc. This may also explain why you are getting different results. Try reversing the order of the words.

> When you're applying the coin flag, you're doing that to the second mnemonic word, right?

Correct.

## knaccc | 2020-06-23T13:53:01+00:00
> Right now I can't see how, for single seeds produced independently, you can do better than just using a good source of randomness and hope for different first words.

I had incorrectly assumed that the seed data would start with the 00000 reserved bits, followed by the 0000000000 birthday bits. This would have meant that all seeds created in the same month would have always started with the same first word.

Now I see that tevador's implementation is ordering the checksum word such that the first word would in fact be evenly distributed.



## knaccc | 2020-06-23T14:57:47+00:00
@tevador I'm not a C coder, so I'm struggling to test your RS library. Please could you tell me:

If I start with the data `0,1,2,3,4,5,6,7,8,9,10,11,12`, then after it has been RS encoded, what should the array look like? Currently mine looks like `0,1,2,3,4,5,6,7,8,9,10,11,12,52`.

I've tried altering my code so that it looks like either `52,0,1,2,3,4,5,6,7,8,9,10,11,12` or `52,12,11,10,9,8,7,6,5,4,3,2,1,0` but that does not seem to fix the issue.

## tevador | 2020-06-23T16:49:21+00:00
I'm getting `{358,0,1,2,3,4,5,6,7,8,9,10,11,12}`. My generator polynomial is `{2,1}`.

Have you tested `12,11,10,9,8,7,6,5,4,3,2,1,0,358`?

## knaccc | 2020-06-23T19:04:00+00:00
@tevador I'm out of my depth here with understanding the Reed Solomon implementation enough to know what my 'generator polynomial' is.

According to https://www.mathworks.com/help/comm/ref/rsgenpoly.html the default primitive polynomial for a Galois Field `GF(2^11)` is `D^11 + D^2 + 1`, which has an 'integer representation' of `2053`.

I'd initialized my RS encoder with `GenericGF(2053, 2048, 1)`, meaning `primitive=2053, size=2048, generatorBase=1`. The `size` appears to affect the size of the `expTable` and `logTable`.

I'm not sure if I am passing the correct values to GenericGF(). Can you suggest values what I should be using please?

This is the implementation I'm using: https://github.com/cho45/reedsolomon.js/blob/master/reedsolomon.js

Note that the implementation goes into an endless loop if I attempt to encode using `GenericGF(2053, 11, 2)` or `GenericGF(7, 11, 2)`.

## tevador | 2020-06-23T20:59:24+00:00
`2053` is the primitive of the Galois Field. I was talking about the generator polynomial of the RS code, which is initialized [here](https://github.com/cho45/reedsolomon.js/blob/master/reedsolomon.js#L352) in the javascript implementation.

I managed to reproduce my result with the following code:

```js
var rs = require('./reedsolomon.js');

var encoder = new rs.ReedSolomonEncoder(new rs.GenericGF(2053, 2048, 1));

const messageLength = 14;
const dataLength = 13;
var message = new Int32Array(messageLength);
for (var i = 0; i < dataLength; i++) message[i] = dataLength - 1 - i;

console.log('original');
console.log(Array.prototype.join.call(message));

encoder.encode(message, messageLength - dataLength);

console.log('rs coded');
console.log(Array.prototype.join.call(message));
```

output:
```
original
12,11,10,9,8,7,6,5,4,3,2,1,0,0
rs coded
12,11,10,9,8,7,6,5,4,3,2,1,0,358
```

Note that the coefficients are reversed compared to my implementation, but the values match.

## knaccc | 2020-06-23T23:36:13+00:00
@tevador Thanks, this has helped me ensure my RS encoding matches yours.

I have another problem: I'm using your test seed `test park taste security oxygen decorate essence ridge ship fish vehicle dream fluid pattern`.

The first data word is `park`, which is word index 1282. I then unflag this word by adding 0x539 mod 2048, which gives me `1282+1337-2048=571`. In binary, `571` is `01000111011`. This means the reserved bits are `01000`... but the reserved bits should all be zero, right? Am I missing something? The bits following the first 5 reserved bits are `111011`, which are the first bits of the correct quantized timestamp `1110111101`, so it looks like I'm almost getting the correct result, but not quite.

In my code, I get the entire 143 bits of the data (after unflagging) as:
`01000111011110111100011100001011010011110010001110010000100110101010111001100110001100000101011110111110001111010000101000101100110110100001010` or `23bde385a791c84d5733182bdf1e85166d0a` in hex.

Does that look right to you?

## tevador | 2020-06-24T06:33:22+00:00
> then unflag this word by adding 0x539 mod 2048

Addition in GF is XOR, so you have to do `1282^1337 = 59`.

## knaccc | 2020-06-24T11:09:27+00:00
@tevador Thanks, our implementations are perfectly compatible now! https://github.com/knaccc/monero-seed-js

I just thought I'd double check my understanding of RS with you (w.r.t. this scenario with a one word checksum):

1. If exactly one particular word is entered incorrectly, and all others are correct, and if the incorrect word is still a valid electrum word, then that error will always be detected. Although the error will be detected, it will not be possible to know which word in the mnemonic was incorrect.

2. Therefore the seed can only be corrected if the incorrect word position is known, and if there is only one incorrect word. In this circumstance, brute forcing the word from the electrum list will always find exactly one word that causes the mnemonic to validate (as an implication of point 1), and a false positive is impossible when brute forcing the word known to be incorrect.

## tevador | 2020-06-24T11:32:57+00:00
@knaccc 

1. Correct. Two ~~different phrases~~ phrases differing in just one word can never have the same checksum.

2. Correct. I should add that I'm using bruteforcing for error correction because we have just one check word. There are (more complex) algorithms that can correct errors efficiently for an arbitrary number of check digits. See for example [Berlekamp–Massey algorithm](https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Massey_algorithm)

## knaccc | 2020-06-26T21:45:42+00:00
I cross-checked the electrum words list against an English dictionary, and there is one word that stood out: "satoshi".

I'd imagine that we should be taking that word out and adding in something else... suggestions?

## hyc | 2020-06-26T21:53:41+00:00
If you want to claim electrum-compatible then we should be using their wordlist as-is, no?

## knaccc | 2020-06-26T23:31:21+00:00
@hyc I'm not sure if anyone was suggesting that it would be beneficial to be "electrum-compatible". The only reason for using the electrum word list is that it contains 2048 words instead of 1626. We've already broken electrum compatibility by having 14 words instead of 12/13, a different type of checksum, and a 'coinflag' applied.

I just checked, and the [non-English word lists](https://github.com/bitcoin/bips/tree/master/bip-0039) for BIP39 do not include the word 'satoshi'. So we'd only be messing around with the English wordlist. I'd argue that normal people will not recognize the word 'satoshi', and so the presence of this word slightly hinders the ability of a normal person to write down the seed or communicate it verbally to another.

One could make the argument that someone implementing 14-word Monero seed functionality could easily make a mistake if they did not notice that we had changed the English wordlist slightly. But I think that's a difficult argument to make, since their implementation would not be able to validate seeds generated by other Monero implementations, and it'd be hard to pay enough attention to successfully implement the Reed Solomon algorithm yet miss the implementation notes about the English wordlist being different.

## xiphon | 2021-04-24T21:52:49+00:00
Pinging @tevador and others interested.  
Please double check point 3, let me know if i'm missing something.


Current seed scheme is a two-way conversion, i.e. one can freely get a seed from wallet key on a wish.

Given that https://github.com/tevador/monero-seed PoC is a one-way conversion (i.e. you can't generate a seed from wallet keys):
1. No way to migrate current wallets to new scheme. All monero users will have to generate new wallets to use new seed scheme.
2. Requires to store the seed on disk and to load it on wallet startup to provide a way to print wallet seed (`seed` command).  
   Currently we convert wallet key into mnemonic seed on the fly.
3. I'm also somewhat concerned that it might affect security due to using only 128 instead of 256 bits of entropy.
    | Attack | monero-seed scheme | Current scheme |
    | - | :-: | :-: |
    | **Brute-force ALL seeds** | **2<sup>128</sup>** | **2<sup>256</sup>** |
    | Brute-force ALL key | 2<sup>256</sup> | 2<sup>256</sup> |
    | Recover 1 specific key (Pollard's Rho algo) | 2<sup>128</sup> | 2<sup>128</sup> |

    *\* omitted guessing a few wallet birthday bits in monero-seed case*

Opinions? Should we consider discussing some other seed scheme?


## tobtoht | 2021-04-24T22:05:38+00:00
>Requires to store the seed on disk and to load it on wallet startup to provide a way to print wallet seed (seed command).

An elegant solution to this problem is to store the mnemonic seed in `.keys`. This way it will always be available in case the wallet cache is discarded.

>omitted guessing a few wallet birthday bits in monero-seed case

Birthday bits are in addition to the 128-bit private key seed.

## xiphon | 2021-04-24T22:45:53+00:00
> An elegant solution to this problem is to store the mnemonic seed in `.keys`. This way it will always be available in case the wallet cache is discarded.

The point is about the additional logic that looks redundant to me.  We do store the keys and we will have to also store the seed basically in plaintext.

PS: yes. Obviously, `.keys` file is the only possible place to store the seed.  Using wallet cache would be a mistake.

> Birthday bits are in addition to the 128-bit private key seed.

That's exactly what i mean. You can't just count them in because actual range to brute force will be based on the implementation.

If 3) is a valid concern, a few extra bits barely change anything.

## tobtoht | 2021-04-24T23:04:58+00:00
>basically in plaintext.

As I'm sure you know `.keys` is encrypted on disk, so I'm not sure what you mean by this. The mnemonic seed would benefit from identical protection as the private spend key, and it can even be encrypted in memory until it is needed similarly to the other keys.

I don't see how storing an additional value in .keys is an issue at all.

>If 3) is a valid concern, a few extra bits barely change anything.

Yes, but there are no extra bits. Anyone attempting to brute force all possible spendkeys that can be generated with this seed scheme would just iterate over the 128-bit key seeds directly.

## rbrunner7 | 2021-04-25T05:45:33+00:00
My thoughts about those issues:

1\) is certainly unfortunate from an UX point of view, but I think we should take the long view here. If Monero really is successful as a currency it will probably live on for many years, if not decades, and all the wallets and all the users of the few years that already passed will become a small and therefore more and more unimportant minority over time.

2\) does not worry me one bit, frankly. Sometimes UX improvements lead to more effort needed in code, but so what? On other fronts person months are spent, e.g. to make transactions somewhat smaller and verify somewhat faster to improve UX, so surely extending the things stored in the .keys file somewhat should not matter too much. I sneaked in something there for the MMS, without anybody barely noticing, and it was programmed in half a day.

3\) Seems to me we are not talking about a key space of 128 bits versus one of 256 bits in isolation, but we are talking about Monero wallets in particular. And here I really wonder whether there is a viable method to even make, say, 1,000,000 attempts, to brute-force your way into a wallet in a reasonable time. How would that work, in detail? Seems to me brute-forcing stands and falls with a **fast** method to check whether guesses are correct. Is this given here?

## tevador | 2021-11-21T18:25:46+00:00
I revisited my PoC mnemonic seed and reimplemented it as a C-library. Should be pretty much plug and play and ready to be integrated into simplewallet.cpp.

https://github.com/tevador/polyseed

Some of the improvements I made:
* Added 2 extra words to increase the security margin. The total seed space (including the birthday bits) now exceeds 160 bits, which is similar to the total number of possible Bitcoin addresses.
* Better encoding to hide the non-random bits (seeds generated in the same month no longer have the same word in the 2nd position).
* All BIP-39 official wordlists are supported, including some of the special features such as prefix matching and accent-insensitivity.
* The seed can be serialized in 32 bytes (the library can decode this back into the mnemonic phrase). Should fit easily into the `.keys` file.

The only concern that remains is the one-way conversion. There is no way around it, it's simply the price to pay for a more compact mnemonic seed. But since we have to keep supporting the 25-word seed anyways, users don't *have to* generate new wallets. Legacy wallets would still have to input the wallet birthday manually, but eventually (as the blockchain grows), this prompt could be removed as the fraction of outputs created during the old seed scheme becomes negligible (I think this is the point @rbrunner7 was making).

## CryptoGrampy | 2022-11-02T01:22:54+00:00
Hi @tevador - 

It's been nearly a near since we've seen any movement on this topic; do you have any concerns with Polyseed/have there been any issues with its implementation in Feather? Do you think it should be added to GUI/CLI wallets?  

## tevador | 2022-11-02T05:49:22+00:00
I'm not aware of any issues with Polyseed. AFAIK it's still on the roadmap for Seraphis.

# Action History
- Created by: dEBRUYNE-1 | 2020-06-10T13:36:39+00:00
