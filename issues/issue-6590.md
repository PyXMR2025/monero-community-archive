---
title: Possible tor/i2p relay bug in 0.16 daemon
source_url: https://github.com/monero-project/monero/issues/6590
author: MoneroArbo
assignees: []
labels: []
created_at: '2020-05-25T12:40:28+00:00'
updated_at: '2020-12-23T22:05:11+00:00'
type: issue
status: closed
closed_at: '2020-12-23T22:05:11+00:00'
---

# Original Description
This is going to be a long one, so, apologies.

Yesterday I created a transaction in the GUI wallet (0.15.0.4) and sent it to my local daemon (0.16.0) which was set up to relay transactions over i2p. This morning, after 12+ hours of not being able to establish any outbound i2p connections (I have plenty of inbound active connections), I decided to restart the daemon with the option to relay over tor as well as i2p.

After a few minutes, I see the transaction still has not been broadcast, despite the daemon reporting an active outbound tor connection. I was thinking, maybe since the transaction was created when I was set up to only relax over i2p, it will only automatically broadcast over i2p, not tor. A little wonky, but no problem. I go to the daemon and use the relay_tx command to relay my transaction.

[This is the output](https://user-images.githubusercontent.com/65900302/82809979-585e2980-9e5b-11ea-8690-2b1f48836de5.png)

Something about failing to parse (I copied the tx_id straight from the GUI to my clipboard), then a warning about not being able to send over the anonymity network (even though I have outbound tor connections), then a message saying success.

Except there was no success. The transaction has been not been relayed. It has not been confirmed and is not showing up in the mempool at xmrchain.net.

As a next step, I close and open the daemon again, this time without any --tx-proxy flags, since my understanding is that a transaction waiting to be relayed over an anonymity network is supposed to be relayed over ip4 if the daemon is started without these flags, and try the relay_tx command again. [This is the output](https://user-images.githubusercontent.com/65900302/82810141-b985fd00-9e5b-11ea-8e71-d1f276efe072.png).

At this point I gave up, flushed the tx from my local mempool, then deleted the wallet state file and re-opened my wallet for a rescan before creating a new transaction.

The re-attempt: the daemon is set it with --tx-proxy to both i2p and tor. The transaction will not relay even though I DO have an outbound tor connection. [Here](https://paste.debian.net/1148714/) is a paste which shows me with an outbound tor connection. Then it shows the error when I attempt to do relay_tx. Then it shows that I'm STILL reportedly connected to the tor node, even though the tx relay just failed due to there reportedly being no outbound anonymity connections.

So again, I try starting monerod without the --tx-proxy flags. It still doesn't relay automatically, so I try again to relay the tx manually. The error from my second link re-appears.

Ultimately, I ended up clearing this transaction as well before firing up the daemon with no --tx-proxies and sending a third one unencrypted over ip4. This third attempt over ip4 succeeded.

As a final experiment, I started monerod with ONLY the tor transaction relay enabled, no i2p, and tried another transaction once I had established an outbound Tor connection. This one was successfully relayed over Tor with zero issues.

So, a few possible bugs here:

1) The transaction created while set up to relay over i2p will not relay over tor, not even when I attempt to manually relay it

2) The transaction created with i2p/tor relaying enabled will not relay over tor if it is the only available outbound connection.

3) Transactions created with i2p/tor relay enabled will not relay over ip4, even when the daemon is restarted without the --tx-proxy flags and relay is attempted manually

4) The 'relay_tx' command says success, even when it is not successful

Now, the first three I'm not sure about. Maybe transactions created with only i2p relay enabled should not relay over tor, even manually. Though I am of the mind that this should be possible, even if it requires a specific command / confirmation.

The second one could admittedly be a case of my outbound connections not being very stable. Unlike the first attempt with i2p only, I did not wait for hours. Only for a couple of minutes. However, without i2p enabled, I WAS able to relay a tx over tor very quickly and with no manual intervention.

The third one could just be me misunderstanding how the daemon is supposed to work with the --tx-proxy flags, but I remember reading that transactions intended to be relayed over anonymity nets would be held only until 1) an outbound connection was available or 2) the daemon was restarted without the --tx-proxy flags.

The fourth one is, to me, most obviously a bug. I do not think the relay_tx command should say 'success' unless the tx has actually been relayed successfully.

Finally, a question: why do I even need an outbound connection to relay a transaction? My understanding is that outbound vs inbound is just about who initiates the connection. But once the connection is initiated, isn't it supposed to act as a two-way circuit between peers? It doesn't fit my understanding of what peer-to-peer means for me to only be able to perform certain actions over outgoing connections. So, I'm curious.

(edited for clarity and grammar)

# Discussion History
## vtnerd | 2020-05-25T17:22:51+00:00
Unfortunately this giant writeup doesn't contain logs. So while it seems "obvious" that the transaction is not being sent, the transaction could also be blackholed somewhere in the I2P chain after it leaves the daemon. The bigger issue is why the daemon wasn't relaying over ipv4 mode. Run `set_log +net.p2p.traffic:DEBUG` in the daemon to get some information on whether the proper commands are being sent out from the daemon. The log statement will contain the connection id used and the command number 2002.


> 1. The transaction created while set up to relay over i2p will not relay over tor, not even when I attempt to manually relay it
> 2. The transaction created with i2p/tor relaying enabled will not relay over tor if it is the only available outbound connection.

If two anonymity networks are enabled, only one is chosen to relay transactions. The first one with available outgoing connections is selected. I2P is preferred over Tor. So with both enabled, it is intentionally only sending over I2P.


> 3. Transactions created with i2p/tor relay enabled will not relay over ip4, even when the daemon is restarted without the --tx-proxy flags and relay is attempted manually

This is probably the most concerning issue. I'm not sure what to make of it without further information - I tested this kind of thing locally so I'm not sure what state your daemon/tx was in at the time.


> 4. The 'relay_tx' command says success, even when it is not successful

Unfortunately this has always been suspect - historically if there were never any connections this message would be displayed. I agree it could use updating, correctness is tricky here because with white noise there is a delay (up to ~15 seconds) so the message would have to be pushed later. Messages are displayed asynchronously already, so this should be acceptable.

> Finally, a question: why do I even need an outbound connection to relay a transaction? My understanding is that outbound vs inbound is just about who initiates the connection. But once the connection is initiated, isn't it supposed to act as a two-way circuit between peers? It doesn't fit my understanding of what peer-to-peer means for me to only be able to perform certain actions over outgoing connections. So, I'm curious.

The recipient can associate a transaction with a fixed i2p/tor address, which defeats the purpose of routing the transaction over the network. It would allow someone to identify multiple transactions from the same source, and possibly unmask the ring signature entirely. Monero could fluff routing to make it difficult to know whether the transaction is relayed or sourced at that address, but sending to outgoing connections only is using i2p/tor "as designed" (at least imo).

## MoneroArbo | 2020-05-25T20:44:03+00:00
Sorry for not including logs originally. I wasn't sure what would be useful, and when interacting with the node it's a little difficult to see what's going on with set_log above 0. Anyway, here is my [bitmonero.log](https://github.com/monero-project/monero/files/4678721/bitmonero.log.txt) with the set_log command you requested.

What you see in this log is me starting the daemon with an i2p --tx-proxy, trying to send a transaction before a connection is established, then purposefully closing the daemon, and re-opening it without the tx-proxy. Then, just a few moments after the daemon finishes initializing, I issue the relay_tx command and get the error I first reported.

After that, I closed the daemon again and opened it once more with an i2p --tx-proxy. After establishing an outbound i2p connection, I try once again to use the relay_tx command. It fails with the same error message.

I'm happy to collect more logs if needed.

On another note, while trying to create these logs, I was accidentally successful relaying a transaction over i2p. So at least I know it works! I was kind of worried when I didn't manage to establish a single outbound connection over the course of something like 16 hours.

Or maybe I did establish an outbound connection and the transaction was stuck for another reason. After all, I do currently have a stuck transaction despite having established an outbound i2p connection. At least, that's what 'print_cn' reports.

> So with both enabled, it is intentionally only sending over I2P.

I feel like if somebody has both enabled, they are implicitly saying they are okay with either. Just my 2c.

> The recipient can associate a transaction with a fixed i2p/tor address, which defeats the purpose of routing the transaction over the network. It would allow someone to identify multiple transactions from the same source, and possibly unmask the ring signature entirely. 

Thank you for the explanation. I think that makes sense. Do you mean that it might unmask the actual output of the ring signature in the same way that it can be revealed to a nefarious RPC node if it sends an error and you broadcast a new tx?

Maybe this will be a non-issue if / when i2p is integrated to the point where anyone with i2p enabled can receive incoming connections easily or by default, but at the same time, right now, I feel like I'd like the option to have my transactions relayed through an inbound i2p connection (or through tor for that matter) rather than not at all.

Perhaps the solution is that the relay_tx command should automatically, or have a flag to, override these defaults?

> Monero could fluff routing to make it difficult to know whether the transaction is relayed or sourced at that address,

Does Dandelion++ accomplish this?

**edit:** I'm seeing in the log where the daemon is sending command 1001 to its own i2p address, like, several times. If I understand correctly, peer IDs are supposed to prevent self connections over anonymity networks. Assuming that function is still in tact / working as intended, shouldn't it blacklist the i2p address after finding the peer ID matches? At least temporarily. I can file this as a separate bug report, I just want to make sure first that I'm not just being dumb.

## vtnerd | 2020-05-26T06:48:40+00:00
> Sorry for not including logs originally. I wasn't sure what would be useful, and when interacting with the node it's a little difficult to see what's going on with set_log above 0. Anyway, here is my bitmonero.log with the set_log command you requested.

A warning message is displayed in the log, indicating there are no connections available for sending the transaction. Based on the commands being sent, it appears that a connection was never fully established to an i2p peer. In this particular case, no transaction could ever be sent (which sounds different from your first test).

> I feel like if somebody has both enabled, they are implicitly saying they are okay with either. Just my 2c.

It will use tor, but only if i2p has no outbound connections. Its designed to only use one, as I didn't see an advantage to sending data over multiple "anonymity" networks. It seemed more likely to  increase the chances of unmasking.

> Does Dandelion++ accomplish this?

Dandelion++ fluff. Although I wouldn't recommend it for the reasons stated elsewhere.

> Thank you for the explanation. I think that makes sense. Do you mean that it might unmask the actual output of the ring signature in the same way that it can be revealed to a nefarious RPC node if it sends an error and you broadcast a new tx?
>
> Maybe this will be a non-issue if / when i2p is integrated to the point where anyone with i2p enabled can receive incoming connections easily or by default, but at the same time, right now, I feel like I'd like the option to have my transactions relayed through an inbound i2p connection (or through tor for that matter) rather than not at all.
>
>  Perhaps the solution is that the relay_tx command should automatically, or have a flag to, override these defaults?

The change output is eventually re-used as an input to a ring signature of a future transaction. Therefore, if an adversary can determine that  2+ transactions are from the same source, they have a decent shot at knowing the "real" spend in the ring signature. An inbound i2p/tor hidden service has a randomly generated public key, which can be used as an identifier in this situation. The odds of someone else generating that public key are low (else public key crypto has been effectively broken). Broadcasting transactions to inbound connection is more risky than using outbound only connections. The behavior is more simple to analyze.

> edit: I'm seeing in the log where the daemon is sending command 1001 to its own i2p address, like, several times. If I understand correctly, peer IDs are supposed to prevent self connections over anonymity networks. Assuming that function is still in tact / working as intended, shouldn't it blacklist the i2p address after finding the peer ID matches? At least temporarily. I can file this as a separate bug report, I just want to make sure first that I'm not just being dumb.

No blacklisting occurs over i2p/tor. Its currently not possible because we haven't implemented the relevant control protocols for i2p/tor to know the inbound address. And if we implemented that feature, banning the address is defeated by churning public keys (although it would stop the kind of behavior you are describing).

This one is _probably_ a bug, as I don't recall how this was handled. The code may need to track to its inbound address better, the code for ipv4 doesn't work quite right here. 

## MoneroArbo | 2020-05-26T12:09:27+00:00
> A warning message is displayed in the log, indicating there are no connections available for sending the transaction

I tried to describe, but the part of the log this message is in is from when I was initially creating the transaction in order to replicate the bug. During this part of the log, I was intentionally trying to compose and send an i2p transaction before a connection was established, so that I could recreate the issue of it not going through later.

You should see, further in the log, after the daemon is stopped and re-started, where I use 'print_cn' to show that there is an outbound i2p connection, then issue the relay_tx command and get the error.

> It will use tor, but only if i2p has no outbound connections. Its designed to only use one, as I didn't see an advantage to sending data over multiple "anonymity" networks.

Perhaps I misunderstood you, then. The behavior I observed (which is not in the logs I uploaded) was one where a transaction created with i2p+tor enabled would not relay when there was only a tor outbound connection available. I'll see about collecting logs.

> Dandelion++ fluff. Although I wouldn't recommend it for the reasons stated elsewhere.

Do you mind if I ask where? I am curious about this.

> The change output is eventually re-used as an input to a ring signature of a future transaction. Therefore, if an adversary can determine that 2+ transactions are from the same source, they have a decent shot at knowing the "real" spend in the ring signature. An inbound i2p/tor hidden service has a randomly generated public key, which can be used as an identifier in this situation.

I can of course see the logic in not giving away information that correlates transactions when it can be avoided. But still, it would be nice, as a user, being aware of the risk, to relay my transaction without having to restart the daemon. Even if sending over inbound i2p is a terrible idea that users should be disallowed from ever doing, it should at least be possible to force it over ip4 without restarting the daemon.

That said, I'm having a hard time seeing how pushing it over an inbound ip4 connection would be worse than sending it clear over the wire with ip4. It had already occurred to me that doing so would correlate the TX with my inbound i2p address, but I've never read that Ring Signatures can be revealed by the observer looking at multiple transactions that don't share the same input. If true, it seems like a major problem for Monero generally, not just Monero over i2p. Anybody using a public RPC node and not changing their node connection super frequently would be subject to this attack, no? Yet, in all the warnings I've read about using public nodes over RPC, this particular concern was never mentioned. And for ip4, even with Dandelion++, this issue you just described would seem to risk revealing Ring Signatures to an ISP level observer.

But really, I suppose the larger issue is that there are so few connectable i2p peers. Having zero outbound connections currently seems to be a very common occurrence that can persist for long stretches of time. Are there really so few connectable peers? Perhaps its an issue of the i2p network becoming partitioned. I added the dsc*.i2p address mentioned [here](https://github.com/i2p-zero/i2p-zero/blob/master/mipseed.md) as a peer, but I don't know that I ever actually managed to establish a connection to it. I only managed to get any i2p peers at all after I connected with knacc on reddit and got them to add me as a peer to their node.

Or, here's yet another thought: if, say, the max number of outbound peers were 8, and the node had already established 8 outbound ip4 connections, might that prevent an outbound i2p connection from being established?

> This one is probably a bug, as I don't recall how this was handled. The code may need to track to its inbound address better, the code for ipv4 doesn't work quite right here.

Cool, thanks. I'll open up a new issue for this, then.

## MoneroArbo | 2020-05-26T12:45:45+00:00
[Here](https://github.com/monero-project/monero/files/4682195/bitmonero.log2.txt) are are the logs related to the issue where a transaction will note route over tor if both i2p and tor tx-proxies are enabled but only a tor outbound connection is available is available. In this log, with both tor and i2p tx-proxies enabled, I waited for an outbound tor connection to establish, then sent a tx from the wallet. It went nowhere. You can see in the logs that the outbound tor connections are a little unstable, but you can see in the log that I did establish, at one point, two outbound connections with one lasting for over two minutes.

[Here](https://github.com/monero-project/monero/files/4682237/bitmonero.log3.txt) is a log where I have ONLY tor tx-proxy enabled and successfully relay a tx over tor. This is why I do not think the issue when i2p+tor are enabled is my connection quality. It works when only tor is enabled, but not when both are enabled, reliably.

## vtnerd | 2020-05-27T05:33:30+00:00
> After that, I closed the daemon again and opened it once more with an i2p --tx-proxy. After establishing an outbound i2p connection, I try once again to use the relay_tx command. It fails with the same error message.
>
> I'm happy to collect more logs if needed.

I'm not certain what would cause the behavior you are seeing right now. I may have to duplicate locally if I cannot spot through code audit.

>>   Dandelion++ fluff. Although I wouldn't recommend it for the reasons stated elsewhere.
>
> Do you mind if I ask where? I am curious about this.

I stated rationale in my first two posts, perhaps it wasn't clear.

Using outbound connections over i2p/tor to send transaction is leveraging the research/design/security/privacy of those networks to route transactions. The "server" cannot make associations between  "streams" unless it is leaked within the stream. Using Dandelion++ fluff mode to mitigate a privacy leak when using i2p/tor inbound connections is a different security model, requires separate analysis, and is likely never going to be sufficient no matter how many mitigations are made.

Read the Dandelion papers. The protocol routes transactions over outbound connections in the initial stage for a separate and related reason - sybil attackers can fill your incoming table. This is even easier over i2p/tor, because inbound addresses are a cheap to construct public key instead of an ipv4/6 address. Or in other words, "full" Dandelion++ over i2p/tor requires outbound connections to send transactions, and "fluff only" mode to get the behavior you want changes the security model of that protocol and the security model of typical i2p/tor usage.

> I can of course see the logic in not giving away information that correlates transactions when it can be avoided. But still, it would be nice, as a user, being aware of the risk, to relay my transaction without having to restart the daemon. Even if sending over inbound i2p is a terrible idea that users should be disallowed from ever doing, it should at least be possible to force it over ip4 without restarting the daemon.

A new daemon command (or option to existing one) might be useful for this.

> That said, I'm having a hard time seeing how pushing it over an inbound ip4 connection would be worse than sending it clear over the wire with ip4. It had already occurred to me that doing so would correlate the TX with my inbound i2p address, but I've never read that Ring Signatures can be revealed by the observer looking at multiple transactions that don't share the same input. If true, it seems like a major problem for Monero generally, not just Monero over i2p. Anybody using a public RPC node and not changing their node connection super frequently would be subject to this attack, no? Yet, in all the warnings I've read about using public nodes over RPC, this particular concern was never mentioned. And for ip4, even with Dandelion++, this issue you just described would seem to risk revealing Ring Signatures to an ISP level observer.

The initial "stem" phase of Dandelion++ explicitly sends transactions over outbound connections, to prevent "sybil" attackers from spying on the network (i.e. **not** at ISP level, but spying within the p2p network).

And yes, @moneromooo-monero suggested enabling SSL but I (foolishly?) NACKed because of my abhorrence to SSL and OpenSSL. The daemon could force TLS 1.3 (the least bad yet!) or use the NK Noise protocol (some small benefits to its use), but it still takes some tricky key management to get working (pubkeys in a dynamic-ip p2p network). Or else, no authentication ever. Regardless, encryption for transaction sending is provided by i2p/tor **today**, and in the short-run the next push will be for i2p/tor seeding so that everything "just works" with only the `--tx-proxy` flag set.

And as for public RPCs not mentioning this behavior - all information on the subject has stated repeatedly that there is reduced privacy with that mode.

## MoneroArbo | 2020-05-28T12:41:52+00:00
Hey thanks for all the info, it really does help me understand. Just one thing:

> all information on the subject has stated repeatedly that there is reduced privacy with that mode.

I have read most or all of the public documentation on RPC and while it does, repeatedly, talk about reduced privacy, the particular attack you are talking about, is not mentioned anywhere that I can recall reading.

It also doesn't seem to be common knowledge that IPv4 traffic, both p2p and RPC, is totally unencrypted by default. TLS 1.3 or whatever would be an improvement imo, but I'd say the lack of awareness of the lack of encryption is more of a problem than the lack of encryption itself.

Just my 2c. I for one will definitely be doing my part to spread awareness of the situation.

## MoneroArbo | 2020-05-28T12:46:19+00:00
I think maybe the relay_tx saying 'success' when it fails is related to this pull request: https://github.com/monero-project/monero/pull/6599

Other issues mentioned in this report may still be relevant, though. I think.

## MoneroArbo | 2020-06-11T11:32:37+00:00
Here is a [bitmonero.log](https://github.com/monero-project/monero/files/4764401/bitmonero.log.txt) snippet from this morning. The daemon is running with an i2p --tx-proxy and also with an outbound i2p node set as a priority node, as mentioned in #6631

What the log shows is that me regularly losing all outbound connection, as is typical, then the line "Unable to send transaction(s)" when I try to send a connection while there are no outbound anonymity connections. Then you can see the "Lost all outbound connections" message happening several more times, which I believe implies that an outbound i2p connection has been re-established. However, the transaction still has not broadcast. It has, as of this writing, been sitting in my local TX pool for almost 30 minutes.

Also, on another note, it _really_ seems like the daemon log should report not only when anonymity connections are lost, but also when they're established. If all you see are log entries saying the connection has been dropped, how do you know when you have an active connection? Yes, 'print_cn' exists, but that only works if the daemon is in interactive mode.

## moneromooo-monero | 2020-06-11T11:59:35+00:00
You can run print_cn on a detached daemon with: bitmonerod print_cn

## MoneroArbo | 2020-06-11T12:05:15+00:00
I think you mean monerod not bitmonerod but wow, thanks! I had no idea you could interact with the daemon binary in that way.

## MoneroArbo | 2020-12-23T22:05:11+00:00
relay_tx has been working for me in recent releases, closing this issue

# Action History
- Created by: MoneroArbo | 2020-05-25T12:40:28+00:00
- Closed at: 2020-12-23T22:05:11+00:00
