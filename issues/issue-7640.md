---
title: Enable pruning by default
source_url: https://github.com/monero-project/monero/issues/7640
author: erciccione
assignees: []
labels: []
created_at: '2021-03-28T13:11:37+00:00'
updated_at: '2024-03-24T08:22:28+00:00'
type: issue
status: closed
closed_at: '2024-03-24T08:22:28+00:00'
---

# Original Description
Now that pruning is mature and battle tested, would make sense to make it the default. This would improve UX, since the size of the database will be 2/3 smaller, without impacting the usability or security of the network.

If we prefer a more conservative approach, we could prompt the user when syncing a node for the first time, asking if they want to sync a pruned or normal node.

# Discussion History
## erciccione | 2021-03-28T13:12:25+00:00
logs from a short conversation in #monero-dev:

```
12:35:57 <ErCiccione3> I have the feeling that people are still not very much aware of pruning. Would it make sense to ask users if they prefer to run a pruned node the first time they sync a node from scratch? Similar from how we do for solo mining.
12:36:32 <gingeropolous> like in the GUI?
12:36:46 <ErCiccione3> do we do that in the GUI?
12:37:01 <ErCiccione3> i haven't opened the GUI in quite some time to be honest
12:37:15 <ErCiccione3> was talking about the cli btw
12:39:16 <ErCiccione3> i know we prune differently, but for example bitcoin core has pruning enabled by default. That's definitely better ux imo.
12:50:12 <moneromooo> I would not mind pruning being default, it's pretty solid now.
12:55:26 <dEBRUYNE> Think we can make it default for the GUi at least
13:15:17 <Lyza> if you have a pruned node and you want to make it a full node, do you need to re-download everything or only the missing pieces?
13:16:41 <moneromooo> Everything.
13:16:42 <ErCiccione3> everything, as far as i know. you can only got full -> pruned
13:17:23 <ErCiccione3> *go
13:17:54 <ErCiccione3> i think we can safely make it default for both gui and cli
13:19:07 <Lyza> I would say that's an argument for making it a checkbox or prompt instead of default imo
13:19:52 <Lyza> not sure what making it default for CLI would mean. CLI doesn't spin up it's own instance of monerod the same way the GUI does, I think?
13:19:54 <M1312test1312[m]> Is there a reason one would rather run the full chain?
13:20:17 <Lyza> <M1312test1312[m]> to provide that data to the network when needed?
13:20:34 <M1312test1312[m]> Does the network need it?
13:21:13 <moneromooo> If a node wants to get the chain and verify it all, yes.
```

## Gingeropolous | 2021-03-28T14:32:59+00:00
I dunno. I'm hesitant to make it default for the CLI. I view the CLI as the actual bones of the network. I.e., if you just simply run monerod , you can expect the software to do everything thats needed to run and secure the network. That being said, the CLI doesn't mine by default, so perhaps this is just a waste of typing. 

and then again, a CLI user is probably more technically inclined to know that they need to include a string of command line arguments to make their software run they way they expect. 

I think this comes from a feeling that the monero network is still somewhat juvenile in its size. A quick googling leads me to the monerohash stats, which list ~2k nodes. Which isn't nothing, but its not the 10-12k that google reports for bitcoin.  

And yes, I know these node counts are somewhat crap because some unknown percentage doesn't allow incoming.... but that's also sorta the point. I'd argue its more likely someone spinning up a node using CLI is more likely to be able to punch a hole through their firewalls to actually allow incoming connections. Thus, these nodes that allow incoming connections should default to storing, providing, and sharing the full blockchain. 

## erciccione | 2021-03-28T15:29:51+00:00
> the CLI doesn't mine by default,

But we ask the user if they want to mine when starting the node, we could do something like that.

## trasherdk | 2021-03-29T02:57:51+00:00
The `monero-wallet-cli` connects to a already running `monerod`, and can tell the daemon to start mine on the wallets behalf.

I would imagine, telling a running daemon to prune would require the wallet to restart the daemon. Scary 

## Gingeropolous | 2021-03-30T16:02:39+00:00
> > the CLI doesn't mine by default,
> 
> But we ask the user if they want to mine when starting the node, we could do something like that.

yeah, thats true for the GUI I guess? And when you interact with monerod with a wallet CLI too. 

But don't get me wrong. i think the GUI should default to pruned from the start. For one, its less likely the average GUI user will want to dive into the weeds that much. They just want it to work. If a GUI user wants to get advanced, they can explore the GUI advanced options and opt-in to re-download the full blockchain, and probably eventually end up just using a CLI. 

so yeah. GUI default pruned - yes.

# Action History
- Created by: erciccione | 2021-03-28T13:11:37+00:00
- Closed at: 2024-03-24T08:22:28+00:00
