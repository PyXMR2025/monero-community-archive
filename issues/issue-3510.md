---
title: '[feature][discussion][bug] It''s difficult to know if one''s helping the Monero
  network - Feature: Status Footer'
source_url: https://github.com/monero-project/monero-gui/issues/3510
author: ghost
assignees: []
labels: []
created_at: '2021-05-26T23:16:16+00:00'
updated_at: '2021-05-26T23:16:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Background: 

In the current Monero GUI, it's challenging (especially for a newb) to quickly diagnose whether or not your full node is actually helping the network via p2p / RPC. Additionally, it's useful to be able to quickly see that your node is NOT participating in p2p / RPC for security purposes. In a GUI app, I don't believe one should have to type cli commands in a hidden panel to see the status of these items.

I've seen posts from people who say they've been running the GUI with a full node for years thinking they were seeding the network, but had no idea their network port wasn't open as well as others who express difficulty in getting p2p set up in the first place. 

I think there are others who would be eager to participate in p2p seeding with a UI nudge and tutorials that can quickly point users at a status bar values in the GUI.  

Relevant posts:
- https://twitter.com/Andr3wJackson/status/1396538165159022595?s=20
- https://www.reddit.com/r/Monero/comments/nlm0vi/someone_with_good_knowledge_to_make_some/
- https://www.reddit.com/r/Monero/comments/kkr04n/infographic_running_a_node_which_ports_should_i/

I think having an informational status bar footer similar to what one would see in the Deluge torrent app, or even Bitcoin Core node would be helpful in providing this information (also useful in tutorials... check the footer- do you have p2p peers?)  

Beyond that, the footer icons could potentially provide more info in a tooltip sort of way, or act as links to the relevant pages in the GUI for updating the relevant settings.    

This is a very quick rough mockup of what I'm proposing:

![image](https://user-images.githubusercontent.com/84093240/119742551-abdbcc80-be4d-11eb-8151-3dc77001f16b.png)

Most of these items are self explanatory, but:

1. Full / Pruned / Remote /  Bootstrapping Node (Could use yellow dot when user is using Remote as a nudge to use Full/Pruned)
2. Node Storage Use (could also do storage used/storage available)
3. Out: out peers
4. P2P: in peers- Listing this value as 'p2p' rather than 'in' is a very easy way for users to know if their node is participating in P2P
5. RPC: rpc peers 
6. Earth/TOR: Perhaps a way to know if your node is a full public node and / or using TOR

I think that color or different icons could perhaps nudge users in a direction that helps the Monero network, while also cautioning them when certain things are putting their network at heightened security risk. I'm a little shaky on RPC/Tor stuff, but it would be useful for the user to know if their node is a 'full public node', running on TOR, and/or if their RPC port is open to the public.   




# Discussion History
# Action History
- Created by: ghost | 2021-05-26T23:16:16+00:00
