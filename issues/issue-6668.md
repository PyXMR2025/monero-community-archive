---
title: '[Discussion] Consider removing the tx_extra field'
source_url: https://github.com/monero-project/monero/issues/6668
author: tevador
assignees: []
labels: []
created_at: '2020-06-20T09:37:55+00:00'
updated_at: '2023-04-27T01:40:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
First discussed here: https://github.com/monero-project/meta/issues/356

We should consider removing the tx_extra field from all non-coinbase transactions.

Main reasons:

1. Enhanced fungibility due to a more uniform transaction format.
2. Protection from the risks of arbitrary data on the blockchain, e.g. copyrighted material, privacy violations, politically sensitive or illegal content etc.

Required data that is currently stored in tx_extra (e.g. transaction public key) could be moved to a dedicated field.

Miner (coinbase) transactions could still allow the tx_extra field for the following reasons:

* coinbase transactions are already distinguishable
* the risk of harmful content is lower because it would require mining a block
* tx_extra is needed for merged mining

Disadvantages of removing the tx_extra field:

* losing the ability to soft-fork the transaction format

# Discussion History
## fluffypony | 2020-06-20T10:29:48+00:00
I support this. I'm perpetually worried about someone wanting to pack stuff into tx_extra unnecessarily.

## ghost | 2020-06-20T10:42:09+00:00
Are you suggesting giving mining pools the privilege to store arbitrary data into the blockchain?

## sumogr | 2020-06-20T11:03:53+00:00
afaik there is a proposal (an open pr) already from mooo to make use of extra to encrypt recipient's private data into it which is quite interesting https://github.com/monero-project/monero/pull/6410

## tevador | 2020-06-20T12:14:32+00:00
> Are you suggesting giving mining pools the privilege to store arbitrary data into the blockchain?

No. Currently anyone can store arbitrary data on the blockchain. We could either completely remove this option or keep it just for miners (e.g. for merged mining).

> afaik there is a proposal (an open pr) already from mooo to make use of extra to encrypt recipient's private data into it which is quite interesting #6410

The problem is that the consensus mechanism cannot *force* the data in tx_extra to be encrypted. A malicious sender can still include arbitrary data and claim that it's the ciphertext. Additionally, even the mere presence of encrypted data is a distinguishing factor for transactions (unless all transactions include data of the same length).

## sumogr | 2020-06-20T12:19:29+00:00
> The problem is that the consensus mechanism cannot _force_ the data in tx_extra to be encrypted. A malicious sender can still include arbitrary data and claim that it's the ciphertext. Additionally, even the mere presence of encrypted data is a distinguishing factor for transactions (unless all transactions include data of the same length).

There's supposed to be an off-chain agreement-trust between sender and receiver already, for this to be working, i agree with that, that's the point (assuming i understood mooo's intentions correctly). Padding of arbitrary data up to a pre-specified size was already suggested for uniformity, indeed.  



## tevador | 2020-06-20T12:38:10+00:00
> There's supposed to be an off-chain agreement-trust between sender and receiver 

A malicious sender doesn't need an agreement with anyone. As an extreme example, imagine a KYC exchange started sending the recipient's name and amount in tx_extra.

## sumogr | 2020-06-20T12:44:19+00:00
> > There's supposed to be an off-chain agreement-trust between sender and receiver
> 
> A malicious sender doesn't need an agreement with anyone. As an extreme example, imagine a KYC exchange started sending the recipient's name and amount in tx_extra.

there i agree but i already can encode in the tx extra my name or yours, if i knew it, into any tx. Anyway it will be an interesting discussion, lets see

## ghost | 2020-06-20T12:53:23+00:00
@tevador 

> We could either completely remove this option

I like this.

## hyc | 2020-06-20T13:27:36+00:00
>     * losing the ability to soft-fork the transaction format

This bothers me a bit, but really, when have we soft-forked anything? So far all changes have been hard forks.

## SomaticFanatic | 2020-06-20T16:33:18+00:00
Also support removing tx_extra. Increasing fungibility is always a good thing. Is this a holdover from Bitcoins way of doing things? What, do people imagine, was the motivation for including it in the first place?

## tevador | 2020-06-20T16:48:43+00:00
This proposal by @UkoeHB is also relevant: https://github.com/monero-project/monero/issues/6456

It suggests removing all non-optional parts of a transaction from the tx_extra field.

## UkoeHB | 2020-06-20T16:58:42+00:00
My argument against removing the extra field completely (copy pasted from #6456):

The Monero core team cannot see the future nor evaluate all possible usecases of Monero. To a large extent, it is up to users how Monero actually gets used. If there is a feature which only a subset of Monero users find valuable, it requires adding data to transactions, and the core team either isn't interested or does not have the resources to implement it, then the only way that feature can exist without a fork is with something like the extra field. Moreover, if for some reason periodic hard forks become no longer feasible, then without an extra field the Monero transaction structure will be frozen for eternity. Just as Monero is changing today, who knows how it will change in the future. An extra field permits changes that don't depend on hard forks.

## tevador | 2020-06-20T18:28:40+00:00
>  If there is a feature which only a subset of Monero users find valuable, it requires adding data to transactions, and the core team either isn't interested or does not have the resources to implement it, then the only way that feature can exist without a fork is with something like the extra field

If such feature is only used by a subset of transactions, it will affect the privacy of everyone using Monero. In theory, there could be dozens of these extensions in the future, which could be enough to tag users based on the specific set of extensions they use. Do we want this?

## UkoeHB | 2020-06-20T19:52:11+00:00
> If such feature is only used by a subset of transactions, it will affect the privacy of everyone using Monero. In theory, there could be dozens of these extensions in the future, which could be enough to tag users based on the specific set of extensions they use. Do we want this?

The biggest problem is if a feature clearly improves the Monero user experience in some way, but for a reason we don't know about today a hardfork isn't possible, then that feature can't be implemented without the extra field. It's painful from a privacy perspective, but I feel we shouldn't underestimate the danger of backing ourselves into a corner by mistake. Imo the extra field is an insurance policy that acknowledges our fallibility as protocol designers.

## fluffypony | 2020-06-20T20:09:45+00:00
You don’t need tx_extra for that, you can use the range proofs for data storage and all sorts. If we’re going to go down the road of ossifying our tx format then the current one is woefully unsuitable, with or without tx_extra.

## moneromooo-monero | 2020-06-20T22:03:50+00:00
That's not a good argument, since it's relying on extra removal not preventing the thing that was sought to be prevented in the first place.

## ghost | 2020-06-20T22:04:39+00:00
> you can use the range proofs for data storage and all sorts

Can you explain what you mean or give some reference?

## UkoeHB | 2020-06-20T22:55:01+00:00
>That's not a good argument, since it's relying on extra removal not preventing the thing that was sought to be prevented in the first place.

@moneromooo-monero can you clarify this statement?

## moneromooo-monero | 2020-06-20T23:06:35+00:00
"You don’t need tx_extra for [embedding extra data for future use]" implies removing extra will not prevent people putting custom data in a tx, which was the intent of the issue. The comment was used in support of extra removal though, so it relies on the intent of the issue being made moot. 

## Gingeropolous | 2020-06-22T12:10:37+00:00
I favor removing tx_extra for tx uniformity. A potential hybrid approach that would allow opt-in tx_data is a secondary chain/database that is linked to the main monero chain. 

Basically, you have the tx, and then you have a data packet that sticks onto the tx by referencing its tx_hash. Thus, if a node wants to participate in relaying these data packets, they can signal that they offer this service. Otherwise, the node just relays the tx without the data packet. The data packet isn't mined into the chain, instead it exists as a separate database linked to the chain. 

Well, this might be tangential. 

## SamsungGalaxyPlayer | 2020-06-22T16:46:57+00:00
While I really like removing tx_extra for uniformity, I strongly recommend that we take a cautious approach here. We should aggressively solicit feedback from services to make sure they have no intended use for tx_extra. Sadly I am aware of at least one service that plans to use tx_extra in some capacity as a stopgap for Travel Rule compliance until industry tools are available and adopted. To any outsider observer reading this, services should *really* prefer to use off-chain solutions. However, we may see creative (undesired) use of tx_extra to aid compliance before the industry gets its shit together.

## tevador | 2020-06-23T18:48:30+00:00
I suggest to at least make an announcement that Monero is planning to discontinue the tx_extra field in the near future to discourage new implementations. We can then discuss the details, e.g. if we allow it for coinbase transactions and if we phase out integrated addresses at the same time.

Keeping tx_extra for coinbase txs could alleviate some of the concerns regarding the ability to soft-fork. Future extensions could be placed there by miners similar to how SegWit works in Bitcoin.

## UkoeHB | 2020-06-23T19:02:11+00:00
> and if we phase out integrated addresses at the same time.

@knaccc expressed concern during discussion of #6456 that moving encrypted payment IDs out of the extra field would make them harder to deprecate.

## SamsungGalaxyPlayer | 2020-06-24T14:12:21+00:00
It's my recommendation that we announce a plan to phase out tx_extra by late 2021, and solicit feedback like we did for address types.

## Mitchellpkt | 2020-06-28T23:58:00+00:00
An arbitrary plaintext data payload in a system whose privacy relies on indistinguishably is like a screen door on a submarine. 😂 ❤️

## Mitchellpkt | 2020-08-08T22:05:14+00:00
Hahah, Neptune and I analyzed tx_extra use and found some interesting [on-chain data](https://github.com/noncesense-research-lab/monero_tx_extra/blob/master/ascii_data.md) 😆 

## High-level overview:
- 350+ dates 
- 80+ email addresses
- 10+ URLs
- 100+ variations on "X is the best X"
- 250+ messages

## Examples
### Dates
Multiple formats observed, including:
- Repeating YYYY-MM-DD: `2017-05-22DM2017-05-22DM2017-05-`
- "ID" + YYYYMMDD + tag: ` ID201904060422492k5oCZ1K71J8ZODB9d`
- YYYYMMDDhhmmss + tag: `20190406042249vxBGF5xa5jqbb3GT1Q`

These dates and PIDs are often repeated, probably for convenient transaction linkability.

### Email addresses
There are a large number of email addresses, including personal domains, and several widely-known cryptocurrency ecosystem contributors. 

### URLs 
There are a variety of URLs including:
- LinkedIn profiles
- A [short story](https://pastebin.com/mpJwkf7R)
- An article about a [ring size update](http://weuse.cash/2016/03/23/hard-fork/)

### X is the best X
There are boatloads of transactions with variations on "X is the best X", a few examples including:
- fluffypony is tge best pony ever
- fluffypony is tha best pony ever
- fluffypony is the best pony eveB
- fluffypony is the best pony ever
- fluffypony isbsýìûr5st pony ewww
- fluffypony&86(G(e best pony etRû
- xmrscott is the best Scott      
 
### Messages
There are hundreds of messages, ranging from jokes to vulgarity. MANY include PII such as names, handles, transaction amounts, credit card info, and contact information (not included below):
- `LEALANA 5 XMR RCT( û(bí)ì 1C!2S(`
- `<*> Joins [#xmrchain] ->Guest1`
- `  FUCK BINANCE FUCK CHAINALYSIS`
- `Mining Payout`
- `Here, have some kitt-katt - -`
- `1000000 Monero blocks - XMR4ever`
- `ThisthebestpaymntIDwehaveeverhad`
- `anycoin040820190441anycoin040820`
- `50X.COM Best Exchange         "ç`
- `For guns, drugs and prostitutes!`
- `RouziLovesPLGuitarAndLSMusic`
- `MONERO.RS 100 XMR Giveaway W#1`
- `This is a test transaction`
- `@@~:good luck in life:~@@`
- `DEADINSIDETID4`
- `¡¿¡They are watching you`
- `This tx was generated by Coinomi`
- `Fuck-your-donations,assholes!`
- `trololololipopspaymentidmymoscow`
- `Monero is AWSOME!!!`
- `FUCK THE SYSTEM`
- `ETCheckThisOutHereIsYourFirstXMR`
- `EPOL Group 2 #ICSSS2019 Victory!`
- `Here'sAnotherMoneroFundTransfer!`
- `Sic semper tyrannis!`
- `hallohallo eine neue monero tro`
- `Everyone should use Monero!!!!!!`
- `SleezyMacMoonster(1800-225-5324)`
- `hei dette er meg`
- `warm summer buffer zone`
- `minexmrcomdevfeeminexmrcomdevfee`
- `thanks for everything`
- `Test 0.1 XMR to Personal Account`
- `Yet another uneventful hardfork`
- `thanks a lot for sharing ideas!!`
- `13 tx.s: ASCII_EPOL.html.tar.bz2`
- `im the king of monero fuckyouall`
- `>>FUCK YOU BYTECOIN SCAM PIGS!<<`
- `THANK YOU!`
- `#Egö           !"#$%&'()0123456`
- `Thou shalt not track my Monero!!`
- `myfirstmonerodonationtopiratebay`
- `This is the end my friend again8`
- `forgot to send this a while ago!`
- `WE WANT TO USE MONERO TO UPGRADE`
- `Istanbul 1st monero meetup`
- `To the Moonero!`
- `I\'d like to eat some bananasyoy`
- `ADD-BITCOIN-AND-MONERO-PAYMENTS`
- `Electroneum Wallet----Payment ID`
- `Drugs@FBI-Catch-me-if-you-can`
- `LOL@Chainalysis@LOL`
- `     thisismypaymentidyoufucker!`
- `DONATION FOR AN AMAZING SERVICE!`
- `We are the champions, my friends`
- `XMR IS ANONYMOUS. TRACK MY COCK!`
- `Thanks for the helphavesome beer`
- `ICSSS-2019-EUROPOL-GROUP2-FTW!:)`
- `WhenIwasachildIspakeasachildIun`
- `Hallo Hallo das ist ein test fr`
- `it's been a pleasure trading w/u`
- `We need more DOGE smut for ads`
- `thanks for the graphs theyrecool`
- `monerogenesismining`




## sedited | 2020-08-08T22:43:24+00:00
This is great! I'm surprised there are not more malicious payloads, which I guess is what `<*> Joins [#xmrchain] ->Guest1` tried to achieve, targeted at whatever is indexing the transactions. 

## tevador | 2020-12-07T21:21:15+00:00
Any progress on this issue? Is there consensus to put this on the roadmap for a future protocol update?

## Gingeropolous | 2021-03-26T02:41:48+00:00
random ping on this to see if there's any further decisions / ideas

## Gingeropolous | 2021-04-28T19:04:18+00:00
@SamsungGalaxyPlayer , you had mentioned above:

> It's my recommendation that we announce a plan to phase out tx_extra by late 2021, and solicit feedback like we did for address types.

is it time to put these wheels in motion? I'm scratching my head remembering exactly how it all happens. Do we start with a mailing list update? Or just a "press release" and hope folks come across it in time? Or do we announce a dev meeting focused on the topic first?

I feel like this could / should get wrapped in with the next major release, which seems like its gonna be late 2021 anyways. 

ping @dEBRUYNE-1 as well. 

edited to add dev meeting idea

## Gingeropolous | 2021-05-04T14:15:51+00:00
from @SamsungGalaxyPlayer 



It's worth noting that Thorchain wishes to use tx_extra to pass along commands to the Thorchain nodes. Messages will be of the two formats:

Format 1: Adding XMR liquidity

ADD:XMR:<thorchain_address>

example: ADD:XMR:tthor1zpa4c6zpa4cyz9s93xuje2pwkswsqzn2zpa4c

Note: relies on https://gitlab.com/thorchain/thornode/-/issues/917, or else replace XMR with XMR.XMR

Format 2: Swapping XMR for another asset

SWAP:CHAIN.ASSET:DESTINATION:LIMIT:AFFILIATE:FEE

example: SWAP:THOR.RUNE:tthor1zpa4c6zpa4cyz9s93xuje2pwkswsqzn2zpa4c:3141441780:tthor1ql2tcqyrqsgnql2tcqyj2n8kfdmt9lh0yzql2tcqy:10


## kayabaNerve | 2022-07-21T00:13:24+00:00
1)  TX extra, under Seraphis, will become solely for arbitrary data already. This would be the perfect time to remove it.
2) Removing it may be one of the worst ideas out there.

While I agree removing all wallet data is a great idea, as Seraphis does, that does not change the fact there are L2-esque platforms relying on it for short memos. My simple statement on the matter is as follows:

If I can not place arbitrary data in TX extra, I'll place it elsewhere.

We can remove TX extra and celebrate it. Great. Except now, when I need 128 bytes, I'm adding 2 fake outputs worth 0 to get 1 TX key, 1 R, and 1 commitment. It's trivial to find a valid point with the first two bytes and get 30 bytes per point, of which I have 2 * 3. I now have a less efficient scheme using more bytes than needed (both due to imperfect packing and the multiples used) while also adding processing requirements to all parties just for the same base penalty.

My proposal, as TX extra becomes for arbitrary data only, would be to cap it at 256 bytes. While ideally we'd only allow 128 bytes, which will fit into a 1-byte VarInt, JAMTIS certified addresses are 168 bytes raw. While we can not use a VarInt to denote its length, yet rather a single byte, I feel that's another discussion.

This means we'd have 88 bytes after a full JAMTIS certified address. Without certification, we have 48 bytes after two JAMTIS addresses, enough for a key and a couple of words. I believe 256 should accordingly be plenty.

We should also discuss an increased economic fee, perhaps 2x per byte, for such TXs, yet we have to be careful we don't encourage steganography (unless we want to for privacy reasons? Where's that one issue to give every TX 16 outputs?).

I talked with a few people at MoneroKon about this, and we (our small group talking at a dinner) did seem to agree that TX extra should stay within reason, such as the above proposal.

## Gingeropolous | 2022-07-25T20:20:16+00:00
> the fact there are L2-esque platforms relying on it for short memos. My simple statement on the matter is as follows:

can these be ephemeral? I.e., can the payload (the stuff in tx-extra) be pruned almost immediately for nodes that don't care? So it ends up just being memos in the txpool or memos for those that care?

## kayabaNerve | 2022-07-26T09:42:58+00:00
No. They have to be signed, tied to a transaction, and practical flow operates on the 10th block, not the mempool. While signed memos could be separate, increasing bandwidth and processing power while decreasing storage, we're then building a distinct messaging layer. While that messaging layer, which is more resource intensive and has an ordering problem (as it's no longer part of the transaction) could be built by L2 services, there's design problems (from chicken-egg to a requirement on permanence for verifiability) which is why they don't simply do it in the first place and instead rely on the base-layer.

If asked if it'd be easier to use steganography or build such a system, I'd say steganography. I believe that should be sufficient to comment on the practical choice developers will make in such cases. While I don't mean to be an antagonistic asshole, and wouldn't flood any chain solely to lower my own requirements, I actually did comment on the ability to achieve needed functionality via steganography on another network over a single transaction. This wasn't an 'option', yet a proper comment on the way to do it, if done. The discussion here, +3 Monero outputs, would absolutely be far easier for me to solve this and I don't consider it sufficiently negative to Monero to consider not using 5-output* transactions. I believe such TXs would have an almost identical privacy impact though.

*Change, output, +3 data. In my specific case, a Monero -> Monero swap, if they existed, would need 3 outputs for data, hence that number. For Monero -> BTC (20-byte address)/ETH, it'd only need 1. 3 output TXs may exist much more frequently and have less of an impact on privacy? And then for Monero -> BTC (32-byte address), it'd be 2 (4 outputs). This ignores the fact this network is already doxxing Monero in, just as any exchange does, which is why we are trying to minimize TXs on XMR itself.

## tevador | 2022-07-26T18:01:00+00:00
> My proposal, as TX extra becomes for arbitrary data only, would be to cap it at 256 bytes.

Except this doesn't fix the main issue, which is splitting the anonymity pool. Apart from removal, the second best option would be to mandate a tx_extra field of a fixed size in all transactions.

> Except now, when I need 128 bytes, I'm adding 2 fake outputs worth 0 to get 1 TX key, 1 R, and 1 commitment. It's trivial to find a valid point with the first two bytes and get 30 bytes per point, of which I have 2 * 3. I now have a less efficient scheme using more bytes than needed (both due to imperfect packing and the multiples used) while also adding processing requirements to all parties just for the same base penalty.

You are correct. It is possible to put arbitrary (even plaintext) data in various other parts of the transaction and still have a transction that passes the consensus rules. With Seraphis/Jamtis, that would be about 87 bytes of data per output (<code>K<sub>e</sub>, v, t<sup>\~</sup>, K<sub>o</sub>, a<sup>\~</sup></code> can contain arbitrary data. You cannot put arbitrary data in the commitment `C`, because you won't be able to make a valid rangeproof.).

If we wanted to make it harder to include plaintext data in a transaction, there could be a non-consensus rule (enforced by nodes when relaying a tx) that the supplementary tx data must pass some quick statistical test of randomness.

## UkoeHB | 2022-07-26T18:04:51+00:00
> With Seraphis/Jamtis, that would be about 87 bytes of data per output (Ke, v, t~, Ko, a~ can contain arbitrary data.

I recently added a rule that all `K_e` and `K_o` must successfully deserialize as EC points. `K_o` deserializing is required for the squashed enote model, and `K_e` deserializing reduces exception safety uncertainties in scanning (and reduces fingerprintability).

## tevador | 2022-07-26T18:25:18+00:00
As noted by @kayabaNerve, you can take 30 arbitrary bytes and bruteforce the remaining 16 bits until you get a valid EC point (the chance of failure is only 2<sup>-16</sup>).

For example:
Hex: `5468697320697320612076616c6964206564323535313920706f696e742e2e2e`
ASCII: `This is a valid ed25519 point...`

## kayabaNerve | 2022-07-26T18:40:14+00:00
Thanks for the corrections, @tevador. I also only assumed 30-bytes per using my above 3-output example, yet earlier assumed 96 (which you noted was wrong. I was thinking because of the mask... but that requires solving the DL problem).

... do we just want to encourage steganography? It'd take +2 outputs for a Monero swap (origin address for failure, destination address, that leaves 44 bytes when my metadata is ~13). It may increase the amount of 3-4 output TXs, yet I'm not sure that's directly negative. It's that, or a fixed 256 byte payload AFAICT. These message should still be a fraction of items though.

Relation to https://github.com/monero-project/research-lab/issues/96 and its cited comment. If this is ever implemented, then it'd cover the "everyone does it" case already, while solving other considerations.

## UkoeHB | 2022-07-26T18:54:04+00:00
I am not a big fan of restricting the tx extra beyond stricter semantics (sorted TLV) because it's a field that's literally 'for anything we can't know in advance or are unable to pass judgement on'. At the very least, if a byte restriction is imposed, it should be a per-output limit since memos are generally aimed at a single recipient.

## kayabaNerve | 2022-07-26T20:20:47+00:00
Any thoughts on removing it for steganography or a mandatory inclusion?

## UkoeHB | 2022-07-26T20:45:17+00:00
Steganography does not excite me (typically you want tx output + memo - stenography means adding additional outputs which is just a DDOS on scanning), mandatory inclusion implies adding way too many bytes.

## tevador | 2022-07-26T21:21:38+00:00
> Any thoughts on removing it for stenography or a mandatory inclusion?

I don't understand the urge to use precious blockchain space as a communication channel. With just 32 bytes, you can commit to arbitrary data and share that off-chain.

If you want to know my personal opinion, I'm for going all in on privacy. That means removing the tx_extra field and mandating all transactions to have 2 inputs and 2 outputs.

## kayabaNerve | 2022-07-27T06:21:26+00:00
You actually can't, easily, commit to arbitrary data shared off chain.To discuss my specific use case:
- We can't have people post it on the L2 as it would cost additional fees. They can't pay fees if they can't enter the ecosystem because they can't post messages because they can't pay fees. It's a chicken/egg.
- It can't be ephemeral and therefore unverifiable in the future.
- There's a variety of DoS concerns with accepting arbitrary data which is promised to be committed to in a TX, before that TX exists in a confirmed state. I did consider an IPFS node, which could run only accepting allowed hashes, but the issue is it has to wait 20 minutes for the IPFS hash on Monero, which isn't a feasible UX.

That's why underlying networks are preferred, not to mention the simplicity of doing so. It's the one model which doesn't open additional attack vectors and problems.

The computation cost of steganography are why I advocated for a 256-byte TX extra, justifying that specific size. While steganography would be a valid replacement, largely preserving privacy, it has that trade off.

... you can also just encode data bytes in CLSAGs? It gives you 15 * 252 bits? 0-additional bandwidth, just reduces ring size and still enables creating a separate privacy pool. By just using the newly added 5 decoys though, you can safely get ~150 bytes, which is sufficient. I'd rather do that than work on a new IPFS setup which is likely to be DoSed while notably increasing resource requirements.

And yes, this is a discussion I believe currently regarding Seraphis/other future protocols. For now, TX extra is still here and this hasn't evolved into antagonistic cat and mouse. I'm trying to highlight the point of view which depends on TX extra, and explain the thought process and reasoning which will occur. While I completely understand Monero potentially not wanting to cater to this use case, that will force developers to find solutions which do work. We have to ask if an optimal TX extra use-case is more damaging than the sub-optimal TX-extra-equivalent use case. Since the next optimal solution is steganography, either in the inputs or outputs, we have to consider if we prefer steganography or if we prefer offering TX extra.

## tevador | 2022-07-27T08:07:27+00:00
> It can't be ephemeral and therefore unverifiable in the future.

Why would an atomic swap need to be verifiable forever? Once the swap is completed, the metadata become irrelevant. To future blockchain verifiers, it should look like any other transfer.

I still don't understand why the atomic swap parties would have to communicate using the blockchain. There needs to be at least one round of off-chain communication prior to the swap (to agree on the amount and the price). From a security standpoint, there is no difference between an encrypted on-chain memo field and an off-chain message (e.g. an e-mail attachment). Both are completely irrelevant to 3rd parties.

For example, the following Bitcoin-Monero atomic swaps protocol doesn't need any on-chain memos: https://eprint.iacr.org/2020/1126

## kayabaNerve | 2022-07-27T08:32:06+00:00
Swaps wasn't referring to atomic swaps, yet multisig-based DEXs which have a large threshold multisig (so also not like Bisq). Funds are sent to the multisig, trusting it to execute, with the memo saying what to do. I am working on one and there is another who has announced their intention to list Monero, with an (incomplete) integration candidate. We both have similar requirements here.

Atomic swaps should solely use ephemeral messaging though, yes.

## tevador | 2022-07-27T08:47:13+00:00
The DEX can have its own P2P network for passing the memos. You could submit a transaction with a 32-byte hash of the memo on the Monero network and then submit the TXID and the memo on the DEX P2P network. The DEX would look up the TX and check that the hash there matches the internal memo.

It would take more development effort, but it's a much better solution from a privacy and scalability perspective.

## kayabaNerve | 2022-07-27T09:05:30+00:00
> You actually can't, easily, commit to arbitrary data shared off chain.To discuss my specific use case:
> - We can't have people post it on the L2 as it would cost additional fees. They can't pay fees if they can't enter the ecosystem because they can't post messages because they can't pay fees. It's a chicken/egg.
> - It can't be ephemeral and therefore unverifiable in the future.
> - There's a variety of DoS concerns with accepting arbitrary data which is promised to be committed to in a TX, before that TX exists in a confirmed state. I did consider an IPFS node, which could run only accepting allowed hashes, but the issue is it has to wait 20 minutes for the IPFS hash on Monero, which isn't a feasible UX.

While yes, parties could work out an additional solution, it overall increases complexity dramatically and isn't desirable. Even the best solutions still increase the attack surface while decreasing UX. While it would be better, regarding Monero's privacy, it's only a theoretical advantage since any competent party will already know all these transactions and be able to create the differing pools accordingly. While yes, they must know of the network and sync it, any competent party will. So while yes, there's a theoretical advantage to Monero privacy here, there's not a practical advantage.

There is potentially a practical transformation dependent on other schemes which don't require publicly acknowledging data long term. The distinction is anything which doesn't need the data long term, such as swaps, already isn't discussing using TX extra.

## tevador | 2022-07-27T09:25:29+00:00
Forcing the whole Monero network to sync and store your DEX data forever is clearly not the best solution.

## kayabaNerve | 2022-07-27T10:00:37+00:00
... from my perspective, I'd disagree. While yes, it is an additional burden on Monero, we're discussing ~100 bytes on relevant TXs. While I'll agree there are better solutions for Monero, none of them offer the necessary security, guarantees , and user experience desired for connecting projects of this type.

I'd also cite how Monero has payment IDs in its code, when we could've had off-chain solutions for that. While yes, this is longer than even original payment IDs, it does make the comment Monero needs to consider UX. This is one of those discussions.

I'd personally be fine with either <= 256-byte optional OR steganography, yet steganography doesn't practically help with privacy since that points likely won't be uniform and that likely will be enough to flag steganographed TXs. These discussions are all about theoretical improvements which we're unfortunately not mapping to actual practical benefit at this time (though I'm sure we can create a contrived scheme which may).

Also, to clarify, it does sounds like you'd endorse a 32-byte TX extra? I assume that'd be mandatory and random bytes (hashed) upon non-inclusion?

## kayabaNerve | 2022-07-27T10:37:41+00:00
*steganographied data can be encrypted so they do have uniform bytes and do appear indistinguishable. The sole disadvantage is the less efficient encoding combined with the processing costs. Considering we're likely only discussing +1/2 outputs on relevant TXs (which are planned to be infrequent), this is my currently preferred solution. Considering we're not discussing moving to 2/2 only anytime soon (AFAIK), which would seem to be very difficult to manage with the 10-block lock, I'm happy to leave it at that for now as what will likely happen if TX extra is removed (which I do understand the theoretical privacy benefits of doing so).

## tevador | 2022-07-27T11:48:18+00:00
Actually, the extra blockchain data would probably be a minor issue compared to the fact that the DEX most likely has to publish its private view key, which would allow anyone to determine when an output owned by the DEX is spent. This reduces the effective ring size for everyone using the DEX outputs as decoys.

## kayabaNerve | 2022-07-27T12:21:07+00:00
Correct. That was what I was trying to highlight with the distinction of theoretical and practical. I still believe there are value in theoretical improvements though. I could say, because DEX inputs are known, and TXs out are known, there's no value in using randomness for TXs out. TXs out appear identical to any other TX though, which I worked hard on, and there is a chance even with knowing TXs out, they won't be perfectly linkable (beyond statistical analysis thanks to the known inputs, which could be solvable with a circuit membership proof). This is because ephemeral data as part of the signing process is used.

Even if the DEX wanted to keep view keys private, there'd still be 100 distinct individuals (the multisig holders) who could dox it though :/ It's why we're not solely acting as an instant exchanger yet also enabling long-term balances, in order to reduce the amount we 'poison' the Monero TX pool. While that has an issue as it's custodial, and not just for a moment, it's been accepted by the markets and larger crypto community. While yes, I'll immediately agree it's technically inferior... that's not what we're discussing.

I will note this makes it identical to a CEX with regards to governments. With regards to firms, it enables more firms (even ones without the relevant partners) to dig in. There's also no level of oversight with data usage. There's a variety of discussions on the impact of this available.

As one final note, though it is off topic, I'm not building a DEX like this to harm Monero, despite the discussions here being about the harm to Monero and me taking the side of the harmer. I decided to build a DEX like this because that other integration was moved into testing. This is the future we're faced with. The other integration however, in my opinion, has several damaging aspects to the community. I could let them move forward, obtaining whatever market share they will, or compete for the same market share while doing less harm. I'm here in these discussions to comment on this same reality. I also believe there is a legitimate service here, which I hope to advocate for.

I believe steganographied data is the best path, and if the computational cost isn't preferred, optional extra < 256 bytes. It maintains the offering to legitimate services, which Monero may not want to encourage, which I'd understand. The former however can't practically be stopped, as it'll appear random if encrypted, with the sole note being it has 3-4 outputs instead of 2. While yes, that was another discussion raised, I don't see it as possible for as long as we have the 10-block lock. I also don't see how that's removeable. Even with a circuit, we need a sufficiently cemented reference point... (though they would be much faster to check the consistency of if we use a 32-byte long form instead of a VarInt short form).

I'll also note without the 10-block lock, you can solely have a carry output and then use the intended change out for steganography. Now we have to ask if developers will use a chain of 3 transactions or tackle infrastructure problems making more things their problem *while simultaneously opening up the attack surface*. While it'd make me review and prefer an IPFS-esque structure, I'd understand if other developers just chained 3 TXs. 

TL;DR Everything sucks. How can we make things suck the least given our reality so maybe things don't suck?

Alternative TL;DR: 

  With a sufficient number of users of an API, it does not matter what you promise in the contract:
  all observable behaviors of your system will be depended on by somebody.
  -- Hyrum's Law

## SamsungGalaxyPlayer | 2022-07-27T14:01:45+00:00
I think from a matter of being pragmatic, it's a weird balance, and it's easy to be on one of two extremes:

1. Monero is pure, keep your crap off it
2. Monero should be usable for anything so long as people pay for the space

We saw a similar discussion in the past with the Bitcoin developers considering certain types of transactions as spam, including Counterparty transactions. Are these transactions reasonable or spam depends heavily on one's opinion.

While I think a level-headed approach is necessary, the general attitude of "keep your spam off" is a dead-end. Spam is mitigated with fees. If fees aren't enough, that's the main problem. Hike the fees.

The main attitude I care about is mitigating privacy issues.

The Monero community should take efforts to standardize common forms to mitigate privacy leaks on it.

Some hard truths:

1. We can't prevent sharing of view keys
2. We can't prevent people from trying to pad information in somehow

In my view, having a standardized way of storing information in a sensible way is ideal at mitigating the damage from 2. If there's no standard way to store info, you'll have 1 person doing A, 1 person doing B, etc. and they'll all suck. Then, after we place most activity into this standard format, then we can more easily improve network privacy.

Efficiency is another consideration. If only 1 transaction wants to store data a certain way, then it's clearly not worth padding every other transaction to account for this. It's about picking reasonable standards, and eating an efficiency cost if the privacy benefit is worth the cost.

We can keep playing a game of whack-a-mole to try to discourage development and storing of arbitrary data in specific ways, but it ultimately won't lead anywhere.

## spirobel | 2022-08-07T12:12:55+00:00
1. We should try to avoid making it look random when it is not. It is good if transactions of Defi protocols are non uniform and easy to identify, because it is known to the public what these transactions are anyway. If they are easy to identify the decoy selection process could take into account that there is a public dataset out there that marks these transaction hashes as part of a certain defi protocol.
2. If we want to improve the privacy of tx_extra and its usability for new use cases we should make the length random instead of fixed. (for example letting a browser wallet save the url of the website where the transaction was made instead of the (dummy) payment id that is currently the default. I want to implement this because I want users to recover their wallet from just the seedphrase without losing information) 
How would this work in practice:
currently tx_extra is always padded with a dummy payment id so all transactions look like they are made to integrated addresses. (so the transactions are as uniform as possible). So the norm is this fixed length. But the norm should be a random length. (possibly  probabilistic based on the current circumstances in the network; similar considerations to decoy selection) 

## hyc | 2023-02-04T02:47:28+00:00
Given the recent attention to the topic, some additional thoughts:

1) we could keep tx_extra, and continue to mandate the use of tag-length-value for each element stored there.
2) we can also mandate that anything over a threshold (e.g. 32 bytes) must be encrypted. This will prevent liability issues if people decide to attach large blobs of controversial data. We'd need something like an Authenticated Encryption cipher that allows a check to see if data was encrypted correctly.

The only downside here is a potential DoS vector if it costs a lot to verify encryption of the data.

## kayabaNerve | 2023-02-04T07:08:46+00:00
Two comments.

1) I am against TLV. If we have TX extra, it should only be for arbitrary data. It only makes sense to enforce an encoding if we then place wallet protocol items back in there. If that's a legitimate consideration, I'd rather:
A) Have a second TX extra for wallet protocol usage
B) Just hard fork in explicit fields as needed

2) If there is an encryption primitive, that allows verifying it's well formed without knowing the decryption key, I'm all for it. AFAIK, we cannot determine if data is encrypted except for testing how uniform it is. If the authentication was layered, then while we could verify its authenticity, we'd run into the same problem of not knowing if it's actually encrypted.

As for a uniformity test, I am generally against statistical tests on transactions, as they lead to potentially random failures. For any uniformity test, with a set encryption algorithm and set key, there will be messages which naturally are unsendable. While they may be few and far between, or even 2^64 unlikely, I despise systems which can randomly fail. I do acknowledge prefixing a 8-byte nonce practically solves this for any deployed system.

If we want to move forward on this discussion, I'd first ask which branch we're pursuing.
A) Fully uniform TXs, removing arbitrary data for steganography (technically non-uniform by output quantity), increasing global scan time and chain state size
B) An explicit arbitrary data field

If A, we no longer need a further discussion of anything IMO. If B, my advocacy is for Monero to do absolutely nothing with it. It shouldn't check it, no wallets should put data there, nada. The only bounds should be on max size and weight calculation. I'd *tolerate* a uniformity requirement, not that my tolerance decides what's done, due to liability concerns yet I'd note we shouldn't require `> 32` bytes. Stream ciphers can be applied to an arbitrary amount of bytes trivially, and if you're concerned about liability, a URL can be just a few bytes (4?).

I also believe requiring the data to be encrypted would increase privacy. I personally just rather yell at people to encrypt their data before placing it on chain than make a consensus rule out of it.

## tevador | 2023-02-04T11:16:47+00:00
> We'd need something like an Authenticated Encryption cipher that allows a check to see if data was encrypted correctly.

Authenticated encryption doesn't allow you to check that the data was encrypted correctly unless you know the secret key. Proving that something is encrypted without revealing the secret key is hard and expensive as it requires proving statements over general ZKP circuits.

It would be much simpler and cheaper to do a quick statistical test when relaying a transaction (it would be a non-consensus rule).

> As for a uniformity test, I am generally against statistical tests on transactions, as they lead to potentially random failures. For any uniformity test, with a set encryption algorithm and set key, there will be messages which naturally are unsendable. While they may be few and far between, or even 2^64 unlikely, I despise systems which can randomly fail. I do acknowledge prefixing a 8-byte nonce practically solves this for any deployed system.

For any randomized encryption (and you *need* randomized encryption to achieve IND-CPA), you can make the chance of failure arbitrarily low by rerandomizing until the test is passed. Moreover, the statistical check would be done when relaying a transaction, so it would not affect blockchain consensus.

## kayabaNerve | 2023-02-04T11:22:10+00:00
If it's under TX sanity, I have no objections at all. If it's under relay, I still have my concerns.

Regardless, it's trivial to just append a trailer to the encrypted data to achieve uniformity on any uniform message not detected as uniform (which should already be incredibly unlikely). I will caveat that just as an near-uniform message can have a trailer to achieve statistical uniformity, so can a non-uniform message. It may be proper to:

1) Check for near-uniformity under sanity
2) Ban ASCII messages entirely

I caveat 2 in case there remains some ASCII strings which would pass uniformity (I assume we'd do it on a bit level, and ASCII just has the first bit never set. That only makes it non-uniform by 12.5%). If the concern is perception against malicious messages, saying we banned plaintext, both with a statistical distribution check preventing long alphanumeric strings AND by literally banning ASCII would likely be solid.

I do acknowledge actually achieving that statement we don't allow public messages require this be under relay. While I have my irks, I can ack the benefit.

## spirobel | 2023-02-04T15:22:42+00:00
>It would be much simpler and cheaper to do a quick statistical test when relaying a transaction (it would be a non-consensus rule).

All of these attempts will forever be snakeoil. The only clean solution to this is to get rid of the transaction uniformity issue entirely (by building a better protocol where transaction uniformity has no effect on privacy).

The tx_extra debate is a strawman. The fundamental trade off is between transaction fees and "blockspace filled with stuff somebody considers spam". A simple solution like getting rid of tx_extra wont get rid of this trade off. You cant have cheap transactions and a jpeg free blockchain at the same time.

## tevador | 2023-02-04T16:46:45+00:00
> a better protocol where transaction uniformity has no effect on privacy

A blockchain with non-uniform transactions will always contain some extractable information. That's a basic information-theory fact that cannot be fixed by any protocol.

> transaction fees

Transaction fees exist to limit the *volume* of on-chain spam. They don't do anything against harmful content.

tx_extra is an arbitrary-size field that's completely ignored by consensus, so it's a very efficient way to stuff data onto the blockchain. For example, you can pay fees for 100 KB of blockchain space and get about 98 KB space for arbitrary data (~2 KB is the consensus "overhead", such as signatures and range proofs).

If there was no tx_extra, you could stuff let's say 30 bytes of data into the output key. 100 KB of blockchain space will get you 50 2-in/2-out transactions for a total of ~3 KB of arbitrary data. "Uploading" to the blockchain has just become 30x more expensive without affecting the fees for ordinary transfers.

## hyc | 2023-02-05T03:52:52+00:00
> I am against TLV. If we have TX extra, it should only be for arbitrary data.

If you don't use tags, then two different apps that both use arbitrary data will be mixing up their usage, with no way to distinguish them. That would be an incredibly shortsighted design.

> It would be much simpler and cheaper to do a quick statistical test when relaying a transaction

That would be fine. You could improve the test by doing one pass of encryption (with an arbitrary key) and comparing the statistical result of the input and encrypted output. If the input is already encrypted then it should be nearly equally distributed in both cases.

## kayabaNerve | 2023-02-05T07:58:36+00:00
@hyc Considering I don't care for Monero to become an application layer, I don't care for multiple apps to co-exist in TX extra, which is the only way that'd be an issue.

I'd also note that apps are welcome to define whatever formats they want, including ones with magic bytes, and if one app wants to work off another, it can build a complimentary format. All of that is in the realm of the apps, not in the realm of Monero. Monero enforcing TLV, in almost every case, will just add 2 bytes to the arbitrary data, increasing its size by >2% (assuming most messages are <=100 bytes. For my desired messages, it's actually 4-6%).

With regards to detecting uniformity, I don't see value in doing another pass and checking uniformity against that. Encryption should be uniform. Why should we generate a theoretically uniform value (which isn't exactly cheap, at best it's an extra hash round) to check against when we can just check uniformity in general?

With regards to checking uniformity, I'd suggesting checking the distribution of nibbles. They only have 16 possibilities and even just 8 bytes will provide that many instances. With regards to checking that distribution, this isn't my field of expertise. I'll ack that another encryption pass *would* demonstrate practical distribution for the given length, yet hope we can find a cheaper check.

## spirobel | 2023-02-05T12:04:44+00:00
@tevador 
>A blockchain with non-uniform transactions will always contain some extractable information. That's a basic information-theory fact that cannot be fixed by any protocol.

that is an irrelevant technicality. The  issue is that Monero depends on statistics for its privacy guarantees. That is a major weakness and the reason why this debate exists in this form.

The only solution to the transaction uniformity problem is to use a protocol where spent notes are completely disconnected from transactions.


>tx_extra is an arbitrary-size field that's completely ignored by consensus, 

it is more complex than that. 

>If there was no tx_extra, you could stuff let's say 30 bytes of data into the output key. 100 KB of blockchain space will get you 50 2-in/2-out transactions for a total of ~3 KB of arbitrary data.

what about multi destination transactions for example? what about transactions with more outputs?

@hyc 
>That would be fine. You could improve the test by doing one pass of encryption (with an arbitrary key) and comparing the statistical result of the input and encrypted output. If the input is already encrypted then it should be nearly equally distributed in both cases.

You could also just calculate the entropy of the string.
Easier to implement and does the same thing.


It is generally not a smart idea to prove that something is random. (because it is not possible)
But this is what what we are talking about here. 

It would be much better to stop these futile attempts and focus on solving the root cause.
Why is transaction uniformity even an issue? Because there is a relationship between utxos and transactions.


## dan-da | 2023-02-05T13:07:28+00:00
> Why is transaction uniformity even an issue? Because there is a relationship between utxos and transactions.

@spirobel Are you suggesting to somehow separate and unlink utxos from tx?   How would that work?

From what little I've gathered from the sidelines, people advocating for uniformity have suggested allowing only 2 in 2 out tx and eliminating tx_extra.  Perhaps get rid of multisig also, I'm not sure.  I'm unsure of all the implications and tradeoffs here, but I do find it interesting to think about ways to make every tx look exactly like every other, so we get a single anon pool...

Are you hinting at another way to go about this?

## tevador | 2023-02-05T13:56:27+00:00
> The only solution to the transaction uniformity problem is to use a protocol where spent notes are completely disconnected from transactions.

What you are proposing is already listed in [Open Research Questions](https://github.com/monero-project/research-lab/issues/94) as one of the highest priority topics. The closest concrete proposal is https://github.com/monero-project/research-lab/issues/100 which does not even have a PoC that would have a chance of working with Monero. It will take many years before something like that can be deployed.

Reducing tx non-uniformity caused by tx_extra has a positive impact on privacy and can be implemented *now*.

> that is an irrelevant technicality

It is very relevant. Even if we have a protocol that offers a global anonymity set, tx non-uniformity will cause anonymity puddles to form, significantly reducing the actual privacy properties of the protocol.

For example, refer to this [zcash issue](https://github.com/zcash/zcash/issues/4332), which shows how tx non-uniformity can leak information even with a global anonymity set.

> it is more complex than that

Can you elaborate?

> what about multi destination transactions for example? what about transactions with more outputs?

Ideally, we would only have 2-in/2-out transactions for maximum uniformity. Using multiple outputs per transaction would somewhat improve the efficiency of steganography, but it's still much less efficient than overtly putting the data in tx_extra.


## kayabaNerve | 2023-02-05T15:00:17+00:00
1) Not to sidetrack, yet a SNARKs PoC would take weeks and an actual impl months. Not many years. There's just a lot of discussions on its benefit/desirability/practicality. It's more bureaucratic bs/developer availability than actual technical issues IMO.

2) 2-out, for as long as we have a 20-minute lock, sounds horrifically infeasible. I do understand that grows exponentially. It's just still hell for every single integration.

3) If there's no TX extra, and only 2-out TXs, I'm cutting every corner I can.

There's two considerations here.
1) I don't want to be an asshole. Obviously, we're all here for Monero to do our best to produce the best protocol we can. While we may disagree on what that is/how, we're here to work together.
2) I'm supposed to be an asshole. If we're discussing removing TX extra, then I, as the theoretical developer needing TX extra (and also a practical example) am required to discuss how I will surpass limitations placed so we can discuss how effective they are.

With that out of the way, here's all the corners I know of which can be cut.

1) The TX ephemeral key. If you're fine with a fully public wallet, which deterministically derives the `r` off public data, it can offer ~30 bytes by using the public key.
2) JAMTIS enc tag (18 bytes).
3) JAMTIS hint (2 bytes).
4) View tag (1 byte).

So far, we're at ~51 bytes.

5) Balance proof (32-bytes). This has the side effect of doxxing the balance of the change output. This can only be prevented by not exposing this scalar and returning to a zero sum check (not to suggest that's possible).
6) Selected group members. This could potentially offer ~100 bytes, albeit by potentially eliminating most decoys in the transaction. This can only be prevented by deterministic group selection.
7) Possibly some nonce abuse for <=32 bytes each? But breaking the privacy of the proofs underneath them.

So ~51 bytes safely (if calling published view keys safe), though with a good amount of pain, and then ~200 bytes if you disregard safety.

I'm actually fine with just 51 bytes. It's manageable for my needs. While Monero isn't about me, I argue in this discussion based on real world implications of TX extra, and my needs are real world considerations. The concern is people who want more than 51 bytes. They will then be forced to endanger their users. While that's... arguably fine? They're 'consenting' to it? It raises the discussion on user knowledge of privacy protocols and if it's informed consent, and if forcing these protocols to such drastic measures is best for Monero and its users.

As one final note on 2-2 TXs, if the 20 minute lock is maintained, handling a 1 TPS in/out flow, aggregating, then with the full balance funding outputs (to enable handling one really large output with further logic), would take 7 hours. This is definitely a side track, yet I hope to point out how much of a complexity it is in hopes to largely drop it from this discussion, enabling re-focusing it.

AFAICT:
A) Remove TX extra. +uniformity +pain for arb data
B) Keep TX extra, likely requiring some statistical uniformity/non-ASCII. There's also advocacy for forcing TLV which I cannot say I believe should be in-scope to Monero who I believe should leave this field as *arbitrary*.

I do truly believe consensus should be reached on one of these two options before we lose ourselves in nits in every single direction *if we want to accomplish practical change by Seraphis*. In that spirit, cutting through the debate here, we have TX extra now, koe implemented it into their Seraphis work (along with a TLV encoder/decoder, which I'm unsure the exact relation to consensus/relay on). If this discussion doesn't have a resolution by then, we'll at least maintain the status quo, and just be at risk for spam/have uniformity concerns.

If this is to remain a discussion for the next two years, as it has the past two, then I'm fine dropping my pressure on having a directed discussion. The truth *is* Monero is an evolving protocol. We don't need to make decisions now, and we can give ourselves the time to evaluate all options to be fully informed. I'm solely concerned that we'll lose our opportunity to make this change with Seraphis, getting implicitly locked into whatever's written there while this discussion continues ad infinitum.

## kayabaNerve | 2023-02-05T15:04:07+00:00
*There's a few more things you can do for a few more bytes. Steg'ing a 2-2 would prob still get you up to 60+ bytes without compromising privacy.

## tevador | 2023-02-05T15:06:53+00:00
> Not to sidetrack, yet a SNARKs PoC would take weeks and an actual impl months. Not many years.

I was talking about mainnet deployment. Seraphis has been in development since 2020 and will probably hit mainnet in 2024 or 2025. I would be very surprised if SNARKs can be done much faster than that, including all audits etc.

## tevador | 2023-02-05T15:35:04+00:00
> As one final note on 2-2 TXs, if the 20 minute lock is maintained, handling a 1 TPS in/out flow, aggregating, then with the full balance funding outputs (to enable handling one really large output with further logic), would take 7 hours. This is definitely a side track, yet I hope to point out how much of a complexity it is in hopes to largely drop it from this discussion, enabling re-focusing it.

Limiting transactions to 2/2 was just an example how to achieve perfect tx uniformity. I don't *actually* think it's a good idea to implement it in practice, at least not for now.

This discussion is about tx_extra. Even if we don't remove it entirely, any restrictions placed on tx_extra would be an improvement since it's completely unmitigated at the moment.

At the very least, we should:

1. Remove all mandatory transaction data (such as public keys) from tx_extra. This is already being implemented with Seraphis.
1. Place a reasonable upper limit on the size of tx_extra -OR- make tx_extra prunable.

I'm also in favor of putting additional uniformity requirements on tx_extra, but it seems that there is no consensus about that.

## kayabaNerve | 2023-02-06T08:17:43+00:00
- 255-byte limit, giving it a one byte length prefix (micro-optimizing the VarInt, sure, but it adds up)
- Statistical uniformity check
- ASCII ban
- Don't force apps to use TLV when we already aren't an app chain and it only helps when multiple apps use the same TX. If someone wants to build a service with that behavior, they can use TLV themselves.

That is my current advocacy.

## dan-da | 2023-02-06T09:54:14+00:00
ascii ban would prevent eg base 32, 58, 64 encoding, no?  (which could pass uniformity check if input is encrypted).   Is that desired?

## kayabaNerve | 2023-02-06T10:24:11+00:00
It's an ack of hyc's thoughts. While I don't personally have a concern Monero will be criticized for having garbage, I can agree it's undesirable. Banning the entire TX extra from being a valid string would force users to encrypt it in some way or turn it into some data object. Accordingly, we could no longer be accused of having messages nor enabling messages. Solely payloads.

Then, the statistical uniformity check turns payloads into encrypted payloads, fully absolving us of concerns.

The ASCII string check is cheap, and for some short ASCII strings, they'll likely pass uniformity (again, a URL can be just 4 bytes), hence the benefit in their explicit ban.

## jeffro256 | 2023-02-07T15:02:21+00:00
> If we want to move forward on this discussion, I'd first ask which branch we're pursuing.
> A) Fully uniform TXs, removing arbitrary data for steganography (technically non-uniform by output quantity), increasing global  scan time and chain state size
> B) An explicit arbitrary data field

I'll propose something slightly different which I think will make an good compromise between usability for DEXes and other use cases, and keeping malicious content off-chain. Non-malicious use cases of arbitrary data in transactions fall into three main categories: 1) "Receipt stuff" for bookkeeping between counterparties (Descriptions, real world IDs, refund addresses, etc), 2) "Offchain consensus stuff" which are inherently tied to the success/failure of a certain transaction becoming confirmed (Atomic swaps, Uniswap, Serai, etc), and 3) "toy features" like encrypted messaging and storing source code. All of the uses for arbitrary data are NOT relevant to the consensus of a Monero transaction. Monero has no scripts, and it is otherwise generally hard to enforce encryption without a lot of computation. It is hard to enforce randomness without causing weird hard to debug issues like @kayabaNerve mentioned.

My proposal is as follows: move everything consensus related outside of `tx_extra`, and change `tx_extra` to a fixed-length 32-byte hash field. If it ends up not being used in a transaction, fill it with a dummy hash. BUT create relay rules on the daemon side which will store arbitrary blobs (up to a certain reasonable size, say 1024 bytes) which match `tx_extra` hashes for a medium block-time (say 512 blocks), just for wallet's convenience sake. We can also formulate many relay rules regarding these blobs using ideas already mentioned here (encryption enforcement, randomness tests, no ASCII, other length tests, TLV, etc, etc) WITHOUT having to affect consensus (hard or soft forking) or relay reules for the rest of the transaction. Daemon operators will get to choose which arbitrary blobs they host and for how long, creating a "blob pool" alongside the transaction pool.

For every bit of information which is needed for cases 1) and 2), it is in the sender's own interest to communicate that data to counterparties if they go offline for more than 512 blocks. Storing and serving large blobs of non-consensus information should not be a task that the dameons should shoulder, rather the counterparties which need that functionality can just pass it to the person that needs that information. But especially for use case 2, there is easily verifiable cryptographic proof that some specific bit string was constructed and signed by the maker of that transaction (as long as you verify the rest of the transaction).

This scheme mitigates a lot of on-chain spam and the risk of storing illegal content while maintaining usability. It also slightly increases on-chain transaction uniformity (albeit with some flaws). 

EDITED

## kayabaNerve | 2023-02-07T20:06:15+00:00
NACK. This does not properly solve the data availability problem which is why people want to use TX extra in the first place. While it does do better at it than just a 32-byte hash, with the nodes never seeing the payload, this will be extremely frustrating to design around, even with a long block period.

To be clear, I would prefer to steg data than to use such a scheme, just to ensure the data's lifetime is equivalent to the transaction's.

## jeffro256 | 2023-02-07T20:24:15+00:00
> with the nodes never seeing the payload, this will be extremely frustrating to design around, even with a long block period.

What kind of application requires that ephemeral data can't be sent alongside transactions?

## kayabaNerve | 2023-02-07T22:43:04+00:00
In my use case, a DEX with its own blockchain, all interactions require validator interactions or transactions.

To start with the latter, that means users who send in Monero then have to send the payload, which costs fees, creating a chicken and egg problem (need gas to pay for payload, can't get gas because the payload wasn't sent). This does not work.

While the users could send it directly to the validators, this necessitates users being able to directly communicate with validators (which has its own commentary regarding DoSs and network architecture). This is an entire additional data pipeline. I also then have to publish that data onto my chain to ensure a copy is available for as long as relevant (it's relevant till Monero dies or the DEX dies, whichever comes first). While you can argue that's fair, it's my chain's data, as a hub that'll become excessive to store full data payloads from every chain vs minimal representations.

It's infinitely less of a headache to not necessitate that pipeline + publish IPs of validators + store full payload backups on my end to simply having the original chain carry the original data. It's more efficient for storage overall and has one pipeline for Monero, not one pipeline for Monero and one for payloads. Steganography is also far easier than that pipeline and tackles Monero's lack of data with a Monero specific solution.

You can say I'm an ass for this opinion/stance. That's the point. The discussion is on making TX extra not problematic. Nuking its functionality like this is damaging enough it's problematic to some users, who will then seek other options, making it damaging to Monero. It's an inevitability.

TX extra is just one way to store data on chain. Monero needs to either:

- Make it the best option to store data
- Remove it

IMO, your proposal makes it no longer the best option.

## Gingeropolous | 2023-02-08T01:06:45+00:00
so in essence, no prunable solution would work because you ultimately need the data on chain forever. 

## jeffro256 | 2023-02-08T06:56:40+00:00
> You can say I'm an ass for this opinion/stance. That's the point.

I don't mind, I don't think you're an ass :). I'm a gremlin that thrives on disagreement, so don't worry about that.

> creating a chicken and egg problem (need gas to pay for payload, can't get gas because the payload wasn't sent). This does not work.

Now I won't claim to be an expert on Serai, but validators need to be able to access on chain Monero transactions anyways right? The rules can be changed such that required blockchain blobs which are verifiable can allowed on the Serai chain, no?

> as a hub that'll become excessive to store full data payloads from every chain vs minimal representations.

If it's excessive for your chain, imagine how much more excessive it is for every other node operator who has to store payloads for Serai when they don't even use it. These "excessive payloads" would make running a node on low grade hardware much less feasible, reducing decentralization.

> It's more efficient for storage overall

Not necessarily, since on-chain Monero space is arguably (at least right now (; ) more expensive and more valuable than Serai chain space, especially due to the large PoW base. 

> Steganography is also far easier than that pipeline and tackles Monero's lack of data with a Monero specific solution.

This is a whataboutism, IMO. Just because there are other uniformity weaknesses in Monero's transaction protocol is not an argument to allow large arbitrary payloads embedded in transactions.

>  TX extra is just one way to store data on chain. Monero needs to either:
>
>    Make it the best option to store data
>    Remove it

I don't think it needs to be that black and white. You mentioned "minimal representations". You argue that the minimal representation should be stored on the Serai chain, while the Monero chain shoulders the burden of bulk data. I believe it should be the other way around, since I believe it makes more sense from a privacy standpoint and from a self-interest standpoint. We might just fundamentally disagree on that, though. I don't know how to fix that.

> IMO, your proposal makes it no longer the best option.

Yes, I agree. `tx_extra` shouldn't be the most efficient way to store data because storing data inside a PoW blockchain will always be 100,000x less efficient than just sending a regular old TCP message to a counterparty. In my opinion, if the data is not necessary for consensus, then it should not be on a blockchain. It makes sense to put hashes of stuff on chain, as to indirectly verify that data through hard consensus, but it doesn't make sense to keep that stuff embedded in-chain forever for anyone who is not a counterparty. If some data is necessary for your concensus, Serai or otherwise, you will be self-interested in propogating/storing that data. Thus, those problems will sort themselves out naturally. Is that kind of a "screw you deal with it" answer? Maybe. But it puts the burden on those who who use the features, and not everyone else.

Hopefully, inb4 "[Discussion] Consider removing non 2-output transactions"

Mandatory: sorry for being an ass

## spirobel | 2023-02-08T09:36:49+00:00
@kayabaNerve 
>TX extra is just one way to store data on chain. Monero needs to either:

    Make it the best option to store data
    Remove it

>IMO, your proposal makes it no longer the best option.

and that is really the gist of it.
We should also avoid adding more and more "clever" little bureaucratic rules to the monero codebase and consensus.
Like this one for example: https://github.com/monero-project/monero/pull/8733

The tradeoff is between arbitrary data saved on the blockchain and low transaction fees.
No amount of clever little rules is going to change this.
Also the goal of @tevador to make this use case more inefficient is counterproductive and damaging to the long term value and health of the Monero chain and ecosystem.
There are two reasons for this:
1. The tradeoff of low fees and arbitrary data saved on the blockchain cant be avoided by making it more inefficient to save the data. **It makes the bloat problem even worse.** It will still be cheaper to save data on the Monero blockchain compared to Bitcoin for example. No matter if you add a premium to it by making it more inefficient. All you achieved is adding even more bloat and overhead to the chain.
2. Ad hoc additions of new rules damage the trust in the consistency and continuity of the meta consensus, that we create here about the monero protocol. We need to give people reason to believe that the rules can't be changed randomly because somebody does not like the aesthetics of what is being saved on chain. **It is also important to keep sending this message to governments and regulators. Code is law. And this law can't be changed randomly because of someones feelings.**

@jeffro256 
> It is hard to enforce randomness

it is impossible in general to prove that something is random.
Can we please all agree on this assumption?

That is a philosophical and scientific fact. **It is impossible to prove that something is random.** I thought that was common knowledge and I am a bit surprised that we even need to have this conversation.

If anyone has doubt about this, we should walk it through and make sure we convince ourselves of this very basic truth: there is no way to prove that something is truly random.



## tevador | 2023-02-08T11:59:21+00:00
> We should also avoid adding more and more "clever" little bureaucratic rules to the monero codebase and consensus.
> Like this one for example: #8733

It's a relay rule, not a consensus rule. Node operators have every right to place restrictions on the data that resides on their machines. There is broad consensus that the default limit should be what the PR is proposing. Anyone who disagrees can simply change the limit before building their binary. That's the power of open source software.

> The tradeoff is between arbitrary data saved on the blockchain and low transaction fees.

As I said before, fees only limit the volume of spam, not its content. This discussion is not about fees.

> That is a philosophical and scientific fact. It is impossible to prove that something is random.

That's an irrelevant technicality. You can decide that something is **not random** with a probability of *p*, for a value of *p* arbitrarily close to 1. It's called statistical hypothesis testing.


## j-berman | 2023-02-08T13:06:21+00:00
I don't think statistical testing for uniformity will work. It sounds trivial to fool. Simply use an encoding scheme where you XOR plaintext with a static random pad, and then decode by doing the same.

Example plaintext payload:

00000000 10101010

Static random pad:

01101000 11101001

Encoded payload that will pass a uniformity check:

01101000 01000011

## tevador | 2023-02-08T13:25:49+00:00
At least it would force developers to think about encryption. Static key streams, reused nonces, AES-ECB are all better than plaintext. There is a good chance that at least some of them would use a common library that offers secure encryption.

## spirobel | 2023-02-08T14:43:37+00:00
@tevador 
>As I said before, fees only limit the volume of spam, not its content. 

So you want to police the content of transactions? Dangerous precedent to set. We are trying to build a censorship resistant system. **It is not a good signal to be sent to governments and regulators that ad hoc rules can be added that police the content of transactions.**

For sure there needs to be a consensus that clearly defines what is a valid transaction and what isn't. But these rules need to make sense.
>At least it would force developers to think about encryption. Static key streams, reused nonces, AES-ECB are all better than plaintext. There is a good chance that at least some of them would use a common library that offers secure encryption.

"Developer education" is not a valid reason to add rules to the Monero network.
A consensus or relay rule is not the right place to give lectures.

>This discussion is not about fees.

Yes it is. That is the tradeoff. If you limit the size of tx_extra the jpg can just be split into parts and you end up with even more overhead.

>Node operators have every right to place restrictions on the data that resides on their machines. 

That means they are liable for its content. This logic is wrong. We should not go down this route because it will directly lead to censorship. This is similar to the discussion that happens in bitcoin right now. **Code is law.** The feelings of node operators should not matter. They need to be bound by this law and by nothing else.

>You can decide that something is not random with a probability of p, for a value of p arbitrarily close to 1. It's called statistical hypothesis testing.

that is snake oil cryptography. **You can't prove that something is random and you should not try.**

## jeffro256 | 2023-02-08T15:53:18+00:00
> that is snake oil cryptography. You can't prove that something is random and you should not try.

No one said anything about “proving” randomness, though. A statistical randomness test is not a proof of anything, it would mainly just prevent users from making from low effort abuse or accidents. I don’t think we should do it just because it might make UX a little worse unpredictably, but don’t strawman.

## tevador | 2023-02-08T15:59:31+00:00
> So you want to police the content of transactions?

Yes, we want to police transactions for maximum uniformity. This is already done in Monero:

* We require a specific ring size (since v8).
* We require at least 2 outputs in all transactions (since v12).
* The 10-block lock time is enforced (since v12).
* etc.

Do you also consider this to be "censorship"?

> A consensus or relay rule is not the right place to give lectures.

It is when the privacy of others or the network security is in stake. For example, the 10-block lock time was often violated (by mistake or on purpose) by wallet developers before being enforced by consensus in 2019.

> If you limit the size of tx_extra the jpg can just be split into parts and you end up with even more overhead.

If someone wants to spam the network, they can do so even without tx_extra.

> The feelings of node operators should not matter.

They do matter. Nodes are run by volunteers. Ideally, we don't want them to be forced to shut down.



## spirobel | 2023-02-08T16:30:26+00:00
@jeffro256 

> If some data is necessary for your concensus, Serai or otherwise, you will be self-interested in propogating/storing that data. Thus, those problems will sort themselves out naturally. Is that kind of a "screw you deal with it" answer? Maybe. But it puts the burden on those who who use the features, and not everyone else.

There should be some consideration for data that is not directly necessary for the consensus of the main protocol. Without projects like @kayabaNerve 's Serai, Monero will become an island.
All successful chains allow this to some degree or another.

While the main focus should be on the security of the consensus of the main chain, we should not ignore the outside world completely.

>No one said anything about “proving” randomness, though.

You said enforcing randomness is hard. It is not hard. It is impossible. 

>don’t strawman.

why are we discussing this with such a seriousness then? From the suggestion that enforcing randomness is hard (and not impossible) and the vigor in which @tevador presents his ideas here, I gathered that maybe we were not as aware of this ground truth as we should be.

>I don’t think we should do it just because it might make UX a little worse unpredictably,

I agree! Good point! Same goes for the size limit.

@tevador 
>Do you also consider this to be "censorship"?

I consider these duct taped solutions until the root problem is fixed.
It would be better if we spent our efforts on this.

Why are you not working on the issue that you mentioned earlier?
https://github.com/monero-project/research-lab/issues/100
Would be a better use of your time!

>It is when the privacy of others or the network security is in stake.

I totally I agree with this. That is why we need to fix the root cause and not try to chase the aesthetics of randomness here which will give us nothing. It just makes the user and developer experience worse.

>They do matter. Nodes are run by volunteers. Ideally, we don't want them to be forced to shut down.

So it would be best to not make changes that enable selective censorship of "spam" at the node level. Lets just not go down this rabbit hole.

## tevador | 2023-02-08T16:46:28+00:00
> I don’t think we should do it just because it might make UX a little worse unpredictably

The test can be deterministic, so there would be no unpredictability.

> I consider these duct taped solutions until the root problem is fixed.

As I said earlier, the problems caused by transaction non-uniformity cannot be fully solved just by a better membership proof.

See: https://github.com/zcash/zcash/issues/4332

## jeffro256 | 2023-02-08T17:02:25+00:00
> I agree! Good point! Same goes for the size limit.

> The test can be deterministic, so there would be no unpredictability.

Yes, and no. The test itself would be deterministic, but if you construct a payload and it happens to fail the randomness test, you have to change the message, whether that is an issue or not depends on if you expect the test to fail and have a nonce to inject randomness, or something else similar. Just adds an extra layer of tests which you can't necessarily predict before making the payload, unlike with a length limit which is very easy to verify beforehand. 

## spirobel | 2023-02-08T17:03:04+00:00
@tevador 
>As I said earlier, the problems caused by transaction non-uniformity cannot be fully solved just by a better membership proof.

but obviously they make the problem a lot less severe. Decoy selection is one of the weakest points of Monero.
And I am sure you can come up with a way to overcome the challenge that you mentioned! 

How would you deal with the arity correlation attacks? are there similar attacks? 
Maybe you can add that to the issue that you mentioned: https://github.com/monero-project/research-lab/issues/100

>The test can be deterministic, so there would be no unpredictability.

the test would also be useless, because it can be circumvented easily.
It is better to work on things where we can actually have an impact.

The last post by @narodnik https://github.com/monero-project/research-lab/issues/100#issuecomment-1374407464

did not get an answer yet. He also seems very willing to help as he indicated earlier.
So it would be a good idea to confront him with these concerns you have identified.


## jeffro256 | 2023-02-08T17:16:11+00:00
> Yes, we want to police transactions for maximum uniformity. This is already done in Monero:
>
>    We require a specific ring size (since v8).
>    We require at least 2 outputs in all transactions (since v12).
>    The 10-block lock time is enforced (since v12).
>    etc.

+1. We should move towards transaction uniformity since fungibility has always been one of the, if not the most important, goals of Monero. It's what separates digital cash from speculative garbage coins. As @spirobel pointed out, removing `tx_extra`, or at least standardizing it, will not fix all transaction uniformity problems. Also, as @tevador pointed out, neither will simply changing membership proofs. Improving `tx_extra` does not need to be the silver bullet that fixes everything uniformity related, but it would help. IMO, we should explicitly leave in one field per transaction which would indirectly allow other arbitrary data to be verified through Monero PoW, but no more than that. 

## spirobel | 2023-02-08T17:28:30+00:00
>+1. We should move towards transaction uniformity since fungibility has always been one of the, if not the most important, goals of Monero.

Ultimately it is about fungibility of coins and not of transactions. Transaction uniformity only matters because we need to select decoys and that means utxos are still somewhat connected to transactions.

https://github.com/monero-project/research-lab/issues/100 this issue is about trying to find a solution where utxos get completely disconnected from transactions.

It seems like @tevador has identified some caveat to this, but it is still better to investigate this caveat instead of trying to beat the dead horse of tx_extra removal or restrictions.

It will have a much bigger impact than this.

## tevador | 2023-02-08T17:40:02+00:00
> if you construct a payload and it happens to fail the randomness test, you have to change the message

Assuming you use a secure encryption method (IND-CPA), there must be a nonce, so the tx builder API can simply reroll the nonce until the test is passed. With a test confidence of 0.95, you can expect to have to encrypt 1.05x before you have a valid ciphertext. Note that a similar "reroll the nonce" process already exists when constructing the range proof.

> IMO, we should explicitly leave in one field per transaction which would indirectly allow other arbitrary data to be verified through Monero PoW, but no more than that.

Ideally, the size of the "extra" field should not be arbitrary, but it could be a function of the number of outputs. For example 128 bytes for all 2-out transactions (this is enough to fit a refund address) and `32*num_outputs` bytes otherwise. If the field is also encrypted, this would leak the least amount of information.

@spirobel I think most of us agree that implementing trustless zk-SNARKs would be great for Monero, but it's not something that can be done quickly. Feel free to continue the discussion [there](https://github.com/monero-project/research-lab/issues/100) and let's focus on tx_extra here.

## spirobel | 2023-02-08T17:48:04+00:00
@tevador 
>I think most of us agree that implementing trustless zk-SNARKs would be great for Monero, but it's not something that can be done quickly. Feel free to continue the discussion https://github.com/monero-project/research-lab/issues/100 and let's focus on tx_extra here.

Both of these issues are related. 
As @kayabaNerve mentioned earlier: a SNARKs PoC could be done in weeks and an actual implementation in months.

It seems currently that this kind of project is blocked by seraphis and its outcome.

**We should make a competition between seraphis and a SNARK based protocol.** 

What do you think about that?
It would also have the added benefit that it would reduce researcher bias during the Seraphis audits and we would have an alternative if Seraphis does not come through for whatever reason.


## kayabaNerve | 2023-02-08T18:08:25+00:00
1) This conversation has gone off the rails.

2) I don't want to infinitely discuss Serai's architecture. While I don't mind briefly doing so, I'll keep my commentary short.

> It's more efficient for storage overall

Was a comment that given the full payload and the minimal payload, the storage cost is F+M. With an additional hash on Monero, the cost is H+F+M, compared to Monero just having F and us having M. While there are discussions on if Monero could have H and H could be of M which we have, as the 'minimal' payload is only slightly more minimal in this context, the main issue is chain-specific post-processing we'd have to move on-chain which is hell.

Also, yes, you can say Monero shouldn't have any payloads and you're not an ass for doing so. I'm telling you the path of least resistance for me is to put this data on Monero and I'm going to. You can either:

A) Let me do this in the best way for all of us. That means a sane TX extra amenable to users who want to place data on Monero.

B) Accept people will just use steganography, which may already be preferable.

Personally, I already summarized what I think makes sense for TX extra, yet I legitimately wouldn't mind only having steganography. I also want to comment all my advocation for Monero has been what I legitimately believe is best for Monero, not for my own project. I just acknowledge that this feature is meant to be used so the question is what's legitimately useful, and I've advocated for it to be legitimately useful (or removed due to the vector it is).

3) > I don't think it needs to be that black and white.

If TX extra isn't the best way to store data on Monero, it has no reason to exist. The wallet protocol shouldn't be there, as universally agreed. If people aren't using it for arbitrary data, then no one is using it for anything except exploits due to our increased surface area of having it. While I won't say it must be the best way for every single use case and every person, I believe it not solving the data availability problems makes it far too infrequently the best way to store data on Monero. Since its only point is to be the method to store data on Monero, why keep it around then?

4) We should improve the protocol as we can. There are many issues with Monero and we should work to fix those. If you want a static protocol, go bother BSV or don't update your node. I don't care to halt discussion on the premise changes due to discussions are bad.

5) I don't want to comment on SNARKs, a completely unrelated topic, yet it keeps getting brought up. I call for everyone to stop discussing SNARKs in this discussion and if someone else brings it up, just ignore it.

## spirobel | 2023-02-08T18:14:56+00:00
> a completely unrelated topic, yet it keeps getting brought up. I

It is getting brought up because it is related to transaction uniformity. The reason  we are worried about tx_extra in the first place. It would address the root cause of this whole debate.


## kayabaNerve | 2023-02-08T19:49:31+00:00
No, it wouldn't. There are many different ways transactions can be non-uniform. The ring is a completely different topic from TX extra. While both can make TXs non-uniform, one does not affect the other.

## spirobel | 2023-02-08T21:02:53+00:00
>No, it wouldn't.

yes it would. 

>The basis of the privacy properties of Zcash is that when a note is spent, the spender only proves that some commitment for it had been revealed, without revealing which one. This implies that a spent note cannot be linked to the transaction in which it was created. That is, from an adversary’s point of view the set of possibilities for a given note input to a transaction —its note traceability set — includes all previous notes that the adversary does not control or know to have been spent.

>This contrasts with other proposals for private payment systems, such as CoinJoin [Bitcoin-CoinJoin] or CryptoNote [vanSaberh2014], that are based on mixing of a limited number of transactions and that therefore have smaller note traceability sets.

from: https://zips.z.cash/protocol/protocol.pdf

You would still have to worry about some meta data leakage as @tevador pointed out. But there is still a fundamental difference in the impact that transaction uniformity has on privacy. It turns "everything could be a problem" into "some things could be a problem."

There is no point to just focus on tx_extra if we are unwilling to make changes so that there is no link between notes and transactions anymore.
Then we need to focus on transaction uniformity in general and not just tx_extra.






## UkoeHB | 2023-02-08T21:14:26+00:00
Transaction uniformity is not an all-or-nothing game, there are many incremental improvements that can and should be made as solutions present themselves.

## LocalMonero | 2023-02-08T21:18:57+00:00
In addition to the tx uniformity argument, one more argument in favor of removing the tx_extra field is that a dynamic (i.e. potentially infinite) block size that Monero has combined with an arbitrary field leads to Monero becoming a vector for uses that aren't money, meaning it's going to be less efficient at what its purpose is: being next-gen money.

## paulshapiro | 2023-02-08T21:21:20+00:00
Okay but what exactly is "money"?

Like ukoe says there are increments. 

We just need to make sure we're not making monero useless at the expense of an ideal. 

## LocalMonero | 2023-02-08T21:25:36+00:00
Digital cash. I.e. a decentralized, fungible, electronic way of transferring value and storing it.

If incremental improvements present themselves we can fork.

## spirobel | 2023-02-08T21:35:06+00:00
@UkoeHB 
>Transaction uniformity is not an all-or-nothing game, there are many incremental improvements that can and should be made as solutions present themselves.

How do you differentiate between sweeping things under the carpet and actually improving transaction uniformity?

The presented solutions here sound more like rug sweeping. @kayabaNerve says he does not mind using steganography to insert data into the Monero blockchain for his serai protocol.

The actual danger here is that these transactions get selected as decoys by other users and it damages their privacy. It would be much better if we went the opposite route and the serai transactions were clearly marked as serai transactions and the decoy selection algorithm of other Monero users could ignore those.

We dont know what kind of information an adversary could gather through observing these outside protocols and then seeing all these Monero transactions with steganographically hidden information inside of them as decoys.

@LocalMonero 
>In addition to the tx uniformity argument, one more argument in favor of removing the tx_extra field is that a dynamic (i.e. potentially infinite) block size that Monero has combined with an arbitrary field leads to Monero becoming a vector for uses that aren't money, meaning it's going to be less efficient at what its purpose is: being efficient next-gen money.

you obviously have a vested interest in not having an easy to use DEX, but even aside from that this it is just unrelated to tx_extra. 

You can save arbitrary data on Monero without tx_extra if you get creative. This whole debate is just about aesthetics.  

## LocalMonero | 2023-02-08T21:48:15+00:00
Didn't think I'd encounter an ad hominem attack in a tx_extra field discussion 😅

Our interest is in Monero succeeding, with or without an easy-to-use DEX (but preferably with). In addition, there's nothing in the concept of an easy-to-use DEX that is necessarily dependent on a certain blockchain having an arbitrary data field.

> You can save arbitrary data on Monero without tx_extra if you get creative.

There's a difference between constructing a tx a certain way to hide arbitrary data and having a field that invites arbitrary data. The conceptual discussion revolves around plugging those holes to the greatest possible extent.

## spirobel | 2023-02-08T21:51:25+00:00
>The conceptual discussion revolves around plugging those holes to the greatest possible extent.

please read the comment above again. The question is if we sweep things under the rug or if we actually help users select good decoys. 

So some might think they are plugging holes, while it makes it harder in practice to distinguish between what is a good decoy and what is a bad decoy.

Of course it would be best and it would change the whole situation if we would not have to select decoys in the first place.

## LocalMonero | 2023-02-08T22:07:52+00:00
Decoys are separate question. The question here is whether a field for arbitrary data should be allowed on the Monero blockchain, arguments pro and against.

## spirobel | 2023-02-08T22:17:26+00:00
>The question here is whether arbitrary data 

Again. There is no way to prevent that. 

>Decoys are separate question. 

No they are related. That is actually the real issue here. What happens if your wallet selects transactions as decoys that look random and uniform, but in reality they are special transactions made by a separate protocol like serai?

wouldn't it be better for the decoy selection algorithm of your wallet to know that these are not actually uniform and have stegnographically inserted information in them?

wouldn't it be better if they were excluded from the decoy selection process, especially if there is additional information disclosed to the public by this separate protocol?

## LocalMonero | 2023-02-08T22:28:07+00:00
> Again. There is no way to prevent that.

Removing the arbitrary data field clearly does a huge service to this end. Any further holes can be plugged to the greatest possible extent so as to render arbitrary data storage unfeasible through impracticality, strengthening fungibility and improving time and space efficiency of Monero at the same time.

> No they are related. That is actually the real issue here. What happens if your wallet selects transactions as decoys that look random and uniform, but in reality they are special transactions made by a separate protocol like serai?

If the Monero protocol is constructed strictly enough to ensure uniformity then they will be indistinguishable by definition.

> wouldn't it be better if they were excluded from the decoy selection process, especially if there is additional information disclosed to the public by this separate protocol?

No, it would be better if there were no distinguishable outputs in the first place. What you're proposing (excluding decoys due to them being Serai-related) is a direct threat to fungibility.

## kayabaNerve | 2023-02-08T22:28:36+00:00
1) I almost wish for this discussion to be whitelisted re: participants.

2) We can:

- Keep TX extra, optionally with statistical checks, optionally in a mode where it's prunable. I wouldn't mind if TX extra contributed towards the TX via its hash *and* pruned nodes only kept the hash. I personally mind when full nodes fail to solve the data availability problem.

- Remove TX extra in favor of steganography.

This discussion needs to be refocused on these two topics.

Personally, I believe it sounds like no one's actively calling to completely remove TX extra. Accordingly, I'd actually argue to refocus to:

- Do we want a statistical check/ASCII ban?
- Should TX extra be hashed re: TX/sig hash?
- Should pruned nodes keep TX extra?
- Should full nodes keep TX extra?

I only personally insist on the last one. I think TX extra being prunable, and pruned nodes pruning it, is sane, as I do statistical checks and an ASCII ban.

After these questions, all that remains is TX extra size discussions. I believe the currently open PR is a good first step, and would like to wait to further discuss size until we know how TX extra will exist as a concept.

## LocalMonero | 2023-02-08T23:11:44+00:00
> Personally, I believe it sounds like no one's actively calling to completely remove TX extra. 

@kayabaNerve I'm pretty sure most people would agree that it needs to be removed, especially with Ordinals reigniting this discussion and making it clear what a liability arbitrary data can be. it is no coincidence that ordinals exploding in popularity led to the biggest Bitcoin blocks ever mined, one can only speculate how it would affect Monero with its potentially infinite block size.

Nobody is denying that the field can be used for good, such as for a DEX like yours. However, one can have a DEX without also having the downsides of the arbitrary data storage field.

@UkoeHB states:
> it's a field that's literally 'for anything we can't know in advance or are unable to pass judgement on'

This is not an asset. It's a liability.

## kayabaNerve | 2023-02-09T00:33:32+00:00
@LocalMonero I will note your objection. If we remove TX extra, it will be effectively supporting steganography, increasing the amount of outputs, not allowing pruning, and globally increasing scan time. tevador, koe, jeffro, myself, and I believe sgp and hyc are for keeping it.

I recently talked with @jeffro256 on Monero Research Lounge. It sounds like we do mutually agree on making TX-extra prunable. This would mean only including it sig/TX hashes by hash, and having pruned nodes prune it. While we can further work on this (split full nodes into full/archive, with its own discussions there*), that'd be the first step.

Since TXs would only truly hold the hash, and nodes would be able to prune it, I don't feel a need to enforce any properties on the payload itself. We *can* still do a statistical check however.

*It should be possible to configure a node to hold all TX extras, and it should be possible for any new node to join and sync all historic TX extras so long as any node on the network still has a copy IMO. If those conditions are met, I wouldn't mind if full nodes only kept a week's worth, and only 'archive' nodes kept everything. The issue is how do two, not directly connected, archive nodes still sync over a net of (presumably primarily) full nodes?

## LocalMonero | 2023-02-09T00:49:30+00:00
> If we remove TX extra, it will be effectively supporting steganography, increasing the amount of outputs, not allowing pruning, and globally increasing scan time.

@kayabaNerve Could you please describe exactly how you plan on encoding data into the blockchain in the absence of tx_extra?

> tevador, koe, jeffro, myself, and I believe sgp and hyc are for keeping it.

I didn't see them stating that they are outright *for* keeping it, most of them have only directly stated to be *against* keeping it. I only saw them propose what *additional policing* needs to be done to the field *if it is kept*. Would @Tevador @UkoeHB @jeffro256 @SamsungGalaxyPlayer and @hyc please confirm that they are for keeping the tx_extra field?

## spirobel | 2023-02-09T00:58:08+00:00
>@kayabaNerve Could you please describe exactly how you plan on encoding data into the blockchain in the absence of tx_extra?

I would like to know too. Fake outputs already seem obvious. But how would we use CLSAGs. You mentioned earlier that there is also the possibility to save data in the CLSAGs. Are there any pitfalls with this?

## kayabaNerve | 2023-02-09T01:54:46+00:00
@LocalMonero Fake outputs to fake keys. On the one hand, such TXs will appear like any other, other than having more than two outputs. On the other hand, they'll globally increase scan time, be un-prunable, and take up twice as much space as arbitrary data would have. That's the trade off.

@spirobel A reduction in sender privacy.

Also, I'm pretty sure my list of "for" is correct, yet if I did miscategorize anyone, I apologize.

EDIT: Upon misreading, tevador explicitly said to the contrary, later acknowledging there's a larger issue regardless. But that's definitely not for keeping it. Sorry, tevador. I do know koe is for keeping TX extra based on comments from IRC. The only other person I dragged in, explicitly, was jeffro, who I'll confirm with now

## LocalMonero | 2023-02-09T02:00:34+00:00
@kayabaNerve could you please go into detail on how you would construct the tx and how the data would be encoded so that we can get a better idea of the time, space and cost requirements per byte of data that you wish to encode?

## kayabaNerve | 2023-02-09T02:01:44+00:00
@LocalMonero It's been prior discussed. https://github.com/monero-project/monero/issues/6668#issuecomment-1195807365

Here's koe commenting, on this issue, against steganography: https://github.com/monero-project/monero/issues/6668#issuecomment-1195962883

I'd also note tevador, the party who frequently brings up limiting TXs to just 2 outputs (though I'm unsure if they were the original proposer of the idea), acknowledging it's not currently a good idea: https://github.com/monero-project/monero/issues/6668#issuecomment-1418051785

Without doing so, you cannot prevent steganography by outputs. Even when you do are several options available. Some damaging to Monero, some not.

Here's jeffro discussing a "good compromise", which involves keeping TX extra: https://github.com/monero-project/monero/issues/6668#issuecomment-1420920513 I've also privately confirmed they're for fixing, not removing.

## LocalMonero | 2023-02-09T02:17:41+00:00
> It's been prior discussed. https://github.com/monero-project/monero/issues/6668#issuecomment-1195807365

@kayabaNerve Thanks. Sounds like an additional arbitrary data hole that needs to be plugged. I agree that limiting to two outputs is a bad idea. I also, like @tevador, don't have ideas on how to prevent this. This doesn't mean, however, that there is no fundamental solution or that an arbitrary data field is desirable or that arbitrary data in the Monero blockchain is desirable.

As I see it, and correct me if I'm wrong, your argument is basically "Some people want to doodle on a dollar bill. You can't stop them from doodling on it, so let's dedicate some white space on the dollar bill for doodling".

My argument is that if we can prevent doodling we should to the greatest possible extent do that and make it a design goal, not cater to the doodlers.

## kayabaNerve | 2023-02-09T02:23:04+00:00
@LocalMonero Monero has to decide what's best:

- A new iteration of TX extra, sanely ruled yet still sufficiently desirable.
- Leaving people who want to put data on chain to use steganography, with all its upsides and downsides.

The discussion here has been making TX extra sane, limiting spam. @jeffro256 proposed a prunable solution, which I endorsed. There's an open PR to limit size already, as a relay rule. We've also discussed preventing malicious messages and ensuring message uniformity. This entire discussion here has been sane design goals to limit bs. Keeping TX extra, in some form, just ends up being the best way to limit bs.

If you have a third option, please let us know.

## kayabaNerve | 2023-02-09T02:38:16+00:00
> - Do we want a statistical check/ASCII ban?
> - Should TX extra be hashed re: TX/sig hash?
> - Should pruned nodes keep TX extra?
> - Should full nodes keep TX extra?

Back to these, I don't see any reason TX extra shouldn't be hashed, allowing pruning, and why pruned nodes should keep it. I'd raise the further question: Do we want TX extra to be per output?

A continually raised point has been about per-output usage/per-output sizing. Moving from a TX extra to an output extra would signify that. I'd question exactly how this should be implemented, as it wouldn't be preferable if pruned TXs grew 32b per output compared to 32b per TX, but they're are plenty of discussions possible down that route.

I'd also like to question if a statistical check is still desirable when the actual TX only has a hash the Monero node itself made, guaranteeing its uniformity. I personally would say the situation is largely unchanged, yet others may disagree.

## LocalMonero | 2023-02-09T02:38:35+00:00
@kayabaNerve  Monero should not cater to those who want to put arbitrary data on the chain. I acknowledge that to a certain extent this is impossible to fully prevent, but that doesn't mean that it should be catered to or made a design goal, which is akin to the Federal Reserve leaving some blank space on dollar bills for people to doodle on because they cannot prevent people from doodling on bills. It almost encourages people to.

The "steganography" hole for arbitrary data will exist in Monero with or without the tx_extra field. Your framing of this as "either we do tx_extra or steganography" is a false dichotomy from the blockchain's point of view. The pruning angle is also a dead end as @Gingeropolous explained https://github.com/monero-project/monero/issues/6668#issuecomment-1421730675

If you're going to "steg" your way into recording arbitrary data into the chain then so be it. Hopefully as the software continues to develop this will become harder and more costly so as to eventually become impractical.

## kayabaNerve | 2023-02-09T02:42:10+00:00
If we do not compromise with them, we accept that they'll move to a solution that multiple people view as even worse for Monero. There's also the argument it's better for Monero as it's less distinguishable. I'll also note, as I've said prior, I wouldn't actually mind being moved to steganography. It's still perfectly fine for the amount of data I'm looking to place in TXs, is less distinguishable, and actually only ~2x as much as TX extra currently is.

Ginger's comment was in response to my own comment on jeffro's solution failing the data availability problem. I later commented here: https://github.com/monero-project/monero/issues/6668#issuecomment-1423429102 my support for a prunable solution and commented how data availability would be amenably handled under it.

## LocalMonero | 2023-02-09T02:48:35+00:00
@kayabaNerve I don't see it as worse. Since it's basically the same as a tx and you're paying for the tx fee then it's indistinguishable from the tx, which helps fungibility. We can tweak the tx format to plug these holes even further in the future. Not removing but standardizing and expanding the tx_extra field will only invite further reliance upon it with all the associated baggage, not to mention the increased complexity of the protocol due to its presence leading to worse UX and DX (with all the rules that will be applied to it that are being discussed over in this thread, some of which will almost certainly change as issues with existing rules are discovered) . Since you don't seem to mind either I think the path forward is clear and the tx_extra field should be removed.

## kayabaNerve | 2023-02-09T02:54:24+00:00
- It's about half as efficient by space usage
- It's not prunable
- It decreases privacy* by adding junk outputs as possible decoys (given no complete membership proofs)
- It globally increases scan time

If you still believe it's better, I will stop arguing the point with you. You are welcome to have that belief, as it does still have merit.

It's also not clear. I'm fine with either, but I prefer an explicit extra. @jeffro256 is for fixing, not removing. koe is against steganography > extra. tevador is against keeping extra last time they commented one way or another. The other commentators I'd want to hear from, for their thoughts, are sgp and hyc.

*Any TX with extra does also decrease privacy. It just only does it for its two outputs. Not the n a TX with more than 2 outputs will. It's a trade off.

## LocalMonero | 2023-02-09T03:15:45+00:00
@kayabaNerve 
> It's about half as efficient by space usage

That's good, Monero should not be space-efficient for arbitrary data.

> It's not prunable

And if tx_extra *is* prunable and through its existence encourages people to use it for their applications then you are discouraging people from running full nodes in order to avoid hosting application data, which leads to centralization. So it's a trade off, and a bad one AFAIC.

> It decreases privacy* by adding junk outputs as possible decoys (given no complete membership proofs)

This is an invalid argument as this capability exists with or without the tx_extra field.

> It globally increases scan time

By what percentage would you calculate the global scan time would increase?

## spirobel | 2023-02-09T03:22:42+00:00
>By what percentage would you calculate the global scan time would increase?

we would have to know how many transactions will result from this and that is something we dont know yet.
Also wonder how this relates to viewtags. Could the fake outputs interfere with viewtags?

>That's good, Monero should not be space-efficient for arbitrary data.

You should scroll up this thread, I think we went through this loop in the dialog tree already.
It is also interesting to read that at the beginning of this thread the sentiments about this topic were a lot different and people seemed to have changed their viewpoints on this. 


## LocalMonero | 2023-02-09T03:47:51+00:00
One extra point counterpoint about the scan time, any set of rules that will be devised over the kept tx_extra field will also add scan time to check the field against those rules. The complexity of those rules will determine the additional scan time, obviously. Not to mention the increased added global UX and DX complexity associated with tx_extra being a part of the protocol.

Fundamentally the question one must answer to determine their position is as follows:
Is arbitrary data desirable on the Monero blockchain?
    a. If yes, then tx_extra is desirable
    b. if no, then tx_extra should be removed 


## dan-da | 2023-02-09T15:31:27+00:00
+1 for remove tx_extra.

I zoom out a bit, and think of monero as digital cash.  Cash does not have any memo field.  Yet finance still exists using cash.    Contracts are often/usually payable with cash.  Loans can be repaid with cash, etc.   Cash is plenty good for pawnshops, loan sharks, etc.   They simply keep their own ledger.

I think Bitcoin muddied the waters a bit with its "scripts" and "programmable money" that has the potential to turn each tx into a contract with its own rules.  And then Eth went full throttle with the idea.  Both at the expense of fungibility.   To me though, it seems that cash/money is a separate concern from a contract.  A good money is fungible with each unit the same as every other.  A good contract will refer to sums of fungible money but need not specify individual notes.

In summary, I think that tx_extra is baggage from bitcoin that never should've been included in monero and should be removed.   For monero to succeed it must become and remain the most fungible money.  This is one step on that path.  

## vtnerd | 2023-02-09T17:33:23+00:00
@kayabaNerve my apologies for the lazy request for information - this thread is quite long - have you written down what you intend to put in `tx_extra`?

FWIW, the people expressing their opinions about how `tx_extra` need to be removed for privacy purposes aren't necessarily considering how other projects interact with Monero. Is Monero claiming to be the do-everything chain? That stuff outside of pure fungible money is irrelevant and unnecessary (NFTs, etc)? That adaptor signatures are sufficient for all interactions? That centralized exchanges are sufficient? And mind you - I have a couple of ideas for NFTs which aren't too scummy and my humble opinion way more fascinating than the last round of "whatever" NFTs - but these ideas are years out if ever going to met.

Basically, @kayabaNerve isn't necessarily some jerk trying to hijack Monero, he represents a potential honest real-world user that could highlight where future MRL funding should go (i.e. the users requesting removal should possibly be campaigning for MRL funds for taproot+bulletproofs research to meet his demands instead of the other way around).

## vtnerd | 2023-02-09T17:38:10+00:00
> (i.e. the users requesting removal should possibly be campaigning for MRL funds for taproot+bulletproofs research to meet his demands instead of the other way around).

There's also the perspective that Monero should just have a fixed-size `tx_extra` which I think is the most fascinating argument, far more than removal.

## vtnerd | 2023-02-09T17:40:27+00:00
Also @hyc @kayabaNerve @tevador is 256-bytes enough for a statistical test? It would filter out blatant uses of ascii and unicode, but possibly not much else ... or ...?

## kayabaNerve | 2023-02-09T17:46:38+00:00
~80 bytes of structured data which will be publicly accessible to anyone in the know, yet I'll probably encrypt on chain (with a static, public key) just to be polite there.

I've made my arguments out of a legitimate belief TX extra is better than steganography. For it to be better, it must be more appealing. As a real world user, I can comment what's desired/appealing. That's how I've premised my discussions. None of it has been about what's necessarily best for me.

Active questions:

- Do we want TX extra at all, or to shunt users to steganography? Myself, koe, and jeffro do. I believe tevador does not. I'm unsure on hyc/sgp. LM and dan-da have since commented in favor of removal.
- Do we want a statistical check/ASCII ban? I assume just 32-bytes would be plenty. At a nibble level, that'd be 64 samples of a value with only 16 options.
- Should TX extra be hashed re: TX/sig hash? I don't see why it shouldn't be, enabling pruning. jeffro agrees, I believe tevador also liked this idea.
- Should pruned nodes keep TX extra? I, and jeffro, have said no.
- Should full nodes keep TX extra? <- I say yes. Else, TX extra fails to solve the data availability problem. While this *can* be made only for a limited time, with certain other infra commentary ("archive" nodes which still keep extra), it's a complexity for a later discussion IMO.
- Should TX extra be per output?
- Should we mandate a small amount of TX extra to force uniformity?

## tevador | 2023-02-09T19:03:37+00:00
> tevador is against keeping extra

As my [last comment](https://github.com/monero-project/monero/issues/6668#issuecomment-1423000650) implied, I'm not *strictly* for removal. but I'm definitely against the current form.

If we keep tx_extra, it should be a uniformly sized field manadated by consensus (the length could be a function of the number of tx outputs, but definitely not arbitrary). 128 bytes is probably sufficient for most use cases, including a return address. It's approximately 4% of the size of a 2/2 Seraphis transaction. It could be prunable, so pruned nodes would only keep a 32-byte hash, saving 75% of space.

Additionally, I'm suggesting a relay rule that the tx_extra content must pass a quick statistical test that will fail for obviously unencrypted/plaintext messages.

> One extra point counterpoint about the scan time, any set of rules that will be devised over the kept tx_extra field will also add scan time to check the field against those rules. The complexity of those rules will determine the additional scan time, obviously. Not to mention the increased added global UX and DX complexity associated with tx_extra being a part of the protocol.

Wallets don't verify any consensus rules when scanning. If you meant IBD, the consensus rule would simply mandate the length of the field, which it a cheap rule to check.



## LocalMonero | 2023-02-09T19:30:21+00:00
> If we keep tx_extra, it should be a uniformly sized field manadated by consensus (the length could be a function of the number of tx outputs, but definitely not arbitrary). 128 bytes is probably sufficient for most use cases, including a return address. It's approximately 4% of the size of a 2/2 Seraphis transaction. It could be prunable, so pruned nodes would only keep a 32-byte hash, saving 75% of space.


@tevador Why maintain all this complexity and attack surface for the sake of enabling easy arbitrary data storage on the Monero blockchain? If arbitrary data is to be stored on the blockchain don't you think it's better if it's homogeneous with and indistinguishable from any and all other data on the blockchain by being virtually identical to other txs? Just because some people have uses for it that aren't malicious? So did legacy payment IDs. Devs have been advised against utilizing the tx_extra field for years at this point.

There were people who advocated for keeping legacy payment IDs due to backwards-compatibility and the lack of a need of a shared counter despite them being detrimental to privacy and bad for UX and DX. Despite all this it was removed because it's good for Monero. Now, we cater to arbitrary data injectors?

The framing of this question as "either steg or tx_extra" is a false dichotomy. _Junk outputs can and will be exploited with or without the tx_extra field_. It's not a "compromise" to keep the tx_extra field, it's a concession and a redefinition of Monero's design goals and principles.

> Additionally, I'm suggesting a relay rule that the tx_extra content must pass a quick statistical test that will fail for obviously unencrypted/plaintext messages.

And now we have this can of worms where we people are going to debate what sort of content should be allowed or not and this side will be accusing that side of censorship while that side will be accusing this side of being unreasonable and whatnot. If the arbitrary data is steganographed into the txs this issue completely disappears.

## tevador | 2023-02-10T09:40:25+00:00
@LocalMonero You are preaching to the choir.

There are good arguments both against and for keeping tx_extra. We can either keep repeating the arguments or try to find a solution that has a chance to get consensus and improve the current situation.

> If arbitrary data is to be stored on the blockchain don't you think it's better if it's homogeneous with and indistinguishable from any and all other data on the blockchain by being virtually identical to other txs?

A mandatory 128-byte encrypted field in all transactions won't hurt tx uniformity.

> It's not a "compromise" to keep the tx_extra field, it's a concession and a redefinition of Monero's design goals and principles.

The reality is that Monero has an unrestricted tx_extra field. Any compromise would be an improvement.

> And now we have this can of worms where we people are going to debate what sort of content should be allowed or not

That's nothing new. Monero already "censors" transactions for uniformity purposes ([see this comment](https://github.com/monero-project/monero/issues/6668#issuecomment-1422851389)).

> If the arbitrary data is steganographed into the txs this issue completely disappears

There is nothing that forces "steganographed" data to be encrypted. You can easily place ASCII text into output keys.

It seems that people will always try to sneak some extra data onto the chain ([see this comment](https://github.com/monero-project/monero/issues/6668#issuecomment-1418008913)), so keeping some limited field reserved for it might reduce the number of junk outputs that take up more resources to verify.

## dan-da | 2023-02-10T11:41:19+00:00
> A mandatory 128-byte encrypted field in all transactions won't hurt tx uniformity.

but it does add 128 (useless) bytes to (vast majority?) of regular "payment" tx that otherwise would not include any tx_extra data at all.  no?

My gut instinct is that less data (blockchain space) would be used overall by dropping tx_extra than by having a fixed length 128byte field.   show me wrong...?

Of course it may be difficult to reason about this because popularity/usage of future apps is unknowable.   Still, it seems we *could* do everything possible to encourage such apps to store data offchain in their own ledgers.  I understand that is not always easy... but then I come back to separation of concerns.

## spirobel | 2023-02-10T11:44:55+00:00
As @j-berman  pointed out [in this comment](https://github.com/monero-project/monero/issues/6668#issuecomment-1422568902) statistical tests for uniformity dont work. 
> I don't think statistical testing for uniformity will work. It sounds trivial to fool. Simply use an encoding scheme where you XOR plaintext with a static random pad, and then decode by doing the same.
> 
> Example plaintext payload:
> 
> 00000000 10101010
> 
> Static random pad:
> 
> 01101000 11101001
> 
> Encoded payload that will pass a uniformity check:
> 
> 01101000 01000011

@tevador 
>A mandatory 128-byte encrypted field in all transactions won't hurt tx uniformity.

The right place to do this would be in the wallets. The easiest way to achieve this goal is to increase the length of the paymentId to 128bytes. The code to generate transactions already creates dummy paymentIds for every transaction to increase uniformity (every transaction looks like a transaction to an integrated address)

>It seems that people will always try to sneak some extra data onto the chain (https://github.com/monero-project/monero/issues/6668#issuecomment-1418008913), so keeping some limited field reserved for it might reduce the number of junk outputs that take up more resources to verify.

but that only works if there is a reasonable expectation that this field wont be removed, altered or pruned in the future.

To avoid fatal mistakes, consensus and relay rules should only be added if they meet these requirements: 

1. **they should have a clear goal**
2. **they should achieve that goal**
3. **they should be as simple as possible**

If rules are added in the heat of the moment as a reaction to things without clearly considering this, people will trust the protocol and its continuity less and less.

Neither the tx_extra size limit on the relays nor the statistical uniformity checks pass these requirements.

It seemed like an adhoc reaction to ordinals that was well meant, but after more consideration can not achieve its objective.

## tevador | 2023-02-10T12:13:02+00:00
@dan-da @spirobel All of this has already been discussed above. We are just cycling through the same arguments over and over.

> The right place to do this would be in the wallets. The easiest way to achieve this goal is to increase the length of the paymentId to 128bytes

Seraphis has no payment ID, so it must be a separate field.

## vtnerd | 2023-02-10T12:47:41+00:00
Thanks @kayabaNerve I just read the entire discussion thread, as I should've from the beginning. My thinking is most similar to @tevador in the end. I will have some differing thoughts as this nears some kind of consensus, but I see my thoughts most reflected in @tevador .

> ~80 bytes of structured data which will be publicly accessible to anyone in the know, yet I'll probably encrypt on chain (with a static, public key) just to be polite there.

You deflected here, please provide what is actually being stored. You have stated that you are willing to record information on the Monero blockchain that links certain transactions to your DEX system, and you are willing to use the ZKP system to achieve your goals. In either case (`tx_extra` or "stenography"), chain analysis companies are able to identify these transactions and link them to this other chain, which (by your claims) isn't providing any meaningful privacy either.

The ideal (based on Monero community ethos) would be a system where the transaction wasn't guaranteed to be 100% linkable to your DEX. And I'm with @tevador in that I'm skeptical that the same thing cannot be achieved with only hashes.

## spirobel | 2023-02-10T12:59:19+00:00
@tevador 

>Seraphis has no payment ID, so it must be a separate field.

I was speaking about the current situation. The relay rule for the tx_extra size limit that you want to introduce was also for the current protocol, right?

@vtnerd 
>There's also the perspective that Monero should just have a fixed-size tx_extra which I think is the most fascinating argument, far more than removal.

I have a valid usecase for this kind of encrypted data field that even enhances  user privacy instead of diminishing it: 

I wrote a browser wallet for Monero that interacts with a website via calls to a standardized rest api endpoint at this respective website).
Please take a look at this demo video to see how it works (a transaction on the monero stagenet is made in the video):
https://youtu.be/4DLcsQ45zoE?t=132

This is how the wallet code and the demo backend (localhost:3006 in the demo video) that I wrote works:

1. the user wants to buy a product (like access to a chat group or a private RSS feed)
2. the browser wallet sends a tx proof to the website (at a standardized rest endpoint) directly after making the transaction. (so the backend does not even need to have access to the viewkeys of the merchant. Which enables the possibility of non custodial marketplace websites)
3. Afterwards the wallet can automatically relogin into the website via the spendproof of the txid. This means no emails, usernames or passwords are necessary anymore. Authentication is possible with just the txid and there is no need to ever copy addresses.

It would be great to recover all the information just from the wallet seed. So I would like to save the website url in which context the transaction was made.
This way if the user recovers from seed he wont risk disclosing himself with the wrong txid at the wrong website. (also all the login information neatly syncs between devices)

The Zcash encrypted memo field is 512 bytes by the way: https://zcash.readthedocs.io/en/latest/rtd_pages/memos.html they pad with zeros if it is not used. (before encryption)

## tevador | 2023-02-10T14:11:48+00:00
> I was speaking about the current situation. The relay rule for the tx_extra size limit that you want to introduce was also for the current protocol, right?

Tx_extra currently cannot be easily removed because it contains data required to recognize payments (DH public keys and payment IDs). Seraphis obsoletes payment IDs and moves the DH keys elsewhere, which could facilitate the removal of tx_extra. The tx_extra size limit proposal is a stopgap solution before Seraphis.

## spirobel | 2023-02-10T14:30:24+00:00
>Seraphis obsoletes payment IDs and moves the DH keys elsewhere, which could facilitate the removal of tx_extra. 

have read my above post and reviewed the use case that I presented? Do you think it is valid? 


## kayabaNerve | 2023-02-10T23:55:16+00:00
@vtnerd Sorry, I didn't mean to deflect. I thought that was the relevant information and didn't want to bloat the discussion with Serai-domain-specific commentary.

Specifically, the "instruction". The instruction specifies what to do with the received coins. For an output of 5 XMR into Serai, that may be a 32 byte Serai address to receive sriXMR, or it may be an instruction to swap to BTC and send to a BTC address.

Serai is actually out-of-scope for any privacy discussion because it's publishing its view keys and all TXs out are in plaintext on the Serai chain. My personal policy is its TXs should *appear* like any other, minus the additional data we throw in (either via TX extra or additional outputs), but the fact we publish view keys means it'll never actually be private.

This has implications as effective decoy poisioning which does justify discussions on complete membership proofs, yet those are out of scope to this conversation and I'd rather not bring it up again.

> The ideal (based on Monero community ethos) would be a system where the transaction wasn't guaranteed to be 100% linkable to your DEX.

I explicitly disagree here. I believe the point of decentralized technology is to be trustless. In order to be trustless, it must be verifiable. When 100 sriXMR come into existence, the only way to verify that is to see 100 XMR on chain. That *requires* revealing the Monero output.

... theoretically ideally? Sure. We'd be able to *verifiably* say we received 100 XMR without saying in which TX. Practically ideally? It's impossible.

> And I'm with @tevador in that I'm skeptical that the same thing cannot be achieved with only hashes.

The issue with hashes isn't any commentary on correctness/verifiability. It's about mandating I build an entire data pipeline, and spam preventative measures, to handle it. If Monero only gives me a hash, users cannot submit the data on-chain due to on-chain TXs requiring fees and these users presumably not having any SRI. Just XMR they sent to Serai to swap.

So they could submit to the validators who use a zero-fee transaction! I now have to make the validators directly publicly accessible, and directly handle connections from every Monero user to receive and validate their data. Then I need to duplicate that data to ensure it's verifiable over the entire amount of time its relevant (the shorter of Monero/Serai's existence).

That adds network architecture issues on my end and DoS concerns. While it'd be an improvement to the system, sure, if I could spare the bandwidth to build that entire pipeline, I can't justify it right now when I can trivially put the data on Monero instead. I am available to be attacked for taking the easy way out. I am also available to tell you most developers wanting to use TX extra will also take the easy way out. I'd also note this is only the easy way out because Serai's design has a secondary synchronized database which I'm simply not choosing to extend/use. For most designs, it's not the "easy way out". The entire point is using X for data storage (see Bitcoin ordinals not simply referring to IPFS URLs).

I'd also note this is again going in circles, which I share great frustration in. I responded here to ensure vtnerd, who has my utmost respect, is caught up. The only other comment I'd chime in on is @j-berman's about using a static pad to 'cheat' the uniformity check. That 'cheats' the uniformity check by encrypting your data to a uniform string of data only actually accessible to those with the decryption key. Congrats. That's the point :p

## Gonbatfire | 2023-02-11T16:24:53+00:00
> "either steg or tx_extra" is a false dichotomy. Junk outputs can and will be exploited with or without the tx_extra field. 

@LocalMonero Yes, but without tx extra, users will be **incentivized** to generate even more junk ouputs.

You can't prevent people from storing arbitrary data on Monero, so at least we should **incentivize** them to do it in the least harmful way.

## LocalMonero | 2023-02-11T18:20:40+00:00
@Gonbatfire quite the opposite, you are disincentivizing it by making it more costly. In addition, junk outputs are an exploit that also need to be fixed, but this is beyond the scope of this issue.

Fundamentally, Monero is a project with one mission: being digital cash. UNIX philosophy applies: do one thing and be good at it. Branching out into arbitrary data storage is not only beyond the scope of Monero but also hurts the efficiency of its purpose. 

If you want to have some sort of a Monero/Ethereum hybrid you're welcome to do what @fluffypony did with [Tari](https://www.tari.com/). DEXs are possible with or without tx_extra: in addition to [Haveno](https://haveno.exchange) existing, even @kayabaNerve admits that it's not a requirement for his DEX but merely a preference.

## Gonbatfire | 2023-02-11T18:35:42+00:00
>disincentivizing it by making it more costly

@LocalMonero  It will be more costly but it also will make data storage (that's gonna happen anyway) more harmful to users privacy, it's not worth it.

I agree Monero's focus is *private* digital cash, but by removing tx_extra I believe we are harming user privacy, since it's increasing the incentive to create MORE garbage outputs, garbage outputs are a problem right now, _until we find a way to fix that, let's not make it worse._

I'm not a fan of storing jpegs on scarce blockspace that has the potential to be the foundation for humanity, but we either learn to live with it or we start playing an unwinnable Whac-A-Mole game that will only result in negative side-effects for users.

I'm afraid this may become like the war on drugs, the war does more damage than the drugs themselves.



## LocalMonero | 2023-02-11T19:03:23+00:00
@Gonbatfire if it's more costly to store arbitrary data on the chain then *less of it will be stored*. If junk outputs are a threat to user privacy then just like any other threat to user privacy (like legacy/integrated payment IDs vs subaddresses) they need to be patched as soon as possible, even if that means breaking backwards compatibility. The "junk outputs harm privacy" argument is something that everyone can agree on and that it needs to be patched I also hope everyone can agree on.

The argument "given that we have a privacy exploit that, as a side effect, enables arbitrary data storage we should make arbitrary data storage easier" makes no sense to me.

The argument "while we have this privacy exploit that, as a side effect, enables arbitrary data storage let's enable another privacy attack vector that specializes on easy arbitrary data storage, otherwise a well-intentioned dev may exploit user privacy" makes no sense to me either. 

Well-intentioned devs developed applications around payment IDs since they don't require a shared counter unlike subaddresses, and I think we all agreed that this hole needs to be plugged. Even LocalMonero had to switch (subaddresses didn't exist back when LocalMonero started), and it was a costly switch, but we did it because it's best for user privacy, despite the fact that it was easier for us to just keep things as is.

As a side note, perhaps well-intentioned devs shouldn't be exploiting user privacy, especially given that it is not a necessity? So, if well-intentioned devs shouldn't be exploiting privacy holes, who does that leave us with but malicious actors and those who are ignorant (and can they really be that ignorant if they understand such advanced exploits)?

> but we either learn to live with it or we start playing an unwinnable Whac-A-Mole game that will only result in negative side-effects for users.

As @UkoeHB said, it's not an all-or-nothing game. It's incremental. Plug this hole, plug that hole, keep moving in the right direction. And keeping tx_extra post-Seraphis is a step in the wrong direction.

## kayabaNerve | 2023-02-12T14:51:58+00:00
> even @kayabaNerve admits that it's not a requirement for his DEX but merely a preference.

Without TX extra, I'm embedding data in outputs. It's a trivial solution solving the data availability problem without a month or two of my own architecting. While you can comment it's not a requirement, and we can discuss the theory of that, I've been clear my personal advocacy is for a practical solution which is optimal *to all parties*.

No matter what, I have a solution. Output encoding is only minimally more invasive on my end. To Monero, it's globally increasing scan time, poisoning decoys, and using about twice as much space. The only benefit is some argument about uniformity which doesn't legitimately stand when most TXs are 2-out.

Sure, that arguably makes me malicious, as I try to comment on the practicality of this. I'm also here arguing to never create that future. I'd also, personally, note that if I was forced between *damaging* steganography (a question of scale) and not having a widely used DEX, I'd question which is more damaging and pick whichever is *better*. That may mean withdrawing from Monero, or it may mean reducing Monero's effective privacy (which could be solved with other methods). Either way, as long I do my best to make Monero better overall, I don't believe I can be argued as malicious. Just misinformed/misevaluating at worst.

I'd also hope to be able to commit development resources to avoid this problem entirely in the future, yet I can't right now and won't make assumptions on that premise. I also don't assume the next person who walks in can nor that they have a design which even offers a path reachable with more resources. There are some designs which will fundamentally want to use Monero for its data. While I don't support anyone adding KBs, I don't personally mind bytes. Finally, I'll reiterate I haven't premised any of my arguments on my project directly. Just with the perspective I have thanks to my project.

> The argument "given that we have a privacy exploit that, as a side effect, enables arbitrary data storage we should make arbitrary data storage easier" makes no sense to me.

Monero will always have arbitrary data storage as it's a data protocol. While we attach the intent of currency to that data, that doesn't change it's a data protocol. The fact Monero communicates arbitrary data is a natural side effect which can never be stopped. The only question is where we go from there.

## LocalMonero | 2023-02-12T16:51:10+00:00
> Without TX extra, I'm embedding data in outputs.

For a certain period of time you are. And when that exploit's patched you'll have to find a new one that's probably even less cost-efficient, which, I assume, you will also report to the community (or, hopefully, you'll figure out a design that doesn't require you to store anything on the chain). It's a process.

> I've been clear my personal advocacy is for a practical solution which is optimal to all parties.

Monero should not offer practical solutions for arbitrary data injectors. There are plenty of other projects that do. 

> No matter what, I have a solution. Output encoding is only minimally more invasive on my end. To Monero, it's globally increasing scan time, poisoning decoys, and using about twice as much space. 

For how many transactions? 0.01% out of the whole network? If someone who actually wants to harm Monero's privacy, scan time, and poison decoys they will attempt to make these txs a large portion of the overall network (which will certainly trigger an urgent response from the dev community), so *your* usage of it doesn't seem to be that big of a problem prior to this being patched. I'm much more concerned with actual malicious actors exploiting this.

> The only benefit is some argument about uniformity which doesn't legitimately stand when most TXs are 2-out.

And tx_extra with arbitrary data doesn't hurt uniformity even more? And if it's encrypted or otherwise uniform in nature and every transaction will have to have it be fully filled, that doesn't hurt space requirements? And that doesn't make transaction costs higher for all users globally, regardless of whether they are utilizing tx_extra or not, making *not* utilizing tx_extra be unproductive for the fee they're paying?

> Sure, that arguably makes me malicious

I didn't say *you* were malicious. I was talking about the fact that the hostile exploiters of the junk outputs are the actual problem, as well-intentioned devs will strive to avoid harming user privacy. This is why the junk outputs are beyond the scope of this discussion and are a separate issue.

>   I'm also here arguing to never create that future. 

"Hey man, listen, I got these boxes of my stuff that I want to store in your bank. I know your bank doesn't allow random people to store boxes of stuff here but listen man if you don't let me in through the door I'll break through your window but I don't want to create that future so how about you designate a key card for me, alright? It's for your own good."

Sounds like the solution is putting bars on the window.

> I'd also, personally, note that if I was forced between damaging steganography (a question of scale) and not having a widely used DEX, I'd question which is more damaging and pick whichever is better.

Thank goodness that in reality having a widely-used DEX is not predicated on that 😅

> I'd also hope to be able to commit development resources to avoid this problem entirely in the future, yet I can't right now and won't make assumptions on that premise. I also don't assume the next person who walks in can nor that they have a design which even offers a path reachable with more resources. There are some designs which will fundamentally want to use Monero for its data. While I don't support anyone adding KBs, I don't personally mind bytes. Finally, I'll reiterate I haven't premised any of my arguments on my project directly. Just with the perspective I have thanks to my project.

If your or the next person's design necessarily requires arbitrary data injection into the Monero chain to work they are welcome to use another project or deal with the fact that even if they find a way to inject data it's going to be as  inefficient as possible.

> Monero will always have arbitrary data storage as it's a data protocol. While we attach the intent of currency to that data, that doesn't change it's a data protocol. The fact Monero communicates arbitrary data is a natural side effect which can never be stopped. The only question is where we go from there.

It's true that someone can take the "Date of Birth" field on some website and use it to encode a certain amount of bytes, and perhaps through encoding this way over a long enough chain of accounts encode the entire `Bee movie` into that website's database. Does this mean that this website should cater to anyone who wants to store movies on it?

Data constraints work. Yes, they don't (and maybe can't) work 100%, but defining the transaction structure as strictly as possible will make arbitrary data storage as costly and inefficient as possible, disincentivizing  arbitrary data storage to the greatest possible extent which in turn makes the Monero chain to the greatest possible extent void of arbitrary data and optimized for transactions. In addition, this will also ensure maximum uniformity and by extension privacy and fungibility. The opposite is true for making arbitrary data storage easier: Monero will be worse at what it should be best.

I remember similar arguments being made in favor of giving in to ASICs, which were "inevitable" until @SChernykh and @hyc brought us RandomX. Monero stuck to its core and didn't give in, and thank goodness for that.

## TheCodeingPadawan | 2023-02-12T18:13:35+00:00
TL;DR: 
In summary, A developer utilising Monero payment should implement accounting and metadata on their own systems to track what they need to track. Monero should always just be the private and fungible medium of exchange.

Wall of Text version:
Arbitrary data should be stored on the side. Any logic or arbitrary data should always be separate from the cash itself. You can consume and dispense Monero as required within a private platform, but those inputs and outputs should always just remain as fungible Monero. 

The only way to fix this would be by adding fixed arbitrary data bytes to each transaction, and force encryption to keep everything on the public chain indistinguishably fungible and private between the two transacting parties. But this will consume valuable space on every transaction, when practically all transactions do not use the TX extra field. Those that do would also likely consume little of the dedicated space, as it would need buffer room to give it more utility.

It just seems like wasting blockchain space for the fraction of a fraction of a percent that have a use case, for negative to little benefit to the overall project.

## kayabaNerve | 2023-02-12T18:31:39+00:00
> For now you are

I'm not.

> And tx_extra with arbitrary data doesn't hurt uniformity even more?

It explicitly depends on the over-arching scheme. I wouldn't immediately say yes.

> And if it's encrypted or otherwise uniform in nature and every transaction will have to have it be fully filled, that doesn't hurt space requirements? And that doesn't make transaction costs higher for all users globally, regardless of whether they are utilizing tx_extra or not, making not utilizing tx_extra be unproductive for the fee they're paying?

Encryption would not hurt space requirements. All TXs having a default sized blob is a distinct discussion I'm personally not in favor of.

> TL;DR:

This fails to be a proper TL;DR of the many arguments at stake. I do not feel a need to continue running down these nits. I'll withdraw from this discussion until there's a legitimately new argument, or a conversation of sufficient weight begins. Right now, this is just back and forth bickering which is productive to none of us.

## LocalMonero | 2023-02-12T18:38:58+00:00
> I'm not.

The "now" I meant was in the post-tx_extra-removal time, I was answering in the context of "without the tx_extra I will", as I quoted.

> Encryption would not hurt space requirements. All TXs having a default sized blob is a distinct discussion I'm personally not in favor of.

If the tx_extra field isn't uniform then it's a massive privacy/fungibility issue. If it is then it would have to be fixed length and encrypted, permanently increasing space requirements for txs globally, forcing people to store data and pay fees whether they're utilizing the field or not.

## hbs | 2023-03-17T07:54:04+00:00
The recent debate on channel MRL got me thinking about that whole tx_extra and more recently m0rdinals issue. Please excuse my potentially naive ideas, I've only recently started diving into the code base so some of my ideas may be totally stupid, both from a protocol or from an implementation perspective, but hey, this is how you learn, so don't hesitate to point out anything in my reasoning which just doesn't work. So far I've leant towards the removal of tx_extra as a solution but the more I dig the more my conviction crumbles.

If I understand correctly, the tx_extra field can contain multiple chunks which are prefixed with a byte indicating their type, 0x01 for public keys, 0x04 for additional pubkeys and 0x00 for padding. My understanding is that this padding type is the one allowing arbitrary data to be included in tx_extra. The first good thing is that we can then easily identify tx_extra fields with arbitrary data since they will be the ones containing 0x00 tags.

The issue with tx_extra uses (with 0x00 tags I presume) is that they make transactions stand out since it somehow breaks uniformity (few transactions make use of that tag). My understanding of this is that this somehow taints the outputs of those transactions which may help chainanalysis actors to gain a clearer image of the tx graph. This is still something I need to get my head around though, as I may miss some impacts of that lack of uniformity.

One alternative to using tx_extra, though more costly, is to use steganography to create dummy outputs which will contain  roughly 30 bytes of arbitrary data each. This approach may impact the chain by creating more outputs than what "normal" use of the chain would do.

Whether via tx_extra or via steganography, storing arbitrary data has at least two consequences. The first one is that it increases the amount of data stored in the chain, hence increasing the cost of operating nodes. The second one is that it taints outputs and may ease the work of chainanalysis processes which attempt to identify true spends.

The tainting of outputs seems to me the most impactful for normal users since without them knowing it it will reduce their privacy because some outputs chosen as decoys might be useless and their rings might in reality provide the security of far less than the current 16 membership.

While using the Monero chain for storing arbitrary data is far from the original goal of true digital cash, as some have pointed out, given the Monero transaction protocol is a data protocol it seems rather intractable to ensure that this type of usage does not occur. But what if the use of the tx_extra field to store arbitrary data was assorted of an explicit reduction of privacy? What if transactions which include arbitrary data were limited to inputs with no mixins, hence exposing the true spends? The use of tx_extra for storing arbitrary data would therefore be done knowing the privacy would be reduced. This in turn would allow to mark some outputs as effectively spent and they would not be accepted as decoys anymore. This would induce a Monero chain with really two sets of outputs, those that are known to be spent and the others. What I am struggling to grasp is if it is really a pitfall to have those two sets of outputs when it comes to privacy of the "normal" users of the chain.

I have not a good enough understanding of the actual transaction protocol to determine if it is possible to have a "ring" size of 1, but I guess the protocol could be adapted to allow the spending of outputs this way.

If solution B3.x is implemented, the net effect on the stored size would be potentially negative since removing decoys will reduce the size of the inputs spent in those "doxing" transactions.

For uses of the tx_extra field in some applications (exchanges?), I don't really see an issue in terms of privacy since those applications could introduce an intermediary transaction to first consolidate whatever outputs into a single one before tainting this single output in a txn with tx_extra set.

Again, sorry if this doesn't make any sense.


## martin-braun | 2023-03-20T04:44:01+00:00
[Mental Outlaw has mentioned this issue.](https://www.youtube.com/watch?v=wj4poJOInDo)

I really hope there will be progress on this issue, because NFTs and Monero don't belong together imho. NFTs are the exact opposite of privacy and the `tx_extra` field is mis-used for that purpose, similarly to Bitcoin's Ordinal Inscriptions.

## rwjack | 2023-03-20T08:55:41+00:00
As someone mentioned above, to me it makes sense that monero (cash) should be like cash and have it used exclusively for transactions. If a user needs to store additional metadata related to the transactions, then that should be done within another piece of software.

From my shallow understanding, setting a fixed size for tx_extra and disincentivizing users to use it, is the way to go. On the other hand, this may be exactly the direction "someone not friendly to monero", would want it to go in.

So the main question would be, what would be the best possible use case for keeping tx_extra, in the xmr vs fiat duel?

## povertyhacked | 2023-03-20T10:16:25+00:00
I am going to keep this very simple. I am not a miner and I do not have a node but I care deeply about privacy and by extension of that, Monero. Having said that, I've never gotten involved in Monero matters because I do not know code and there is a competent team, and community, in place - I've just stuck to advocating for privacy through law.

Having said all of that, the tx_extra field needs to be removed. Monero is privacy and any other considerations do not matter. People will come to Monero and inscribe NFTs because the R:R is great. If that means, even for one person, that one of the 16 decoy sigs is distinguishable, that's a big problem. But what if it happens for me? Or for you?

The 3 letter agencies will jump on the bandwagon when they realise the size of attack vector at play here (I don't even want to put this in writing on the Internet but I'd be kidding myself to not acknowledge that they are clever and will get there anyway, if they haven't already).Just look at the block bloat size BTC has experienced... couple that with a significantly cheaper price, and it becomes a no-brainer for them to try, or another entity to try and then collect the bounty/bounties. 

I've read through a fair few comments that note that tx_extra is needed for other things like merge mining - if this is true, merge mining isnt the focus of Monero; privacy is. The only fair comment(s) I've seen against removing tx_extra have been that people will just find another way to store data. Those considerations are fair and probably correct but if that happens, if it opens up an attack vector, then work needs to be done then again.*

Simply put, Monero is meant to be very simple (aside from the processes used to achieve anonymity/privacy). Privacy is the name of the game and other add-on's are cool but not at the expense of losing privacy. Lets not become ZEC.





*For the avoidance of doubt, I am not attacking anyone's position - I am simply advocating for the most privacy possible.

## UkoeHB | 2023-03-20T16:12:44+00:00
> I really hope there will be progress on this issue, because NFTs and Monero don't belong together imho. NFTs are the exact opposite of privacy and the tx_extra field is mis-used for that purpose, similarly to Bitcoin's Ordinal Inscriptions. @martin-braun 

Monero is a system for recording and transferring ownership of money. It is not appropriate for the core team to adjudicate the _reasons_ that people transfer money, whether they be NFTs or anything else. The main reason for considering consensus rule changes around the `tx_extra` is that its current incarnation has very weak privacy under generally-supported-use.

The current leading proposal that keeps the field specifies an optional fixed-size field (which would be encrypted by default). That proposal reduces the privacy cost of default use to the smallest possible non-zero level: 'is a field present or not?' (that's a lower privacy impact than all other sources of distinguishability in txs: tx input/output counts, ring member selection, tx fees, potential for steganography). Decrying 1 bit of distinguishability as a privacy disaster, as some have done, is pure hyperbole.

The other leading proposal, which is to remove the field completely, has two weaknesses:
1. It is not a conservative change. The _current_ protocol has a tx extra, so keeping the field in some form is more conservative than removing it. In some sense, the current protocol is the most canonical representation of what Monero 'should' be.
2. It encourages a higher rate of future hard forks. Removing the field is a clear signal that future features must go through core team assessment and then be proposed for a hard fork. In my view, it sets the expectation that future features _will_ be assessed and proposed for hard fork, which basically cements perpetual hard forking into the ecosystem. As we have seen with comments like @martin-braun's, people are more than willing to advocate for censorship via hard fork. I predict that over time we will just see more and more calls for censorship via hard fork, and for much less benign reasons than opposing NFTs. It is **not** reasonable to expect that future incarnations of the core team will be as opposed to censorship, or to weakening of other essential properties of Monero (e.g. immutability/permanence - we have already seen some people in favor of 'pruning' old block contents), as the current core team. Next to critical security vulnerabilities, hard forking is the greatest long-term threat to Monero (bitcoin maxis understand this well).


## trymeouteh | 2023-03-21T05:15:04+00:00
My opinion as a XMR user is to remove tx_extra. If not tx_extra should have a size limit and perhaps additional fees. The NFTs on Monero chain is a privacy concern and to also keep the chain from storing bloat and nonsense.

## Burnsedia | 2023-03-22T17:39:18+00:00
@trymeouteh  we could use fixed compression with a default message/data in the tx_extra, so all blocks have the same size, and all wallets in the ring signature are the same. there are non-NFT uses for having the ability to store data in any blockchain, but if tx_extra is kept, we need to anonymize it as much as possible. 

## hyc | 2023-03-22T18:08:32+00:00
You'd have to use a fairly primitive compressor, like Huffman Squeeze. LZW-based compressors don't just fail on uncompressible data, they make it larger. The usual approach taken by standard compression programs is to pass the original data through unmodified when this happens, but we have to guarantee that the unmodified data is never passed through.

## Burnsedia | 2023-03-22T19:37:35+00:00
Ok, my bad. Maybe instead of on-chain storage, use an RPC with something like Gunjs to store data. Use the transition information from the monero rpc to generate the seed data in gunjs and key-value pair. 

## kayabaNerve | 2023-03-23T03:02:02+00:00
This does not open the door for "Tracking Organizations" to flood Monero to increase traceability. That is a distinctly possible issue due to the decoy model.

I'd encourage community members without a clear understanding of the actual technicalities to withhold their commentary.

## Burnsedia | 2023-03-23T06:58:21+00:00
I am just throwing out ideas; I am new to blockchain development. If they are dumb, please tell me why. 

## kayabaNerve | 2023-03-23T20:20:53+00:00
I was responding to dylanthall, who treated the transaction flooding attack present under the decoy model as being premised on TX extra when it isn't. Any bad actor can flood Monero with outputs in order to achieve a large amount of decoys, and Monero has prior experienced such attacks. They did not rely on TX extra. Removing TX extra would actually increase the amount of low quality decoys *by non-malicious actors* under practical use cases.

If you, or anyone else, wants to learn more, I'd encourage reading through the entire issue and potentially asking around the IRC channels.

For your (Burnsedia) commentary specifically, I'd point out your idea mentions compression yet doesn't actually use compression AFAICT. It suggests a fixed-size TX extra, which isn't achievable with compression, yet with a commitment or with padding.

> if tx_extra is kept, we need to anonymize it as much as possible.

Is a generic comment prior stated many times throughout this very long issue, without a new contribution. While I don't want to be too harsh on community members trying to contribute, I'm personally frustrated by *some* comments making this very long issue longer (which is why I haven't replied to all of them, as now I'm making the issue longer. I only do so here per request).

## LocalMonero | 2023-03-23T20:37:37+00:00
>  Removing TX extra would actually increase the amount of low quality decoys by non-malicious actors under practical use cases.

@kayabaNerve  is it my correct understanding that you can steg into CLSAG with essentially no network privacy implications, as CLSAG steg only reveals the decoys to the receiver instead of any observer like with output steg?

## kayabaNerve | 2023-03-24T01:24:05+00:00
It depends on what exactly you do. If you write raw data in there, it'll still damage network privacy. It also reveals decoys to the receiver, which I personally don't consider acceptable.

Output steganography would also only reveal its data to the intended sender if encrypted, and appear normal to everyone else, so

> instead of any observer like with output steg

is incorrect.

## LocalMonero | 2023-03-24T01:34:48+00:00
Right, the question was operating under the assumption of stegging encrypted data in CLSAG vs encrypted data in outputs and the impacts on decoys. Meaning that assuming you're stegging encrypted data into CLSAG you're affecting network privacy to a lesser extent than if you stegged into outputs.

Though, in the case of Serai specifically it doesn't really matter as you're revealing the encryption keys anyway, from what I understand.

## kayabaNerve | 2023-03-24T05:17:55+00:00
Encrypted data in CLSAG/outputs is indistinguishable to outside observers. In CLSAG, the receiver learn the decoys. In outputs, there's no privacy loss of the sender, though there are more outputs 'contributing' to the decoy set. The outputs only damage network privacy if they're known to be meaningless (such as if the sender publishes their recipient). There are also network privacy implication if the receiver of a message in CLSAG publishes the message, as it harms the tree Monero transactions form.

## kkarhan | 2023-03-31T14:31:35+00:00
TLDR:
**OPINION: tx_extra should be removed completely.**

---


Reasoning:

As someone interested in Monero and considering to mine it, the tx_extra field is a legal liability amidst the amount of [documented abuse of said function](https://github.com/monero-project/monero/issues/6668#issuecomment-670978771).

Notwithstanding the technological disadvantages like the fact that [Ordinals as a means to do NFTs will baloon the block- and chainsize and harm legitimate users wanting to use Monero as actual online payment](https://youtu.be/wj4poJOInDo?t=445) this can and will be used as a nail in the coffin for payment providers to reject it's use, cuz the last thing any bona-fide business [i.e. in Germany] wants to be associated with is "distribution of CSAM" [which is a felony](https://www.gesetze-im-internet.de/stgb/__184b.html).

This is why [Ahmia only releases hashes of the onion sites they blacklist which are almost exclusively CSAM](https://ahmia.fi/blacklist/) so other search engines can do the same or at the very least compare their index and decide what they want to blacklist.



**I think that Monero's prime goal was to be an actually fungible currency** and a better option than PayPal.

Considering that @fluffypony [went out of the project based off solely on random accusations](https://twitter.com/fluffypony/status/1638396328161030144) was a clear sign that [like OpenBSD](https://en.wikipedia.org/wiki/OpenBSD#Security), Monero would not compromise it's security at all and would rather go out of it's way to shed staff/personnel/contributors/maintainers and features than lessen it's security.


**As a matter of fact [tx_extra data (or the absense of it) not only can but will likely be weaponized against users](https://youtu.be/wj4poJOInDo?t=616) to the point that it'll harm everyone's privacy.**


So as much as I hate it, removing it seems to be the only feasible option to do so.
_After all, Monero isn't intended or designed to be used as a [Messenger](https://en.wikipedia.org/wiki/Bitmessage) or something else but a payment & transaction system._

If anyone wanted to communicate something like "This Transaction is a Payment to B for Purchase X from Customer A" that's not part of the payment system and not only can be handled sufficiently by other communications [i.e. Accounting System] but in many places (again thanks to German Bureaucracy) [must be handled by a seperate system](https://de.wikipedia.org/wiki/Technische_Sicherheitseinrichtung) [as per law](https://de.wikipedia.org/wiki/Kassensicherungsverordnung), thus tx_extra already falls flat in terms of bona-fide use-cases.

At the end of the day it would be far easier and simpler to just copy & paste the txid and block_id for the completed transaction as proof of payment and sent it to the seller by eMail or Messenger or whatever.


After all, Monero can be otherwise operated completely legal and compliant with accounting regulations using the ViewKey. It's not perfect [and it should also show outgoing transactions]( #1070 ) and has [severe security and privacy drawbacks](#5145 ) but that's outside the scope of this, since this feature isn't bad per-se and has valid use cases, is opt-in per wallet.

Unlike choosing to use a "lite wallet", the use or rather abuse tx_extra isn't something [the reciever can actually deny or prevent](https://youtu.be/YQ_xWvX1n9g?t=4987), copying the whole [TornadoCash prank issues](https://youtu.be/x7gaqhF-wrQ?t=289) and not only incentivize [bloatware like MetaMask that should not exist to begin with](https://youtu.be/YQ_xWvX1n9g?t=4804) but will inevitably get us [NFT-Malware](https://youtu.be/YQ_xWvX1n9g?t=4968) that [exists in the wild already](https://youtu.be/YQ_xWvX1n9g?t=5377)...


I mean there's a reason why there [ain't Smart Contracts on Monero](#7864):
Because for any "Smart Contract" to work would inevitably need privacy to be weakened and expose at least the wallets and amounts to be interacted with, reducing the privacy for everyone else when [Multisig can basically do the same as a private smart contract](https://monerodocs.org/multisignature/) and is pretty [straight-forward](https://web.getmonero.org/resources/user-guides/multisig-messaging-system.html).


For those that want to use NFTs [which I don't but that doesn't matter!] there are better and more efficient blockchains like [Solana](https://en.wikipedia.org/wiki/Solana_(blockchain_platform)) to handle those.


Similar to the [clear stance against ASICs by Monero](https://medium.com/luxor/monero-randomx-asic-resistance-abb96b50bdaf) there should also be a clear stance against ["Ordinals" / NFTs that are exploiting tx_extra](https://github.com/mooonero/mordinals#technical-details) and attacks that tried to distinguish transactions by reducing the ringsize to 0 or allowing for [different and/or distinguishable ringsizes, thus making transactions stand out](#8178).

**_After all, if people wanted "scarcity" on a privacy blockchain, they could just use [Wownero](https://wownero.org/) or opt-in privacy chains like Dash or Zcash instead._**


**I'll await the decision re: this issue before considering to contribute anything further...**




---

**Addendum:**

_If someone wants to self-d0x their income in Monero, then that's their choice by publishing the ViewingKey...
**But Ordinals like NFTs threaten the fungibility of Monero and the privacy of everyone else, thus are non-consensual anti-anonymity exploits that should be regarded with the same severity as past issues and thus fixed accordingly.**_

**We ain't on Ringsize 3 anymore for very good reasons!**

## UkoeHB | 2023-03-31T15:33:42+00:00
@kkarhan The problem you describe **can never be resolved by consensus rules**. You can **always** encode at least some data in a transaction using user-defined data fields in ways that **cannot** be prevented or 'forcibly privatized' using consensus rules.

## bt4599 | 2023-04-01T08:57:01+00:00
@UkoeHB You may be confusing user submitted data with arbitrary data. Fields with a defined purpose can potentially have such a purpose enforced at consensus level since the range of allowed values can be smaller than the range of numerically possible values. 
For example, placing arbitrary data in the decoys could be made much more difficult by requiring - and checking at consensus level - that the decoys really are decoys, e.g. that they actually exist on chain, that there are no duplicates in the selected decoys and so on.
Even if some data can still be encoded, the amount can be reduced.

## kayabaNerve | 2023-04-01T09:22:22+00:00
> and checking at consensus level - that the decoys really are decoys, e.g. that they actually exist on chain, that there are no duplicates in the selected decoys and so on.

These properties are already checked. Monero would have an infinite mint bug if we didn't. 

Please don't make me tap the sign: https://github.com/monero-project/monero/issues/6668#issuecomment-1480536557

## bt4599 | 2023-04-01T15:39:27+00:00
@kayabaNerve Which is why i said "for example". It was just one of the easiest ways to illustrate the difference between user submitted and arbitrary data. The "amount that could be reduced" was not referring to the specific example.

## UkoeHB | 2023-04-01T20:07:24+00:00
> Fields with a defined purpose can potentially have such a purpose enforced at consensus level since the range of allowed values can be smaller than the range of numerically possible values.

This doesn't solve anything, because there are still bits available for encoding data even if you constrain everything as much as possible. In practice, a large amount of tx output data is semantically unenforcable.

> You may be confusing user submitted data with arbitrary data.

This is just an arbitrary distinction with no functional value in terms of security analysis. All unchecked/uncheckable data is arbitrary data. Even parts of a tx that are highly-checked, like signatures, can be brute-forced to encode information.

## Rucknium | 2023-04-14T13:35:38+00:00
I analyzed the privacy impact of Mordinal "NFTs" that store data in tx_extra: https://www.reddit.com/r/Monero/comments/12kv5m0/empirical_privacy_impact_of_mordinals_monero_nfts/

## kkarhan | 2023-04-18T05:43:54+00:00
> I analyzed the privacy impact of Mordinal "NFTs" that store data in tx_extra: https://www.reddit.com/r/Monero/comments/12kv5m0/empirical_privacy_impact_of_mordinals_monero_nfts/

Thanks @Rucknium for that [deep dive analysis.](https://github.com/Rucknium/misc-research/tree/main/Monero-Effective-Ring-Size)

![Percentage of Monero Transactions that are Coinbases and/or Mordinals](https://user-images.githubusercontent.com/30401796/232680572-c3fe2bc1-f7af-4697-805c-0fc26ccb10f9.png)
![Average Empirical Ringsize per Monero Transaction](https://user-images.githubusercontent.com/30401796/232680535-f9bfd85d-2479-4ba4-9ea5-cb29cfc8bb39.png)
![Effective Ringsize for the unluckiest 5% of Monero Rings](https://user-images.githubusercontent.com/30401796/232680506-63448a96-8cee-48e9-9c16-03d8b8948398.png)

This CONFIRMS my fears that this not only can but actually decreases the security of Monero:
> "[...] attacks that tried to distinguish transactions by reducing the ringsize to 0 or allowing for [different and/or distinguishable ringsizes, thus making transactions stand out](https://github.com/monero-project/monero/issues/6668#8178). [...]"
-  https://github.com/monero-project/monero/issues/6668#issuecomment-1492016289

**I don't want to sound alarmist, but this could be the state-sponsored attacks by Chainalysis et. al. who got awarded $625k from the IRS**
_After all, they don't need to break the chain entirely from one day to the other, but slowly downgrade it's privacy to be useless._

The data suggests that this is partially successful to the point that it undoes the ringsize upgrade for quite a significant chunk of transactions.


Which brings me to the next point:

What we've not considered is the abuseability by regulators!
Imagine if - due to it's widespread use - Regulators and Exchanges give up on discriminating and trying to ban Monero but instead make up arbitrary bs rules like requiring individuals and businesses i.e. to add their Tax-ID to every tx_extra field when they sent something...
Kinda like the ham-fisted approach to cannabis relegalization in Germany being landmined with regulatory bs compared to tobacco and alcohol.

Cuz that would be another "well-meant" but actually cyberfacist & dysthopian law and not be used to enforce taxation of i.e. billionare wankers but go after small coin investors with - compared to Banksters - basically nonexistant wealth.

[Okay, legit businesses would likely have to provide bulk access to their accounting systems and accounts when audited but that would not impact the privacy and security of Monero as a Payment System in General]...


**My opinion _still_ stands:**
**tx_extra should be deprecated as it's a security issue - period!**

## Burnsedia | 2023-04-27T01:40:27+00:00
OK, my bad

On Wed, Mar 22, 2023 at 11:02 PM Luke Parker ***@***.***>
wrote:

> This does not open the door for "Tracking Organizations" to flood Monero
> to increase traceability. That is a distinctly possible issue due to the
> decoy model.
>
> I'd encourage community members without a clear understanding of the
> actual technicalities to withhold their commentary.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/6668#issuecomment-1480536557>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AH4ZR52EMVP7SJ66L3R2KZDW5O4LNANCNFSM4ODJ5GQQ>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


# Action History
- Created by: tevador | 2020-06-20T09:37:55+00:00
