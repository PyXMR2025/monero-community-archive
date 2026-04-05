---
title: Half of the threads fail with RX470 and AstroBWT
source_url: https://github.com/xmrig/xmrig/issues/2670
author: thespicer21
assignees: []
labels: []
created_at: '2021-11-03T15:11:49+00:00'
updated_at: '2021-11-06T23:32:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When starting a rig with 3 x RX470's I get the errors listed below, these threads fail to mine while the rest work just fine.

```
error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueWriteBuffer
thread #4 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueWriteBuffer
thread #0 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueWriteBuffer
thread #2 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
```

Screenshot -> https://ibb.co/XVQxLQr

I've tried to dig around and it seems that these errors can be due to the wrong intensity settings, but I then ran into 2 major problems trying to fix it :

1) I can't find any information on how to set intensity levels in the official docs

2) The user submitted info I could find relative to intensity settings was all for Monero (and years old at that) - there is virtually nothing about AstroBWT out there.

I'm using xmrig 6.5.13

I'm using the latest AMD drivers (as of the date of this post) and all cards are running on their factory bios.

I'm starting xmrig using a .bat file (not using the config file)


# Discussion History
## Spudz76 | 2021-11-04T00:32:43+00:00
Do you have 11472MB of free RAM?  Does each card have 3824MB free?

## thespicer21 | 2021-11-04T03:00:43+00:00
Hi, I only have 8GB of RAM on this machine, wasn't aware I needed more as I thought the cards were doing the work.
All cards are 4GB versions. I have several of them running on other rigs mining alongside decent Ryzen CPUs and they work fine. Could the crappy old Celeron 1840 in this machine be causing problems even though I'm not CPU mining on this one?

## thespicer21 | 2021-11-06T23:32:36+00:00
Okay there is definitely a problem here with AstroBwt so I'm leaving this here as a warning for others. One of the cards I mentioned above has now died after mining for less than 15 minutes. In total over the past 3 or 4 weeks this combo of XMRig & AstroBwt (mining DERO) has now killed 5 of my cards. 3 x RX470 (4gb), 1 x RX 480 (4gb) and 1x RX480 (8gb). I've been GPU mining since 2017 and never had 1 card die on me before (out of 30 x GPUs). 

When the first one went I figured it was just that cards time to die. After the second I started getting suspicious, but with the third I was convinced that maybe my motherboard or PSU was blowing them, so I tried a completely different MB and PSU for the rest. 

The new combo killed 2 more. 3 of them died when they were the only GPU in the system (direct to board), the last 2 died while on a multi GPU system (using powered USB risers).

I took one of the cards apart and after some testing it turns out the single 1808 fuse near the bottom of the card (the PCIE one) had blown, I haven't checked the others yet but I'm pretty confident that it's going to be the same scenario on all of them. None of them were running hot and none of the ones that blew were running for longer than 20 mins max before they died. Should also note that none of these cards were being over clocked and they were all running on factory Bios'.

I do have several other cards that have been mining DERO for the past couple of months (in single GPU rigs - again fact bios and not overclocked) and they seem to have survived so far so I don't know what to say really. I find it hard to believe that 5 cards would all die coincidentially within the space of a few weeks though. Is there anything about AstroBwt that is particularly hard on GPUs as opposed Ethash or anything else? Any help would be appreciated.

# Action History
- Created by: thespicer21 | 2021-11-03T15:11:49+00:00
