---
title: 'Feature request: Add operating system and platform to get_info'
source_url: https://github.com/monero-project/monero/issues/9031
author: 4rkal
assignees: []
labels: []
created_at: '2023-10-22T15:21:45+00:00'
updated_at: '2023-10-30T15:18:00+00:00'
type: issue
status: closed
closed_at: '2023-10-30T15:18:00+00:00'
---

# Original Description
## Description
Add a feature to return the operating system that a node is running on and the cpu architecture. 

## Why?
Quoting from [The Tor BSD Diversity Project](https://torbsd.github.io/)
```
While recognizing the Tor Project is a dynamic open source project with a vibrant community, 
we are also concerned with the overwhelming GNU/Linux monoculture that is an Achilles’ Heel. 
Monocultures in nature are dangerous, as vulnerabilities are held in common across a broad spectrum. 
In contrast, diversity means single vulnerabilities are less likely to harm the entire ecosystem. 
In a global anonymity network, monocultures are potentially disastrous.
A single kernel vulnerability in GNU/Linux impacting Tor relays could be devastating. 
We want to see a stronger Tor network, and we believe one critical ingredient for that is operating system diversity.
```
This also applies to monero!
To put this simply. We need to understand what platforms are more popular, so that we are able to encourage users to switch platforms.

## Suggested implementation
I am not very experienced with the code base but this is roughly how I think it should be implemented:
By default, include OS information in the /get_info response, with an option to disable that eg `--disable-os-info` flag.

# Discussion History
## iamamyth | 2023-10-22T17:03:58+00:00
Disclosing a server's operating system makes it an easier attack target and should certainly not be done by default.

Setting aside security-related objections, the core mechanism you've proposed seems flawed:
 
> We need to understand what platforms are more popular, so that we are able to encourage users to switch platforms.

How would this encouragement work? Presumably there's a motivation behind the popularity of certain platforms. Do you really expect users to run a totally different OS in the name of "platform diversity for Monero"? Assuming an initial imbalance large enough to justify the initiative, you'd need a large number of users to switch.

## 4rkal | 2023-10-22T18:33:50+00:00
Maybe having this by default is not a good idea. But having an optional flag would really help gather some statistics. 
About how we will make users switch. I mean people are already running nodes, using p2pool etc. All of that to further decentralize the network. This is the same thing. For most experienced Linux users (most node runners) switching to something like OpenBSD shouldn't be too hard.

## plowsof | 2023-10-22T18:46:45+00:00
ask a privacy conscious user if they wish to opt-in to having usage statistics collected. how do you want people to know about it? show a popup? not a good look. this was discussed today https://github.com/monero-project/monero/issues/9031#issuecomment-1774166565 




## iamamyth | 2023-10-22T19:32:50+00:00
The threat model here also makes no sense: Imagine someone has a zero day and decides its worthwhile to use it on a Monero attack. Assuming people actually respond to the network composition data, that actor could simply start faking the data to drive the composition towards the vulnerable OS.

## 4rkal | 2023-10-23T04:42:27+00:00
If someone has the resources to spin up a lot of nodes I don't think that's the first thing they'll try.

## iamamyth | 2023-10-23T17:54:26+00:00
> If someone has the resources to spin up a lot of nodes

Not a requirement to influence sampling of get_info. For example, proxying would work, as might an approach specifically targeting the sampling methodology. Your proposal effectively tries to wish away Sybil attacks.

# Action History
- Created by: 4rkal | 2023-10-22T15:21:45+00:00
- Closed at: 2023-10-30T15:18:00+00:00
