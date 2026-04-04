---
title: Monero Research Lab Meeting - Wed 08 January 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1138
author: Rucknium
assignees: []
labels: []
created_at: '2025-01-07T20:42:13+00:00'
updated_at: '2025-01-21T19:53:14+00:00'
type: issue
status: closed
closed_at: '2025-01-21T19:53:14+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography](https://github.com/monero-project/research-lab/issues/131)

4. Any other business

5. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1134 

# Discussion History
## Rucknium | 2025-01-09T17:05:15+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1138     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< c​haser:monero.social >__ hello     

> __< v​tnerd:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< a​rticmine:monero.social >__ Hi     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< s​yntheticbird:monero.social >__ Hello     

> __< r​ucknium:monero.social >__ me: Finishing up milestone 3 of my OSPEAD CCS.     

> __< r​ucknium:monero.social >__ jeffro256 in case you need a meeting time reminder.     

> __< v​tnerd:monero.social >__ working on typing another ccs, I’ll likely finally do another one soon     

> __< r​ucknium:monero.social >__ 3) Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography https://github.com/monero-project/research-lab/issues/131     

> __< r​ucknium:monero.social >__ I think jeffro256 wanted to discuss something about Carrot and its extra bits when self-sending.     

> __< s​yntheticbird:monero.social >__ Last time Jeffro talked about https://github.com/monero-project/research-lab/issues/106, as being a quick solution to get post quantum security for monero. However, i still agree with kayabanerve, i hate this UX     

> __< j​berman:monero.social >__ my update: continuing integrating FCMP++ prove     

> __< s​yntheticbird:monero.social >__ I think compared to december meeting, we stoped talking about economic viability/amount security with a QC. Afaik FCMP++ doesn't prevent a QC to double spend, iiuc the switch commitment revision for Carrot doesn't address this or help at addressing this?     

> __< r​ucknium:monero.social >__ I thought that the Carrot switch commitments were proposed to help prevent quantum counterfeiting, in combination with more steps that would have to be taken.     

> __< rbrunner >__ I don't remember anything so specific about these things, thus I am no help there ...     

> __< r​ucknium:monero.social >__ With the proposal in MRL issue 106, all transactions would have to have off-chain communication, right? It could not be opt-in like Carrot, correct?     

> __< c​haser:monero.social >__ FCMP++/Carrot *alone* can't prevent quantum counterfeiting. I think Jeffro talked about modifying Carrot to prepare the future introduction of switch commitments.     

> __< s​yntheticbird:monero.social >__ Chaser Rucknium, yes, switch commitment is here to prepare a migration to a pq resistance for amount. But I don't remember it addressing the double spend issue, since a QC can forge two outputs with the same key image.     

> __< v​tnerd:monero.social >__ why the sudden concern about QC? the hype over recent Google claims? Haven’t they always over-stated QC capabilities (scammers)? Anyway switch commitments don’t really help with counterfeiting unfortunately. They simply allow us to safely “reveal” amounts as we transition to a new system     

> __< s​yntheticbird:monero.social >__ Yes.     

> __< s​yntheticbird:monero.social >__ Anticipating worst case scenario. Kayabanerve and other share these concerns. We also have to assume governments might have better advancements in quantum computing than private companies.     

> __< r​ucknium:monero.social >__ vtnerd: From what I've observed, you can almost draw a separating line between those who are concerned about QC and those who are not, based on age.     

> __< rbrunner >__ Based on age? Indeed?     

> __< r​ucknium:monero.social >__ This is my observation as a social scientists hahaha     

> __< r​ucknium:monero.social >__ Age is strongly correlated with experience, of course     

> __< rbrunner >__ So old people must mostly not fear those QC, because I am firmly in that camp :)     

> __< j​effro256:monero.social >__ So sorry I'm late....     

> __< rbrunner >__ But well, what was described seemed like a pretty cheap thing to have, in comparison, which would help just in case they do arrive     

> __< s​yntheticbird:monero.social >__ To copy what i said in my mrl issue. It's not a matter of "will we be ready for QC era" but also "we should  be ready N years prior to avoid people being in trouble in face of law retroactively, as the current blockchain will be transparent"     

> __< s​yntheticbird:monero.social >__ In most countries the statute of limitations is of minimum 10 years     

> __< c​haser:monero.social >__ vtnerd: I think Kayaba's recommendation in their stepping-back note is what created this momentum for the QC theme. personally, I was always concerned, and I think any opportunity is the best yet to start tackling the potential threat.     

> __< s​yntheticbird:monero.social >__ so we should be PQ 10 years before     

> __< v​tnerd:monero.social >__ and to clarify on my previous comment, old amounts are “statistical bound” (via hash) to a value, so you cannot create money in old transactions, assume hashes are not broken by QC. IIRC, you could theoretically inflate _just before_ the turnstile/reveal was made mandatory     

> __< v​tnerd:monero.social >__ so presumably this is why some people dont like switch commitments, a secret ECDLP solver is still wrecking havoc     

> __< a​rticmine:monero.social >__ I don't see a reason for panic, but given the likely timelines on our, realistically ~ 5 years minimum for a QC main chain HF starting the research and work now is just prudent.     

> __< a​rticmine:monero.social >__ Our end     

> __< j​effro256:monero.social >__ Carrot has a 16 byte field per enote called the anchor which is required for normal transfers, but is unused for change outputs and other selfsends (when using the new Carrot key hierarchy). We can use this field to send encrypted transaction memos for free. The question is whether or not we should expose this feature to users to put arbitrary data in there, since a quantum comput<clipped messag     

> __< j​effro256:monero.social >__ er may come along and decrypt it at some point     

> __< v​tnerd:monero.social >__ this is insane, we stopped seraphis for fcmp++ to suddenly just drop all the work?     

> __< s​yntheticbird:monero.social >__ ? we're not planning on dropping fcmp++     

> __< v​tnerd:monero.social >__ ok, I guess just some people dropped out (temporarily), not the entire thing stopping. Misread the room a bit     

> __< v​tnerd:monero.social >__ just skimmed through the Ruffing paper on QC, my understanding seems correct if others could follow it     

> __< c​haser:monero.social >__ FCMP++ is still full steam ahead, from what I gather.     

> __< v​tnerd:monero.social >__ *on switch commitments     

> __< r​ucknium:monero.social >__ AFAIK, the plan is still to activate FCMP, hopefully this year. kayabaNerve suggested that after its activation, non-QC-resistant cryptography should not be on the Monero research agenda. Instead, QC-resistant cryptography should be researched.     

> __< c​haser:monero.social >__ I would be for not exposing that field for such. broken crypto and security bugs could both make a lot of privacy mess out of on-chain memos.     

> __< j​effro256:monero.social >__ Switch commitments alone can't prevent counterfeiting in Monero, we also nee the key images to be intact. However, they are a crucial component of preventing counterfeiting in the future     

> __< k​ayabanerve:matrix.org >__ vtnerd: The issue today is to set up integrity even against a QC. There's minimal changes which can be made now which prevent a QC from counterfeiting years from now, and means anyone who uses a wallet made next year won't be at risk at having their funds burnt.     

> __< k​ayabanerve:matrix.org >__ Yes, the old protocol has to be turned off before a QC becomes active for integrity. The migration scheme would withstand a QC.     

> __< rbrunner >__ I don't remember, was the hope that we could get those switch commitments into "the" hardfork to FCMP++, in about a year?     

> __< rbrunner >__ If we don't take too long to research and decide of course ...     

> __< v​tnerd:monero.social >__ yes, I think the plan was to incorporate switch commitments into the fcmp++ fork     

> __< k​ayabanerve:matrix.org >__ The rest can be done without a hard fork.     

> __< j​effro256:monero.social >__ This is correct: mainly switch commitments + key image binding proofs would prevent counterfeiting. Then, we also need PQ resistant proofs of opening of pubkeys to prevent theft     

> __< j​effro256:monero.social >__ But strictly speaking, if we didn't care about theft, just inflation, we just need switch commitments and key images to be statistically binding     

> __< k​ayabanerve:matrix.org >__ jeffro256: If the 16 bytes is only for change outputs and uses a key not at risk to a quantum adversary who has your address, I don't see the issue.     

> __< k​ayabanerve:matrix.org >__ If a quantum adversary with your address can recover these messages, I don't believe we should represent Monero as a private messenger, even njst to yourself. It's reckless and unsafe.     

> __< k​ayabanerve:matrix.org >__ *just to yourself     

> __< rbrunner >__ Maybe it will be a bit hard to become *really* sure those switch commitments do what we hope for, but maybe we could ask the opposite question: Could something go seriously wrong if we add them?     

> __< rbrunner >__ Right now we don't have any candidates for something else to add instead, do we?     

> __< r​ucknium:monero.social >__ jeffro256: Say I'm a merchant. My database gets corrupted and I have to sync my wallet from its seed words. I hope to recover my accounting records as much as possible. Could those 16 bytes help me at all? AFAIK, the status quo is that I lose the addresses that I sent funds to.     

> __< r​ucknium:monero.social >__ By "database" I mean wallet cache file and associated records in my payment system.     

> __< k​ayabanerve:matrix.org >__ rbrunner: it's an additional hash of the randomness. It can't go wrong. We also can prove the scheme secure for an adversary who can't find preimages to a hash function (chosen collision).     

> __< r​ucknium:monero.social >__ Or maybe just the wallet cache     

> __< j​effro256:monero.social >__ Switch commitments could definitely be part of a solution that DOES allow for mitigating of counterfeiting theoretically. And the changes that we have had to make to FCMP / Carrot aren't all that big IMO. For example, for our switch commitments, in Carrot, we just changed how the blinding factor was bound to certain information.     

> __< j​effro256:monero.social >__ The changes to output pubkeys will likely be similar: hash them a certain way that guarantees opening it and providing a preimage to the opening is computationally intractable even for a QC     

> __< j​effro256:monero.social >__ I definitely am not proposing we try to stuff PQ proving systems with actual PQ cryptography into the upgrade at the moment     

> __< j​effro256:monero.social >__ But cheap stuff like this which may (or may not) give us security in the future is just low hanging fruit IMO     

> __< k​ayabanerve:matrix.org >__ CARROT already implements the necessary output key derivation, no? It's changes to *address derivation* we'd need?     

> __< j​effro256:monero.social >__ > I don't remember, was the hope that we could get those switch commitments into "the" hardfork to FCMP++, in about a year?     

> __< j​effro256:monero.social >__ Much shorter than than, and it doesn't have to be a hard/soft fork decision, it can be completely off-chain loose consensus     

> __< j​effro256:monero.social >__ Yes     

> __< j​effro256:monero.social >__ > Maybe it will be a bit hard to become really sure those switch commitments do what we hope for, but maybe we could ask the opposite question: Could something go seriously wrong if we add them?     

> __< j​effro256:monero.social >__ Not AFAIK     

> __< rbrunner >__ Thanks for the clarifications. So I guess we go for them? (Maybe the decision was already taken, I just was too busy mentally to really get that)     

> __< k​ayabanerve:matrix.org >__ We can't change output derivation without synchrony across wallets? Wouldn't we need a hard fork to ensure that?     

> __< s​yntheticbird:monero.social >__ Reasking what i said at the end of last meeting. Would a PQ addressing protocol using KEM be possible? Afaik, serpahis-pq only made use of DSA, so i wonder.     

> __< k​ayabanerve:matrix.org >__ The point is switch commitments in this HF, as they need a HF, and the new address derivation later, as that doesn't need a HF.     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: Completely different discussion to supply integrity.     

> __< s​yntheticbird:monero.social >__ Ah yes you are right, sry :p     

> __< j​effro256:monero.social >__ It couldn't help with this specific problem without adding additional data. We could derive the ephemeral private keys deterministically, which is also a piece of data that gets lost after a wallet cache is lost. The ephemeral private keys can be used to proving that you *sent* payments to another address. However, you still need the public address on-hand. If your wallet cache ge<clipped messag     

> __< j​effro256:monero.social >__ ts corrupted, and you don't know the address, then you're in the same position. But if you would've known the address, just not the ephemeral private keys, then deterministic derivation of those keys would help you on a corrupted wallet cache     

> __< j​effro256:monero.social >__ But that doesn't require this 16-byte field     

> __< j​effro256:monero.social >__ And the field is too small to put a full Monero address in it     

> __< j​effro256:monero.social >__ So TLDR no     

> __< rbrunner >__ I think we should leave those 16 bytes in peace. Yes, they are there for free, but using them would complicate things, and it could entice some people to do unfortunate things     

> __< s​yntheticbird:monero.social >__ yeah i agree, no compelling reason to use them, more risk     

> __< rbrunner >__ As far as I remember we intend to carry the "traditional" tx_extra forward, so people can still play with that.     

> __< rbrunner >__ With those 16 bytes we would have two mechanisms then, right?     

> __< k​ayabanerve:matrix.org >__ The 16 bytes are fixed, unavoidable, and would be encrypted under CARROT so it isn't immediately the same.     

> __< rbrunner >__ Yeah, but also unused, unless I think of something for me personally?     

> __< j​effro256:monero.social >__ So it's encrypted by default to your view-balance secret, which is PQ resistant, as it is a uniform 32 byte secret only used in key derivation functions. But it's a 16-byte field, so it could be encrypted to anything, hence it's usability for transaction memos. It would have the same privacy implications characteristics as normal transfers: if a quantum computer could see your pub<clipped messag     

> __< j​effro256:monero.social >__ lic address, then they could calculate your private view-incoming key and decrypt the memo, as they can the amount received, the address received to, the payment ID, etc. I wonder if the temptation for doing it, with it being indistinguishable on-chain, will be so high that some wallets will implement it anyways.     

> __< j​effro256:monero.social >__ Quantum computers can already decipher which subaddress the payments go to even knowing just one address in the account     

> __< rbrunner >__ I think it will still make a difference how we label and comment that field, and what we "officially" recommend     

> __< k​ayabanerve:matrix.org >__ ACK for internal memos if we care, NACK external memos. Those schemes already largely suck in that they generally assume 2-output so the output the receiver didn't receive is the change output.     

> __< c​haser:monero.social >__ so, practically, is this only about how the field is labeled?     

> __< j​effro256:monero.social >__ Basically. It's completely possible to use it this way, and we can't really stop it, it's just a matter of official support     

> __< r​ucknium:monero.social >__ Is there any benefit from officially supporting the 16 byte arbitrary data that will discourage "third-party" wallet implementors from doing it "badly", if it can be done badly? Or maybe the benefit is that I don't have to add the Nth private memos paper to moneroresearch.info because some researchers needed to "discover" another way to add private messaging to Monero.     

> __< rbrunner >__ Yes, like many other things that we could not stop. But what we can do is stating clearly that we don't recommend to use it, if we can agree on that.     

> __< c​haser:monero.social >__ I generally assume all crypto to be broken on a long-enough time frame, so I encourage putting as little data into quasi-permanent storage as possible.     

> __< s​yntheticbird:monero.social >__ *16 bytes of arbitrary data, we recommend not using them and relying on tx_extra. This will be decrypted by a quantum adversary. cordially, Monero Project.*     

> __< rbrunner >__ Exactly :)     

> __< j​effro256:monero.social >__ Recommending tx_extra over this field is objectively worse since the memos would be *possibly* decrypted BUT guaranteed to be distinguishable on-chain trivially     

> __< c​haser:monero.social >__ I think one of the first references to public key crypto was someone in the 19th century assuming that factoring a 10-digit number is intactable. we are those people for cryptographers in 2150     

> __< s​yntheticbird:monero.social >__ well, it's always a matter of buying time     

> __< rbrunner >__ I wait for people to produce 10 change outputs to have 160 bytes to use ...     

> __< c​haser:monero.social >__ SyntheticBird I think that will do     

> __< c​haser:monero.social >__ rbrunner: not under the max 8-out regime :)     

> __< r​ucknium:monero.social >__ Mordinals did something clever with brunt outputs and ring signatures, to show transfer of them. I guess Mordinals in the 16 bytes is unlikely since you could only put a hash there, not a full image, but is there anything about the 16 bytes that is not being considered that could make it more attractive to a Mordinal revival?     

> __< rbrunner >__ Duh ...     

> __< j​effro256:monero.social >__ But moving memos to a different part of the transaction doesn't magically  make the encryption stronger, it just signals that you're definitely using this feature     

> __< s​yntheticbird:monero.social >__ Oh no no, i didn't meant that this would be safer, at the opposite; just signaling in the recommendation that they shouldn't expect a stronger encryption. You're still right on the deniability of extra data use.     

> __< j​effro256:monero.social >__ Not AFAIK over the 1060 bytes we already allow in tx_extra     

> __< s​yntheticbird:monero.social >__ 1080*     

> __< r​ucknium:monero.social >__ The 16 bytes is provably linked to a key, right? That's a little different from the data in tx_extra     

> __< c​haser:monero.social >__ could this field be multiple times larger and then tx_extra, assuming some tweaks to the tx format, be deprecated?     

> __< rbrunner >__ But it's encrypted with a secret key? The receiver can't read it?     

> __< s​yntheticbird:monero.social >__ this would fall back into the discussion of whether deprecating tx_extra. What size should user be expecting. Also whether you are using it or not doesn't change the tx will be N time larger than it needs     

> __< s​yntheticbird:monero.social >__ If a lot of people were using tx_extra it would make sense to make every tx 64 bytes larger for uniformity, but right now tx_extra is rare     

> __< j​effro256:monero.social >__ Its 1060     

> __< s​yntheticbird:monero.social >__ If a lot of people were using tx\_extra it would make sense to make every tx 64 bytes larger for uniformity, but right now tx\_extra is rare afaik     

> __< j​effro256:monero.social >__ https://github.com/tevador/bitmonero/blob/3771641fc5f40cee20df297f49f0dc2213947a45/src/cryptonote_config.h#L212     

> __< c​haser:monero.social >__ oh, can of worms.     

> __< r​ucknium:monero.social >__ Isn't the receiver always yourself? So you could always read it. And if you give they key to someone else, they can read it     

> __< s​yntheticbird:monero.social >__ thx I literally looked at it yesterday but misread 👓     

> __< rbrunner >__ I mean that tx_extra is a lot more flexible in this regard. You can even send things in the clear there     

> __< r​ucknium:monero.social >__ I am just trying to get some adversarial thinking about what a Mordinal reviver might want to do.     

> __< k​ayabanerve:matrix.org >__ FWIW unless there's an explicit use case posited here, I'd say no official support, acknowledgement of potential for *internal use*, but no endorsement.     

> __< j​effro256:monero.social >__ Depends on what you mean by "provably linked". Its just space in some enote that can be written to by anyone signing the transaction     

> __< j​effro256:monero.social >__ Its not necessarily "linked" by any force greater than convention     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: I considered advocating for a fixed, encrypted blob in TX extra and decided against it for how much of a mess it'd be. Making TX extra larger to provide uniformity to bad TXs doesn't change how we shouldn't be encouraging bad TXs which are fundamentally bad.     

> __< rbrunner >__ Can't we tweak the format of change enotes a little bit and get something that we *must* put into those 16 bytes? So they are not free anymore, discussion closed?     

> __< k​ayabanerve:matrix.org >__ jeffro256: but the only idea officially posited, and safely posited, is to encrypt with the sender's key which is symmetric and not recoverable by a QC     

> __< rbrunner >__ (I am about 50% serious with this question)     

> __< k​ayabanerve:matrix.org >__ So while yes, it's not ZK proven to be encrypted to that key, and is arbitrary, that's not the use-case posited here today     

> __< j​effro256:monero.social >__ > <r​brunner> Can't we tweak the format of change enotes a little bit and get something that we *must* put into those 16 bytes? So they are not free anymore, discussion closed?     

> __< j​effro256:monero.social >__ Like any regular encrypted data, we can't enforce the contents without adding some kind of verifiable encryption scheme which would put compute load on the nodes and probably make transactions sizes bigger     

> __< rbrunner >__ No, I mean we add some short key, or some hash, or whatever, that is needed for processing change enotes     

> __< rbrunner >__ So the statement "Those 16 are unused" becomes false     

> __< r​ucknium:monero.social >__ If I'm a third-party wallet dev and I put the same thing in those 16 bytes every time instead of random data, e.g. `000000`, is there any cryptographic risk of re-using plaintext again and again? Just trying to understand how things could go wrong.     

> __< c​haser:monero.social >__ maybe add something that only the one doing the enote scanning has to compute, not all full nodes.     

> __< rbrunner >__ Yes     

> __< rbrunner >__ But well, maybe that whole idea could be just nonsense ...     

> __< k​ayabanerve:matrix.org >__ Rucknium: You'd create a fingerprint     

> __< r​ucknium:monero.social >__ I am always thinking about mistakes wallet devs can make since I see them on the blockchain too often     

> __< rbrunner >__ Which is ... unfortunate, but can happen easily?     

> __< j​effro256:monero.social >__ > No, I mean we add some short key, or some hash, or whatever, that is needed for processing change enotes     

> __< j​effro256:monero.social >__ Hmmm I will think about this more but probably not. The field is on an internal selfsend enote , not the transferred one, so it would mean that enotes can fail to scan based on the contents of other enotes which is kind of gross     

> __< rbrunner >__ Maybe the thing that they want to put in there really does not change much, or hardly at all?     

> __< j​effro256:monero.social >__ Also if the check is trivial and I lose money adhering to it, I'm probably going to run a wallet which let's me recover those funds even if it means breaking some trivial rule     

> __< rbrunner >__ If one part of the change enote is encrypted with the key that is in those 16 bytes? How would you circumvent that and still (ab)use the field?     

> __< rbrunner >__ But I agree that goes pretty far, just to prevent use of the bytes     

> __< j​effro256:monero.social >__ I think Rucknium meant 0s BEFORE encryption to self, right ?     

> __< r​ucknium:monero.social >__ Yeah I do mean that. But also after "encryption" if a wallet dev can somehow get around that encryption step     

> __< k​ayabanerve:monero.social >__ Oh, sorry if I misunderstood Rucknium     

> __< k​ayabanerve:monero.social >__ A wallet dev can do whatever they want there     

> __< k​ayabanerve:monero.social >__ *if they sufficiently fork the stack     

> __< r​ucknium:monero.social >__ IMHO, it is best to have the path of least resistance (least dev work) to be the safest. So if the path is to enable an "easy" API to add data, but make it add no data by default, then maybe that is best.     

> __< r​ucknium:monero.social >__ And good docs are needed. Don't forget that :)     

> __< s​yntheticbird:monero.social >__ yeah Docs are the key here     

> __< j​effro256:monero.social >__ Yeah it could be a fingerprint if they screw it up and put the 0s into the tx without fingerprinting     

> __< r​ucknium:monero.social >__ Remember, recently Siren (comfy)  was adding a fingerprint to their MoneroPay txs accidentally because the docs were not clear.     

> __< v​tnerd:monero.social >__ Sorry got behind on the list. Probably want to do it a hardfork though, otherwise people might use wrong version and get locked out of the switch phase     

> __< j​effro256:monero.social >__ If we do it now, then there won't HAVE to be any fork     

> __< r​ucknium:monero.social >__ The meeting has gone pretty long. I think the 16 free bytes can be put on next agenda's meeting, unless people think that everything is settled.     

> __< j​effro256:monero.social >__ Out of curiosity, What was the fingerprint ?     

> __< r​ucknium:monero.social >__ Unlock time 10     

> __< r​ucknium:monero.social >__ Should be 0     

> __< j​effro256:monero.social >__ I'm fine for now not officially supporting external memos until it comes back up again downstream     

> __< v​tnerd:monero.social >__ does this mean no payment id like functionality? I assume thats what you mean by memo?     

> __< v​tnerd:monero.social >__ I need to re-read your carrot proposal I think, things have changed since I first looked     

> __< j​effro256:monero.social >__ Payment IDs are separately supported     

> __< j​effro256:monero.social >__ They also have the same PQ privacy issues     

> __< j​effro256:monero.social >__ Except that they're smaller so they  allow "less" arbitrary data     

> __< r​ucknium:monero.social >__ --- Meeting end ---     

> __< r​ucknium:monero.social >__ Feel free to continue discussing :)     

> __< c​haser:monero.social >__ a remark re: Carrot address format. AFAIK it's he first change in Monero's history where the same mnemonic will be able to resolve to two different key chains (barring a potential feature bit flipping for *newly generated* Polyseeds, but that's out of scope for my point here).     

> __< c​haser:monero.social >__ this seems like a good opportunity to unify prefixes, doing away with the 4/8 (primary/subaddress) distinction for Carrot addresses.     

> __< c​haser:monero.social >__ IMHO, ideally all becoming 8... addresses, so Carrot users can blend into the already existing crowd of legacy subaddress users.     

> __< c​haser:monero.social >__ *the     

> __< j​effro256:monero.social >__ You have to have a signifier between main/integrated addresses and subaddresses because the sender handles them differently. Namely, they construct the ephemeral pubkey differently. But Carrot addresses will already be indistinguishable from legacy addresses     

> __< j​effro256:monero.social >__ Thanks everyone for the meeting BTW!     

> __< s​yntheticbird:monero.social >__ thanks delicious meeting as always     

> __< c​haser:monero.social >__ jeffro256 got it, thank you. so is this is a requirement on the consensus side, not related to the derivation scheme?     

> __< c​haser:monero.social >__ and, likewise, thank you all!     

> __< j​effro256:monero.social >__ No not a consensus requirement at all. The ephemeral pubkey is indistinguishable as belonging to either a main address or a subaddress, but if you try to make an enote ephemeral pubkey like you would for a subaddresses, when the address is actually a main address, then the payment simply won't be scannable by the receiver     

> __< j​effro256:monero.social >__ And vice cersa     

> __< j​effro256:monero.social >__ versa     

> __< a​rticmine:monero.social >__ There is also an important cultural benefit in China by moving entirely to all becoming 8... Addresses     

> __< s​yntheticbird:monero.social >__ TIL ArticMine is not only knowledgeable on scalability     

> __< c​haser:monero.social >__ I once listened to Artic speaking 2 hours about the dynamic block size algorithm, and they eventually drove it back to how holes were arranged on punched cards for 1960s' computers. so, yeah, pretty much.     

> __< v​tnerd:monero.social >__ I _think_ this may have been asked+answered before, but what happens to the existing ring-ct outputs if we transition to switch comittments? Those outputs have to move before the “switch” occurs, otherwise they have to be locked out. Any existing pre-ringct outputs can still be converted. Anyway, it’s an unfortunate that the only mitigation is a PSA to move outputs, etc.     

> __< s​yntheticbird:monero.social >__ Yes they will need to transition during the pre-QC period. And after a reasonable amount of time (2~3 years?) the migration will be completed and old outputs will be locked. Pre-ringCT outputs will have to transition too. Kayabnerve argued that most of these outputs are probably lost/burnt.     

> __< v​tnerd:monero.social >__ yes, I remember the prior discussion now.     

> __< j​effro256:monero.social >__ Previously, I mistakenly stated that we could migrate pre-RingCT outputs, since they have a cleartext amount, but I didn't take into account how FCMP++ will interact with key images for those outputs     

> __< j​effro256:monero.social >__ Hypothetically, we might be able to make them spendable if we chose the `T` generator for FCMP++ in a way that is cryptographically verifiable that guessing the generator before some point in time, after the RingCT hard fork, is intractable     

> __< j​effro256:monero.social >__ Because the problem with making them spendable is that if pre-RingCT outputs are constructed O = x G + y T with a known y value known s.t. y != 0, then the key image spending in a FCMP++ is L = x Hp(O), which is different than what we expect them to be, which is L = dlog(O, G) * Hp(O)     

> __< j​effro256:monero.social >__ But if `T` isn't guessable until some point in the future, then it would be impossible to create a valid key image in a FCMP++ for that output that ISN'T L = dlog(O, G) * Hp(O)     

> __< j​effro256:monero.social >__ Then, during the PQ migration, we can check that if-and-only-if the originating height of the spent output is < v6 hard fork height, we allow the output to be migrated if the key image is exactly L = dlog(O, G) * Hp(O)     

> __< j​effro256:monero.social >__ If we made the `T` generator a function of the current Monero block ID, then the trust assumption for preventing inflation would be 1-of-N honest participants, where N is the number of total transaction creators on the Monero blockchain, ever     

> __< j​effro256:monero.social >__ Actually, not ever, just sincev6     

> __< k​ayabanerve:matrix.org >__ jeffro256: FYI, non-RingCT outputs can still be created today.     

> __< j​effro256:monero.social >__ Yes, namely "unmixable sweep" txs. Hence, the height requirement     

> __< k​ayabanerve:matrix.org >__ We'd need a HF banning non-RingCT outputs, then to decide T via the blockchain if that's considered secure, then to activate FCMP++.     

> __< k​ayabanerve:matrix.org >__ Or at least a designation height for which non-RingCT outputs won't be migrateable.     

> __< j​effro256:monero.social >__ I'd vote the latter     

> __< k​ayabanerve:matrix.org >__ I'd vote none of this mess.     

> __< j​effro256:monero.social >__ TBF It's a small tweak to a single value and we don't actually have to handle the implications *now*     

> __< k​ayabanerve:matrix.org >__ Also, AFAICT, your security analysis is wrong.     

> __< j​effro256:monero.social >__ Certainly possible. How so?     

> __< k​ayabanerve:matrix.org >__ Considering the entire blockchain as a transcript, and T a sampled challenge, makes it effectively impossible to define a key on the blockchain which uses T. It's secure in general, not under a 1-of-n trust assumption.     

> __< k​ayabanerve:matrix.org >__ An adversary who could could break our proofs.     

> __< k​ayabanerve:matrix.org >__ But I also don't want to debate this ad infinitum. We should define a migration scheme and rely on it. I don't believe we should work on alternative schemes to expand the class of migratable outputs when the existing class is sufficiently wide to the point this is complexity without sufficient benefit.     

> __< k​ayabanerve:matrix.org >__ Also, your proposal, if implemented, cryptographically binds a checkpoint into the blockchain and technically means Monero either doesn't follow the chain with most work OR Monero may fork to an chain where the security is broken.     

> __< k​ayabanerve:matrix.org >__ It also mandates T not be a constant but variable to each network (unless we allow inflation on testnet and co) which would be a mess to implement.     

> __< j​effro256:monero.social >__ I wonder how well the current reference node can currently handle a 1.9 million block reorg....     

> __< k​ayabanerve:matrix.org >__ Would that be if you used the RCT activation height?     

> __< j​effro256:monero.social >__ Pre-RingCT deactivation height, excluding unmixable v1 sweep txs     

> __< j​effro256:monero.social >__ I don't care to try to migrate those     

> __< j​effro256:monero.social >__ Or we could just hash in all three block IDs into `T` and it works across all networks     

> __< k​ayabanerve:matrix.org >__ Verifying that as a NUMS constant now requires syncing three different blockchains?     

> __< j​effro256:monero.social >__ If you care about all three blockchains, then yes. But if you just cared about mainnet, it would suffice to check just the mainnet block ID, because adding in more block IDs won't reduce the entropy of the `T` result     

> __< k​ayabanerve:matrix.org >__ It does change the security analysis?     

> __< k​ayabanerve:matrix.org >__ It makes the T generator malleable w.r.t. the mainnet blockchain. There's no longer a single choice but 2**512 (which presumably collapse into most of the ~2**252 results).     

> __< j​effro256:monero.social >__ I understand what you're saying, but we're already assuming for our PQ migration that adversaries cannot find hash collisions or preimages, even with large entropy inputs     

> __< j​effro256:monero.social >__ For example, our switch commitmen blinding factors hash a lot of information, including a 32-byte secret, a 32-byte address, and an amount into a scalar, then the preimage is revealed     

> __< k​ayabanerve:matrix.org >__ I was trying to point how that your proposal of multiple inclusions can't be so trivially stated, not claiming that breaks the scheme.     

> __< k​ayabanerve:matrix.org >__ I've somehow allowed this to take half an hour of my time. I still personally find this proposal messy and not sufficiently worthwhile. I will be withdrawing from further conversation on it tonighy.     

> __< j​effro256:monero.social >__ Fair enough, thanks for the discussion thus far though :)   



# Action History
- Created by: Rucknium | 2025-01-07T20:42:13+00:00
- Closed at: 2025-01-21T19:53:14+00:00
