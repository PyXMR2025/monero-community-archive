---
title: 'Seraphis wallet workgroup meeting #20 - Monday, 2023-04-10, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/823
author: rbrunner7
assignees: []
labels: []
created_at: '2023-04-07T15:43:45+00:00'
updated_at: '2023-04-10T18:31:58+00:00'
type: issue
status: closed
closed_at: '2023-04-10T18:31:58+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #820

We will see who will be around, because Easter. I will in any case be in the room at the hour.

# Discussion History
## rbrunner7 | 2023-04-10T18:31:58+00:00
````
<rbrunner7[m]> Meeting in a bit more than 1 hour
<rbrunner7[m]> Hey, meeting time already :) Will be fully present in about 2 Minutes
<rbrunner7[m]> Alright! Somebody else here with me, or still enjoying Easter holiday?
<rbrunner7[m]> https://github.com/monero-project/meta/issues/823
<jberman[m]> I'm here
<jberman[m]> howdy
<rbrunner7[m]> dangerousfreedom[m] is definitely away until about end of month
<rbrunner7[m]> Unfortunately he did not have time to still PR's his recent work so we can easily comment. But I had a look anyway already.
<rbrunner7[m]> jberman: Do you happen to know whether UkoeHB explained somewhere the general approach, the "philosophy" behind those versioned classes that dominate the Seraphis library, all those with "V1" at the end of the name?
<rbrunner7[m]> So we will know when and how (or when not) to extend that to Seraphis wallet classes? 
<jberman[m]> I've run into it mostly with enotes (which already have LegacyEnoteV1 - V5) and IIRC the idea is to enable/encourage clearer code separation when working with older versions, rather than have massive functions that have branch conditions nested within them that do related things
<rbrunner7[m]> Yeah, pretty clear. I am wondering also what possible scenarious he thought through how this may develop into the future, if Jamtis evolves, if Seraphis evolves. Maybe I will ask more clearly in the coming days. Could be valuable guidance for us, I think.
<rbrunner7[m]> dangerousfreedom[m] now made a `SpTransactionStoreV1`, but I am not sure whether this is appropriate or not.
<rbrunner7[m]> Alright, I think we will have the shortest meeting ever until now, with so many people enyoying a break!
<rbrunner7[m]> An announcement in advance, maybe people will see it later: In 2 week, I will be away for 3 weeks. I won't be able to manage any meeting on April 24, May 1 and May 8.
<jberman[m]> I see what you're saying. Ya would be interesting to have a better idea why a lot of classes are given v1 when no v2 exists yet
<rbrunner7[m]> Who knows, maybe koe has this planned out for years to come, like a chess player that thinks X moves ahead :)
<jberman[m]> general update on my end: I'm still working through pointing koe's optimized scanner to a local daemon. been running into annoying bugs, but almost finished with it
<rbrunner7[m]> Bugs in which code?
<jberman[m]> building off this pointing it to a local daemon: https://gist.github.com/UkoeHB/4b3528a5c3a3134bd82d19a2bc6a8e87
<rbrunner7[m]> I see. I guess you find your way around the library quite well already?
<jberman[m]> I'd say yes, it's easier to navigate and find what I need when I have a focused task
<rbrunner7[m]> Good to hear. I have a bit of envy that I myself probably won't be able to go into programming anytime soon here. It's tempting, but that's probably a way into burnout at the moment ...
<rbrunner7[m]> Alright, thanks for the chat, jberman . Until next week!
<UkoeHB> I erred on the side of 'maybe it will be needed' when versioning everything
<UkoeHB> stuff like the enote store and other caches don't need to be versioned
````


# Action History
- Created by: rbrunner7 | 2023-04-07T15:43:45+00:00
- Closed at: 2023-04-10T18:31:58+00:00
