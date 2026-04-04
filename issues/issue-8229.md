---
title: monerod blocks exclusive node
source_url: https://github.com/monero-project/monero/issues/8229
author: Gingeropolous
assignees: []
labels: []
created_at: '2022-03-28T19:49:13+00:00'
updated_at: '2022-05-29T21:25:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
presumably the reason to add-exclusive-node is because you trust the node. 

It makes no sense why the daemon would block its only designated connection.

# Discussion History
## trasherdk | 2022-03-29T10:26:12+00:00
Well, if there is only one exclusive node, it makes little sense.
If it's one in a list, and it start to misbehave, it makes more sense.

```
  --add-exclusive-node arg              Specify list of peers to connect to 
                                        only.
```

## Gingeropolous | 2022-04-01T13:52:45+00:00
ok, so if exclusive node list == 1, then ban = false. 

if exclusive node list > 1, and [exclusive_node_list] are all "misbehaving" (according to what?), pick one at random to stick with? 

i mean, you've directed your monerod to bind to the rest of the network by forcing it to connect to a specific node or set of nodes. In doing so, you've nullified the ability of the monerod to reach out and attempt to find its own way into the network. Presumably, you don't want your monerod to reach out on its own, thats why you gave it an exclusive node(s) to connect to. Furthermore, the implication is that you trust the exclusive node(s), therefore any interpretation of those nodes as malicious by your daemon is a case of the software thinking it knows better than the user. 

## hyc | 2022-04-01T14:04:38+00:00
Yes. The real problem is whatever went wrong in the first place, to make it think it needed to ban a node at all.

## jeffro256 | 2022-04-01T14:21:27+00:00
@trasherdk the whole point of explicitly specifying exclusive nodes is to curate your list of connections. The node software shouldn't override that decision on its own because a connected node is misbehaving. 

## trasherdk | 2022-04-02T21:31:27+00:00
So, even if you know you get bad information, just roll with it?
Maybe the banning thingy need a review.

# Action History
- Created by: Gingeropolous | 2022-03-28T19:49:13+00:00
