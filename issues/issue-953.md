---
title: 'Seraphis wallet workgroup meeting #52 - Monday, 2024-01-08, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/953
author: rbrunner7
assignees: []
labels: []
created_at: '2024-01-05T17:01:26+00:00'
updated_at: '2024-01-08T18:27:22+00:00'
type: issue
status: closed
closed_at: '2024-01-08T18:27:22+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/950

# Discussion History
## rbrunner7 | 2024-01-08T18:27:22+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/953
<SNeedlewoods> hey
<jberman> howdy
<rbrunner7> So, now with the festivities definitely behind us, what is there to report?
<SNeedlewoods> added EnoteRecords to https://github.com/seraphis-migration/strategy/wiki/Seraphis-Documentation even if no one else will ever use the doc, at least it helps me solidify my understanding
<dangerousfreedom> Hello!
<jeffro256> Howdy 
<SNeedlewoods> and I made pretty good progress on my PR, been working on the tests which isn't too hard but laborious
<jeffro256> +1
<jberman> +
<rbrunner7> Nice to see your steady progress, 
<jeffro256> I'm just doing research about wallet design, collecting and comparing different APIs, looking at requirements
<jberman> +1
<rbrunner7> Love to hear that.
<jberman> Still working on tightening the final fingerprint edges in monero-serai, but very close to done with that. I'm hoping I'll be done today/tomorrow, then back to continuing in here
<rbrunner7> Plenty of good news then in the new year. Will this be the year that serai will go live, or is that not yet fully sure?
<dangerousfreedom> SNeedlewoods: definitely it is worth documenting it. Thanks!
<SNeedlewoods> +1
<jberman> pinging kayabanerve to speak on that for serai. monero-serai in particular (a monero wallet lib) I think should definitely be ready for use in production much sooner than end of year
<rbrunner7> That was just my curiosity, not very close to all things Seraphis :)
<rbrunner7> Anything in particular to discuss in this round today?
<rbrunner7> Does not seem to be the case. Well, less meeting, more time to code :)
<dangerousfreedom> From my side, I have started working on creating the basic functions to open a wallet and load the keys. I'm working on ghostway's KeyContainer to address some issues and will ask for ghostway's
<dangerousfreedom>'opinion and your reviews on the next couple days. I'm willing to let it with the same security level that we have today (using cn_slow_hash and chacha) but will document all the steps (using the same page as SNeedlewoods is using) and leave it in a way that we can easily replace to argon2 if we decide that (will also try to implement it if we have it in our library).
<ghostway> Generate_chacha_key is using cn_slow_hash directly... That's basically the whole function 
<ghostway> But sure 
<rbrunner7> So maybe soon we will have a thing to play with a bit.
<ghostway> If you need anything I'm here. Trying to grasp bulletproofs :)
<rbrunner7> Alright. Thanks for attending, read you next week!
<SNeedlewoods> exciting stuff going on here, thanks everyone
````


# Action History
- Created by: rbrunner7 | 2024-01-05T17:01:26+00:00
- Closed at: 2024-01-08T18:27:22+00:00
