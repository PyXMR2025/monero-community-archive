---
title: 'Monero Tech Meeting #167 - Monday, 2026-04-27, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1378
author: rbrunner7
assignees: []
labels: []
created_at: '2026-04-24T19:01:21+00:00'
updated_at: '2026-04-29T16:57:33+00:00'
type: issue
status: closed
closed_at: '2026-04-29T16:57:33+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1373).


# Discussion History
## rbrunner7 | 2026-04-29T16:57:33+00:00
````
<r​brunner7> Meeting time. Hello! (No link to the meeting's meta issue, because GitHub is borked right now)
<j​berman> *waves*
<s​needlewoods> hey
<UkoeHB> Hi
<j​pk68> Hello
<r​brunner7> Alright, what are the reports about last week? Me: Could continue a bit with implementing Polyseed for the CLI wallet
<k​oe000> Me: multisig slowly
<s​needlewoods> added struct to describe transfers: https://github.com/monero-project/monero/compare/c233a3eff0721686a39f7bb363b57a53aa5a75b2..55d02066515d54ba97a2be645b5d33e6bb803ba7
<s​needlewoods> (hopefully) as you rbrunner recommended/imagined
<s​needlewoods> also worked on some smaller reports and reviews
<j​pk68> Added support for standard I2P hostnames to the daemon (awaiting review); published an AUR package for Cuprate; attempted to improve fiat API support in the GUI
<j​berman> me: mostly beta stressnet prep (binaries coming soonTM) and followup on PR's for release v0.18.5.0
<r​brunner7> jpk68: Looks like you pick up speed :)
<jpk68> +1
<j​effro256> howdy
<r​brunner7> So, if you hope for binaries soon, jberman , no real blockers left I guess?
<j​effro256> me: also stressnet prep, plus some vuln handling
<j​berman> a small log spam thing I've been discussing with jeffro, it's not a major blocker but I think would be nice to have done. And ofrn is still doing some testing AFAIK
<j​effro256> Will have that done in the next couple hours btw
<jberman> +1
<r​brunner7> I wonder how we will fare as an open source project in the light of a possible pick-up of AI found issues. Might get interesting, or maybe merely annoying if we have bad luck
<r​brunner7> As I see it, we can't do anything pro-actively, just wait what will happen. I think more or less the whole IT scene is now waiting for how things will turn out security-wise.
<selsta> we received like 30 reports in the past month
<selsta> so far the AI reports have been a couple interesting things and lots of more or less irrelevant edge cases
<r​brunner7> Was that above long-term average?
<selsta> yes, previously it would be like 1 report per month
<r​brunner7> Ah, you mean only the AI reports were 30?
<r​brunner7> 1 per month - oh, ok
<selsta> yes so 30x increase, though i assume we will have solved the low hanging fruits with the next release so let's see if the high amount of reports continue
<j​effro256> https://github.com/seraphis-migration/monero/pull/336
<j​pk68> jeffro256: Sorry for asking you this for the 10th time, but have you heard anything new from Ledger/Trezor?
<j​pk68> I also wonder if the Trezor dev who originally implemented support is aware of the possibility of opening a new CCS for it
<selsta> to be precise he was never CCS funded, in the past Trezor paid for it
<jpk68> +1
<j​effro256> Unfortunately, nope
<r​brunner7> I dimmly remember that with one of the two there is a potential problem with a new protocol that pretty complicated, the protocol to talk to the device?
<j​pk68> RIP
<j​pk68> Yeah, it's kind of ludicrous
<r​edsh4de> the protocol, for reference: https://github.com/trezor/trezor-firmware/blob/main/docs/common/thp/specification.md
<selsta> jeffro if you could prioritise 10431 and 10367 that would be great, last thing missing for the release
<j​pk68> They created a new protocol that can work over Bluetooth or (Web)USB, that includes a cusom NoiseXX handshake and like 4 different trasnport layers
<j​pk68> The spec document (linked above) is quite literally 10x longer than the 'legacy' one
<r​brunner7> That does not sound good.
<MarkoPohlo> rbunner, re: the future of open source projects facing AI-found issues - that's where protocol modelling and formal verification come in!
<r​brunner7> MarkoPohlo: Hmm, yes, but I guess anything in such a direction will take time, and quite some effort in itself
<r​brunner7> Maybe stupid question, but was there a real *need* for a new protocol?
<j​pk68> No...
<r​brunner7> You could get the suspicion that they don't want other apps talking to their devices that eagerly anymore ...
<j​pk68> They also advertise their new device as 'post-quantum' despite the fact that the THP (Trezor Host Protocol) in its current state uses ECDH
<j​pk68> I think this is pretty disingenuous
<j​effro256> selsta: heard, ty will do that today
<j​pk68> Anyways, I've become sort of intrigued by how an implementation of this would work, and at first glance, it appears we would need to have some sort of abstraction layer that manages the encryption and state machine
<j​effro256> Yeah that new protocol seems like it was born in committee hell. Hopefully, once we have Rust toolchain integration, we can simply use Trezor's Rust library
<j​effro256> haven't looked into it though
<j​pk68> AFAIK Trezor doesn't have a Rust library for that. Just Python at the moment
<r​brunner7> Ah, there is a Rust library that speaks the new protocol? That's at least a shimmer of hope
<j​pk68> There is a BTC-only third-party implementation of it, but it's third party
<j​pk68> and tobtoht has also said it would not be preferable to add more Rust crates
<j​effro256> https://github.com/trezor/trezor-firmware/tree/main/rust/trezor-thp/
<j​pk68> How did I now know about that, lmao
<j​pk68> Apologies :)
<j​effro256> I also would prefer not to add more crates, but I would prefer less to spend a crap ton of time reinventing the wheel.
<r​brunner7> Well, I understand reluctance for adding more dependencies, but maybe it will turn out to be the lesser evil. Somehow I don't see somebody doing that protocol in C++
<j​effro256> Especially since Trezor THP is ridiculously complicated
<r​brunner7> Complicated == hight potential for bugs. Just saying :)
<r​brunner7> I would say what you want when you buy a hardware wallet is a solid step up in security. Maybe that is not that.
<j​pk68> The Rust library also doesn't have an insane amount of dependencies (11, to be exact)
<r​brunner7> Alright, looks pretty bleak then. Do we have something else to discuss today?
<p​alinatolmach> It is, but FV is benefitting a lot from AI improvements in terms of proof generation and scalability. Having a protocol model also unlocks many downstream positive effects as it can serve as a reference for AI codegen, audits, test generation, vulnerability detection, and so on
<r​brunner7> Doesn't look like it. Thanks everybody for attending, read you again in 1 week!
<pk68> +1
<s​needlewoods> thanks everyone
````


# Action History
- Created by: rbrunner7 | 2026-04-24T19:01:21+00:00
- Closed at: 2026-04-29T16:57:33+00:00
