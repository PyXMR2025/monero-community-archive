---
title: P2P Encryption+Authentication Discussion
source_url: https://github.com/monero-project/monero/issues/7078
author: vtnerd
assignees: []
labels: []
created_at: '2020-12-05T00:29:24+00:00'
updated_at: '2023-05-02T20:25:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
My apologies to @moneromooo-monero  for previously pushing back against TLS of p2p links. As outlined below, encryption of p2p connections is funky ...

I've got a massive writeup on thoughts about encryption of the p2p links, including quasi-specifications, but I will try to keep thing short so that I get some feedback first.

Adding encryption and authentication to p2p increases the attack surface, and increases the value of a zero-day in the Monero p2p code. A zero-day on a p2p network allows an attacker to move through multiple machines with a difficult to audit trail. Eclipse attacks cannot be prevented either - an attacker can hijack TCP sessions, and the local node doesn't know whether a MitM is occurring or whether the remote node has changed pubkeys (dynamic IP or settings change). An attacker can also drop all packets until an IP is dropped from the peerlist (assume peer is permanently offline). Authentication also provides a mechanism to track a specific node over time via the pubkey. There is also more overhead for initiating an encrypted link, so auditing the incoming connections path is needed too.

However, encryption stops passive surveillance of p2p communications. An ISP cannot just sit idle and monitor transaction flow to determine source. The TCP stream must be hijacked to inject different pubkeys into the channel. Once the connection is established, nothing can be observed unless the attacker drops packets to force a new connection. The primary benefit of authentication is that zero round-trip encryption can be done with the noise protocol (the initial handshake message can be encrypted without waiting for server response).

At a high-level the options are:
 * Change nothing
 * Use TLS 1.3 with/without authentication
 * Use Noise Protocol framework with/without authentication

TLS 1.3 requires 1 round-trip to initiate connection, whereas the Noise protocol can be done in 0 round-trips in certain modes. TLS 1.3 requires ~21 bytes overhead per 2^14 bytes in a p2p message, whereas Noise protocol can be done in 16 bytes overhead for p2p messages of any size. The Noise protocol should have a smaller overall attack surface, with the downside that the Monero project has to maintain/test a bit more code to get it working (risk of new code).

My suggestions for Noise Protocol are `Noise_NK` if using authentication, and `Noise_NN` if not doing authentication. The rationale is a big longer, and the focus should be selecting a high-level option above.

# Discussion History
## moneromooo-monero | 2020-12-05T00:58:34+00:00
If we use TLS, can we essentially look like any other encrypted P2P connection (disregarding traffic timing/volums analysis for now) ?

## xiphon | 2020-12-05T09:44:43+00:00
I would definitely go for widespread encryption protocol - TLS 1.3 + ECH (Encrypted Client Hello) (optional, though would be nice to have it at a glance).

I wouldn't choose immature Noise Protocol as an encryption protocol.

## vtnerd | 2020-12-05T17:21:19+00:00
@moneromooo-monero I will respond a little later today with some thoughts on "cloaking" or hiding the connection type. There are some tradeoffs with each. Some quick things to consider (TLS cloaking is more obvious):

The biggest property we can get is making the entire stream indistinguishable from noise (thus the name). This complicates DPI engines because they cannot "key" on pattern matching, it has to be statistical analysis to identify a lack of bias in this data (and therefore probably encrypted). TLS client hello can be identified with minimal processing on any port.

The server/responder can also tell in the first data payload when its _not_ Monero related with Noise, which is indirectly related to TLS cloaking with port 443 (which will obviously be a part of that discussion). In fact, the server/responder pubkey has to be fetched over p2p before initiating connection with `Noise_NK`; the server computes an invalid MAC on first data payload if data was destined to another pubkey.

> I wouldn't choose immature Noise Protocol as an encryption protocol.

I'm not sure if this criticism applies. Wireguard, a VPN included in recent Linux Kernel releases, is based on `Noise_IK` and has been looked at by multiple researchers with [formal verifications](https://www.wireguard.com/formal-verification). There are also other major deployments: WhatsApp (`Noise_XX` and `Noise_IK`), BTC/Lightning (`Noise_XK`), and I2P (`Noise_XK`). There is also one other attempt at doing [formal verification](https://noiseexplorer.com/) of the high level design patterns. However, this paper has probably been peer reviewed less.

The protocol is fairly simple and straight-forward from a security analysis perspective. There are less knobs. The zero-RTT claim above should possibly be disregarded because it implies some slight sketchiness that I was going to propose that noise protocol authors don't recommend because its a general framework instead of specific design. But the server can immediately detect whether the client/initiator has correct pubkey.

The concern is a bug in the less circulated/used (Monero specific) implementation, rather than the protocol design itself.

> But for encryption of all P2P connections, how to do that reliably? If key verification is not handled properly, it will result in fake security. MitM can't be detected so in theory it's not more secure than no encryption BUT people may think it's secure and this can be worse than no security at all IMO.

As stated above, this mode would make MitM more involved, but not impossible. It seems like it would be simple to state publicly "this is for confidentiality with passive monitoring, mitm protection isn't feasible with this design". Also, in this context the p2p connections happen "magically" anyway, the user isn't specifying a known party typically. Which is why mitm is so convoluted.

However, this would provide a secure connection mode to **known** peers. MitM would be prevented because the user would manually specify the pubkey identity. We could even do a more secure variation on trust-on-first-use, where a pubkey is published in a DNSSEC TLSA record (with either TLS or Noise) for when the user specifies a hostname for a node. If the pubkey is not cached locally, it is fetched from DNSSEC in a difficult (but not impossible) to forge method. An out-of-band channel would be even more secure. All of the hard-coded seed nodes would have this property for instance. My apologies for forgetting to mention this in the writeup, authenticated connections to known peers is certainly a big benefit.

## vtnerd | 2020-12-05T20:46:00+00:00
> If we use TLS, can we essentially look like any other encrypted P2P connection (disregarding traffic timing/volums analysis for now) ?

TLS is deployed for HTTPS, OpenVPN, Tor, and probably too many other things to count. Noise protocol is used by I2P, WhatsApp, and BTC/Lightning. WireGuard is over UDP, and is therefore easily separated from Monero p2p.

DPI engines (pattern matching / regex ) can identify TLS client hello messages somewhat easily on any port. Noise protocol is indistinguishable from noise so typical pattern matching won't work. Basically they are identified by a statistical test of the bytes. Its probably slightly more effort to identify these streams because it should require more per-connection tracking. A slight benefit to Noise protocol I think - if only because existing DPI engines are designed around finding distinguishing bytes instead of identifying purely random bytestreams. This edge may not last long if some clever "researchers" investigate the (non-)problem.

Monero has a standard port number, 18080, that is used for p2p traffic. Repeated connections to this destination port are a giveaway of Monero p2p traffic without doing any packet inspection. TLS+destination port 18080 would be an even stronger indicators per-connection and per source-IP. Same applies to Noise protocol to port 18080 based on above paragraph, with the caveat that DPI should be harder because it will typically be reported as "unidentified/18080".

**Scenario: user needs to hide/cloak Monero usage**. TLS has a massive advantage - specify exclusive nodes with certificate to port 443. This port is used by HTTPS (servers) and OpenVPN fallback (office/home), so DPI analysis finding TLS/443 won't immediately appear strange in any context. If incoming connections are _not_ allowed, the exclusive peers (assuming they can be trusted), will not share the ip/port in peerlist requests over p2p either. Monero usage wouldn't be completely hidden, especially since I mentioned this publicly, but fairly reasonable effort has to be done to identify Monero usage. Some external "tip" or "hint" most likely (such as user logging into crypto-exchange from that IP). Or just randomly guess Monero and start doing packet timing analysis.

**Scenario: user wants to hide/cloak Monero usage with "standard" p2p behavior**. TLS/18080 or unidentified/18080 connections are enough to stand out. Slight benefit to noise protocol unless engines "catch-up"; all connections will typically appear as "unidentified", which can be anything. TLS to/from a bunch of arbitrary ports would stand out a bit too.

**"Cloaking" Summary:** Scenario 1 is uncommon but big benefit to TLS. Scenario 2 is more common with a small (and possible no) benefit to Noise. This is not considering security analyis - as an example, the increased likelihood of random "probes" when having a TLS/443 open port where the server cannot reject until after the handshake and the first payload from client arrives.

## vtnerd | 2020-12-05T22:21:41+00:00
> I would definitely go for widespread encryption protocol - TLS 1.3 + ECH (Encrypted Client Hello) (optional, though would be nice to have it at a glance).

I didn't include this in my analysis above. ECH is still marked as a draft, and [OpenSSL](https://github.com/openssl/openssl/issues/7482) has indicated they don't intend to include it until the protocol is finalized. We wouldn't be able to use it in the near-term without using an alternative SSL implementation. If we went with the TLS option, eventually Monero should enable it when available.

The above recommendations for hiding data don't change much because ECH is primarily about hiding information about the client, and not about hiding TLS occurring on the connection. Noise specifically was designed to make it hard to identify, which is likely the reason why I2P in particular switched to this mode despite the pain of switching a working p2p system. I can inspect the header a bit further, but a quick pass shows that it should still be identifiable.

## moneromooo-monero | 2020-12-06T14:07:23+00:00
Any can be used. I've actually got an old --use-random-port patch somewhere IIRC.

## vtnerd | 2020-12-06T23:10:48+00:00
The ability to change your local port is irrelevant if some reasonable percentage of nodes use the default port number. Your node ends up making connections to that port with more frequency, and switching to TLS will generate TLS/18080 reports without requiring specific Monero data tracking. As an example, recently I had 2 out connections to 18080 and 8 unique out ports. This bias towards 18080 will show up in easy to generate reports. You'd need a `--ignore-p2p-default-port-nodes` option to make a difference. Other projects aren't using port 18080 with frequency and definitely not TLS/18080 with any frequency.

Even with that option, its still somewhat uncommon to see non-443 TLS connections to many distinct IPs that frequently. Unfortunately, having completely random port usage is identifiable in the same way that a TCP connection with statistically random data is identifiable - virtually no one else is doing this. Still, it should be more annoying to see a bunch of random TLS ports because false positives (especially with generic processing) are more likely,

Which is why the best technique is probably to aggresively use TLS/443 if the goal was cloaking, with the second best option being TLS/9001 (Tor). In fact, switching to 9001 default is interesting because it probably mimmicks Tor behavior more closely for users that aren't interested in aggressively setting only a couple of known 443 peers. Although, Monero IPs being classified as Tor IPs may not be a huge advantage.

I could research more TLS p2p systems or more TLS systems in general if cloaking is a partial goal. Tor is just any obvious major p2p project that uses TLS.

## moneromooo-monero | 2020-12-06T23:30:48+00:00
I asked out of curiosity really. I don't *want* this now.

## vtnerd | 2020-12-06T23:35:37+00:00
Lol, sorry. This really was an onslaught of response info.

The important take-away is that TLS/443 is the best way to get "lost in the crowd". Everything else is a bit murky and mostly speculative.

## vtnerd | 2020-12-06T23:36:56+00:00
Pinging @TheCharlatan to this thread, who discussed with me in person about encrypted Monero p2p links.

## bill-mcgonigle | 2020-12-30T02:44:55+00:00
I found this issue when thinking about the current ongoing attack and node authentication.  Given reliable key-based authentication, I can imagine a node storing the public key of peers that behave well over time and adding a reputation score to them as they continue to behave.  Given a new network attack like the current one a node operator could relaunch with `--minimum-node-reputation=5` or whatever and then the network would stabilize until a point release could correct the underlying problem.

Sure, an attacker could pre-stage behaving nodes for a while before turning them to evil, but this increases his costs and puts a limit on the damage as those keys could be put on an enhanced version of the current blocklist (or the DNS one which could also suggest a reputation level).  Eventually gossipy nodes might even sign and send out their reputation lists for a new node to learn from, requiring an attacker to own > 50% of nodes to break consensus and create a situation like we have now.  So effectively there would be an auto-whitelist to complement the static blacklist, based on keys.  An auto-blacklist could have minor benefits. Also, a trustworthy node operator could move IP's but keep the same key.

This isn't a proposal but some thoughts about some of the benefits having key-based authentication could enable while getting away from IPs for reputation (it's too bad the Tor users took friendly fire in the current attack).

FWIW I recently moved my infrastructure to WireGuard and the performance and simplicity are substantially better than OpenVPN's 'TLS'-over-UDP system. Compact keys too. But I'd be happier with TLS than no authentication and multi-level signing could offer a potential benefit which I haven't seen in NOISE (fact-check this).  IMO Stability > Information Disclosure > MITM > traffic classification, but all are are valid concerns.

## sedited | 2021-01-18T23:29:26+00:00
> Pinging @TheCharlatan to this thread, who discussed with me in person about encrypted Monero p2p links.

I am not entirely decided on using Noise or TLS but tend towards Noise. I'll try to not just pile on to the arguments @vtnerd and others already presented here. Just for clarification, when talking of TLS1.3 I assume no usage of an existing, but rather a monero-specific public key infrastructure and some pinned set of available cipher suites.

I am not sure if the TLS 'cloaking' argument really applies. Even on the normal TLS port, and with using a TLS handshake, monerod is still broadcasting communication patterns that are typical for it, following its Levin protocol. Much unlike Tor, this is not mostly typical HTTP traffic. The Tor developers seem to have specifically chosen TLS because it actually does mostly overlay web traffic (HTTP) traffic. Tor traffic has also detected in normal TLS traffic before though, see [this paper](https://ntnuopen.ntnu.no/ntnu-xmlui/bitstream/handle/11250/143950/Identifying_TLS_abnormalities_in_Tor_AndersOlausGranerud.pdf?sequence=1) from 2010 (though IIRC some of these particular problems have since been addressed). Their feat was repeated more recently by a another research team [in 2016](https://www.icir.org/johanna/papers/pam16tor.pdf). In their case, they collected their traffic data from university uplinks. Note that both papers name certificate rotation and cipher suite selection as key ingredients to detect Tor-usage. The [tor-spec](https://gitweb.torproject.org/torspec.git/tree/tor-spec.txt#n350) gives a thorough description of cipher suite selection and certificate rotation.

Could you briefly explain why using TLS would really cloak monerod's behavior, even when using the Levin protocol @vtnerd? Might it be that monero more closely follows broadcast patterns of other p2p applications, which with growing popularity use Noise, than typical Tor traffic? 

I'd also like to add that using TLS, even with non-perfect cloaking could still have benefits, for example, if all non-TLS or non-HTTP traffic is blocked.

I like Noise. It's small, a growing number of widely used, popular p2p networks and applications are using it, and its [authentication patterns](http://www.noiseprotocol.org/noise.html#handshake-pattern-basics) make the authentication hell that is TLS certificate pinning a ghost of the past. I have to think again if your named selection of Noise patterns is optimal for Monero's usage though.

Besides the other good reasons already presented for using authenticated encryption for the p2p traffic, it gives clearnet users a bit more anonymity. A man in the middle will no longer be able to observe the contents of a transaction broadcast. To me, this is the final piece in the transaction broadcast puzzle. Especially since the adoption of a default overlay network for monero seems to be shelved, I am strongly in favor of completely encrypting p2p chatter.

## vtnerd | 2021-01-20T18:41:34+00:00
> I am not entirely decided on using Noise or TLS but tend towards Noise. I'll try to not just pile on to the arguments @vtnerd and others already presented here. Just for clarification, when talking of TLS1.3 I assume no usage of an existing, but rather a monero-specific public key infrastructure and some pinned set of available cipher suites.

Yes, my proposal was to pin a specific ciphersuite(s) and require all nodes to support that set. The pubic-key infrastructure was going to be difficult though; preventing a mitm is actually fairly difficult since there is no single "authority" on keys. The main objective will be to force an attacker to be active, whereas currently they can snoop passively.

> Could you briefly explain why using TLS would really cloak monerod's behavior, even when using the Levin protocol @vtnerd? Might it be that monero more closely follows broadcast patterns of other p2p applications, which with growing popularity use Noise, than typical Tor traffic?

My claim was that using TLS/443 might help Monero usage go unnoticed in some situations where basic analysis+reporting is being conducted. Defending against traffic pattern analysis is difficult and possibly permanently out-of-scope for the project. Enough nodes listen on the unique+default TCP port that it will "leak" Monero usage regardless of encryption scheme, unless an (impossible?) effort is made to change port usage behavior.

> I'd also like to add that using TLS, even with non-perfect cloaking could still have benefits, for example, if all non-TLS or non-HTTP traffic is blocked.

Yup. It would be nice if more systems adopted noise protocols, because this would force the filtering techniques to be more permissive.

> Besides the other good reasons already presented for using authenticated encryption for the p2p traffic, it gives clearnet users a bit more anonymity. A man in the middle will no longer be able to observe the contents of a transaction broadcast. To me, this is the final piece in the transaction broadcast puzzle. Especially since the adoption of a default overlay network for monero seems to be shelved, I am strongly in favor of completely encrypting p2p chatter.

Yes, encryption with Dandelion++ helps with privacy immensely. Some users thought Monero p2p traffic was already encrypted, as a result of how the technology was being discussed. In other words, users basically expect the p2p data to be encrypted.


## garlicgambit | 2021-02-13T19:14:53+00:00
Any updates on this issue?  
  
Are there any arguments against (opportunistic) encryption of the P2P layer? More code and more complexity are two important ones.  
  
What would be the deciding factor(s) into picking TLS or Noise or something else?  
  
Which protocol and implementation will likely lead to the lowest amount of serious security vulnerabilities? Serious as in an attacker being able to steal coins and/or significantly degrade the privacy/anonymity of users.  
  
Will encrypted P2P be enabled by default? Could make it opt-in for testing a couple releases and make it the default once it's stable.

## vtnerd | 2021-02-15T16:56:19+00:00
> Are there any arguments against (opportunistic) encryption of the P2P layer? More code and more complexity are two important ones.

Increased latency for block and transaction propagation. Increased CPU usage. Small bit of memory overhead.

It also increases the value of a zero-day - an attacker can move around the p2p network with only packet size/timing behavior being exposed. External packet recording (ISPs, etc.) are blinded. Monero users are only concerned about the increased attack surface and increased value of finding a vulnerability.

> What would be the deciding factor(s) into picking TLS or Noise or something else?

Efficiency, protocol simplification, and control vs implementation mishaps. The noise protocol has been formally verified and there's no downgrade options, so its basically trusting whether we can meet the specification without screwing it up. There are several sharp corners - AES-GCM or Chacha20-Poly1305 for instance are both stream ciphers and very bad things happen with nonce re-use. With TLS there are less sharp corners but a larger code footprint that we really haven't audited.

> Which protocol and implementation will likely lead to the lowest amount of serious security vulnerabilities? Serious as in an attacker being able to steal coins and/or significantly degrade the privacy/anonymity of users.

Its tempting to say OpenSSL, but the protocol and that implementation have been plagued with issues. TLS 1.3 should (hopefully?) be a simplification of the protocol that prevents the protocol level attacks. The OpenSSL implementation probably hasn't been simplified since it supports older TLS versions - perhaps there is an implementation that only does TLS 1.3.

The best mitigation we can do with noise is thorough fuzz testing and an audit to make sure implementation met noise specifications. Fuzz techniques have improved, and they now catch heartbleed for instance, without any special prepping. Auditing is difficult as mentioned earlier; there are subtle ways to break the implementation.

EDIT: I am going to say OpenSSL for this question, but I'm trusting that the problems of the past are being worked out as funding to improve the codebase has been provided.

> Will encrypted P2P be enabled by default? Could make it opt-in for testing a couple releases and make it the default once it's stable.

It would have to be optional initially because daemons are upgraded slowly. The "in" peer would detect encryption by looking for the levin magic bytes and switch to encryption mode if not found.

If encryption can be disabled via command line, then it would take 3 fork-releases to make it mandatory (with the 2nd fork being defacto always encrypted except for hooligans). If there is no option to disable, then those fork numbers can be reduced by 1.

I think making it optional for a time period would be preferred. Exchanges and other high value targets can disable it for security (their privacy is basically non-existent anyway), while the rest of users can immediately use the feature. This also provides an opportunity to get performance feedback from users. But this does delay the roll out significantly, and users aren't completely protected until its mandatory.

## vtnerd | 2021-03-31T13:16:24+00:00
I'm definitely moving forward with this (some people on IRC have requested), but there doesn't appear to be any strong feelings on TLS vs Noise. I'll focus on trying to figure out if some limited authentication is possible (I initially thought it was, but then began to backtrack on that). In a p2p environment this is tricky because of spoofing reasons. There's a decent chance I will push for noise if the initial round-trips to initiate a connection can indeed be kept to a minimum.

## trasherdk | 2021-03-31T13:53:54+00:00
I kinda like the way Apache grant access to clients presenting a certificate signed by a CA.

```
<Directory "/home/blabla/local/www/example.com/secret">

  # Certificate authorization
	# require a client certificate which has to be directly
	# signed by our CA certificate in ca.crt
	SSLVerifyClient			require
	SSLVerifyDepth		1
	SSLOptions			+FakeBasicAuth
	SSLRenegBufferSize 		2048000
	# SSLRequire			(%{SSL_CLIENT_S_DN_Email} eq "hostmaster@example.com")
  # Certificate authorization - END
</Directory>
```

EDIT: This is probably only useful for RPC access.

## vtnerd | 2021-03-31T14:09:54+00:00
@trasherdk as your edit suggests, I'm not sure how this applies to p2p authentication. The problem is that some (not so trusted) peer is providing a public key. And when it fails it could because of operator changes (new deployment) or IP re-assignment. It looked like the best I could is have "trusted" peers where an IP+z85 pubkey could be provided on command line. And maybe trust peerlists directly from that peer and nothing further (with perhaps seed nodes being auto-trusted). But a number of the connections would likely be unauthenticated.

I looked briefly at what other projects were doing and didn't see anything useful at a glance. Ideally at least the initial bootstrap from seed nodes would be authenticated in a best effort manner.

## moneromooo-monero | 2021-04-15T16:43:13+00:00
Maybe some know nodes could have their pubkey in the monero source, then every peer would try to have one of these in their connection list. This would avoid complete eclipse. I can't qiute decide whether this centralizes the network though. Probably not much since it all works without it anyway.

## vtnerd | 2021-08-28T01:24:03+00:00
I haven't got much traction on this, because I've largely been overthinking the TLS vs. Noise debate. After thinking about @TheCharlatan comments, I think Noise wins out. I'll explain why briefly -

My recommendation would be to use `Noise_IK`, which is a 0-RTT handshake. The byte stream will be 16-bytes random, 64 bytes obfuscated, then the remainder will be encrypted. This leaves nothing identifiable for a typical DPI engine - it will generally be classified as "unidentified port number X". Aggressive spies could track the Monero p2p protocol for IP/Ports, but this forces an active instead of passive strategy. This strategy is similar to I2P. I am also going to suggest randomized padding to further enrage the DPI engines - although admittedly they still may "win" since the traffic patterns will typically be within a certain size window. Adding padding to the existing protocol is trivial as the "noise" portion of I2P/Tor already implements it.

The first packet handshake/ping packet will only be half-forward secrecy for efficiency (responder long-term secret can decrypt first packet). The first response and every subsequent packet will use forward-secrecy.

If the client/initiator is **not** using `--proxy`, then one ephermal pubkey is sent followed by one-long term pubkey in the first packet. Otherwise, two ephermal pubkeys are sent. This allows the responder to immediately authenticate peers specified on the command line in the first packet. TLS requires another RTT for this - so either every connection has an 2 RTT before data OR there is a passive-leak identifying the association between IPs using `--add-node` authentication.

I'm looking for feedback on whether the last point is too paranoid - implementing `Noise_IK` will be a decent development effort, but hopefully not a massive maintenance burden (the project already has to maintain custom crypto far more complicating than this). A determined spy can probably guess if someone is using `--priority-node` since the peer is _always_ used basically.

-----------

@moneromooo-monero 

> Maybe some know nodes could have their pubkey in the monero source, then every peer would try to have one of these in their connection list. This would avoid complete eclipse. I can't qiute decide whether this centralizes the network though. Probably not much since it all works without it anyway.

Yes, I'm thinking that authentication will only occur with seed nodes AND pubkeys listed on the command line. Both will make eclipse attacks more difficult, and I don't see how this centralizes the network.

## vtnerd | 2021-08-28T01:29:56+00:00
> If the client/initiator is not using --proxy, then one ephermal pubkey is sent followed by one-long term pubkey in the first packet. Otherwise, two ephermal pubkeys are sent. This allows the responder to immediately authenticate peers specified on the command line in the first packet. TLS requires another RTT for this - so either every connection has an 2 RTT before data OR there is a passive-leak identifying the association between IPs using --add-node authentication.

Already bumping my own response because I forgot one point. I wasn't sure if concealing Monero P2P was worth the effort since the protocol leaks IP/Ports, however, only IP/Ports accepting inbound connections are leaked. So the major leak is the standardized port numbers, which perhaps can be partially addressed by a campaign to use non-standard ports and a `--avoid-standard-port` switch or similar. People keep asking about this kind of thing, so at a certain it just seems like the Monero thing to implement.

## vtnerd | 2021-08-31T23:00:22+00:00
A [writeup](https://github.com/vtnerd/monero/blob/docs_p2p_e2e/docs/LEVIN_PROTOCOL.md#encryption) of how the encryption mode will work on a technical level, with some justifications for the choices made.

## vtnerd | 2021-08-31T23:02:12+00:00
This markdown file will be PR'ed to the main repo for feedback before serious development effort gets done. The investigation work has already been done (meaning, I have a rough idea of how to incorporate these changes into the existing implementation).

## cirocosta | 2021-09-03T20:04:02+00:00
Great stuff @vtnerd ! Will definitely go through it 👍  

I noticed there's not a PR opened for it, but I think it'd be nice to have so folks could collaborate on it (sure, GitHub allows per-commit comments even without a PR, but the user experience is subpar, imo), unless you want to keep the discussion focused on this thread. wdyt?

---

@vtnerd , in the meantime, I've left  a few comments in the latest commit (https://github.com/vtnerd/monero/commit/ef605b2098ce420aac641c2acb7b50ee3e1e8b24) - not very familiar with the noise framework, so still wrapping my head around it asking some questions there; really fascinating nevertheless!

## SyntheticBird45 | 2023-05-02T13:59:57+00:00
Hi,
This dicussions seems to be halted since the the Noise_IK vs TLS 1.3 debate. And didn't appear in the Monero Dev Meeting logs. @vtnerd actually [write out his proposal](https://github.com/monero-project/monero/pull/8028) and encourage the use of Noise_IK 
I would like this discussion to be restarted. I'm developing [Cuprate](https://github.com/Cuprate/cuprate) and [I planned to integrate encrypted P2P](https://github.com/Cuprate/cuprate/issues/11) through the QUIC Protocol. It has several qualities over TCP:
- Native multiplexing with loss recovery
- Better efficiency, less latency
- Enforcing TLS 1.3, with Client Hello and headers encrypted.
- Support for 0-RTT TLS Handshake (what originally make the proposal go for Noise_IK)
- also check MsQuic's [doc](https://github.com/microsoft/msquic/blob/main/docs/Deployment.md)

I actually propose to use TLS 1.3 as it permit us, and the monero-project, to not rely on the Noise library.
We would even be glad if our idea of using QUIC ~over~ alongside TCP+TLS would be accepted by the core-project, [MsQuic](https://github.com/microsoft/msquic) library is available with C++ API


## vtnerd | 2023-05-02T17:03:44+00:00
This stalled because Monero shouldn't do _any_ authentication in the standard case, so the proposal needs to be re-written. The pubkey can act as an identifier, so the user needs to opt-in and be aware that they should generate new keys when an IP /hostname changes. Keep that in mind if your pursue Quic.

------------------

If you are writing a Rust compatible node, why push Quic when it may differ with what `monerod` is doing? This response is basically tantamount to coercing me (and others in the community) to agree to Quic.

Quic is over UDP with its own retransmit mechanism, etc.. Seems a bit much. Monero doesn't need the multiplexing (afaik). The other features are nice, but only less latency is interesting (and what about latency comparisons to TCP+noise_*?).

One advantage the various Noise_* protocols have is some can have "noise" from byte 0. I don't think we can do this with the average p2p connection, but we can do this with authenticated connections (ones where people "opt-in" to a consistent pub key for authentication). Users could theoretically only allow authenticated style connections too. I don't think this is possible with Quic, but I would have to go back through the spec.

## SyntheticBird45 | 2023-05-02T18:52:07+00:00
> If you are writing a Rust compatible node, why push Quic when it may differ with what monerod is doing? 

I consider encryption, even without proper authentication, to be a security improvements. The fact that I can right now start `mitmproxy`, and give bullshit core sync data to my node or others, is a red flag for me. I'm also convinced that the more the monero network traffic looks like everything except monero network, the better it is, long-term standing.

> This response is basically tantamount to coercing me (and others in the community) to agree to Quic.

Actually Cuprate is going to use the standard protocol for `monerod` peers, while using (by default) QUIC for Cuprate peers. So It's not really coercing people to agree to Quic, you can opt-out if you want. I just find it better this way.

> Quic is over UDP with its own retransmit mechanism, etc.. Seems a bit much. Monero doesn't need the multiplexing (afaik).

For Cuprate this isn't an issue, but for monerod yeah I understand. And yeah Monero don't need multiplexing. It's just QUIC's way to increase efficiency and reduce latency/overhead

> The other features are nice, but only less latency is interesting (and what about latency comparisons to TCP+noise_*?).

I don't know for TCP+noise+*?, but what's sure is that QUIC is faster than TCP+TLS. Now don't get me wrong, [Noise+QUIC is actually a thing](https://eprint.iacr.org/2019/028.pdf), but if monerod is tying to simplicity, QUIC-TLS seems equivalent to the improvements Noise brings over TCP-TLS.

> One advantage the various Noise_* protocols have is some can have "noise" from byte 0. I don't think we can do this with the average p2p connection, but we can do this with authenticated connections (ones where people "opt-in" to a consistent pub key for authentication). Users could theoretically only allow authenticated style connections too

Could you elaborate ?

Anyway thx for the feedback I'll have to think too at the pubkey.

## vtnerd | 2023-05-02T20:25:45+00:00
>> One advantage the various Noise_* protocols have is some can have "noise" from byte 0. I don't think we can do this with the average p2p connection, but we can do this with authenticated connections (ones where people "opt-in" to a consistent pub key for authentication). Users could theoretically only allow authenticated style connections too
>
> Could you elaborate ?

The Noise protocol doesn't have any headers, and the first ephermal pubkey that usually gets sent can be symmetrically encrypted by the servers long-term pubkey. This is actually an obfuscation, but it creates problems for standard DPI engines trying to fingerprint connections - typically they have to (1) determine the static pubkey via p2p protocol, (2) decrypt it, and (3) determine if it matches a point on the curve. This slows down the server a bit (symmetric crypto is still fast), but for DPI engines scanning/filtering traffic this hell. OTOH most are just going to assume the standard Monero ports means Monero traffic. So perhaps a waste of time.

Unfortunately it is only likely to be used when someone opts-in to the static pubkey mode.

# Action History
- Created by: vtnerd | 2020-12-05T00:29:24+00:00
