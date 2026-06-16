---
title: Hide certain data in logs
source_url: https://github.com/Cuprate/cuprate/issues/540
author: Boog900
assignees: []
labels:
- C-request
created_at: '2025-08-29T17:39:33+00:00'
updated_at: '2026-06-15T08:42:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

## Feature
Hide certain data from the log file, like stem tx hashes or onion addresses, with an option to show these details. 

## Why
To prevent the log file from being a target.

## Additional context
arti has a crate for this: https://docs.rs/safelog/latest/safelog/index.html

and some guideline for arti: https://tpo.pages.torproject.net/core/arti/contributing/for-developers/logging/


# Discussion History
## SyntheticBird45 | 2025-08-29T18:23:07+00:00
Interesting. May this behavior be gated behind a release cfg? Or will this be opt-in + flag/config line to disable

## Boog900 | 2025-08-29T19:13:22+00:00
making it opt in would be bad as most wont, it would be opt-out by config/command line yes 

## MavenRain | 2026-06-13T09:20:55+00:00
I took a first pass at this using `safelog` (already a workspace dep).  PR adds the opt-out mechanism (a `tracing.redact` config option + `--no-redact` flag, redacting by default per the thread above) and applies it to the transaction-hash log sites in `cuprated`'s txpool.  The peer-address / onion-address sites live in the `p2p-core`, `p2p`, and `address-book` library crates, which don't currently depend on `safelog`;  I'd be happy to extend there in a follow-up if you're OK adding the dep to those crates.  I left the startup `info!("{config}")` dump and block-hash logs out of scope on purpose (notes in the PR).

## redsh4de | 2026-06-13T20:28:17+00:00
This is a bit radical, but thoughts on additionally refusing to start the node if:
1. log redaction has been turned off
2. a node has any RPC enabled on a non-local address (publically available)

Effectively by default, only allowing to disable redaction if the RPC is not available to the outside - i.e. local networks, testing, development, etc. The reason is to make the log file be a target as difficult as possible and an impossibility under normal circumstances unless the user really wants to

This behaviour could be overriden with a `i_know_what_im_doing_allow_unredacted_public_logs` flag, similar to how we gate a unrestricted RPC on a non-local IP.

## Boog900 | 2026-06-14T11:09:56+00:00
RPC does not expose the log file though so I am unsure of the gain there?

## redsh4de | 2026-06-14T11:23:47+00:00
it's moreso making sure that in case the RPC is exposed to the public - meaning users other than the node operator are able to connect to it - redaction should be a especially strong default in that case, since the logs can now contain third party data that can be targeted by potential adversaries

ex: if Eve knows that Alice uses Bob's node, Eve can - subpoena for data, compromise Bob's infra, etc like it has happened with Tor node operators

## Boog900 | 2026-06-14T12:06:14+00:00
Ok that makes sense. What data would we hide though? I doubt just hiding tx hashes will be enough, you would need to hide addresses of connections. As otherwise knowing the time a tx was sent will be enough to get the number of potential txs quite low. Hiding addresses is not a great idea though as it makes it harder to find bad actors.

Maybe for certain requests we hide the address that sent it? 

## redsh4de | 2026-06-14T15:44:49+00:00
Yeah, i think we can hide the IP for transaction requests, etc, things that equal normal use

In #644 it currently hides:
- transaction hashes
- onion addresses
- clearnet addresses (partially, first octet's visible)
- proxy auth info

For the bad actor finding angle - we def could selectively reveal the plain address depending on the event type. For ban/unban events, and maybe when a peer sends a malformed message or something that drops the connection, basically anything that cannot happen normally.

For that we might need some kind of classifier to distinguish events that we redact the address for, and others that we publish it for

## redsh4de | 2026-06-15T08:42:52+00:00
Updated #644 to reveal the IP on a peer ban event

# Action History
- Created by: Boog900 | 2025-08-29T17:39:33+00:00
