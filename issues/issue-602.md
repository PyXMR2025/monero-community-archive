---
title: Automatically Connect to Open Remote Nodes in GUI
source_url: https://github.com/monero-project/monero-gui/issues/602
author: SamsungGalaxyPlayer
assignees: []
labels:
- resolved
created_at: '2017-03-24T07:42:10+00:00'
updated_at: '2019-09-23T11:45:39+00:00'
type: issue
status: closed
closed_at: '2019-09-23T11:45:39+00:00'
---

# Original Description
Many users have asked for an easier way to use a remote node in the GUI. Other users have expressed concerns for having and maintaining a "master list" of nodes somewhere, and while a plugin (for example: a MoneroWorld Nodes plugin) can be helpful, it still takes the user an extra step and relies on an extra party.

Gingeropolous wrote [moneriote](https://github.com/Gingeropolous/moneriote) for scanning the network for open nodes. Can this be added to the GUI, in the initial configuration settings and settings panel, to have the service provide the option to scan the network for open nodes and automatically connect to a random one?

In the initial GUI config, show three options: 1) I would like to use a local node on this computer (safest), 2) I would like to connect to a specific remote node by URL, 3) I would like to connect to a random open node on the network

Some advantages of this method:

1. No need to keep or maintain a list of open nodes. Users can find them for themselves with minimal effort

2. May make it easier for some users to connect to a remote node, since they can do so directly from the GUI instead of searching for other sources (notably MoneroWorld)

3. By selecting one at random, it can reduce the impact of a single node registered to a centralized directory

Some disadvantages of this method:

1. I have not tested the performance of moneriote. It might not be reasonable for a normal user to use in its current form. It may take too long, use too much bandwidth, etc.

2. An attacker can control a large number of these open nodes, but they can already do the same for centralized lists. For instance, suppose an attacker launched FastMoneroNodez that many people used. It's probably more risky to have only a handful of centralized node lists imo.

3. People may not want to have their node process the requests of these users. To address this, the moneriote currently searches for the nonstandard RPC port 18089. We can keep using this port.

I'd love to hear some of your thoughts on this.

# Discussion History
## Jaqueeee | 2017-03-24T10:11:31+00:00
related to #572

## SamsungGalaxyPlayer | 2017-03-24T18:51:06+00:00
[Here is a crude mockup](http://i.imgur.com/KeAcWtUl.png).

## loopyman | 2017-03-24T20:45:28+00:00
I personally do not trust the idea of selecting a "random" node even if they are vetted prior or "approved". However if I could create my own list of my trusted nodes like a favorites/bookmark list then I would be just as happy. 

## ghost | 2017-03-24T20:46:34+00:00
I would prefer a dev meeting discussion about this (people smarter than myself)

## SamsungGalaxyPlayer | 2017-03-25T10:01:58+00:00
I know that connecting to a random node is not ideal. Running your own node is ideal. 

But we currently allow people to connect to a remote node. The remote nodes can be run by trusted people, or they can be run by total strangers and attackers. From what I can tell, the community suggests for more and more people who care the most about convenience to [use a MoneroWorld random node](https://moneroworld.com/#nodes).

This change would essentially replicate the process with two advantages: 1) a user can find a remote node directly from the GUI, without tracking down a certain website, and 2) the service is decentralized

As I suggested [in the mockup](http://i.imgur.com/KeAcWtUl.png), this change would provide the easiest option for people. I don't think it will be faster than manually finding a remote node and connecting, but we don't exactly want new users to try and comb the internet for open nodes anyway. In this way, connecting to a random node is probably preferable to a node listed on a website run by an attacker.

## SamsungGalaxyPlayer | 2017-03-26T18:11:16+00:00
From the [dev meeting](https://monerobase.com/wiki/DevMeeting_2017-03-26), we want to get away from the connecting to a remote node method. This solution is for a problem that should be going away soon.

## Jaqueeee | 2017-03-26T18:43:44+00:00
@SamsungGalaxyPlayer tbh i don't think this problem will go away "soon". But it depends on when soon is I guess. :)

## hyc | 2017-10-04T22:59:56+00:00
IMO this is the right solution https://github.com/monero-project/monero/issues/2204

## erciccione | 2018-11-18T13:18:16+00:00
Think this is resolved with new versions. @SamsungGalaxyPlayer can you cinfirm?

## SamsungGalaxyPlayer | 2018-11-19T03:13:04+00:00
No @erciccione, this particular issue is not resolved with new versions. This is what the Monero GUI v0.13.0.3 looks like:

![image](https://user-images.githubusercontent.com/12520755/48684215-4f114400-eb76-11e8-90b9-c8bac13f9faf.png)

I will edit this issue to be more specific, but ultimately it recommends that the wallet is able to *automatically* scan the network for open remote nodes and select one to connect to. In the current GUI, you can manually specify a remote node, but you need to find one.

In my opinion, the GUI should automatically connect to open remote nodes that the wallet finds with a quick network scan. This improves UX, since people don't need to search for a remote node manually. Of course, the wallet can still warn against the privacy reductions when using remote nodes.

## SamsungGalaxyPlayer | 2018-11-26T15:49:50+00:00
This behavior should operate like [Monerujo's Node-o-matiC feature](https://www.reddit.com/r/Monero/comments/9zzr90/update_monerujo_1105_nodeomatic_beta/).

## xiphon | 2018-11-27T17:45:38+00:00
> This behavior should operate like [Monerujo's Node-o-matiC feature](https://www.reddit.com/r/Monero/comments/9zzr90/update_monerujo_1105_nodeomatic_beta/).

The link doesn't contain any information on how the feature works. Could you provide any detailed description?

## xiphon | 2018-11-27T17:58:26+00:00
Okay, i had to dig into xmrwallet repo to answer my previous question:

> ## Node List
> If the list is empty, you can either add new nodes manually or let Monerujo
> scan the network for you. Or both. Read on&#8230;
> The node list shows all currently known nodes. Additionally, the timestamp
> of the latest block known to each node is shown under the node name. An icon
> representing the node&apos;s response behaviour
> (which indicates the level of connectivity to be expected)
> is shown next to each node.
> Any node in the list can be bookmarked for later use.
> Nodes which are not bookmarked will be forgotten.
> Monerujo will choose the optimal bookmarked node each time you use it.
> It does this by checking the blockheight (how up-to-date
> is the node?) as well as the response behaviour (how fast does the node respond to requests?).
> The list is sorted by these characteristics, so the top node would be the one Monerujo
> would choose right now. The bottom of the list would show very slow or unavailable nodes.
> ## Add a Node
> By touching the &quot;Add Node&quot; button at the bottom, you will be asked to
> enter the node details in the following dialog.
> The &quot;Address&quot; is the hostname or IP-address of the node - this is the only
> mandatory entry.
> Enter the &quot;Port&quot; if the node runs on a non-default port (e.g. 18089).
> You can also optionally name the node, so you can identify it easier later on.
> Some nodes require credentials to use them. Enter the provided username &amp;
> password in the appropriate fields. Now you can &quot;Test&quot; these setting.
> The &quot;Test Results&quot; will display the blockheight, response time and actual IP used.
> The result may also be an error - usually because the hostname provided is
> not reachable in a sensible amount of time or the credentials are incorrect.
> Or the hostname/port combination does not point to an actual Monero Node!
> Once the test passes (no error) - you&apos;re set to press &quot;OK&quot; to save &amp;
> bookmark this node.
> ## Scan for Nodes
> Additionally, you can scan the network for nodes. Monerujo will start
> scanning the network for Remote Nodes on port 18089. It begins by asking your
> bookmarked nodes for other peers in the Monero P2P network and then continues
> by asking those for their peers, and so on. If you have no bookmarked nodes
> (or they don&apos;t tell us about their peers),
> Monerujo will go straight to the Monero seed nodes hardcoded into Monero. The
> scan stops when it finds 10 remote nodes in total.

## xiphon | 2018-11-27T18:19:51+00:00
This approach has major consequences on Monero users' security, it heavily weakens the users' anonymity. 

Nothing stops a third-party remote node from keeping a record of all the users' identities and corresponding tx ids that were sent through this remote node.

The only way to implement this and not weaken the users' security is to utilize an anonymity network like TOR, I2P, or Kovri (at some point) to establish remote nodes connections.

## SamsungGalaxyPlayer | 2018-11-27T20:10:34+00:00
@xiphon I strongly disagree for several reasons:

1. Any users who truly care will run their own node. This can be communicated to others in the GUI.

2. Users who prioritize convenience will simply go to Google and search for open nodes. Now instead of finding the advertised "Free Monero Node" that someone is paying to run and likely collecting information from, they will connect to random nodes on the network.

This second component is better for two reasons:

1. It's more convenient, since users don't need to manually find nodes and deal with down nodes.

2. It's more secure in my opinion, since there is less opportunity for an attacker to try and get people to use their nodes.

Of course, people using remote nodes should ideally use Kovri or another service in the future. However, this is separate from this issue. This issue regards *for people who wish to use remote nodes, should we auto-connect to one or have a user manually fill one in?* I argue for the two main reasons above that people should have the option to have the wallet automatically find and connect to nodes. It's much better UX and is arguably safer than using other remote nodes.

Keep in mind that the status quo is relying on MoneroWorld to direct traffic, which is a clear point of centralization.

## sanderfoobar | 2019-04-23T16:17:13+00:00
Implemented since #1909 

+resolved

## SamsungGalaxyPlayer | 2019-04-23T16:24:05+00:00
@xmrdc no, this is not resolved. The current implementation uses your centralized service to select nodes. This implementation, something @xiphon created a recent CCS proposal for, would bundle the scanning tool with the GUI. Thus, simple mode would instead search the network for available nodes and connect to one, not ask your server for an open one.

## selsta | 2019-04-23T16:31:07+00:00
@SamsungGalaxyPlayer You can set your own node aggregator using the config file.

## sanderfoobar | 2019-04-23T18:10:01+00:00
@SamsungGalaxyPlayer whoops

+open

## erciccione | 2019-04-23T18:40:21+00:00
@xmrdsc i think you need toremove the label

-resolved

## SamsungGalaxyPlayer | 2019-04-23T18:58:38+00:00
@selsta this issue specifically discusses a remote node scanning tool packaged with the GUI, which is different than the current solution(s).

## SamsungGalaxyPlayer | 2019-05-30T21:20:08+00:00
This issue is part of @xiphon's work in their CCS: https://ccs.getmonero.org/proposals/xiphon-part-time.html

## erciccione | 2019-09-23T11:43:53+00:00
This is resolved by #2370 

+resolved

# Action History
- Created by: SamsungGalaxyPlayer | 2017-03-24T07:42:10+00:00
- Closed at: 2019-09-23T11:45:39+00:00
