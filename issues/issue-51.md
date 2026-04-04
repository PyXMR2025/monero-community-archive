---
title: Bitmessage-Style Messaging for Monero Addresses
source_url: https://github.com/monero-project/research-lab/issues/51
author: RandomRun
assignees: []
labels: []
created_at: '2019-03-12T05:09:15+00:00'
updated_at: '2019-04-16T07:50:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The Bitmessage protocol is based on the Bitcoin messaging layer protocol in which every node stores
all the messages in the network, thus behaving as a collective inbox. Proof of work on each message is used to deter spam abuse. Messages are kept by nodes for a determined period of time depending on the PoW applied to each message. Bitmessage is metadata free since no information about sender or receiver is included, and the message is just a ciphertext that each user tries to decrypt with their own keys. Bitmessage also uses Dandelion for broadcasting its messages to protect user's IP addresses.

Some Monero applications already make use of Bitmessage messaging system. For example:
 
(i) broadcasting Monero transactions to break link to originating IP address (Noether’s Gate);
(ii) multisig participants use Bitmessage to coordinate wallet creation and spending from it  (MMS);
(iii) recently a version of Monero coinjoin has come under consideration. Participants will need to colaborate by messaging each other to coordinate the signing of different rings of a single transaction and generating corresponding bulletproofs required. This will likely use the MMS as well.

Bitmessage, however, is based on Bitcoin's cryptography and, to my knowledge, does not currently support Ed25519 cryptographic primitives. Also, Bitmessage nodes have to try to decrypt every single message to check whether they are the intended recipient, so they suffer from the same problem Monero had before the adoption of subaddresses.

Considering that these applications that Monero already have for Bitmessage-style messaging, and that the problem of scanning for multiple keys has already been solved in Monero, it would perhaps be a natural step to enable direct messaging between Monero addresses as viewed as Bitmessage-like addresses.  

If that is achieved, Monero users may seamlessly and directly message other users they are transacting with, and conversely users that are chatting to each other may seamlessly send tips to each other. This could make the claim that cryptocurrencies make payments as easy as sending an email a reality for users of the system.

Here is the scheme I was thinking about. Please let me know what you think. 

Let the user pick random `a, b` to form a family of subaddresses in the usual way. Let `(C, D)` be one such subaddress. For Monero uses, `C` is the view key, and `D` the spend key, as normal. 

For messaging purposes, let `E = e*G := C+D = (c+d)*G` be the encryption key, and `V = v*G := D = d*G` be the verifying key.

For user `(C' ,D') = (c'*G, d'*G)`, with encrypting and verifying keys `(E',V') = (e'*G, v'*G) := ((c'+d')*G, d'*G)` to send a message `msg` to `(C, D)`, he proceeds as follows:

1. Pick a random `r`, and compute `P := H(r*C)*G + D`;
2. Compute the ciphertext `ct := Enc(msg, E)`;
3. Compute the signature `sig := Sign(ct, v')`;
4. Find suitable `nonce` such that the hash value `H(ct, sig, (P,R), nonce)` is low enough;
5. Broadcast `(ct, sig, (P,R), nonce)`.

User `(C, D)` scans the message pool and checks, for each message, whether `P - H(c*R)*G` belongs to his hash table. If so, he proceeds as follows: (Here I am assuming the sender's subaddress `(C', D')` is included in the message, since it should be hidden.)

1. Decrypt the message contents by computing `msg := Dec(ct, e)`;
2. Parse `(C',D')` from `msg`;
3. Verify that it is properly signed by computing `Verify(sig, V')`.

When replying back to `(C',D')`, he repeats the process above, encrypting his reply with `E'` and signing with his signing key `v`.

Notice that the pair `(P,R)` in this context works only as an identifying tag that saves on scanning time for multiple keys. The choice of not encrypting with `P` is deliberate since, I believe (according to my extremely superficial knowledge of quantum computers), that not providing the encryption key along with the message might confer some level of quantum resistance, in the case that the keys `(C, D)` and `(C',D')` are assumed to have been exchanged securely; e.g. exchanged in person.

[Edit : The naive scheme I suggested at first (i.e. using the view key alone as the encryption key) had the severe drawback that if a wallet service, or any other entity, knows the user's private view key, then they would be able to read his messages. To avoid that, both the encryption and signing keys should depend on the spend key in some secure way. (At this time, I am suggesting the encryption key to be `C+D`, but clearly the goal should be to find the best way to view Monero addresses as Bitmessage addresses, and vice-versa.) Conveniently, a web wallet provider can still detect and keep the messages for the intended user. When the user logs in, he uses his private spend key to decrypt (with `c+d`) and sign new messages (with `d`). The wallet provider could enable client side in browser mining for the computation of the required PoW.]

Assuming that this idea or some variation of it is sound and secure, we could contact the Bitmessage developers to see if they would like to implement this as another address type in Bitmessage itself, which could foster Monero adoption among Bitmessage users; or perhaps or fork Bitmessage and bring this modified version under MMS development, which would allow for further tailoring it to Monero's needs.




# Discussion History
## b-g-goodell | 2019-03-16T20:30:17+00:00
Big red flag: in encrypt-then-authenticate, you must also authenticate-then-decrypt. You don't want to decrypt a message before authenticating the ciphertext.

I think there could be a simple fix for that, though...

## knaccc | 2019-03-25T20:41:29+00:00
I like the idea.

I assume the simple fix is to just ensure that authenticated encryption such as AESGCM is used. Or ChaCha20-Poly1305 encrypt-then-mac.

I think you could also achieve this without Bitmessage's help by simply having a Bitmessage channel just for messages encrypted with your scheme, where that Bitmessage channel key is widely known.

## RandomRun | 2019-03-31T00:49:05+00:00
Okay. I am learning that there is a lot that I don't know about this subject, so here are just some lose thoughts as I read more about this stuff.

I think I am resisting the idea of doing encrypt-then-authenticate just because I am having trouble seeing how this could remain metadata-free, which IMO is the main selling point of something like Bitmessage. If I am missing how this could be done without revealing to the network who is signing the message, please let me know how that would work.

@b-g-goodell I have read the paper you linked https://link.springer.com/chapter/10.1007/3-540-44448-3_41 
It seems to cover only the case of symmetric encryption, and it declares that a composition scheme is insecure "if it is secure for some instantiations but not others". This seems to leave the door open to specific instantiations of authenticate-then-encrypt that may be secure (I need to read the full paper that contains the proofs to see what the issues are). In fact, I have come across this video lesson by Dan Boneh where he mentions at 3:30 that authenticate-then-encrypt is secure if it is used with Counter Mode and CBC encryption. I don't know if that is applicable to what we are discussing yet, though. https://www.youtube.com/watch?v=40m3gcdGDu0

@knaccc Same issue as above: using ChaCha20-Poly1305 to encrypt-then-mac sounds like a fine idea, but how is the final format of the package that is broadcast going to look like, and will it hide the sender?
I am also not clear about the implications of using a common well known channel to do that. I mean, would this messages stand out, or be more likely to be dropped or censored? I have seen that there are concerns about BM channels IP linking users, possibly because of Dandelion not working so well if the contents can be decrypted by any node (although in this case the content would be just another encrypted message, so I don't know if that makes any difference).

@b-g-goodell, @moneromooo-monero, @knaccc:
About the concern of decrypting some malicious code from an untrusted sender, how bad is this issue? I mean, once decrypted, would the user have to take some action, or are there instances where the code would just run? (Apologies in advance for the basic, and perhaps malformed, question.) If it requires user action, the system could alert the user that the message comes from an untrusted sender before even displaying the message, so that the user would be prepared and act accordingly.
On the other hand, if just having the code written in one's computer would be enough for it to run and cause damage, then couldn't a malicious actor just include the malicious code as a bogus ciphertext, so that by the time the verification fails it would be already too late?  

## knaccc | 2019-03-31T13:09:32+00:00
@RandomRun Great point about censorship if a well-known channel is used. 

The problem in general if you don't authenticate before decryption is the [cryptographic doom principle](https://moxie.org/blog/the-cryptographic-doom-principle/)

There are two types of authentication though. There is the authentication of ciphertext that has been encrypted with a symmetric key, and then there is public key signature verification to check that the message has come from the sender that you're expecting.

Since it looks like it would be desirable to receive a message either from an anonymous sender or from a previously unknown sender that wishes to declare their identity to you and not to any outside observers, there will need to be an outer layer of encryption and authentication followed by an inner layer which will use public key authentication if necessary.

You've written `ct := Enc(msg, E)` and `msg := Dec(ct, e)`, and that would normally be done using an ECIES scheme. I'm not sure if that was what you were thinking when you wrote it, but if it is done with ECIES then you have a shared secret that you can use for authentication prior to decryption, at the outer layer.

Here is the outer layer part using ECIES:

Encryption:

1. Pick a random scalar `r`, and compute `P := Hs(r*C)*G + D` and a message public key `R = r*D`.
2. The shared secret between the sender and receiver `s = keccak(r*C)` (keccak instead of Hs() for uniformly distributed 256 bits of entropy for use as a symmetric encryption key)
3. Pick a unique IV and compute the authenticated ciphertext `act = AEAD_ENC(IV, msg, s, AD)` where the associated data `AD` includes `P, R`. 
4. Broadcast `(IV, act, P, R, nonce)`

Decryption:

1. Proceed if `P - Hs(a*R)*G` belongs to the subaddress lookup table.
2. Symmetric key `s = keccak(a*R)`
3. `msg = AEAD_DEC(IV, act, s, AD)`, which will fail if the authentication tag is incorrect.

Note: The [AEAD](https://en.wikipedia.org/wiki/Authenticated_encryption) scheme could be e.g. AESGCM.


## RandomRun | 2019-04-02T03:59:03+00:00
>Since it looks like it would be desirable to receive a message either from an anonymous sender or from a previously unknown sender that wishes to declare their identity to you and not to any outside observers, there will need to be an outer layer of encryption and authentication followed by an inner layer which will use public key authentication if necessary.

@knaccc Maybe I am missing the point of the authentication. 
What key is authenticating `act`, `s`?
If Alice `(A,B)` wants to send a message to Bob `(C,D)` and takes the steps you mentioned, then shouldn't authentication mean that Bob knows that the message is coming from Alice, and in which case `(A,B)` should be taken as input at some point? You hinted at that but it is not explicit from what you wrote in more detail. 
Where is Alice identifying herself, are her keys and signature contained in `msg`? 


## knaccc | 2019-04-02T11:44:16+00:00
@RandomRun The AEAD scheme (e.g. AESGCM) would use an authentication key derived from the encryption key `s`. See https://crypto.stackexchange.com/questions/44526/why-does-aes-gcm-not-require-an-auth-key-but-encrypt-then-mac-does

It's important that the integrity of the ciphertext is verified, and AESGCM will do that for you.

> shouldn't authentication mean that Bob knows that the message is coming from Alice, and in which case (A,B) should be taken as input at some point?

There is the symmetric authentication in the outer layer, which I've just mentioned.

Then there is the asymmetric (public key) authentication after that outer layer is unwrapped, which should be checked prior to then doing anything with the message you've unwrapped. You're right that I perhaps confusingly mentioned the outer layer but not explicitly the inner layer.

So to be explicit, perhaps the message you'd encrypt with the outer layer would be:

`A || B || innermessage || schnorr signature`

And then you'd check the signature prior to doing anything with the innermessage.

Alternatively, maybe the sender wants to be anonymous, perhaps because they're simply informing another node of a transaction and don't want to identify themselves. In that case, there would just be an `innermessage` with no `A`, `B` or `signature`. But the outer layer would still authenticate the integrity of the ciphertext, which is the critical part.

## RandomRun | 2019-04-05T01:01:35+00:00
@knaccc That makes sense, thanks. 

However, I think that `s` should be something other than `keccak(r*C)` to avoid the concern with third parties that may know the user's viewkey. 

So the outer layer is encrypted and authenticated with `s`, to guarantee that it was not tampered with when in traffic, and then in the inner layer, either have just the message; or, if the sender wants to identify herself, we could even do authenticated encryption again with encrypt-then-mac. 

In the case of the sender wanting to reveal her address, the inner message could be authenticated as well. I was thinking that if `enc := Enc(actual_message, s)`, and `h := hash(enc)`, then the `innermessage` could be:

`A || B || h || Sign(h, B) || enc`.

So that at least the receiver can see that Alice's key has been used to sign something before proceeding to decrypt the `actual_message`.  


## knaccc | 2019-04-05T19:23:27+00:00
@RandomRun I think the following would work - it would mean that:

1. We still get the subaddress scheme scalability advantage of being able to detect all incoming messages with just a single private view key scalar multiplication

2. Knowledge of the private view key would be enough to detect a message is destined for the user, but is not enough to decrypt it

3. It would not be necessary for a second symmetric encryption operation for the inner message

To do this,  the receiver could look at `R==rD` and determine `rG = d^-1 * R`. The sender would calculate `s = keccak(rE)` and the receiver would calculate `s =  keccak(e*rG)` (or more directly, `s = keccak(d^-1 * eR)`. So effectively there is a DH exchange between the public keys `rG` and `E`. This means the receiver needs to know `e` to authenticate and decrypt, which requires knowledge of `d` and in turn knowledge of the private spend key `b`.

## RandomRun | 2019-04-07T13:34:32+00:00
@knaccc Using `E = C+D` for subaddresses may not prevent someone with access to the private view key from reading the message, since given `R = r*D`, they can compute `a*R = a*(r*D) = r*C`, and adding the two and taking the hash they could deduce `s = keccak(R + a*R) = keccak(r*D + r*C) = keccak(r*E)`.

For subaddresses, perhaps simply using `s = keccak(r*G)` could work as their shared secret, since knowledge of `d` is already required to recover `r*G` from `R = r*D`. I am not sure if it matters that `d` is not involved in the formula for `s`, but only the secure transmission of `r*G` from the sender to the owner of the secret spend key (without letting the someone with access to the secret view key read the message).

W.r.t. encrypting a second time in the inner message, I was thinking that anyone, say Carol, could send a message to Bob, since the outer encryption does not take any of the sender's prior information into account, then claim to be Alice in the inner message. Of course, at this point verification should fail, and Bob would be alerted about the fact that the message is actually not from Alice. What I am still fuzzy about is whether having the final message encrypted would confer any additional safety to Bob compared to having it already in the clear at that point. 

## knaccc | 2019-04-07T19:37:26+00:00
@RandomRun Excellent point about `R + a*R` being recoverable since `rD` is posted.

> For subaddresses, perhaps simply using s = keccak(r*G) could work as their shared secret

Ooh, yes very nice, you've totally nailed it!

> I was thinking that anyone, say Carol, could send a message to Bob, since the outer encryption does not take any of the sender's prior information into account

> then claim to be Alice in the inner message

I think that is a necessary side-effect of allowing the subaddress-style high-performance scanning for incoming messages. I don't think it should be an issue as long as the inner message has an identification and signature to check the real sender. You can't claim to be anyone other than the specified sender if there is a signature there.

> What I am still fuzzy about is whether having the final message encrypted would confer any additional safety to Bob compared to having it already in the clear at that point

I can't see a reason to have it double-encrypted, because as far as I can see, all that matters is that whoever encrypts it does so in a manner that prevents anyone other than the person in possession of the private spend and view keys from decrypting it.

## RandomRun | 2019-04-09T09:27:46+00:00
Great :) It looks like this works well for encrypting to subaddresses, indeed!

I guess for regular addresses, since `R = r*G`, the sender could set `s := keccak(r*B)`, and the receiver could recover it by computing `keccak(b*R)`.

This way, we are using the public spend key for encryption (or at least to communicate the symmetric encryption key). There is still the matter of signing, though, if the sender chooses to do so.

We now have partially defined maps `(C,D) <--> (E,V)` setting `E := D` for subaddresses, and `(A,B) <--> (E,V)` setting `E := B` for regular addresses. It is not clear yet to me how to best define `V` in those cases.

Setting `V := D` and `V := B` (for subaddresses and regular addresses, respectively), is considered bad practice in many cryptosystems (but we can get away with that here?). And in any case, having just one key would not allow messaging users to send money to each other in the usual way, which is one of the main initial motivations for this issue.

On the other hand, setting `V := C` and `V := A` might allow whoever knows the private view key to impersonate the user, depending on how the signing is done.

So I am wondering how best to define the verification key `V` in each of those cases, such that messaging users can still send money to each other, and at the same time, someone with access to the secret view key cannot impersonate (or decrypt those messages).

The natural choice seems to be to use `V = C+D` and `V = A+B`, but I need to think more about possible problems. 


## knaccc | 2019-04-09T21:36:29+00:00
Perhaps you can flesh out the use cases more so we can understand the workflows. For example, I didn't understand why it would not be an advantage for an auditor to be able to view messages sent to an address holder.

## RandomRun | 2019-04-14T22:18:22+00:00
I am having trouble answering your question because the answer is a bit open ended to me still. So here are some thoughts again.

**About the auditor** (in relating to transactions):

I don't know the motivations of who created stealth addresses, but it seems to me that it is first and foremost a tool to generate unlinkable one-time addresses for which the receiver can recover the private key. I could be wrong, but I don't think that the auditor idea was a design goal, and is rather an after thought given the observation that one can find outputs belonging to an user, while not having enough information to spend them.

Indeed, a proper audit would probably not be satisfied with just being able to see incoming outputs, but would also require to see the user's spend patterns. In this situation, the user would probably provide the auditor with all the key images of those outputs.

If that is the case already, IMHO it would be preferable to encrypt the amounts and other information in the transaction using `Hs(rB)` instead of `Hs(rA)`, as is currently done with regular addresses; and with `Hs(rG)` instead of `Hs(rD)`, for subaddresses.

**Going back to the messaging system:**

For the same reason, I don't think it is a problem to have the messages be auditable requiring the use of the spend key, and specific user action.

My concern (which may not be a reasonable one) is that a lot of users give away their private view keys to web wallets not realizing the privacy implications. If, on top of viewing transaction details, the holder of the private viewkeys is able to impersonate the user, and that is something they hadn't considered at the time of making the private viewkey available to a third party, that could be a problem.

One approach is (i) to say that it is up to the user to not reveal their private viewkey, and use `A` or `C` as the signing key in the messaging system anyway. Or (ii) we could set the signing key to be `A+B` or `C+D`, thus requiring the user's secret information and proving to the receiver that they indeed control both keys of their purported address.

Like I mentioned, I am a bit unclear of possible security implications of each choice, but I tend to favor the latter right now, since I believe that proving the user's identity should be on the same level of access as having the ability to spend their money and read messages addressed to them; i.e. not readily available to an entity that is just scanning for messages or outputs addressed to them.

**Fleshing out the use case for regular addresses:** (This is mostly rewriting what we discussed, so I am not sure if this answers your question. Please let me know if I am missing something.)

**User `(C,D)` sending a signed message `m` to `(A,B)`:**

1. Pick random `r` and compute `P := Hs(rA)G + B`.
2. Compute `h := hash(m)`
3. Compute `sig := Schnorr_sign(h, C+D)`.
4. Compute `s := keccak(rB)`, and use `s` as the symmetric key for encrypting the message `m`. That is, use `s` with Chacha20-poly1305 (or whatever authenticated encryption method is deemed most appropriate) to encrypt-then-authenticate `C||D||sig||m`, thus obtaining `ct := Enc(IV, C||D||sig||m, s, (P,R))`.
5. Find `nonce` such that `hash(IV, ct, P, R, nonce)` is low enough.
6. Broadcast `(IV, ct, P, R, nonce)`.

**User `(A,B)` receives `(IV, ct, P, R)` and verifies the signature:**

1. Check that `P - Hs(aR)G` belongs to the hash table.
2. Recovers `s = keccak(bR)`.
3. Decrypts the information `C||D||sig||m` by performing `Dec(IV, ct, s)`.
4. Parses sender keys, message and signature. Compute `h = hash(m)` and that `Verify(sig, h, C+D) = true`.

For subaddresses the steps are the same, with the changes already noted, namely: `R = rB` instead of `rG`. Also, `s := keccak(rG)`, and receiver recovers that by doing `s = keccak(b^{-1}R)`.

## RandomRun | 2019-04-14T22:33:05+00:00
Here is an important use case that requires messages signed by the sender: 

**Decentralized, censorship resistant, metadata free whitelisted mailinglists.**

As I have discussed with @rbrunner7 and @PeterSurda, currently mailing lists on Bitmessage are riddled with spam, but I believe we could fix that by client side filtering. This could be an important tool to have in case, for instance, Reddit bans /r/monero and users prefer to use a more private messaging system than IRC.

The way this would work is set up an agreed encryption key, for instance set `f := keccac("monero_discussion")` and `F := fG`. Set the address `(G,F)` and either give it to the intended participants, or make it public already.  

So if `(C,D)` wants to send a message to the mailing list, they would go through the above steps using `(A,B) := (G,F)`, and signing the message with `C+D`. (There are privacy concerns with sending a message to an address that any node can decrypt, but I think this can be fixed by encapsulating the message into  private message to a random node in the network that would in turn rebroadcast the original message once it decrypts it.)

If we can all read messages sent to `(G,F)`, then the problem becomes what to do with all the unwanted spam messages. The solution, I think, is to whitelist all addresses we care to hear from in the client level, and ignore all the rest.

For instance, you and I could start the above mailinglist and only whitelist each other's addresses, so that if anyone else sends to it, our clients would not display those messages right away. We could set up other actions that it should take.

How do new participants join in?

There are a number of policies that we can take on the client side if we want to see messages from new users. For instance, I could set up that a messages from new users will only appear in my client if they produce a very expensive proof of work. Or that my client could let me know that there are so many messages from non-whitelisted sources that I may want to see etc. 

Importantly, if for whatever reason I happen to reply to a new user message, then, since you have whitelisted my address, you would see that my message is quoting the new user. Presumably you care about my opinions if you are whitelisting me, so perhaps, since I bothered to reply to this new user, you might want to whitelist them as well. In that case your client should detect that and ask you "Hey, RandomRun is replying to this new user. Would you like to whitelist them as well so that you can follow their discussion?". And if you think it is worth while, you can then whitelist this new user, and your client can fetch and display all previous messages from them that may still be in the message pool. If they are gone from you message pool your client could ask mine for those messages. Of course, you can also remove any user from your whitelist at any later time.

I believe that setting up whitelisted mailinglists would also reduce the incentive to spamming in the first place. 

Also, if we refer to message ids in our replies in the mailing list, we could get conversation threading, for a Reddit-like experience :)

## PeterSurda | 2019-04-15T09:55:34+00:00
> The problem in general if you don't authenticate before decryption is the [cryptographic doom principle](https://moxie.org/blog/the-cryptographic-doom-principle/)

I looked at the page. It looks like the vulnerability depends on the ability to distinguish between a MAC error and a padding error. While It probably is possible to do this with profiling PyBitmessage locally, I find it difficult to find out how it would work over the net, since Bitmessage is an asynchronous protocol and an object it can't decrypt produces no external feedback, irrespective of the reasons. Only correctly decrypted messages which include an ACK (and some other conditions are fulfilled) produce a feedback in the form of ACK, and with the current version with default settings that's dandelion routed.

Furthermore, even though Bitmessage uses Sign-then-Encrypt, there is still a PoW on top of that, which would have to be calculated for each manipulated object, increasing his costs.

## knaccc | 2019-04-15T16:41:17+00:00
@PeterSurda When you say Bitmessage does "sign-then-encrypt", does "sign" mean a symmetric or asymmetric signature? It's the symmetric signature (e.g. some kind of HMAC using a symmetric authentication key) that is generally considered important to verify prior to decryption.

## PeterSurda | 2019-04-16T07:49:04+00:00
@knaccc I'll try to reply as best as I can, considering I'm not a cryptographer and I didn't design or code Bitmessage's encryption (only bugfixes and compatibility updates). PyBitmessage uses pyelliptic for both signing and encryption. Encryption uses ECIES. There are separate keypairs for signing and encryption.

I'm now looking at the code. It looks like I was partially both correct and wrong (in the positive direction). ECIES, or at least how it's used in PyBitmesage, uses an ephemeral key for encryption, as well as a checksum. Upon decryption, this key is re-constructed using the private key and the data in the object, and then its checksum is verified against one calculated from the ciphertext. Only once this verification succeeds is a decryption of the ciphertext attempted.

So if I understand correctly, the "cryptographic doom principle" wouldn't work. You'd be lucky to get the checksum right, since it's HMAC-SHA-256 (32 bytes). The encrypted objects are protected by a checksum, which has a fixed length (so do the ephemeral pub key and iv). The signature inside the encrypted object is an additional layer, to authenticate the sender.

Good thing that this was designed by someone who knew what they were doing :-)

# Action History
- Created by: RandomRun | 2019-03-12T05:09:15+00:00
