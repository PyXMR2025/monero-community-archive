---
title: Exploring Trustless zk-SNARKs for Monero's payment protocol
source_url: https://github.com/monero-project/research-lab/issues/100
author: sethforprivacy
assignees: []
labels: []
created_at: '2022-05-02T17:12:33+00:00'
updated_at: '2025-02-20T20:28:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The goal of this meta issue is to build a go-to place for links, information, and opportunities for building trustless zk-SNARKs as a potential future protocol building-block for Monero.

Disclaimer: I am not a cryptographer or a dev, so please provide corrections and context if I have missed key details here. I am merely seeking to pull people together who are, provide resources, and ensure we take as close of a look as necessary at zk-SNARKs as a potential upgrade for Monero in the future.

## Why zk-SNARKs?

Monero has iterated over the years to continue in leading the way in building out a cryptocurrency that puts user's privacy and security above all else. The Monero community has done this through finding the gaps and flaws in the protocol, watching external projects and researchers work, and implementing both internal and external developments over time to improve the holistic privacy provided to every user of the Monero network.

The weakest aspects of Monero's current approach to privacy is that of ring signatures, the approach that is taken to hide the true spend in each transaction among a set of potential signing inputs. These ring signatures have been an excellent tool for Monero so far, allowing us to build stable, efficient, and trustless privacy into each transaction, and are greatly strengthened by the added privacy of one-time addresses and confidential amounts.

While these three building blocks provide strong privacy today and show no signs of causing broad issues, they have [noted weaknesses](https://www.youtube.com/watch?v=iABIcsDJKyM), especially for targeted threat models or those where multiple entities collude to form a transaction graph via EAE attacks or similar. This key weakness, combined with the ability to build probabilistic transaction graphs with off-chain data, should push us to keep seeking how we can mitigate the issue entirely.

The proposed [Seraphis protocol](https://github.com/UkoeHB/Seraphis) allows us to greatly reduce the chances of successful probabilistic tracing, but is not necessarily a complete solution for targeted attacks or those aided by off-chain metadata. I *do not* want to prevent the further exploration of Seraphis with this effort, and a migration to Seraphis could even simplify a potential future migration to zk-SNARKs thanks to the modularity of Seraphis approach to the payment protocol.

zk-SNARKs allow us to move from obfuscating the true spend to truly hiding it, a large step forward in preventing even targeted attacks from building a transaction graph, while doing so in a way that remains trustless and efficient.

While it is outside of the scope of this issue, zk-SNARKs can also be used to build out much more advanced protocol features such as colored coins, smart contracts, etc. like currently being built out by DarkFi. This flexibility can pave the way for greater use-cases being built out on Monero in the future, and could be an extremely useful building block.

## Why now?

With the advent of trustless and relatively efficient zk-SNARKs via advances like [PLONK](https://eprint.iacr.org/2019/953.pdf) and implementations of it like [Halo 2](https://electriccoin.co/blog/explaining-halo-2/), zk-SNARKS are finally at a state where we can truly explore what an implementation of them in Monero's broader transaction protocol would look like, the implications it would have, the leg-work required, etc.

While Seraphis will bring much greater per-transaction graph obfuscation, it still provides some attack vectors for targeted attacks. As such, we should keep looking to the future and find ways that we can continue improving the Monero protocol over time.

## Proposed efforts

While I know this is a major shift in the approach Monero has taken to output hiding in the past, there are some unique opportunities available to us today thanks to the wealth of effort being poured into zk-SNARKs across the cryptocurrency and privacy ecosystem today.

1. Amir Taaki (@narodnik) of Dark.fi has offered to contribute whatever education/bootcamping is necessary to get Monero developers up to speed on implementing zk-SNARKs in a payment protocol
	1. Amir's estimate is ~2wks of full-time bootcamping to get up to speed and implement a  PoC in a simple language
	2. I would love to see developers that are familiar with cryptography/math jump in on this and will help in crafting a CCS proposal for funding if necessary
2. If necessary, I will organize a meeting of the MRL to discuss the viability of zk-SNARKs in the Monero protocol
3. I will write up a blog post further outlining in laymen's terms why exploring zk-SNARKs as a replacement for ring-signatures (and likely confidential amounts) is an interesting and worthwhile topic to explore for the community (can publish on my own blog or getmonero.org if suitable)
4. Collect feedback on ways that a migration to zk-SNARKs would effect current ecosystem participants, atomic swaps development, etc.

## Open research questions

There are many open questions that we would need to (or should) answer in the process of exploring what an implementation of trustless zk-SNARKs would look like in Monero. If you want to take on one of these open questions, please open a new issue/gist and provide the link so I can update it here.

- Can zk-SNARKs offer improvements to specific functions in the Monero payments protocol, i.e. *just* membership proofs?
  - Being investigated by @UkoeHB and @kayabaNerve
- What are the practical implications to user privacy with ring-signatures vs a zk-SNARK approach to input hiding?
  - What attacks or flaws in ring-signatures are mitigated by zk-SNARKs?
  - What new attacks or flaws are created by zk-SNARKs?
- What would the potential transaction size, generation, and verification times look like for a Halo 2-like payment system in Monero?
  - How would transaction verification be affected by batching? How about multithreading?
  - Can mobile devices easily and quickly generate transactions?
- Can existing hardware wallets (Trezor/Ledger) support a zk-SNARK system for Monero?
- What is the quantum-resistance offered by zk-SNARKs as opposed to ring signatures + RingCT?
- What effects would a migration to zk-SNARKs have on atomic swaps with Bitcoin and Ethereum?
- What advantage or disadvantage would the elliptic curves used in a zk-SNARK implementation have on interoperability between Monero and other networks/chains?
- What functionality extensions can zk-SNARKs bring to Monero's base layer?
  - Layer-two networks?
  - Smart contracts?
  - Colored coins?

## Extra notes

- We do not need to leverage any of Zcash's existing code for this, and can (and should!) explore a from-scratch implementation in C++ that better fits our broader payment protocol
- I hope that we can see past the "Monero v Zcash" ongoing drama and approach this from a research and technology perspective, especially as much of the technology and research here was invented or improved upon by researchers and developers entirely outside of the Zcash space
- zk-SNARKs have *a lot* of weight behind them in the privacy space, layer-two developments space, Zcash space, and other places, making them a great option to explore as we can benefit greatly from the broad academic and development work ongoing around the concept of trustless zk-SNARKs

## Helpful links

### Educational resources and explainers

- [Awesome zero knowledge proofs resource list](https://github.com/matter-labs/awesome-zero-knowledge-proofs)
- [Awesome zero knowledge proofs resource list - SNARKs](https://github.com/matter-labs/awesome-zero-knowledge-proofs#snarks)
- [Awesome zero knowledge proofs resource list - SNORKs](https://github.com/matter-labs/awesome-zero-knowledge-proofs#snorks)
- [Awesome PLONK resource list](https://github.com/Fluidex/awesome-plonk)
- [Sapling payment scheme (mint/burn) - DarkFi](https://darkrenaissance.github.io/darkfi/zkas/examples/sapling.html)
- [Halo 2 book - Zcash](https://zcash.github.io/halo2/)

### Existing implementations and code examples

- [PLONK implementation in C++ - Aztec](https://github.com/AztecProtocol/barretenberg/tree/master/barretenberg/src/aztec/plonk)
- [Halo 2 implemenation in Python/Sage - DarkFi](https://github.com/darkrenaissance/darkfi/blob/master/script/research/halo/halo2.sage)
- [Bulletproofs implementation in Python/Sage - DarkFi](https://github.com/darkrenaissance/darkfi/blob/master/script/research/bltprf/singleround.sage)
- [Mint contract (circuit) in Rust - DarkFi](https://github.com/darkrenaissance/darkfi/blob/master/src/zk/circuit/mint_contract.rs)
- [Burn contract (circuit) in Rust - DarkFi](https://github.com/darkrenaissance/darkfi/blob/master/src/zk/circuit/burn_contract.rs)
- [Halo 2 Rust crate - Zcash](https://github.com/zcash/halo2)

P.S. -- if you come across helpful research that could be applicable to zk-SNARKs in Monero, please consider submitting it for inclusion on https://moneroresearch.info.

# Discussion History
## jstkdng | 2022-05-02T18:08:21+00:00
Hey man, blink if you've been compromised by any 3 letter agencies.

## sethforprivacy | 2022-05-02T18:09:42+00:00
> Hey man, blink if you've been compromised by any 3 letter agencies.

Exploring broadly used and researched tech has nothing to do with any 3 letter agencies. Take your spam elsewhere, please, this is supposed to be a place for on-topic discussion into research topics, not pointless harassment.

The topic of zero-knowledge proofs (and zk-SNARKs) is *much* broader than Zcash, so don't let your animosity (for good or bad reasons) towards them cloud your judgement on the broader technology.

## narodnik | 2022-05-02T18:34:53+00:00
Hey, so I wrote the first implementations of coinjoin and stealth addresses, and implementations of all the major anon algos: ring sigs, mimblewimble, lelantus, bulletproofs, and the major zk algos: groth16, sonic, plonk, halo1, halo2, ... and a ton of experiments.

I did a ton of optimization on ring sigs, and got 100k keys verification down to a few secs, but that still isn't good enough since the glowies can put in fake duds to compromise the anon set. Lelantus/jens groth 1 out of n proofs are decent, but Zk is the best. Verification is only a few ms, and the anonymity set is practically infinite (2^32).

For your implementation, you don't need orchard since you should write your own zk contracts (called "circuits"), which is trivial enough to do. If halo2 being in rust is a problem, then you should look at aztec's plonk implementation which is in C++.

ZK proofs are two parts:
* Arithmetization which is turning your contract into a mathematical arithmetic operators add and multiply. This part is relatively simple and straightforward to grasp.
* Polynomial commitment proof, which is given a commitment `A = commit(a(x))` to a polynomial, you can make a proof `pi = prove(A, s, a(x))` which then a verifier can prove that `z = a(s)` like this: `verify(pi, A, s, z)` which doesn't reveal `a(x)` itself.

```
halo2 = plonk arithmetization + bulletproofs polynomial commitment proof
```

So basically Monero already contains the core component of zk-snarks (which is used for rangeproofs).

For the arithmetization, we can talk to aztec. Ariel Gabizon invented plonk which is actually what halo2 is really, the zcash team replaced the polynomial commitments with bulletproofs instead of the KZG scheme which has a trusted setup. Happy to make that intro. Their plonk implementation is in C++ iirc.

From our side, we're happy to work with a team of focused Monero devs to step them through the algo and get them up to speed, and then follow their development doing code reviews and offering feedback. We have several devs in our team writing zk contracts and who are familiar with zk algos.

Monero is the backbone of the crypto minecraft markets, and our community deserves the very best. Self defense of the people is crucial in this coming dawn of the new era.


## parazyd | 2022-05-02T18:41:27+00:00
On top of this, I've written a VM and a language + compiler for prototyping ZK circuits/contracts with Halo2: https://darkrenaissance.github.io/darkfi/zkas/

And indeed, we're happy to help with advice and guidance if there is proper focus and commitment.

## sethforprivacy | 2022-05-02T18:43:10+00:00
Thanks for the comments and details, @narodnik, demistifying the approaches taken in something like Halo 2 is extremely helpful. Very grateful for the offer of help and the quick input, and am hopeful this exploration can be meaningful and lead to a potential future implementation for Monero.

I've also tracked down and added the link to the Aztec PLONK implementation in C++ to the Helpful Links section.

## UkoeHB | 2022-05-02T21:20:33+00:00
> I did a ton of optimization on ring sigs, and got 100k keys verification down to a few secs, but that still isn't good enough since the glowies can put in fake duds to compromise the anon set. Lelantus/jens groth 1 out of n proofs are decent, but Zk is the best. Verification is only a few ms, and the anonymity set is practically infinite (2^32). @narodnik 

Am I reading this correctly, and you know how to implement a membership proof ('ring sig') with Zk (a Halo2 circuit)? I already have a full transaction protocol (Seraphis) that just wants a better membership proof (ideally one that can just plug-and-play with the rest of the protocol, even if a different underlying curve than ed25519 is required). My confusions with this Halo2 stuff are whether anyone actually knows how to make a membership proof with it, what the design of that circuit would look like (some kind of oblivious Merkle or Verkle proof?), and what requirements it would impose on the surrounding protocol (curves, ways of building points, prerequisites to build and verify proofs, etc.).

## kayabaNerve | 2022-05-02T22:02:39+00:00
Zcash's circuits are Merkle tree based, from my understanding. Instead of key images, you specify nullifier hashes, and the ZK proof says it's some member of the merkle tree (whose root hash is referred to as the anchor) which is appended to with each output.

Regarding Seraphis, it's important to note an isolated ZK proof for membership would be incredibly inefficient. You'd want one proof for both membership and validity. It'd effectively be two BPs to have it as an isolated proof when they'd be mergeable to just one.

I'd be personally interested in shadowing these discussions.

## UkoeHB | 2022-05-02T23:02:02+00:00
To clarify, a Seraphis membership proof needs to say the following:
- we have a vector of points `V = {Q_1, Q_2, ... Q_n}`
- I have a commitment `Q' = xG + Q_l` for some `l`
- the membership proof shows that `Q'` is a commitment to a member of `V` but doesn't show which one
- after the membership proof is done, I can do whatever normal EC ops with `Q'` that I want (ideally, in ed25519)

After discussing with @kayabaNerve, the above proof seems possible with existing techniques (it is the simplest possible zk proof that we could use). Stuff like recursive proofs, nullifier hashes, etc... don't really get me excited. Batch verification would get me excited (specifically batching with BP+ proofs - can we share generators? please yes please). Combining range proofs with the membership proofs in one zk proof is an interesting idea _iff_ the efficiency gains are well understood and non-trivial. Combining them is not necessary, and could easily be rolled out in an update after the one that implements the simple membership proof (if deemed worthwhile).

## kayabaNerve | 2022-05-03T02:30:45+00:00
I did agree to put forth a demo of the above in Rust when I have the time, based on discussions on Matrix. That isn't a pivot within Seraphis, to either ZK-SNARKS nor Rust, yet it's a comment on potential API/flow/performance. I may use either Dalek's Bulletproofs (which would likely be the easiest to move from a PoC to something actually in C++ in Monero, guaranteeing ed25519 and batch verification) or Halo 2, or another PLONK system, and have yet to decide.

## narodnik | 2022-05-03T08:38:31+00:00
Aha so Seraphis is based off of Jens Groth 1 out of N commitment to 0? That's also a solid anonymity scheme.

Yes, we have the membership proofs working. They are quite easy to do. You provide the pathway in a merkle tree then inside the zk proof, you do:
```
current = X
for i in range(32):
    left = current
    right, is_right = merkle_path[i]
    # since is_right is a bool, you can do this:
    #     is_right * left + (1 - is_right) * right
    #     is_right * right + (1 - is_right) * left
    left, right = if is_right { left, right } else { right, left }
    current = hash(left, right)
```

The basic ZK payment scheme is the following:

Mint:
```
private serial = random_scalar()
private blind = random_scalar()
public C = hash(serial, blind)
```

Then the coin C gets added in the merkle tree.

Burn:
```
public nullifier = hash(serial)
private C = hash(serial, blind)
assert C in merkle_root
make_public(merkle_root)
```

In practice we add more attributes to the coin C such as a public key (so nullifier can only be constructed by secret key), a value (so we hide amounts with CT), a token ID, and other attributes (such as permissions or owners).

## kayabaNerve | 2022-05-03T08:43:02+00:00
Right. I am sufficiently familiar with the Zcash side of things to know the algorithm to use for this.

I also do understand Zcash is just one of many players in the field, yet they're the one I'm most familiar with and they do use merkle trees to store their outputs (with the Sapling input proof containing merkle tree pathing). I've also reviewed Tornado Cash which has its own merkle tree work and understand the multiplication used to achieve constraint definitions successfully. I only expect it to take a few hours to a couple of days, personally, I'm just busy for a bit.

## narodnik | 2022-05-03T08:45:48+00:00
You guys don't need to code the zk contracts (circuits). Here is the code for halo2:

https://github.com/darkrenaissance/darkfi/blob/master/src/zk/circuit/mint_contract.rs

https://github.com/darkrenaissance/darkfi/blob/master/src/zk/circuit/burn_contract.rs

It's more if you want to make your own plonk/halo2 prover/verifier system instead of using aztec or halo2 lib. That would be the work that actually takes time.

## narodnik | 2022-05-03T08:47:35+00:00
And here they are written with @parazyd 's compiler:

* https://github.com/darkrenaissance/darkfi/blob/master/proof/burn.zk
* https://github.com/darkrenaissance/darkfi/blob/master/proof/mint.zk

## kayabaNerve | 2022-05-03T09:10:27+00:00
narodnik: That isn't the point. At all.

koe is specifically requesting a simple membership proof which is a trivial circuit to write. I am personally interested in providing such a demonstration so not only can they get a feel for it in a very self contained box, yet I can finally say I've successfully written a circuit. If your goal is to encourage Monero developers to move from the theoretical to the implementation, I'd hope you agree with my goal. If you'd rather simply post a Rust demo which handles membership and lets us do feasibility analysis, and be the Monero developer, you can also do that. I can't exactly complain in that case.

I will note your examples include nullifiers which is *not* what koe is requesting. While I advocated for the input ZK proofs as an equivalence to the modern CLSAG, Seraphis has a distinct design which separates membership proofs from linkability from range proofs. Personally, I can see why that might have an advantage. If we're able to define an accumulator which solely contains outputs, and only ever have to prove membership in it, we can change our membership proof (say, from Bulletproofs to Halo 2 or from Halo 2 to Halo 3 ~~or from Halo 3 to Halo Reach~~) without needing to define a new transaction pool as the linkability proof would remain constant and consistently formed. While it should also be possible without issue for such a limited output definition to produce consistent nullifier hashes across such proof formats, I am trying to note the potential advantages of a flexible and concise design and the considerations desired. The other important items are the distinction between spend authorization and spend detection (outgoing view keys, which I know plenty of existing SNARK systems offer, yet a distinct linkability proof may simplify), and the feasibility of multisig.

While I don't know the full details of how this may play out, I will say the immediate task is solely the membership proof as that serves a drop in role to the currently designed next protocol with no further considerations needed. From there, it's a discussion on evolution and moving more items over as proper. I'm also more interested in a BP+ design than a Halo 2 design at this point so Monero can more easily integrate it, as unfortunately there may be an aversion to Rust, not to mention the fact we already have BPs available (so we'd also not require adding an entirely external cryptsetup we haven't reviewed).

This is a very experimental topic opened by @sethforprivacy. koe, who's effectively leading the next transaction protocol, didn't want to immediately start a potentially not used idea with reformatting back to the existing system (membership + linkability as a single proof), and instead just wants a simple membership proof as a demo. I, as a developer who can probably write a basic circuit and was here to comment, offered to. This change won't happen overnight. You're welcome to post a series of ZK circuits based on Halo 2 and say Monero should move to it and leave it at that. The discussion being had here is taking it one step at a time. We have the option for a more efficient membership proof (one which is vastly more private). Once we have that proven, we'll see how else we can improve along this path.

You're obviously someone who has more experience than anyone who has commented thus far (except maybe parazyd who's with you :p ) and I'd appreciate your help as I work on a PoC, as I need it, and your help as we discuss protocol boundaries and further movements from there if we continue the discussion. I just, at least personally, don't appreciate being dumped full setups and being told we don't need to do anything. Seraphis is the future privacy protocol for Monero and accordingly needs to be the perfect fit for Monero. If an existing protocol is that perfect fit and has the most efficient code, I would see no issue with adopting it. If we were willing to accept something potentially good enough because it already existed... we probably wouldn't have made RingCTs and would still have public amounts :p

The important part is there needs to be a process here instead of a statement. Any process is going to be based off the current plan, which is Seraphis. koe's statement on the next step for bringing SNARKS into Seraphis is just a membership proof. If it legitimately is more efficient and it's believed to be feasibly integrateable... then it needs to be discussed with other developers from a variety of standpoints (extending our own BP+ impl to include programs, implementing another system, grabbing a C++ library, officially introducing Rust to the toolchain...). It's just a process.

EDIT: I will also note the provided code is AGPL which means we can't even use it in a proof of concept without the proof of concept being AGPL and... while I have no issue with AGPL in the right place, and a PoC should be an isolated PoC which means it shouldn't be an issue, I would like to avoid any licensing issues while this is prototyped and worked with.

## narodnik | 2022-05-03T10:37:27+00:00
lmk then what you need.

I would proceed like this:
* Learn plonk algo
* Learn halo2 algo
* Write simple circuits such as mimc or poseidon hash functions
* Implement your merkle proof

You can also start with the merkle proof then go backwards. You might want to do all of this in sage/python.

## UkoeHB | 2022-05-03T12:43:47+00:00
> In practice we add more attributes to the coin C such as a public key (so nullifier can only be constructed by secret key), a value (so we hide amounts with CT), a token ID, and other attributes (such as permissions or owners). @narodnik 

It sounds like a lot of the work put into these zk circuits focuses on building a large transaction protocol _within_ the circuit (i.e. proving many kinds of statements within a single proof). Unfortunately, there are always design and efficiency consequences to coupling proof statements. In Cryptonote/RingCT, we had multiplicative inefficiency in the ring signatures in addition to a clumsy key image construction. In all privacy protocols that couple 'ledger membership' of inputs with 'ownership/authorization' and 'unspentness', it is impossible to build transactions in a modular fashion. We are stuck building an entire transaction in one pass (or preparing a full tx context before doing a full construction pass).

With Seraphis I am trying to break away from that past common sense. Every piece of the protocol is as loosely coupled as possible. Txos (I call them enotes) can be constructed in isolation (no related tx context). Membership proofs don't need to be constructed until right before a tx is submitted to the ledger (letting you chain transactions together completely off-chain, and/or hide timing information about when a tx started being built). Input proofs of ownership and unspentness can be individually and separately constructed (allowing multiple parties to contribute funds to a tx), are only coupled to the set of outputs (another requirement for tx chaining), and the linking tags (key images) can be proven valid without a membership proof (allowing senders/recipients of funds in an off-chain environment to be fully confident about balance changes). Range proofs and the balance proof can be defined as soon as the set of inputs and outputs are known (another requirement for tx chaining: you should be able to chain off txs that are completely valid within the protocol rules as soon as membership proofs for inputs are added - which can be trivially mocked, letting you easily validate partial txs).

Given the advantages of tx modularity, I really am looking forward to the simplest solution zk circuits can offer - just the membership proof piece. If there are non-trivial advantages to moving other pieces within the circuit (probably just the range proofs, which are the bulk of verification and tx size cost next to membership proofs), then absolutely let's consider it. One step at a time :)

## sethforprivacy | 2022-05-03T12:51:57+00:00
As the conversation is referring to Seraphis quite a bit, just linking the protocol and current code here for reference and clarity:

https://github.com/UkoeHB/Seraphis
https://github.com/UkoeHB/monero/tree/seraphis_lib
https://github.com/UkoeHB/monero/tree/seraphis_perf

## mckibbinusa | 2022-05-08T03:59:43+00:00
Intriguing idea, but is the idea implemented? I read, "zk-SNARKs allow us to move from obfuscating the true spend to truly hiding it, a large step forward in preventing even targeted attacks from building a transaction graph, while doing so in a way that remains trustless and efficient." I am eager to see how one 'hides' the true spend within a deterministic algorithm. Such a method could create vast risks beyond the known and measurable risks of obfuscation outcomes.  

## kayabaNerve | 2022-05-08T05:30:09+00:00
It's not anymore deterministic than rings are. rings used exposed members, randomly selected from a larger subset, and then creates a signature with 11 decoy responses. The actual response then replaces its decoy, itself combined with a random value to prevent private key recovery.

With circuits, every member is exposed, because that's how outputs work. That said, we use every member, not just a subset. Randomness isn't needed here, as it wouldn't be if we created a ring of every single output. Same amount of randomness.

The distinction is there's no decoy responses. "So if I see your actual response and it alone I'll instantly know your actual spend!" Well... no. This is because the response, a variable, is combined with a random value just as regular signatures are. Sure, we eliminate decoys, but the response given looks the same as a response for any other member proof, which is all decoys needed to do (look identical to the actual to hide the actual). Since the actual looks identical to any other actual, and we never actually reveal any of the variables... it works.

Now if you want to ask how we can verify variables we don't know... magic. ZK circuit magic. I honestly can't say I know enough of to sit and write it out at an academic level. I know enough to work with it though and am here to do exactly that.

To provide an extremely basic explanation, every variable is composed of two things. The actual variable and a blinding factor (random value). These are combined via a Pedersen commitment (which we use to hide output amounts). Then, we can provide a proof that for a theoretical variable, it was executed according to this code, and we can verify that because we can provide data constructed from the variables and blinding factors as needed (yet not the actual blinding factors as that would remove the blinds and reveal everything). If we executed different code, the blinding factors wouldn't line up, and...

## baro77 | 2022-05-09T13:30:43+00:00

> 
> ```
> halo2 = plonk arithmetization + bulletproofs polynomial commitment proof
> ```
> 

so does halo2 ultimately rely on Fiat-Shamir heuristic (instead of _legacy SNARKs_' CRS/trusted setup) to gain non-interactiveness?
I'm speaking about things I don't still really know, anyway just to have a bird's-eye view of the whole context, what about any implementation of Groth-Sahai NIZK flavour ?


## kayabaNerve | 2022-05-09T17:45:27+00:00
When discussing implementation into Monero, I'm mainly interested in keeping with the existing technology (Bulletproofs) available rather than distinct systems, especially for the initial circuit we consider deploying. Potentially more efficient systems, such as Halo 2 as a whole, or other systems, seem a bit much given the immediate discussion, and resources, at hand (in my opinion).

## baro77 | 2022-05-10T14:36:32+00:00
@kayabaNerve I understand your point. If your message has been inspired by mine, I have to explain that my question was just to take advantage of @narodnik knowledge about the field (which seems to me the highest here) to sketch the context... 

There's hype about halo2 'cause it doesn't need trusted setup, but if it avoids CRS by use of Fiat-Shamir heuristic it's important to be known because it's weaker than a non-interactiveness by trusted setup under standard assumptions... It's true that Fiat-Shamir it's also used in Schnorr signature and Bulletproof so ROM is an already accepted ideal-model someway, but I asked about Groth-Sahai NIZK flavour because I have read that -if I'm not wrong- it could offer non-interactiveness without trusted setup but under assumption provable in the standard model. 

So let's say I was trying to have an idea of the widespread context, believing it's useful to be more aware of choices and their tradeoffs. That said, you are right that maybe it's a bit much given the purpose of the discussion, I have ventured 'cause anyway there's not a lot of traffic here

## baro77 | 2022-05-19T10:10:18+00:00
BTW I think I have to withdraw my question to narodnik 'cause in my day-by-day learning I think to have understood that Groth-Sahai NIZKs do **not** avoid CRS

## narodnik | 2022-12-31T06:08:45+00:00
Basically gave up on this thread. Not much actual desire to learn or do anything, just make up random excuses. Adding arithmetization on top of the existing bulletproofs for a set inclusion proof is perfectly doable and not difficult. I already linked the 300 line sage script above but nobody actually bothered to look or try to understand.

I'm cross posting a benchmark I shared elsewhere here in case it's useful for people in the future.

```rust
use darkfi::{
    zk::{
        proof::{Proof, ProvingKey, VerifyingKey},
        vm::{Witness, ZkCircuit},
        vm_stack::empty_witnesses,
    },
    zkas::decoder::ZkBinary,
    Result,
};
use darkfi_serial::Encodable;
use darkfi_sdk::{
    crypto::{
        pedersen::pedersen_commitment_u64, poseidon_hash, MerkleNode, PublicKey, SecretKey, TokenId,
        constants::MERKLE_DEPTH, Nullifier
    },
    incrementalmerkletree,
    incrementalmerkletree::{bridgetree::BridgeTree, Hashable, Tree},
    pasta::{
        arithmetic::CurveAffine,
        group::{
            ff::{Field, PrimeField},
            Curve,
        },
        pallas,
    },
};
use halo2_proofs::circuit::Value;
use rand::rngs::OsRng;

type MerkleTree = BridgeTree<MerkleNode, { MERKLE_DEPTH }>;

fn main() -> Result<()> {
    let mut tree = MerkleTree::new(100);

    // Add 10 random things to the tree
    for i in 0..10 {
        let random_leaf = pallas::Base::random(&mut OsRng);
        let node = MerkleNode::from(random_leaf);
        tree.append(&node);
    }

    let leaf = pallas::Base::random(&mut OsRng);
    let node = MerkleNode::from(leaf);
    tree.append(&node);

    let leaf_position = tree.witness().unwrap();

    // Add 10 more random things to the tree
    for i in 0..10 {
        let random_leaf = pallas::Base::random(&mut OsRng);
        let node = MerkleNode::from(random_leaf);
        tree.append(&node);
    }

    let root = tree.root(0).unwrap();

    // Now begin zk proof API

    let bincode = include_bytes!("../proof/inclusion_proof.zk.bin");
    let zkbin = ZkBinary::decode(bincode)?;

    // ======
    // Prover
    // ======
    // Bigger k = more rows, but slower circuit
    // Number of rows is 2^k
    let k = 11;
    println!("k = {}", k);

    // Witness values
    let merkle_path = tree.authentication_path(leaf_position, &root).unwrap();
    let leaf_position: u64 = leaf_position.into();

    let prover_witnesses = vec![
        Witness::Base(Value::known(leaf)),
        Witness::Uint32(Value::known(leaf_position.try_into().unwrap())),
        Witness::MerklePath(Value::known(merkle_path.clone().try_into().unwrap())),
    ];

    // Create the public inputs
    let merkle_root = {
        let position: u64 = leaf_position.into();
        let mut current = MerkleNode::from(leaf);
        for (level, sibling) in merkle_path.iter().enumerate() {
            let level = level as u8;
            current = if position & (1 << level) == 0 {
                MerkleNode::combine(level.into(), &current, sibling)
            } else {
                MerkleNode::combine(level.into(), sibling, &current)
            };
        }
        current
    };

    let public_inputs = vec![leaf, merkle_root.inner()];

    // Create the circuit
    let circuit = ZkCircuit::new(prover_witnesses, zkbin.clone());

    let now = std::time::Instant::now();
    let proving_key = ProvingKey::build(k, &circuit);
    println!("ProvingKey built [{} s]", now.elapsed().as_secs_f64());
    let now = std::time::Instant::now();
    let proof = Proof::create(&proving_key, &[circuit], &public_inputs, &mut OsRng)?;
    println!("Proof created [{} s]", now.elapsed().as_secs_f64());

    // ========
    // Verifier
    // ========

    // Construct empty witnesses
    let verifier_witnesses = empty_witnesses(&zkbin);

    // Create the circuit
    let circuit = ZkCircuit::new(verifier_witnesses, zkbin);

    let now = std::time::Instant::now();
    let verifying_key = VerifyingKey::build(k, &circuit);
    println!("VerifyingKey built [{} s]", now.elapsed().as_secs_f64());
    let now = std::time::Instant::now();
    proof.verify(&verifying_key, &public_inputs)?;
    println!("proof verify [{} s]", now.elapsed().as_secs_f64());

    let mut data = vec![];
    proof.encode(&mut data)?;
    println!("proof size: {}", data.len());

    Ok(())
}
```

```
constant "InclusionProof" {
}

contract "InclusionProof" {
	Base leaf,
	Uint32 leaf_pos,
	MerklePath path,
}

circuit "InclusionProof" {
	constrain_instance(leaf);

	# Merkle root
	root = merkle_root(leaf_pos, path, leaf);
	constrain_instance(root);
}

```

```
k = 11
ProvingKey built [1.393294228 s]
Proof created [1.105254593 s]
VerifyingKey built [1.240241996 s]
proof verify [0.018967216 s]
```

This is using bulletproofs for inner product proof, so there's no trusted setup.
It proves that $leaf has a pathway to $root without revealing the exact path.
Verification takes 0.019 secs and proof size is 6403 bytes.
This tree has a anon size of 2^32, while Seraphis current ring size is 128 and ~800 bytes.
So an 8x proof size increase for 33554432x increase in anonymity set.

It's pretty much just defining a polynomial relation to prove the merkle tree inclusion, then committing to that using the bulletproofs scheme. Given a and b are boolean ints, you can arithmetize them as so:
```
a AND b = ab
a OR b = a + b - ab
NOT a = 1 - a
```
then we convert our algo to that format, and we construct polynomials that interpolate those points, then commit and open it using bulletproofs.

Literally the main critique of monero is anon set size. Imagine if that is solved. then monero would solve the biggest issue, and might become finally a large mcap project if it could pull this off.


## baro77 | 2022-12-31T08:57:17+00:00
thanks for your code and ideas @narodnik !

## kayabaNerve | 2022-12-31T23:11:12+00:00
I have a few comments, and I'm a bit annoyed by the above presentation, so please forgive me for any extraneous snark.

1) I don't believe anyone made up random excuses.

2) A circuit meeting Seraphis's needs must do elliptic point addition in the circuit. It's not feasible to do Ed25519 point addition in a Ed25519 Bulletproof. You need a curve that towers down to Ed25519.

3) There is such a curve. I have a (rather slow) impl and was working on a bellman circuit in my spare time.

4) Dev bandwidth is, as usual, a problem. I have no objection to that point.

5) The above circuit does not do point addition to blind the member. It is a (presumably) valid Merkle tree inclusion proof. While I appreciate the... contribution, it adds nothing to the conversation. It was already known we'd need a merkle tree-based proof. You quickly being able to write one with your SDK and the Halo 2 libs is a great comment on how far this problem has come, yet doesn't contribute to Monero. It fails to exhibit any new contribution to the protocol unless we moved completely over to Halo 2. Else, we have to rewrite all of this tooling, returning to the previous point.

6) We *can* move to Halo 2 by using COPZ's discrete-log equality proof, which would have the cost of BP(+)s + some misc 512-bit arithmetic ops. Prior to COPZ's publication, the DLEq proof took an eighth of a second to verify and was completely infeasible. I'm not sure switching curves is sufficiently beneficial when compared to tower considerations. It'd depend on how much BPs fail to recursive proofs like Halo 2.

7) We can't have a fixed size merkle tree and also need to handle things at that.

8) I believe more efficient constructions than Poseidon have been put forth. While I'm not against Poseidon, I'd want to review options like Reinforced Concrete before building a full impl of anything.

## narodnik | 2023-01-07T07:44:23+00:00
Thanks for your works and commitment to Monero, which is an important service. Monero preserves the original spirit of crypto. I can imagine the frustration of having an outsider come and start being pushy.

Privacy is likely to become a big issue within crypto. The ring size is the achilles heel for Monero, and biggest source of doubt. If it gets fixed, then the project can claim its position within the markets. Otherwise as it stands, the project will leak a lot of value which translates to a smaller shrinking community. It's the time to expand rather than consolidate since an opportunity is beginning to open up ahead, and for the project to succeed it must be ready.

As an alternative, here's some code for curve trees which is an alternative to merkle proofs:

```python
import hashlib
from collections import namedtuple

# Your Funds Are Safu

p = [
    0x40000000000000000000000000000000224698fc094cf91b992d30ed00000001,
    0x40000000000000000000000000000000224698fc0994a8dd8c46eb2100000001
]

# Pallas, Vesta
K = [GF(p_i) for p_i in p]
E = [EllipticCurve(K_i, (0, 5)) for K_i in K]
# Scalar fields
Scalar = [K[1], K[0]]

base_G = [E_i.gens()[0] for E_i in E]
assert all(base_G_i.order() == p_i for p_i, base_G_i in zip(reversed(p), base_G))

E1, E2 = 0, 1

gens = [
    [E[E1].random_point() for _ in range(5)],
    [E[E2].random_point() for _ in range(5)],
]

def hash_nodes(Ei, P1, P2, r):
    G1, G2, G3, G4, H = gens[Ei]

    (P1_x, P1_y), (P2_x, P2_y) = P1.xy(), P2.xy()

    v1G1 = int(P1_x) * G1
    v2G2 = int(P1_y) * G2
    v3G3 = int(P2_x) * G3
    v4G4 = int(P2_y) * G4
    rH   = int(r)    * H

    return v1G1 + v2G2 + v3G3 + v4G4 + rH

def hash_point(Ei, P, b):
    G1, G2, G3, G4, H = gens[Ei]
    x, y = P.xy()
    return int(x)*G1 + int(y)*G2 + int(b)*H

# You can ignore this particular impl.
# Just some rough code to illustrate the main concept.
# The proofs enforce these relations:
#
#   σ ∈ {0, 1}
#   C = x1  G1  + y1  G2 + x2 G3 + y2 G4 + rH
#   Ĉ = x_i G1  + y_i G2                 + bH
#
# where
#
#   x_i = { x0  if  σ = 0
#         { x1  if  σ = 1
#
#   y_i = { y0  if  σ = 0
#         { y1  if  σ = 1
#
# It is just a quick hackjob proof of concept and horribly inefficient
load("curve_tree_proofs.sage")
test_proof()

# Our tree is a height of D=3

def create_tree(C3):
    assert len(C3) == 2**3

    # j = 2
    C2 = []
    for i in range(4):
        C2_i = hash_nodes(E2, C3[2*i], C3[2*i + 1], 0)
        C2.append(C2_i)

    # j = 1
    C1 = []
    for i in range(2):
        C1_i = hash_nodes(E1, C2[2*i], C2[2*i + 1], 0)
        C1.append(C1_i)

    # j = 0 (root)
    C0 = hash_nodes(E2, C1[0], C1[1], 0)
    return C0

def create_path(C3):
    # To make things easier, we assume that our coin is
    # always on the left hand side of the tree.

    X3 = C3[1]
    X2 = hash_nodes(E2, C3[2], C3[3], 0)

    X1 = hash_nodes(
        E1,
        hash_nodes(E2, C3[4], C3[5], 0),
        hash_nodes(E2, C3[6], C3[7], 0),
        0
    )

    return (X3, X2, X1)

def main():
    coins = [E[E1].random_point() for _ in range(2**3)]
    root = create_tree(coins)

    path = create_path(coins)

    # Test the path works
    X3, X2, X1 = path
    C3 = coins[0]
    C2 = hash_nodes(
        E2,
        C3,
        X3,
        0
    )
    C1 = hash_nodes(
        E1,
        C2,
        X2,
        0
    )
    C0 = hash_nodes(
        E2,
        C1,
        X1,
        0
    )
    assert C0 == root

    # E1 point
    C3 = coins[0]

    Ĉ0 = root
    r0 = 0
    # Same as this:
    # Ĉ0 = hash_nodes(E1, C2, X2, 0)

    # j = 1
    b1 = int(Scalar[E2].random_element())
    Ĉ1 = hash_point(E2, C1, b1)

    C1_x, C1_y = C1.xy()
    X1_x, X1_y = X1.xy()

    proof1, public1 = make_proof(
        E2,
        ProofWitness(
            C1_x,
            C1_y,
            X1_x,
            X1_y,
            r0,
            b1,
            0
        )
    )
    public1.C = Ĉ0
    public1.D = Ĉ1

    assert verify_proof(E2, proof1, public1)

    # j = 2

    # Now we know that Ĉ1 is the root of a new subtree
    # But Ĉ1 ∈ E2, whereas we need to produce a blinded
    # Ĉ1 ∈ E1.
    # The reason this system uses curve cycles is because
    # EC arithmetic is efficient to represent.
    # We skip this part so assume these next to lines are
    # part of the previous proof.
    r1 = int(Scalar[E1].random_element())
    Ĉ1 = hash_nodes(E1, C2, X2, r1)
    ################################

    b2 = int(Scalar[E1].random_element())
    Ĉ2 = hash_point(E1, C2, b2)

    C2_x, C2_y = C2.xy()
    X2_x, X2_y = X2.xy()

    proof2, public2 = make_proof(
        E1,
        ProofWitness(
            C2_x,
            C2_y,
            X2_x,
            X2_y,
            r1,
            b2,
            0
        )
    )
    public2.C = Ĉ1
    public2.D = Ĉ2

    assert verify_proof(E1, proof2, public2)

    # j = 3

    # Same as before. We now have a randomized C2
    r2 = int(Scalar[E2].random_element())
    Ĉ2 = hash_nodes(E2, C3, X3, r2)
    #################################

    b3 = int(Scalar[E2].random_element())
    Ĉ3 = hash_point(E2, C3, b3)

    C3_x, C3_y = C3.xy()
    X3_x, X3_y = X3.xy()

    proof3, public3 = make_proof(
        E2,
        ProofWitness(
            C3_x,
            C3_y,
            X3_x,
            X3_y,
            r2,
            b3,
            0
        )
    )
    public3.C = Ĉ2
    public3.D = Ĉ3

    assert verify_proof(E2, proof3, public3)

    # Now just unblind Ĉ3

main()
```

[Check here](https://github.com/darkrenaissance/darkfi/blob/master/script/research/halo/curve_tree.sage) for the code. It works by using a 2 cycle of EC curves where the scalar field is the base field of each one. There are a number of simple curves with this property. This enables fast EC calculation inside ZK, so you'd still need a bulletproofs circuit. Check the code comments for more info.

## spirobel | 2023-02-08T17:41:54+00:00
@narodnik 

>Privacy is likely to become a big issue within crypto. The ring size is the achilles heel for Monero, and biggest source of doubt. If it gets fixed, then the project can claim its position within the markets. Otherwise as it stands, the project will leak a lot of value which translates to a smaller shrinking community. It's the time to expand rather than consolidate since an opportunity is beginning to open up ahead, and for the project to succeed it must be ready.

I very much agree with this!

In this issue about tx_extra @tevador mentioned some doubts about the benefits of switching to a system like the one you are proposing: 

>As I said earlier, the problems caused by transaction non-uniformity cannot be fully solved just by a better membership proof.

>See: https://github.com/zcash/zcash/issues/4332

https://github.com/monero-project/monero/issues/6668#issuecomment-1422925066
Can you maybe respond to some of these doubts? It seems like there are these  input arity correlation attacks against Zcash. Are there more attacks like this? what could be done about them?

@tevador is currently focused on adding aesthetic changes to tx_extra to increase transaction uniformity. But this seems like a dead end.

How would your solution help with transaction uniformity?
would it solve the problem?

Thank you very much for your help! 

## kayabaNerve | 2023-02-08T19:47:26+00:00
jberman has requested I submit a comprehensive hand-off level write-up on this for a few weeks, and we had a discussion today cementing some details. This is completely unrelated, in timing and content, to the above post.

# Why

A complete membership proof:
- Removes all statistical analysis on the selected group
- Massively simplifies wallet development by no longer needing decoy selection algorithms
- Prevents bad wallets from differentiating themselves by using distinct algorithms

# Requiremenets

For an arbitrary point, prove its existence in some set and output it +xG, for some x and some generator G.

# Options

### Curve Trees

> For a concrete instantiation targeting 128 bits of security we obtain: a commitment to a set of \textit{any} size is 256 bits; for |S| = 2^40  a zero-knowledge membership proof is 3KB, its proving takes 2s and its verification 40ms on an ordinary laptop.

These would require a curve cycle.

### Halo 2

Halo 2, by the ECC, uses a curve cycle to create recursive proofs. It builds on top of the work of several contributions to the space, such as Bulletproofs.

> The time for verifying an individual transaction on a single thread is around 30ms,

I'm unsure on how valid the comparison between this 30ms and the Curve Trees 40ms is. I'd assume the later is heavily optimized and the former was a proof of concept, yet I cannot say for certain. Please note Zcash transactions have one collective proof for all inputs and outputs, distinct forom Seraphis's design, yet signifying the membership portion would be a fraction of the time benchmarked here.

### Bulletproofs++

We can continue using Bulletproofs, more specifically Bulletproofs++, which has the same prover complexity as verifier complexity. This is feasible by doing a proof over bulletproof25519, a curve whose scalar field is equivalent to Ed25519's field element field. This allows efficiently proving about Ed25519 points within a SNARK.

# Current work

https://github.com/kayabaNerve/serai/tree/tony contains an implementation of bulletproof25519, with no optimizations to the point it's horrendously slow. It also contains work on a circuit which does blind a point (and hashes it, yet I did not yet create a tree for merkle membership). It still needs:

- An efficient bulletprof25519 impl
- A BP++ impl
- An efficient hash (currently it uses a non-arithmetic hash)
- Potentially to be moved from bellman to arkworks, which seems to be the current best library for building circuits
- A complete circuit

# On the necessity of a curve cycle

Without a curve cycle, we risk always having solutions equal to prove as to verify. Not only is this a massive DoS conceern, it's a fundamental lack of scalability. With a curve cycle, we have multiple paths towards logarithmically performant solutions. While, for now, we can trade blows with solutions based on curve cycles, we will be fundamentally held back by our own inability to adopt such solutions. It's arguably already too late for Monero to argue practical performance benefits.

# Options to move forward

### Move Seraphis to secp256k1 or pallas (vesta?)

With COPZ's cross-group discrete logarithm equality proof, we can move curves for just over the current cost of a bulletproof. This would require:

- A library for the curve we move to
- An implementation of COPZ's DLEq proof
- Redoing existing work on Seraphis to be over the new curve

With this, we have the benefit of obtaining a curve without torsion.

### Fund discovery of a curve cycle for Ed25519

We can hope there will eventually be a Ed25519 cycle. While this sticks us with Ed25519, which annoyingly has torsion, it is possible. I'd argue this should be done as soon as possible if we're unwilling to move. That way, we can know if a curve cycle is available and we aren't either dooming ourselves or necessitating yet another migration in the future.

### Accept likely long-term inferiority

We can accept a lack of cycle, either hoping for logarithmic non-cycle solutions, or just accepting the tower. The current work, premised on a tower, should be moved forward with in this case as our best bet. I'd ask who is able to successfully optimize the low-level arithmetic, and then further discuss hiring Sarang via CypherStack to work on a BP++ implementation. I'd also explicitly argue on maintaining it being in Rust, as almost all modern ZK-circuit work is, calling it foolish to rewrite everything in C++. This would officially make Monero a bilingual project.

# Actual next steps

I'd like to call for discussions on moving to a cycle with Seraphis and ask if the Monero project will accept Rust membership proofs in the larger C++ project. I'd note Zcash has long used Rust libraries (librustzcash, which has all their ZK code) in their Bitcoin fork.  Depending on how those go, I'd like to discuss finding a cycle for Ed25519 and having someone else continue working on the towering Bulletproofs++ possibility, yet I'd note that isn't urgent. Only either deciding to move curves, or deciding to commit to Ed25519 despite the potential lack of cycle, is urgent.

## tevador | 2023-02-08T21:54:16+00:00
The biggest issue with moving to another curve would be the required migration of amount commitments (in order to prove that transactions balance out).

Any transaction spending RingCT e-notes (and producing Seraphis e-notes) would need to include:

1. ed25519 "pseudoOut" key `C_1`, which is the masked commitment (used in CLSAG)
1. pallas "pseudoOut" key `C_2`, which would be used for the balance proof
1. a proof that `C_1` and `C_2` contain the same amount

The proof would presumably be done using the algorithm described in this paper: https://eprint.iacr.org/2022/1593.pdf
We'd have to use the parameter `b_x = 64` and the proof size would be roughly 100 bytes per spent e-note.

For Jamtis addresses, we could keep X25519 for the Diffie-Hellman exchange as it's completely unrelated to the output key group.

Overall, I think it would be feasible. Seraphis is probably the only time when we could afford to do this since we are already changing the address format.





## kayabaNerve | 2023-02-08T22:50:36+00:00
Regarding COPZ, we do have the pleasure of having already proved the commitments are in-range (hence why the actual proof is so small, at just 100 bytes or so).

## kayabaNerve | 2023-02-09T01:46:42+00:00
It's not possible to find a cycle.

https://arxiv.org/pdf/1803.02067.pdf#page17

> Hence for any 2-cycle with nontrivial cofactors, the elliptic curves must have small orders.

Specifically, no curve may exist with a cofactor, which isn't 1, in a 2-cycle uncless the order is <= 48.

I'm officially recommending moving Seraphis to be premised on pallas, which has a known cycle with vesta as documented here: https://github.com/zcash/pasta/

We could also use the tweedle{dee, dum} cycle, documented here: https://github.com/daira/tweedle, yet it's inferior, as documented here: https://electriccoin.co/blog/the-pasta-curves-for-halo-2-and-beyond/

The only other option would be sec{p, q}256k1. They have inferior arithmetic, and it'd increase point representations by 3%.

I'd also note many projects which have adopted pallas/vesta, from Darkfi (whose developers have commented here) to Mina.

Without this move, I do not believe we will ever achieve complete membership proofs. We will always fight with decoy selection algorithms, p2pool outputs, spam outputs from malicious adversaries, and doxxed outputs. If we do not make this move now, we force migrating yet again in just a few years, if we aim to stay meaningful.

We can either re-impl pallas in C++ or finally add Rust to Monero. I vote the latter, since almost all modern arithmetic circuit tooling is in Rust, and I believe we may have a majority of new crypto being written in Rust as well. It'd also decrease our development scope by not requiring doing an entirely new curve library.

## dan-da | 2023-02-09T02:59:37+00:00
> or finally add Rust to Monero. I vote the latter

+1

## tevador | 2023-02-10T14:58:06+00:00
> I'm officially recommending moving Seraphis to be premised on pallas, which has a known cycle with vesta as documented here

Do we need the other properties of Pallas/Vesta besides the cycle?

Specifically (quoted from [here](https://electriccoin.co/blog/the-pasta-curves-for-halo-2-and-beyond/)):

> They are designed to be highly 2-adic, meaning that a large power-of-two multiplicative subgroup exists in each field. This is important for the performance of polynomial arithmetic over their scalar fields and is essential for protocols similar to [PLONK](https://eprint.iacr.org/2019/953).

> Unlike with the Tweedle curves, both Pallas and Vesta have low-degree [isogenies](https://www.johndcook.com/blog/2019/04/21/what-is-an-isogeny/) (both of degree 3) from curves with a nonzero j-invariant. This is [useful](https://eprint.iacr.org/2019/403.pdf) when hashing to the curve using the “[simplified SWU](https://www.ietf.org/archive/id/draft-irtf-cfrg-hash-to-curve-10.html#name-simplified-swu-for-ab-0-2)” algorithm, and perhaps for other not-yet-known purposes.

If they are not needed, we might be able to find a better curve cycle for Monero. It's advisable to avoid unnecessary properties that can facilitate future attacks against the curves.


## tevador | 2023-02-10T18:14:00+00:00
Here is a curve cycle I found:

```
Curve Ep: y^2 = x^3 + 6 mod p with order q
Curve Eq: y^2 = x^3 + 6 mod q with order p
  p = 0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff942f
  q = 0x7fffffffffffffffffffffffffffffff92c36c8a4337bf923f29c63bdf7fee15
Ep security = 126.5 bits, embedding degree = (q-1)/1
Eq security = 126.5 bits, embedding degree = (p-1)/1
```

Both curves have a CM endomorphism to speed up scalar multiplication.

A big advantage is that `p = 2^255 - 27601`, which enables a very efficient modular reduction on curve `Ep`, improving the performance of curve operations on the application layer (i.e. faster signatures and range proofs). Large parts of the optimized x86 assembly code for Curve25519 could probably be reused just by changing the constants `19` and `38` to `27601` and `55202`.

Unlike sec{p,q}256k1, compressed points with the above curves fit into 32 bytes.

## kayabaNerve | 2023-02-10T23:32:28+00:00
Advantages to using pallas:

- Existing library
- Existing security review
- Known performance benefits (2-acidity)
- Industry adoption (which becomes beneficial to Monero since multiple hardware wallets are already integrating pallas)
- Existing trustless proof systems built around it (in the future, potentially less scope on our end)
- 2-adicity, creating efficient multiplicative subgroups. PLONK, one of the state of the art ZK systems, is premised on these, as is Halo 2 and HyperPlonk.

I have no personal objection to using another cycle *which has its merit argued*. That means, not only finding a cycle, yet also redoing the security analysis. My only, personal, concern from there is the performance. While it'd be nice to hear we don't need to help HW wallets with the curve, just the proofs on top, that isn't as critical for me as I'm sure we'd work through it eventually.

I will note my personal goals, beyond security:
- Lack of a cofactor
- Fits within 32-bytes without trickery (only allowing even points)

Regarding 2-adicity, we can dismiss PLONK-ish protocols as an option without it. While the original Halo wasn't premised on what PLONK contributed, Halo 2 would more than make up for any performance lost by not having a small difference (`p = 2^255 - 27601`). Then again, another new proof may come out which doesn't care for multiplicative subgroups, in which case the general performance gain of a small difference would show its benefit.

Personally, believing in the long term, I'd rather ensure we support the current state of the art. Not having 2-adicity is either limiting ourselves or gambling on the current state of the art being deprecated for different fundamental techniques. While that's inevitable, sure, I'm unsure exactly how long it'll take before this is deprecated. When it is, who knows what will then be beneficial and how the curves shake out. I don't personally care to see weeks of work go into review/debate just to move which side of the coin flip we're on.

This was discussed on Matrix and my personal summary is this post. I have been asked to benchmark pallas vs secp256k1, the latter being considered comparable to tevador's cycle by tevador, for more context. I will include those numbers here once I have them.

## tevador | 2023-02-11T10:57:51+00:00
If we found a faster 2-adic curve cycle, would that make a difference? Or is pallas pretty much the only choice for Seraphis because it's the "industry standard"?

## kayabaNerve | 2023-02-11T17:39:12+00:00
> I have no personal objection to using another cycle which has its merit argued. That means, not only finding a cycle, yet also redoing the security analysis. My only, personal, concern from there is the performance. 

If you can find an improvement on pallas, I'd have no issue deploying it :)

EDIT: To be clear, I'm willing to drop arguments for pallas on the fact it's an "industry standard". If there's an improvement, which may or may not require being 2-adic (it's a debate to have), and we have the development resources to put behind a curve library for it, I'd be happy to deploy it. I'm willing to drop the arguments on existing tooling around pallas, as per future considerations, so long as we have the parts relevant now.

## tevador | 2023-02-13T21:02:49+00:00
I did some more research and I have to conclude that it's impossible to find a 2-adic cycle with the additional condition that `p = 2^255 - c` for `c < 2^64`, which would give a performance advantage.

The method used by Zcash doesn't work because it requires finding integer constants `v` and `k` such that:

```
2^191 - 1 = 3*v^2 + 9*k^2
```

Since the left side is not divisible by 3, there are no solutions.

A bruteforce search is unlikely to turn up anything as there are only ~20 million primes in the range and the chance that some of the resulting curves has a prime order `q = 1 mod 2^32` is vanishingly small.



## tevador | 2023-02-16T18:11:45+00:00
Besides Crandall primes in the form of `2^x-c` for small `c`, there are also "Montgomery-friendly" primes that have a form of `a*2^x+1` for small or sparse `a`. These primes allow faster reduction in the Montgomery form [1].

The advantage of these primes is that the 2-adicity requirement does not reduce the search space. In fact, 2-adicity is implied.

I found the following curve cycle:

```
Curve Ep: y^2 = x^3 + 278 mod p with order q
Curve Eq: y^2 = x^3 + 278 mod q with order p
  p = 0x5eca430000000000000000000000000000000000000000000000000000000001
  q = 0x5eca43000000000000000000000000010dd00000000000000000000000000001
Ep security = 126.3 bits, embedding degree = (q-1)/4
Eq security = 126.3 bits, embedding degree = (p-1)/4
Ep twist security = 108.8 bits
Eq twist security = 32.7 bits
```

Compared to the Pasta curves:

#### Advantages:
- `p` equals `6212163 * 2^232 + 1`, which is a "Montgomery-friendly" prime, allowing faster modular reduction on both 32-bit and 64-bit machines. This speeds up all curve operations on curve Ep.
- ~`p` has a 2-adicity of 232, allowing much faster square root calculation [2], which speeds up point decompression~
- both curves have 2-adicity at least 112 so they can in theory support more complex circuits than the Pasta curves (which have 2-adicity of 32)
- Ep has twist security >100 bits, which is a tiny advantage compared to Pallas (if we decide to use Pallas as the primary curve - Vesta has >100 bits of twist security)

#### Disadvantages:
- "non-standard"
- primes are not near a power of 2, so generating unbiased scalars requires a little bit more work
- each curve has a different 2-adicity, making the implementation slightly more complex

I will probably try to implement the reduction algorithm from ref. [1] to measure the performance advantage compared to Pallas. In any case, I think this is a viable alternative.

[1] https://eprint.iacr.org/2020/665.pdf
[2] https://eprint.iacr.org/2020/1407.pdf

## DarkWingMcQuack | 2023-02-16T20:11:21+00:00
Let me play devil's advocat here for one second.
Is there a way in which @tevador can propose a curve cycle which is not secure, but it is almost impossible for the rest to check this?

EDIT: same question holds for Pasta curves i guess

## UkoeHB | 2023-02-16T20:49:15+00:00
@DarkWingMcQuack not necessarily, although you may want to read Bernstein and Lange's thoughts on [rigidity](https://safecurves.cr.yp.to/rigid.html).

## tevador | 2023-02-16T21:36:40+00:00
@DarkWingMcQuack Both Pallas/Vesta and my cycle were found by the same script. You can check [my changes](https://github.com/tevador/pasta/commit/948d0f3923eb8cde56c758997a95b46d085b3eb1) and see that there is nothing malicious there.

You can reproduce my cycle by running the script as:

```
sage amicable.sage --sequential --requireisos --ignoretwist --anyeqn --montgomery 255 112
```
It's the first cycle found.

Likewise, Pallas/Vesta can be reproduced by running:

```
sage amicable.sage --sequential --requireisos --sortpq --ignoretwist --nearpowerof2 255 32
```

## kayabaNerve | 2023-02-17T05:16:01+00:00
> Ep twist security = 108.8 bits
Eq twist security = 32.7 bits

I know pallas is less than 100, yet can you comment what it is exactly? I'm not sure twist security matters at all for our use case to be honest, yet it'd be good know if pallas also sucks, yet cleared review, or if pallas was just under 100 (so still generally infeasible).

> primes are not near a power of 2, so generating unbiased scalars requires a little bit more work

I believe Seraphis is already doing a 512-bit wide reduction which should be sane here as well.

> each curve has a different 2-adicity, making the implementation slightly more complex

There is a development effort to be done if this is the curve we want to move to.

---

I'll have to run some tooling to evaluate this myself, and I also want to reach out to some communities. Thanks for finding this, tevador. If this is legitimately more performant, and passes scrutiny, I'm up for it.

I'll note regarding your second cited source, it has a complexity of O(n^1.5). These curves have a n of 232. Pallas's n is 32. While having more subgroups enables rows in PLONKed arithmetic, I'm unsure that's beneficial here as 32 subgroups seems sufficient.

Pallas/Vesta brag about supporting the GLV endomorphism. Does that apply here (or some other, similarly/more efficient option)? It sounds like GLV *was* quite specific in how it could be applied, yet this has since widened: https://www.iacr.org/archive/eurocrypt2009/54790519/54790519.pdf

The final notable claim from pasta is:

> Both fields do not have 5-order, 7-order, etc. multiplicative subgroups, so that exponentiation by these small primes is a permutation — a crucial requirement for algebraic hash functions such as Rescue and Poseidon.

Do these curves have any such subgroups?

## tevador | 2023-02-17T09:00:05+00:00
> I know pallas is less than 100, yet can you comment what it is exactly? I'm not sure twist security matters at all for our use case to be honest, yet it'd be good know if pallas also sucks, yet cleared review, or if pallas was just under 100 (so still generally infeasible).

Pallas has a twist security of 86.7 bits. I agree that twist security is probably meaningless for us (unless we decide for some reason to use the curve for DH, which would not be a good idea). But it's prescribed by SafeCurves, so some people care about it.

> I'll note regarding your second cited source, it has a complexity of O(n^1.5). These curves have a n of 232. Pallas's n is 32.

I admit I haven't read the second paper in detail. I was going by a statement from the zcash blog post that claims 2-adicity "may assist in square root performance". If the algorithm is O(n^1.5) then it might actually be slower, which is unfortunate and may negate the other performance benefits.

> I'm unsure that's beneficial here as 32 subgroups seems sufficient.

I also couldn't find any information about what specific 2-adicity is required for PLONK and the limitations implied. But nevertheless, this curve cycle should work at least as well as Pasta.

> Pallas/Vesta brag about supporting the GLV endomorphism. Does that apply here (or some other, similarly/more efficient option)?

Yes, my curves have the same CM endomorphism as Pallas/Vesta. The zcash script only finds such curves.

> Do these curves have any such subgroups?

```
gcd(p-1, α) = 1 for α ∊ {5, 7, 11, 13, 17}
gcd(q-1, α) = 1 for α ∊ {7, 11, 13, 17}
```

So the only difference from Pasta is that `q-1` is divisible by 5, but I don't think it's a problem since there will be other small primes that work if more than 4 permutations are needed (the zcash script only checks 5, 7, 11, 13, 17).


## kayabaNerve | 2023-02-18T03:35:18+00:00
@tevador The multisig is premised on DH, which koe reminded me of recently (though I'm unsure they intended to point it out re: twist). That arguably means we should use your Ep/vesta, not pallas, except I don't think twist security matters regardless since we use compressed points, which are guaranteed to be on-curve or error. If it does, I heave to learn why pallas was chosen over vesta in the first place. While the DH multisig sucks anyways, I don't immediately care to posit rewriting it.

> this curve cycle should work at least as well as Pasta.

Agreed.

> Yes, my curves have the same CM endomorphism as Pallas/Vesta. The zcash script only finds such curves.

Great :) Just checking.

> So the only difference from Pasta is that q-1 is divisible by 5, but I don't think it's a problem since there will be other small primes that work if more than 4 permutations are needed (the zcash script only checks 5, 7, 11, 13, 17).

The Poseidon pre-print defines its s-boxes as the smallest possible gcd which = 1. It prefers 3/5, and instantiates most crypt-analysis against 5, per page 6 of https://eprint.iacr.org/2019/458.pdf. 7 should still be fine? Yet I'm unsure how it impacts performance.

I will note Poseidon is one of the top algebraic hashes. While there is a faster option from 2021, Reinforced Concrete,, it explicitly requires gcd(p, 5) = 1. Page 5, section 4.1 https://eprint.iacr.org/2021/1038.pdf.

So I'm unsure the performance of these when used in circuits, whose priority can be debated, and then immediately there's practical items such as O(n^1.5).

## tevador | 2023-02-18T14:14:04+00:00
I'm naming the new curves Vega and Deneb for easier referencing.

To get a clear picture about the performance of the involved curves, I implemented a benchmark for modular multiplication and squaring in assembly (to remove compiler effects).

https://github.com/tevador/ec-bench

Here are the results on my laptop, in nanoseconds per operation:

| Curve   | Prime    | `fe_mul` | `fe_sqr` |
|---------|----------|----------|----------|
| Ed25519 | 2^255-19 |  11.03   |   9.62   |
| Pallas  | 2^254 + 45560315531419706090280762371685220353 | 16.80 | 15.26 |
| Vega    | 6212163 * 2^232 + 1 | 10.59 | 9.30 |

Note that Pallas is at least 50% slower than both Ed25519 and Vega.

To understand why, you can see the modular reduction code for the three primes:

Ed25519: https://github.com/tevador/ec-bench/blob/master/src/fe_mul_ed25519.inc#L72-L98
Pallas: https://github.com/tevador/ec-bench/blob/master/src/fe_mul_pallas.inc#L72-L166
Vega: https://github.com/tevador/ec-bench/blob/master/src/fe_mul_vega.inc#L72-L114

For Pallas, the modular reduction actually takes longer than the multiplication itself. I compared my reduction code with the [zcash rust repo](https://github.com/zcash/pasta_curves/blob/main/src/fields/fp.rs#L356-L385) and they match closely. Modular reduction for general-form primes is just that slow.

Ed25519 and Vega both use special-form primes with much faster reduction. The Mongomery reduction for Vega is slightly faster because it has 4 (nearly) independent carry chains, while Ed25519 slightly stalls on the carry propagation.

These are not all field operations, but elliptic curves involve mostly modular multiplication and squaring (plus a few additions). For Pallas and Vega, the curve performance will be proportional to their field performance since both are short Weierstrass curves using the same formulas. Ed25519 is a twisted Edwards curve, which has slightly faster formulas for the group law.

We can estimate the curve performance using the most efficient formulas from the [Explicit-Formulas Database](https://hyperelliptic.org/EFD/index.html).

| Curve   | addition | doubling | addition ns/op | doubling ns/op |
|---------|----------|----------|----------------|----------------|
| Ed25519 |    8M    | 4M + 4S  |     ~90        |       ~80      |
| Pallas  | 11M + 5S | 2M + 5S  |    ~260        |      ~110      |
| Vega    | 11M + 5S | 2M + 5S  |    ~160        |       ~70      |

One thing to note is that both Pallas and Vega have a GLV endomophism that can reduce the number of additions and doublings needed for scalar multiplication. More benchmarks would be needed to assess that but it's clear that **Pallas is approximately 50% slower than Vega for all curve operations**.


## tevador | 2023-02-18T14:19:29+00:00
> immediately there's practical items such as O(n^1.5)

It seems that for large n there are better algorithms that scale as O(n), such as the [Cipolla's algorithm](https://en.wikipedia.org/wiki/Cipolla%27s_algorithm), but it would require more benchmarks to see the real world performance difference for point decompression.

## kayabaNerve | 2023-02-18T14:25:10+00:00
I'll be happy to solicit feedback, and I'll do my own review on its security (running tooling myself to evaluate criteria, obviously not an expert). Thanks for finding these :D

## tevador | 2023-02-18T15:58:11+00:00
> I will note Poseidon is one of the top algebraic hashes. While there is a faster option from 2021, Reinforced Concrete,, it explicitly requires gcd(p, 5) = 1

There is another curve cycle that satisfies both `gcd(p-1, 5) = 1` and `gcd(q-1, 5) = 1`, but the curves don't have isogenies. If using Poseidon is more important than isogenies, we could instead use this cycle. It would be equally fast (it has `p=27488187*2^230+1`) and twist security is 102.3 bits.

## kayabaNerve | 2023-02-19T08:50:57+00:00
Two questions as I work on my review.

1) How long should it take to recreate the curve with the above specified params? Few hours or a few days?

2) Did you have the x0/x1/y0/y1 values for each curve I can run verify.sage with? I *believe* this should be the generator, where convention would either be some hash or the lowest valid set of coordinates. I'm sure I can grab one myself, just figured you may have it handy.

## tevador | 2023-02-19T10:00:52+00:00
> How long should it take to recreate the curve with the above specified params? Few hours or a few days?

I'm not sure what exactly you mean, but you can clone my repo:

https://github.com/tevador/pasta

and run

```
sage amicable.sage --sequential --ignoretwist --anyeqn --montgomery 255 112
```

In about 15 minutes, it will find a total of 3 cycles:

1. `y^2 = x^3 + 97` with `p=27488187*2^230+1`. This cycle has both `gcd(p-1,5)=1` and `gcd(q-1,5)=1`. Ep has twist security of 102.3 bits. There are no isogenies.
2. `y^2 = x^3 + 278` with `p=6212163*2^232+1`. This is the cycle mentioned above. It has `gcd(p-1,5)=1` but `gcd(q-1,5)≠1`. Ep has twist security 108.8 and both curves have isogenies.
3. `y^2 = x^3 + 74` with `p=299340363*2^226+1`. This cycle has both `gcd(p-1,5)=1` and `gcd(q-1,5)=1`. Ep has twist security of only 50.4 bits. Both curves have isogenies.

Since we require twist security on Ep, we can decide between cycle 1 and 2 depending on the importance of having `gcd(q-1,5)=1` or having isogenies.

> Did you have the x0/x1/y0/y1 values for each curve I can run verify.sage with? I believe this should be the generator

You can choose any point on the curve for the generator, but the convention is to find the point with the smallest value of `x`. I haven't tried that yet.

## kayabaNerve | 2023-02-19T10:06:30+00:00
Ah. Thanks for the link to your own repo. I missed that and was running on zcash's with your prior commented discovery command, which I now see is distinct.

Also yes, I was asking for the answer of "15 minutes".

## tevador | 2023-02-19T10:12:48+00:00
Yeah, the `--anyeqn --montgomery` commands are specific to my repo. The zcash script will ignore these options and likely won't find anything.

## tevador | 2023-02-19T11:08:11+00:00
> `y^2 = x^3 + 97`

Btw, this equation has a non-modular solution of `x=18, y=77`, so if we use this cycle, I'd recommend using this as the base point because then we could have the same base point on both curves.

## tevador | 2023-02-20T08:39:29+00:00
> Since we require twist security on Ep, we can decide between cycle 1 and 2 depending on the importance of having `gcd(q-1,5)=1` or having isogenies.

Isogenies are needed only for efficient hashing onto the curve. I don't think it is needed for our use case (Seraphis has a different key image construction that doesn't invove hashing). Can someone confirm that hash-to-point is not needed for the Merkle tree proof? Note that without isogenies, hashing onto the curve is still possible, just slower.

It would be nice to be able to use Reinforced Concrete for the Merkle tree proof. Can someone confirm we need both `gcd(p-1,5)=1` and `gcd(q-1,5)=1` for this?

If the above hypotheses are confirmed, I would suggest using the first cycle with the equation `y^2 = x^3 + 97`.


## kayabaNerve | 2023-02-20T18:02:20+00:00
From my immediate understanding, algebraic hashes are needed, the only hash to points needed are as parameters (similar to H/Bulletproofs).

ReinforcedConcrete's Bricks function is written a degree 5 polynomial where gcd(p - 1, 5) = 1. They do not describe that as being variable nor say that security analysis holds when it's distinct. Ideally, we only use one hash, yet it may theoretically be possible to use RC on one curve and Poseidon on another?

I'll double check on the usage of hash to point. What's the 2-adicities of the first one?

## tevador | 2023-02-20T18:49:37+00:00
> the only hash to points needed are as parameters

We don't need a fast hash for these as it's a one-off thing.

> Ideally, we only use one hash, yet it may theoretically be possible to use RC on one curve and Poseidon on another?

My main question was if both fields need the hash. The Merkle tree only contains points from one curve (the "application" curve where the output keys live).

RC claims to be 15x faster than Poseidon, so it would presumably be beneficial if we can use it.

> What's the 2-adicities of the first one?

```
p   = 0x68dbeec000000000000000000000000000000000000000000000000000000001 (bitlength 255, weight 18, 2-adicity 230)
q   = 0x68dbeec00000000000000000000000011bc80000000000000000000000000001 (bitlength 255, weight 26, 2-adicity 115)
```

## kayabaNerve | 2023-02-20T21:13:20+00:00
> We don't need a fast hash for these as it's a one-off thing.

Agreed.

> My main question was if both fields need the hash. The Merkle tree only contains points from one curve (the "application" curve where the output keys live).

Curve trees has both curves perform hashes. They both need *a* hash. While we could likely do RC on one, and Poseidon on the other, we obviously would be best of simply having a curve which RC works for both. That'd be 1 or 3.

## tevador | 2023-02-20T22:01:52+00:00
We have a classic case of "pick 2 options out of 3".

Cycle 1 has: twist security, gcd(q-1,5)=1
Cycle 2 has: twist security, isogenies
Cycle 3 has: gcd(q-1,5)=1, isogenies

I think isogenies are the least useful option for us, so cycle 1 should be the best choice. If you can confirm that we don't need a fast hash-to-curve function, I will start implementing cycle 1.

## kayabaNerve | 2023-02-21T08:17:27+00:00
We can eliminate curve 2. I hope to provide my opinion on hash to curve, and put forth my own comment on security, within two days.

## DarkWingMcQuack | 2023-02-21T15:58:22+00:00
Is it possible to bruteforce a "perfect" curve?
If so, i have lots of computing power at hand which i could use to search for such a curve cycle.

## sethforprivacy | 2023-02-21T16:20:31+00:00
I won't pretend I understand pretty much anything being discussed in here recently, but just wanted to say thank you to @kayabaNerve and @tevador for diving in and trying to make some headway here!

IMO a move to a complete membership proof instead of ring signatures would be the single most needed and most impactful move for the Monero community to make, enabling Monero to both retain it's share of usage among privacy coins and to ensure that all users are protected as much as possible, even against targeted attacks.

As we move into a more and more adversarial environment, the relatively problematic ring signature approach will lead to more and more issues, so I'm happy to see this gaining traction.

## tevador | 2023-02-22T09:08:35+00:00
> Is it possible to bruteforce a "perfect" curve?
> If so, i have lots of computing power at hand which i could use to search for such a curve cycle.

I updated my script to do an exhaustive search and found two additional cycles with `p = c * 2^x + 1` where `c < 2^32`. Both of these cycles have `gcd(q-1,5)=1` and isogenies, but their twist security is poor, so they are equivalent to cycle 3 above.

"Cycle 4"
```
p   = 0x71b50f0300000000000000000000000000000000000000000000000000000001 (bitlength 255, weight 16, 2-adicity 224)
q   = 0x71b50f0300000000000000000000000127830000000000000000000000000001 (bitlength 255, weight 24, 2-adicity 112)
Ep/Fp : y^2 = x^3 + 284
Eq/Fq : y^2 = x^3 + 284
gcd(p-1, α) = 1 for α ∊ {5, 7, 11, 13, 17}
gcd(q-1, α) = 1 for α ∊ {5, 11, 13, 17}
Ep security = 126.4, embedding degree = (q-1)/32
Eq security = 126.4, embedding degree = (p-1)/2
Ep twist security = 56.7
Eq twist security = 33.2
```

"Cycle 5"
```
p   = 0x7410694b00000000000000000000000000000000000000000000000000000001 (bitlength 255, weight 14, 2-adicity 224)
q   = 0x7410694afffffffffffffffffffffffed5710000000000000000000000000001 (bitlength 255, weight 117, 2-adicity 112)
Ep/Fp : y^2 = x^3 + 41
Eq/Fq : y^2 = x^3 + 41
gcd(p-1, α) = 1 for α ∊ {5, 7, 11, 13, 17}
gcd(q-1, α) = 1 for α ∊ {5, 11, 13, 17}
Ep security = 126.5, embedding degree = (q-1)/2
Eq security = 126.5, embedding degree = (p-1)/146
Ep twist security = 62.8
Eq twist security = 55.8
```

While we could technically continue the search for `c >= 2^32`, there would be performance impact on some systems (slower modular reduction).

I'm still running a search for 254-bit primes (all the cycles mentioned so far are 255-bit), but it's likely that there are no "perfect" curves and we will have to make compromises (either dropping some requirements or accepting a slower curve).

## tevador | 2023-02-22T16:07:15+00:00
FYI, I searched all primes of 240-254 bits that would provide a general speed-up and found no other useful cycles.



## tevador | 2023-02-24T16:11:39+00:00
https://github.com/monero-project/research-lab/issues/100#issuecomment-1423154798

> ### Fund discovery of a curve cycle for Ed25519
> We can hope there will eventually be a Ed25519 cycle. While this sticks us with Ed25519, which annoyingly has torsion, it is possible. I'd argue this should be done as soon as possible if we're unwilling to move. That way, we can know if a curve cycle is available and we aren't either dooming ourselves or necessitating yet another migration in the future.

> It's not possible to find a cycle.

While there cannot be a direct cycle with Ed25519, there can be an indirect cycle that requires going through an intermediate curve:

```
                    ---->----
                   /         \
Ed25519 -> Er -> Eq           Ep
                   \         /
                    ----<----
```

Here `Er`, `Ep` and `Eq` are three new curves such that:

1. `Er` is defined over `GF(p)` and contains a subgroup with order 2^255-19 (its scalar field has the same size as the Ed25519 base field).
2. `Eq` is defined over `GF(q)` and has order `p` (i.e. its scalar field has the same size as the `Er` base field)
3. `Ep` is defined over `GF(p)` and has order `q` (i.e. it forms a cycle with `Eq`).

These curves exist:

```
Curve Er: y^2 = x^3 + 4 mod p with order h*(2^255-19)
Curve Ep: y^2 = x^3 + 14 mod p with order q
Curve Eq: y^2 = x^3 + 14 mod q with order p
  h = 1407
  p = 0x2bf8000000000000000000000000000003053b33f6622b8802b5c85a5af1dadc389
  q = 0x2bf80000000000000000000000000000060a7667ecc45710056b90b4b5e3b5bef81
```

This could be a backup solution in case we decided to stick with Ed25519 for whatever reason. The three new curves would be used solely in the membership proof, which could be implemented with Curve Trees using the cycle `Ep`/`Eq` with an additional point blinding proof over the curve `Er`.

While this would be much more efficient than the Bulletproofs solution, there are major drawbacks compared to a native cycle:

* The curves in the indirect cycle cannot have a high 2-adicity, which rules out PLONK and related protocols.
* There is an additional inefficiency due to the intermediate curve and the related proofs.
* The curves use 266-bit fields, so they would be about 2x slower and the public keys would require 34 bytes instead of 32.


## UkoeHB | 2023-02-24T23:46:17+00:00
@tevador is there a reason you need three curves? Why not just go directly from `Ed25519` to `Ep`?

## tevador | 2023-02-25T11:07:50+00:00
Going from `Ed25519` directly to `Ep` would imply that `q = 2^255-19`, so there would have to be a CM curve over `GF(2^255-19)` such that its order is a prime `p`.

CM curves over `GF(q)` only have 6 possible orders:

```
q + 1 + T
q + 1 - T
q + 1 + (T+3*V)/2
q + 1 + (T-3*V)/2
q + 1 - (T+3*V)/2
q + 1 - (T-3*V)/2
```

where `4*q = T^2 + 3*V^2`

For `q = 2^255-19` we have

```
T = 384483085883472032291258361162322087063
V = 167089731525863132650062706797393049103
```

and the  6 possible orders are:

```
57896044618658097711785492504343953926250509246936809987437533642794242732887
57896044618658097711785492504343953927019475418703754052020050365118886907013
57896044618658097711785492504343953926576599278473223336899327124341636289827
57896044618658097711785492504343953927077868473050812734849515244733815437136
57896044618658097711785492504343953926693385387167340702558256883571493350073
57896044618658097711785492504343953926192116192589751304608068763179314202764
```

None of these is a prime number.

This proves that you cannot have a cycle of CM curves that involves the field GF(2^255-19).

The workaround is to insert a third curve that has a small cofactor `h` and then search for a prime `p` such that one if its 6 possible orders is `h*(2^255-19)` and another one is a prime `q`. The smallest `p` I found is with `h = 1407`.

## narodnik | 2023-03-04T16:56:50+00:00
Hey guys, I haven't been following the thread but really excited to see this research going forwards!!!

I've been investigating another thread which I was planning to present once more further along, but happy to share details here to find collaborators. If I finish in time, then I'll present it at Monerotopia and happy to discuss more with devs.

Basically with curve trees, the main slowdown is the need for a fast EC inner product proof. I've been looking at a paper by Liam Eagan (who made bulletproofs++ as well) on using the Weil reciprocity trick.

Functions can be represented by divisors (equivalent up to a constant) which tracks the zeros and poles. Weil reciprocity states that $f(\textrm{div}(g)) = g(\textrm{div}(f))$, and we can use this to make a compact proof that a function interpolates some points. Then we can build up a statement about the structure of a point from these proofs. For now the first version will use normal double and add (actually there's 3 states per digit, not 2), but it can be sped up further with addition chains (needs further research).

The code below just constructs the function for a divisor. Here are [some additional notes](https://github.com/narodnik/arithmetic-elliptic-curves-silverman/blob/master/ecip-proof.pdf).

```python
# Initialize an elliptic curve
p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
r = 115792089237316195423570985008687907852837564279074904382605163141518161494337
Fp = GF(p)  # Base Field
Fr = GF(r)  # Scalar Field
A = 0
B = 7
E = EllipticCurve(GF(p), [A,B])
assert(E.cardinality() == r)

K.<x> = PolynomialRing(Fp, implementation="generic")
L.<y> = PolynomialRing(K, implementation="generic")
eqn = y^2 - x^3 - A * x - B

# Returns line passing through points, works for all points and returns 1 for O + O = O
def line(A, B):
    if A == 0 and B == 0:
        return 1
    else:
        [a, b, c] = Matrix([A, B, -(A+B)]).transpose().kernel().basis()[0]
        return a*x + b*y + c

def dlog(D):
    # Derivative via partials
    Dx = D.differentiate(x)
    Dy = D.differentiate(y)
    Dz = Dx + Dy * ((3*x^2 + A) / (2*y))
    assert D != 0
    return Dz/D

P0 = E.random_element()
P1 = E.random_element()
P2 = E.random_element()
Q = -int(Fr(5)^-1) * (P0 + 2*P1 + 3*P2)
assert P0 + 2*P1 + 3*P2 + 5*Q == 0

def div_add(div_f, div_g):
    div = div_f.copy()
    for P, n in div_g.items():
        if P in div:
            div[P] += n
        else:
            div[P] = n
    div = dict((P, n) for P, n in div.items() if n != 0)
    return div

def div_invert(div):
    return dict((P, -n) for P, n in div.items())

def div_sub(div_f, div_g):
    inv_div_g = div_invert(div_g)
    return div_add(div_f, inv_div_g)

# 2[P₂] + [-2P₂] - 3[∞]
f1 = line(P2, P2)
D1 = {"P2": 2, "-2P2": 1, "∞": -3}
# 2[P₁] + [-2P₁] - 3[∞]
f2 = line(P1, P1)
D2 = {"P1": 2, "-2P1": 1, "∞": -3}
# [P₂] + [-P₂] - 2[∞]
f3 = line(P2, -P2)
D3 = {"P2": 1, "-P2": 1, "∞": -2}
# [P₀] + [-P₀] - 2[∞]
f4 = line(P0, -P0)
D4 = {"P0": 1, "-P0": 1, "∞": -2}

# (2[P₂] + [-2P₂] - 3[∞]
#  + 2[P₁] + [-2P₁] - 3[∞]
#  + [P₂] + [-P₂] - 2[∞]
#  + [P₀] + [-P₀] - 2[∞])
# =
# [P₀] + 2[P₁] + 3[P₂] + [-P₀] + [-2P₁] + [-2P₂] + [-P₂] - 10[∞]
f5 = f1*f2*f3*f4
D5 = div_add(div_add(D1, D2), div_add(D3, D4))
assert D5 == {
    "P0":   1,
    "P1":   2,
    "P2":   3,
    "-P0":  1,
    "-2P1": 1,
    "-2P2": 1,
    "-P2":  1,
    "∞":  -10
}

# [-2P₂] + [-2P₁] + [2(P₁ + P₂)] - 3[∞]
f6 = line(-2*P2, -2*P1)
D6 = {"-2P2": 1, "-2P1": 1, "2P1 + 2P2": 1, "∞": -3}
# [-P₂] + [-P₀] + [P₀ + P₂] - 3[∞]
f7 = line(-P2, -P0)
D7 = {"-P2": 1, "-P0": 1, "P0 + P2": 1, "∞": -3}

# ([P₀] + 2[P₁] + 3[P₂] + [-P₀] + [-2P₁] + [-2P₂] + [-P₂] - 10[∞]
#  - [-2P₂] - [-2P₁] - [2(P₁ + P₂)] + 3[∞]
#  - [-P₂] - [-P₀] - [P₀ + P₂] + 3[∞])
# =
# [P₀] + 2[P₁] + 3[P₂] - [2(P₁ + P₂)] - [P₀ + P₂] - 4[∞]
f8 = f5/(f6*f7)
D8 = div_sub(D5, div_add(D6, D7))
assert D8 == {
    "P0":         1,
    "P1":         2,
    "P2":         3,
    "2P1 + 2P2": -1,
    "P0 + P2":   -1,
    "∞":         -4
}

# [P₀ + P₂] + [2(P₁ + P₂)] + [-(P₀ + 2P₁ + 3P₂)] - 3[∞]
f9 = line(P0 + P2, 2*(P1 + P2))
D9 = {"P0 + P2": 1, "2P1 + 2P2": 1, "5Q": 1, "∞": -3}
# ([P₀] + 2[P₁] + 3[P₂] - [2(P₁ + P₂)] - [P₀ + P₂] - 4[∞]
#  + [P₀ + P₂] + [2(P₁ + P₂)] + [-(P₀ + 2P₁ + 3P₂)] - 3[∞])
# =
# [P₀] + 2[P₁] + 3[P₂] + [-(P₀ + 2P₁ + 3P₂)] - 7[∞]
# = [P₀] + 2[P₁] + 3[P₂] + [5Q] - 7[∞]
f10 = f8*f9
D10 = div_add(D8, D9)
assert D10 == {
    "P0": 1,
    "P1": 2,
    "P2": 3,
    "5Q": 1,
    "∞": -7
}

# Now construct 5[Q]

# 2[Q] + [-2Q] - 3[∞]
f11 = line(Q, Q)
D11 = {"Q": 2, "-2Q": 1, "∞": -3}

# [-2Q] + [2Q] - 2[∞]
f12 = line(-2*Q, 2*Q)
D12 = {"-2Q": 1, "2Q": 1, "∞": -2}

# (2[Q] + [-2Q] - 3[∞]) - ([-2Q] + [2Q] - 2[∞])
# ==
# 2[Q] - [2Q] - [∞]
f13 = f11/f12
D13 = div_sub(D11, D12)
assert D13 == {
    "Q": 2,
    "2Q": -1,
    "∞": -1
}

# multiply by 3
# 6[Q] - 3[2Q] - 3[∞]
f14 = f13*f13*f13
D14 = div_add(div_add(D13, D13), D13)
assert D14 == {
    "Q": 6,
    "2Q": -3,
    "∞": -3
}

# 2[2Q] + [-4Q] - 3[∞]
f15 = line(2*Q, 2*Q)
D15 = {"2Q": 2, "-4Q": 1, "∞": -3}

# (6[Q] - 3[2Q] - 3[∞]) + (2[2Q] + [-4Q] - 3[∞])
# ==
# 6[Q] - [2Q] + [-4Q] - 6[∞]
f16 = f14*f15
D16 = div_add(D14, D15)
assert D16 == {
    "Q": 6,
    "2Q": -1,
    "-4Q": 1,
    "∞": -6
}

# [2Q] + [-2Q] - 2[∞]
f17 = line(2*Q, -2*Q)
D17 = {"2Q": 1, "-2Q": 1, "∞": -2}

# (6[Q] - [2Q] + [-4Q] - 6[∞]) + ([2Q] + [-2Q] - 2[∞])
# ==
# 6[Q] + [-2Q] + [-4Q] - 8[∞]
f18 = f16*f17
D18 = div_add(D16, D17)
assert D18 == {
    "Q": 6,
    "-2Q": 1,
    "-4Q": 1,
    "∞": -8
}

# [-2Q] + [-4Q] + [6Q] - 3[∞]
f19 = line(-2*Q, -4*Q)
D19 = {"-2Q": 1, "-4Q": 1, "6Q": 1, "∞": -3}

# (6[Q] + [-2Q] + [-4Q] - 8[∞]) - ([-2Q] + [-4Q] + [6Q] - 3[∞])
# ==
# 6[Q] - [6Q] - 5[∞]
f20 = f18/f19
D20 = div_sub(D18, D19)
assert D20 == {
    "Q": 6,
    "6Q": -1,
    "∞": -5
}

# [6Q] + [-6Q] - 2[∞]
f21 = line(6*Q, -6*Q)
D21 = {"6Q": 1, "-6Q": 1, "∞": -2}

# (6[Q] - [6Q] - 5[∞]) + ([6Q] + [-6Q] - 2[∞])
# ==
# 6[Q] + [-6Q] - 7[∞]
f22 = f20*f21
D22 = div_add(D20, D21)
assert D22 == {"Q": 6, "-6Q": 1, "∞": -7}

# [Q] + [-6Q] + [5Q] - 3[∞]
f23 = line(Q, -6*Q)
D23 = {"Q": 1, "-6Q": 1, "5Q": 1, "∞": -3}

# (6[Q] + [-6Q] - 7[∞]) - ([Q] + [-6Q] + [5Q] - 3[∞])
# ==
# 5[Q] - [5Q] - 4[∞]
f24 = f22/f23
D24 = div_sub(D22, D23)
assert D24 == {"Q": 5, "5Q": -1, "∞": -4}

# Now combine the result
f = f10*f24
D = div_add(D10, D24)
assert D == {
    "P0": 1,
    "P1": 2,
    "P2": 3,
    "Q":  5,
    "∞": -11
}

f_numer = f.numerator().mod(eqn)
f_denom = f.denominator().mod(eqn)
# ZeroDivisionError
#DLog = dlog(f_numer)

assert f(x=P0[0], y=P0[1]) == 0
assert f(x=P1[0], y=P1[1]) == 0
assert f(x=P2[0], y=P2[1]) == 0
# Need to modify f because this is 0/0
#assert f(x=Q[0], y=Q[1]) == 0

```

## narodnik | 2023-03-04T17:17:40+00:00
> Please note Zcash transactions have one collective proof for all inputs and outputs

I don't recommend this. Essentially it just merges the input and output proofs together and uses a selector bit to choose which part of the circuit is used. Some parts are reused between both parts, but IMO it doesn't bring much anonymity and complicates things. But this is a minor point if you prefer this technique.

Also I am now suddenly very bullish on Monero. wagmi

> I heave to learn why pallas was chosen over vesta in the first place.

@kayabaNerve iirc there is a conversion from vesta is embedded into pasta, and there is a conversion mod_r_p() so pallas Base field values can be imported directly into the scalar field (for use in circuits). It's a trick that can only be used one way but not the other.

> I also couldn't find any information about what specific 2-adicity is required for PLONK and the limitations implied. But nevertheless, this curve cycle should work at least as well as Pasta.

@tevador  standard circuits in production usually use k = 11 to 13 in my experience. Above 15, it is far far too slow, but big prod circuits like rollups would do weird things like FRI or pairings inside. Unlikely you'll need that though.

You also don't even need 2-adicity. You need a subgroup of a certain size that fully contains your circuit + 5 extra blinding rows. The cosets form the other columns (gates in halo2 terminology). More cosets/columns = more operators in your circuit.

This is in the permutation argument. The [original plonk paper](https://raw.githubusercontent.com/arielgabizon/plonk/master/PLONK.pdf) used quadratic residues to select distinct cosets of the subgroup (see bottom of page 26). You can look at [the halo2 docs](https://zcash.github.io/halo2/design/proving-system/permutation.html) for $\delta^i$ which is the coset selector, whereas $\omega^j$ selects the row. This permutation argument is based off the earlier proof of a mixnode mixing by Jens Groth btw if curious (hence why roots of unity is used).

```python
q = 0x40000000000000000000000000000000224698fc0994a8dd8c46eb2100000001
K = GF(q)
P.<X> = K[]

# GENERATOR^{2^s} where t * 2^s + 1 = q with t odd.
# In other words, this is a t root of unity.
generator = K(5)
# There is a large 2^32 order subgroup in this curve because it is 2-adic
t = (K(q) - 1) / 2^32
assert int(t) % 2 != 0
delta = generator^(2^32)
assert delta^t == 1

# The size of the multiplicative group is phi(q) = q - 1
# And inside this group are 2 distinct subgroups of size t and 2^s.
# delta is the generator for the size t subgroup, and omega for the 2^s one.
# Taking powers of these generators and multiplying them will produce
# unique cosets that divide the entire group for q.

def get_omega():
    generator = K(5)
    assert (q - 1) % 2^32 == 0
    # Root of unity
    t = (q - 1) / 2^32
    omega = generator**t

    assert omega != 1
    assert omega^(2^16) != 1
    assert omega^(2^31) != 1
    assert omega^(2^32) == 1

    return omega

# Order of this element is 2^32
omega = get_omega()
k = 4
n = 2^k
omega = omega^(2^32 / n)
assert omega^n == 1

# ...

a_1_X = P.lagrange_polynomial((omega^i, A_1_i) for i, A_1_i in enumerate(A1))
a_2_X = P.lagrange_polynomial((omega^i, A_2_i) for i, A_2_i in enumerate(A2))
a_3_X = P.lagrange_polynomial((omega^i, A_3_i) for i, A_3_i in enumerate(A3))
a_4_X = P.lagrange_polynomial((omega^i, A_4_i) for i, A_4_i in enumerate(A4))

# ...

indices = ([omega^i for i in range(n)]
           + [delta * omega^i for i in range(n)]
           + [delta^2 * omega^i for i in range(n)]
           + [delta^3 * omega^i for i in range(n)]
           + [delta^4 * omega^i for i in range(n)])
assert len(indices) == 80
# Permuted indices
sigma_star = [indices[i] for i in permuted_indices]
s = [sigma_star[:n], sigma_star[n:2 * n], sigma_star[2 * n:3 * n],
     sigma_star[3 * n:4 * n], sigma_star[4 * n:]]

```

## narodnik | 2023-03-04T18:07:25+00:00
Monero will become the #1 privacy coin with this upgrade. We believe the return to values agorist narrative will be the next driving force in this cycle.

This video explains why: [Lunarpunk and the Dark Side of the Cycle](https://www.youtube.com/watch?v=QA3YZVDUN5s)

Original text is [here](https://www.egirlcapital.com/writings/107533289). This was published Feb 2022. Then Tornado Cash happened. The events are unfolding as claimed. We must be prepared to meet the challenge!

## kayabaNerve | 2023-03-04T18:23:02+00:00
@narodnik A larger 2-adicity offers more options, yet any smaller `k` value can still be used, right?

Also, do you have a link to the cited paper by Eagen available?

## narodnik | 2023-03-04T18:52:52+00:00
Yes correct. k = 11, corresponds to the $2^{11}$ subgroup.

Here is the paper: https://eprint.iacr.org/2022/596

If you check the end part, it mentions curve trees.

## kayabaNerve | 2023-03-04T19:16:32+00:00
It looks like that doesn't put any bounds on the elliptic curve, which is great. It'd also greatly accelerate Pedersen hashes...

> Each additional hash adds only two multiplications and one scalar

It does conflict with "SNARKs", yet should work with Bulletproofs, which curve trees are based on. I'm unsure if Halo 2, a Bulletproof inspired protocol, is fit under the former or later category.

@narodnik I can't find any mention of "trees" in the paper nor IACR page. Mind clarifying the section?

## tevador | 2023-03-04T19:48:30+00:00
> I can't find any mention of "trees" in the paper nor IACR page. Mind clarifying the section?

I think §5.1 and §5.2 indirectly relate to Curve Trees, which internally use Pedersen hashes and a recursive construction with a 2-cycle. 

## narodnik | 2023-03-04T19:52:39+00:00
yep apologies, I thought it mentioned curve trees but that's the section.

## narodnik | 2023-03-05T07:27:33+00:00
Check these slides out for more info on the construction of pallas and vesta curves:
https://github.com/daira/halographs/blob/master/deepdive.pdf

Also if you're concerned with efficiency, a more experimental idea would be genus-2 hyperelliptic curves which are known to be secure and are slightly more efficient than usual EC. They are degree 5 curves so each line through them creates 5 points. The group law is constructed using the picard group.

The 2 cycle is mainly for proof composition. The older curve was BLS12-381 which was able to embed jubjub inside. This was a one way embedding.

The [halo1 paper](https://eprint.iacr.org/2019/1021.pdf) describes the amortization strategy which happens in the polynomial commitment proof.

The large 2-adic subgroup means we can do efficient DFFT/lagrange polynomials which is the core of plonk-based protocols.

## tevador | 2023-03-05T09:58:28+00:00
I'd like to focus on Curve Trees first, because that could work while keeping the Ed25519 curve.

I think the next steps should be:

1. Implementing Curve Trees in Sage using the [indirect cycle](https://github.com/monero-project/research-lab/issues/100#issuecomment-1443923679) I found to check the technical feasibility of such protocol.
2. Implementing the Weil Reciprocity optimization from this paper: https://eprint.iacr.org/2022/596
3. Implementing the protocol in C/C++ or Rust to measure the real-word performance.

If step 1 shows that the protocol is infeasible or step 3 shows that the verification performance is insufficient, then we can move to research plonk and decide which new curve to use.

## kayabaNerve | 2023-03-06T10:00:51+00:00
@tevador 

1.

```
d = -15203, h(d) = 38

p = 2^255 - 19
A_p, B_p = 42133672695493072568592123651119866263416556208894889063239545248024637995649
E_p/F_p : y^2 = x^3 + A_p x + B_p
#E_p = q

q = 57896044618658097711785492504343953926225696987256860989792804023844074237167
A_q, B_q = 29601700755814669423401170136441329018751839114999486207043705707424836093663
E_q/F_q : y^2 = x^3 + A_q x + B_q
#E_q = p
```

This is from Eagen and is a direct cycle of 2^255-19. The reason we shouldn't use this cycle or an indirect cycle is performance. The curve cycle you noted is directly competitive with Ed25519 and has a high 2-adicity.

3. https://github.com/simonkamp/curve-trees is a modification of dalek's bulletproofs used a curve tree PoC. It may be a valuable base/reference as its generic to its curve and tested with the pasta curves. Since we know the comparative performance of pasta and and your proposed cycle, it'd minimize your work to the noted optimization/indirect cycle perf testing.

## narodnik | 2023-03-06T14:47:46+00:00
He also kindly sent me these calculations: https://agorism.dev/uploads/ecip_calculations.ipynb

Next week I'll post a longer write up of all the steps with self contained sage code. There's a few helper utilities I need to create, then we can start work on a prototype rust version to benchmark against halo2 merkle proofs. Feel free to poke me on IRC for more info. Happy to explain anything in the paper.

There is a bug in sage so the dlog calculation fails for higher multiplicity functions. The fix is to turn the denominator into a function in x by taking the norm. Observe that every function in the function field can be written as $\frac{a(x) + yb(x)}{c(x) + y d(x)}$, which is the same as

$$\frac{(a(x) + yb(x))(c - yd(x))}{c(x)^2 - y^2 d(x)^2} = \frac{(a(x) + yb(x))(c - yd(x))}{c(x)^2 - (x^3 + Ax + B) d(x)^2} = \frac{(f \circ \bar{g})(x, y)}{N_g(x)}$$

## daira | 2023-03-06T15:48:36+00:00
@tevador :
> @kayabaNerve :
> > I'll note regarding your second cited source, it has a complexity of O($n^{1.5}$). These curves have a n of $2^{32}$. Pallas's $n$ is 32.
> 
> I admit I haven't read the second paper in detail. I was going by a statement from the zcash blog post that claims 2-adicity "may assist in square root performance". If the algorithm is O($n^{1.5}$) then it might actually be slower, which is unfortunate and may negate the other performance benefits.

To explain this: 32 is a multiple of 8, and this facilitates using [Sarkar's algorithm](https://eprint.iacr.org/2020/1407) with 8-bit tables, which are a convenient size (as done in the https://github.com/zcash/pasta_curves implementation). The benefit is fairly small but measurable when compared to a similar 2-adicity that is not a convenient multiple. In general, a larger 2-adicity does give slower square roots (but not egregiously so, and it really only matters for point decompression).


## daira | 2023-03-06T16:06:05+00:00
@narodnik :
> @kayabaNerve :
> > Please note Zcash transactions have one collective proof for all inputs and outputs
> 
> I don't recommend this. Essentially it just merges the input and output proofs together and uses a selector bit to choose which part of the circuit is used. Some parts are reused between both parts, but IMO it doesn't bring much anonymity and complicates things. But this is a minor point if you prefer this technique.

This description is a bit confused; there are two things is could be referring to:

1. In Orchard, we have a single "action" circuit that combines a spend and an output. This is not the same as having a selector bit; an action does both simultaneously. The motivations for this are largely specific to Zcash, but it does simplify the way that we prevent Faerie Gold attacks (which also potentially apply to Monero; your "burning bug" was a Faerie Gold attack in our terminology), because it means that we have a guaranteed-unique nullifier from the spend side that we can use in the output side.
2. If you are doing multiple Halo 2 proofs at the same time then you can share some values. This shortens the overall proof and, more importantly, gives a much lower *marginal* verification time per extra proof &mdash; because you only need to check one inner product argument, which is the slow part, per transaction. If you use Halo 2 or *any* other IPA-based proof system (the same idea can be adapted to Bulletproofs) then you really want to take advantage of this; it's a big win for verification cost.


## narodnik | 2023-03-06T16:32:08+00:00
Aha right because you want to guarantee that the serial produced by the output is unique and not reused in another output. You do that by merging the spend + output proof, and using the spend nullifier in the output serial. Thanks a lot for clarifying.

## str4d | 2023-03-06T18:58:00+00:00
> > I heave to learn why pallas was chosen over vesta in the first place.
>
> @kayabaNerve iirc there is a conversion from vesta is embedded into pasta, and there is a conversion mod_r_p() so pallas Base field values can be imported directly into the scalar field (for use in circuits). It's a trick that can only be used one way but not the other.

Yep. The specific issue is that in a couple of places in the Orchard protocol, we needed to be able to treat a *protocol curve point coordinate* as a *protocol curve scalar*, which means treating a *circuit curve scalar field element* as a *circuit curve base field element*. Using Pallas as the *protocol curve* made this easier because its base field is smaller than its scalar field (and correspondingly for Vesta as the *circuit curve* its scalar field is smaller than its base field).

We could technically have chosen the other way around, but then would have needed to deal with the fact that the mapping would cause a reduction. As it was, we still had some complexity because even though the mapping wouldn't cause a reduction, we still needed to ensure canonical representation of the wrong-field element, so overall the complexity was probably equivalent either way (but the way round we chose meant the complexity was in the circuit implementation, not the protocol).

## tevador | 2023-03-06T21:02:44+00:00
> The reason we shouldn't use this cycle or an indirect cycle is performance.

I don't think performance is a sufficient reason to switch curves unless we can show that the indirect cycles are too slow.

> This is from Eagen and is a direct cycle of 2^255-19.

Interesting find, but I'm not convinced it would be faster because there is no endomorphism on these curves and the values of the curve constants require slower formulas to be used.


## kayabaNerve | 2023-03-07T00:05:58+00:00
@daira @str4d Thank you for chiming in. Your knowledge/experience is greatly appreciated :)

@tevador Regarding the indirect 2-cycle, I just wanted to make it available.

In order to better comment on switching curves, what would be the performance of your tower-cycle compared to Ed25519? The cycle you put forth was directly competitive. This will also be the most expensive proof in Monero, so that will weight it significantly.

## tevador | 2023-03-08T21:26:12+00:00
> This is from Eagen and is a direct cycle of 2^255-19

I think I know how this cycle was discovered.

I was able to reproduce it by following the algorithm described in this paper: https://arxiv.org/abs/0712.2022

Here is a slightly better one I found:

```
p = 0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffed
q = 0x7fffffffffffffffffffffffffffffffbb2d703f7a1e51cdf484069145e5f0f7

a_q = 13033894050202716689882839840150569719615712187482288559001333083615467046208
Eq: y^2 = x^3 + a_q*x + a_q
#Eq = p

a_p = 48408044624602722078043330694711161699859898671792113289661329891201103641892
Ep: y^2 = x^3 + a_p*x + a_p
#Ep = q
```

This one is preferable because `2^256 - 2*q < 2^128`, which means the prime supports a competitively fast Barrett reduction (albeit still much slower than 2^255-19).

It is a "short tower-cycle":

```
             ---->----
            /         \
Ed25519 -> Eq         Ep
            \         /
             ----<----
```

Unfortunately, these curves don't have an efficiently computable endomorphism, so while their field arithmetics might be faster than Pallas/Vesta, scalar multiplication will be slower. However, this is much better than the 266-bit primes presented earlier.

## Cli5y | 2023-03-09T19:58:27+00:00
Commenting due to this forum thread: https://forum.zcashcommunity.com/t/allow-special-exception-to-the-orchard-codebase-for-the-monero-project/41392

The BOSL exemptions for Orchard, as stated by [ECC](https://electriccoin.co/blog/bosl-exceptions-added-for-zcash-projects-and-friendly-forks/), are:

_-     Projects that are designed to integrate with Zcash and provide additional functionality or utility to the Zcash network and users of the ZEC coin_

_-     Blockchains that descend from the Zcash blockchain and that are forked within 100 blocks of the current block height at the time of the code fork_

I'm curious if Monero could qualify for a permissionless exemption via the first bullet point. It would require development efforts (that also aid Zcash) outside of implementing Halo2/Orchard into Monero, but could give Monero ability to use Orchard.

Not sure if Monero would need to use Orchard code, but gives teams the ability to do this:

_- The Monero project could include Orchard code to make a derivative work without needing to license the Monero code under the same BOSL restrictive license._

Just a thought. Could be wrong with my interpretation.

## narodnik | 2023-03-10T08:54:50+00:00
@esepibito the zcash team are kind enough to make halo2 available. Orchard is a relatively small code and not needed here.

@tevador about lack of endomorpism, another possibility for speedup is [addition chains](https://en.wikipedia.org/wiki/Addition-chain_exponentiation#Addition-subtraction%E2%80%93chain_exponentiation). Also succinct EC multiplication proofs might reduce the cost further. Although I'm not sure how impactful these changes would be (and having a proof means extra data) so ECM is much preferred.

## kayabaNerve | 2023-03-10T09:20:11+00:00
@esepibito We are not interested Orchard. We have our own transaction protocol, Seraphis.

While their Halo 2 library is of potential interest, it's not a current discussion. The current discussion is on a curve cycle for curve trees. In the future, we may further consider replacing the Bulletproofs used within curve trees with a proof like Halo 2, then leading into a discussion on using the Halo 2 library, that's far out of scope right now.

I'd also further note a complete lack of interest in any non-FOSS usage of code. Exemptions are not FOSS. While the BOSL may be arguable as a FOSS license, it is so restrictive I cannot in good faith ever advocate its usage within Monero. This is comparable to how we cannot, and should not, use GPL code (as it'd require moving to the GPL license).

## narodnik | 2023-03-10T13:51:40+00:00
I have the core part of the ECIP proof working here:

https://github.com/darkrenaissance/darkfi/blob/master/script/research/zk/ecip/proof.sage

Now I'll generalize it to proving point relations. Then after that's finished, I'll make a writeup/explainer and can start writing a Rust version so we can benchmark its speed.

## kayabaNerve | 2023-03-15T23:44:14+00:00
@tevador I don't believe an indirect curve cycle will work.

For:

Ed25519 - X - Y <-> Z

We need to perform an EC add for Ed25519 *and* prove membership. We'd have to prove the addition over X, yet then prove the membership over Y/Z. The entire process has to be done in ZK to be a valid membership proof however.

Any thoughts on this? Am I missing something?

## tevador | 2023-05-04T19:07:27+00:00
> I don't believe an indirect curve cycle will work.

I'm not an expert on ZKP, so CMIIW, but from what I understand, I think it should work.

Consider the tower-cycle:

```
Ed25519 -> Ep <-> Eq
```

In order to normalize the group law, it's better to convert all keys from `Ed25519` to the isomorphic curve `Wei25519`, which is a short Weierstrass curve.

The Merkle tree would look like this:

* The leaf keys are in `Wei25519`
* 2nd level keys are in `Ep`
* 3rd level keys are in `Eq`
* 4th level keys are in `Ep`
* etc.
* The root is in `Ep` or `Eq` depending on the number of levels.

You have a `Wei25519` key `K_o` you want to prove is in the tree.

The recursive proof construction works exactly as described in the Curve Trees paper. You use the "Select and rerandomize" proof at each tree level. At the leaf level, you get the commitment `K_o' = K_o + r G`, which is published to be used in the composition proof (after converting it back to `Ed25519` using the isomorphism map).

Notice that the leaf-level proof is done on the curve `Ep`. This means that all the proofs are either in `Ep` or `Eq`, so we can merge them into just 2 proofs as it's done in the Curve Trees paper. The only difference will be the constants used in the rerandomization at the leaf level (those will be the `Wei25519` curve constants), but I don't think this prevents merging.

If this is confirmed to be possible, I think it's the preferable solution because it avoids the commitment migration that would be needed if we switched curves.

## kayabaNerve | 2023-05-08T06:05:18+00:00
While that sounds possible, it'd mean we'd always need an additional proof. Not only would we always need an additional proof, if not two for your optimized tower-cycle, the lowest proof(s) would never be SNARKs under current academia due to verification time.

The first proof is also the largest one due to performing the ECC op *and* the hashes. For that to not be a SNARK would be... extremely detrimental.

## tevador | 2023-05-08T09:34:38+00:00
> The first proof is also the largest one due to performing the ECC op and the hashes.

Curve Trees perform point blinding and hashing on every level. See the [paper](https://eprint.iacr.org/2022/756.pdf), section 4.2.1.

## kayabaNerve | 2023-06-24T07:41:05+00:00
https://github.com/kayabaNerve/full-chain-membership-proofs/

Considerations:

1) It's in Rust. I can comment on the code cleanliness that enables, or on the shared efforts it can bring us with other projects, or on the safety... or we can say that's unacceptable and someone else can rewrite it in C++. Personally, I'd like to see a hybrid approach where most is kept in Rust, yet some (like the tree code) may or may not be rewritten in C++.

2) It's slow. Without a proper vector commitment scheme, it's ~33x slower than Grootle proofs for a 777m membership set. With one, it's only an order of magnitude slower. I see a path of getting it to just 3-5x slower, and the curve trees PoC even beat Grootle (with heavy parallelization). With further work on internal structuring, inspired by the curve trees PoC, I'd hope to end up at 2-3x times slower.

3) I implemented the DLEq proof, and technically implemented tevador's first cycle candidate. My impl of tevador's first cycle candidate is unviable and needs a complete rewrite. I've been testing with the pasta curves. With a proper impl of tevador's first cycle candidate, we're looking at just ~3x slower. I'd also note we do use hash to curve, currently, so we may prefer tevador's second cycle candidate (discussions pending).

4) My presentation at MoneroKon, which has been uploaded to the repo, goes over it briefly (and non-technically). I hope to discuss this at the next MRL meeting to further clarify. After initial understandings are present, I hope to provide a clear path forward of actionable steps with @j-berman.

## kayabaNerve | 2023-06-26T19:11:10+00:00
I'm still overall working on summaries/exact specifications to refer to, yet to start:

1) Would enable a clean solution to #96 AFAICT
2) Would void #87 and #109
3) Would prevent a remote node from sending a skewed output distribution, nuking privacy (they could only send a historical honest distribution, which can be mitigated by having the block header be binding to the output tree root)
4) #95 is unaffected. The tree root contains all outputs, so any re-org of outputs will provide a different tree root, voiding any TXs reliant on the original tree root

I'd also note #101 becomes more notable. The biggest concern I've heard is over the proof size which BP++ should also reduce. We would need a modified BP++, as we need a modified BP+ though. Modifying BP+ still makes sense as BP++ argues its norm argument is a reduction to BP+'s WIP argument, so modifying BP+ sets applicable groundwork.

EDIT: BP++ will only cause a size reduction of 3.6%. The main benefits would be in greater flexibility regarding circuit layout and verification time.

## kayabaNerve | 2023-06-26T21:48:28+00:00
Discussing with @jeffro256 and @j-berman, a novel vector applicable to rings came up.

If a coinbase output is swept, rings are effectively null since the received output amount + fees will equal one of the ring members exactly (as the coinbase output has a known amount). This is somewhat mitigated with tail emission normalizing coinbase amounts, yet that reduces the ring to the amount of tail emission coinbases if a tail emission coinbase is swept/"send max"d.

Full chain membership proofs include all tail emission coinbases, and for non-tail-emission coinbases, increases the odds a distinct output with a matching value *when including whatever the change output may or may not be as if it was a sweep/"send max" is undetectable* was spent.

---

I'll also note that while DSAs aren't dead, they become limited to light wallets (instead of requesting a single path, doxxing the spent output, a ring of paths would be requested). This greatly reduces their importance and issues raised by implementation faults.

## kayabaNerve | 2023-06-27T13:44:10+00:00
I believe I made a mistake, and each input proof would only be 2kb, not 4kb as I off hand estimated. Accordingly, 2-in, 2-out TX sizes would be ~5.5kb, not 10kb.

## kayabaNerve | 2023-06-27T14:09:03+00:00
We can also use one pair of membership proofs for every input, instead of per input. That'd make the second input add a few hundred bytes, not double the entire proof size. Unfortunately, I believe that breaks the flexibility of Seraphis a bit too much, with a notable privacy impact when TX-chaining/doing collaborative TXs (which are also how we start discussing payment channels, so I wouldn't appreciate so harming them).

EDIT: politicalweasel on Twitter suggested pairing each pair of inputs with a single proof. This would have slightly improved verification times, notable space savings, yet still allow collaborative transactions without participants doxxing their memberships to each other. They'd simply need an (unnecessary) 3rd input, with a second proof (handled by the second party).

We could also review MPC proving of BP+ if this is important yet we want to batch all inputs in a TX under a single proof.

## UkoeHB | 2023-06-29T16:29:52+00:00
> We can also use one pair of membership proofs for every input, instead of per input. That'd make the second input add a few hundred bytes, not double the entire proof size. Unfortunately, I believe that breaks the flexibility of Seraphis a bit too much, with a notable privacy impact when TX-chaining/doing collaborative TXs (which are also how we start discussing payment channels, so I wouldn't appreciate so harming them).

If aggregating provides significant reductions in perf/size then we should definitely consider it.

## UkoeHB | 2023-06-29T16:46:34+00:00
@tevador's short tower-cycle requires three relations for each of the three curves. Could the Wei25519 -> Eq relation be simplified by letting Eq be the leaf layer, and then doing a direct conversion to Wei25519 (via plain commitment to plain commitment instead of vector commitment to plain commitment)?

## kayabaNerve | 2023-07-02T00:15:12+00:00
There's no change to perf. There is a significant reduction in size.

You'd need to promote a "Wei25519" key to Eq. While that can be down at time of tree addition, it can't be done at time of membership proof. The underlying point isn't available, only a blinded version, and whatever promotion occurs will remove the relationship of its blinding.

## UkoeHB | 2023-07-02T01:53:08+00:00
> You'd need to promote a "Wei25519" key to Eq. While that can be down at time of tree addition, it can't be done at time of membership proof. The underlying point isn't available, only a blinded version, and whatever promotion occurs will remove the relationship of its blinding.

I'm not sure what you're getting at here. Yes, the idea is to transmit Wei points into the tree during accumulation, then output blinded Wei points from the membership proofs.

> There's no change to perf. There is a significant reduction in size.

This is a bit hard to believe, but will take your word for it until it's easier to evaluate.

## kayabaNerve | 2023-07-03T11:30:47+00:00
1) If you promote Wei points at time of accumulation, so Ep points are the leaf layer, then at time of proof, you need to unblind the blinded Wei point into an Ep point. That requires unblinding as Wei, then performing the same promotion. The issue is that if there's an Ep leaf, there's an Eq proof, and with an Eq proof, Wei points aren't native so this would be extremely expensive.

2) Bulletproofs has O(n) verification time. While you save the BP setup costs, it doesn't change the total circuit size which is most of the expense. It's probably slightly more performant over all, though it does reduce the ability to batch a bit (as instead of 2 proofs with 512 shared generators, it's 1 proof with 1024 generators). Proof size is O(log n), so doubling the circuit size only adds 1 LR commitments (64 bytes). There's an extra couple hundred bytes on commitments but meh.

---

To discuss the short tower in more general, if we have Wei points as leaves, then the first proof would be Ep. Then the next Eq, and the cycle continues. The immediate issue is tevador's short cycle is slow.

The next issue is Ed25519 has torsion. I'm unsure the safety of that in the current proof, and I'm unsure the safety of divisors over torsioned curves. I believe the primary issue is the current on curve code expects points not to be identity, yet the small subgroup points would pass. While we can check that by doing 3 doubles, that'll take... 6 gates a point? And increase our proof size 10%. That ignores any larger safety concerns which may exist.

That also assumes we just to check isn't identity/small subgroup. If we have to check isn't torsioned, and we can't simply torsion clear, then the proof size will 3x. That'd be the worst case, yet immediately, the step would be to confirm the safety/applicability of divisors to torsioned curves. While we can drop divisors, that'd double the proof size.

And then long term, the issue is that the short tower cycle doesn't include Ed25519 scalars as a native field, solely Ed25519 field elements. The end goal of Monero should be each block, or the entire blockchain, having a single proof of range proofs for all prior TXs, either via Nova or Halo. If we do proofs over Ed25519, or Wei25519, then we can never have both fields natively available in a cycle.

TL;DR Would hurt perf by ~50%. Would need redone security analysis. At worst, it'll 2-3x our proof due to torsion. I'd guess it at least increases proof size 10% which will reduce the anonymity set to keep current perf. Long term, could make the only way to actually scale the Monero L1 multiple orders of magnitude less efficient.

## chaserene | 2024-04-24T19:37:36+00:00
it's funny how this issue has been dormant while the biggest developments  were taking place in the past month.

documenting the most important resources, as discussed in the 2024-04-24 MRL meeting:

* @kayabaNerve: **[Full-Chain Membership Proofs + Spend Authorization + Linkability gist](https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86)** (2024-03-31)

* @tevador: **[Elliptic curve tower-cycle for Curve25519](https://gist.github.com/tevador/4524c2092178df08996487d4e272b096)** (2024-04-06) (I forgot about this, thanks tevador for bringing it up below!)

* @kayabaNerve: **[FCMP++ Research  CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/449)** (first published: 2024-04-13, as part of the below Development CCS proposal)

* @kayabaNerve: **[FCMP++ Development CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/448)** (2024-04-13)

* @kayabaNerve: **FCMP++** ([direct PDF view](https://raw.githubusercontent.com/kayabaNerve/fcmp-ringct/develop/fcmp%2B%2B.pdf), [Github view](https://github.com/kayabaNerve/fcmp-ringct/blob/develop/fcmp%2B%2B.pdf)) (first published: 2024-04-23)

* @tevador: **[JAMTIS-RCT](https://gist.github.com/tevador/d3656a217c0177c160b9b6219d9ebb96)** (2024-04-28)

* @jeffro256: **[Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md)** (2024-07-31)

## tevador | 2024-04-24T20:59:49+00:00
This gist is also closely related to the current FCMP effort: [**Elliptic curve tower-cycle for Curve25519**](https://gist.github.com/tevador/4524c2092178df08996487d4e272b096)

## kayabaNerve | 2024-10-23T21:46:02+00:00
Initially discussed in https://github.com/monero-project/meta/issues/1098.

---

MAX_OUTPUTS = 16 is because a Bulletproof for 17 outputs wastes 15*64 gates (960). A FCMP++ uses 256+128 gates. That means if we have 5 inputs (in a single BP), we use 1280+640 gates, wasting 768+384 (1152).

This implies per the existing MAX_OUTPUTS, we should limit MAX_INPUTS to 4. I don't support MAX_INPUTS < MAX_OUTPUTS at this time due to the creation rate exceeding accumulation rate (though you can achieve a logarithmic time bound regardless). I also don't support MAX_OUTPUTS < 4. MAX_OUTPUTS = 2 requires perfect planning to make a tree of payments with only a logarithmic delay, and may be incompatible with Carrot as you wouldn't have change outputs in your own TXs.

Accordingly, with the hard fork, I'd support MAX_INPUTS = MAX_OUTPUTS = 4, which leads nicely into padding input/output count for privacy reasons (#96, #114). To minimize the disruption of so drastically limiting in/outs at this time, my proposal is 8/4. I'd accept 8/8 as well but I believe the end goal should be 4/4 (or 2/2 if we're extremely aggressive and have sufficient wallet protocol logic).

---

Elaborating on why I don't support MAX_OUTPUTS = 2: If a user has to make 128 payments, they can take an aggregated master output and make a transaction with:

- One change output
- The sum value of all 128 payments (plus fees), denoted the tree root

They can then spend the tree root, creating 0_1, 64_1.  They can then spend 0_1 creating 0_2, 32_2 and spend 64_1, creating 64_2 and 96_2. This continues until there is outputs for all even indexes at generation 8 (0_8, 2_8, 4_8...). Finally, 0_8 is used to fulfill payments 0/1, 2_8 is used to fulfill payments 2/3, etc. This works and is the exact logic seen in Serai. The issue is it requires perfection (for a batch of payments, you must always make a payment tree and never waste an output in it, not being allowed a change output) and it's in violation of Carrot.

> 7.8.3 Mandatory self-send enote rule
>
> Every transaction that spends funds from the wallet must produce at least one self-send (not necessarily internal) enote, typically a change enote. If there is no change left, an enote is added with a zero amount. This ensures that all transactions relevant to the wallet have at least one output. This allows for remote-assist "light weight" wallet servers to serve only the transactions relevant to the wallet, including any transaction that has spent key images. This rule also helps to optimize full wallet multi-threaded scanning by reducing state reuse.

4 outputs isn't in violation of Carrot, allowing a change output with each TX, and requires much fewer generations to fulfill a payment tree.

---

I'm not firm on not allowing MAX_INPUTS to be less than MAX_OUTPUTS. Since one can always achieve a logarithmic depth bound for the accumulation of received outputs, it's arguably a needless bound. Outputs are also much, much, cheaper than input. Resolving to 2/4 may make the most sense per that view and my commentary above on not setting MAX_OUTPUTS = 2. I leave this to be further discussed.

## Rucknium | 2024-10-23T21:51:36+00:00
## Tabulation of Monero transaction inputs and outputs

Here is a tabulation of the number of inputs and outputs of each Monero transaction during a five-year period (2019-03-04 to 2024-03-04).

R code to reproduce:

```R
# Run https://github.com/Rucknium/misc-research/blob/main/Monero-Effective-Ring-Size/xmr-ring-gathering.R
# Then:

# install.packages("knitr")

beginning.height <- 1784324  # 2019-03-04 15:20:22 UTC
start.spam.height <- 3097764 # 2024-03-04 15:21:24 UTC


n.inputs <- xmr.rings[ beginning.height < block_height_ring &
  block_height_ring < start.spam.height, 
  .(number_of_inputs = max(input_num)), by = c("tx_hash")]

n.inputs <- as.data.frame(prop.table(table(n.inputs$number_of_inputs)) * 100)
n.inputs$cumulative <- cumsum(n.inputs$Freq)
names(n.inputs) <- c("Number of inputs", "Share (percentage)", "Cumulative share")

knitr::kable(n.inputs, format = "pipe", row.names = FALSE,
  digits = 5)


n.outputs <- output.index[beginning.height < block_height &
  block_height < start.spam.height &
    output_amount == 0 & tx_num != 1, 
  .(number_of_outputs = max(number_of_outputs)), by = c("tx_hash")]

n.outputs <- as.data.frame(prop.table(table(n.outputs$number_of_outputs)) * 100)
n.outputs$cumulative <- cumsum(n.outputs$Freq)
names(n.outputs) <- c("Number of outputs", "Share (percentage)", "Cumulative share")

knitr::kable(n.outputs, format = "pipe", row.names = FALSE,
  digits = 5)

```

## Number of inputs

|Number of inputs | Share (percentage)| Cumulative share|
|:----------------|------------------:|----------------:|
|1                |           54.06724|         54.06724|
|2                |           38.98393|         93.05116|
|3                |            1.91450|         94.96566|
|4                |            0.97294|         95.93861|
|5                |            0.62223|         96.56084|
|6                |            0.46069|         97.02153|
|7                |            0.35652|         97.37805|
|8                |            0.29441|         97.67246|
|9                |            0.24665|         97.91911|
|10               |            0.24168|         98.16079|
|11               |            0.18053|         98.34133|
|12               |            0.15063|         98.49196|
|13               |            0.13002|         98.62198|
|14               |            0.11427|         98.73625|
|15               |            0.10234|         98.83859|
|16               |            0.09614|         98.93473|
|17               |            0.07834|         99.01306|
|18               |            0.06833|         99.08139|
|19               |            0.06239|         99.14378|
|20               |            0.05884|         99.20263|
|21               |            0.04949|         99.25212|
|22               |            0.04272|         99.29484|
|23               |            0.03846|         99.33330|
|24               |            0.03545|         99.36875|
|25               |            0.03390|         99.40265|
|26               |            0.02823|         99.43088|
|27               |            0.02553|         99.45641|
|28               |            0.02386|         99.48027|
|29               |            0.02166|         99.50193|
|30               |            0.02229|         99.52422|
|31               |            0.03664|         99.56086|
|32               |            0.01672|         99.57758|
|33               |            0.01513|         99.59271|
|34               |            0.01453|         99.60724|
|35               |            0.01326|         99.62051|
|36               |            0.01264|         99.63315|
|37               |            0.01123|         99.64438|
|38               |            0.01048|         99.65485|
|39               |            0.00992|         99.66478|
|40               |            0.01008|         99.67485|
|41               |            0.00909|         99.68395|
|42               |            0.00821|         99.69215|
|43               |            0.00784|         99.69999|
|44               |            0.00746|         99.70745|
|45               |            0.00718|         99.71463|
|46               |            0.00687|         99.72150|
|47               |            0.00649|         99.72798|
|48               |            0.00627|         99.73425|
|49               |            0.00613|         99.74038|
|50               |            0.00717|         99.74755|
|51               |            0.00541|         99.75296|
|52               |            0.00510|         99.75806|
|53               |            0.00502|         99.76308|
|54               |            0.00465|         99.76773|
|55               |            0.00435|         99.77208|
|56               |            0.00418|         99.77626|
|57               |            0.00407|         99.78033|
|58               |            0.00417|         99.78450|
|59               |            0.00393|         99.78843|
|60               |            0.00606|         99.79449|
|61               |            0.00404|         99.79853|
|62               |            0.00363|         99.80215|
|63               |            0.00356|         99.80571|
|64               |            0.00373|         99.80945|
|65               |            0.00326|         99.81271|
|66               |            0.00337|         99.81608|
|67               |            0.00302|         99.81910|
|68               |            0.00321|         99.82230|
|69               |            0.00315|         99.82545|
|70               |            0.00425|         99.82970|
|71               |            0.00278|         99.83248|
|72               |            0.00287|         99.83535|
|73               |            0.00309|         99.83844|
|74               |            0.00272|         99.84116|
|75               |            0.00180|         99.84296|
|76               |            0.00166|         99.84463|
|77               |            0.00165|         99.84628|
|78               |            0.00170|         99.84798|
|79               |            0.00164|         99.84962|
|80               |            0.00169|         99.85131|
|81               |            0.00162|         99.85293|
|82               |            0.00155|         99.85448|
|83               |            0.00154|         99.85602|
|84               |            0.00160|         99.85761|
|85               |            0.00144|         99.85905|
|86               |            0.00144|         99.86050|
|87               |            0.00154|         99.86204|
|88               |            0.00150|         99.86354|
|89               |            0.00146|         99.86499|
|90               |            0.00138|         99.86638|
|91               |            0.00141|         99.86778|
|92               |            0.00128|         99.86907|
|93               |            0.00137|         99.87044|
|94               |            0.00126|         99.87169|
|95               |            0.00128|         99.87297|
|96               |            0.00116|         99.87413|
|97               |            0.00114|         99.87527|
|98               |            0.00125|         99.87652|
|99               |            0.00124|         99.87776|
|100              |            0.00131|         99.87907|
|101              |            0.00117|         99.88024|
|102              |            0.00111|         99.88135|
|103              |            0.00104|         99.88239|
|104              |            0.00097|         99.88336|
|105              |            0.00106|         99.88442|
|106              |            0.00107|         99.88549|
|107              |            0.00096|         99.88646|
|108              |            0.00090|         99.88736|
|109              |            0.00095|         99.88831|
|110              |            0.00092|         99.88923|
|111              |            0.00101|         99.89024|
|112              |            0.00088|         99.89112|
|113              |            0.00094|         99.89206|
|114              |            0.00085|         99.89292|
|115              |            0.00078|         99.89369|
|116              |            0.00089|         99.89459|
|117              |            0.00089|         99.89548|
|118              |            0.00090|         99.89638|
|119              |            0.00422|         99.90060|
|120              |            0.00596|         99.90656|
|121              |            0.00076|         99.90733|
|122              |            0.00064|         99.90797|
|123              |            0.00057|         99.90853|
|124              |            0.00057|         99.90910|
|125              |            0.00068|         99.90978|
|126              |            0.00056|         99.91034|
|127              |            0.00059|         99.91092|
|128              |            0.00055|         99.91148|
|129              |            0.00060|         99.91207|
|130              |            0.00058|         99.91265|
|131              |            0.00056|         99.91321|
|132              |            0.00053|         99.91375|
|133              |            0.00060|         99.91434|
|134              |            0.00058|         99.91493|
|135              |            0.00054|         99.91547|
|136              |            0.00049|         99.91596|
|137              |            0.00059|         99.91655|
|138              |            0.00054|         99.91709|
|139              |            0.00052|         99.91762|
|140              |            0.00050|         99.91812|
|141              |            0.00044|         99.91855|
|142              |            0.00050|         99.91905|
|143              |            0.00064|         99.91970|
|144              |            0.00055|         99.92025|
|145              |            0.00078|         99.92102|
|146              |            0.03634|         99.95736|
|147              |            0.00160|         99.95896|
|148              |            0.00096|         99.95992|
|149              |            0.00080|         99.96072|
|150              |            0.00087|         99.96160|
|151              |            0.00077|         99.96237|
|152              |            0.00065|         99.96302|
|153              |            0.00040|         99.96342|
|154              |            0.00020|         99.96362|
|155              |            0.00019|         99.96382|
|156              |            0.00018|         99.96400|
|157              |            0.00024|         99.96424|
|158              |            0.00022|         99.96445|
|159              |            0.00022|         99.96467|
|160              |            0.00017|         99.96485|
|161              |            0.00014|         99.96499|
|162              |            0.00017|         99.96517|
|163              |            0.00020|         99.96537|
|164              |            0.00021|         99.96558|
|165              |            0.00017|         99.96575|
|166              |            0.00020|         99.96595|
|167              |            0.00018|         99.96613|
|168              |            0.00016|         99.96629|
|169              |            0.00017|         99.96646|
|170              |            0.00016|         99.96663|
|171              |            0.00017|         99.96679|
|172              |            0.00021|         99.96701|
|173              |            0.00021|         99.96721|
|174              |            0.00018|         99.96739|
|175              |            0.00016|         99.96755|
|176              |            0.00018|         99.96773|
|177              |            0.00020|         99.96793|
|178              |            0.00013|         99.96805|
|179              |            0.00021|         99.96826|
|180              |            0.00014|         99.96841|
|181              |            0.00015|         99.96856|
|182              |            0.00013|         99.96869|
|183              |            0.00017|         99.96885|
|184              |            0.00017|         99.96902|
|185              |            0.00179|         99.97081|
|186              |            0.00015|         99.97096|
|187              |            0.00009|         99.97105|
|188              |            0.00013|         99.97118|
|189              |            0.00013|         99.97132|
|190              |            0.00468|         99.97600|
|191              |            0.00016|         99.97615|
|192              |            0.00019|         99.97634|
|193              |            0.00336|         99.97971|
|194              |            0.01854|         99.99824|
|195              |            0.00031|         99.99855|
|196              |            0.00013|         99.99869|
|197              |            0.00005|         99.99873|
|198              |            0.00007|         99.99880|
|199              |            0.00006|         99.99887|
|200              |            0.00006|         99.99893|
|201              |            0.00006|         99.99899|
|202              |            0.00005|         99.99903|
|203              |            0.00004|         99.99907|
|204              |            0.00005|         99.99912|
|205              |            0.00003|         99.99915|
|206              |            0.00003|         99.99919|
|207              |            0.00003|         99.99922|
|208              |            0.00005|         99.99927|
|209              |            0.00002|         99.99930|
|210              |            0.00003|         99.99933|
|211              |            0.00004|         99.99937|
|212              |            0.00004|         99.99941|
|213              |            0.00005|         99.99945|
|214              |            0.00003|         99.99948|
|215              |            0.00002|         99.99951|
|216              |            0.00002|         99.99952|
|217              |            0.00001|         99.99953|
|218              |            0.00002|         99.99954|
|219              |            0.00001|         99.99955|
|220              |            0.00001|         99.99956|
|221              |            0.00001|         99.99957|
|222              |            0.00001|         99.99958|
|223              |            0.00002|         99.99960|
|224              |            0.00001|         99.99961|
|225              |            0.00001|         99.99961|
|226              |            0.00001|         99.99962|
|227              |            0.00002|         99.99965|
|228              |            0.00002|         99.99966|
|229              |            0.00001|         99.99967|
|230              |            0.00002|         99.99968|
|231              |            0.00002|         99.99970|
|232              |            0.00002|         99.99972|
|233              |            0.00000|         99.99973|
|234              |            0.00001|         99.99973|
|235              |            0.00001|         99.99974|
|236              |            0.00001|         99.99975|
|237              |            0.00001|         99.99976|
|238              |            0.00002|         99.99977|
|239              |            0.00002|         99.99979|
|240              |            0.00002|         99.99981|
|241              |            0.00001|         99.99982|
|242              |            0.00001|         99.99983|
|243              |            0.00000|         99.99983|
|244              |            0.00002|         99.99984|
|245              |            0.00001|         99.99985|
|247              |            0.00002|         99.99987|
|248              |            0.00001|         99.99987|
|249              |            0.00002|         99.99989|
|250              |            0.00001|         99.99990|
|251              |            0.00001|         99.99991|
|252              |            0.00001|         99.99991|
|253              |            0.00001|         99.99993|
|254              |            0.00002|         99.99994|
|255              |            0.00001|         99.99995|
|259              |            0.00001|         99.99995|
|261              |            0.00000|         99.99996|
|264              |            0.00001|         99.99996|
|265              |            0.00000|         99.99997|
|266              |            0.00001|         99.99997|
|267              |            0.00000|         99.99998|
|268              |            0.00000|         99.99998|
|270              |            0.00000|         99.99998|
|272              |            0.00000|         99.99998|
|273              |            0.00000|         99.99999|
|274              |            0.00001|         99.99999|
|277              |            0.00000|        100.00000|
|282              |            0.00000|        100.00000|

## Number of outputs

Some transactions in 2019 have only one output. Those transactions were produced before the two-output-minimum blockchain consensus rule.

|Number of outputs | Share (percentage)| Cumulative share|
|:-----------------|------------------:|----------------:|
|1                 |            0.00609|          0.00609|
|2                 |           94.16030|         94.16639|
|3                 |            1.43294|         95.59933|
|4                 |            0.88349|         96.48282|
|5                 |            0.46521|         96.94803|
|6                 |            0.33533|         97.28336|
|7                 |            0.24259|         97.52595|
|8                 |            0.18496|         97.71091|
|9                 |            0.25809|         97.96901|
|10                |            0.09523|         98.06423|
|11                |            0.25446|         98.31869|
|12                |            0.05823|         98.37693|
|13                |            0.05679|         98.43371|
|14                |            0.04863|         98.48234|
|15                |            0.04930|         98.53164|
|16                |            1.46836|        100.00000|






## kayabaNerve | 2024-10-23T22:25:13+00:00
Please note a 16-output transactions becomes 16 2-output transactions, even if done with logarithmic depth via a binary tree structure. Those additional transactions incur FCMPs which may be more expensive than simply biting the bullet on giving all transactions 4 outputs (even if 96% won't use all of them).

## kayabaNerve | 2024-10-24T15:01:44+00:00
[Curve Forests](https://eprint.iacr.org/2024/1647) is a derivative of the Curve Trees scheme by the same authors. It removes permissibility with a similar trick to the one tevador proposed (adding a generator with a fixed coefficient). It also collapses the the amount of scalar multiplications necessary in-circuit from `O(n + n log s)` to `O(n + log s)` when proving for `n` members at once (with a set size of `s`).

It does this by building `n` trees, where `n` is the maximum amount of elements which can be proven with a single batch. In the worst-case (adding a single element outside of a batch), this causes `n log(s)` point scalings and additions. The notable distinction is in-circuit scalar multiplications are _much more expensive_ that out-of-circuit scalar multiplications.

We use elliptic curve divisors to efficiently verify in-circuit scalar multiplications. We still have two Pedersen Commitments per scalar multiplication in our proof data, which means verifying those requires two point scalings. This immediately makes each in-circuit mul twice as expensive as the out-of-circuit muls, without mentioning the bandwidth savings.

Curve Forests also only publishes `log s` commitments for the branches. We publish `n log s` commitments. This means Curve Forests would notably decrease bandwidth in the multi-input case (from + ~600 bytes to + ~ 200 bytes per additional input). Those decreased commitments also further benefit our computational savings.

It does require a low `MAX_INPUTS` however. If we set `MAX_INPUTS=16`, we have to maintain 16 different trees (5 GB each). `16 log s` scalarmuls per output may not save computational complexity if effectively no transactions actually use so many inputs at once (paying back the cost).

There's also IO cost to the additional trees, which can be discussed. When we're done with the current scheme (either due to having a more efficient scheme or due moving to PQ cryptography), the trees could be pruned. The larger proofs can not (trivially, technically they can with a recursive proof scheme) as they'll be part of the blockchain however.

There's also notably decreased prover time. Proving the scalarmuls are the majority of the complexity for the prover. Wallets would be screwed over however, as they don't benefit from the faster verification time *and now have to build additional trees when they're already more resource-constrained than nodes*. 

I first made some initial notes in MRL on this a week ago. It fits quite nicely into the current discussion on an input limit. I don't support adopting Curve Forests now yet it'd make sense to potentially improve with in a future hard fork. While @jberman is noting the tree calculation is expensive, this should pay for itself *for nodes*. For wallets, we'd need to verify they can pay the computational cost (potentially requiring SIMD/GPU implementations of tree building). It also enables discussing having wallets download trees again yet I'm very strongly against that idea. Another option would be to discuss PIR so paths can be ad-hoc privately downloaded?

Also, at some point we need to decide if the tree root is going in the header (or at least hashed into the header).

## kayabaNerve | 2024-10-28T20:21:30+00:00
https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898

## kayabaNerve | 2024-10-28T20:26:51+00:00
cc @Rucknium What percentage of blocks include at one TX with >= 8 inputs? What percent include two? (etc)

I maintain my advocacy for 8/4 on a premise of reasonable UX/tolerable performance (though the full set of data hasn't been presented yet), but will likely encourage 4/4 with the most to Curve Forests.

## Rucknium | 2024-10-30T16:22:08+00:00
> cc @Rucknium What percentage of blocks include at one TX with >= 8 inputs? What percent include two? (etc)

Below is a table of this. An example interpretation: The share of blocks with at least two txs with 8 or more inputs is 14.38%.

| Number of qualifying txs in block| Share of blocks| Reverse cumulative share (percentage)|
|---------------------------------:|---------------:|-------------------------------------:|
|                                 1|        18.09951|                              32.48107|
|                                 2|         6.95244|                              14.38156|
|                                 3|         3.40785|                               7.42912|
|                                 4|         1.63593|                               4.02128|
|                                 5|         0.89011|                               2.38534|
|                                 6|         0.50950|                               1.49524|
|                                 7|         0.34223|                               0.98573|
|                                 8|         0.21250|                               0.64350|
|                                 9|         0.13468|                               0.43101|
|                                10|         0.09448|                               0.29632|
|                                11|         0.06510|                               0.20184|
|                                12|         0.03700|                               0.13674|
|                                13|         0.02771|                               0.09974|
|                                14|         0.01896|                               0.07202|
|                                15|         0.01363|                               0.05307|
|                                16|         0.01043|                               0.03944|
|                                17|         0.00944|                               0.02901|
|                                18|         0.00449|                               0.01957|
|                                19|         0.00396|                               0.01507|
|                                20|         0.00274|                               0.01112|
|                                21|         0.00206|                               0.00837|
|                                22|         0.00152|                               0.00632|
|                                23|         0.00114|                               0.00480|
|                                24|         0.00076|                               0.00365|
|                                25|         0.00053|                               0.00289|
|                                26|         0.00023|                               0.00236|
|                                27|         0.00038|                               0.00213|
|                                28|         0.00015|                               0.00175|
|                                29|         0.00015|                               0.00160|
|                                30|         0.00008|                               0.00145|
|                                31|         0.00023|                               0.00137|
|                                33|         0.00015|                               0.00114|
|                                36|         0.00023|                               0.00099|
|                                37|         0.00023|                               0.00076|
|                                38|         0.00008|                               0.00053|
|                                40|         0.00008|                               0.00046|
|                                43|         0.00008|                               0.00038|
|                                45|         0.00008|                               0.00030|
|                                47|         0.00008|                               0.00023|
|                                53|         0.00008|                               0.00015|
|                                54|         0.00008|                               0.00008|

A work-in-progress analysis of the storage and computational cost of different `MAX_OUTPUT` parameter values with very preliminary results is here: https://gist.github.com/Rucknium/784b243d75184333144a92b3258788f6


## kayabaNerve | 2025-02-20T18:21:12+00:00
Side note, I'm not sure about the security of Curve Forests which I discussed above. I don't believe it matters but I don't want someone to do the work on such a HF believing it's fine without further review of the premise. I lean towards it being fine? But review never hurts.

# Action History
- Created by: sethforprivacy | 2022-05-02T17:12:33+00:00
