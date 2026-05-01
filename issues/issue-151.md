---
title: Post-quantum encryption
source_url: https://github.com/monero-project/research-lab/issues/151
author: tevador
assignees: []
labels: []
created_at: '2025-10-24T10:50:46+00:00'
updated_at: '2026-04-29T16:59:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The purpose of this issue is to discuss the post-quantum (PQ) encryption algorithm selection for Jamtis - the next addressing scheme for Monero.

## Motivation

FCMP++ will be shipping with Carrot [1], which is a CryptoNote-compatible addressing scheme. Carrot already brings several forward-secrecy improvements, notably:

1. A quantum enabled adversary (QEA) is not able to construct a transaction graph just by observing the blockchain.
2. Several parts of the transaction protocol use symmetric-key derivations that are PQ secure. This includes address generation and internal enotes.

However, if a QEA learns just one wallet address, they can deanonymize a large portion of the wallet's transaction history, including:

1. All incoming external enotes with their amounts.
2. In some cases, the spends of such enotes (this requires at least 2 enotes received to the same wallet address to be spent).

The purpose of Jamtis is to provide forward secrecy against a QEA even if a wallet address is publicly known or under a stronger assumption that the address-generator wallet tier is leaked.

Achieving the above goal boils down to selecting a suitable PQ public key encryption scheme.

## Post-quantum encryption

### Key exchange types

When talking about PQ encryption algorithms in a blockchain setting, it is important to distinguish between non-interactive key exchange (NIKE) and a more general key encapsulation mechanism (KEM).

#### Non-interactive key exchange (NIKE)

With a non-interactive key exchange, Alice and Bob can establish a shared secret just by knowing each other's public keys. If Alice's public key is `A = a * G` and Bob's public key is `B = b * G`, then their shared secret is `a * B = b * A`. Here the symbol `*` refers to the application of some secret action on a public key and `G` is a common base key.

Notice that the action `*` must be commutative: `(ab) * G = (ba) * G`. The most common example is scalar multiplication in an elliptic curve group or in the multiplicative group of integers modulo a prime, which was the first public key algorithm published by Diffie and Hellman in 1976 [2].

The advantages of NIKE for Monero are two-fold:

1. NIKE allows multiple recipients to use the same public key to calculate a shared secret with the sender of the transaction. It means that a 16-output transaction still only needs one public key.
2. The fact that NIKE applies a secret action directly to a public key allows for rerandomizations of a public key. This means that the address-generator wallet tier can generate unlinkable addresses without the knowledge of the resulting decryption key.

#### Key encapsulation mechanism (KEM)

KEM is a generalized key exchange for algorithms that don't have the symmetry needed for NIKE. Most PQ key exchange algorithms belong to this category.

With a KEM, Alice takes Bob's public key `B` and mixes it with some randomness `a`, which produces a shared key and a ciphertext. Bob can then decrypt the ciphertext with his private key `b` to get the shared key. Notice that Alice has no defined public key in this process.

If Alice wants to communicate with Bob and Charlie, she needs to produce two different ciphertexts, one using Bob's public key `B` and one using Charlie's public key `C`.

This has two implications for Monero:

1. A multi-output transaction needs to contain one ciphertext per recipient.
2. There is no way to rerandomize a public key, which means the address-generator tier can always decrypt transactions.

### Hardness assumptions and protocols

The discrete logarithm problem (DLP) is not considered to be hard to solve for a QEA.

The following 3 problems are assumed to be hard and have been used to construct PQ key exchange protocols:

#### Error correcting codes

Decoding a randomly chosen linear error correcting code is assumed to be computationally hard. One of the first public key cryptosystems, published in 1978 by R.J. McEliece [3], is based on this assumption. This cryptosystem has withstood almost 50 years of cryptanalysis and is considered to be one of the most secure choices for PQ encryption.

A modern version of the McEliece cryptosystem was submitted to the NIST Post-Quantum Cryptography Standardization (PQCS) [4], where it advanced to the 4th round, but was not selected for ratification.

Besides high security, classic McEliece also has a very small ciphertext size, which is convenient for blockchain transaction sizes. Unfortunately, its usability is limited by the large public key size. 

#### Lattices

Finding a short vector in a multidimensional lattice is assumed to be computationally hard. A large number of PQ cryptosystems are based on this assumption. This includes CRYSTALS-Kyber [5], which was standardized by NIST in 2022. Other notable cryptosystems are NTRU [6] and NTRU Prime [7], which also participated in the NIST PQCS and both advanced to the 3rd round.

Lattice-based cryptosystems have public keys and ciphertext sizes of around 1 KB and offer high security and high speed. However, some of the proposed cryptosystems might be covered by patents (for example US9094189B2 and US9246675B2).

#### Isogenies

Finding an isogeny between two elliptic curves is assumed to be hard. A prominent cryptosystem based on this assumption was SIKE [8], which advanced to the 4th round of the NIST PQCS, but was completely broken by a classical attack in 2022 [9]. The attack on SIKE doesn't imply that the isogeny hardness assumption is wrong becaue SIKE implicitly used a much stronger assumption.

CSIDH (pronounced "sea-side") is another cryptosystem based on isogenies. It was published in 2018 [10], so it didn't participate in the NIST PQCS. CSIDH uses a commutative action, so it's a rare example of a PQ NIKE. All known classical attacks on CSIDH have exponential complexity, but a subexponential quantum attack is known [11], which somewhat reduces the security of CSIDH compared to the previously mentioned cryptosystems.

### Comparison of algorithms

Table 1 lists a selection of PQ key exchange algorithms, resulting Jamtis address sizes and approximate pruned transaction sizes.

I selected the smallest proposed parameter sizes for classic McEliece [4] and NTRU [6] and the two smallest parameter sizes for CSIDH [10]. Curve25519 is listed for comparison.

| Algorithm | Type | Address size | 2/2 tx size | 2/16 tx size |
|-----------|------|--------------|--------------------|---------------|
| Curve25519 | NIKE | 244  | 278 | 2021 |
| McEliece-3488 | KEM | 418000 | 374 | 3557 |
| NTRU-509   | KEM  | 1363 | 977 | 13205 |
| CSIDH-512  | NIKE | 346  | 342 | 2085 |
| CSIDH-1024 | NIKE | 449  | 406 | 2149 |

*Table 1: Address sizes and pruned transaction sizes of various PQ key exchange algorithms in comparison with Curve25519.*

Pruned transaction sizes include a 32-byte key image per input and a 32-byte output key, 32-byte commitment, 32-byte ephemeral key, a 3-byte view tag, a 8-byte encrypted amount, a 16-byte encrypted Janus anchor and the required PQ key material for each recipient.

Classic McEliece has acceptable blockchain cost, but results in unusably large addresses. It's therefore disqualified.

NTRU (and other lattice-based cryptosystems) would require addresses longer than 1300 characters and would significantly increase the pruned sizes of all transactions (up to 6x for 16 outputs). If there were no alternatives, I think these costs might be acceptable, but it would have a negative impact on the uptake of Jamtis and willingness of users to run Monero nodes.

However, CSIDH offers significiantly better results than lattice based cryptosystems, so it's the clear winner here.

## CSIDH

This section examines CSIDH in more details and focuses on its security and performance.

### Brief description

In CSIDH, Alice's private key is a secret isogeny `a` and Bob's private key is another secret isogeny `b`. The base curve is <code>E<sub>0</sub>: y<sup>2</sup> = x<sup>3</sup> + x</code>. Elliptic curves are defined over the prime field <code>F<sub>p</sub></code>. The size of `p` determines the security level.

Alice's public key is a curve <code>E<sub>A</sub>: y<sup>2</sup> = x<sup>3</sup> + Ax<sup>2</sup> + x</code> such that <code>E<sub>A</sub> = a * E<sub>0</sub></code>, where `*` is the application of the secret isogeny. Similarly for Bob, <code>E<sub>B</sub> = b * E<sub>0</sub></code>. Public keys are uniquely encoded with the coefficient of the x<sup>2</sup> term of the curve equation.

Alice's and Bob's shared secret is simply <code>E<sub>AB</sub> = a * E<sub>B</sub> = b * E<sub>A</sub></code> thanks to the commutativity of the isogeny action. CSIDH is nearly a drop-in replacement for the classical Diffie-Hellman key exchange.


### Classical security and performance

The best classical attack on CSIDH-p has a complexity of <code>O(p<sup>1/4)</sup></code>. The smallest instance that reaches 128 bits of classical security is CSIDH-512.

Table 2 also lists the performance of CSIDH compared to Curve25519 in Intel Skylake cycles. The CSIDH-512 isogeny action takes approximately 1000 times longer than a Curve25519 scalar multiplication. The slowness of CSIDH is not a big problem for Jamtis. The PQ shared secret will be calculated only for enotes with a matching 24-bit view tag. However, it might have an impact on users who receive lots of payments to Jamtis addresses.

CSIDH public keys need to be validated to avoid attacks. Table 1 lists the validation time in Skylake cycles. The key validation could be a consensus rule, in which case it would add roughly 1.3 ms (13 ms) to transaction verification times for CSIDH-512 (CSIDH-1024), assuming a 3 GHz CPU.

| Cryptosystem | Algorithm | Attack complexity | Compute action [cy] |  Validate pub. key [cy] | Impl. ref. |
|--------------|-----------|----------------|-----------|------------|---------------------|
Curve25519 | Pollard's rho |      2<sup>126</sup>     |   100 000    |  0    |   [12]      |
CSIDH-512 | Meet-in-the-middle |  2<sup>128</sup>  |  125 000 000  |  4 000 000  | [13]    |
CSIDH-1024| Meet-in-the-middle|  2<sup>256</sup>  |  470 000 000  |   41 000 000 | [13]    |

*Table 2: Classical security and performance of CSIDH in comparison with Curve25519.*

### Post-quantum security

The post-quantum security of CSIDH is more complicated. The attack with the lowest asymptotic complexity is based on Kuperberg's collimation sieve and has a time complexity of <code>2<sup>O(√log(N))</sup></code>, where `N` is the size of the CSIDH group. In comparison, Shor's algorithm has an asymptotic complexity of <code>log(N)<sup>3</sup></code>.

Table 3 lists the quantum computer resources needed to break a key.

| Cryptosystem | Algorithm | Logical qubits | QROM bits |  T-gates   | Attack time | Ref. |
|--------------|-----------|----------------|-----------|------------|---------------------|------|
Curve25519 | Shor's     |      3000     |   2<sup>26</sup>    |    2<sup>27</sup>   |     8.3 seconds  |  [14]  |
CSIDH-512 | Kuperberg's|  1000000     |   2<sup>40</sup>    |    2<sup>61</sup>    |     4500 years      | [11, 15]
CSIDH-1024| Kuperberg's|  >1000000     |   2<sup>44</sup>    |    2<sup>73</sup>    |     2×10<sup>7</sup> years      | [11, 15]

*Table 3: Post-quantum security of CSIDH in comparison with Curve25519.*

#### Logical qubits

This is the number of logical qubits needed to run the algorithm. Note that the quantum oracle proposed in ref. [15] requires 2<sup>40</sup> qubits, but there is an optimization that can reduce the number of qubits to 2<sup>20</sup> at the cost of of increasing the number of gates by a factor of 4. I'm assuming the optimization is used.

#### QROM

QROM (sometimes called QRAM or QRACM) is a special type of memory that stores read-only classical data ("ones and zeroes") that can be accessed by a quantum computer.

The exact technology how to make QROM is unclear (it can't use transistors like classical RAM), but it is assumed that QROM will be cheaper than quantum memory. Note that this is not a generally accepted assumption. For example, ref. [16] argues that highly scalable QROM is unlikely to ever exist.

Kuperbergs'a algorithm requires a high amount of QROM, so it would become impractical if QROM can't be made to scale. Shor's algorithm can work without QROM (it's only used to store a precomputed table of points to speed up the algorithm).

#### Attack time

The number of T-gates measures the running time of the algorithm. For Shor's algorithm, ref. [14] assumes a highly scalable quantum computer using superconducting qubits with a cycle time of 1 μs. When parallelized, these devices can break one Curve25519 key per 8.3 seconds. A quantum computer based on trapped ions would be about 1000 times slower.

I've extrapolated the attack times from ref. [14] to the number of T-gates for CSIDH. Note that this ignores the much higher memory requirements of the the CSIDH algorithm. Even under these optimistic asumptions, the time to break CSIDH-512 is in thousands of years and the time to break CSIDH-1024 is in millions of years.

### CSURF

There is a variant of CSIDH called CSURF, which was published in 2019 [17]. CSURF requires `p = 7 mod 8` (CSIDH has `p = 3 mod 8`) and uses elliptic curves in the form of <code>y<sup>2</sup> = x<sup>3</sup> + Ax<sup>2</sup> - x</code>. It can use 2-isogenies to slightly speed up the calculation of the group action (the claimed speed-up is around 5%). Otherwise it's very similar to CSIDH. 

A 2023 paper analyzed the recovery of CSIDH/CSURF private keys if some bits are known [18]. Their main result is that a CSIDH private key can be quickly recovered if ~54% of the high bits are known. For CSURF, this raises to ~76% (improved to 74% in a later paper [19]). This means that CSURF has better resistance to side channel attacks (which might leak some private key bits) but also to quantum attacks. For example, the Kuperberg's sieve calculations from ref. [11] assume that all but the lowest 56 bits of the secret key need to be recovered by the quantum computer. Ref. [18] shows that only 139 bits of the 256-bit CSIDH-512 private key need to be recovered quantumly (the rest can be recovered classically in polynomial time).

Further research shows that CSURF is not actually faster than CSIDH, despite the claims from ref. [17]. The problem is that elliptic curves <code>y<sup>2</sup> = x<sup>3</sup> + Ax<sup>2</sup> - x</code> have slower projective formulas than standard Montgomery curves. Specifically, the cost per ladder step is 11M + 5S vs 8M + 4S [20]. This makes CSURF practically slower than CSIDH because high performance implementations use projective formulas.

However, primes `p = 7 mod 8` can still be used with standard Montgomery curves. This is briefly mentioned in ref. [17, Remark 3] and further researched in ref. [21]. This approach requires selecting one of the two orbits and validating that public keys are in the correct orbit. While this adds some small overhead (2 Legendre symbol calculations), it mitigates a general key control vulnerability in CSIDH [22].

### PEGASIS

A new method of calculating the group action called PEGASIS was published in 2025 [23]. PEGASIS calculates the whole group action using one 2<sup>e</sup>-isogeny so it can be considered as an extension of CSURF. A major advantage of PEGASIS is that it can use special-form primes such as <code>p = 15 * 2<sup>1004</sup> - 1</code>, which have a much faster field arithmetic than the general-form primes used by CSIDH and CSURF. A later published variant qt-Pegasis [24] brought some incremental efficiency improvements. No optimized imlpementation currently exists (the papers only give python/sage implementations), so real-world performance is uncertain, but it's probably faster than both CSIDH and CSURF. Note that the last PEGASIS paper is less than 1 month old, so this is cutting-edge research.

## Summary

I'm proposing to use CSIDH/CSURF for PQ encryption with Jamtis addresses. I think the best choice is CSIDH-1024 for a more conservative security margin.

| Algorithm | Address | 2/2 tx | 2/16 tx | Decrypt enote | Validate pubkey | log(T)  | Years to break |
|-----------|---------|--------|---------|---------------|-----------------|---------|----------------|
| CSIDH-512  | 346    | 342    | 2085    | ~83 ms        | ~1.3 ms         |  61     | 4500           |
| CSIDH-768  | 397    | 374    | 2117    | ~180 ms       | ~5 ms           |  67     | 300 000        |
| CSIDH-896  | 422    | 390    | 2133    | ~240 ms       | ~8 ms           |  70     | 2 000 000      |
| CSIDH-1024 | 448    | 406    | 2149    | ~310 ms       | ~13 ms          |  73     | 18 000 000     |

*Table 4: Summary of CSIDH parameters. Performance of CSIDH-512 and CSIDH-1024 is from ref. [13], the numbers for CSIDH-768 and CSIDH-896 are extrapolated.*

## References

[1] "Carrot" https://github.com/jeffro256/carrot/blob/master/carrot.md

[2] "New directions in cryptography", W. Diffie; M. Hellman (1976) https://ieeexplore.ieee.org/document/1055638

[3] "A public-key cryptosystem based on algebraic coding theory.", R.J. McEliece (1978) https://ipnpr.jpl.nasa.gov/progress_report2/42-44/44N.PDF

[4] "Classic McEliece:
conservative code-based cryptography", Albrecht et al. (2022), https://classic.mceliece.org/nist/mceliece-submission-20221023.pdf

[5] "CRYSTALS-Kyber", Avanzi et al. (2021), https://pq-crystals.org/kyber/data/kyber-specification-round3-20210804.pdf

[6] "NTRU", Chen et al. (2020), https://csrc.nist.gov/CSRC/media/Projects/post-quantum-cryptography/documents/round-3/submissions/NTRU-Round3.zip

[7] "NTRU Prime", Bernstein et al. (2020) https://ntruprime.cr.yp.to/nist/ntruprime-20201007.

[8] "Supersingular Isogeny Key Encapsulation", Jao et al. (2022), https://csrc.nist.gov/csrc/media/Projects/post-quantum-cryptography/documents/round-4/submissions/SIKE-spec.pdf

[9] "An efficient key recovery attack on SIDH", W. Castryck, T. Decru (2022) , https://eprint.iacr.org/2022/975

[10] "CSIDH: An Efficient Post-Quantum Commutative Group Action", Castryck et al. (2018), https://eprint.iacr.org/2018/383

[11] "He Gives C-Sieves on the CSIDH", C. Peikert (2019), https://eprint.iacr.org/2019/725

[12] "Security and Efficiency Trade-offs for Elliptic Curve Diffie-Hellman at the 128-bit and 224-bit Security Levels", K. Nath, P. Sarkar (2019), https://eprint.iacr.org/2019/1259 

[13] "CTIDH: faster constant-time CSIDH", Banegas et al. (2021), https://eprint.iacr.org/2021/633

[14] "How to compute a 256-bit elliptic curve private key
with only 50 million Toffoli gates", D. Litinski (2023), https://arxiv.org/abs/2306.08585

[15] "Quantum circuits for the CSIDH: optimizing quantum evaluation of isogenies",  Bernstein et al. (2018), https://eprint.iacr.org/2018/1059

[16] "QRAM: A Survey and Critique", S. Jaques, A. G. Rattew (2023), https://arxiv.org/abs/2305.10310

[17] "CSIDH on the surface", W. Castryck and T. Decru (2019), https://eprint.iacr.org/2019/1404

[18] "Solving the Hidden Number Problem for CSIDH and CSURF via Automated Coppersmith", J. Meers, J. Nowakowski (2023), https://eprint.iacr.org/2023/1409

[19] "Computing Asymptotic Bounds for Small Roots in Coppersmith's Method via Sumset Theory", Feng et al. (2024), https://eprint.iacr.org/2024/1330

[20] "On the Performance Analysis for CSIDH-Based Cryptosystems", Heo et al. (2020), https://www.mdpi.com/2076-3417/10/19/6927

[21] "Optimized CSIDH Implementation Using a 2-torsion Point", Heo et al. (2020), https://eprint.iacr.org/2020/391

[22] "A note on key control in CSIDH", A. Sanso (2022), https://eprint.iacr.org/2022/847

[23] "PEGASIS: Practical Effective Class Group Action using 4-Dimensional Isogenies", Dartois et al. (2025),  https://eprint.iacr.org/2025/401

[24] "qt-Pegasis: Simpler and Faster Effective Class Group Actions", Dartois et al. (2025), https://eprint.iacr.org/2025/1859

# Discussion History
## kayabaNerve | 2025-10-24T10:57:28+00:00
Clarifying, do you plan to propose CSIDH alone or a hybrid?

Personally, I don't believe parameters smaller than 768 are reasonable due to the evolution of attacks seen overtime.

The bandwidth looks great though!

## tevador | 2025-10-24T11:02:07+00:00
Yes, Jamtis uses hybrid encryption. It has 3 shared secrets with Curve25519 and 1 shared secret with CSIDH. Full specs will follow once the PQ algorithm is selected. I'm also tentatively in favor of CSIDH-1024 for conservative security, but we need to make sure that the address size and performance is acceptable.

## tevador | 2025-10-24T11:05:28+00:00
Also note that while CSIDH-768 is possible, no such implementation exists. We have constant-time implementations for CSIDH-512 and CSIDH-1024 only.

## tevador | 2025-10-25T18:27:20+00:00
I added CSIDH-768 and CSIDH-896 as options to Table 4. The performance numbers are extrapolated from the asymptotic complexities of the respective operations.

## tevador | 2025-10-27T15:29:34+00:00
Futher CSIDH-related research:

### CSURF

There is a variant of CSIDH called CSURF, which was published in 2019 [[17](https://eprint.iacr.org/2019/1404)]. CSURF requires `p = 7 mod 8` (CSIDH has `p = 3 mod 8`) and uses elliptic curves in the form of <code>y<sup>2</sup> = x<sup>3</sup> + Ax<sup>2</sup> - x</code>. It can use 2-isogenies to slightly speed up the calculation of the group action (the speed-up is around 5%). Otherwise it's very similar to CSIDH. 

A 2023 paper analyzed the recovery of CSIDH/CSURF private keys if some bits are known [[18](https://eprint.iacr.org/2023/1409)]. Their main result is that a CSIDH private key can be quickly recovered if ~54% of the high bits are known. For CSURF, this raises to ~76% (improved to 74% in a later paper [[19](https://eprint.iacr.org/2024/1330)]). This means that CSURF has better resistance to side channel attacks (which might leak some private key bits) but also to quantum attacks. For example, the Kuperberg's sieve calculations from ref. [11] assume that all but the lowest 56 bits of the secret key need to be recovered by the quantum computer. Ref. 18 shows that only 139 bits of the 256-bit CSIDH-512 private key need to be recovered quantumly (the rest can be recovered classically in polynomial time).

The conclusion is that CSURF might be not only a faster but also a more secure variant of CSIDH.

### PEGASIS

A new method of calculating the group action called PEGASIS was published in 2025 [[20](https://eprint.iacr.org/2025/401)]. PEGASIS calculates the whole group action using one 2<sup>e</sup>-isogeny so it can be considered as an extension of CSURF. A major advantage of PEGASIS is that it can use special-form primes such as <code>p = 15 * 2<sup>1004</sup> - 1</code>, which have a much faster field arithmetic than the general-form primes used by CSIDH and CSURF. A later published variant qt-Pegasis [[21](https://eprint.iacr.org/2025/1859)] brought some incremental efficiency improvements. No optimized imlpementation currently exists (the papers only give python/sage implementations), so real-world performance is uncertain, but it's probably faster than both CSIDH and CSURF. Note that the last PEGASIS paper is less than 1 month old, so this is cutting-edge research.

---

Apart from the size of the prime `p`, we have 3 options for Jamtis:

### CSIDH

Pros:

* a high-performance constant-time implementation exists (for 512 and 1024)
* detailed post-quantum security estimates have been done

Cons:

* slower than CSURF
* probably less secure than CSURF

### CSURF

Pros:

* slightly faster than CSIDH
* probably more secure than CSIDH

Cons:

* there is no high-performance constant-time implementation
* quantum oracle analysis has not been done (but is likely very similar to CSIDH)

### PEGASIS

Pros:

* probably the fastest variant

Cons:

* there is no high-performance constant-time implementation
* quantum oracle analysis has not been done
* uncertain security

## tevador | 2025-12-11T06:47:58+00:00
## Selecting CSIDH parameters

### 1. Prime size

The post-quantum security of CSIDH is determined by the size of the class group $N \approx \sqrt{p}$, where $p$ is the prime field modulus [1]. For simplicity, we only consider $p$ sizes of about 512, 1024 or 2048 bits. Table 1 summarizes the costs and the post-quantum security of the evaluated CSIDH instances compared to Curve25519.

| Cryptosystem | Address | 2/2 tran. | Validate | Decrypt | Qubits | QROM | T-gates | Attack time |
|--------------|-----------|--------|----------|---------|--------|------|---------|-------------|
Curve25519     | 260       | 278    |   0      | <1 ms   |  3000  |2<sup>26</sup>|2<sup>27</sup>|     8.3 seconds  |  [14]  |
CSIDH-512      | 362       | 342    |  1 ms   |  70 ms  |2<sup>20</sup>|2<sup>40</sup>|2<sup>61</sup>    |4500 years|
CSIDH-1024     | 464       | 406    |   10 ms  |  250 ms |2<sup>21</sup>|2<sup>44</sup>|2<sup>73</sup>    |2×10<sup>7</sup> years|
CSIDH-2048     | 668       | 534    |  100 ms |  1000 ms    |2<sup>22</sup>|2<sup>48</sup>|2<sup>87</sup>    |3×10<sup>11</sup> years|

*Table 1: Performance and post-quantum security of CSIDH. "Address" is the Jamtis address length in base32. The pruned 2-input/2-output transaction size assumes 2 key images, 2 standard Carrot enotes and one CSIDH public key without encoding overhead. The public key validation and decryption times were measure on a 3 GHz AMD Ryzen CPU using the constant-time software from ref. [3] with a key space of 2<sup>256</sup>. The quantum hardware requirements for Curve25519 are taken from ref. [4]. The quantum hardware requirements for CSIDH are based on ref. [2] and [5]. The number of qubits for CSIDH-512 is reduced from 2<sup>40</sup> to 2<sup>20</sup> using the optimization from [5], which raises the number of T-gates by a factor of 4. For larger primes we assume the number of qubits scales as O(log(p)). QROM (or QRACM) refers to quantumly accessible classical memory. "Attack time" is scaled from Curve25519 using the number of T-gates, which ignores the much higher memory requirements of CSIDH.*

Increasing the prime size proportionally raises the address length in base32 ("Address" column) and the approximate pruned transaction size ("2/2 tran." column). CSIDH-2048 has the worst UX, with addresses exceeding 600 characters, and also nearly doubles the pruned size of the average transaction.

The CSIDH public key in each transaction needs to be validated by all network nodes. The approximate key validation time on a 3 GHz AMD Ryzen CPU is in the "Validate" column. For comparison, a 2/2 FCMP++ transaction takes about 50 ms to verify, so CSIDH-2048 would triple the verification cost.

The time to decrypt an e-note with a matching view tag is in the "Decrypt" column. The slowness of CSIDH-2048 is less problematic here, but still noticeable, especially for users who receive a lot of e-notes, such as merchants and exchanges.

All three CSIDH instances appear practically unbreakable with a quantum computer, but CSIDH-512 has the smallest security margin and would become breakable in case of a future 1000x speed up.

Based on the above arguments, we select CSIDH-1024 as a good compromise between address length, blockchain size, performance and security.

### 2. Floor vs Surface

While traditional CSIDH operates on the "floor" of the isogeny graph, there is a variant called CSURF that operates "on the surface" [6]. CSURF requires $p \equiv 7\ (mod\ 8)$, while CSIDH has $p \equiv 3\ (mod\ 8)$.

A 2023 paper analyzed the recovery of CSIDH/CSURF private keys if some bits are known [7]. Their main result is that a CSIDH private key can be quickly recovered if ~54% of the high bits are known. For CSURF, this raises to ~76% (improved to 74% in a later paper [8]). This means that CSURF has better resistance to side channel attacks (which might leak some private key bits) but also to quantum attacks.

The original CSURF paper recommeneded to use elliptic curves in the form of $y^2 = x^3 + Ax^2 - x$, but this comes with a significant performance penalty due to slower ladder formulas [9]. However, it is also possible to use standard Montgomery curves $y^2 = x^3 + Ax^2 + x$, but this requires keys to be selected from one of two orbits [7, Remark 3]. An advantage of this approach is that negating `A` produces a curve in the other orbit, which can be detected and prevents some key control attacks on CSIDH [10].

In summary, for security reasons, it is better to use elliptic curves located on the surface of the isogeny graph with $p \equiv 7\ (mod\ 8)$.

### 3. Prime search

CSIDH-1024 uses a 1020-bit prime [1] such that $p \equiv 3\ (mod\ 8)$ and $p+1$ has 130 odd prime factors. Note that 130 is the maximum for 1024 bits because the product of the smallest 131 odd primes is $> 2^{1027}$.

In our case, we want $p \equiv 7\ (mod\ 8)$ and we also want $p+1$ to have 130 odd prime factors. We will search for primes in the form of:

$$
p_S = \left( 8 \cdot \prod_{\ell \in L_{132} \setminus S} \ell \right) - 1
$$

where $L_{132} = \\\{3, 5, 7, 11, \ldots 743, 751\\\}$ is the set of the first 132 odd primes and $S$ is a set of two primes to skip. Note that $L_{132}$ is the smallest possible set for the search. Using $L_{131}$ and skipping one prime yields no results.

The smallest posible size of $p$ in our case is 1021 bits, which is also convenient because the remaining Jamtis address fields have a size congruent to 4 mod 5, so adding one element of $F_{p}$ will produce a payload that can be optimally encoded in base32. We will therefore require $p < 2^{1021}$.

The post-quantum security of CSIDH depends on the class group size $N \approx \sqrt{p}$. Calculating $N$ is computationally expensive, but fast approximations are possible [11, Theorem 8]. We will select the 1021-bit prime with the largest estimated value of $\log(N)$.

The following sage script implements the search:

```python
NUM_PRIMES = 130
BIT_SIZE = 1021

def chi(p, l):
    return kronecker(-p, l)

def approx_class_number(p):
    assert is_prime(p)
    assert p % 4 == 3
    log_cls = log(2 * sqrt(p) / pi, 2).numerical_approx()
    l = 3
    while l < 5000000:
        log_cls += log(l / (l - chi(p, l)), 2).numerical_approx()
        l = next_prime(l)
    return log_cls

primes = [3]

while len(primes) < NUM_PRIMES+2:
    primes.append(next_prime(primes[-1]))

print(f"{NUM_PRIMES} primes up to {primes[-1]}")

for j in range(NUM_PRIMES+1, -1, -1):
    for k in range(NUM_PRIMES+1, j, -1):
        p = 1
        for i in range(NUM_PRIMES+2):
            if i == j or i == k:
                continue
            p *= primes[i]
        p = 8 * p - 1
        nbits = log(p, 2).numerical_approx()
        if nbits > BIT_SIZE:
            break
        if is_prime(p):
            log_cls = approx_class_number(p)
            print(f"Prime p = {hex(p)}, skip = [{primes[j]},{primes[k]}]," +\
                f" log(p) = {round(nbits, 3)}, log(N) ~ {round(log_cls, 3)}")
```

The script finds the following 8 primes:

|prime|  $S$  |$\log(p)$|$\log(N)$|
|-----|-------|---------|---------|
|$p_1$|$\\\{677,719\\\}$|1020.674|512.262|
|$p_2$|$\\\{653,727\\\}$|1020.710|512.287|
|$p_3$|$\\\{641,677\\\}$|1020.839|512.335|
|$p_4$|$\\\{631,733\\\}$|1020.747|512.304|
|$p_5$|$\\\{617,641\\\}$|1020.973|512.395|
|$p_6$|$\\\{577,709\\\}$|1020.924|512.399|
|$p_7$|$\\\{577,677\\\}$|1020.991|512.392|
|$p_8$|$\\\{557,701\\\}$|1020.992|512.408|

The final output of the search is the prime $p_8$ with hexadecimal representation:

```
0x1fd04e89171530f63bd415afc218e1e270e771eb8c5c1bac030657cffee69570f10f756730bb071aa2154816408329ea26c7e2a90f45091485761db82af03257c5e36d7cef41e26da2ddaaebc30ead34f502250b54f9f062a9cfe9bc6eb1d3f43d8f91faa5d1b523497188f200c11574142ed7966746e91b933240af49ca5f47
```

Note: The selected prime $p_8$ is the largest prime from the list, but for example the second largest prime $p_7$ has smaller $N$ than $p_5$ and $p_6$, so larger primes don't always yield larger class groups.

### 4. Key space

While the post-quantum security of CSIDH only depends on the class group size $N$, the classical security depends on the selected key space. With a key space of size $K \ll N$, a meet-in-the-middle attack can break a key in expected time $O(\sqrt{K})$ and memory $O(\sqrt{K})$, so $K = 2^{256}$ is commonly selected for 128-bit classical security [1].

We will use the key structure from CTIDH [3] because it offers the fastest group action calculation.

To find optimal prime batching and batch bounds, we will use the `greedy` script from CTIDH, adding our prime definition there:

```python
  p['1021'] = (3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,709,719,727,733,739,743,751)
```

We can then run the search as `./greedy.py 1021 256 20 0 16`. We found that 20 batches are optimal and the best configuration is:

```
output 373377.77 (3,4,3,4,6,5,6,6,6,8,7,7,6,8,8,8,5,6,13,11) (3,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,4,6,6,4)
```

so one group action calculation takes on average about 373 000 field multiplications. A constant-time implementation always performs exactly 111 isogenies (the maximum for every prime batch).

### 5. Summary

This proposal is for Monero to use CSIDH with the following parameters:

* `p = 0x1fd04e89171530f63bd415afc218e1e270e771eb8c5c1bac030657cffee69570f10f756730bb071aa2154816408329ea26c7e2a90f45091485761db82af03257c5e36d7cef41e26da2ddaaebc30ead34f502250b54f9f062a9cfe9bc6eb1d3f43d8f91faa5d1b523497188f200c11574142ed7966746e91b933240af49ca5f47` is a 1021-bit prime.
* Valid public keys are supersingular elliptic curves $E_A: y^2 = x^3 + Ax^2 + x$ with $A, x, y \in F_p$ such that both $A-2$ and $A+2$ are squares in $F_p$.
* The starting curve is $E_6: y^2 = x^3 + 6x^2 + x$.
* Private keys are generated by splitting the 130 odd primes dividing $p+1$ into 20 batches of sizes 3,4,3,4,6,5,6,6,6,8,7,7,6,8,8,8,5,6,13,11. Isogeny exponents are assigned to each prime so that the sum of the absolute values of the exponents within each batch does not exceed the bounds: 3,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,4,6,6,4. This allows for approximately $2^{256}$ distinct keys.

## References

[1] "CSIDH: An Efficient Post-Quantum Commutative Group Action", Castryck et al. (2018), https://eprint.iacr.org/2018/383

[2] "He Gives C-Sieves on the CSIDH", C. Peikert (2019), https://eprint.iacr.org/2019/725

[3] "CTIDH: faster constant-time CSIDH", Banegas et al. (2021), https://eprint.iacr.org/2021/633

[4] "How to compute a 256-bit elliptic curve private key
with only 50 million Toffoli gates", D. Litinski (2023), https://arxiv.org/abs/2306.08585

[5] "Quantum circuits for the CSIDH: optimizing quantum evaluation of isogenies",  Bernstein et al. (2018), https://eprint.iacr.org/2018/1059

[6] "CSIDH on the surface", W. Castryck and T. Decru (2019), https://eprint.iacr.org/2019/1404

[7] "Solving the Hidden Number Problem for CSIDH and CSURF via Automated Coppersmith", J. Meers, J. Nowakowski (2023), https://eprint.iacr.org/2023/1409

[8] "Computing Asymptotic Bounds for Small Roots in Coppersmith's Method via Sumset Theory", Feng et al. (2024), https://eprint.iacr.org/2024/1330

[9] "On the Performance Analysis for CSIDH-Based Cryptosystems", Heo et al. (2020), https://www.mdpi.com/2076-3417/10/19/6927

[10] "A note on key control in CSIDH", A. Sanso (2022), https://eprint.iacr.org/2022/847

[11] "CSIDH ON THE SURFACE (CSURF)", W. Castryk (2021), https://homes.esat.kuleuven.be/~wcastryc/summer_school_csurf.pdf


## kayabaNerve | 2025-12-12T16:33:48+00:00
Is the memory cost truly that high? For the case of hash collisions specifically, I know that on paper there is an infeasible memory cost (2**128), but the usage of distinguished points and similar descending works allow building theoretical machines with low memory costs. Accordingly, I'm not immediately sure we should bound on the memory cost as seen above. I do understand the computational complexity is a trade-off with the memory usage and that is modeled above though.

I'll try to add the relevant links I'm thinking of later today. It's been a while since I've reviewed collision algorithms. I'm still a bit uncomfortable with the presentation of memory however.

## tevador | 2025-12-13T00:09:42+00:00
Note that the attack doesn't *need* that much memory, but the runtime increases with less memory. The formula with $K = 2^{220}$ and $M = 1$ gives a time complexity of $2^{165}$. The idea is to put an upper bound on $M$ to calculate the required key space for ~128 bits of security. If the attacker's memory is unbounded, then $K = 2^{220}$ only gives 110 bits of security.

## tevador | 2025-12-13T11:06:36+00:00
After reading [Low Memory Attacks on Small Key CSIDH](https://eprint.iacr.org/2023/507), I'm not anymore convinced that $K = 2^{220}$ is viable. Their technique reduces the time complexity to about $K^{0.52}$ with $M = K^{0.36}$ (Fig. 5b with m = 3), which would imply only 114 bits of security for $K = 2^{220}$.

I updated my proposal to use the conservative key space of $K = 2^{256}$. This comes with a ~30% performance penalty, but provides 128 bits of security regardless of memory, which makes things easier for a future audit.

## tevador | 2026-04-09T05:09:44+00:00
### Optimized key spaces

The previous comment recommends to use a 256-bit key space for all CSIDH private keys.

The CSIDH shared secret of an e-note is constructed as:

<code>X4 = z<sub>a</sub><sup>j</sup> * z<sub>ur</sub> * Z<sub>e</sub></code>

so it requires 2 isogeny actions with 2 different private keys:

1. <code>z<sub>a</sub><sup>j</sup></code> is the address-specific private key known to the address generator wallet tier. The purpose of this key is to make addresses unlinkable.
2. <code>z<sub>ur</sub></code> is the wallet-specific private key known to the payment validator wallet tier. The purpose of this key is to provide forward secrecy in case the address generator wallet tier is compromised.

However, I think we can get away with using a reduced key space for <code>z<sub>a</sub><sup>j</sup></code>, which would speed up e-note decryption by around 25%. This works under the assumption that the public key <code>Z<sub>ur</sub> = z<sub>ur</sub> * E</code> is only revealed to the address generator wallet tier and it's never published separately.

The meet-in-the-middle attack on CSIDH finds the private key `x` such that `A = x * B`, given both `A` and `B`. Protection from this attack requires `x` to be selected from a 256-bit space. However, if `B` is unknown, the attack cannot be used.

The CSIDH public key in each address is constructed as:

<code>Z<sub>5</sub><sup>j</sup> = z<sub>a</sub><sup>j</sup> * Z<sub>ur</sub></code>

If an attacker has 2 different keys <code>Z<sub>5</sub><sup>j1</sup></code> and <code>Z<sub>5</sub><sup>j2</sup></code>, then linking those two addresses to the same wallet boils down to finding <code>Z<sub>ur</sub></code>.

Assuming the keys belong to the same wallet, we have the following relation:

<code>Z<sub>5</sub><sup>j2</sup> = (z<sub>a</sub><sup>j2</sup> - z<sub>a</sub><sup>j1</sup>) * Z<sub>5</sub><sup>j1</sup></code>

(Note: the CSIDH private keys form an additive group, so negating a private key inverts it.)

The attacker can mount a meet in the middle attack on the previous equation. To get 128 bits of security, we only need the combined key space of <code>(z<sub>a</sub><sup>j2</sup> - z<sub>a</sub><sup>j1</sup>)</code> to be 2<sup>256</sup>, so we only need about half the number of isogenies for each <code>z<sub>a</sub><sup>j</sup></code>, which can be achieved by using the same batch sizes, but reduced batch bounds of 1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,2, which is a total of 56 isogenies rather than 111.

## tevador | 2026-04-13T17:20:44+00:00
The selected algoritm (CSIDH) with the proposed parameters has been included in the [Jamtis specification](https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832).

## tevador | 2026-04-20T15:01:04+00:00
It turned out that this issue is not quite settled yet.

There are 3 possible PQ encryption options and the only viable PQ encryption algorithm is CSIDH (details below).

## Summary

This table rates the 4 possible choices based on practicality (includes address length, pruned blockchain size and scanning/decryption speed), PQ privacy (privacy against a quantum attacker capable of breaking Curve25519) and PQ security (difficulty of eventually being broken by a hypothetical quantum attack beyond the break of Curve25519).

| Choice    | Practicality | PQ privacy | PQ security |
|-----------|--------------|------------|-------------|
| **X25519** |   :star::star::star::star: |   :star: |      |
| **AC1152**|    :star::star::star: |    :star::star: |    :star::star::star: |
| **BC704**|    :star::star::star: |    :star::star::star: |    :star::star: |
| **CC832**|    :star::star: |    :star::star::star::star: |    :star::star: |

For each of the PQ options A/B/C, the table lists the most secure CSIDH size that results in an address length not exceeding 420 characters.

## Details

### Option A: PQ encryption for the amount

The transaction amount and the spend key extensions use PQ encryption. This approach uses 4 classical public keys and 1 PQ public key per address.

If Curve25519 is broken, a quantum attacker can locate enotes received to a known address, but can't decrypt the amount and can't track the spending transaction. If Curve25519 is not broken, this option offers the same privacy properties as legacy addresses (i.e. enotes cannot be located). The privacy regression only applies to the post-quantum scenario.

Possible encryption algorithms: CSIDH, NTRU.

### Option B: PQ encryption for everything except the primary view tag

The secondary view tag, address tag, transaction amount and the spend key extensions use PQ encryption. This uses 3 classical public keys 2 PQ public keys per address and 1 PQ public key per transaction output (except for 2-out transactions).

If Curve25519 is broken, a quantum attacker can find a 1/256 subset of the blockchain that contains enotes received to a known address.

Possible encryption algorithms: CSIDH.

NTRU is not compatible with this option because it doesn't support O(1) balance recovery with respect to the number of wallet addresses.

### Option C: PQ encryption for everything + PQ-unlinkable addresses

Everything, including the primary view tag, uses PQ encryption and addresses stay unlinkable even if Curve25519 is broken. This is the most private option, but comes with severe performance drawbacks. Option C addresses include 2 classical public keys and 2 PQ public keys.

Possible encryption algorithms: CSIDH.

### Details table

Crossed out choices exceed the address length limit of 420 characters.

| Choice    | PQ am | PQ vt | PQ unlink | LWS priv | Algorithm  | Address | 2/2 tran. | 2/16 tran. | Scan time/day | PQ security  |
|-----------|-----------|------|-------|----------|------------|---------|-----------|------------|---------------|--------------|
|  **X25519**        | :x:       | :x:         | :x: |:white_check_mark: | Curve25519 |  223    |   278     |    2021    |      4 s      |2<sup>26</sup>|
| AC512| :white_check_mark: | :x: | :x: |:white_check_mark: | CSIDH-512 |  309    |   342     |    2085    |      4 s      |2<sup>60</sup>|
| AC1024 | :white_check_mark: | :x: | :x: |:white_check_mark: |CSIDH-1024 |  395    |   406     |    2149    |      4 s      |2<sup>72</sup>|
| **AC1152**| :white_check_mark: | :x: | :x: |:white_check_mark: |CSIDH-1152 |  416    |   422     |    2165    |      4 s      |2<sup>74</sup>|
| ~~AC2048~~| :white_check_mark: | :x: | :x: |:white_check_mark: |CSIDH-2048 |  567    |   534     |    2277    |      4 s      |2<sup>86</sup>|
| ~~AN509~~ | :white_check_mark: | :x: | :x: |:white_check_mark: | NTRU-509  |  1162   |   977     |   13205    |      4 s      |2<sup>106</sup>|
| BC512 | :white_check_mark: | :warning: | :x: | :warning: |CSIDH-512|352|342  |    3056    |     21 s      |2<sup>60</sup>|
| **BC704** | :white_check_mark: | :warning: | :x: | :warning: |CSIDH-704|416|366  |    3429    |     40 s      |2<sup>63</sup>|
| ~~BC1024~~| :white_check_mark: | :warning: | :x: | :warning: |CSIDH-1024|524|406 |    4069    |     71 s      |2<sup>72</sup>|
| ~~BC2048~~| :white_check_mark: | :warning: | :x: | :warning: |CSIDH-2048|868|534|    6117    |    5 min      |2<sup>86</sup>|
| CC512 | :white_check_mark: | :white_check_mark:| :white_check_mark:| :warning: |CSIDH-512|309|342|    3056    |    1 hour      |2<sup>60</sup>|
| **CC832**| :white_check_mark: | :white_check_mark:| :white_check_mark:| :warning: |CSIDH-832|416|382|    3685    |    3 hours      |2<sup>67</sup>|
| ~~CC1024~~| :white_check_mark: | :white_check_mark:| :white_check_mark:| :warning: |CSIDH-1024|481|406|    4080    |    5 hours      |2<sup>72</sup>|

* PQ am - if the amount is PQ-encrypted
* PQ vt - if the view tag is PQ-encrypted; :warning: means only the secondary view tag is PQ-encrypted
* PQ unlink - if addresses stay unlinkable even if Curve25519 is broken
* LWS priv - if using LWS hides users' enotes among false positives
* Algorithm - the encryption algorithm
* Address - address length in a base32+base62 hybrid encoding
* 2/2 tran. - approximate pruned size of a 2/2 transaction
* 2/16 tran. - approximate pruned size of a 2/16 transaction
* Scan time/day - approximate time to scan 100 000 enotes using 1 core of a desktop CPU @ 3 GHz, assuming an optimized x86 assembly implementation (further major optimizations are unlikely)
* PQ security - the approximate number of quantum T-gates to break a key

### Post-quantum security

The table below lists the number of T-gates (a measure of algorithmic complexity) and an example of resources and the attack time needed to break a single key.

| Algorithm    | T-gates  | Resources and attack time |
|--------------|----------|---------------------------|
| Curve25519   |2<sup>26</sup> | a quantum computer running for 11 minutes
| CSIDH-512    |2<sup>60</sup> | 65 thousand quantum computers running for 5 years
| CSIDH-1024   |2<sup>72</sup> | 67 million quantum computers running for 22 years
| CSIDH-2048   |2<sup>86</sup>  | 260 billion quantum computers running for 90 years
| NTRU-509     |2<sup>106</sup>| a trillion quantum computers running for 2 million years

"Quantum computer" here means a fast-cycle quantum cluster (e.g. based on superconductivity or photonics) with a sufficient number of logical qubits to execute the algorithm and sufficiently low qubit error rate for the run time of the attack. For CSIDH, it would likely be a building-sized object with a lot of cryogenic equipment. Note that the attack times for CSIDH cannot be reduced by more parallelism, they are based on the estimated quantum circuit depth. For Curve25519 and NTRU-509, the attack time can be shortened with more parallelism, but it's irrelevant.

## kayabaNerve | 2026-04-20T20:06:55+00:00
https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832?permalink_comment_id=6110120#gistcomment-6110120 was my comment on a gist discussing this, for which I effectively advocated for BC2048, with additional commentary including the agreement that optimal should not be the enemy of better.

## tevador | 2026-04-21T05:25:31+00:00
My personal preference is ~~BC512 (for best performance) or~~ BC1024 (for extra security margin). I think BC2048 is beyond the acceptable UX threshold in terms of scanning performance, pruned blockchain size and address length. If we decide that CSIDH-2048 is a must, then AC2048 is a more acceptable choice.

## tevador | 2026-04-21T05:34:24+00:00
### The PQ security of CSIDH

It should be noted that the technological jump from running Shor's on Curve25519 to running Kuperberg's on CSIDH-512 is quite significant even if we assume the former is quite likely to become feasible before 2035.

Ideally, we would not have to guess what is and what isn't possible, but unfortunately, there is no perfect solution and any choice we make will be a trade-off.

Here is a short summary of the technological differences between a quantum computer usable to break Curve25519 and one usable to break CSIDH-512:

| Resource       | Curve25519 |  CSIDH-512  |
|----------------|------------|-------------|
| Logical qubits |  1200      |  40 000  |
| Error rate     | < 10<sup>-10</sup>| < 10<sup>-15</sup>|
| Code cycle     |  < 10 ms   |   < 10 μs   |
| QRACM size     |    0       | 2<sup>30</sup> - 2<sup>40</sup>   |

#### Logical qubits

The minimum number of fault-tolerant qubits to run the algorithm [1, 7]. Note that the CSIDH-512 oracle from ref. [7] has a much higher complexity than the optimized oracle from ref [2], which needs 1 000 000 logical qubits.

#### Error rate

This is the required logical error rate. Lower error rates imply more quantum error correction. This determines the number of physical qubits needed to represent a logical qubit [3]. CSIDH-512 might need up to 1 billion physical qubits.

#### Code cycle

The cycle time depends on the physical realization of the quantum computer. Slow-cycle technologies like trapped ions and neutral atoms have code cycles measured in milliseconds. These are still fast enough to break Curve25519 in a couple hours, but too slow to break CSIDH-512 in less than a few hundred years. CSIDH needs a fast-cycle quantum computer based on superconducting qubits or photonics. [4]

#### QRACM

The fastest quantum algorithm to break CSIDH-512 from ref. [5] additionally needs a certain amount of quantum random-access memory (QRACM). This is classical memory that can be read in a quantum superposition using a quantum address register. Unlike typical RAM, it needs to access all data stored in the memory simultaneously and return a quantum superposition. While theoretical algorithms use it as a "cheap alternative" to quantum memory, QRACM is very hard to build in practice and the required capacity for CSIDH-512 might not be feasible to achieve. [6]

The T-gate estimates for CSIDH are based on 2<sup>40</sup> bits of QRACM. The amount can be somewhat reduced at the cost of increasing the complexity of the attack.

Ref. [7] presents 3 quantum attacks that don't need QRACM but have much higher gate counts than the optimized attack from ref [5].

### Summary

Based on my understanding of physics and the current technological progress in quantum computing, I think CSIDH-512 is very unlikely to be broken before 2100, if at all. CSIDH-1024 should offer a comfortable security margin for an intermediate hybrid protocol.

### References

[1] "Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities: Resource Estimates and Mitigations", Babbush et al. (2026), https://arxiv.org/abs/2603.28846

[2] "Quantum circuits for the CSIDH: optimizing quantum evaluation of isogenies", Bernstein et al. (2018), https://eprint.iacr.org/2018/1059

[3] "How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits", Gidney, Ekerå (2021), https://arxiv.org/abs/1905.09749

[4] "How to compute a 256-bit elliptic curve private key with only 50 million Toffoli gates", D. Litinski (2023), https://arxiv.org/abs/2306.08585

[5] "He Gives C-Sieves on the CSIDH", C. Peikert (2019), https://eprint.iacr.org/2019/725

[6] "QRAM: A Survey and Critique", S. Jaques, A. G. Rattew (2023), https://arxiv.org/abs/2305.10310

[7] "Quantum Security Analysis of CSIDH", X. Bonnetain and A. Schrottenloher (2020), https://eprint.iacr.org/2018/537


## tevador | 2026-04-22T07:28:59+00:00
Edit: The comment I was replying to has been deleted.

> I would also like to add that the legacy version of Monero currently hides outputs. Upgrading to post-quantum security (Option A) would reduce the level of anonymity compared to the current cryptographic setup. I don't want to sacrifice anonymity for security. It is better to pay for it with overhead.

I have to correct you here. Option A has the same classical privacy as legacy addresses. Against a quantum attacker, legacy addresses offer zero privacy, while Option A offers a reduced level of privacy compared to the classical case.

> with performance enhancements addressed afterward

> Optimizations must follow the nature of the project.

One thing I didn't mention is that all performance numbers in this issue are based on an already optimized x86 assembly implementation using mulx/adox instructions. **Portable code will be significantly slower.**

Further software optimizations are unlikely without hardware upgrades, e.g. AVX512 or GPU acceleration.

## j-berman | 2026-04-24T17:56:37+00:00
A follow-up on @kayabaNerve 's question regarding if the scheme is a hybrid one. Just to confirm, does hybrid here mean that if there is some vulnerability in CSIDH, that the scheme falls back to Curve25519, and vice versa? E.g. [X-Wing](https://eprint.iacr.org/2024/039) claims "X-Wing is secure if either X25519 or ML-KEM-768 is secure"

## tevador | 2026-04-24T18:49:04+00:00
Yes, it's a type of hybrid encryption. The final sender-receiver shared secret <code>s<sub>sr</sub><sup>ctx</sup></code> is calculated from all the individual shared secrets, which includes both X25519 and CSIDH. See [here](https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#65-sender-receiver-shared-secrets) (note: the current version of specs uses AC1024, so it's subject to changes).

## te-mpe-st | 2026-04-25T11:37:29+00:00
> NTRU (and other lattice-based cryptosystems) would require addresses longer than 1300 characters and would significantly increase the pruned sizes of all transactions (up to 6x for 16 outputs). If there were no alternatives, I think these costs might be acceptable, but it would have a negative impact on the uptake of Jamtis and willingness of users to run Monero nodes.

Recently, SWOOSH(EPRINT 2023/271) [1] proved lattice NIKEs are possible. Would there be consideration for using them if the overhead dropped below a certain threshold via optimisation or otherwise?

Also, I wanted to ask about the Jamtis spec in regards to a paper by Dunman et. al, (EPRINT 2022/1230) [2]. It showed the natural GA-HDH NIKE requires strong assumptions for active security in the QROM. ssrctx seems to mitigate this by not exposing the raw CSIDH secret and binding to the classical components, has this composition been analysed in this context or one similar? (Or was the twinning from the paper considered an alternative?) Sorry for the proof-theoretic stuff.

[1] https://eprint.iacr.org/2023/271.pdf
[2] https://eprint.iacr.org/2022/1230.pdf

## tevador | 2026-04-25T15:44:55+00:00
@te-mpe-st 

> Recently, SWOOSH(EPRINT 2023/271) [1] proved lattice NIKEs are possible. Would there be consideration for using them if the overhead dropped below a certain threshold via optimisation or otherwise?

Yes, I'm aware of Swoosh. However, the public key size (>200 KB) makes it completely impractical for an addressing protocol and there is little hope of major improvements in that area (see eprint 2020/1555 for the relevant arguments).

> Also, I wanted to ask about the Jamtis spec in regards to a paper by Dunman et. al, (EPRINT 2022/1230) [2]. It showed the natural GA-HDH NIKE requires strong assumptions for active security in the QROM. ssrctx seems to mitigate this by not exposing the raw CSIDH secret and binding to the classical components, has this composition been analysed in this context or one similar? (Or was the twinning from the paper considered an alternative?) Sorry for the proof-theoretic stuff.

I haven't analyzed this specifically, but IIUIC it concerns a chosen ciphertext attack, which Jamtis thwarts with `input_context` included in the shared secret calculation. The classical components are irrelevant for post-quantum security.

## te-mpe-st | 2026-04-26T04:01:46+00:00
Alright cool. Thanks.

# Action History
- Created by: tevador | 2025-10-24T10:50:46+00:00
