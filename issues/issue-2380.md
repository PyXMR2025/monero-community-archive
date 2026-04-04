---
title: Remove CloudFlare DDoS protection, explore other options
source_url: https://github.com/monero-project/monero-site/issues/2380
author: rottenwheel
assignees: []
labels: []
created_at: '2024-10-08T01:47:29+00:00'
updated_at: '2025-11-08T17:46:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If getmonero.org is using Nginx as the webserver implementation, [this](https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS) could be a great alternative to look into and test, that gets rid of dependency on CloudFlare's evil practices, yet keeps us protected from DDoS attacks. Some shenanigans pulled by CF highlighted [here](https://0xacab.org/dCF/deCloudflare/-/blob/master/readme/en.md).

You may get an idea of how it may look by visiting the Nitter instance [Xcancel](https://xcancel.com/).

# Discussion History
## librootorg | 2025-11-08T17:46:54+00:00
Relying on Cloudflare is fundamentally at odds with Monero's privacy goals ([our post](https://libroot.org/posts/getmoneroorg-should-move-beyond-cloudflare/)). Other projects, like Tor and WikiLeaks, manage without Cloudflare, so it seems feasible for getmonero.org as well. The project `Nginx-Lua-Anti-DDoS` mentioned by @rottenwheel could work, but it relies on client-side JavaScript, which is undesirable, getmonero.org should function fully without requiring client-side JavaScript.

# Action History
- Created by: rottenwheel | 2024-10-08T01:47:29+00:00
