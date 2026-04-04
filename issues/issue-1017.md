---
title: 'Cuprate Meeting #6 - Tuesday, 2024-06-04, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1017
author: Boog900
assignees: []
labels: []
created_at: '2024-06-01T01:10:22+00:00'
updated_at: '2024-06-09T15:07:08+00:00'
type: issue
status: closed
closed_at: '2024-06-09T15:07:08+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

> Note that there are currently communication issues with Matrix accounts created on the matrix.org server, consider using a different homeserver to see messages.

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: boog900

Main discussion topics:
- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- Any other business

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Previous meeting with logs: #1014



# Discussion History
## Boog900 | 2024-06-09T15:07:08+00:00
logs: 

```
18:00:20 - boog900 (@boog900:monero.social): Meeting time: https://github.com/monero-project/meta/issues/1017
18:00:30 - boog900 (@boog900:monero.social): 1. Greetings 
18:01:03 - SyntheticBird: Hi
18:03:56 - boog900 (@boog900:monero.social): 2. Updates
18:04:58 - hinto (@hinto:monero.social): hello
18:05:36 - boog900 (@boog900:monero.social): Me: I have been continuing to work on the block downloader, got it to a state where it is pretty quick. As mentioned earlier I've also put together a binary that downloads, verifies and stores the blockchain  
18:07:54 - hinto (@hinto:monero.social): me: porting Monero's RPC types, think I found some unused types/routes
18:08:42 - boog900 (@boog900:monero.social): 3. Project: What is next for Cuprate?
18:09:20 - SyntheticBird: <@hinto:monero.social "me: porting Monero's RPC types, ..."> could you provide example?
18:09:51 - boog900 (@boog900:monero.social): Update on the syncing progress: the good news is ity hasn't crashed yet, the bad news it's not as fast as I was hoping 
18:10:50 - boog900 (@boog900:monero.social): but with more tweaking it should be ok, it's not too slow 
18:10:54 - SyntheticBird: <@boog900:monero.social "Update on the syncing progress: ..."> Can you send me the compiled binary over in dm. I would like to test it also with my NVMe
18:12:21 - boog900 (@boog900:monero.social): I'll put the code on GitHub, after the meeting 
18:14:19 - hinto (@hinto:monero.social): SyntheticBird: https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/daemon_handler.cpp#L94
18:14:55 - hinto (@hinto:monero.social): `get_output_keys`, not sure if it's a working endpoint but it isn't documented
18:16:14 - hinto (@hinto:monero.social): it may just be a handler with a non-matching type/name too, e.g. `/get_blocks.bin` -> `GetBlocksFast`
18:19:08 - hinto (@hinto:monero.social): boog900: re: https://github.com/Cuprate/cuprate/pull/146#issuecomment-2145734838 - is there a reason it should be done like this instead of a `method` and `params` field?
18:20:13 - hinto (@hinto:monero.social): e.g. like so: https://docs.rs/jsonrpsee-types/0.22.5/jsonrpsee_types/request/struct.Request.html
18:21:50 - boog900 (@boog900:monero.social): so serde knows what the expected params are. If we keep them separate then we either have to serde in 2 steps or use serde(untagged) which isn't great for performance 
18:22:45 - SyntheticBird: <@hinto:monero.social "`get_output_keys`, not sure if i..."> Nah I think you're right, there is no definition of it and its not part of the `URI_MAP` in `core_rpc_server.h`
18:23:31 - SyntheticBird: I'm not sure whats the usage of this `constexpr const handler_map handlers[]`
18:25:06 - SyntheticBird: I may say somthing stupid but I think `DaemonHandler` is deprecated
18:25:42 - hinto (@hinto:monero.social): boog900: okay, I don't think there's there a big tradeoff we take for doing it that way other than being a bit different, right?
Fri, Jun 7, 2024, 15:58:56 - dllud joined the room
18:26:05 - hinto (@hinto:monero.social): also means the method + param types are nicely linked
Fri, Jun 7, 2024, 16:00:56 - fluorescent_beige joined the room
18:26:48 - boog900 (@boog900:monero.social): <@hinto:monero.social "boog900: okay, I don't think the..."> yeah I don't think so 
18:27:16 - boog900 (@boog900:monero.social): <@hinto:monero.social "also means the method + param ty..."> yep, I would also not expose the `Request` object to the inner request handler 
18:28:13 - boog900 (@boog900:monero.social): so in the handler function extract the method/body field and wrap that in the enum not the whole request object  
18:29:47 - hinto (@hinto:monero.social): does moving my `json-rpc` crate in-tree with the changes sound okay?
18:31:11 - boog900 (@boog900:monero.social): should be ok 
18:31:46 - boog900 (@boog900:monero.social): we could also do something similar for the response object 
18:36:42 - SyntheticBird: We're 37 minutes in. Is the binary still alive ?
18:36:48 - boog900 (@boog900:monero.social): Anything else people want to discuss?
18:37:16 - SyntheticBird: <@boog900:monero.social "Anything else people want to dis..."> blog
18:37:23 - SyntheticBird: public report of progress
18:37:33 - boog900 (@boog900:monero.social): <@syntheticbird:monero.social "We're 37 minutes in. Is the bina..."> It is but I stopped it to test some changes 
18:37:51 - boog900 (@boog900:monero.social): I started it back up again 
18:38:17 - hinto (@hinto:monero.social): that's all for me - I expect boring porting and json-rpc work for the next few days
18:38:36 - hinto (@hinto:monero.social): boog900: as expected, is the bottleneck in `cuprate-blockchain`?
18:40:17 - boog900 (@boog900:monero.social): <@syntheticbird:monero.social "blog"> This is something I want to do, but I want to do it at the right time
18:40:54 - boog900 (@boog900:monero.social): <@hinto:monero.social "boog900: as expected, is the bot..."> I *think* so
18:42:35 - hinto (@hinto:monero.social): any notable difference between heed/redb?
18:43:57 - boog900 (@boog900:monero.social): redb is a lot slower for the first 10,000 blocks 
18:44:26 - boog900 (@boog900:monero.social): but I didn't really give it a chance 
18:45:12 - boog900 (@boog900:monero.social): If I am honest I am really happy that we are syncing without anything breaking considering this is literally the first sync 
18:46:00 - SyntheticBird: Good mindset
18:46:08 - SyntheticBird: Good job hinto boog900
18:47:21 - hinto (@hinto:monero.social): ....give it time, I guarantee things will break :)
18:48:02 - boog900 (@boog900:monero.social): hinto: do you have any opinions on publishing a blog post on cuprate.org on current progress? 
18:49:49 - hinto (@hinto:monero.social): sure, no idea how to set that up though - I can review writing though
18:50:17 - hinto (@hinto:monero.social): I'd recommend following https://blog.rust-lang.org style
18:51:19 - hinto (@hinto:monero.social): i.e. info, some impl details, no big opinions
18:52:26 - boog900 (@boog900:monero.social): <@hinto:monero.social "i.e. info, some impl details, no..."> a small political statement at the start? 
18:52:37 - boog900 (@boog900:monero.social): /s 
18:54:00 - hinto (@hinto:monero.social): propaganda is on the homepage only
18:54:01 - SyntheticBird: *SyntheticBird is preparing the drama dictionnary*
18:56:24 - SyntheticBird: As said in other channels. I've mirrored Cuprate repository in Librejo, so in case of takedown or maintenance, Librejo is at worst 8 hours behind
18:56:50 - boog900 (@boog900:monero.social): If thats all I think we can end here
18:57:02 - SyntheticBird: yes
18:57:11 - SyntheticBird: Thx everyone
18:57:25 - boog900 (@boog900:monero.social): alright then, thanks everyone 
18:58:28 - hinto (@hinto:monero.social): thanks
```

# Action History
- Created by: Boog900 | 2024-06-01T01:10:22+00:00
- Closed at: 2024-06-09T15:07:08+00:00
