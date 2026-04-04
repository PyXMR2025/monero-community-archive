---
title: Monero Research Lab Meeting - Wed 20 September 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/897
author: Rucknium
assignees: []
labels: []
created_at: '2023-09-19T21:49:50+00:00'
updated_at: '2023-09-27T14:35:24+00:00'
type: issue
status: closed
closed_at: '2023-09-27T14:35:24+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#894 

# Discussion History
## plowsof | 2023-09-20T18:51:17+00:00
Logs 
```
17:01:13 <Rucknium> Meeting time! https://github.com/monero-project/meta/issues/897

17:01:22 <Rucknium> 1) Greetings

17:01:35 <tevador> Hi

17:01:49 <rbrunner> Hello

17:02:04 <m-relay> <v​tnerd:monero.social> Hi

17:03:06 <m-relay> <m​urksombra:matrix.org> hi!

17:03:39 <Rucknium> 2) Updates. What is everyone working on?

17:04:30 <m-relay> <v​tnerd:monero.social> me: finished testing up P2P+SSL, and pushed a PR. Also working on
subaddresses (more this week than last)

17:05:03 <m-relay> <v​tnerd:monero.social> cryptogrampy: made some good comments (on subaddresses+LWS) that I
will address

17:05:26 <Rucknium> I finished the draft of the discussion note: "Formula for Accuracy of Guessing Monero Real
Spends Using Fungibility Defects" https://github.com/Rucknium/misc-research/blob/main/Monero-Fungibility-
Defect-Classifier/pdf/classify-real-spend-with-fungibility-defects.pdf

17:05:55 <tevador> jeffro256 and I have been working on a proposal to change the Jamtis specs to improve the
privacy for users of 3rd party scanners.

17:06:26 <m-relay> <m​urksombra:matrix.org> me: joined yesterday. Catching up with current developments and
see where I can contribute.

17:06:59 <Rucknium> m​urksombra: Welcome! Do you have a specific area you are interested in?

17:07:15 <m-relay> <v​tnerd:monero.social> tevador: where is this discussion taking place? I need to at least
watch the discussion for LWS purposes

17:07:54 <m-relay> <m​urksombra:matrix.org> I can help from coffee to cryptography :)

17:07:55 <tevador> The (incomplete, work in progress) proposal and discussion is here: https://gist.github.com
/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4692457#gistcomment-4692457

17:07:57 <m-relay> <m​urksombra:matrix.org> mostly cryptography I should say :)

17:08:19 <rbrunner> You can never have enough cryptographers, it seems sometimes :)

17:08:56 <rbrunner> Er, *too many

17:09:02 <Rucknium> m​urksombra: Great. The main cryptography things happening are Seraphis/Jamtis and Full
Chain Membership Proofs using Curve Trees

17:09:44 <m-relay> <m​urksombra:matrix.org> ack. will check.

17:10:58 <m-relay> <m​urksombra:matrix.org> but again, I can war multiple hats and contribute in other areas
as well. Hardening, OPSec yadda yadda

17:11:23 <Rucknium> 3) Discussion. What do we want to discuss?

17:13:33 <rbrunner> Maybe, as tevador is here, a question from me

17:13:41 <Rucknium> tevador: Do you want to summarize the main points you want feedback for the changes to
Jamtis specs?

17:13:53 <rbrunner> Right, that was also my question :)

17:14:20 <rbrunner> Where do we stand with that? Still fully open? Slowly converging towards an improved
Jamtis?

17:14:58 <tevador> OK. The proposal is to introduce "dynamic view tags", which adjust according to tx volume,
plus to remove some privacy leaks from the current specs.

17:16:01 <tevador> The current Jamtis spec leaks to the 3rd party scanner any outputs that have been received
to a reused address and also outputs received to publicly known addresses.

17:16:59 <tevador> Also the current spec has a fixed 8-bit view tag and some people noted that if tx volume
increased dramatically, 3rd party scanners would become useless.

17:17:41 <tevador> Or more likely would have to switch to a less private wallet tier.

17:18:37 <Rucknium> I would predict that some 3rd party scanner services would implement just one static
receive address, so the privacy improvements there are a good idea.

17:20:29 <tevador> The proposal would increase address length from 196 to 244 characters, but that's still
withing an acceptable range.

17:20:41 <Rucknium> The dynamic view tag size will be determined by a formula in monerod's code that
automatically adjusts so no software update needed when tx volume rises, right?

17:20:46 <rbrunner> So the two view tags with different sizes, as already put into code by jeffro256, morphed
into a single view tag, but with variable, adjusting size?

17:21:30 <tevador> Yes, the view tag size adjusts automatically by using a formula based on the number of
outputs in the last 100 000 blocks.

17:21:46 <Rucknium> Addresses do not change when the view tag size changes, right? So an address would be
valid both before and after adjustment?

17:22:11 <tevador> No, only the view tag inside transactions changes.

17:22:41 <tevador> It's meant to adjust to follow long-term tx volume.

17:23:04 <tevador> 100 000 blocks is also what the block size limit is based on

17:24:39 <rbrunner> About 4 months

17:24:59 <tevador> I will post more details later, but for example, between 2018 and 2023, the view tag would
have grown from 4 bits to 6 bits (with a period of 7 bits during the spam attack last year).

17:25:54 <tevador> The size is adjusted for 1 false positive per block on average.

17:27:28 <Rucknium> What is "one false positive per block"?

17:28:01 <tevador> Besides the outputs you own, the view tag will also match, on average, 1 output per block
that you don't own.

17:28:02 <rbrunner> A tx sent to somebody as "probably yours" but turning out not be such?

17:28:51 <rbrunner> Over all tx receivers of the block, right?

17:29:27 <tevador> Every wallet will calculate a different view tag for every output, but on average, everyone
will see 1 false match per block.

17:29:45 <tevador> This is done to hide your real outputs from the 3rd party scanner.

17:30:05 <rbrunner> Ah, ok

17:30:36 <Rucknium> Dynamic view tag size good to me on first hearing it :). The point of debate to the new
changes will probably the "is more privacy for 3rd party scanning worth adding 48 characters to an address?"
question.

17:30:42 <tevador> The 3rd party scanner will send all matches to your wallet, so you have to scan only 720
outputs per day.

17:31:09 <rbrunner> Is this a new idea? Making the view tags *less* precise?

17:32:04 <tevador> I think so. View tags that are too precise would basically leak your outputs to the 3rd
party scanner.

17:32:52 <rbrunner> I mean was this already a consideration when we came up with the current 1-byte view tag?
Maybe not

17:33:48 <tevador> The difference is that whoever can calculate the current 8-bit tag can also fully recognize
owned outputs. That changes with Jamtis.

17:34:20 <tevador> Jamtis has one key that can only calculate view tags. Another key is used to actually
calculate if the output key is yours.

17:34:39 <rbrunner> I see

17:35:21 <tevador> There are basically 3 different levels of "view only" wallet rather than just one level.

17:36:02 <rbrunner> Does sound quite attractive, that dynamically sized view tag.

17:36:05 <Rucknium> UkoeHB said in the Sept 11 No Wallet Left Behind meeting:

17:36:16 <Rucknium> "Planning for users who need 2-byte filters in order to use monero is planning for users
who cannot use monero AT ALL without a light wallet server, which is not a situation we should aim for. Local
scanning is a first class citizen, and if a user can't local scan then they are out of our design space."

17:36:42 <Rucknium> Is there general agreement on this point: "if a user can't local scan then they are out of
our design space"?

17:37:40 <tevador> The dynamic tag has a range 1-16 bits. The 16-bit size is probably unrealistic, would need
around 65k outputs *per block*, but that's future-proofing I guess.

17:38:38 <rbrunner> I think it's a bit hard to find the proper context of that opinion stated by UkoeHB

17:39:09 <rbrunner> There was much back-and-forth discussion by him and jeffro256 about this

17:39:44 <rbrunner> with a large numbers of different arguments

17:39:49 <tevador> The benefit of the dynamic tag is that 1) Users of remote scanners get to keep some
privacy. 2) Users of remote scanners only have to download about 200 KB per day. Basically instant sync.

17:41:10 <rbrunner> You could argue in the extreme that currently a rarely used smartphone Monero wallet
borders on unsusable, because of the long time to catch up without any third-party scanning support

17:41:43 <rbrunner> E.g. don't use for a few months, wait hours until synced again

17:42:08 <Rucknium> I don't think it will be hard to document it since it seems like a simple rule, but please
document the formula/algorithm well if it's planned for implementation so "third party" wallets know what to
do :)

17:43:00 <tevador> Yes, our goal is to have a precise specification.

17:43:07 <rbrunner> Including the times around switching bit size, which may be a bit tricky

17:43:15 <Rucknium> because I know a lot of them don't know what to do with fees.

17:43:44 <rbrunner> Well, maybe they are just lazy to implement it properly :)

17:45:12 <tevador> Yes, we don't want the tag size to create anonymity puddles, so the size will be enforced
by a relay rule.

17:45:33 <Rucknium> which is a good segue into https://github.com/Rucknium/misc-research/blob/main/Monero-
Fungibility-Defect-Classifier/pdf/classify-real-spend-with-fungibility-defects.pdf

17:45:36 <tevador> Wallets that cut corners and hardcode the size won't work.

17:46:22 <Rucknium> I'll quote the main point from the abstract:

17:46:40 <Rucknium> "Using basic probability concepts I develop a closed-form expression for the probability
that the classifier correctly classifies a ring member as the real spend. This probability, the Positive
Predictive Value (PPV) is a function of ring size, the probability that a user spends change in a ring, and
the proportion of transaction outputs on the

17:46:41 <Rucknium> blockchain that have the defect."

17:46:57 <Rucknium> "For example, when these values are 16, 40%, and 5%, respectively, the probability that
the classifier correctly classifies a ring member as the real spend is 31.7%, much higher than the 1/16 =
6.25% probability of randomly guessing between the 16 ring members."

17:47:42 <Rucknium> Table 1 has a lot more possible value for probability of spending change and proportion of
outputs with the defect. Table 2 does the same for ring size 128

17:48:42 <Rucknium> I think this is a nice little contribution. For years there has been a worry about how
much tx fungibility defects are affecting user privacy. Now we can put specific numbers on it.

17:49:07 <rbrunner> Agree

17:49:46 <Rucknium> If there is some tradeoff between requiring more transaction format strictness and some
other goal, we can weigh the options with the estimated privacy benefits.

17:51:27 <Rucknium> What's in the note isn't quite mathematical proofs of the formula, but it's pretty close.
Assuming I didn't make an algebra mistake ;)

17:52:23 <Rucknium> I wrote a Monte Carlo simulation, too, and it gives the same values (within epsilon) as
the closed-form expression I developed.

17:52:52 <tevador> Hopefully, these problems will disappear with full chain membership proofs.

17:53:10 <tevador> Or at least be much less severe.

17:53:20 <m-relay> <m​urksombra:matrix.org> is this public?

17:53:52 <Rucknium> Yes, much less severe. Only really rare defects would be a problem with full chain
membership proofs.

17:54:38 <Rucknium> m​urksombra: My discussion note? Yes: https://github.com/Rucknium/misc-
research/blob/main/Monero-Fungibility-Defect-Classifier/pdf/classify-real-spend-with-fungibility-defects.pdf

17:54:51 <m-relay> <m​urksombra:matrix.org> ty

17:58:08 <Rucknium> Feel free to type any comments or questions about the discussion note here in the MRL
channel. We're almost at the end of the hour, so let's end the meeting here.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-09-19T21:49:50+00:00
- Closed at: 2023-09-27T14:35:24+00:00
