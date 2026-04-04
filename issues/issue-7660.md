---
title: More flexible definition of RPC ports
source_url: https://github.com/monero-project/monero/issues/7660
author: moneromooo-monero
assignees: []
labels: []
created_at: '2021-04-11T11:49:34+00:00'
updated_at: '2021-04-11T12:11:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
From JaakkoLuttinen[m on IRC:

For monerod, I'd like more flexible definition of various RPC endpoints. Now there are two ports (normal and restricted) and it's sometimes confusing which option affects which. For instance, does `--rpc-login` affect both or just one? How can use different logins for them? 
                          
Personally, I'd like to have three ports: one for localhost that doesn't require any credentials (for other processes on the same machine), one over SSL requiring credentials (for my various wallet clients) and one without credentials but with RPC payments (for any other users). So,  I'd like to see much more flexibility in how RPC is defined: arbitrary amount of RPC ports and each one has its configuration. This is very impractical with command-line options though..

But at least the very minimum: `--rpc-login` could be set only for the restricted RPC port (e.g., `--rpc-restricted-login` which defaults to `--rpc-login` if not given).

Another feature request would be `--rpc-restricted-login`. If not given, it could perhaps default to what's given by `--rpc-login`. However, in that case, I'm not sure how to unset any login requirements with `--rpc-restricted-login` if `rpc-login` is given..


# Discussion History
# Action History
- Created by: moneromooo-monero | 2021-04-11T11:49:34+00:00
