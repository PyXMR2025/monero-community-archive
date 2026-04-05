---
title: read error "end of file" no active pools, stop mining
source_url: https://github.com/xmrig/xmrig/issues/1678
author: ghost
assignees: []
labels: []
created_at: '2020-05-15T09:26:41+00:00'
updated_at: '2020-08-29T04:39:47+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:39:47+00:00'
---

# Original Description
Hello,
as the title say i have an issue with xmrig v5.11.1 
after a couple of minutes comes a error message 
xmr.pool.minergate.com read error "end of file" 
net: no active pools stop mining
after that it will repeat mining but wont connect back to my wallet

How can i fix this issue ? 

# Discussion History
## zn3x | 2020-05-22T18:14:03+00:00
Try other pool. Minergate is not advisable

## Kudabelangfx | 2020-05-25T19:45:32+00:00
 which os? 
had same problem with hiveos connect to miningrigrental and use xmrig for mining to any pool. “no active pool” keep happens. miner restarting everytime.

## Masterbob79 | 2020-05-25T21:32:04+00:00
I have had this on hiveos before. What I found is TLS is on when it doesnt need to. Or it's off when it should be on. 

## Kudabelangfx | 2020-05-25T21:38:21+00:00
> I have had this on hiveos before. What I found is TLS is on when it doesnt need to. Or it's off when it should be on. 


by default it is off. 
how much accurate of your findings? any log? how did you get solve?

## Masterbob79 | 2020-05-25T21:47:38+00:00
I use supportxmr. When use pool.supportxmr.com:7777 with tls on I get the error. If I use pool.supportxmr.com:443 without tls, same error. 443 is their tls port. I asked the pool about it.

## Kudabelangfx | 2020-05-29T22:07:38+00:00
i see. thought tls from miner conf. 

# Action History
- Created by: ghost | 2020-05-15T09:26:41+00:00
- Closed at: 2020-08-29T04:39:47+00:00
