---
title: v18 syncing issues linux
source_url: https://github.com/monero-project/monero-gui/issues/3989
author: fugbixer
assignees: []
labels: []
created_at: '2022-08-01T11:27:10+00:00'
updated_at: '2022-09-08T20:41:18+00:00'
type: issue
status: closed
closed_at: '2022-08-14T16:46:32+00:00'
---

# Original Description
it starts over scanning blocks i have already scanned before and sometimes also syncing the blocks again and again. (each restart)

never saw this in any previous release

using remote node (simple modus)

Blocks last 24h	733
Blocks avg. per hour (last 24h)	31

had this on multiple debian based distros all kvms

![node-related cleaned](https://user-images.githubusercontent.com/107816169/184546382-e43c0227-0342-4f49-97eb-0bf396861843.png)

i have scanned the blockchain already but still few thousand blocks to sync when i restart later 

![oVxBVt0](https://user-images.githubusercontent.com/107816169/184546348-92a9353b-8945-4fac-8baf-e93bf95227d0.png)



# Discussion History
## selsta | 2022-08-01T20:34:54+00:00
Are you sure that the wallet saves correctly? Could it be that you have permission issues?

## fugbixer | 2022-08-03T16:50:54+00:00
@selsta seems to be the first run of the new client only which triggered the rescan. 

## fugbixer | 2022-08-14T16:38:11+00:00
i get the same issue over and over again

![node-related cleaned](https://user-images.githubusercontent.com/107816169/184546382-e43c0227-0342-4f49-97eb-0bf396861843.png)

than i have to restart the gui until it finally does the syncing.

@selsta could this be node related?

i have internet access but the selected nodes crap around but why the number below in this image is displayed?

could it be provider related censorship which block the communication with the nodes? 
i doubt that since sometimes it works and sometimes it does not...

## selsta | 2022-08-14T16:42:57+00:00
It is possible the simple mode might make issues around the network upgrade if you connect to nodes that didn't update. I would recommend you to select Advanced mode and connect to a remote node manually.

You can go to the main menu by clicking on the exit symbol in the top left corner.

Then click on "Change wallet mode" and select "Advanced mode". Afterwards open your wallet again, go to Settings -> Node, select "Remote node" and enter the following node:

address: `selsta2.featherwallet.net`
port: `18081`

This should resolve your issue for now. No extra hard disk space required.

----------

Other remote node in case the above has issues:

address: `node.supportxmr.com`
port: `18081`

address: `selsta1.featherwallet.net `
port: `18081`

address: `node.community.rino.io`
port: `18081`

More nodes: nodes.monero.com

## fugbixer | 2022-08-14T16:46:32+00:00
Maybe not such a bad idea to hard code some community nodes to be preferred in simple mode node selection...

I wonder why did this issue happened before the hard fork i mean the issue first occurred 13 days ago.  

## selsta | 2022-08-14T16:47:30+00:00
We will remove simple mode and replace it with community nodes. We tried to make a decentralized node scanner and it is only causing issues :/

## fugbixer | 2022-08-15T12:50:44+00:00
![nodes cleaned](https://user-images.githubusercontent.com/107816169/184637761-57d8834c-e9d6-4830-bbcb-c4aa93bfe31f.png)

this issue currently cripples the gui for noobs

would be beneficial... could it be fixed when the node sends his version of monero to the client so that he can just see okay my minimum required version is higher and than keeps searching for nodes so this cant happen in the next hard fork?

## fugbixer | 2022-08-15T13:02:56+00:00
monero should be plug and play.

the current state of the gui makes monero look like trash for noobs.
i still love the project but imagine someone not knowing the tech behind it facing this:

![fail cleaned](https://user-images.githubusercontent.com/107816169/184639908-12cee095-3d4e-4dcf-a1ac-2e4b646e0590.png)

unusable crap as first impression would be very unpleasant 

# Action History
- Created by: fugbixer | 2022-08-01T11:27:10+00:00
- Closed at: 2022-08-14T16:46:32+00:00
