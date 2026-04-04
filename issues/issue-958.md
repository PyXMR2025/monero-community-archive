---
title: 'Seraphis wallet workgroup meeting #54 - Monday, 2024-01-22, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/958
author: rbrunner7
assignees: []
labels: []
created_at: '2024-01-19T18:18:15+00:00'
updated_at: '2024-01-22T18:21:42+00:00'
type: issue
status: closed
closed_at: '2024-01-22T18:21:41+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/955

# Discussion History
## rbrunner7 | 2024-01-22T18:21:41+00:00
````
<g​hostway> Hello
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/958
<s​needlewoods_xmr> hey
<j​berman> hello
<r​brunner7> So, anything to report from last week?
<s​needlewoods_xmr> since my last update (still visible in recent backlog) I struggled a bit with the combination of maps, variants, constructors and initializer lists, but I think now with the latest commit, the PR is doing what it's supposed to and is ready for review
<ghostway> +1
<rbrunner7> +1
<g​hostway> I've replied to SNeedlewoods's review, and after that is done I think we're good to go
<g​hostway> I'll review their pr too, probably this week/coming days
<r​brunner7> You saw my +1 vote for descriptive variable names for the keys, right?
<j​berman> Nothing to report on my end this week, made a bit more progress on fcmp's but nothing significant to share
<g​hostway> Yep, but that means either changing the names on the spec or, more sensibly, just comment the spec names
<g​hostway> Will commit that as well, then
<r​brunner7> Yes, I think adding comments is the way to make the connection to the spec
<ghostway> +1
<r​brunner7> If we are here, and have ample time left in the meeting, anyway, maybe some thoughts about that little indentation question for the serializing macros
<g​hostway> Just forgot about it :)
<r​brunner7> I think there is a good argument for *not* indenting, if you look at the fact that all those macros just generate some method calls, and those are - of course - on the same level :)
<s​needlewoods_xmr> would we start to not indent from here, or do we change all the code from the past to be not indented then?
<r​brunner7> Well, we usually refrain from making such "whitespace" changes retro-actively. It can mess up the Git history, for example, and that's usually not worth it.
<r​brunner7> So, yes, for our Seraphis wallet code to not indent, and the other code is none of our business
<r​brunner7> This is then also in line what that rule file thinks, yes?
<g​hostway> yep
<r​brunner7> Alright. Do we happen to have something to discuss, beyond reports and that little indentation story?
<s​needlewoods_xmr> I'm okay with not indenting
<s​needlewoods_xmr> besides that nothing from my side
<r​brunner7> Ok. Looks like we can close early. Thanks for attending, read you again next week!
<s​needlewoods_xmr> thanks for moderating, cu all
````


# Action History
- Created by: rbrunner7 | 2024-01-19T18:18:15+00:00
- Closed at: 2024-01-22T18:21:41+00:00
