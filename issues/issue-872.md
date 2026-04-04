---
title: 'Seraphis wallet workgroup meeting #30 - Monday, 2023-07-31, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/872
author: rbrunner7
assignees: []
labels: []
created_at: '2023-07-28T13:59:44+00:00'
updated_at: '2023-07-31T18:15:11+00:00'
type: issue
status: closed
closed_at: '2023-07-31T18:15:11+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #861

# Discussion History
## rbrunner7 | 2023-07-31T18:14:52+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/872
<dangerousfreedom> Hi
<rbrunner7[m]> For the record, jberman here yesterday: "I don't think I'll be able to make the meeting this coming Monday, but will be at all future meetings starting the following Monday. Also planning to resume coding Seraphis lib work this coming week"
<rbrunner7[m]> So we might be a week too early with resuming meetings, if only the two of us are here.
<dangerousfreedom> Yeah maybe, so from my side:
<rbrunner7[m]> Anyway, anything to report? Not from my side. I recently reviewed some non-Seraphis PR from jberman.
<ghostway[m]> I think I have almost everything for my pr. Mostly learned about curve trees and might be doing something there
<dangerousfreedom> This week I have looked again on how to simulate a node and I think I am progressing. I also started looking at jeffro's wallet2_basic and it looks pretty important for us to retrieve the info from the wallet files. @jeffro256, would you also consider making a PR into the seraphis_wallet repo as lean as possible (without the wallet2 modifications) so we can use the load_keys_and_cache_from_file? 
<rbrunner7[m]> Ah, the strong lure of those curve trees ...
<ghostway[m]> Oh I already have that though (with wallet2 dependencies)
<ghostway[m]> dangerousfreedom[m]^
<rbrunner7[m]> Is that what you prepare as your first PR?
<ghostway[m]> The key container is, I was just lazy not submitting the actual pr
<rbrunner7[m]> Well, wait for a rainy day with nothing else to do, and then just do it :)
<ghostway[m]> Rainy days are in a few months, you sure? 
<ghostway[m]> Lol 
<rbrunner7[m]> dangerousfreedom[m]: Yeah, I should also take a look. It will of course be essential to offer full and fully automatic wallet migration.
<rbrunner7[m]> Maybe we will have him around next week to discuss, and hopefully I will be prepared, after having a look.
<dangerousfreedom> I will have some things to show by next week for sure. But yeah, looks like jeffro's PR could be very useful even if we dont modify wallet2
<rbrunner7[m]> By the way, stumbled over the following video from May from Monerotopia, looks like a good introduction to Seraphis and some info about where we stand: https://www.youtube.com/watch?v=vXqy0WFbdQc
<ghostway[m]> Yea, I've seen it. It's quite good, actually
<rbrunner7[m]> Right from the horse's mouth, so to say.
<rbrunner7[m]> Alright, guess just today we don't have much to discuss yet. Let's meet again in 1 week!
<dangerousfreedom> rbrunner7[m]: Yeah. Thanks.
````


# Action History
- Created by: rbrunner7 | 2023-07-28T13:59:44+00:00
- Closed at: 2023-07-31T18:15:11+00:00
