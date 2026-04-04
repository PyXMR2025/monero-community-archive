---
title: 'Seraphis wallet workgroup meeting #80 - Monday, 2024-07-29, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1045
author: rbrunner7
assignees: []
labels: []
created_at: '2024-07-26T19:52:59+00:00'
updated_at: '2024-07-29T18:23:28+00:00'
type: issue
status: closed
closed_at: '2024-07-29T18:23:28+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1042

# Discussion History
## rbrunner7 | 2024-07-29T18:23:28+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1045
<s​needlewoods> hey
<o​ne-horse-wagon> Hello.
<j​berman> *waves*
<r​brunner7> So, what is there to report from last week?
<d​angerousfreedom> Hi
<d​angerousfreedom> I'm still in the quest of trying to understand fcmp. I believe I did a lot of progress with the theory but didnt write any code though. I'm planning to write a summary of my understanding here (and bother jberman  and kayabanerve  with some questions a bit more) and start looking at the `grow` algorithm before next meeting. I am pretty convinced now that I should change the direct<clipp
<d​angerousfreedom> ion of my ccs and help with the efforts of fcmp. If I do something useful then I will claim the funds already donated. Otherwise I won't.
<s​needlewoods> This week went very productive for me. I'm 97% done with the boring part (going through wallet2) and will just have to add a couple more functions and comments to the API before I'm ready to PR, hopefully will be finished before next meeting, but depends on how much distractions there will be.
<rbrunner7> +1
<dangerousfreedom> +1
<k​ayabanerve> *waves*
<k​ayabanerve> I prepped a few crates for auditing
<r​brunner7> "If I do something useful then I will claim the funds already donated. Otherwise I won't." I hope it does not come to the latter :)
<sneedlewoods> +1
<dangerousfreedom> +1
<j​berman> me: syncing the fcmp merkle tree, migrating outputs into the tree, grow_tree, trim_tree are in the touch-up phase, ~90% done. Working on touch up (cleaner migration, finalized db ipml, fewer params/cleaner functions, comilation fixes etc.), and updating the transaction class for fcmp's this week
<k​ayabanerve> Oh. I also figured out how to make proving with divisors constant time, which was prior a challenge.
<r​brunner7> "I prepped a few crates for auditing" Is this more or less classic "review", as we usually review each others' PR, or more?
<r​brunner7> I wonder how that will work anyway, now with 2 programming languages in play ...
<k​ayabanerve> No, one the GBP review is done and the divisors is done, each lib should be audited by an external group (such as Cypher Stack)
<d​angerousfreedom> Yeah, it has been part of the challenge to understand the `prove` and `verify`of fcmp in rust :p
<r​brunner7> I see
<r​brunner7> Many things running nicely in parallel then.
<r​brunner7> Do we have anything special to discuss together today?
<s​needlewoods> I don't
<r​brunner7> Doesn't look like it. Well, short meeting then. Thanks for attending everybody, read you again next week!
<k​ayabanerve> The FCMP prove/verify are quite ugly right now :/
<s​needlewoods> thanks everyone, cu
<d​angerousfreedom> Yeah. I really want to understand exactly how a tuple [O,I,C] (for example one of my outputs) would be hidden in the tree and how it could be verified. I understand the idea now but still need to make efforts to understand exactly what is happening in the math and code.
<d​angerousfreedom> Probably I will ask you a few questions again this week. Thanks for answering in advance kayabanerve
<r​brunner7> Sounds quite ambitious. Wish you luck. Certainly a plus if more people understand things down to a fundamental level.
````

# Action History
- Created by: rbrunner7 | 2024-07-26T19:52:59+00:00
- Closed at: 2024-07-29T18:23:28+00:00
