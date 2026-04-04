---
title: 'Seraphis wallet workgroup meeting #19 - Monday, 2023-04-03, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/820
author: rbrunner7
assignees: []
labels: []
created_at: '2023-04-01T16:01:27+00:00'
updated_at: '2023-04-03T18:29:55+00:00'
type: issue
status: closed
closed_at: '2023-04-03T18:29:54+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #816

I am musing about some issues regarding project management but not yet sure I will have something to bring up already this coming Monday.

# Discussion History
## plowsof | 2023-04-01T22:09:25+00:00
We have 2 open Serpahis CCS ideas. Would be good to share opinions (if any) on / invite other contributors to consider making a CCS themselves:
- Dangerous freedom: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377 
- Koe: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/384

Also Josh Babbs task (no  progress update so far) https://bounties.monero.social/posts/75/6-500m-blake2b-c-dev-challenge-seraphis Hopefully we can get an update from Josh

## rbrunner7 | 2023-04-03T18:29:54+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/820
<dangerousfreedom> Hello
<UkoeHB> hi
<ghostway[m]> Hello
<rbrunner7[m]> Any progress reports since last week's meeting?
<dangerousfreedom> Not from my side
<rbrunner7[m]> Nothing heard from jberman for some time ...
<JoshBabb[m]> Just minor, same, sorry :)
<dangerousfreedom> I will try to write something during the week
<JoshBabb[m]> same to that ^
<jberman[m]> Still working through using koe's latest changes to the scanning code in a scanner that points to a local daemon, nothing to report on my end
<ghostway[m]> I've made the key container with jamtis' constructs. Nothing much to show yet, but I'd love to discuss a comprehensive, "approved" Todo so I and others can work on stuff
<rbrunner7[m]> Yeah, we had some interesting discussion in a "Todo list" issue that dangerousfreedom[m]  started. In the spirit of some "rapid prototyping approach" I tried to sketch an absolutely minimalistic wallet there that we could use as the starting point for design discussions, and for fleshing it out in iterations: https://github.com/seraphis-migration/wallet3/issues/53#issuecomment-1489148840
<UkoeHB> I made a new CCS https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/384, started updating the seraphis paper
<rbrunner7[m]> That paper had to be patient for quite a while :)
<rbrunner7[m]> Feel free to comment on the CCS of UkoeHB, and also that of dangerousfreedom[m] . These things live on good feedback.
<rbrunner7[m]> Er, the CCS proposals of course
<rbrunner7[m]> Anything specific to discuss today from some side?
<UkoeHB> not from me
<rbrunner7[m]> I think regarding things "To do", ghostway won't be wrong if they implement a key container.
<rbrunner7[m]> A first version of it, in any case :) Who knows how many times we will refine that.
<rbrunner7[m]> If nothing else is hot right now, I would like to tell some of my recent thoughts regarding comments to this round
<rbrunner7[m]> When I first looked at the Seraphis library quite a while ago already, I immediately noticed something that probably every dev does likewise:
<rbrunner7[m]> It has a lot of comments.
<rbrunner7[m]> I would estimate maybe the "raw rate" of comment lines versus code lines is somewhere maybe at 1 to 4
<rbrunner7[m]> Compare that with other large parts of the Monero codebase, especially wallet2 :)
<rbrunner7[m]> From this first look at the library I got a gut feeling about these comment: "Nice, but maybe a tad excessive".
<rbrunner7[m]> Then something funny happened about a week ago when I looked at code I wrote in my dayjob: It had almost exactly the same level of commenting!
<rbrunner7[m]> Why? It's code that sits right at the center, at the core of a big library.
<rbrunner7[m]> Many people will probably read it in the future, and also modify it.
<rbrunner7[m]> More or less a role that the Seraphis library also has.
<rbrunner7[m]> That could will live maybe 10 years or longer, and scores of people will read it and try to understand it
<rbrunner7[m]> In short: Such code parts are better commented to such a level.
<rbrunner7[m]> I therefore propose that we try to reach a similar level of detail in commenting our wallet code.
<rbrunner7[m]> Thoughts?
<jberman[m]> +1 I like detailed comments
<rbrunner7[m]> By the way, last October I tried to give some ideas about how to find out what profits most from which kinds of comments, here: https://github.com/seraphis-migration/wallet3/issues/26#issuecomment-1296261119
<dangerousfreedom> Yeah, I think it is pretty good the level of comments. Initially it was hard to me to do that but now I think this is the best way to do it
<rbrunner7[m]> Good to hear. Putting this into practice may need some effort. Mentally prepare yourself for me bitching after PR's "But his has only about 0.6 times the level of details in comments that we try to achieve as our quality standard set by the Seraphis lib".
<rbrunner7[m]> Alright, if that's it already for today, we may close the meeting early.
<rbrunner7[m]> Thanks everybody for attending!
<dangerousfreedom> Thanks rbrunner7[m]
<ghostway[m]> Thanks
````


# Action History
- Created by: rbrunner7 | 2023-04-01T16:01:27+00:00
- Closed at: 2023-04-03T18:29:54+00:00
