---
title: '[Question] Is there a way to override embedded config?'
source_url: https://github.com/xmrig/xmrig/issues/3345
author: hang3r
assignees: []
labels: []
created_at: '2023-10-18T00:20:12+00:00'
updated_at: '2025-06-18T22:18:58+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:18:58+00:00'
---

# Original Description
As title, command line options don't seem to work so can we change the code somewhere or maybe add a way to dynamically control some of the config and keep all others options the same?

# Discussion History
## geekwilliams | 2023-10-18T18:07:22+00:00
Please refer to the documentation [here.](https://xmrig.com/docs/miner/config) the best option to do what you're asking is to use the config file, and enable the watch option. Some parameters cannot be changed after the miner has started, but most can. 

Addendum: there is also a REST api that can be used to change settings on the fly. [Look here](https://xmrig.com/docs/miner/config/api) for info on how to set that up. 

# Action History
- Created by: hang3r | 2023-10-18T00:20:12+00:00
- Closed at: 2025-06-18T22:18:58+00:00
