---
title: Monero Research Lab Meeting - 24 February 2021 @ 17 UTC
source_url: https://github.com/monero-project/meta/issues/553
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2021-02-24T15:52:41+00:00'
updated_at: '2021-02-24T18:38:54+00:00'
type: issue
status: closed
closed_at: '2021-02-24T18:38:54+00:00'
---

# Original Description
Time: 17 UTC

Location: #monero-research-lab

Main discussion topics:
* BP+ second audit
* monero-project/research-lab#70 (comment)

Second audit SoWs:

[Quarkslab.pdf](https://github.com/monero-project/meta/files/6037184/PRO_Quarkslab_Monero_Bulletproof_RPS_security_assessment_public.pdf)
[JP.pdf](https://github.com/monero-project/meta/files/6037185/bpplus-review-sow.pdf)


# Discussion History
## SamsungGalaxyPlayer | 2021-02-24T18:38:54+00:00
```
[2021-02-24 11:00:59] <sgp_> Monero Research Lab meeting time
[2021-02-24 11:01:59] <sgp_> ping ArticMine sarang knaccc DeanWeen Isthmus SerHack vtnerd xmrscott
[2021-02-24 11:02:26] <sgp_> I know this wasn't scheduled much in advance, but we need to make a decision on BP+ today
[2021-02-24 11:02:36] <Isthmus> hey, I'm partially around
[2021-02-24 11:02:37] <sgp_> (ideally regarding the audit because we now have SoWs)
[2021-02-24 11:03:45] <sgp_> https://github.com/monero-project/meta/issues/553
[2021-02-24 11:03:55] <sgp_> first up, BP+ second audit
[2021-02-24 11:04:36] <sgp_> we have received 2 SoWs
[2021-02-24 11:05:04] <sgp_> TrailofBits may be submitting one, but it's been a few weeks and we don't have it yet. They are also not likely available in the short term
[2021-02-24 11:05:11] <sgp_> Quarkslab: https://github.com/monero-project/meta/files/6037184/PRO_Quarkslab_Monero_Bulletproof_RPS_security_assessment_public.pdf
[2021-02-24 11:05:19] <sgp_> JP: https://github.com/monero-project/meta/files/6037185/bpplus-review-sow.pdf
[2021-02-24 11:08:26] ⇐ lef quit (~drlef@p200300fd07011a0591292f19c946e599.dip0.t-ipconnect.de): Read error: Connection reset by peer
[2021-02-24 11:08:52] → drlef joined (~drlef@p200300fd07011a0591292f19c946e599.dip0.t-ipconnect.de)
[2021-02-24 11:10:22] <sgp_> wow, silence lol
[2021-02-24 11:10:41] → x3nu[m] joined (x3numatrix@gateway/shell/matrix.org/x-exzdtqabmvqnbwps)
[2021-02-24 11:10:56] → rj_ joined (~x@gateway/tor-sasl/rj)
[2021-02-24 11:10:59] <SerHack> hey!
[2021-02-24 11:11:05] <sgp_> hey serhack :P
[2021-02-24 11:11:24] <sgp_> here's what's next for the audit to proceed
[2021-02-24 11:11:28] <sgp_> 1. we need to pick one
[2021-02-24 11:11:48] <DisBotXMR1> <glennhodl> im interested I just have no idea what's going on, so just observing
[2021-02-24 11:11:56] <sgp_> 2. I need to confirm with MAGIC that we can open a campaign for this (likely)
[2021-02-24 11:11:59] <SerHack> +1 for JP, I chatted for a while with him and he seems really expert, I wonder about deadline
[2021-02-24 11:12:16] <sgp_> JP says he is available within the next 1-2 weeks
[2021-02-24 11:12:26] <sgp_> we can have an audit report in 3 weeks
[2021-02-24 11:12:29] <gingeropolous> woof that quarkslab
[2021-02-24 11:12:30] <sgp_> from today
[2021-02-24 11:12:35] <SerHack> I see
[2021-02-24 11:13:09] <SerHack> and what about quarkslab?
[2021-02-24 11:13:16] <sgp_> I think Quarkslab is a good choice, but I have a lot of confidence in JP and think he is a great choice personally
[2021-02-24 11:13:53] <sgp_> JP is also <1/3 the cost
[2021-02-24 11:13:56] <gingeropolous> who / what is JP?
[2021-02-24 11:14:20] <sgp_> gingeropolous: https://www.aumasson.jp/
[2021-02-24 11:14:58] <sgp_> JP led this Monero bulletproofs audit https://research.kudelskisecurity.com/2018/07/23/audit-report-of-moneros-bulletproofs-integration/
[2021-02-24 11:15:06] → somni[m] joined (M0komomatr@gateway/shell/matrix.org/x-qffgeznkcmpcvvsc)
[2021-02-24 11:15:39] <sgp_> JP also audited CLSAG https://ostif.org/wp-content/uploads/2020/07/ostif-clsag-audit-final-public.pdf
[2021-02-24 11:18:00] — xmrscott[m]1 attempts to slide into meeting quietly
[2021-02-24 11:19:45] <h4sh3d[m]> JP is a really good choice
[2021-02-24 11:20:16] <sgp_> imo, with his expertise and immediate availability, we jump on it
[2021-02-24 11:21:31] <sgp_> and we would do it through magic so we can send him a check in USD, and USD and XMR donations would be tax deductible
[2021-02-24 11:21:31] ⇐ drlef quit (~drlef@p200300fd07011a0591292f19c946e599.dip0.t-ipconnect.de): Read error: Connection reset by peer
[2021-02-24 11:21:35] → lef joined (~drlef@p200300fd07011a0591292f19c946e599.dip0.t-ipconnect.de)
[2021-02-24 11:21:49] <gingeropolous> so that'll be 2 total audits so far?
[2021-02-24 11:22:00] <gingeropolous> if JP is selected?
[2021-02-24 11:22:02] <sgp_> the original plan was to do 2
[2021-02-24 11:22:20] <sgp_> yeah, JP's will build on the previous one which was quite extensive
[2021-02-24 11:24:10] <gingeropolous> ok. my general gut feeling is to not skimp on this, mainly because of all the "mOneRo prIntS iNfIniTe mOneY", but thats not really technical or scientifically based opinion.
[2021-02-24 11:24:21] <dEBRUYNE> I'd do JP, seems like a suitable candidate + availability
[2021-02-24 11:25:03] <sgp_> gingeropolous: I think a third is relatively excessive personally, but obviously security is important
[2021-02-24 11:25:41] <sgp_> first audit: https://suyash67.github.io/homepage/assets/pdfs/bulletproofs_plus_audit_report_v1.1.pdf
[2021-02-24 11:26:18] <gingeropolous> right. at what point is it just throwing money at a problem just because. i dunno.
[2021-02-24 11:28:08] <sgp_> is there anyone here that feels strongly that we need a third?
[2021-02-24 11:28:20] <gingeropolous> it's good that this is iterative though. can always assess after JP whether a third is warranted.
[2021-02-24 11:29:02] <sgp_> is there anyone against me opening the fundraising campaign for JP ASAP?
[2021-02-24 11:29:22] <h4sh3d[m]> I'd go for assessing after JP, if the time frame allows it
[2021-02-24 11:29:50] <h4sh3d[m]> but that's not something we want to rush anyway
[2021-02-24 11:31:49] ⇐ tobtoht quit (~tobtoht@gateway/tor-sasl/tobtoht): Remote host closed the connection
[2021-02-24 11:32:06] → tobtoht joined (~tobtoht@gateway/tor-sasl/tobtoht)
[2021-02-24 11:32:18] <xmrscott[m]1> Sounds like no one is against then
[2021-02-24 11:32:32] <xmrscott[m]1> *against doing the JP campaign ASAP
[2021-02-24 11:33:06] <sgp_> okay, I will talk with MAGIC and open a fundraising campaign for JP's audit pending board approval
[2021-02-24 11:33:20] <sgp_> if MAGIC can't do it, I'll let you know ASAP and open a CCS
[2021-02-24 11:34:08] <Isthmus> Thanks for coordinating this
[2021-02-24 11:34:33] <sgp_> ty to sarang also for sitting on some of the auditor calls with me :)
[2021-02-24 11:34:48] <sgp_> is ArticMine here to talk about the block size / fee penalty?
[2021-02-24 11:36:50] <sgp_> any other MRL topics for this meeting?
[2021-02-24 11:40:09] ← rj_ left (~x@gateway/tor-sasl/rj): 
[2021-02-24 11:40:21] → kowalabearhugs joined (c636854a@static-198-54-133-74.cust.tzulo.com)
[2021-02-24 11:43:58] → nssy2 joined (~nssy@154.159.238.13)
[2021-02-24 11:45:12] → rj_ joined (~x@gateway/tor-sasl/rj)
[2021-02-24 11:45:51] ⇐ rj_ quit (~x@gateway/tor-sasl/rj): Remote host closed the connection
[2021-02-24 11:46:04] ⇐ kowalabearhugs quit (c636854a@static-198-54-133-74.cust.tzulo.com): Quit: Connection closed
[2021-02-24 11:46:14] → rj_ joined (~x@gateway/tor-sasl/rj)
[2021-02-24 11:46:14] → Adidas joined (~Harold4@192.145.118.117)
[2021-02-24 11:46:19] <sgp_> okay, meeting adjourned then :)
```

# Action History
- Created by: SamsungGalaxyPlayer | 2021-02-24T15:52:41+00:00
- Closed at: 2021-02-24T18:38:54+00:00
