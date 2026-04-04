---
title: '[DRAFT] Monero Sub-addresses'
source_url: https://github.com/monero-project/research-lab/issues/7
author: JollyMort
assignees: []
labels: []
created_at: '2017-02-08T18:16:14+00:00'
updated_at: '2022-02-20T06:43:55+00:00'
type: issue
status: closed
closed_at: '2017-06-21T20:25:59+00:00'
---

# Original Description
Ok, so I'm moving this here to keep the https://github.com/monero-project/monero/pull/1345 clutter-free.

@fluffypony @kenshi84 @knaccc @luigi1111

Todo:
- choice of method for `n` derivation
- some tweaks: https://paste.fedoraproject.org/551200/77652148/

Changelog:

2017-02-07: Initial: http://termbin.com/vdam, http://termbin.com/0a3o, http://termbin.com/n58g - knaccc
2017-02-07: Changed notation and supporting normal addresses as well: https://paste.fedoraproject.org/550729/50082614/ - all :)
2017-02-07: Multi-address support: https://paste.fedoraproject.org/550761/06389148/ - Luigi/JM
2017-02-08: More tweaks and improvement of readability: https://paste.fedoraproject.org/550825/65211341/ - Kenshi
2017-02-08: More tweaks, formatted and copied from https://github.com/monero-project/monero/pull/1345#issuecomment-278228450 - Luigi/JM
**2017-02-09: Apparently this is broken, because knowing C and n, it's trivial to find A**
2017-02-17: See discussion below...

Initial discussion: https://paste.fedoraproject.org/551203/78349148/

## Monero Sub-addresses

### Brief

Currently, each Monero wallet generates one set of keys and one public address which is given out to receive payments. However, a user may want to give out a dedicated address to each sender for dual purpose: to know which payment came from which sender and to avoid privacy loss via off-chain linking of the one address. To accomplish both goals, we propose a way to create multiple addresses which maintains reasonable performance of scanning the blockchain for outputs sent to any of the addresses created, all accessible from within the same wallet.

### Sub-addresses creation

A recipient's root wallet address is defined as a pair of public view and spend keys (A,B) = (a\*G,b\*G), where a and b are the secret view and spend keys. The recipient creates a sub-address by choosing an arbitrary scalar n and defining a triplet (C,D,n). The choice of scalar n could be deterministic, as proposed below:
 
    n = Hc(a || j)
    C = n*A
    m = Hs(a || n)
    M = m*G
    D = B+M,

where

    j = 1,...,p.
 
Such a sub-address (C,D,n) gets passed to the sender. Note that the sender can't determine its root address (A,B). The sender can, if necessary, transfer to more than one such sub-addresses (C\_i,D\_i,n\_i), i=1,...,w (either to the same recipient or to different recipients) in a single
transaction.

### Transaction Construction

When constructing a transaction, the sender generates the transaction key R=r\*G in a particular
manner: he rolls a random scalar s, and computes r as
 
    r = s * n_1 * n_2 * ... * n_w.
 
Then, an output public key P for any standard destination address (A,B) is created as usual:
 
    P = Hs(r * A) * G + B
 
In contrast, an output public key P\_i for the i-th sub-address (C\_i, D\_i, n\_i) is created as:
 
    P_i = Hs(s * n_1 * n_2 * ... * n_{i-1} * n_{i+1} * ... * n_w * C_i) * G + D_i
 
Since C\_i = n\_i * A\_i (while A\_i is not known to the sender), the trick is in the following property:
 
      s * n_1 * n_2 * ... * n_{i-1} * n_{i+1} * ... * n_w * C_i
    = s * n_1 * n_2 * ... * n_{i-1} * n_{i+1} * ... * n_w * n_i * A_i
    = r * A_i
 
Therefore, the output public key P_i is effectively equivalent to:
 
    P_i = Hs(r * A_i) * G + B_i + M_i
 
even though the sender doesn't know (A\_i,B\_i).

### Scanning for Incoming Transfers

When a recipient checks for incoming transfers, he first performs the standard key derivation
procedure to check if a given output key P matches to:
 
    P' = Hs(a * R) * G + B.
 
If this test fails, he then goes through all previously created sub-addresses (C,D,n) and
checks if P matches to:
 
    Q' = Hs(a * R) * G + B + M.
 
Similar to the aggregated addresses approach [1], this search can be done in a constant time
using a hash table: instead of computing Q' directly, the recipient computes
 
    (B + M)' = P - Hs(a * R) * G, // I think that this is faster, as you pre-compute the EC addition only once, store it in the hash table and now don't have to subtract the B for each output. So, only one EC subtraction per output.
 
and looks for (B + M)' in the hash table. If such an (B + M)' is found, the output key P belongs to the recipient and its private key x can be recovered as:
 
    x = Hs(a * R) + b + m.

### Wallet Recovery

From a known set of private keys (a,b), and with assumed number of previously used sub-addresses q>=p, the wallet must first reconstruct all the sub-address information:

    n = Hc(a || j)
    C = n*A
    m = Hs(a || n)
    M = m*G
    D = B+M,

where

    j = 1,...,q.

Then, it performs the full scan, as described in the previous section.

To make it stateless, wallet software could limit the range of p, and have q=p=10000, or any other arbitrary number.

### Notes

The root address should never be made public because in that case, anyone could check whether any 2 sub-addresses belong to the same root address.

### Credits

knaccc for the initial idea, Luigi for guidance and solution for multiple addresses, and kenshi84 for opening the topic in the first place and final touches. 

### References
 
[1] https://bytecoin.org/static/files/docs/aggregate-addresses.pdf

# Discussion History
## JollyMort | 2017-02-09T01:28:09+00:00
also fyi @RandomRun maybe you'd be interested to have a look

## RandomRun | 2017-02-17T03:29:18+00:00
@JollyMort: Thanks for sharing, this is indeed a nice problem!

I was just discussing this problem with a friend, and below is more or less what we have come up with. This happened just a few hours ago, and I am tired, so I expect it to contain some imprecisions, or perhaps even a blunder, but I hope that the idea is helps :)

1) The receiver, Alice, picks in her wallet two random numbers `(a, b)`, and shares the subaddress `(abG, bG)` with the sender, Bob.

2) Bob picks his own random number `r` and computes `R = r(bG)`, and the one-time address `P = H(r(abG))G + bG`. He includes `R` in the transactions sending money to `P`.

3) Alice computes `P' = H(aR)G + bG` and checks whether `P == P'`. If so, she can move the funds with the signing key `x = H(aR) + b`.

This is almost identical to what happens with regular stealth addresses currently used, but now Alice can keep `a` fixed, and use a new random (or pseudo-random, deterministic) value of `b` to ask funds from Carol. 

Over time, she will end up with a collection `{(a, b_i): i = 1, 2, ....., n}`, but the important thing to notice is that she only needs `a` (and therefore just one operation) to compute `H(aR)G`, since the value `b` was already conveniently baked into `R`, so she doesn't have to try all her `b` values at this point. After that, she computes `P - H(aR)G` and checks whether it is in her precomputed set of points  `{b_i*G: i = 1, 2, ....., n}`.

I am hoping that the bulk of the scanning cost was the group multiplication, and the hash function. If so, maybe this can be considered reasonable performance.

[**Edit**: ~~In this case, for each `b` there would be a corresponding view key `(ab, bG)`. (I am not now sure if using publishing `ab` for many values of `b` should be a security concern...)~~ Actually, the viewkey remains just `(a, bG)`! So I guess no more problems leaking private keys through the view keys :)]

PS.: Our original setup was to make the address longer, like `(sA, sB, sG)`, and have Bob publish `R = r(sG)`, and `P = H(r(sA))G + sB`, but I felt like it could be simplified to what I described above, with the random parameter `s` being "absorbed into" `b`.



## knaccc | 2017-02-17T04:30:59+00:00
I've been staring at this for 40 minutes, and can't see a flaw, up until the private view key part. I've posted this stackexchange question about the EC point factorization issue: http://crypto.stackexchange.com/questions/43951/can-elliptic-curve-point-common-factors-be-detected

I think it is probably the case that the private view key can be factored, because RSA needs far longer key lengths than 256 bits to be secure. So I think that giving away multiple view keys will allow the signing keys to be determined. I hope I'm wrong about this.

## knaccc | 2017-02-17T05:28:19+00:00
Perhaps the view key issue could be fixed by passing to Bob a third item cG, where c is another random number.

Bob would compute `P = H(rA)G + C == H(r(abG))G + cG`, Alice would compute `P' = H(aR)G + cG`, and the signing key would be `x = H(aR) + c`

For each subaddress:
the wallet address would be: `(A, B, C) == (abG, bG, cG)`
the private spend key would be `(ab, c)`
the private view key would be `(ab, C)`

Note that I've defined `A==abG` rather than `A==aG`

## RandomRun | 2017-02-17T06:19:46+00:00
@knaccc: Thanks for finding out the that the view keys do leak the spend key. 
[**Edit**: I had the wrong view key in my first comment, but it is fixed now.]

One way of perhaps fixing that is to go back to the original approach we had, which is: fix `(a, b)`, and for each different sender, generate a random `s` value. Pass `(sA, sB, sG)` to them so that they can pick their own  random `r`, and compute `R = r(sG)`, and `P = H(r(sA))G + sB`. Sender sends out `R` and `P`.

Alice checks: `P' = H(aR)G + sB = H(a(rsG))G + sB = H(r(saG))G + sB = H(r(sA))G + sB = P`. The corresponding view key is `(a, sB)`, and here I see no leak of the private spend key `sb`.
_______________________________

> The view key for each subaddress would be `(ab, cG)`

If your `b` varies, then `a` could be exposed, but I guess your approach is good because even if that happens, there is no way to deduce `c`, right? I am just not clear how Bob computes his `R` here. It seems that it would have to be `R = r(bG)`, but he is not being given `bG`.

## knaccc | 2017-02-17T06:22:01+00:00
@RandomRun Bob is given the address `(A, B, C)` so he will know `bG==B` in order to create `R==rB`

You're right, my comments fixed the problem of allowing the private spend key to be determined, but did not prevent multiple private view keys from being compared to notice common factors to link them together. This leak is probably not a big deal, because it is only a leak to an auditor that you'd probably want to share all subaddresses within a wallet to anyway. The main thing is that holders of different subaddresses cannot see that they're linked, and that the spend keys are safe from the auditor.

I think your original approach also suffers from the same private spend key exposure issue when multiple subaddress view keys are shared with an auditor.

Edit: The view key for multiple individual subaddresses cannot be given out without exposing the signing keys, but I don't think that's a problem worth moving to my three EC-point (A, B, C) address format to fix since the user can just be told to share either the view key for all subaddresses or for none at all.

## RandomRun | 2017-02-17T06:29:09+00:00
@knaccc: But when Alice wants to receive money from Carol, will `A` and `B` be provided to her as well? If so, that creates an off chain link we should avoid; if not, then will that change the value of `b`? Because if so, it seems that that would make Alice have to compute `H(r(abG))G` one time for each different `b`.

## knaccc | 2017-02-17T06:32:29+00:00
@RandomRun Bob would be sent an address composed of 3 different EC points, as defined in my comment https://github.com/monero-project/research-lab/issues/7#issuecomment-280556481

Including an extra EC point is not conceptually different from including a payment id with a wallet address (although of course those things would be implemented with different address formats)

## knaccc | 2017-02-17T06:33:49+00:00
I think there might be some confusion because I did make multiple edits to https://github.com/monero-project/research-lab/issues/7#issuecomment-280556481 which you may have missed prior to replying

## knaccc | 2017-02-17T06:56:00+00:00
Just in case it's not clear, i'll restate the whole thing:

Alice rolls a random number a, which is shared between each subaddress

To generate each subaddress, Alice rolls two further random numbers `b, c`
the subaddress public wallet address would be: `(A, B, C)` where `A=abG, B=bG, C=cG`
the private spend key would be `(ab, c)`
the private view key would be `(ab, C)`

Bob would compute `R = rB`
Bob would compute `P = H(rA)G + C`
Alice would compute `P' = H(aR)G + C`
Shared secret is `rA == abrG == arB == aR`
The signing key is `x = H(aR) + c`

Note that Alice's computation of `H(aR)G` is the same for every subaddress since `a` is shared between subaddresses.

The slightly confusing bit is to note I've defined `A = abG` instead of  `A = aG`, and I've defined `R = rB` instead of `R = rG`

## kenshi84 | 2017-02-17T07:04:39+00:00
Here's my interpretation of @RandomRun's original idea:
(also thanks to @luigi1111)

 # assumptions/characteristics

- Address of the recipient (Bob): `(A, B) = (a*G, b*G)`
- Address of the sender (Alice) : `(X, Y) = (x*G, y*G)`
- Alice can pay to the same sub-address of Bob any number of times
- The tx pubkey `R` is defined as a _variant of_ DH shared secret between Bob & Alice; i.e., neither Alice nor Bob can know the tx private key `r`
- The tx can have only two destinations, one to Bob and the other to Alice (as her change). Payments to more than one destinations have to be done using the standard address format.


# generating a sub-address
 
Bob's `j`-th sub-address `(j=1,2,...)` is a pair of EC points `(C,D)` where:

    m = Hs(a || j)
    M = m*G
    D = B + M
    C = a*D
 
Note that `(A,B)` and `(C,D)` are unlinkable. Bob then registers `D` to a hash table `T`:
 
    T[D] <-- j
 
To handle his main address in a unified way, Bob also registers `B` to the hash table:
 
    T[B] <-- 0
 
 
# sending to a sub-address
 
When constructing a transaction, Alice first chooses a random scalar `s` and generates a tx pubkey:

    R = s*D

She then computes an output pubkey to Bob:

    P = Hs(s*C)*G + D

She finally computes an output pubkey to herself as her change:

    Q = Hs(x*R)*G + Y
 
Alice can prove her payment to Bob by using `s`.
 

# receiving by a sub-address
 
Bob checks if an output pubkey `P` in a new transaction belongs to him or not by computing
 
    D' = P - Hs(a*R)*G
 
and looking for `D'` in the hash table. If the transaction was indeed bound to Bob's sub-address `(C,D)`, `D'` should equal to `D` because
 
    a*R = a*s*D
        = s*a*D
        = s*C
 
Therefore, Bob should be able to find `D'` in the hash table:
 
    j <-- T[D']
 
and obtain the private key of `P`:
 
    p = { Hs(a*R) + b                   j == 0
        { Hs(a*R) + b + Hs(a || j)      otherwise
 
 
# disposable address
 
Bob can generate a one-time disposable address associated with one of his sub-addresses `(C,D)` using a 64bit random payment ID `k` as `(C~,D~,k)` where
 
    m~ = Hs(a || k)
    M~ = M~*G
    D~ = D + M~
    C~ = a*D~
 
Note that `(C,D)` and `(C~,D~,k)` are unlinkable. To reduce the additional scanning time, the class of `k`'s that can be used for Bob's disposable addresses is limited to those satisfying the following equation:
 
    Hs(a || k) % 256 == k % 256                                 (1)

Bob can also generate one-time disposable addresses associated with his main address `(A,B)` as a special case: 

    m~ = Hs(a || k)
    M~ = m~*G
    D~ = B + M~
    C~ = a*D~


## sending to a disposable address
 
Alice's procedure is exactly the same as above: she first generates a tx pubkey:
 
    R = s*D~
 
and then generates an output pubkey `P` to Bob:

    P = Hs(s*C~)*G + D~
 
Importantly, she finally attaches the payment ID `k` to the transaction *without* encryption.
 

## receiving by a disposable address
 
When Bob processes a new transaction, he first computes
 
    D~' = P - Hs(a*R)*G
 
and looks for `D~'` in the hash table. If not found, and if the transaction has a payment ID `k` that satisfies equation (1), Bob then computes
 
    m~ = Hs(a || k)
    M~ = m~*G
    D' = D~' - M~
 
and looks for `D'` in the hash table. If the transaction was indeed bound to Bob's disposable address `(C~,D~,k)`, `D~'` should equal to `D~` because
 
    a*R = a*s*D~
        = s*a*D~
        = s*C~
 
and `D'` should be found in the hash table:
 
    j <-- T[D']
 
Bob can obtain the private key of `P` as:
 
    p = {Hs(a*R) + b + Hs(a || k)                   j == 0
        {Hs(a*R) + b + Hs(a || k) + Hs(a || j)      otherwise

**Edit:**
Swapped `C` and `D` so that `C` and `D` nicely correspond to `A` and `B`, respectively.

## RandomRun | 2017-02-17T20:30:15+00:00
@knaccc: I think I just found my blunder, but it may actually fix thiings: the view key is not `(ab, bG)` as I wrote. Rather it is still just `(a, bG)`!

## knaccc | 2017-02-17T20:45:20+00:00
@RandomRun You were right that the view key for an individual subaddress was `(ab, bG)` - but as you point out you never need to give those to an auditor because you can just simply give out the main view key for all subaddresses `(a, bG)`. As long as no-one needs to give out the view key for an individual subaddress, there is no problem, so my (A, B, C) style address is most probably overkill. Very nice solution by the way, I'm still working through it to check for any issues but I really like it.

## RandomRun | 2017-02-17T21:01:08+00:00
@knaccc: Thanks!

View key: If you were given only `(ab, bG)` and wanted to check whether `(P, R)` belongs to Alice, how would you do it?

## knaccc | 2017-02-17T21:05:30+00:00
@RandomRun You can't do it if you're only given one view key. But if you have been given 2 view keys as an auditor, you might be able to find the common factor `a` between the two pairs `ab_1` and `ab_2`. As I say, that's no big deal since I don't see the need to give out the individual subaddress view keys at all, the master view key for all subaddresses `(a, bG)` will be what the auditor will want.

The issue I'm highlighting isn't that you can tell (P, R) belongs to Alice, as far as I know, but it's that `a` can be discovered from the view keys of two different subaddresses. 

## RandomRun | 2017-02-17T21:16:44+00:00
@kenshi84:
> The tx pubkey R is defined as a variant of DH shared secret between Bob & Alice; i.e., neither Alice nor Bob can know the tx private key r

The way I suggested, the sender can keep track of each value `r` used to produce each output `P`, so we would have a `R` for each `P`. We can talk about outputs keys, instead of transaction keys.

Edit: I see now that the transactions key, in the usual sense, allows the sender to provide evidence of authoring a transaction without revealing any information about the recipient's address. In this new setup, the sender could still show evidence of authoring the output `P`, but that would require revealing part of the address.

Edit: Please see my first comment, as it contained an error and has been edited.

## RandomRun | 2017-02-17T21:20:26+00:00
@knaccc: Please see my first comment, it contains a mistake which I have edited. The correct view key pair doesn't contain the product `ab`.

## RandomRun | 2017-02-17T21:28:00+00:00
@knaccc: `R = r(bG)`, so what you need as an auditor is `(a, bG)`, so you can check that `H(aR) = H(a(rbG)) = H(r(abG))`. If you do that starting with `ab` instead of just `a` you end up with an extra`b`.

## knaccc | 2017-02-17T21:42:58+00:00
@RandomRun I think I might have gotten myself into a muddle because lots of the workings I have been using may have been using the original `(ab, bG)` without properly amending it as you've noted. I think I'm having an algebraic meltdown because `b` has different meanings across my notation, your notation and kenshi84's.

## knaccc | 2017-02-17T23:09:39+00:00
@kenshi84 So you're saying that a subaddress `(C, D) = ((b+m)G, a(b+m)G)`. I think it's fantastic.

The view key per subaddress in @kenshi84's notation is `(a, (b+m)G)`, which means that the holder of any two view keys can discover that both subaddresses belong to the same person, but I don't think that's a problem as long as users are told not to give out different view keys except to someone they don't care is aware that those subaddresses belong to the same person.

## RandomRun | 2017-02-19T14:25:42+00:00
@kenshi84: 
> Here's my interpretation of @RandomRun's original idea

Yes, I think it is pretty much all there. 

[I was a bit thrown off by the notation, so this is just one suggestion, if I may: can we flip the address notation, like `(C,D) := (D,C)`, so that the last part is the spend public key that gets added to the one-time address so that neither sender nor auditor can move the money?]

> The tx pubkey `R` is defined as a variant of DH shared secret between Bob & Alice; i.e., neither Alice nor Bob can know the tx private key `r`
The tx can have only two destinations, one to Bob and the other to Alice (as her change). Payments to more than one destinations have to be done using the standard address format.

The way I understand it, currently each transaction contains only one key `R` that allows different recipients to deduce which one-time addresses, and corresponding private keys, belong to them. It also serves as a way for the sender to prove that he authored the transaction, although that is something outside of the protocol level.

If the sender tries to use the same value to create both one-time addresses for the recipient and for the change, then this has a couple of disadvantages. (i) As you noted, only those two people can be part of the transaction; [~~(ii) Alice and Bob have different ways to check whether the one-time addresses belong to them, one asuming they were the recipient, and another time as if they were getting the change, so that would double the scanning time.~~ **Edit**: (ii) is nonsense, it is the same procedure indeed, as both Alice and Bob use `R` directly in their scanning multiplied by `a` or `x`, correspondingly...]

Having a different `s`, and corresponding `S = sC` published, would preserve the ability to have multiple receivers (and senders), and would allow each sender to prove authorship of each output individually and as needed, as opposed to proving authoring the whole transaction. 

In fact, considering that we usually assume that one transaction has a single author, represented by their knowledge of `r`, I was wondering if using different values of `S` for individual outputs could break that assumption, kind of like what allowed for coinjoin transactions in Bitcoin. Of course Monero already has good privacy, but we can always introduce one more level of uncertainty, and who knows what challenges will come up, and the solutions people might want to build on top of this?

**Sub-addresses**:

From what I understood, addresses would be now of the form: `(C, D) = (b_j*G, a*b_j*G)` with `b_j = b + h(a || j)`, and the corresponding view key (in the sense of the information used by an auditor, or light client server, to see incoming transactions) is `(a, b_j*G)`. This means the auditor would eventually figure out `b*G` and know the whole sequence of view keys, for all `j = 1, 2, ...`, even though the user might have provided just a couple of such view keys, and that is because `a` is also the seed to the pseudo RNG that creates that sequence. There is nothing necessarily bad about it, provided that the user wants to do that for convenience, in the cases where privacy is not such a big concern. But if they want better privacy, maybe it is best to use `b_j = b + h(s || j)`, where `s` is some secret seed that is stored locally in the user's wallet. Perhaps we can even take `s = b`? 

**Disposable addresses**:

This is just sub-addresses with `j` being drawn uniformly at random from `{0,1}^{64}`, as opposed to sequentially, and stored on the blockchain, as opposed to the user's wallet? If so, isn't the utility of it already contained in the regular sub-address construction?

## RandomRun | 2017-02-19T15:42:03+00:00
By the way, instead of `j` being a naturan number, we could just pick any secret `s`, according to some deterministic pseudo random rule, and use it as our `b_j`. Meaning that the addresses would again look like `(s*G, a*s*G)`.

So now if we consider, for instance, a Bitcoin HD wallet scheme (like BIP0032/BIP0044, I believe), and `s` to be the private key generated at each node of the tree, then we have just got ourselves Monero HD wallets for free, with all the nice structures of sub wallets/accounts that come with it!

## knaccc | 2017-02-19T16:13:39+00:00
@RandomRun You've written it as `(C, D) = (b_j*G, a*b_j*G) with b_j = b + h(a || j)`, meaning:
`(C, D) = ((b + h(a || j))*G, a*(b + h(a || j))*G)`

@kenshi84 wrote it as:
`(C, D) = (a*D, B + M) =  (a(B+M), B+M) = (a(b+m)G, (b+m)G)`, meaning:
`(C, D) = (a*(b + (h(a || j)))*G, (b+h(a || j))*G)`

So for clarity on two contiguous lines:
`(C, D) = ((b + h(a || j))G, a*(b + h(a || j))*G)` @RandomRun 
`(C, D) = (a*(b + (h(a || j)))*G, (b + h(a || j))*G)` @kenshi84 

@kenshi84 just needs to define in his document `C` as the public view key and `D` as the public spend key to clear up this confusion. @luigi1111 has previously commented on IRC that he also prefers the order to be (spend, view), i.e. he'd prefer to see written:
`(D, C) = (b + h(a || j))*G), a*(b + (h(a || j)))*G)`

We'd better pick a preference for the order or it'll get very confusing. I personally prefer that `A` or `C` should mean a public view key and `B` or `D` should mean a public spend key (as the cryptonote white paper does), although feel free to contradict that if the source code or other documentation does things differently.

## andre-amorim | 2017-02-19T18:10:04+00:00
fwd{ack}

## kenshi84 | 2017-02-21T09:57:10+00:00
@RandomRun 

> Having a different s, and corresponding S = sC published, would preserve the ability to have multiple receivers (and senders)

I have considered this approach and consulted privately with @luigi1111 but the conclusion was that the computational cost due to additional key derivation processes for per-output tx pubkeys would be unacceptably high.

> This means the auditor would eventually figure out b*G and know the whole sequence of view keys, for all j = 1, 2, ...

The point of my proposal is to achieve sub-addresses while still being able to scan outputs in new transactions using the same key derivation `a*R` - the auditor needs to know `a` in order to recognize incoming transfers. The reason I chose sequential numbers for `j=0,1,2...` was to be able to reconstruct the wallet solely from the seed. If we relied on some other secret to generate sub-addresses, that would mean that the user needs to remember that extra secret in addition to the wallet seed. I don't find this approach particularly appealing.

> This is just sub-addresses with j being drawn uniformly at random from {0,1}^{64}, as opposed to sequentially, and stored on the blockchain, as opposed to the user's wallet?

No. Disposable address is different from sub-address, actually it builds on top of sub-address. It derives additional random pubkey `M~` from an unencrypted payment ID and adds it to the spend pubkey `D` of an existing subaddress. Because sub-addresses need to be stored in a hash table, we can have only moderate number of sub-addresses, such as 10000; millions or billions of subaddresses would be impractical to handle. In contrast, disposable addresses can be created practically unlimited number of times. Its downside is that it doesn't allow reuse, obviously.


## RandomRun | 2017-02-22T20:47:20+00:00
Apologies in advance for asking so many questions at once. I am just trying to understand things!

> the computational cost due to additional key derivation processes for per-output tx pubkeys would be unacceptably high.

Since a tipical transaction is expected to have, for the most part, only two outputs, I guess that would about double the scanning cost, or are there more complications to it?

>The point of my proposal is to achieve sub-addresses while still being able to scan outputs in new transactions using the same key derivation `a*R` - the auditor needs to know a in order to recognize incoming transfers.

What is the plan in that case, use subaddresses in transactions that only involve Alice and Bob, and keep the usual static address scheme working for other transactions? [Edit: I see you answered yes to that [here](https://github.com/monero-project/monero/pull/1753).] I wonder how many people will stick with static addresses when subaddresses comes out. 

> The reason I chose sequential numbers for `j=0,1,2...` was to be able to reconstruct the wallet solely from the seed. If we relied on some other secret to generate sub-addresses, that would mean that the user needs to remember that extra secret in addition to the wallet seed. I don't find this approach particularly appealing.

Storing two secrets `(a, b)` is not that different than storing just `a`, which is what is currently done already. And of course the user would retain the ability to recover all their keys with just that pair and reconstructing the sequence with ` j=0,1,2...`. As I pointed out, if you don't use another secret value `b`, then giving out just a couple of your view keys would reveal them all, which may or may not be a good thing, depending on the use case. Maybe I am missing some other problem or costs?

> No. Disposable address is different from sub-address

I still don't see this. I mean, if you go by your description of how to generate them, it seems like it is just copy and paste, replace `j` with `k`, and put tildas on what is generating using the `k` value.

The exception being the generation of `D` and `D~`:

`D = B + M`
`D~ = D + M~ = B + M + M~`

but I am not quite sure I get why it is defined like that. What would be the problem the problem of using `D~ = B + M~`? And in any case, you can choose to publish `k` on the blockchain, or keep it stored locally, it seems.

>  Because sub-addresses need to be stored in a hash table, we can have only moderate number of sub-addresses, such as 10000; millions or billions of subaddresses would be impractical to handle. In contrast, disposable addresses can be created practically unlimited number of times. Its downside is that it doesn't allow reuse, obviously.

I like your optimism estimating the number of addresses a user will need! :) Although I guess one use case could be an exchange.

When you say it doesn't allow reuse, you mean that it is not good practice to reuse them, and that, unfortunatelly, depends on the sender, right?

## kenshi84 | 2017-02-23T00:50:38+00:00
> Since a tipical transaction is expected to have, for the most part, only two outputs, I guess that would about double the scanning cost, or are there more complications to it?

Doubling the scanning cost is already way more than unacceptable. In addition, it'll be more than double since some transactions are multi-destination transfers, e.g. transfer to 4 or 5 recipients. This is most common for pool payouts which is not the majority of all transactions. Imposing such an immense additional cost to all users merely to enable multi-destination transfer with subaddresses, would be inappropriate.

> I wonder how many people will stick with static addresses when subaddresses comes out.

Subaddresses in the current implementation is fully usable for the most common use case which is payment to a single recipient. Less common multi-recipient transfers can be just done using standard addresses. After hard thinking and private discussion with @luigi1111, I came to a conclusion that there doesn't seem to be any workable way of achieving sub-addresses capable of multi-recipient transfer without increased scanning cost. My proposed scheme provides clear improvements over Monero's privacy feature at practically zero cost, so I don't see any reason not to use it (after thorough reviewing and testing, of course).

> giving out just a couple of your view keys would reveal them all, which may or may not be a good thing

I don't understand what you're trying to say. Watch-only wallet `(a,B)` (i.e. the pair of view secret key and spend public key) is supposed to allow you to see all incoming transfers, so my proposal simply follows that principle.

> I still don't see this. I mean, if you go by your description of how to generate them, it seems like it is just copy and paste, replace `j` with `k`, and put tildas on what is generating using the `k` value.

I'm a bit puzzled that this simple idea doesn't get understood by you so easily while it did for other people like @knaccc and @JollyMort. I hope this Reddit post of mine helps:

https://www.reddit.com/r/Monero/comments/5vgjs2/subaddresses_and_disposable_addresses/de28cd1/

> I am not quite sure I get why it is defined like that. What would be the problem the problem of using `D~ = B + M~`? And in any case, you can choose to publish `k` on the blockchain, or keep it stored locally, it seems.

`D~ = B + M~` _is_ a disposable address associated with index=0 which corresponds to the original standard address. The disposable address scheme works only when `k` is stored on the blockchain without encryption; storing `k` locally would be useful for accounting purposes (i.e. to recognize who the payment is from, just like the standard payment ID), but not for scanning.

## JollyMort | 2017-06-21T20:25:59+00:00
Implemented :)

# Action History
- Created by: JollyMort | 2017-02-08T18:16:14+00:00
- Closed at: 2017-06-21T20:25:59+00:00
