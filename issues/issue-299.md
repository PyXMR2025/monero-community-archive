---
title: 'Payment ID Discussion: 25 January 2019 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/299
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2019-01-19T16:46:08+00:00'
updated_at: '2020-02-09T18:01:16+00:00'
type: issue
status: closed
closed_at: '2020-02-09T18:01:16+00:00'
---

# Original Description
**Location**

[Freenode](https://kiwiirc.com/nextclient/#irc://irc.freenode.net/#monero-community) | [Mattermost](https://mattermost.getmonero.org/monero/channels/monero-community) | [Slack](https://monero.slack.com/) | Irc2P

Please test the relays shortly before using. If there are any issues, please use Freenode IRC directly.

Please PM [SGP on Reddit](https://www.reddit.com/message/compose/?to=SamsungGalaxyPlayer&subject=Monero%20Slack%20invite%20(from%20GitHub)&message=Hello%20please%20send%20a%20Monero%20Slack%20invite%20to%20the%20following%20email:) with your email for a Slack invite if desired.

 - `#monero-community`

**Time**

17:00 UTC
12:00 ET
11:00 CT
09:00 PT

[Use this timezone calculator to convert UTC to your time zone](https://www.timeanddate.com/worldclock/converter.html?iso=20190119T170000&p1=tz_et&p2=28&p3=111&p4=49&p5=179&p6=70&p7=224&p8=48&p9=136).

**Proposed Meeting Items**

The Monero researchers, developers, and community members would like to announce an important proposed change regarding Monero payment IDs. Many parts of the Monero ecosystem are reliant on some form of payment IDs. These are exciting changes that improve privacy and reduce user frustration with standalone payment IDs.

The Monero community is proposing to remove support for sending transactions with standalone payment IDs in most wallets in April 2019. They also propose to remove support for sending transactions with payment IDs (including integrated addresses) on the consensus layer in October 2019. Exchanges, payment processors, and other services should upgrade to support Monero subaddresses as soon as possible.

We ask that you please review the attached resources on the background decision to move to subaddresses, the upgrade process, and the timeline.

If you have any questions and would like to participate in a discussion of the future of payment IDs, please participate in the Monero Community meeting Friday January 25 at 17:00 UTC (noon eastern US). We expect to make a final decision during the meeting.

You can always join before the meeting to voice any comments, or leave them in this GitHub issue. Ref: https://github.com/monero-project/monero/issues/3772

[Address Background Prerelease.pdf](https://github.com/monero-project/meta/files/2775744/Address.Background.Prerelease.pdf)
[Upgrade Process.pdf](https://github.com/monero-project/meta/files/2775745/Upgrade.Process.pdf)
![upgrade timeline](https://user-images.githubusercontent.com/12520755/51429744-4ae5bf00-1bd7-11e9-837e-1ecb91369af1.png)

# Discussion History
## SamsungGalaxyPlayer | 2019-01-24T23:33:03+00:00
This issue and the related resources were sent to the Monero-announce [email list](https://lists.getmonero.org/hyperkitty/list/monero-announce@lists.getmonero.org/thread/RF6FI3CE6IETWUKUMGXYQL2VTRMA6I4R/).

## qertoip | 2019-01-25T08:50:45+00:00
For businesses accepting Monero **integrated addresses** have critical advantages over subaddresses:
* No private view key is necessary to generate integrated address. This provides a strong security advantage. Services that generate integrated addresses need no access to wallet (web apps etc). In contrast, to generate a subaddress, one needs a private view key.
* No shared counter is necessary to generate integrated address. This allows individual services to independently generate integrated addresses w/o synchronizing on a common sequence. This is super important from a decoupling and ease of deployment pov. In contrast, subaddresses are generated sequentially, and so the sequence (the counter or index) is a coupling point between the wallet and all services that need to generate the address. Back to integrated addresses, note that embedded payment IDs are 64-bit. This means the space is large enough that one can simply generate them randomly and reliably assume uniqueness.
* Scenario where subaddresses improve privacy is not applicable to businesses b/c businesses have the same identity over time. In this case subaddresses provide no benefits over integrated addresses.

TL;DR: removing integrated addresses will make it harder and less secure to accept Monero directly for exchanges, payment processors, merchants, market making platforms, and other infrastructure building parties.

## fluffypony | 2019-01-25T08:52:16+00:00
@qertoip you can pre-generate a pool of 20 000 subaddresses and then just use a pool address for each transaction.

## qertoip | 2019-01-25T08:59:47+00:00
@fluffypony yes and either assume the thing will never massively catch on ;) **or** code up proper support for address pool refilling in a secure and automated way. Does not sound like ease of deployment.

Also, a pool of pre-generated addresses itself becomes a coupling point for all client services drawing from the pool. I am thinking about mature infrastructure with HA etc.

## LocalMonero | 2019-01-25T10:17:40+00:00
Our representatives won't be able to attend this discussion on IRC, unfortunately, so we'll just comment on this issue here.

We agree with @qertoip that subadresses in their current state do present some quite substantial disadvantages from a merchant point of view, except for his last point. Subadresses certainly improve privacy due to being unlinkable with each other or the base address, unlike integrated addresses. This can provide privacy when, for example, sending from one exchange to another the sending exchange will see the user sending to multiple different subaddresses and won't be able to determine that they are actually being sent to the same exchange. With integrated addresses, even when they are freshly generated, they are linkable between each other and their base wallet, hence generating a new integrated address for every deposit (like what Kraken does) is a futile exercise from a privacy standpoint since if you know Kraken's base Monero wallet address (and everyone can deduce it from the integrated deposit addresses they give you) another merchant/exchange can see from its own outgoing transaction logs who, when and how much Monero did someone send to Kraken.

We believe that unless integrated addresses present a notable privacy risk for the Monero network they should not be abolished until subaddresses can address the shared counter and private viewkey problem. If they do present a notable risk, then we believe it is in the best interests of the community to fully switch to subaddresses. It would be great to get some stats and math on the privacy aspect of having both integrated addresses and subaddresses coexist on the network vs just having subaddresses.

## SamsungGalaxyPlayer | 2019-01-25T20:56:51+00:00
Meeting logs:

https://www.irccloud.com/pastebin/gBn9b9cy/Payment%20ID%20meeting%202019.01.25

## SamsungGalaxyPlayer | 2019-01-26T23:25:33+00:00
@qertoip @localmonero have you had a chance to review the logs? Most people in the meeting recommended a move to subaddress-only.

## LocalMonero | 2019-01-27T05:37:58+00:00
@SamsungGalaxyPlayer Yes, it seems like the community decided integrated addresses are a notable privacy risk. As we've said, if they are considered to be as such, we fully support the switch to subaddresses.

## qertoip | 2019-01-27T14:12:37+00:00
Thanks @SamsungGalaxyPlayer for following up on this. Unfortunately I was not able to participate in the meeting.

I did review the logs. I don't think there was any meaningful discussion about the **cons** of removing integrated addresses, only a mention of my and localmonero concerns (thanks btw!).

The thing is these cons are only apparent and obvious if you have experience in building mature server infrastructures with focus and safety, decoupling of responsibilities, high availability, etc - kind of a CTO or systems architect perspective. This perspective is not well represented in the community.

Of course, world will not come to an end if we remove integrated addresses, but it will be yet another friction point for integrating Monero "the right way" (and not as a quick hack).

## luigi1111 | 2019-02-01T19:37:42+00:00
FYI:
[https://repo.getmonero.org/monero-project/monero-site/merge_requests/990](https://repo.getmonero.org/monero-project/monero-site/merge_requests/990)

## qertoip | 2019-02-01T21:11:48+00:00
There is one more thing. The upgrade friction for these tens of exchanges:
https://coinmarketcap.com/currencies/monero/#markets

Migrating from standalone payment IDs to **integrated addresses** is a relatively straightforward process. It does **not** require any architectural changes. Still, I would expect very many exchanges and services to suspend Monero deposits indefinitely, especially during the bear market. But nevermind that - keeping standalone payment IDs would only make things worse in the long term.

Now, migrating from standalone payment IDs to **subaddresses** may **force changes to the architecture**, which is really a show-stopper. Architectures are very expensive to change. Basically, our hope here would be that exchanges build their architectures w/o capitalizing on decoupling enabled by payment IDs. This seems like a very risky move for little gain.

We are about to break Monero public API the whole ecosystem is built upon. Let's be very careful with that.

## emesik | 2019-02-01T22:08:05+00:00
I was happy to see payment IDs gone but @qertoip's comments are sobering. Dropping them altogether means a major backward incompatibility, requiring costly adaptation from major entities, especially exchanges and merchants. This can be a huge step back.

Monero's biggest problem right now is adoption level. Our coin is not popular and changing it should be top priority. Why? Because its privacy features might come under scrutiny of governments and laws may be passed to make use of Monero harder or even illegal. The window might be closing sooner than anyone expects, and we want to gain popularity before, not after.

Telling major allies to "redesign your integration within 6 months, or get lost" is not a good way to build market in a situation when most of them do use payment IDs. If half of them had switched to subaddresses already, we could count on market competition to roll out the change. But I guess it's not the case.

Unencrypted pIDs are serious privacy leak and should be gone. However, the removal of encrypted ones could wait.

Could the time between deprecation and removal be longer?

Could we look how quickly big players react to removal of long IDs before the final decision on removal of short ones?

Perhaps incur penalty on transactions with IDs, giving economical incentive for the transfer? (I know this sounds extremely controversial.)

Or just leave them be? After all, IDs are great for generating addresses without secret keys. The clients could, however, warn users that transactions with IDs would stand out from the crowd.

## SamsungGalaxyPlayer | 2020-02-09T18:01:16+00:00
I'm closing this. Please open a new discussion if you would like to propose removing encrypted payment IDs.

# Action History
- Created by: SamsungGalaxyPlayer | 2019-01-19T16:46:08+00:00
- Closed at: 2020-02-09T18:01:16+00:00
