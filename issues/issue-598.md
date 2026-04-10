---
title: Trimming from config file and lowercase matching
source_url: https://github.com/Cuprate/cuprate/issues/598
author: SyntheticBird45
assignees: []
labels:
- C-proposal
created_at: '2026-04-09T16:35:07+00:00'
updated_at: '2026-04-09T16:35:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
<!--
Note: Please search to see if an issue already exists for this proposal.
-->

## What
1. Strings defined in config files should be trimmed to avoid confusion on errors.
2. We shouldn't depend on a particular casing for strings.

## Why

Regarding 1. As explained in https://github.com/Cuprate/cuprate/pull/596#discussion_r3050155097

Whitespace typos can happen unexpectedly, Most of the time it's because of the user, but sometimes the software/hardware is at fault. On linux, laptop keyboards can register multiple time a key if battery is short.

I believe this is something Cuprate can entirely ignore. In case, this isn't ignored, whitespace typos can cause immense confusion (which i have experienced twice).
Providing the example I gave from the comment above:
 
`proxy = " socks5://user:pass@ip:port"` => `Error: Unsupported proxy:  socks5://user:pass@ip:port`
`proxy = "socks5://user:pass@ip:port "` => `Error: invalid IPv4 socket address syntax`

If this is 3 AM and you are tired, you will read this and assume the software you are using is complete shit. Most will just go to sleep deceived and feeling betrayed. Some will smash their keyboard against their desk. This is dangerous. But we can avoid these injuries.

Regarding 2.
I don't have a lot of argument. From my experience, this is very uncommon to have configuration or string argument requiring an uppercase character. The way we are requiring this is through the use of serde where we need to define the enum variant name. Which in Rust is by convention (and annoyingly warned) as upper camel case. Conceptually users are not there to write struct or enum names.

I'll add that shift typo can also happen tho much more rare than whitespace.

## How
Describe how the proposal could be implemented.


# Discussion History
# Action History
- Created by: SyntheticBird45 | 2026-04-09T16:35:07+00:00
