---
title: Make it possible to generate multisig address via the Monero RPC JSON API
source_url: https://github.com/monero-project/monero/issues/2175
author: CameronRuggles
assignees: []
labels: []
created_at: '2017-07-16T06:32:58+00:00'
updated_at: '2018-01-04T17:48:27+00:00'
type: issue
status: closed
closed_at: '2018-01-04T17:48:27+00:00'
---

# Original Description
So when multisig gets here, it would be good if we could use the JSON API to send/recieve the info needed to form an integrated multisig address. Is this possible? If not, how can we make it possible?
This seems like it'll be the easiest and quickest way to get monero multisig marketplaces to market. I believe that will dramatically increase the usability and adoption of Monero.

As multisig is already being developed it should be fairly easy to also get it to work with the API?


Sorry if this issue is poor etiquette or done improperly, not really sure the best way to create an issue/feature request, but this is incredibly important. Likely I'll be using it to implement monero multisig in annularis, which is free and open source marketplace software. 


# Discussion History
## moneromooo-monero | 2017-07-16T07:58:07+00:00
There is no RPC for multisig, but I'll add it.

## CameronRuggles | 2017-07-16T22:48:19+00:00
Awesome! I'm not a coder  but if there is anything I can do to help let me know. 
When do you think this will be implemented and where do I go to watch the code development? 


## moneromooo-monero | 2017-07-17T07:32:45+00:00
I started on it, but I don't know when it will be finished. The code will be PR'd in this repo (either in a new PR, or in the current multisig one). As for helping, testing the multisig PR now would be a great way to find any user level problems.

## CameronRuggles | 2017-07-17T10:18:27+00:00
Great thanks. Will look into it :) 

## CameronRuggles | 2017-07-18T06:26:30+00:00
Also does it seem complicated to do? Just curious since you've started on it and have looked around it a bit. 

Thanks again. Extremely excited about Monero and all the implications it has once it gets multisig, and this is just a great step forward. 

## moneromooo-monero | 2017-07-18T07:54:08+00:00
No, that is not complicated.

## lessless | 2017-08-13T13:47:55+00:00
@monero-project what's the progress with this one? 

## moneromooo-monero | 2017-08-13T14:23:34+00:00
There is multisig RPC in my multisig2 branch. If you have comments about it, feel free.

## moneromooo-monero | 2017-10-03T08:43:13+00:00
https://github.com/monero-project/monero/pull/2134 now has full RPC for N-1/N as well.

## moneromooo-monero | 2018-01-04T17:43:36+00:00
+resolved

# Action History
- Created by: CameronRuggles | 2017-07-16T06:32:58+00:00
- Closed at: 2018-01-04T17:48:27+00:00
