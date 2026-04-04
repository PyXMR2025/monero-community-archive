---
title: 'Seraphis wallet workgroup meeting #26 - Monday, 2023-06-12, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/847
author: rbrunner7
assignees: []
labels: []
created_at: '2023-06-10T16:14:44+00:00'
updated_at: '2023-06-12T18:47:35+00:00'
type: issue
status: closed
closed_at: '2023-06-12T18:47:35+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #845

# Discussion History
## rbrunner7 | 2023-06-12T18:47:35+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/847
<dangerousfreedom> Hello
<rbrunner7[m]> Hmm ... just the two of us? :)
<Rucknium[m]> waves
<valldrac[m]> Hi
<dangerousfreedom> Now 3 :p
<jberman[m]> hey I'm here, sorry
<rbrunner7[m]> Splendid! Well then, anything to report? I have been reviewing dangerousfreedom[m] 's PRs a bit and left some comments
<dangerousfreedom> This week I continued implementing the wallet knowledge proofs (for legacy and sp) and took a look at jberman's scanner. A question raised from that: what is the easiest way to communicate with the node in c++?
<rbrunner7[m]> From where?
<rbrunner7[m]> I don't know anything else than the RPC interface
<dangerousfreedom> In jberman's code and at wallet2 you have to set the m_http variable... I was wondering if I should create a module for that or if there is something easier to do
<dangerousfreedom> I will need to request many information from the node and was wondering the easiest way to do it
<rbrunner7[m]> Isn't that just the object for the RPC connection?
<dangerousfreedom> I didnt look deep what this object is doing and its dependencies yet but I guess it wont be hard but instead I just asked to save me some work :p
<dangerousfreedom> But I will find out this week and the goal is to have the spend_proof by next week
<dangerousfreedom> I need something like this: https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L10864
<jberman[m]> I don't think the code I have there is the simplest way, but basically you initialize an http client and use the RPC interface to communicate with the daemon
<dangerousfreedom> Ok. Yeah, I will do something like that
<jberman[m]> this is sort of contained right here: https://github.com/j-berman/monero/blob/1180c8262e405708411d166ef3cb36bd5f98cb92/src/blockchain_utilities/blockchain_scanner.cpp#L203-L213
<dangerousfreedom> Would it be worth to write something modular?
<dangerousfreedom> Or is there something already?
<rbrunner7[m]> I don't think it will get much easier than that, once you know the basics ...
<rbrunner7[m]> Nor is the code very hard to write
<rbrunner7[m]> Tedious maybe, and quite low-level, but why complicate things with yet another layer ... IMHO
<dangerousfreedom> Ok thanks.
<valldrac[m]> In wallet2 there are two functions to call RPC endpoints: epee::net_utils::invoke_http_json_rpc and epee::net_utils::invoke_http_bin. jberman snippet code uses the former 
<valldrac[m]> You need to provide the http client to these functions. I think it's the m_http variable you said 
<shalit[m]> Hello
<dangerousfreedom> Thanks. Sometimes I'm ashamed of my lazyness but I'm improving :p
<rbrunner7[m]> I wondered about another little thing when I reviewed the code in the PRs: What do we do with links to web pages in source code comments
<rbrunner7[m]> I mean, we all know about link rot, but is this already reason enough to not include any links?
<rbrunner7[m]> For example we have a very special Base32 alphabet. There is some page written by Tevador explaining the reasoning.
<rbrunner7[m]> Does it make sense to link to that from the source coude or not?
<rbrunner7[m]> What's the sentiment here?
<dangerousfreedom> I would say it is worth. When the link is not valid anymore we remove.
<jberman[m]> +1^ and include a snippet of reasoning behind what the source link says so it's not doing all the lifting on explanation
<valldrac[m]> Yeah, I often include links to external pages in source code
<Rucknium[m]> Create a snapshot with the Wayback Machine and directly link the snapshotted URL
<rbrunner7[m]> Yeah, the most important, core info copied and a link is of course best :)
<rbrunner7[m]> Ah, you can ask the Wayback Machine for a snapshot?
<Rucknium[m]> Yes
<rbrunner7[m]> Interesting
<valldrac[m]> Unless it's something essential or part of the specification, you can just put it in our wiki or directly in the source code as a long comment :)
<Rucknium[m]> https://archive.org/web/  "Save Page Now" in lower right corner
<rbrunner7[m]> Sure, but I guess our own resources are not necessarily more stable
<rbrunner7[m]> Rucknium[m]: Good to know, thanks for the tipp
<valldrac[m]> Another option is as .md into /docs in the repo
<rbrunner7[m]> There are many options, if the willingness is there, right. But I read the sentiment as "Links can make sense, and they are at least not discouraged"
<valldrac[m]> +1
<rbrunner7[m]> Alright. Anything else for today's meeting?
<dangerousfreedom> Not from me
<valldrac[m]> Is there something that needs to be reviewed?
<rbrunner7[m]> You could have a look anytime of the 3 PRs that dangerousfreedom[m] made
<dangerousfreedom> I will keep updating this draft so my work will be visible there. 
<dangerousfreedom> Now it is in a very raw situation
<dangerousfreedom> Not worthy of detailed review but general advices
<rbrunner7[m]> Understood.
<rbrunner7[m]> Does not look like we have more. Thanks for attending, read you again next week at the latest, the last meeting before Monerokon, hurray.
<rbrunner> Our PRs are here, by the way: https://github.com/seraphis-migration/monero/pulls
````


# Action History
- Created by: rbrunner7 | 2023-06-10T16:14:44+00:00
- Closed at: 2023-06-12T18:47:35+00:00
