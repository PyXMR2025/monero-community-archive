---
title: 'Discussion: Post-quantum security and ethical considerations over elliptic
  curve cryptography'
source_url: https://github.com/monero-project/research-lab/issues/131
author: SyntheticBird45
assignees: []
labels: []
created_at: '2024-12-10T21:03:18+00:00'
updated_at: '2025-02-12T17:15:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue has been created to centralize discussion around post-quantum mitigations for next monero hard forks.

### A reminder:
- In 2020, Monero CCS has funded and obtained an academic review of current Monero quantum security: https://github.com/insight-decentralized-consensus-lab/post-quantum-monero/blob/master/writeups/technical_note.pdf. Ring-signatures are compromised, amount can be faked, and wallet seed extracted from a public address.
- In 2022, in the context of the next transaction protocol Seraphis, @tevador produced a gist draft adaptation of the Seraphis protocol with post-quantum security: https://gist.github.com/tevador/23a84444df2419dd658cba804bf57f1a/revisions
- In 2024, Monero project decided to go over [FCMP++](https://raw.githubusercontent.com/kayabaNerve/fcmp-ringct/develop/fcmp%2B%2B.pdf). The question of whether Seraphis will be implemented later mainly boiled down to: *Can FCMP++ have the same feature set as Seraphis*. As of today, it is very unlikely that Seraphis get implemented after FCMP++.
- End of november 2024, KayabeNerve [stepped back](https://gist.github.com/kayabaNerve/e5b262c5efefcfcfa32748a0d99bc0e1) from MRL research and FCMP++ implementation analysis and invited the researcher community to a moratorium on elliptic curve post-quantum security.
- December 9th 2024, Google announces their [quantum computer Willow, equipped with 105 qubits](https://blog.google/technology/research/google-willow-quantum-chip/). There are others companies (and governments) around the world working on much larger quantum computer with ultimate incentives.

### Moratorium

I created this issue because I do agree with @KayabaNerve that there is an ethical aspect in the current MRL roadmap. In most pessimistic scenarios, Y2Q could happen in 5 years, while most optimistic scenarios expect it to happen in ~10-25 years. Pressure is actually mounting in the industry and NIST have already standardized some PQ algorithms (Kyber, SPHINCS+, Dilithium) and more are waiting to be standardized or being used after study (Falcon, S-NTRU).

**We are at a turning point, where it would become harder for monero users to defend themselves from the total de-anonymization of the blockchain**

10 years is the amount of time, most legal service providers using BTC or XMR are keeping payment information in their database.
10 years is the average amount of time for the statute of limitations in democratic nations
10 years is half the amount of time for the statute of limitations in non-democratic nations (China, Russia).

Monero promises privacy, security and untraceability, and while most users may just hold or spend in perfectly legal situations in their jurisdiction, some users are actually trusting this technology to ensure their freedom of speech or with their live at stake.
That we want it or not, the Monero Project and research community have a part of responsibility in ensuring that future usage of Monero will not retroactively endanger them.

I therefore agree with @KayabaNerve, a parallel effort must **absolutely** be started on implementing post-quantum security for Monero, with ultimate goal to be seen in production in at most 5 years, as FCMP++ and JamtisRCT already provides privacy improvements against a ECDLP solver.

# Discussion History
## jeffro256 | 2024-12-10T22:57:49+00:00
Putting this discussion here for good measure: https://github.com/monero-project/research-lab/issues/106

## kayabaNerve | 2024-12-12T02:03:34+00:00
Switch commitments which bind to the amount are insufficient. A QC cannot forge how much they're worth yet can claim a spent output unspent. This is only detectable if we have more XMR migrated than legitimate or more outputs migrated than legitimate.

We need to bind to the addresses and enforce a derivation scheme for them.

An address is derived as follows:

- `Y = y * T`
- `x = H_0(r_0, Y)`
- `v = H_1(r_1, Y)`
- `A = (x * G + Y, v * G)`

For any `y` value, there are `r_0, r_1` values causing a specific address to be derived. We assume a quantum computer cannot find such values however.

Please note the lack of bounds on how `y` is calculated and the lack of use in derivation. This ensures multisignature schemes can migrate.

Switch Commitments, [as originally defined](https://eprint.iacr.org/2017/237.pdf), were just ElGamal commitments (not perfectly blinding with a process to switch to perfectly binding). [The proposal for an ElGamal commitment, hashed and summed with the blinding factor in a Pedersen Commitment, was made later as an optimization.](https://lists.launchpad.net/mimblewimble/msg00479.html)

I honestly don't know why that proposal exists as it does. If we assume a QC cannot find a preimage, then simply defining the PC randomness as `H(r)` should be sufficient. While a QC can take a `PC(r, a)` and find `PC(r', a')`, they shouldn't be able to find the necessary preimage for `r'`. Arguably, the intent was to switch over to the ElGamal commitment which is computationally hiding for all adversaries without a QC? But you have to publicize the randomness which strips all privacy anyways.

If we define the PC randomness as `H(address, randomness)`, in the future, we can use a PQ ZK proof to:

- Provide the opening of the PC
- Provide the preimage for the PC randomness
- Provide the preimages for the address
- Perform the output key derivation

If an adversary with a QC attempts to open the PC with distinct randomness, they'll lack the preimage. If an adversary with a QC attempts to open the address `x * G + y * T` ` with `x', y'`, they'll lack the preimage for `x'`.

This allows us to provide key images for outputs made under FCMPs++, without forgeries, even once a QC exists. The ability to prove key images is the ability to maintain proving transactions weren't prior spent *and ownership*.

An adversary with your address can find the outputs you've received. They cannot immediately find the place of spend given an address with a `y * T` term as it's unknown the split between the `x * G, y * T` terms. In practice, they can calculate the `x` term and accordingly the `y` term (if two outputs are spent, via some large tables). This would be insufficient to migrate an output. You'd still need `r_0, r_1` which is presumed incalculable to everyone, even those with a QC.

A malicious output which sends to address A yet claims to send to address B can be created, as described in #130. The sender would not know the discrete logarithms for the address B without a QC if randomly selected. With a QC, they wouldn't know the necessary preimages. Address B can be derived from the discrete logarithms of A, but again, without the necessary preimages.

A few notes:

1) I'll email Ruffing asking why use a hash of an ElGamal commitment instead of a hash of the addesss.

2) tevador also proposed a key derivation hierarchy. I don't mean to usurp it. I put a candidate here which works with multisigs to some degree. Anyone in the multisig *with a quantum computer* can perform the migration/someone has to be trusted with `r_0, r_1`/you need a very complicated MPC protocol. If tevador's proposals has the same properties, I'd defer, else I'd suggest reconciliation of the two.

Prior designs were about embedding a PQ signature verification key into addresses, avoided here by defining knowledge of `r_0, r_1` as the signature (within some very large migration proof). Defining at least one of those as a PQ verification key would enable transparently opening historical outputs while achieving the same properties here, except that'd strip the entire wallet of privacy (whereas this scheme is completely private). A ZK proof could be used to extract the PQ verification key, which would be of similar complexity to the proof this scheme requires and enable performing the signature itself *outside of this large proof* (akin to separation of membership and spend-authorization). That would reveal how many outputs a key owned unless we re-randomize the verification key or verify its signature in a ZK proof, and requires us to commit to a PQ signing scheme now. It also only benefits multisig if there is a DKG for the PQ signing scheme available now.

3) We still have to ban spending of FCMP++ outputs before a sufficiently powerful QC goes online, only allowing their migration as described here.

4) How we hash the address should be considered. It's probably ideal if it's a bit for if subaddress, a bit for if the spend key's x coordinate is odd, a bit for if the view key's x coordinate is odd, the spend key's y coordinate, and the view key's y coordinate.

## kayabaNerve | 2024-12-12T12:40:56+00:00
#105 for the existing switch commitments issue.

https://github.com/kayabaNerve/monero-pq for my initial sketches of commitments for a PQ composition.

## jeffro256 | 2024-12-13T08:03:19+00:00
> `A = (x * G + Y, v * G)`

We can't have this relationship for addresses if we want to support subaddresses. The relationship between <code>K<sub>s</sub><sup>j</sup></code> and <code>K<sub>v</sub><sup>j</sup></code> must be <code>K<sub>v</sub><sup>j</sup> = k<sub>v</sub> * K<sub>s</sub><sup>j</sup></code></code>, where <code>k<sub>v</sub></code> is the private view-incoming key (some fixed scalar). So <code>A = (x * G + Y, k<sub>v</sub> * (x * G + Y))</code> might work. However, we wouldn't want to bind to `A` in the PC randomness because that would mean revealing <code>k<sub>v</sub></code> to a quantum computer since they could find the discrete log between <code>K<sub>s</sub><sup>j</sup></code> and <code>K<sub>v</sub><sup>j</sup></code>. At a fundamental level, the verifiers don't need <code>K<sub>v</sub><sup>j</sup></code> at all anyways, since what we're doing here is proving ownership and unspentness, which are functions of <code>K<sub>s</sub><sup>j</sup></code> (and the one-time sender extensions).

I'm confused as to why we should include `A` in the commitment randomness at all? Let's say that we're in the stage of post-switch, where full verification of amount commitments is required. At this point, we are not assuming hardness of the discrete log anymore. As such, FCMPs break down, so we should not be using them. We should be explicitly indexing the outputs to be spent in the ledger. Obviously, this is bad for privacy, but it's the only way unless we want to spent the time to researching, implementing, and integrating post-quantum secure membership proofs on our existing anonset solely for the purpose of inputs in migration transactions. And if we are explicitly indexing inputs, then the output pubkey is available unambiguously.

I do agree though, that without a post-quantum secure range proofs on El Gamal commitments, making the PC blinding factor a function of some El Gamal commitment is pointless, since we need to reveal the blinding factor anyways. If we're revealing the blinding factor, a simple preimage will suffice. 

## kayabaNerve | 2024-12-13T16:14:10+00:00
Heard regarding subaddresses instead of standard addresses, as I sketched.

> However, we wouldn't want to bind to A in the PC randomness because that would mean revealing kv to a quantum computer since they could find the discrete log between Ksj and Kvj. 

This isn't true if we open in a ZK proof as I proposed.

> At a fundamental level, the verifiers don't need Kvj at all anyways, since what we're doing here is proving ownership and unspentness, which are functions of Ksj (and the one-time sender extensions).

This isn't true as unspentness requires a functioning key image system. A functioning key image system requires binding to a spend key, its `x * G` term, and the view key (to bind to the 'one-time sender extensions').

> I'm confused as to why we should include A in the commitment randomness at all?

So key images still work.

> As such, FCMPs break down, so we should not be using them.

But key images wouldn't.

> We should be explicitly indexing the outputs to be spent in the ledger. 

This still requires knowing if unspent or not which requires a functioning key image system. The exact attack is I have 100 XMR now, churn it 1,000 times, then migrate each output once for a total of 100,000 XMR despite 999 of those outputs having already been spent.

> And if we are explicitly indexing inputs, then the output pubkey is available unambiguously.

It has infinite key images with FCMPs++, to an adversary with a QC, and isn't sufficient by itself.

## jeffro256 | 2024-12-13T18:59:24+00:00
> This isn't true as unspentness requires a functioning key image system. A functioning key image system requires binding to a spend key, its x * G term, and the view key (to bind to the 'one-time sender extensions').

We don't need the address view pubkey if we provide a way to derive the one-time sender extensions with a hash, not letting the prover actually provide them. And then we shouldn't need the address *spend* pubkey either if we make proving secret knowledge of some random address intractable for QCs, as you're suggesting. Let's say that we are given an address spend pubkey <code>K<sub>s</sub><sup>j</sup></code> and some shared secret `R`. Let's say our addressing protocol defines <code>k<sub>o</sub><sup>g</sup> = ScalarDerive("... h .. ", ..., R)</code> and  <code>k<sub>o</sub><sup>t</sup> = ScalarDerive("... t .. ", ..., R)</code>. Then the sender constructs the output pubkey <code>K<sub>o</sub> = K<sub>s</sub><sup>j</sup> + k<sub>o</sub><sup>g</sup> G + k<sub>o</sub><sup>t</sup> T</code>. It can be shown that for an existing output pubkey <code>K<sub>o</sub></code>, it is intractable to find `R'` and derive an target address spend pubkey <code>K<sub>s</sub><sup>j</sup>'</code> such that <code>K<sub>s</sub><sup>j</sup>' =  K<sub>o</sub> - k<sub>o</sub><sup>g</sup>' G - k<sub>o</sub><sup>g</sup>' T</code>. So that solves the address binding issue, as long as we are verifying that address opening for random addresses is intractable. However, I'm still open to including <code>K<sub>s</sub><sup>j</sup></code> in the hash for the PC blinding factor for good measure, since it will be revealed anyways.  And if we bind to just <code>K<sub>s</sub><sup>j</sup></code>, then we don't need a ZK proof on the blinding factor to not reveal the private view key. 

> It has infinite key images with FCMPs++, to an adversary with a QC, and isn't sufficient by itself.

But all of them are intractable to find, even with a QC, if we verify addresses to be constructed a certain way. I understand that we need key images to be intact for the migration, but I'm saying we *also* need to not use FCMPs for the membership part of the proofs, since a QCs can fake an element being inside a set with FCMPs, but they can't fake a fetch from a DB. Thus, we need to reference outputs explicitly *and* do key images checks *on that output pubkey*.




## kayabaNerve | 2024-12-13T20:14:50+00:00
I never proposed using FCMPs at this point (at least, never on purpose). See my third note. I proposed a PQ ZK proof for the migration itself.

If we don't create "addresses" as I originally stated, yet the root key pair, subaddresses still work so long as the future migration proof performs subaddress derivation in-circuit. I do hear I didn't say anything about subaddresses, agree those are critical, and would be fine only supporting subaddresses to be honest.

I'd love to discuss further optimizations. I'm discussing chucking everything to what would be a complicated, expensive, future proof. If we can achieve less work within that proof, or remove the need for it to be ZK entirely, great. I can't yet comment on your sketch above but will try to do so later.

## kayabaNerve | 2024-12-13T21:59:37+00:00
Root key pairs now are `x G, v G`. They'll become `x G + y T, v G`. Subaddresses are currently derived by adding an `s G` term to the spend key and defining a public view key as prior described by jeffro256. I assume this continues to hold CARROT (which isn't true but I want to provide the simpler analysis immediately).

I prior wrote about `x, y` with `x` being secret. This was backwards. `x` is the secret in legacy but here, `y` should be the secret as this is a new scheme which can take advantage of that. Apologies there.

We generate `y` however. We generate `x` as a hash of `y T` with an additional `r` (which becomes the PQ private key or is a PQ public key).

CARROT defines an $o_g, o_t$ (my own notation, please forgive me @jeffro256) to re-randomize the public spend key into the output's one time key.

Fundamentally, the inevitable migration requires verifying the root public spend key, its derivation into a subaddress public spend key, and its derivation into a one-time-key.

I'll repeat the obvious, hard constraints:
- There's no bounds on how `y` is generated
- `x` binds to `y T`

I'll add the correction `x` must bind to a Proof of Knowledge for `y` over `T`. Else, an `x` can be generated which binds to `1 G + y T` which can be opened to `x' = x - 1`. By requiring a PoK committed to when the output is created (before QCs), we prevent this issue.

This means we to verify $(x + s + o_g) \cdot G + (y + o_t) \cdot T = O$, the preimage proofs for $x, s, o_g, o_t$, and the PoK for `y` within the `x` variable's preimage. All preimage proofs have to bind to the prior steps to prevent finding independent $x, s, o_g, y, o_t$ variables which combine to a majority of potential points. This means `s` must bind to `x G + y T` and $o_g, o_t$ must bind to `(x + s) G + y T`.

If we don't use a ZK proof, the preimages for each of these terms will be leaked. If there are currently any secrets (such as the ECDH) in there, there must have an additional hash performed so they're no longer present (as already done by CARROT AFAIK) to not be leaked in such an event.

We can generate `v` and the public view key however. If we don't use a ZK proof for migration, the ideal case is everyone only leaks common ownership of the outputs they migrate. Since $o_g, o_t$ for each output on-chain shouldn't be recoverable, leaking $x, y, s$ shouldn't be an issue. I'd have to sit down and do a lot of double checking however.

CARROT does have a multiplicative scalar in its subaddress derivation. That needs to have its preimage proven for, and derivatives checked, as $s$ was written about here.

I'll also clarify the multisig migration path. A multisig generates `y` however and then decides a PQ key. My best solution at this time is for everyone to have a copy of the PQ key. Then, when it comes time to migrate, we also require a signature for the migration TX by $y$. This requires the multisig sign off on it or one of the multisig members to have access to a QC, a decent hurdle.

If we are to decide a PQ scheme now, instead of expecting a ZK proof to open `x`'s preimage, I'd suggest a scheme derived from Lamport with 2**16 uses supported.

Since I'm unhappy with the idea of some giant ZK-STARK doing several Blake2s proofs, I believe the loss in privacy to solely 'common ownership of these outputs, prior unspent' is acceptable. If anyone wishes to not face the loss in privacy, they can migrate while the PQ scheme simultaneously runs, before we disable spending FCMP++ outputs with the ECC proofs.

With all of the above, then Carrot Pedersen commitments can just have their randomness be the hash of their randomness (as @jeffro256 pointed out). Its the key itself which enforces its own verifiability after the fact. I'm sorry for not realizing that's what you were communicating sooner, jeffro. It entirely slipped past me. This scheme here probably just redoes the key scheme tevador already did. This can be done as a distinct topic entirely from switch commitments (with distinct timing too).

## jeffro256 | 2024-12-16T19:27:27+00:00
I agree with almost everything here, and what's nice about this scheme is that no modifications to Carrot need to be made to support switch commitments without revealing the private view key. Since the PC blinding factor is already defined as a hash of a hash of the ECDH pubkey, we can reveal the hash of the ECDH in the PQ migration.

The one thing that we can't do currently is:

> This means `s` must bind to `x G + y T` and `o_g , o_t` must bind to `(x + s) G + y T`.

We cannot bind the one-time sender extensions to the subaddress spend key because the the receiver doesn't know which subaddress they are scanning for until they unwrap it, which is known *after* calculating the extensions and subtracting from the one-time output pubkey. JAMTIS was able to solve this by encrypting the "address tag" to the receiver, a bit of information which told the receiver which subaddress was the target. However, if we want to support legacy addresses, we don't have this luxury. 

## jeffro256 | 2024-12-16T20:01:01+00:00
Actually I will propose one difference: including the amount in the hash-to-PC-blinding-factor. Consider the two constructions:
<code>C<sub>1</sub> = H<sub>n</sub>(r) G + a H          (no 'a' in hash)
C<sub>2</sub> = H<sub>n</sub>(r, a) G + a H        ('a' in hash)
</code>

If a quantum adversary randomly generates `r'` and computes <code>a' = dlog<sub>H</sub>(C<sub>1</sub> - H<sub>n</sub>(r') G)</code> there is an 2<sup>64</sup>/ℓ chance that `r'` is valid for *some* amount <code>a' < 2<sup>64</sup></code>, with the expected value of `a'` being 2<sup>63</sup> pXMR (about 50% current supply). Brute forcing this commitment scheme gives us about 94 bits of security against quantum computers (see [this tevador comment](https://github.com/monero-project/research-lab/issues/105#issuecomment-1233417496) for the math). 

Now consider the second scheme, brute forcing pairs of `r', a'` and computing <code>a'' = dlog<sub>H</sub>(C<sub>2</sub> - H<sub>n</sub>(r', a') G)</code>, such that `a'' == a'`, only gives a success chance of 1/ℓ instead of 2<sup>64</sup>/ℓ. This should get us closer to log<sub>2</sub>(ℓ)/2 bits of security (~126). 

## kayabaNerve | 2024-12-17T02:05:48+00:00
Completely heard on also binding to the amount.

What if we remove commitments as soft targets and bind to the spend key there? Then the output key map check can be done to find which spend key was sent to, and then we can recreate the commitment.

Spitballing, I haven't considered the consequences of that at all. I know you threw out amenability earlier to that idea but I'm unsure you fully scoped it when you did, jeffro.

## jeffro256 | 2024-12-17T08:26:05+00:00
I think binding to the address spend pubkey <code>K<sub>s</sub><sup>j</sup></code> in the PC blinding factor <code>k<sub>a</sub></code> is feasible, and shouldn't affect the overall scanning flow. Here's the proposed chain of calculation dependencies if we bind the blinding factor to both the amount and address spend pubkey:

![carrot_dependencies_sender](https://github.com/user-attachments/assets/5917d2dc-5f47-4921-b2c2-630bc3cf601b)

![carrot_dependencies_receiver](https://github.com/user-attachments/assets/036daad4-ee09-45d6-9e13-eeb7f481e7e5)

Both are DAGs. Also, the receiver *still* doesn't need a subaddress lookahead table to recompute amount commitments since they can unwrap <code>K<sub>s</sub><sup>j</sup></code> from <code>K<sub>o</sub></code> using the one-time sender extensions <code>k<sub>o</sub><sup>g,t</sup></code>, which are functions of the public amount commitment value (already available) and the contextualized sender-receiver secret <code>s<sub>sr</sub><sup>ctx</sup></code>, a function of ECDH.


## Kreyren | 2025-01-25T08:24:42+00:00
Referencing Xanadu's blog post released on 22nd Jan 2025 about their implementation of fault-tolerant, networked, scaleable quantum computing at room temperature that if i am understanding the post correctly could be used to efficiently build a quantum computer that is resourceful enough to threaten the monero's cryptography.

* https://xanadu.ai/blog/lighting-up-the-quantum-computing-horizon-with-aurora

In addition to the claims by IBM Senior Vice President about the timeline for quantum computers which i consider credible and strategy of harvest now decrypt later and from my following of cybersecurity and recommendation from experts i understood that such event is recognized as a breaking point for non-PQ cryptography for me as a system administrator that manages open-source code as infrastructure that provides a public monero node to take it offline.

* https://github.com/Arcanyx-org/NiXium/commit/8ebb723fee3418164abf26752df44dad5c83e630

I am sharing this to spread awareness about it and in case i am wrong/over-reacting to change the approach to this issue.

## SyntheticBird45 | 2025-01-25T13:36:23+00:00
> Referencing Xanadu's blog post released on 22nd Jan 2025 about their implementation of fault-tolerant, networked, scaleable quantum computing at room temperature that if i am understanding the post correctly could be used to efficiently build a quantum computer that is resourceful enough to threaten the monero's cryptography.
> 
>     * https://xanadu.ai/blog/lighting-up-the-quantum-computing-horizon-with-aurora
> 
> 
> In addition to the claims by IBM Senior Vice President about the timeline for quantum computers which i consider credible and strategy of harvest now decrypt later and from my following of cybersecurity and recommendation from experts i understood that such event is recognized as a breaking point for non-PQ cryptography for me as a system administrator that manages open-source code as infrastructure that provides a public monero node to take it offline.
> 
>     * [Arcanyx-org/NiXium@8ebb723](https://github.com/Arcanyx-org/NiXium/commit/8ebb723fee3418164abf26752df44dad5c83e630)
> 
> 
> I am sharing this to spread awareness about it and in case i am wrong/over-reacting to change the approach to this issue.

Thanks for the news. Current state discussed in meeting is:
- Monero is still not economically secure to QC, switch commitments are going to be implemented to later on transparently revel amounts in a PQC migration
- With FCMP++/Carrot, on-chain data alone can't be used to break privacy with a QC, A QC can reveal amount/sender/receiver of transactions associated with a wallet in if it have access to a public address.
- Carrot introduce quantum resistant churning (self send transaction cannot be decrypted by a quantum computer)
- To mitigate this one left privacy issue, we should use post-quantum cryptography based addresses, but the address size is a problem. ed25519 public keys are 32 bytes, ML/FN/SLH public key or signatures are in the order of kilobytes. Unpractical UX wise and poses scalability challenges.

Hopefully someone will rectify me if I missed something

## kayabaNerve | 2025-01-25T20:58:28+00:00
@Kreyren Your claim such computers are believed to be available isn't a widely-held, nor well-founded, belief. They're a likelihood over the next 5-10 years.

## Kreyren | 2025-01-27T16:25:39+00:00
> @Kreyren Your claim such computers are believed to be available isn't a widely-held, nor well-founded, belief. They're a likelihood over the next 5-10 years. -- @kayabaNerve (https://github.com/monero-project/research-lab/issues/131#issuecomment-2614097709)

I don't think that your date prediction is accurate and i do believe it to be an obsolete observation so first lets establish how many qbits are needed to break modern encryption encryption from the quote i got from cybersecurity and personal research:
* RSA-2048 = 4000-5000 qbits (Shor's algorithm)
* RSA-3072 = 6000-7000 qbits (Shor's algorithm)
* ECC-384 = 3000-4000 qbits (Shor's algorithm)
* AES-256 = Grover's algorithm could reduce the effective key lenght to 128 bit to then require around 2000 qbits

Using reference from the following paper to establish the needed amount of qubits:

* [Shor's Factoring Algorithm and Modern Cryptography. An Illustration of the Capabilities Inherent in Quantum Computers](https://arxiv.org/abs/quant-ph/0411184)
* https://spectrum.ieee.org/encryptionbusting-quantum-computer-practices-factoring-in-scalable-fiveatom-experiment

Where the understood main problem with QPUs is error correction, cooling and paralellism where the xanadu blog post above claims to have developed chips that are 12 qbits that are fault tolerant, operates at room temperature and is scaleable and nertowrked. That to me seem like a major breakthrough that could enable construction such quantum computer at reasonable economy to break the encryption.

Alternatively IBM claimed to be on the track to release a fault tolerant quantum computer that has over 4000 qbits:

* https://theafricalogistics.com/ibm-to-unveil-largest-quantum-computer-yet-in-2025-revolutionizing-technology-and-industry/
* https://spectrum.ieee.org/ibm-quantum-computer

Or atom computing developing a quantum computer that has 1180 qbits in 2023:

* https://www.newscientist.com/article/2399246-record-breaking-quantum-computer-has-more-than-1000-qubits/

To me that seems like well founded risk that should be managed as if the prediction above is accurate that could mean that we can expect efficient enough quantum computer this year especially considering that they are getting the funding of major governments for it and that the US/NATO deems it a threat to it's national security:

* https://www.japan.go.jp/kizuna/2024/03/100000_qubit_quantum_computer.html
* https://www.quantum.gov

Now i think it's important to acknowledge that there is a lot of contradicting data due to people who seem like bad actors claiming that the threat of quantum computers in relation to encryption is far away etc.. I am not saying that you are bad actor, but rather pointing out that it's important to talk to experts on the subject and to have up to date information such as

* https://www.forbes.com/sites/digital-assets/2024/12/16/from-qubits-to-cryptos-what-quantum-means-for-ai-and-bitcoin/

that claims 13 Million qubits to break BTC in single day or even 295 Million qubits for AES-256:

* https://freemindtronic.com/quantum-computing-encryption-threats-risks/

Which do not seem credible to me considering the references above.

Additionally even if we ignore the encryption monero does not manage "Harvest now, decrypt later" ("HNDL") a strategy that aims to store the encrypted data to be then decrypted at a later date. Which is what most security-oriented projects are trying their best to manage such as OpenSSH:

* https://www.zdnet.com/article/openssh-now-defaults-to-protecting-against-quantum-computer-attacks/
* https://portswigger.net/daily-swig/openssh-9-0-bakes-in-post-quantum-cryptography-to-future-proof-against-attacks

Or messengers such as SimpleX which handles this via implementing NTRU Prime.

So i would argue that at very least Monero should be mitigating HNDL.

---

Please feel free to disprove anything i've said it would help to have more credible and objective information on the subject to decide whether to take my monero node online where the main motivation for me to take it down being that it's used by a lot of people (approx. 50? 80?) and i don't want to expose them to what seems to me as privacy and security nightmare.

Also thanks to SyntheticBird45 for the update, i've found following on the subject:

* https://www.reddit.com/r/Monero/comments/1hj3znq/comment/m37dm81
* https://github.com/jeffro256/carrot/blob/master/carrot.md
* https://ccs.getmonero.org/proposals/cypherstack-carrot-spec-review.html

## SyntheticBird45 | 2025-01-27T17:03:14+00:00
@Kreyren I think you are missing something crucially important in your depiction of the current landscape. 

There is a difference between **physical qubits** and **logical qubits**. 
Logical qubits are the concept of qubit which do not produce computation fault, while physical qubits are the actual physical unit executing an operaton. As of today publicly available information, you require a substantial amount of physical qubits to "emulate" a logical qubit, The way quantum fault-tolerant computation is done, is by mainly make use of the consensus of several physical qbit doing the exact same operation and such computation cannot be stabilized for a useful period of time.

Shor's algorithm estimates are based on logical qubits, not physical ones. [Willow](https://blog.google/technology/research/google-willow-quantum-chip/) quantum computer have made state of the art advancement in fault-tolerance, but by using their 3x3 lattice they still only have 11 logical qubits with an error rate WAY TOO LARGE over a short-period of time for anything useful. You can expect much less efficiency in other quantum computer composed of thousands of physical qubits.

So no, there are no quantum computers available right now that is capable of breaking encryption. And certainly not in 2 years due to the engineering challenge of building such machine even with the necessary knowledge

## kayabaNerve | 2025-01-27T17:12:40+00:00
Beyond the confusion of logical and physical, your belief this is a likely risk now means everything is over. HTTPS, effectively every chat app, authenticated build pipelines... It isn't just about Monero.

I'd ask we drop this topic from here. It doesn't contribute to actionable goals regarding having Monero pass the transition.

## Kreyren | 2025-01-27T18:22:54+00:00
If i may, i tried to discuss PQ with the monero community (on matrix and IRC and ideally i would like to have it in a way that can be referenced in my infrastructure to have it constructive), but it seems that none has experience in this area and it's very difficult to get credible information. Could you recommend me a different place to ask so that i can figure out a threat model?

Or ideally elaborate on the HNDL Management as well.

Feel free to ignore this reply if it's not constructive here.

## Corneliux-lcx | 2025-02-12T17:15:19+00:00
@SyntheticBird45 i don't think you or anyone else is in a position to say what is or isn't possible within the next 2 years.

And it makes perfect sense that we should be prepared ASAP for the worst case scenario.

# Action History
- Created by: SyntheticBird45 | 2024-12-10T21:03:18+00:00
