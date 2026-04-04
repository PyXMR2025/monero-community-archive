---
title: 'Monero Tech Meeting #113 - Monday, 2025-03-24, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1175
author: rbrunner7
assignees: []
labels: []
created_at: '2025-03-21T13:45:38+00:00'
updated_at: '2025-03-24T18:28:08+00:00'
type: issue
status: closed
closed_at: '2025-03-24T18:28:07+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1172).

# Discussion History
## rbrunner7 | 2025-03-24T18:28:07+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1175
<s​needlewoods> hey
<j​berman> *waves*
<j​effro256> Howdy
<s​yntheticbird> hello
<r​brunner7> So, what is there to report from last week?
<s​needlewoods> I did a little side quest, with help from jberman https://github.com/monero-project/monero/pull/9863
<jeffro256> +1
<jberman> +1
<r​brunner7> Oh, I tried this yesterday, and my attempts went basically nowhere. Did you solve it then?
<j​effro256> This is my WIP branch for carrot scanning in wallet2: https://github.com/seraphis-migration/monero/pull/19/files. Most of the changes are done, and now it's time to debug / prepare HW device support
<sneedlewoods> +1
<s​needlewoods> rbrunner yes I think so, did a lot of testing on this
<r​brunner7> I did what you list there and had the error maybe 1 or 2 times out of 20. No idea why I wasn't able to reproduce reliably
<j​berman> me: implemented @jeffro256 's suggestions to trim the tree via cached right-edge in the db on reorg + delay trimming until the tree is 10 blocks ahead of the chain (more on these here: https://github.com/monero-project/monero/pull/9436#issuecomment-2519858103) which net on net removed somewhere around 1500-2k lines of code from my FCMP++ integration code
<j​berman> I also thought I had gotten the expected RPC functional transfers + blockchain tests working on my FCMP++ branch, looking again at that shortly after this meeting
<r​brunner7> I guess you deleted that much code with a laughing and a cying eye :)
<s​needlewoods> that's strange, I could reproduce it every attempt
<r​brunner7> Anyway, the important thing is that you could correct it
<j​berman> In hindsight, I think it was defensible to write the code the initial way in the first place, but with an additional look from jeffro, his suggestions were stronger. It's nice to delete code sometimes
<r​brunner7> Nice
<j​berman> should make review easier in the end too. the deleted code was the hairiest part of the integration
<r​brunner7> jeffro256: How far will you be able to go without an actual hardware device that supports FCMP++ and Carrot? Will you simulate one?
<j​effro256> Yup! Just like we currently have `hw::core::device_default`, you can make trivial in-memory devices which act like hardware devices
<r​brunner7> Anyway, it seems that both FCMP++ devs are running at full speed right now. Interesting times :)
<r​brunner7> Really time to start that contest then ... I guess that's close now?
<j​berman> +1^
<j​berman> @jeffro256 let's get that across the finish line
<j​effro256> Agreed, sorry I'll address that remaining issue
<r​brunner7> Alright. Do we have something to discuss today beyond these reports?
<r​brunner7> By the way, SNeedlewoods , impressive that you are able to correct multisig related bugs already.
<jeffro256> +1
<jberman> +1
<s​needlewoods> First I was scared, but I learned it's not that scary, at least if you do it alone lol. And jberman helped a lot :)
<j​berman> finding the root issue is the hard part, was all you there. nice work :)
<s​needlewoods> Thanks :)
<r​brunner7> Seems that we can close the meeting now. Thanks for attending everybody, read you again next week!
<s​needlewoods> thanks everyone and see you next time
````


# Action History
- Created by: rbrunner7 | 2025-03-21T13:45:38+00:00
- Closed at: 2025-03-24T18:28:07+00:00
