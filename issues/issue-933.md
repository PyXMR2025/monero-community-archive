---
title: 'Seraphis wallet workgroup meeting #47 - Monday, 2023-11-27, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/933
author: rbrunner7
assignees: []
labels: []
created_at: '2023-11-24T16:56:10+00:00'
updated_at: '2023-11-27T18:19:22+00:00'
type: issue
status: closed
closed_at: '2023-11-27T18:19:22+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/930

# Discussion History
## rbrunner7 | 2023-11-27T18:19:22+00:00
````
<d​angerousfreedom> Hello
<SNeedlewoods> hi, barely made it, because my hard drive fried an hour ago
<r​brunner7> jeffro256 mentioned yesterday that he can't make the meeting, but that he will go back to programming this week, after a break.
<r​brunner7> So, anything to report from last week?
<d​angerousfreedom> The serialization of the enote_store should be working now. But more tests are needed and some issues need to be solved too.
<r​brunner7> Nice. Just shout if something is ready to review and/or test.
<d​angerousfreedom> Ok, thanks for the first review and for raising some important points!
<SNeedlewoods> I looked into contextual_enote_record_types.h for LegacyEnoteOriginContext, made minor changes and added some comments for things I have to figure out
<r​brunner7> SNeedlewoods: Any first comments yet about looking at this codebase?
<d​angerousfreedom> I will try to use it now for the initialization of the wallet and see if other issues appear.
<SNeedlewoods> I really appreciate the clean design compared to legacy code, but it's a lot to digest
<r​brunner7> Sounds like a good summary of the situation :)
<r​brunner7> Did you already stumble over the Seraphis library walkthrough video?
<r​brunner7> Over 1 hour of intense introduction by koe
<SNeedlewoods> the 3h video presented by koe? yes watched it during lunch breaks
<r​brunner7> 3h even? Yeah, that's the one in any case.
<SNeedlewoods> https://www.youtube.com/watch?v=aAvSpfll9z4
<r​brunner7> Right.
<r​brunner7> I can proudly say "I was there".
<r​brunner7> Alright. Anything special to discuss today?
<r​brunner7> Maybe 50% off-topic, 50% on-topic: Just saw today that plowsof asks for opinions about the future of the CCS, escrow by luigi or not: https://github.com/monero-project/meta/issues/935
<d​angerousfreedom> Not from my side
<SNeedlewoods> I feel like talking to celebrities after watching presentations of you guys lol
<r​brunner7> Yeah, I would say that especially koe is quite a high-class cryptographer. I don't think many of those walk around and can be reached by mere mortals like us.
<r​brunner7> Ok, seems we can close the meeting early today. Thanks for attending, read you again next week!
<SNeedlewoods> "Alright. Anything special to discuss today?" unfortunately, because of the fried hard drive incident, I don't hace access to my notes and I'll probably have to get a new ssd and set up my dev environment from scratch
<SNeedlewoods> thanks for the meeting
<r​brunner7> Sounds like work. At least the seeds are safe, if you already have any, right?
<d​angerousfreedom> Thanks rbrunner7
````


# Action History
- Created by: rbrunner7 | 2023-11-24T16:56:10+00:00
- Closed at: 2023-11-27T18:19:22+00:00
