---
title: Monero daemon faild to start
source_url: https://github.com/monero-project/monero-gui/issues/4312
author: AMbns01
assignees: []
labels: []
created_at: '2024-05-03T13:05:33+00:00'
updated_at: '2024-05-03T14:13:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
My monero synced 138Gb data but now after start daemon there is an issue attch please help
![failed to start](https://github.com/monero-project/monero-gui/assets/168646452/3ead2a12-3c66-40c1-b13f-ca319576ed59)


# Discussion History
## selsta | 2024-05-03T13:07:41+00:00
You said you were out of storage in the other comment. Did you solve this?

Also at this point it might be easier for you to just use a remote node.

## AMbns01 | 2024-05-03T13:12:43+00:00
yes dear i was waiting for your help yes i downloaded almost 138Gb files but the my memory ran out now i copied my data to my D drive there i have storage but my daemon not starting getting the above error

## selsta | 2024-05-03T13:13:40+00:00
Did you set the blockchain location in Settings -> Node -> Blockchain directory?

## AMbns01 | 2024-05-03T13:14:45+00:00
yes i tried both the new directory also and by reseting it also

## AMbns01 | 2024-05-03T14:09:08+00:00
bro can you please help me in this


## selsta | 2024-05-03T14:13:03+00:00
It is difficult to remotely figure out what the issue is. Can you just set a remote node?

You go to Settings -> Node, click on Remote Node and then on "Add remote node" and then enter

Address: node2.monerodevs.org
Port: 18089

then click on "Ok" and wait for it to sync.

You can find more remote nodes on monero.fail

# Action History
- Created by: AMbns01 | 2024-05-03T13:05:33+00:00
