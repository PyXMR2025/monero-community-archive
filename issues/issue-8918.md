---
title: It is possible to open >1 connections to the same I2P node
source_url: https://github.com/monero-project/monero/issues/8918
author: nahuhh
assignees: []
labels:
- bug
- important
created_at: '2023-06-27T15:18:25+00:00'
updated_at: '2024-02-24T15:06:02+00:00'
type: issue
status: closed
closed_at: '2024-02-24T15:06:02+00:00'
---

# Original Description
Monero has the same problem that bitcoin once did. You can even connect to yourself multiple times.

Bitcoin issue: https://github.com/bitcoin/bitcoin/issues/21389
comment with proposed fixes: https://github.com/bitcoin/bitcoin/issues/21389#issuecomment-866925116
the merged fix: https://github.com/bitcoin/bitcoin/pull/22112

In monero, `anonymous-inbound` broadcasts the i2p domains to peers. 
`anonymous-inbound` written as `anonymous-inbound=your.b32.i2p:18085,...` will broadcast `your.b32.i2p:18085`. It should only allow `anonymous-inbound=your.b32.i2p:0,...` or perhaps `anonymous-inbound=your.b32.i2p,...`

Im not sure what conditions must be met, but in certain circumstances it will broadcast 18080 as the port. Either way, the fix is to force port i2p peers to only be stored using port 0, and to remove duplicate i2p domains from peerlists.
the merged fix: https://github.com/bitcoin/bitcoin/pull/22112

this is i2p only. Onion works fine and uses ports


# Discussion History
## nahuhh | 2023-06-27T15:24:15+00:00
Worth noting that btc uses i2p sam and we use socks.

Either way, the ability to spam peerlists with "valid" peers on "different" ports (just a change to anonymous inbound i2p port), and being able to connect to yourself are the issues here 

## MoneroArbo | 2023-09-20T14:10:15+00:00
Having a possibly related issue where I did not specify a port in moderod config for my i2p inbound address, but my node makes an outgoing i2p connection to my own address, except it has :18080 appended at the end.

Some i2p peers in my list don't have a port number, others have 18080 or a non-default port, but as mentioned i2p doesn't really use ports so monerod should at a minimum recognize that xxxx.i2p and xxxx.i2p:18080 and xxxx.i2p:18088 and etc are all the same.

**edit:** Self-connect can apparently happen through "misconfiguration" according to the comments on https://github.com/monero-project/monero/pull/7017

It doesn't mention what the proper configuration is (specifying a port?) but regardless the behavior seems incorrect to me since such self connects are trivially avoided by checking the i2p address

## MoneroArbo | 2023-09-21T13:34:02+00:00
Confirming that I also form multiple i2p connections to the same (non-self) node but with different port numbers. Poking around the peer list, there are multiple entries for many if not most addresses. For example:

- s3l6ke4ed3df466khuebb4poienoingwof7oxtbo6j4n56sghe3a.b32.i2p:0
- s3l6ke4ed3df466khuebb4poienoingwof7oxtbo6j4n56sghe3a.b32.i2p:18080:0
- s3l6ke4ed3df466khuebb4poienoingwof7oxtbo6j4n56sghe3a.b32.i2p:28081:0

The extra :0 at the end of the latter two entries stands out as odd to me, especially as IPv4/6 addresses don't have it. It's like the port zero is being appended but without removing the user supplied port number from the string.

Regardless, it seems to me @nahuhh is correct in their assessment of the issue, including monerod sometimes broadcasting 18080 as the port as I was connected to myself on 18080 despite never supplying a port to anonymous-inbound.

## vtnerd | 2024-01-28T20:19:53+00:00
I urge everyone having problems with this to try #9138 if they know how to compile from source. This should collapse overloads on port into one value.

# Action History
- Created by: nahuhh | 2023-06-27T15:18:25+00:00
- Closed at: 2024-02-24T15:06:02+00:00
