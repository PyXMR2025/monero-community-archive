---
title: 'Seraphis wallet workgroup meeting #35 - Monday, 2023-09-04, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/889
author: rbrunner7
assignees: []
labels: []
created_at: '2023-09-01T19:07:39+00:00'
updated_at: '2023-09-04T18:36:18+00:00'
type: issue
status: closed
closed_at: '2023-09-04T18:36:18+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/885

# Discussion History
## rbrunner7 | 2023-09-04T18:36:18+00:00
```
<g​hostway> Hello
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/889
<g​hostway> I've submitted the pr
<g​hostway> For the key container, finally
<r​brunner7> Hurray!
<d​angerousfreedom> Hello
<j​berman> hello
<g​hostway> https://github.com/seraphis-migration/monero/pull/5
<g​hostway> Anyone welcome to comment and review
<g​hostway> Everyone"
<r​brunner7> Alright, anybody else with a report beside ghostway , for last week?
<d​angerousfreedom> I wrote [this issue](https://github.com/seraphis-migration/wallet3/issues/59). If you look at the Seraphis lib, it makes total sense to show enotes [directly](https://github.com/DangerousFreedom1984/seraphis_lib/blob/show_enotes/src/seraphis_wallet/show_enotes.cpp) instead of showing transactions, like it is done on [wallet2](https://github.com/monero-project/monero/blob/master/src/simplewallet/simplewallet.cpp#L8301). Feel free to give your opinions.
<g​hostway> That does sound better, just by hearing the idea
<r​brunner7> Will hopefully come around to comment soon. This is an issue with an almost incredible number of facettes, IMHO.
<d​angerousfreedom> Cool! I will take a look and probably starting using it if I need.
<d​angerousfreedom> True. Thats why I wanted to open discussions and not only do the way I think I should.
<r​brunner7> A question into the round: Do you all get informed by e-mail about such new PRs to "our" own wallet dev repo? I think it would be a good idea if that was the case for all people doing dev work here.
<r​brunner7> And to the opening of new issues of course as well.
<d​angerousfreedom> I dont but I check often.
<j​berman> just started watching the repo to get notified
<r​brunner7> Maybe only members of the project, or members of the repo, get e-mails?
<r​brunner7> Ah, ok, you can also "watch" it?
<j​berman> yep
<r​brunner7> Alright, good to know
<r​brunner7> I am currently the owner of all that stuff, I get everything anyway ...
<r​brunner7> I am new in this role of Monero dev project overlord :)
<j​berman> my update: I've been working on non-Seraphis background wallet sync PR 8619 and should be done with the latest changes in the next 2 days. Hoping to get over to full chain membership proof work next. Will review ghostway 's PR too, looks nice on first glance
<r​brunner7> Judging on the questions that jeffro256 made here over the last week he is in very deep in implementing his proposed Jamtis enhancement. Looks like he may making progress there, from the outside.
<g​hostway> I should make my summary going and put it through kayabanerve (probably won't be too math-y, even though it's the cool part)
<r​brunner7> jberman: Any estimate how long you will make that FCMP phase of yours?
<j​berman> I'd say hopefully 2-3 weeks but will get back to you once I get going on it :)
<r​brunner7> Ok, that doesn't sound too bad. Soon we will also know whether that "retroactive" CCS will go ahead or not. The tension is almost unbearable.
<r​brunner7> I guess if that goes through that will be good for motivation, at least.
<j​berman> hah, no tension from me. I get it
<r​brunner7> Maybe we will have UkoeHB back here soon, coming out of his Monero break.
<r​brunner7> ghostway: Not sure what you mean with "my summary". Can you elaborate a bit?
<g​hostway> Started writing a summary of curve trees but stopped, even though that might be helpful
<g​hostway> Because well, my rate is way less than 100 USD/hour
<r​brunner7> Sound interesting, but also quite ambitious to me as a crypto-noob
<r​brunner7> Could be useful for Reddit also, if it indeed comes out not too "math-y" as you said
<r​brunner7> Maybe we could also start with monthly or bi-monthly posts there to inform about our progress, old idea from one of the first meetings
<g​hostway> Might be followed by some of kayaba's code -- currently explored some of it
<r​brunner7> Alright. Anything else for today's meeting?
<d​angerousfreedom> I believe I'm approaching the end of my CCS (after a small accident on the way) so I will try to wrap and clean everything up on the next weeks and I will be looking for potential next tasks too. I'm learning more about networks and how the daemon works. Looks like this part will be a big construction site too.
<r​brunner7> How time flies.
<r​brunner7> Yeah, the daemon, and simplewallet, and the RPC server, and and and ...
<r​brunner7> But first we need a wallet :)
<d​angerousfreedom> Not sure anymore :p
<d​angerousfreedom> The daemon is coded everywhere on the wallet, we will get blocked at some point :p
<r​brunner7> Right. If somebody codes the handling of Seraphis transactions into the daemon, that would be very welcome.
<r​brunner7> And needed at some point, as you say.
<r​brunner7> Well then, I think we can close. Thanks for attending, read you next week.
<d​angerousfreedom> Yeah, thats what I was thinking about doing next. Writing the wallet function 'transfer' and see what needs to be done on the daemon side
<d​angerousfreedom> Thanks rbrunner7
<g​hostway> Thanks!
<j​berman> thanks :)
```


# Action History
- Created by: rbrunner7 | 2023-09-01T19:07:39+00:00
- Closed at: 2023-09-04T18:36:18+00:00
