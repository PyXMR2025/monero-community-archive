---
title: Want to fork my own monero, what and how does NETWORK_ID WORK ?
source_url: https://github.com/monero-project/monero/issues/4856
author: steffanjensen
assignees: []
labels: []
created_at: '2018-11-15T18:56:24+00:00'
updated_at: '2018-11-16T02:14:44+00:00'
type: issue
status: closed
closed_at: '2018-11-15T19:34:05+00:00'
---

# Original Description
Hi, 

I have forked cryptonote and got it all up and running, but i see a difference between how the deamon connect to the blockchain. 

In crytonote they do it this way.
//TODO Add here your network seed nodes
const std::initializer_list<const char*> SEED_NODES = {
  //"your_seed_ip1.com:8080",
  //"your_seed_ip2.com:8080",


Monero do it like this
boost::uuids::uuid const NETWORK_ID = { {
      0x12 ,0x30, 0xF1, 0x71 , 0x61, 0x04 , 0x41, 0x61, 0x17, 0x31, 0x00, 0x82, 0x16, 0xA1, 0xA1, 0x10
    } };

But what is network id, how does it work, can i just make my own network id, compile 2 monero and they connect without an ip ?

Thanks and sorry for the noob question, i have searched on google for answer without any luck. 

# Discussion History
## fluffypony | 2018-11-15T19:34:05+00:00
No.

## steffanjensen | 2018-11-15T19:37:15+00:00
So whats the next step ?

Do i make the nework id sync my ip or ?

## trasherdk | 2018-11-16T02:14:44+00:00
You might want to take questions like this to [stackoverflow](https://monero.stackexchange.com/tags/monero-forks/hot)

# Action History
- Created by: steffanjensen | 2018-11-15T18:56:24+00:00
- Closed at: 2018-11-15T19:34:05+00:00
