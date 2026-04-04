---
title: 'Seraphis wallet workgroup meeting #48 - Monday, 2023-12-04, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/939
author: rbrunner7
assignees: []
labels: []
created_at: '2023-12-01T20:46:28+00:00'
updated_at: '2023-12-04T18:23:35+00:00'
type: issue
status: closed
closed_at: '2023-12-04T18:23:35+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/933

# Discussion History
## rbrunner7 | 2023-12-04T18:23:35+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/939
<d​angerousfreedom> hello
<s​needlewoods_xmr> hey
<j​berman> *waves*
<r​brunner7> So, what are the reports from last week?
<r​brunner7> Quiet week for me, Seraphis-wallet-wise
<s​needlewoods_xmr> rough week for me, but back on track since friday
<d​angerousfreedom> I just modified again the serializable enote_store considering jeffro PRs on the serialization. I'm definitely the worst programmer here but sometimes I don't know if it is me who am stupid or if Monero over complicate things. So thank you jeffro256  for making things simpler. I understand better now what function calls what and what they do with your changes. I will try to review<clipped 
<d​angerousfreedom>  it but will be away in the next 10 days. I will also review your draft on the jamtis changes when I'm back.
<j​berman> I worked mostly on monero-serai this past week (matching its decoy selection algo to wallet2's). This week I'm going to be focusing on trying to push formalization of Seraphis forwards and a bit of final monero-serai stuff so it's ready for prod, and will get back to Seraphis wallet work probably next week
<r​brunner7> Formalization of Seraphis? Where will that be used? And how will that look?
<s​needlewoods_xmr> I could maybe try to make a draft PR in the near future, but there are more questions than code changes at the moment, so not sure it would be a waste of your time and I should continue to do some more research on my own
<d​angerousfreedom> Sure! If you think something can be changed for better :)
<r​brunner7> SNeedlewoods: I wouldn't worry too much. If you don't take offense easily, if it goes towards a waste of time, what you do, we will just tell, nothing bad happened
<j​berman> rbrunner7: the idea is basically to harden the Seraphis papers with formal proofs / ideally a security model. For moer context, this is basically the scope plowsof has used to communicate with researchers: https://gist.github.com/plowsof/8cb33e2efe4bf0239927ad3bd92326e0
<r​brunner7> I see. Yeah, working towards that is certainly very welcome, and will probably be useful all around.
<r​brunner7> If you are on it couldn't you just continue a little and do the same for multisig ... :)
<j​berman> going to go back and reread the latest MRL metting on that
<r​brunner7> It's nice to see Monero going forward on several fronts at once, but hopefully in the near future the wallet will move a bit more into focus
<r​brunner7> I was only half serious, because I think multisig needs the same you seem to work towards now for Seraphis. But probably too big to just put into the same stroke
<r​brunner7> I think when jeffro256 will be through with his Jamtis improvements we will see him more often :)
<r​brunner7> Anything special to discuss today?
<d​angerousfreedom> Not from me. I think I will be able to dedicate more hours in 10 days so I could take some tasks too. Lets see.
<r​brunner7> Good to hear.
<s​needlewoods_xmr> also nothing from my side
<j​berman> ditto
<r​brunner7> Alright, looks like we are through for today. Thanks for attending everybody, take care, read you next week.
<s​needlewoods_xmr> thanks everyone, cu
<j​berman> right, the current multisig needs focused effort to move forward in its own right, and can't necessarily be grouped with other work imo
````


# Action History
- Created by: rbrunner7 | 2023-12-01T20:46:28+00:00
- Closed at: 2023-12-04T18:23:35+00:00
