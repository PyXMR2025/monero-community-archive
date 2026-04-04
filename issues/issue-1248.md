---
title: 'Monero Tech Meeting #131 - Monday, 2025-08-04, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1248
author: rbrunner7
assignees: []
labels: []
created_at: '2025-08-01T18:38:18+00:00'
updated_at: '2025-08-04T18:23:16+00:00'
type: issue
status: closed
closed_at: '2025-08-04T18:23:16+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1245).


# Discussion History
## rbrunner7 | 2025-08-04T18:23:16+00:00
````
<j​effro256> Sorry I can't be in the meeting today. Not much to report except testing and review.
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1248
<j​berman> *waves*
<s​needlewoods> hey
<r​brunner7> Ok, with jeffro being excused, we can already go to the reports
<r​brunner7> I gave feedback to his review points for my peer selection PR
<r​brunner7> https://github.com/monero-project/monero/pull/9939
<sneedlewoods> +1
<s​needlewoods> I also don't have much to report, still working on CLI
<j​berman> me: ofrn has been sharing solid bug reports on the FCMP++ integration, been working through them, submit a PR to get rid of initial block hash download on wallet restore from wallet2 + fix deep reorg handling + refactor wallet2 refresh a bit (with net fewer lines from what it currently is on fcmp++-stage!) + address issues ofrn/others have shared. Also got and shared current FCMP+<clipped messag
<j​berman> + tx size and verification time figures here: https://github.com/seraphis-migration/monero/issues/44#issuecomment-3150754862
<needlewoods> +1
<r​brunner7> One very busy and productive man.
<j​berman> past week was a big week
<j​berman> ofrn's testing has been very effective and useful, I'm appreciative
<rbrunner7> +1
<r​brunner7> Any surprise in those verification time figures that are worth mentioning shortly?
<j​berman> oh also, payouts have been made to the fcmp++ contest winners! thank you to binary for that
<sneedlewoods> +1
<j​berman> 100+ input verification times are over 3s which IIRC was a bit slower than I recall expecting, but nothing crazy surprising to me at least
<j​berman> just doing the math I should've expected that though, so no not surprising
<r​brunner7> Ok, thanks. Somebody on Reddit asked for "any news" about the results of the competition. What link(s) would you give them?
<r​brunner7> The post-mortem that is somewhere?
<j​berman> jeffro helped me draft up an official announcement. I will post it shortly
<j​berman> it will be a blog post on getmonero
<j​berman> will link it in here and MRL
<r​brunner7> Splendid
<r​brunner7> My "Monero time" currently goes into patiently and seriously researching everything Qubic. Motto is "Know your enemy".
<r​brunner7> It's fascinating to see, for example, how the source of their node is about, oh, one tenth of the Monero daemon source ...
<r​brunner7> Or even smaller
<r​brunner7> Alright, anything to discuss further today?
<j​berman> monerod probably has more than 10x the amount of features + privacy adds an element of extra code to manage. Would expect the difference to be larger
<j​berman> I wonder how cuprate compares to monerod in terms of lines of code too
<r​brunner7> Sure. It's just interesting to see that a viable currency is left after cutting all that out. It barely qualifies as a cryptocurrency, but hey, can't have all :)
<r​brunner7> Yeah, the Cuprate versus C++ daemon comparison will be interesting as well.
<r​brunner7> Ok. Seems we can close. Thanks everybody for attending, read you again next week!
<j​berman> thank you!
<s​needlewoods> thanks
````


# Action History
- Created by: rbrunner7 | 2025-08-01T18:38:18+00:00
- Closed at: 2025-08-04T18:23:16+00:00
