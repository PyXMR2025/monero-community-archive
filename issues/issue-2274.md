---
title: '[Discussion] i2p/Tor Network Screen Designs'
source_url: https://github.com/monero-project/monero-gui/issues/2274
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2019-07-07T22:09:04+00:00'
updated_at: '2026-03-16T01:55:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am continuing a discussion about Monero GUI network connection options. Note that this is subject to change and improvements. [Related Reddit discussion](https://www.reddit.com/r/Monero/comments/bysgry/discussion_gui_network_screen_designs/)

This latest iteration better separates specific options and descriptions with the type of node or connection they are related to. As always, I tried to keep simple mode especially as easy as possible, with a simple on/off.

# Startup Screens

Simple mode: 
![image](https://user-images.githubusercontent.com/12520755/60774335-9c77fc80-a0d8-11e9-83b0-934e415628fc.png)

Expert mode: 
![image](https://user-images.githubusercontent.com/12520755/60774361-aac61880-a0d8-11e9-99d9-3a2ee280190d.png)

# Simple Mode

*Note: default uses i2p for broadcast and syncing new blocks. It falls back to clearnet for old blocks (>1 week? >1 month?)*

![image](https://user-images.githubusercontent.com/12520755/60774365-ba456180-a0d8-11e9-8145-481aa3edc5e2.png)

![image](https://user-images.githubusercontent.com/12520755/60774368-c2050600-a0d8-11e9-84f4-8540a3b2b816.png)

# Expert Mode, Random Nodes and Manual Untrusted Nodes

*Note: if only i2p is selected, all options for Tor are removed. Manual may be removed too.*

![image](https://user-images.githubusercontent.com/12520755/60774377-d517d600-a0d8-11e9-8940-2aa417212d5b.png)

![image](https://user-images.githubusercontent.com/12520755/60774379-dc3ee400-a0d8-11e9-98cf-78cd4ab036a3.png)

![image](https://user-images.githubusercontent.com/12520755/60774382-e365f200-a0d8-11e9-88a7-ca4c9e3430d6.png)

# Expert Mode, Manual Trusted Nodes

*Note: requires https://github.com/monero-project/monero/issues/5590. Automatic mode uses clearnet, i2p, or Tor to connect to the custom node as necessary depending on the TLD.*

![image](https://user-images.githubusercontent.com/12520755/60774389-f973b280-a0d8-11e9-8198-a3264d8a7a9a.png)

![image](https://user-images.githubusercontent.com/12520755/60774392-009ac080-a0d9-11e9-83a0-161e929d1b3b.png)

![image](https://user-images.githubusercontent.com/12520755/60774394-08f2fb80-a0d9-11e9-8c14-ae2780cdca98.png)

![image](https://user-images.githubusercontent.com/12520755/60774397-101a0980-a0d9-11e9-85cf-a245f2ec027f.png)

# Expert Mode, Local Node

![image](https://user-images.githubusercontent.com/12520755/60774408-45bef280-a0d9-11e9-91ea-d6aa26bc1776.png)

![image](https://user-images.githubusercontent.com/12520755/60774410-4eafc400-a0d9-11e9-88fb-e4520656fedd.png)

![image](https://user-images.githubusercontent.com/12520755/60774414-54a5a500-a0d9-11e9-9e97-451dcffa3f96.png)

---

Please leave feedback! This is the third main design iteration. Comment on the basic layout, the wording, setting organization, and more. Let's get some discussions going so that this important feature can be implemented in 0.15, and for the implementation to be super awesome for all users.

# Discussion History
## antanst | 2019-07-08T04:42:48+00:00
Good stuff :-)

I believe it's unclear what the line/circle colors mean. What does it mean for a link to be gray or yellow? Why is the Monero Network red sometimes? It's like warning people that connecting to the network is bad.

IMHO just highlighting the link where the choices apply to would be less confusing.

## sebszz | 2019-07-08T22:55:22+00:00
Good stuff!

screenshot #1:  "Would you like to enable this feature? " this sentence should be as last, before the two buttons. 

Second paragraph, I would remove it. You could show as a possible reason if there were some problems with connecting to i2p or tor.

The two options below the paragraphs don't feel/look like buttons. I would make them look like on the 2nd screenshot, orange. Two buttons next to each other, centered. Also buttons text could be: "Yes, protect my connection" and the other "No thanks"

Screenshot #2: 
- i2p logo poor quality
- last two sections - Why text links? Why they don't have orange buttons like the two sections above? Orange buttons could be bit smaller :)

Other ones, not quite sure what green and red suggest...

Btw. Is it possible to wrap some words in <abbr> (https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_abbr_test)  tag to quickly explain what it is? For example, node, tor, i2p. Not just here but it would be beneficial to do it everywhere. That would save time to explain bits over and over and save time for the user to scan the internet for answers.

Best.

## dginovker | 2019-07-10T18:16:25+00:00
imho, we shouldn't add yet another configuration screen to simple mode. Perhaps add it to the Mode selection with radio buttons, like this? 
![image](https://user-images.githubusercontent.com/32943174/60993769-1c8ea400-a31d-11e9-868a-84019c19a3e2.png)
This way, in Advanced Mode, you can just clarify how you want to use I2P and Tor, and in Simple Mode, it's done by default.

Lastly, if the selected method fails while the user is in simple mode, they get a popup prompting them to change it.


## SamsungGalaxyPlayer | 2019-07-10T19:19:52+00:00
@dginovker we still need to present an option to users in simple mode, since using i2p is more dangerous than using Monero in some jurisdictions.

## adrelanos | 2019-10-28T13:55:38+00:00
> since using i2p is more dangerous than using Monero in some jurisdictions.

Citation required. Non-obvious to me that this is the case.

## adrelanos | 2019-10-28T14:19:40+00:00
When Whonix (or similar) is detected [1], which torifies all connections by default, and to [prevent Tor over Tor](https://www.whonix.org/wiki/DoNot#Prevent_Tor_over_Tor_Scenarios): don't show any of these new screens?

[1] See for detection: https://github.com/monero-project/monero-gui/issues/2421


## eyedeekay | 2021-11-23T04:00:23+00:00
Hey so this seems a little stalled and I'd like to take it up sometime next month. How prepared are you guys for a PR to do accomplish this? Do have you settled o a design yet? Also, have you considered "hybrid" nodes where I2P-using nodes do communicate with the clearnet, but only over Tor, in order to act as anonymous bridges between the networks?

## eyedeekay | 2021-11-29T03:21:24+00:00
I'm sorry I wasn't able to make the meeting today, I was tied up elsewhere and really underestimated how much communication I would need to catch up on when I got back. If possible, could we do some of this discussion asynchronously, here on the github issue? There are a few things of note for me re: this process


 * Setting up a monero-over-I2P node is just a matter of setting up tunnels for that node and informing the monero node of the destinations of those tunnels.
 * If there's an I2P router there already available to use, then we can just run a new instance of I2PTunnel with our preferred tunnel configuration. This also means that it would be easy to turn the monero daemon into an I2P plugin, which might be useful for increasing the number of users running long-term nodes and be a way of providing automatic updates.
 * If there's not an I2P router there already available to use, then we could:
  1. Do nothing. Assume the user never wanted to use I2P.
  2. Use I2P-Zero by including it in the monero `.zip` or `tar.gz` or other package. In this case the monero daemon would have to first discover if an I2P router exists, then if it does not, start I2P-Zero instead. Then the monerod would connect to the I2P-Zero control port in order to set up the tunnels it needs and read the destinations back from the control port.
  3. "Embed" a C++ I2P router using the `libi2pd` library which powers the `i2pd` C++ router. The `i2pd` project uses this library and makes it available to others to use, and it accepts identical arguments to the `i2pd` executable. In this case the monero daemon would need to read the `.dat` keys written by the i2pd router and convert them into `b32.i2p` addresses.
 * I like **2.** partly because I've always liked Zero. I also like **2.** because, since the last I2P-Zero release I2P has added support for custom update servers and custom update post-processing. If I could change two things about `I2P-Zero`, one of those two things would be making it automatically update. An I2P-Zero UpdatePostProcessor could distribute updates using Bittorrent-over-I2P for efficiency and security, and would be able to update a "bundle" of any kind, including updating the `monero` executable, resources and libraries as well. **3.** also has some appeal but lacks the auto-update mechanism.

I will try to be on Matrix all this week.

## SamsungGalaxyPlayer | 2021-11-29T17:19:59+00:00
@eyedeekay I think including i2p-zero is a good idea. Not all users need to use it of course, but a user should be able to toggle it on without needing to worry about opening up another application manually. My personal vote is also for 2.

Can people do clearnet queries through i2p? I'm under the impression that i2p has many limitations there. One of the benefits with Feather defaulting to using Tor is that all the external connections like price feed, Monero CCS, and Reddit are hidden behind Tor. We don't need to do all of this in the GUI (just price queries for fiat prices). i2p seems useful for node connectivity, but I'm a little skeptical if it provides the most comprehensive solution for things most users want.

## eyedeekay | 2021-12-01T15:37:16+00:00
Yeah we don't normally do exit traffic ourselves, but there are a handful of volunteers who run exit proxies(outproxies) which could hypothetically be configured for Monero. The use of a general exit proxy may not be required, though. What would happen in the case of Monero for instance is that some nodes would need to run in 2 modes at once, either with Tor+I2P or with Clearnet+I2P, to communicate between the I2P and non-I2P sides of the network. I usually refer to this technique as being a "Bridge" and IMO it's generally a little easier for individuals to pull off than acting as a general exit proxy, since one side of a bridged connection may not be anonymous.

The chart of meaningful available configurations and their characteristics:

 * Clearnet Only - As private as Monero 
 * Clearnet+I2P - As private as Monero, communicates with some anonymized connections to help I2P-Only users
 * Tor Only - Monero, but with connections universally routed Tor
 * Tor+I2P - Monero, with clearnet and `.onion` connections routed over Tor
 * I2P Only - Monero, only making connections over I2P. Optional SOCKS exit proxy? Exit proxies run for expressly monero purposes might be possible.


## SamsungGalaxyPlayer | 2021-12-06T16:12:35+00:00
| Item to Hide | Options | Comment |
| --- | --- | --- |
| Sync old blocks | Clearnet (fast), Tor (slow), i2p (slow) | Some performance testing is needed, but most users will likely opt to sync old blocks over clearnet. Feather does not hide this by default. |
| Sync very recent blocks | Clearnet (fast), Tor, i2p | Users get better "bang for the buck" with Tor/i2p here. Syncing very recent blocks with Tor/i2p increases plausible deniability versus an ongoing clearnet connection. Feather does not hide this by default (I think). |
| Broadcast transactions | Clearnet (no protection), Tor, i2p | This is the most important information to hide, hands down. Tor and i2p both address this. Feather hides this with Tor by default. |
| Price API lookups | Clearnet (no protection), Tor, i2p (weak support) | Tor is the best trade-off here as things currently stand, because it's far better for reaching clearnet services. Unless someone wants to run a great price API through i2p, this probably won't change. Feather hides this with Tor by default. |

@eyedeekay

What are the benefits to using i2p over Tor for these actions by default? If we were to protect broadcasts to remote nodes by default, would i2p be noticeably better than using Tor?

Supporting i2p makes sense from the perspective of someone connecting to their own Monero node behind a double-NAT. I'm less sure it makes sense for a more novice user connecting to a rando remote node.

Here's a table of the most realistic 2 default options. Other options like Tor-only are possible but shouldn't be a default for performance reasons.

I Item to Hide | Option 1 Default | Option 2 Default |
| --- | --- | --- |
| Sync old blocks | Clearnet | Clearnet |
| Sync very new blocks | Tor | i2p |
| Broadcast transactions | Tor | i2p |
| Price API lookups | Tor | Tor |

In my mind, it's a matter of determining if there's a material benefit to using i2p over Tor by default for those 2 items.

## eyedeekay | 2021-12-07T18:35:15+00:00
Unfortunately I'm not always going to be able to say which one is better or not, because there are sometimes just going to be trade-offs. I've grown to think that comparing I2P and Tor as direct competitors is not usually very productive and distracts from the ways they can be mutually beneficial. Tor's good at exit diversity, I2P's good at relay diversity, etc. One clearer advantage we have is that once you're well-integrated into I2P it's pretty difficult to disconnect your router by killing off connections to your peers. Some of it will also depend on what decisions we make when integrating I2P. I'll try to explain while I answer your questions, most of my theses will revolve around our relatively extensive configurability of tunnels. That said, I think this is probably a case where it makes sense to use them together as a default.

> What are the benefits to using i2p over Tor for these actions by default?
> If we were to protect broadcasts to remote nodes by default, would i2p be noticeably better than using Tor?

 - Sync old blocks: There would appear to be little obvious benefit here, but there is a non-obvious benefit, which is that I2P doesn't need to use long tunnels and it's in fact very easy to treat I2P as a layer of obfuscation-only. A pair of zero or one-hop tunnel over I2P would tend to be very fast, and be indistinguishable from other I2P traffic. Sort of like what would happen if you used a pluggable transport without Tor. Hypothetically, this would help obscure the presence of a Monero node on the device, albeit in favor of an I2P one.
 - Sync very new blocks: Roughly identical benefits to Tor for many purposes. However since we use obfuscated transports, and because I2P participating tunnels(traffic you route for other people) and client tunnels(traffic you initiate yourself) are not straightforwardly distinguishable from eachother, participating in I2P routing may make it more difficult do identify *when* your node is working on syncing new blocks.
 - Broadcast Transactions: Roughly identical benefits to Tor for all intents and purposes. Obfuscation is cool but I'm not even sure it makes a difference here.
 - Price API lookups: No benefit for most users. Being able to host one's own Price API would be neat for enthusiasts, but not ideal for most users.

> Supporting i2p makes sense from the perspective of someone connecting to their own Monero node behind a double-NAT. I'm less sure it makes sense for a more novice user connecting to a rando remote node.

I think the strongest argument is probably(and surprisingly) for the initial syncing.

## eyedeekay | 2021-12-17T20:28:05+00:00
Potentially relevant discussion also happening here: http://zzz.i2p/topics/3219-socks-outproxy-plugin and here https://i2pgit.org/i2p-hackers/i2p.i2p/-/merge_requests/46 

We are considering the possibility of enabling I2P to forward non-I2P requests to a proxy which is running locally, with a default of `localhost:9050`. This would enable I2P to handle Tor connections as well.

## IamOneInx | 2026-03-16T01:55:19+00:00
Iamoneinx Kerry
· 1 second ago

Hello I am Trying to make a claim...

Claiming this bounty — working implementation ready for review.

Fork: https://github.com/IamOneInx/monero-gui/tree/feat/i2p-integration
PR: https://github.com/monero-project/monero-gui/pull/4574

What's implemented:

Bundled i2pd binaries for macOS, Linux x86_64, Linux aarch64, and Windows
with SHA256 hash verification at build time
I2pManager C++ class manages i2pd as a subprocess via QProcess — same
pattern as P2Pool, not embedded libi2pd source
Settings → Node: enable checkbox, start/stop button, live status, port
config, autostart toggle
monerod automatically receives --tx-proxy i2p,127.0.0.1:7656 when i2p is
enabled — no CLI required
Optional --anonymous-inbound support for inbound i2p peers
Tested and working on:

✅ macOS (Apple Silicon)
✅ Linux aarch64 (Raspberry Pi 5, Debian 13)
✅ Windows (code + installer support complete)
User opens Settings → Node → checks "Enable I2P router" → i2pd starts →
monerod routes through i2p. No command line, no separate install required.

Payout address:
475RmTUv6zoeuk3nfme75Ea7X3oa9UctqBkXwFTboydNg4wfK5g6Bqwd22BWjyUxAv6YTqYDaYcb9S
hxb5XUvVpmGaw6SQ2

— IamOneInx

# Action History
- Created by: SamsungGalaxyPlayer | 2019-07-07T22:09:04+00:00
