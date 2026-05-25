---
title: Post-quantum signatures
source_url: https://github.com/monero-project/research-lab/issues/159
author: te-mpe-st
assignees: []
labels: []
created_at: '2026-05-21T10:54:09+00:00'
updated_at: '2026-05-23T07:34:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The purpose of this issue is to serve as a general place of discussion for future post-quantum (PQ) signature schemes for Monero. This issue is primarily based off of @tevador's issue #151 .

## Motivation

FCMP++, as noted in #151 , provides notable improvements to anonymity mechanisms in Monero. Despite this, it still relies on classical elliptical-curve signatures for spend-authorisation.

This allows a quantum-enabled adversary (QEA) to entirely break core mechanics of Monero's architecture, namely, the full breakage of spend-authorisation, leading to theft. [1]

This issue serves as a discussion point for potential candidates for a post-quantum digital signature algorithm (PQ-DSA) to be used, considerations as to transitioning to PQ-DSA, and adjacent topics.

Implementing PQ-DSA in Monero is a nontrivial task, hence, this issue ought be used as a preceding stage to actual implementation and discussions related to such.

## Post-quantum signatures

### Signature types

In the context of PQ-DSA, there are two main types of signature schemes (this is not referring to signature families), stateful and stateless. 

Stateful signature schemes, as the name suggest, have a 'root' secret key which is composed of a seed--a fixed root value--and monotonic counter (ctr), often in the form (seed, ctr). Upon signing, Alice consumes a one-time secret key derived from the root key and increments ctr. Security guarantees of stateful signature families rely on no two one-time secret keys being reused. A good example is XMSS [2].

In contrast, stateless signature schemes have a pure value for the secret key. The follow the normal functional form, (sk, msg) -> sig. Stateless signature schemes make up the entirety of the recent NIST Post-Quantum Cryptography Standardization (PQCS) [3].

Because of potential state desynchronisation between devices--leading to potential compromise--stateless schemes are the most worthy for consideration.

### Hardness assumptions 

The discrete logarithm problem (DLP) is not considered a hard problem for a QEA.

The following five problems are considered hard and have been used to construct signature schemes.

#### Hashes

Finding the preimage/collision of a cryptographic hash function output is assumed to be computationally hard.  The concept of hash assumptions dates back to at least Ralph Merkle's PhD thesis in 1979 [4]. The Lamport one-time signature scheme dates to the same year [5].

SPHINCS+ is the modern, stateless form of a hash-based signature scheme as opposed to the stateful XMSS and LMS. SPHINCS+ was submitted to the NIST PQCS in 2017, standardised by NIST in 2024 [6]. It's considered one of the more conservative approaches.

SPHINCS+ suffers from large signature overhead, signatures range from roughly 8 KB to 49 KB depending on the security level.

#### Lattices

> Finding a short vector in a multidimensional lattice is assumed to be computationally hard. A large number of PQ cryptosystems are based on this assumption. 
(#151 )

Equivalently, solving the module learning-with-errors problem (MLWE) is also assumed to be computationally hard. 

CRYSTALS-Dilithium [7] is based on the latter problem, with schemes such as HAWK [8] and Falcon [9] being based on NTRU assumptions (NTRU-SIS and the Lattice Isomorphism Problem). CRYSTALS-Dilithium is considered to have a balance of security and performance among other PQ-DSAs, with HAWK and Falcon having smaller signatures than Dilithium.  All three options have acceptable verification speeds.

#### Error Correcting Codes

Decoding a randomly chosen linear error correcting code is assumed to be computationally hard. 

Notable code-based signature schemes include CFS [10] and Wave [11]. CFS has large overhead whereas Wave has relatively small signatures and acceptable verification times. However, Wave suffers from large public keys (1-4MB) as with most code-based cryptosystems, limiting usability.

#### Multivariate Quadratic Systems

Solving a system of multivariate quadratic equations over a finite field is assumed to be computationally hard.

Currently, the main notable options are, or are based off of, UOV [12] (Unbalanced Oil and Vinegar). UOV, despite acceptable signature sizes and verification times, suffers large public key sizes (>200KB) as well as certain breaks. SOV [13](Sparse Polynomials-based Oil and Vinegar) claims to reduce public key size, however, it has not yet been put under cryptanalysis as rigorous as that of UOV.

#### Isogenies 

Finding an isogeny between two elliptic curves is assumed to be hard.

The most prominent implementation of isogenies in PQ-DSA is SQIsign [14]. Currently, it offers small key and signature sizes with acceptable speeds. It suffers from a complex signing process.

#### Comparison of algorithms

Table 1 lists a shortened selection of algorithms, key size, signature size, signing and verification times. It is taken from PQShield's NIST Signature Zoo [15].

| Algorithm | Family | pk (B) | sig (B) | sign | verify |
|----------------|-----------|-----------|----------|--------|---------|
| Ed25519 | Elliptic curves | 32 | 64 | 42K | 130K |
| CRYSTALS-Dilithium3 | Lattice (MLWE) | 1952 | 3309 | 529K | 179K |
| Falcon-512 | Lattice (NTRU) | 897 | 666 | 1M | 81K |
| HAWK-512 | Lattice (LIP) | 1024 | 555 | 85K | 148K |
| SPHINCS+ SHAKE-128f | Hashes | 32 | 17088 | 239.8M | 12.9M |
| SQIsign I | Isogenies | 65 | 148 | 101.6M | 5.1M |

*Table 1: Algorithms, key and signature sizes along with signing and verification times of PQ-DSAs compared to Ed25519.*

## References

[1] "The Quantum Menace", A. Faz-Hernández (2019), https://blog.cloudflare.com/the-quantum-menace
[2] "XMSS – A Practical Forward Secure Signature Scheme based on Minimal Security Assumptions", Buchmann et al. (2011), https://eprint.iacr.org/2011/484
[3]  https://csrc.nist.gov/Projects/Post-Quantum-Cryptography
[4] "Secrecy, Authentication, And Public Key Systems", R. Merkle (1979), https://www.ralphmerkle.com/papers/Thesis1979.pdf
[5] "Constructing Digital Signatures from a One Way Function", L. Lamport (1979), https://lamport.azurewebsites.net/pubs/dig-sig.pdf
[6] "SPHINCS+", Aumasson et al. (2022), https://sphincs.org/data/sphincs+-r3.1-specification.pdf
[7] "CRYSTALS-Dilithium", Bai et al. (2021), https://pq-crystals.org/dilithium/data/dilithium-specification-round3-20210208.pdf
[8] "HAWK", Bos et al. (2025), https://hawk-sign.info/hawk-spec.pdf
[9] "Falcon: Fast-Fourier Lattice-based Compact Signatures over NTRU", Foque et al. (2020), https://falcon-sign.info/falcon.pdf
[10] "How to achieve a McEliece-based Digital Signature Scheme", Courtois et al. (2001), https://eprint.iacr.org/2001/010
[11] "Wave: A New Family of Trapdoor One-Way Preimage Sampleable Functions Based on Codes", Alazard et al. (2019), https://www.rocq.inria.fr/secret/Jean-Pierre.Tillich/publications/Wave.pdf
[12] "UOV: Unbalanced Oil and Vinegar", Beullens et al. (2023), https://csrc.nist.gov/csrc/media/Projects/pqc-dig-sig/documents/round-1/spec-files/UOV-spec-web.pdf
[13] "An Efficient MQ-Signature Scheme based on Sparse Polynomials", Shim et al. (2020), https://www.researchgate.net/publication/338959585_An_Efficient_MQ-Signature_Scheme_Based_on_Sparse_Polynomials
[14] "SQIsign", Aardal et al. (2025), https://sqisign.org/spec/sqisign-20250707.pdf
[15] https://pqshield.github.io/nist-sigs-zoo/

# Discussion History
## tevador | 2026-05-21T16:48:17+00:00
None of the PQ DSA algorithms you listed are suitable for Monero.

For Bitcoin, it's enough to have an algorithm that can prove the ownership of the private key corresponding to a specific public key.

For Monero, you need at least the ability to rerandomize a key and prove the ownership of the original private key and the rerandomization in zero knowledge. @kayabaNerve can probably give a more detailed list of requirements. That's why I said it wouldn't be as easy as encryption, which can use existing algorithms without changes.

## te-mpe-st | 2026-05-21T23:18:41+00:00
In that case, I'll put the following here.

Might DilithiumNK [1] or CSI-{FiSH, SharK}[2] be viable? I took interest in the latter, as it's somewhat similar to CSIDH's mechanics.

[1]https://cic.iacr.org/p/2/3/3
[2]https://www.sciencedirect.com/science/article/abs/pii/S0304397525000659

## kayabaNerve | 2026-05-22T00:12:13+00:00
Per my barely-started chicken scratch of https://github.com/kayabaNerve/monero-pq, we really want a key for which:
1) The keys may be re-randomized
2) We can efficiently re-randomize within the membership proof

I nominated Threshold Raccoon and I don't believe any isogeny-based schemes could even be initially considered as possibly non-interactively rerandomizable. DilithiumRK, with non-interactive re-randomization, would technically be a candidate, but I'd rather focus on applying rerandomization to a scheme with support for threshold multisig than discussing it as an 'off-the-shelf' choice.

## tevador | 2026-05-22T16:24:30+00:00
> I don't believe any isogeny-based schemes could even be initially considered as possibly non-interactively rerandomizable

CSIDH/CSI-FiSH public keys are non-interactively rerandomizable (Jamtis actually uses this property when generating addresses).

The problem of CSI-FiSh and CSI-SharK is that they don't scale beyond the CSIDH-512 security level, so they are not viable.




## te-mpe-st | 2026-05-22T18:31:45+00:00
CSI-FiSh actually can scale [1], it's just very slow (so I don't think we'd prefer it unless it gains a speedup). DilithiumRK and things schemes built on it (such as SPIRIT [2]) apparently can work as TSS, however, the construction looks very intricate. [3]

(T)Raccoon does like enticing. I'm just a bit concerned about the size of the signatures.

[1] https://eprint.iacr.org/2023/058
[2] https://dl.acm.org/doi/10.1145/3576915.3623148
[3] https://members.loria.fr/EThome/c2/594760.pdf

## tevador | 2026-05-22T18:48:00+00:00
While SCALLOP/PEGASIS can technically do signatures at higher security levels, they are not merely scaled versions of CSIDH. It's a different type of class group which might have unforeseen security weaknesses due to having a special form. While I don't want to entirely dismiss isogenies, I'm afraid they are not practically usable due to their performance anyways.

## kayabaNerve | 2026-05-22T18:51:33+00:00
For the third link, to quote,

> We introduce a novel threshold signature scheme that achieves highly compact signatures of only 2.6kB for any threshold up to N = 8 users

I wouldn't support a bounded scheme. The notability of Threshold Raccoon is the fact it scales, with constant per-participant broadcast and signing-set-independent signatures. I'm sure there's other schemes we can consider though.

## te-mpe-st | 2026-05-22T21:59:39+00:00
> While I don't want to entirely dismiss isogenies, I'm afraid they are not practically usable due to their performance anyways.

I was concerned about that. In that case, I think until more research comes out, I'll shelve it.

On account of lattices, Raccoon-based schemes seem to be a better option.

On bounded schemes, is there an acceptable bounding? I was looking into Hermine [1] which seems to have very nice properties (FROST-like). Besides that, thoughts on Tanuki [2]?

[1] https://csrc.nist.gov/presentations/2026/mpts2026-3b3
[2] https://csrc.nist.gov/presentations/2026/mpts2026-3b2

## kayabaNerve | 2026-05-22T22:58:39+00:00
> CSIDH/CSI-FiSH public keys are non-interactively rerandomizable (Jamtis actually uses this property when generating addresses).

Apologies, I remember now the discussions re: 'subaddresses'. Thanks for the reminder. Very curious to hear...

## kayabaNerve | 2026-05-22T23:34:50+00:00
@te-mpe-st I don't say this for any specific use-case or project. I say this as someone who has built a large-scale deployment of multisig before, and as part of that, can discuss what a signing service looks like.

It isn't just the core cryptography, such as FROST. It's generally also an ideal network assumption, or a non-trivial networking layer. The simplest networking layer I can acknowledge is [ROAST](https://eprint.iacr.org/2022/550), specific to the two-round threshold signature case _with preprocessing_. I prior worked on a two-round signing protocol for ECDSA, published as [Trout](https://eprint.iacr.org/2025/1666), and for our follow-up, Trout++ (not yet published), composing with ROAST was an explicit goal.

If we look at Trout alone, which requires _key, signing-set, and message determination ahead of time_, it almost immediately becomes a three-round protocol. While participants can be sampled to determine a signing set, there's no guarantee they're available. Checking they're available would take a round itself. When the first round is _independent of the signing-set_ however, declaring availability can be done simply by publishing the message for the first round.

A first round independent of the key offers a bit more flexibility, but isn't an explicit goal in my opinion. Sometimes, being key-independent enables derivative schemes, which may matter re: topics such as rerandomization, but lacking such an explicit goal, it doesn't matter. A first round independent of the message allows... load balancing? One may perform the first round arbitrarily, even when there's no messages to sign, so when there are messages, they already have a head start on the necessary signing protocol for it. It isn't a feature I care for, due to the sensitivity of session management and how the secrets for the first round messages generally allowing recovering the private key (meaning they MUST be securely stored), but it's another discussion.

Preprocessing aside (which isn't limited to just two-round schemes despite me assuming a two-round structure, treating preprocessing as equivalent to the first round), assuming an ideal network practically requires a solution for the Asynchronous Common Subset problem. Solutions for the ACS are _hell_. They generally take several rounds, with cubic or even tesseratic complexity.

One can design a complete signing service with a cryptographic core _and_ such agreement protocols as necessary, producing a singular tailored solution, but then the implementation complexity _dramatically increases_.

These problems don't change at scale, nor for use-case. Everything from a basic 2-of-2 to 666,667 of 1,000,000 have these premises and requirements, unless proven otherwise. That's why it's so important to be mindful when we discuss the cryptographic core all of this will have to be layered on top of.

Unfortunately, the traditional PQ signatures do not neatly transition into having multisignature variants. That's why there's a line of signatures which explicitly support threshold signing, for which Monero would want (as Monero wants the ability to split the spend key) _and which must be indistinguishable to the threshold_ (as else, there's a privacy issue). This means factually, the signature must be of constant size regardless of the threshold.

When we consider the requirements on performance, we generally want the following complexities:
- Publicly verifiable transcripts
- Linear or near-linear verifier complexity ($\mathcal{O}(n)$ or $\mathcal{O}(n log n)$)
- Constant or near-constant prover complexity ($\mathcal{O}(1)$ or $\mathcal{O}(log n)$), though linear is acceptable
- Constant or near-constant upload complexity ($\mathcal{O}(1)$ or $\mathcal{O}(log n)$) in the bulletin board model (a blockchain, consensus protocol, trusted coordinator)

Note the signature should have constant verification complexity. When I say verifier complexity, I mean that verifying the _multisig transcript_ should be linear to the amount of participants in the signing set. Then, for a verified transcript, the prover should continue with a sublinear amount of computation to produce their share of the signature.

I'd say _aggregation_, where a semi-trusted coordinator can verify the multisig transcript and produce a sub-linear transcript to continue signing with, is _nice but not required_. For FROST, the first round publishes commitments to nonces and a semi-trusted coordinator may combine them. This coordinator _can not_ cause a forgery but _may_ force the protocol to fail (by going offline or publishing an incorrect summary). These combined commitments than have size independent to the size of the signing set, but are sufficient for the signers to then produce their signature share. This allows each participant to download a constant-size amount of bytes, achieving an _amortized constant communication complexity_ (as only the coordinator has linear community complexity, but only 1/n participants are the coordinator).

These are strenuous requirements, but the fact is, this is what's necessary for a scheme to scale and remain practical, especially when we then discuss networking which will fundamentally increase the overhead of the scheme.

For [Hermine](https://eprint.iacr.org/2026/419) (for which I link the paper, please do not link powerpoints for review), we have:

- Two rounds
- Preprocessing independent of the message, signing-set, but dependent on the key
- Non-interactive identifiable abort (the only IA I care about, and I also think IA is necessary)
- A signature independent of the signing set

I'm unclear the literal complexities of the preprocess, signing round. They technically seem dependent on the threshold, but practically, preprocess may be constant while sign may be linear computationally with constant upload , which would be fine. I don't see a fundamental reason this is limited to 'medium' sizes, and assume that's simply due to having these linear complexities... Perhaps it's better described as 'targeting' medium than 'for' medium.

Also, Threshold Raccoon and Hermine both produce Raccoon signatures (hence why the signature is independent to the signing set). This would mean Monero would simply use Raccoon and the choice of threshold protocol would be left to users, us being confident we have a threshold-friendly signature.

---

I can't seem to find a paper for Tanuki, but they also output a Raccoon signature. The [NIST preview](https://csrc.nist.gov/csrc/media/Projects/threshold-cryptography/documents/TCall-1/Tanuki-PW01.pdf) notes a trusted setup, which may simply be due to their time constraints or may be a more fundamental problem. They seem to have the same preprocessing properties and same complexities for preprocess/sign as Hermine. I'm unsure if they have any practical differences at this time, other than how Hermine advertises a proper DKG.

---

All this really goes to say, IMO, Raccoon is the best candidate for Monero's PQ signature at this time _if_ we solve for non-interactive re-randomization.

## te-mpe-st | 2026-05-23T00:56:49+00:00
My fault on the slides part, I didn't realise that's what I linked (I had several links open at the time) I've also linked the preview writeup spec for [Tanuki](https://csrc.nist.gov/csrc/media/Projects/threshold-cryptography/documents/TCall-1/Tanuki-PW01.pdf) for that reason (as I do not believe the full paper itself is published.)

Given your experience over mine as well as the arguments presented, I now must agree with the conclusion.

## kayabaNerve | 2026-05-23T01:01:54+00:00
No worries. It's a broad topic and full of complexity. There's a bunch of considerations, which is why I want to ensure the core signature is amenable to threshold protocols themselves amenable to deployment (not just theoretical usage under ideal circumstances). For now, it seems like Raccoon is the solution within the Monero protocol itself _if a non-interactive, public-key rerandomization scheme is developed_.

We can be concerned about the signature sizes, though any PQ scheme will be notably larger regardless, across all proofs. We have two options:

1) Provide a succinct proof the signature exists, either at a transaction level or even the block level
2) Adopt a distinct signature scheme, in which case our struggle will be finding a signature scheme with the desired threshold signing protocols

Both are options, but adopting a scheme without feasible threshold signatures isn't an option unless we effectively want to drop threshold signing.

## te-mpe-st | 2026-05-23T05:51:37+00:00
Has [Raccoon-G](https://eprint.iacr.org/2026/380) already been ruled out due to size?

I'm also somewhat (?) concerned about it because it's new and therefore may have unforeseen security risks like related key attacks.

## kayabaNerve | 2026-05-23T07:30:32+00:00
I'm unsure it was considered as there isn't a group actively working on this. Skimming it, it appears to be what I said our work would be, with the exception it changes the distribution of private keys in a way which may affect the applicability of threshold signature schemes (even though the modified distribution is presented by the Threshold Raccoon paper, which doesn't quite achieve all desirable goals, so then the question is about a Hermine or similar for so-distributed private keys).

The distributions of the signatures also are different based on the amount of key derivations, though Monero could fix the amount of derivations to a constant. The concern is that this may prevents using other private key distributions to produce Raccoon signatures, and this distribution is noted to be more difficult to perform in constant time.

TL;DR Yes, is the rerandomization scheme I said would be needed. You need someone to sit down and do a full analysis on all of these papers and their combined result for Monero though. One key aspect is we need to perform this re-randomization inside the membership proof.

# Action History
- Created by: te-mpe-st | 2026-05-21T10:54:09+00:00
