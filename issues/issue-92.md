---
title: Seraphis Address Schemes
source_url: https://github.com/monero-project/research-lab/issues/92
author: UkoeHB
assignees: []
labels: []
created_at: '2021-11-12T16:47:21+00:00'
updated_at: '2024-04-03T00:28:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Seraphis Address Schemes

Seraphis is not compatible with CryptoNote addressing, due to a different key image design compared to CryptoNote. However, it _is_ compatible with a variety of interesting addressing schemes. In this issue I'd like to present those schemes, so discussion can have a point of reference.

To implement Seraphis in Monero, or another existing CryptoNote-derived cryptocurrency, it would be necessary for all users to generate new public addresses from their private keys (old public addresses would become unusable). They would not need new wallets, just addresses.


### The Schemes

Here are the adddress scheme variants. The 'tiers' are levels of wallet permissions. A Tier 3 wallet can always do everything, while a Tier 2 wallet can never spend funds. A 3-key address would be ~50% longer than existing addresses. Note that 'Janus' refers to the ability to detect a [Janus attack](https://github.com/monero-project/research-lab/issues/62).

|&nbsp;&nbsp;&nbsp;Type&nbsp;&nbsp;&nbsp;| Tier 1          | Tier 2 (+ Tier 1) | Tier 3 (+ Tiers 1 & 2) | Address Size (\#keys) |
|-----------|-----------------|-------------------|------------------------|--------------------|
| Plain A | none            | view received     | spend, view spent      | 2                       |
| Plain B | view received   | view spent        | spend                  | 2                       |
| Plain C | none            | view received, view spent | spend          | 2                       |
| Plain D | compute view tags    | view received, view spent | spend          | 3                       |
| Janus A | view received, Janus     | view spent | spend                | 3                       |
| Janus B | view received (no amounts) | view amounts, view spent, Janus | spend | 3               |
| Janus C | view received (no amounts), view spent | view amounts, Janus | spend | 3               |
| Janus D | none | view received, view spent, Janus | spend              | 3                       |
| Janus E | compute view tags    | view received, view spent, Janus | spend          | 4                       |

- Plain A is functionally equivalent to CryptoNote (however, users would still need new public addresses). The biggest weakness of this scheme is needing Tier 3 to identify spent outputs, which leads to the annoying 'export key images' UX for multisig and hardware wallets.
- 'Plain' variants can mitigate Janus using Tier 1 if data is added to output/transaction memos (one 16-byte encrypted txout private key nonce per output).
- 'Janus' variants mitigate Janus by adding an [extra key](https://github.com/monero-project/research-lab/issues/62#issuecomment-870147617) to addresses. Conveniently, adding this extra key allows more diverse addressing schemes (as shown in the table).
- 'View amounts' generically means 'decrypt messages stored in output memos'. This includes amounts and any miscellaneous encrypted memos that might be stored in memos.
- (@tevador on the 'compute view tags' variants): A Tier 1 wallet would only be able to identify a `2^-T` blockchain subset that contains all of the wallet's actual outputs (here T is the size of the view tag). This would preserve more privacy when using an external scanning service at the cost of more computation for the client to filter out the false positive outputs. The size of the view tag T should be selected as a compromise between anonymity and the amount of data to be downloaded.
  - With all other variants, 'compute view tags' and 'view received' are the same.

Finally, I want to point out that Tier 2 always (except for Plain A) has 'full-view' authority. The main difference between schemes lies in Tier 1 capabilities.


### P.S.

Moving to a new address scheme means it is possible to deprecate normal addresses entirely (i.e. only use subaddresses). This would allow a uniform address format, which would improve UX. Users could use their 'index 0' subaddress in place of their current normal address (or some similar convention).

Deprecating normal addresses is not required, it is just an option to consider.

# Discussion History
## LocalMonero | 2021-11-12T18:03:59+00:00
Unifying to just one type of address should be a design goal. The UX and DX gets exponentially worse with each additional address type.

## rbrunner7 | 2021-11-12T18:48:12+00:00
Regarding Janus, do I read this correctly: The question is whether we judge the Janus attack to be serious enough to merit even longer addresses than today, as a sensible choice?

## UkoeHB | 2021-11-12T18:56:19+00:00
> Regarding Janus, do I read this correctly: The question is whether we judge the Janus attack to be serious enough to merit even longer addresses than today, as a sensible choice?

Yes, but part of the question is also if we want one of the Janus address schemes, due to their basic utility compared to plain schemes (I think Janus B and C are big improvements, since they allow third party scanning without leaking amounts).

## rbrunner7 | 2021-11-12T19:04:13+00:00
> Yes, but part of the question is also if we want one of the Janus address schemes, due to their basic utility compared to plain schemes (I think Janus B and C are big improvements, since they allow third party scanning without leaking amounts).

Thanks, I indeed overlooked the "amounts visible or hidden" dimension until now. Interesting.

## boogerlad | 2021-11-12T20:25:41+00:00
For Janus C Tier 1, "view received (no amounts), view spent" does that mean spent amounts are visible?

## UkoeHB | 2021-11-12T20:27:15+00:00
> For Janus C Tier 1, "view received (no amounts), view spent" does that mean spent amounts are visible?

No... view spent just means 'view what outputs have been spent' (i.e. compute key images for received outputs to check if they exist in the ledger).

## boogerlad | 2021-11-13T00:14:36+00:00
As you said, Janus B and C allow for third party scanning without leaking amounts, which I think makes services like MyMonero way more useful. What would the UX differences be between B and C? As in, in what situation would it be useful for services like MyMonero to know which outputs are spent and presumably when they are spent?

## UkoeHB | 2021-11-13T01:08:17+00:00
> What would the UX differences be between B and C? As in, in what situation would it be useful for services like MyMonero to know which outputs are spent and presumably when they are spent?

If a scanning service can identify spent outputs, then your personal wallet doesn't have to do _any_ scanning. However, this has privacy costs, since the service will learn more information about your transaction flows (i.e. if the service became large enough, then it could basically eliminate the utility of ring signatures).

## UkoeHB | 2021-11-15T14:17:59+00:00
> If a scanning service can identify spent outputs, then your personal wallet doesn't have to do any scanning. However, this has privacy costs, since the service will learn more information about your transaction flows (i.e. if the service became large enough, then it could basically eliminate the utility of ring signatures).

On the other hand (I forgot...), a scanning service that can see all your received outputs can also infer most/all of your spent outputs. The reason is, most/all of the transactions you make will A) have 1+ of your owned outputs in each input's ring members, B) send a _change output_ to you.

Since a scanning service can identify most spent outputs, Janus C might be simply better than Janus B. With Janus B, identifying spent outputs with Tier 1 is not reliable enough to be provided as a feature of a scanning service, but it _is_ reliable enough to degrade privacy. With Janus C, the UX of scanning improves, while the privacy costs stay the same.

**Caveat**: If membership proofs referenced the entire ledger, instead of a small ring, then inferring spent outputs would not work as well (if at all). Since achieving membership proofs on that level is a big goal of privacy-coin research, a 'forward-looking' designer might favor Janus B over Janus C. This way, if ideal membership proofs are ever implemented, the privacy dynamic around scanning is optimized.

## tevador | 2021-11-15T16:30:20+00:00
I haven't studied Seraphis in detail, but I'm wondering if there could also be another option:

|Type|   	Tier 1|	Tier 2 (+ Tier 1)|	Tier 3 (+ Tiers 1 & 2)|	Address Size (#keys)|
|-----|-----------|---------------------|---------------------------|---------------------------|
|Plain D/Janus E|	view tag | view received, view spent, Janus(?) |	spend |	3

A Tier 1 wallet would only be able to identify a <code>2<sup>-T</sup></code> blockchain subset that contains all of the wallet's actual outputs (here `T` is the size of the view tag in bits). This would preserve more privacy when using an external scanning service at the cost of more computation for the client to filter out the false positive outputs. The size of the view tag `T` should be selected as a compromise between privacy and the amount of data to be downloaded.

I put a question mark next to Janus because I'm not sure if this scheme can also mitigate Janus without some additional TX data.


## UkoeHB | 2021-11-15T18:30:40+00:00
@tevador yes I think it is possible. I will add this to the table. It would cost +1 in the address size compared to other schemes.

## chaserene | 2021-11-15T20:14:50+00:00
Is it possible to devise an addresses scheme that won't have to be changed for a long time, e.g. not even with further ring size increases like Arcturus? Requiring everyone who wants to receive to generate a new address is a big pain point, breaking numerous use cases, both known and unknown.

## UkoeHB | 2021-11-15T20:16:39+00:00
> Is it possible to devise an addresses scheme that won't have to be changed for a long time, e.g. not even with further ring size increases like Arcturus? Requiring everyone who wants to receive to generate a new address is a big pain point, breaking numerous use cases, both known and unknown.

Why would any of the above schemes need to be changed, once implemented?

## chaserene | 2021-11-16T02:04:24+00:00
@UkoeHB I don't know in advance. I'm following the logic that van Saberhagen didn't expect it either that it will need to be changed.

## UkoeHB | 2021-11-16T02:10:51+00:00
> @UkoeHB I don't know in advance. I'm following the logic that van Saberhagen didn't expect it either that it will need to be changed.

Likewise, there is no way for any of us to know in advance what the future will bring.

That being said, Seraphis is designed so membership proofs (e.g. ring signatures) are almost entirely independent of addressing. You can easily change the membership proof type without risking changes to the address scheme. In that sense, Seraphis is far more robust against address changes than CryptoNote.

## xxmeta | 2021-11-18T05:27:13+00:00
I think Janus detection should be a priority.

I am leery of enabling 3rd party scanning, as with Janus B & C. 99% of people will allow 3rd party services to scan their entire wallets. The rest of us will not have much anon set, and no way to know if our anon set is any good.

I lean towards Janus A.

## UkoeHB | 2021-11-18T20:35:28+00:00
> I am leery of enabling 3rd party scanning, as with Janus B & C. 99% of people will allow 3rd party services to scan their entire wallets. The rest of us will not have much anon set, and no way to know if our anon set is any good.

@xxmeta I think it is unlikely we can prevent people from offering scanning services without completely unifying all three wallet tiers. Why do you favor Janus A over Janus B/C? Janus B's Tier 1 is significantly weaker than Janus A's Tier 1, and I think Tier 1 is what scanning services would use.

## xxmeta | 2021-11-18T22:48:25+00:00
> > I am leery of enabling 3rd party scanning, as with Janus B & C. 99% of people will allow 3rd party services to scan their entire wallets. The rest of us will not have much anon set, and no way to know if our anon set is any good.
> 
> @xxmeta I think it is unlikely we can prevent people from offering scanning services without completely unifying all three wallet tiers. Why do you favor Janus A over Janus B/C? Janus B's Tier 1 is significantly weaker than Janus A's Tier 1, and I think Tier 1 is what scanning services would use.

I agree with you now about the 3rd party service risk. In light of that, Janus A & B are similar to me. I think the Janus attack can still be practically applied if users use a Tier1 key for fast sync times, so maybe I prefer Janus A for that reason, but the choice is not obvious.

Janus C is less useful I think. I can see many uses for a Tier 1 key that can't view spends, but Janus C doesn't allow that.

## ghost | 2021-11-19T17:05:28+00:00
@UkoeHB continuing the offline-tx discussion from gitlab: 

so Serpahis view-only wallets would eliminate the need to import key images and cut the process down to 3 steps?

1) create transaction on view-only wallet

2) sign tx on offline device

3) broadcast signed tx from online device 



## UkoeHB | 2021-11-19T17:09:17+00:00
@r4v3r23 yes that sounds right to me. 1 -> 2 and 2 -> 3 require communication passes to and then from the offline device.

## ghost | 2021-11-19T17:14:37+00:00
> @r4v3r23 yes that sounds right to me. 1 -> 2 and 2 -> 3 require communication passes to and then from the offline device.

yes Seraphis simplifies the process so that it can be done easily between mobile devices via QR codes







## tevador | 2021-12-02T21:34:39+00:00
There is no doubt that Seraphis will bring quite large user-facing changes regardless of which exact addressing scheme is used. It may be worthwhile to take this opportunity to rethink the paradigm and *move away from addresses completely*.

I understand that this might be too radical and it's unlikely to be implemented in Monero, but I'm going to discribe it anyways in case someone cares.

I will preface this with an explaination why addresses are bad, then I will present an alternative and describe how it works from the user's point of view. The cryptographic details are at the end.

### The original vision

Satoshi Nakamoto originally thought of addresses as "account numbers" and they were meant to be handled and compared by humans directly ([see this comment in Bitcoin 0.1](https://github.com/bitcoin/bitcoin/blob/4405b78d6059e536c36974088a8ed4d9f0f29898/base58.h#L6-L13)). This was also the reason why Bitcoin addresses were 160-bit hashes - to be as short as possible. A typical v1 Bitcoin address is 34 characters long, which is coincidentally the maximum length an [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) can have.

### Problems of addresses

Nowadays cryptocurrencies are not used just by enthusiasts and the inherited paradigm of base58-encoded account numbers is, in my opinion, a UX nightmare. Especially for Monero, the original vision clearly fails. 100+ character strings encoding 2-3 public keys can hardly be considered as identifiers anymore.

 I'd wager that the vast majority of crypto transfers involve copy pasting meaningless strings without any feedback to the user. The main issues of this are:
 
 1. Security. Using humans to verify and pass around cryptographic material is just about the worst option. One of the common attacks involves [clipboard address swapping malware](https://www.reddit.com/r/Monero/comments/mcvuxc/beware_crypto_stealing_malware/).
 2. Susceptibility to mistakes. People send funds to the wrong address all the time. This is also the primary reason why [integrated addresses are still popular](https://github.com/monero-project/monero/issues/7889#issuecomment-907254477) and many people are against deprecating them.
 3. Addresses lack context. From a UX standpoint, the public keys only make sense when bundled with an amount, a human-readable name an a reason to pay. The terms "address" and "address book" imply that they are some sort of identifiers, which is wrong. Addresses are meant for a single use.
 
 ### OpenAlias is not the answer

 Someone might argue that [OpenAlias](https://openalias.org/) is a working alternative to addresses. However, I don't think it can solve the problem for several reasons:

* Not all Monero users can or are willing to register a domain name.
* Putting the whole Monero address into a DNS record is a security issue. If the TXT record is compromised, funds can be redirected to a different address without the sender noticing anything.
* Using OpenAlias leaks information through the DNS system. Whenever an OpenAlias domain name is resolved, an eavesdropper can learn that a particular IP address might be transacting with a particular Monero address.
* OpenAlias is not practical for merchants that need to provide different payment information to every customer. In fact, I've only seen OpenAlias being used for donations and nothing else.

### Possible solution

Everytime a Monero address is shared, there is an implicit expectation of a payment. It may either be a donation without a specific amount and specific sender, or an exact amount as a payment for goods or services. The payee is clearly defined in both cases.

Therefore we can replace addresses with payment requests. A payment request encapsulates all the information the payer's software needs to complete the payment:

1. Version field
1. One or more public keys
1. Payment amount (optional)
1. The recipient's email address or domain name (optional)
1. Payment description (optional)
1. Signature of the above fields with a key tied to the recipient's identity

The main difference from the existing Monero payment url scheme is that each payment request is authenticated with a signature.

The way a payment request is transferred to the wallet software can be entirely opaque to the user. There is no need to examine or compare any cryptographic information (with a single exception described in the next section).

Here are some ways how the actual data transfer can happen:

1. Scanning a QR code
1. Clicking a URL with a custom scheme handler
1. Direct HTTP request
1. Manually copying an ASCII-armored string (for text-only protocols)
1. Manually downloading a file from a website/email attachment

All of these can easily support transferring a few hundred bytes needed for a payment request.

### Authenticating the recipient

Once the payment request reaches the payer's wallet software, there are 4 options:

1. The payee's authentication key is already stored in the sender's address book. The signature can be verified directly.
1. The payee has a website. In that case, the authentication key can be downloaded from a DNS TXT record. Note that unlike OpenAlias, a compromised TXT record doesn't lead to a loss of funds.
1. The sender and the receiver are communicating through an onion service. Then the onion public key can be used as the authentication key.
1. The payee's authentication key must be verified manually by the sender. This should be done out-of-band and involves comparing short strings that look like this: `QP4RJ-HIT6W-Z99R1-YFQPP-6PC1Y`.

If the signature of the payment request matches, the user interface should display a prominent symbol, like a check mark: ✔. This is the same paradigm as the padlock symbol for HTTPS and is familiar to users.

(As a side note, the signature also helps with dispute resolution. [The current payment proofs](https://www.getmonero.org/resources/user-guides/prove-payment.html) cannot resolve the case when Bob claims the address Alice made a payment to is not his.)

### User stories

#### Online shopping

1. Charlie buys goods on shop.example.com for the first time.
1. At checkout, he scans a QR code.
1. A prompt is displayed: "You are paying 10 XMR to shop.example.com (verified ✔). Press OK to continue."
1. Charlie presses OK and enters the wallet password.
1. The payment is done.

#### Donation

1. Dave wants to donate to a CCS request as he usually does.
1. He clicks a "donate" button in the CCS request and is redirected to his wallet software.
1. A prompt is displayed: "You are transacting with Monero CCS (verified ✔). The payment is for Atomic swaps XMR/BTC. Please enter an amount to pay."
1. Dave enters an amount, confirms and enters the wallet password.
1. The payment is done.

#### Paying a friend

1. Frank wants to repay a debt to his friend John.
1. He receives a payment request from John via email and drag-and-drops the email attachment into his wallet software.
1. A prompt is displayed: "You are transacting with john.smith@example.com for the first time. Please use an out-of-band communication channel and let them verify that this is their identity: `QP4RJ-HIT6W-Z99R1-YFQPP-6PC1Y`."
1. Frank calls John to confirm that the identity code is his and adds him into his address book.
1. Frank confirms the payment and enters his wallet password.
1. The payment is done.

#### Paying an anonymous user

1. Victor buys some goods from an anonymous online vendor via an onion service.
1. The seller provides him with a payment request, which Victor pastes into his wallet software.
1. A prompt is displayed: "You are paying 5 XMR to example3s7zyrievebrzkactalswnhakbpkazjz2ccimxcfqck52pgyd.onion (verified ✔). Press OK to continue."
1. Victor presses OK and enters the wallet password.
1. The payment is done. 

### Under the hood

This "address-less" scheme is compatible with Seraphis and behaves similar to the "Janus D" option with an extra Tier 1 capability:

|Type|   	Tier 1|	Tier 2 (+ Tier 1)|	Tier 3 (+ Tiers 1 & 2)|	Address Size (#keys)|
|-----|-----------|---------------------|---------------------------|---------------------------|
|Janus X| generate payment requests | view received, view spent, Janus |	spend |	3    |


#### Wallet

A wallet is defined by two private keys <code>k<sub>s</sub></code> (private spend key), <code>k<sub>v</sub></code> (private view key). These can be derived as usual from a mnemonic seed.

There is an associated public spend key <code>K<sub>s</sub> = k<sub>v</sub> X + k<sub>s</sub> U</code>, where `X` and `U` are generators.

#### Accounts

Each wallet can support up to 2<sup>64</sup> different identities, here called "accounts".

Each account index `i` has a private authentication key <code>k<sub>a</sub><sup>i</sup> = H(T<sub>ident</sub>, k<sub>v</sub>, i)</code>. Note that generating authentication keys requires the private view key <code>k<sub>v</sub></code>.

The associated public authentication key <code>K<sub>a</sub><sup>i</sup> = k<sub>a</sub><sup>i</sup> G</code> is used to verify payment request signatures.

Each account has one public view key <code>K<sub>v</sub><sup>i</sup> = k<sub>v</sub> K<sub>a</sub><sup>i</sup></code>.

#### Payment requests

Each account can generate up to 2<sup>64</sup> different payments requests. Each payment request is defined by two indices `i` and `j`, where `i` is the account index and `j` is the payment index.

The payment request contains the following two public keys:

* <code>K<sub>s</sub><sup>i, j</sup> = H(T<sub>payreq</sub>, k<sub>a</sub><sup>i</sup>, j) X + K<sub>s</sub></code> (spend key)
* <code>K<sub>v</sub><sup>i</sup></code> (view key)

Note that the second key doesn't depend on the index `j`.

Additionally, each payment request contains a Schnorr signature `(R, s)` where:

* <code>R = r G</code>
* <code>s = r + k<sub>a</sub><sup>i</sup> * H(T<sub>sig</sub>, R, m)</code>, where `m` is the serialized payment request (the above two public keys and optional metadata).

#### Sending funds

The sender, when presented with a payment request, first needs to recover the public authentication key <code>K<sub>a</sub><sup>i</sup></code>. There are four ways to do that:

1. Lookup the key in the address book (either by payee's name or by the key <code>K<sub>v</sub><sup>i</sup></code>).
1. Lookup the key in a DNS TXT record (if interacting via a domain name).
1. Decode the key from the onion address (if interacting via an onion service).
2. Recover the key from the Schnorr signature: <code>K<sub>a</sub><sup>i</sup> = H(T<sub>sig</sub>, R, m)<sup>-1</sup> (s G - R)</code>

In the last case, the key should be validated manually. The validation code is simply <code>H(T<sub>val</sub>, K<sub>a</sub><sup>i</sup></code>) truncated to 120 bits and encoded in Base32 with a Reed-Solomon checksum digit that ensures two validation codes differ in at least 2 characters.

The output is constructed as follows:

1. A random scalar `t` is generated.
1. The sender-receiver shared secret is: <code>q = H(T<sub>deriv</sub>, t K<sub>v</sub><sup>i</sup>)</code>
1. The one-time output key is: <code>K = H(T<sub>key</sub>, q) X + K<sub>s</sub><sup>i, j</sup></code>
1. The output public key is: <code>Q = t K<sub>a</sub><sup>i</sup></code>
1. The output blinding factor is constructed as <code>C = H(T<sub>blind</sub>, q, t G) G + b H</code>

#### Receiving funds

1. Calculate nominal sender-receiver shared secret: <code>q = H(T<sub>deriv</sub>, k<sub>v</sub> Q)</code>
1. Calculate the nominal spend key <code>K<sub>s</sub><sup>i, j</sup> = K - H(T<sub>key</sub>, q) X</code>
1. If <code>K<sub>s</sub><sup>i, j</sup></code> belongs to this wallet, look up the associated private authentication key <code>k<sub>a</sub><sup>i</sup></code>.
1. Calculate <code>C = H(T<sub>blind</sub>, q, (1 / k<sub>a</sub><sup>i</sup>) Q) G + b H</code>. If it doesn't match the output commitment, this is a Janus attack.

#### Wallet tiers

**Tier 1** wallet for account `i` knows the public keys <code>K<sub>s</sub></code>, <code>K<sub>v</sub><sup>i</sup></code> and the private key <code>k<sub>a</sub><sup>i</sup></code>. This wallet tier is suitable to be used at the point-of-sale as it can generate and sign payment requests on demand.

**Tier 2** wallet knows the public key <code>K<sub>s</sub></code> and the private key <code>k<sub>v</sub></code>. This wallet tier can generate new accounts and can see the total wallet balance.

**Tier 3** knows both private keys <code>k<sub>s</sub></code> and <code>k<sub>v</sub></code> and can spend the money in the wallet.

#### Payment IDs

Payment IDs are not needed in this protocol and can be removed entirely. This protocol can simulate both of the currently used payment schemes in Monero:

1. Integrated addresses are used by merchants to identify payments and provide assurance to customers. This can be achieved by using a long-term account and generating a new payment request for each customer.
2. Subaddresses are used where the recipient doesn't want their online activities linked together by a third party. This can be achieved by using a new account for each online purchase and only using payment requests with `j=0`.

A combination of these two approaches is also possible.

Edits:

* added an onion verification option as suggested by @LocalMonero
* fixed the calculation of the public spend key to match the Janus D address scheme 

## fluffypony | 2021-12-02T22:01:53+00:00
@tevador I like payment requests, but if LN has taught us anything its that people want both payment requests *AND* a short, offline string they can pass around (lnurl). Is there anything fundamental in Seraphis that prevents both?

## UkoeHB | 2021-12-02T22:09:36+00:00
@fluffypony it is possible to do both afaict. It is just a hassle from the implementation side, the more bulky the address scheme gets.

## fluffypony | 2021-12-02T22:10:42+00:00
@UkoeHB can't be much more cumbersome than 95-character long Monero addresses, or 100+ character long integrated addresses;)

## Mikerah | 2021-12-02T22:21:43+00:00
@tevador The main issue I see with passing around URLs is the increase risks of phishing attacks. The crypto space has spent a lot of resources and a lot of money lost to learn lessons in that URLs are not the best way to authorize funds moving from wallet to wallet. There has to be some way for a user to ensure that 1) they are sending the funds to the correct recipient and 2) that the recipient can check that they are indeed receiving the right funds from the correct sender. 

## LocalMonero | 2021-12-02T22:28:51+00:00
@tevador a few questions for you:

1. Could you please provide an example on how a payment URL would look like?
2. What about deposits to exchanges, where the amount is open-ended? Requiring the user to input ahead of time how much coins they wish to deposit is a UX nightmare.
3. Which part of the wallet do you expect to implement the DNS record calls?
4. Is relying on DNS for the green checkmark a good idea, given the centralized nature of the control structure over domain names, where states can seize domains essentially at will? Not to mention DNS poisoning in censored jurisdictions like China, where the Chinese government can essentially change the DNS TXT records to whatever they like for whichever domain they like. This isn't going to be limited to China in the future, as the trends indicate.
5. If DNS is no longer considered, is the manual code verification really that different from checking the address? Especially taking into consideration most people just check the first few and last few characters of an address.

## tevador | 2021-12-02T22:59:21+00:00
> @tevador I like payment requests, but if LN has taught us anything its that people want both payment requests _AND_ a short, offline string they can pass around (lnurl). Is there anything fundamental in Seraphis that prevents both?

A bare payment request can also be passed around as a string and would not be significantly longer than a Seraphis-Janus address (~1 scalar longer).

> The main issue I see with passing around URLs is the increase risks of phishing attacks.

Which URLs are you referring to?

> Could you please provide an example on how a payment URL would look like?

There would not be a payment URL, at least not a human readable one because there is no need for that. QR codes can directly encode binary data and a clickable URL can look something like this: `<a href="monero://M_UcZTqiEIsdlaTuJjpeze3Dx1rgxBf-E44gAH5gVM0HthU1xddkJtuHfbNgI-gOUhE6hlNPPijgN6-PIFEZJEe0dHokdvsvaJbqXgETg0ocEiL8zdYDA382S65UsTPrNmLZVLS_G_f7ZXTB1fU01K2dWLS428RTQNbSeJ8vUuQmCrrMYj3CHOb5IU2opFgirxzW0IoOvNuDB2hJQ6vxS5TKau8ofOv2gHxusTmJvrrl4J7d">PAY HERE</a>`. The user will just see a "PAY HERE" button.

> What about deposits to exchanges, where the amount is open-ended? Requiring the user to input ahead of time how much coins they wish to deposit is a UX nightmare.

That's why the amount is an optional field of the payment request. The only required fields are the 2 public keys and the signature.

> Which part of the wallet do you expect to implement the DNS record calls?

That's not relevant to this protocol. AFAIK wallet2 currently implements DNS requests to support OpenAlias.

> Is relying on DNS for the green checkmark a good idea, given the centralized nature of the control structure over domain names, where states can seize domains essentially at will? Not to mention DNS poisoning in censored jurisdictions like China, where the Chinese government can essentially change the DNS TXT records to whatever they like for whichever domain they like. This isn't going to be limited to China in the future, as the trends indicate.

There is [DNSSEC](https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions), which should be a requirement for the green check mark. The idea was that the DNS verification would be used mainly for online shopping when you are already using DNS to access the website.

> If DNS is no longer considered, is the manual code verification really that different from checking the address? Especially taking into consideration most people just check the first few and last few characters of an address.

The 25-character uppercase string is much easier to verify than a 95-character case-sensitive one*. Moreover, this verification would only be done once for each party you transact with. It's the same as when you import a GPG key for the first time.

\* Currently, there can be valid addresses that differ just in 1 character, for example (spot the difference):
<code>42zDXTDfErPYQDtZGE1JejQ5TsziFp5ep45afwzmjn9hAYxHUzJ5dBZ3udPZsMaQXbRFfBzBZv4CL7CGRfu17scNKXfFtiF</code>
<code>42zDXTDfErPYQDtZGE1JejQ5TsziFp5ep45afwzmjx9hAYxHUzJ5dBZ3udPZsMaQXbRFfBzBZv4CL7CGRfu17scNKXfFtiF
</code>





## LocalMonero | 2021-12-02T23:23:32+00:00
> There is DNSSEC, which should be a requirement for the green check mark. The idea was that the DNS verification would be used mainly for online shopping when you are already using DNS to access the website.

DNSSEC is a nightmare, a lot of registrars don't implement it or implement it poorly, and you haven't addressed the other DNS concerns.

> The 25-character uppercase string is much easier to verify than a 95-character case-sensitive one

Again, nobody checks the whole 95 chars. People check the first few and last few. The example you gave of 1 char diff is an edge case that will essentially never occur in reality. Checking it once as opposed to every time is a benefit, though.

@tevador you should consider coming up with a different **automatic** green check mechanism that doesn't rely on DNS, or at least not *just* on DNS.

## Gingeropolous | 2021-12-03T00:12:50+00:00
im all for a radical re-think :) . I can't comment directly on the technicals, but having to use DNS gives me the heebie-jeebies.

But yeah, with the possibility that seraphis address schemes will create even larger text strings than we have now, it'd be great if we could come up with something different. 

it'd be cool if you could publish something to the blockchain that would function to do something, yeah, u bloat the chain a bit...

## fluffypony | 2021-12-03T00:16:58+00:00
@Gingeropolous I don't think you *have* to use DNS, unless you want the payment request to be "verified" by a particular domain. Also agreed on the last point - aliasing on-chain is always going to be a mess, you're going to have to deal with a landrush *and* phishing.

## fluffypony | 2021-12-03T00:18:35+00:00
@LocalMonero DNS is good for validating origin against a domain. Other mechanisms (eg. have a text file on the root of the domain) would require the wallet to fetch that text file, which is a BAD idea from a privacy perspective. DNS, on the other hand, is recursive by its nature, so you almost never need to fetch the records from the canonical server.

## LocalMonero | 2021-12-03T02:54:41+00:00
@fluffypony what about onion verification?

## fluffypony | 2021-12-03T02:59:53+00:00
@LocalMonero I don't see how that changes things. Instead of "You are paying 10 XMR to shop.example.com (verified ✔). Press OK to continue." it would say "You are paying 10 XMR to duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion (verified ✔). Press OK to continue."

## LocalMonero | 2021-12-03T03:21:17+00:00
@fluffypony the difference is that control over onion domains is outside of rogue state hands (both domain seizing and DNS cache poisoning, and it's not hijackable (see the recent domain hijacking scandals).

## fluffypony | 2021-12-03T03:29:35+00:00
@LocalMonero for all of those benefits it has its own issues - eg. the private key lives on a server that people will not secure well, so then their .onion will get stolen. Either way, the reality right now is that many people are hitting a normal domain and making a payment - if they're making a payment on a .onion their threat model is likely very different.

## OrvilleRed | 2021-12-03T03:55:45+00:00
It does make the "Paying an anonymous user" story flow identical to the "Online shopping" flow. Which is nice.

## LocalMonero | 2021-12-03T04:18:18+00:00
@fluffypony if you can't secure your onion server you won't be able to secure your node/wallet server either.

## fluffypony | 2021-12-03T07:38:13+00:00
> It does make the "Paying an anonymous user" story flow identical to the "Online shopping" flow. Which is nice.

@OrvilleRed there's no UX improvement in showing a .onion over a pubkey. In any event, you could still have the records on a .onion, just without DNSSEC (which would have to be supported anyway, as not every TLD supports DNSSEC).



> @fluffypony if you can't secure your onion server you won't be able to secure your node/wallet server either.

@LocalMonero not true. You can secure your wallet with a Ledger whilst still having an insecure server. They are VERY, VERY different targets.

## tevador | 2021-12-03T08:39:26+00:00
@LocalMonero DNS has its flaws, but if you think about it, there are no better alternatives.

In case the domain is seized, the DNS record spoofed or censored, the worst that can happen is that the automatic check fails for **first time users** and it falls back to the manual check. There is no risk of losing funds unless the secondary communication channel used to deliver the payment request is also compromised.

Using an onion address is just replacing one meaningless long string with another. If you are able to securely deliver an onion address to the payer, then there is no need to do anything else because an **onion address is an encoded public key** and can be used directly as the authentication key (interestingly, this works because Monero and Tor use the same elliptic curve). I agree that this could be an alternative in cases the parties are already interacting via Tor, but it cannot replace the DNS verification completely.




## regret-17 | 2021-12-03T15:37:08+00:00
I think tevador's suggestion would greatly enhance the end-user experience.

> A bare payment request can also be passed around as a string and would not be significantly longer than a Seraphis-Janus address (~1 scalar longer).

I feel like this should be the way to go, though. You receive a string similar to the current address scheme, and it "collapses" into a shorter string that is easier to verify manually. 

Even better if you could just pass the shorter string around and have the wallet figure out what the original was, though I'm not sure that's possible.

## LocalMonero | 2021-12-03T17:22:38+00:00
> @LocalMonero not true. You can secure your wallet with a Ledger whilst still having an insecure server.

@fluffypony We were talking in the context of an online service, clearly you need to run a node/wallet on a server. Hence, the threat model is nearly identical.

> @LocalMonero DNS has its flaws, but if you think about it, there are no better alternatives.

 @tevador No DNS entanglement into the Monero protocol is a preferable alternative to DNS entanglement. if most services switch to DNS-tied payment requests then that would open up a significant vector of attack. Understand the long-term implications of your proposal, especially in the context of aggressive resistance from (evil) state actors to Monero's global adoption.

Either come up with an automatic verification mechanism that doesn't have these attack vectors or don't include it at all and keep only the manual verification.


## fluffypony | 2021-12-03T17:27:31+00:00
> We were talking in the context of an online service, clearly you need to run a node/wallet on a server. Hence, the threat model is nearly identical.

@LocalMonero Huh? No you don't - an online store only needs to be able to verify receipt of the payment, so it can run a watch-only wallet.

> Either come up with an automatic verification mechanism that doesn't have these attack vectors or don't include it at all and keep only the manual verification.

Why do you need in-band verification for most contexts? Sounds like a system where people will get suckered into trusting, and then it'll be abused. Plus you have the out-of-band verification example under tevador's "Paying a Friend" example.

## LocalMonero | 2021-12-03T17:31:28+00:00
@fluffypony *some* can run a watch-only wallet. Others will need a hot wallet. Securing an onion server is a personal responsibility concern, DNS seizing is not.

The "paying a friend" example is what I meant by manual verification.

## tevador | 2021-12-03T21:09:13+00:00
@LocalMonero 
> No DNS entanglement into the Monero protocol

This is not an entanglement, but an optional wallet feature. The built-in Monero wallet already uses DNS, but there is a [command line option to disable it](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L308).

I don't see the harm in providing this function to people who want to use it. People who don't trust DNS will disable it and fall back to the manual verification.

I don't want to get dragged into a lengthy discussion about a minor feature of my proposal. If you don't want Monero to use DNS, I think you should open a separate issue.



## LocalMonero | 2021-12-03T22:47:37+00:00
@tevador that's fine. Green checkmarks breaking if/when a DNS poisoning/hijacking/seizing happens should be sufficient.

## LocalMonero | 2021-12-04T18:44:05+00:00
@tevador do you think one could combine DNS TXT and Onion for a more robust approach? Say the wallet checks if the DNS TXT key matches the onion service key, and if not then a security prompt prevents the sender from moving on with the transaction, like with HSTS in browsers.

And perhaps there should be two levels of checkmarks to encourage service operators to implement the DNS+Onion strategy. If a service only uses DNS TXT then it's a single checkmark (or a grey checkmark) and if verification happens with DNS+Onion then it's two green checkmarks (or a single green checkmark). This is analogous to the grey padlock HTTPS vs green padlock HTTPS.

## fluffypony | 2021-12-04T19:03:11+00:00
@LocalMonero it's not analogous at all. Using DNS validates that the payment is going to that domain, whether it's a .com (see:"Online shopping" in Tevador's example) or a .onion (see: "Paying an anonymous user" in Tevador's example). Not using DNS means that it's effectively like paying a Monero address. There is no possible validation that can happen, since you have been given the address out-of-band and not on a website, so there is no link to that site. Encouraging some sort of link (eg. embedding the URL of the site in the URI) is a TERRIBLE idea, as it is trivial to phish "you are about to make a payment to localmonero.org" by things like Unicode zero-width joiners, similar ASCII characters, etc.

## LocalMonero | 2021-12-04T19:07:13+00:00
@fluffypony what I meant was combining `2. Lookup the key in a DNS TXT record` + `3. Decode the key from the onion address (if interacting via an onion service)` for more robust verification.

## tevador | 2021-12-04T21:18:56+00:00
@LocalMonero They cannot be combined. If you are on a clearnet website, there is no onion address to verify against. Providing the onion address in-band doesn't improve security and if there is an out-of-band channel, you can pass the verification code directly and avoid the DNS check in the first place.

## tevador | 2021-12-05T22:25:35+00:00
As @fluffypony pointed out, the domain name should not be loaded directly from the payment request for security reasons. The request would only contain the public keys, an optional amount, optional description and the signature. The ✔ symbol would be reserved for cases when the recipient is already trusted by the sender (i.e. their key is present in the local address book). The displayed name of the recipient would be taken from the address book.

In case the recipient's key is not in the address book, the user would be prompted to *type in* a domain name, onion address or the 25-character verification code. The DNS check would use the domain name provided by the user. For the manual verification, users would be encouraged to obtain the verification code through a secondary communication channel, if possible.

The user would be allowed to skip the verification step, but then the recipient would be displayed as "unverified"❌.


## tevador | 2021-12-14T23:18:01+00:00
I realized that there is not much practical difference between Janus B and Janus E, so the additional key pair just for view tags is pointless. However, by redefining the private key functions a bit, another scheme can be created with just 3 public keys needed for sending and Tier 1 lower than Janus B (but still useful).

I have integrated it with my proposal for authenticated addresses and made it backwards compatible with the existing division into accounts and subaddresses. For merchant wallets, it supports 5 access tiers.

Available as a gist [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024) (work in progress!).

## SamsungGalaxyPlayer | 2021-12-16T18:34:59+00:00
Seems like this conversation got a little derailed into specific pros/cons with some of the implementations.

From my perspective, @fluffypony's point that people want ***both*** requests ***and*** strings is the most important. So long as we aren't breaking the string option, I don't see an issue with supporting another route at least in theory. So long as the option is remotely sensible, people will make their own choices to build on that method or not.

## elibroftw | 2022-01-05T01:20:06+00:00
Plain C or Janus A/D are good by me because view wallet won't require additional work to view spends. 

Receiving Monero should be easy and shouldn't require gotchas like "you need to specify a memo" especially if it's uncertain whether wallet's will create default and possibly random memos for each address generated.

So go with Plain C if the official wallet, cake wallet, and monerju will implement default memos (should be a setting on by default). I'm just one person saying this so I doubt default memos would be a feature actually included.

So then it's subjectively better to go with Janus A/D over Plain C.

Pick Janus A if it's important to have a wallet that can view received payments but not spends.
Pick Janus D if it's not that import or a feature desired.

Considering Janus A is similar to the current model, Janus A should be the favoured schema over Janus D.

As for this anti-address sentiment, there are issues with the official wallet GUI that prevent me from sending monero by simply clicking a monero: link. This is kind of irrelevant so I won't elaborate.

## UkoeHB | 2022-06-05T14:00:47+00:00
A misleading claim about Janus B ([Jamtis](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)) has been going around.

## Claim

If a malicious third party obtains a user's seraphis view-balance key, then they will have greater insight into that user's transaction history than if they had a cryptonote view key.

## Technically misleading

Jamtis view-balance keys are only superficially more powerful than cryptonote view keys _with any existing or proposed protocol implementation_ (see caveat). A cryptonote view key can identify the full balance for most users (with 95%+ accuracy) because there is a powerful heuristic to identify spent funds.

Whenever you make a transaction, each of your tx inputs will have at least one ring member from your storage of owned funds. Moreover, at least one of the tx outputs will be owned by you (the change output). Most of the txs with outputs sent to you by other people won't satisfy both of those conditions. Therefore, the tx inputs that match with your owned output storage in those kinds of txs were very likely spent by you.

**Caveat**: This heuristic would no longer work if membership proofs had extremely large reference sets (e.g. ring sizes). This means that an upgrade from small to massive reference sets would have a different privacy impact when comparing jamtis/cryptonote view-only wallets. This DOES NOT mean the privacy impact would be in any way a regression compared to our current situation.

## Advantages of Jamtis

1. Jamtis full balance recovery is 100% reliable, which makes it useful _for users_ (the current heuristic isn't reliable enough for a wallet to use it, because the edge cases of unidentified funds would plague the wallet's reputation and support help line). It's primarily a user experience improvement, without materially changing the privacy profile of view-only wallets.
2. It's also a user security improvement, because if view-only wallets are used relatively more, then full-powered wallets will be exposed to theft less often. The importance of this can't be understated. Full-balance recovery in a view-only wallet would make spend-only wallets (e.g. hardware wallets and multisig) _much_ easier to implement and _much_ easier for users to handle.
3. Jamtis was specifically designed to minimize the privacy profile of using a third-party scanning service. Empirically speaking, third-party scanning services are by far the easiest way to leak large amounts of users' transaction activities _today_. In Jamtis, third-party scanners would obtain a user's Jamtis find-received key, which is designed so third-party scanners can provide the expected user experience (~instantaneous and cheap balance recovery), while obtaining far less information about the user's tx history than you get with a cryptonote view key (or Jamtis view-balance key). The find-received key will flag 1/256 of outputs as 'potentially owned' by you. You can fully (and very efficiently) scan those outputs to see if your wallet truly owns any of them (and see the amounts inside). The find-received key will flag 'non-self-send' outputs (e.g. non-change), and can reveal the public spend keys of the owning addresses (for outputs you own). If the owning address of an output is known to the scanner for some reason, then the scanner will know that output is owned by you (but not the amount). For unknown addresses, they won't know (unless they learn them in the future, or acquire your Jamtis generate-address key which can identify all of your addresses). The find-received key will flag 'self-send' outputs (e.g. change), but can NOT reveal the public spend keys of the owning addresses (this breaks, or at least greatly weakens, the heuristic discussed above).


## hbs | 2022-11-27T10:38:19+00:00
In order to make things maybe a little clearer for every one (if I judge by some of the drama in Reddit about Seraphis annihilating all of Monero's privacy), maybe a table with the information made accessible to each of the various types of keys would be good.

The table could list things like received outputs, received amounts, spent outputs, spent amounts, sending address, recipient address, etc with status such as Yes, No, Optional, N/A.


## hbs | 2022-11-27T10:47:26+00:00
As the new address schemes are presented, it seems that the notions of "account" and "subaddresses" will be gone altogether.

The current Wallet RPC interface has many methods which allow to act only on a specific account (via the specification of an account_index), and this possibility is used extensively to segregate funds within a single wallet. Given an instance of the rpc wallet can only open a single wallet, this makes it a useful way to manage funds for various users. I don't have the details of how various exchanges handle deposit addresses but I am pretty sure this is how they do it for example. And I have other use cases in mind too where funds can be sent to multiple sub-addresses of a single account, with several accounts being managed to segregate users all within a single wallet.

How should one go with reproducing something similar with Seraphis/Jamtis? Should the RPC interface be modified to allow the specification of a range of subaddresses instead of an account, or maybe a list of ranges?

## tevador | 2022-11-27T10:56:43+00:00
The functionality of accounts will be preserved. There are currently 4 options [being discussed](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4379590#gistcomment-4379590) how to implement the feature.

# Action History
- Created by: UkoeHB | 2021-11-12T16:47:21+00:00
