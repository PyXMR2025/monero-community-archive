---
title: RPC hardening options
source_url: https://github.com/Cuprate/cuprate/issues/445
author: hinto-janai
assignees: []
labels:
- C-discussion
- A-rpc
created_at: '2025-04-15T20:15:59+00:00'
updated_at: '2025-05-13T18:48:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
The RPC servers should have some hardening/limiting configuration options, these can be individually applied to both unrestricted/restricted RPC servers.

Potential options:

| Option                  | Type       | Default (unrestricted) | Default (restricted) | Description |
|-------------------------|------------|------------------------|----------------------|-------------|
| request_byte_limit      | `usize`    | ?                      | `300_000` (300kB) | If a request is above this byte limit, it will be rejected.
| response_byte_limit     | `usize`    | ?                      | ? | If the response grows above this byte limit, it will be aborted.
| request_timeout         | `Duration` | ?                      | `Duration::from_secs(60)` | If a request does not complete within the specified timeout it will be aborted.
| max_requests_per_minute | `u64`      | ?                      | `600` (10/s) | Rate limit the amount of requests per minute to this amount.
| max_tcp_sockets         | `u64`      | ?                      | `256` (1024 max open files on linux - other files opened by `cuprated` + leeway) | Max amount of TCP sockets that are allowed to be opened at the same time by the (un)restricted RPC server.

# Discussion History
## SyntheticBird45 | 2025-04-16T01:37:17+00:00
- `restricted_request_byte_limit`: 1MB is way too large. There is zero sensible usecase. You can decrease it to 300kB.
- `restricted_request_timeout`: all for it. This should return a [`REQUEST_TIMEOUT`](https://docs.rs/http/1.2.0/http/status/struct.StatusCode.html#associatedconstant.REQUEST_TIMEOUT)
- `max_restricted_requests_per_minute`: Is this a global rate limiting or per IP ?
- `max_restricted_tcp_sockets`: no comments

## hinto-janai | 2025-04-16T13:50:03+00:00
> 1MB is way too large. There is zero sensible usecase. You can decrease it to 300kB.

Just the default value from:

https://github.com/monero-project/monero/blob/3b01c490953fe92f3c6628fa31d280a4f0490d28/src/cryptonote_config.h#L134

Do you know if all {input * endpoint} lead to responses that are <= 300kB? Having the same value as `monerod` may be good to make sure stuff like `wallet2` calling `/get_blocks.bin` doesn't break.

edit: I was thinking about `response_byte_limit` here, smaller limit for requests should be okay

> Is this a global rate limiting or per IP ?

Global, although we can have other filter layers as well. There's also an argument that more complex options are out-of-scope for `cuprated` and dedicated solutions like nginx/apache/cloudflare would be more appropriate.

## SyntheticBird45 | 2025-04-16T15:22:14+00:00
> Global, although we can have other filter layers as well. There's also an argument that more complex options are out-of-scope for cuprated and dedicated solutions like nginx/apache/cloudflare would be more appropriate.

Global is ok for now.

Ngl I was planning on making a PR for once the RPC server were ready. I really do want per IP rate limiting built-in into Cuprate. Beside the wishlist, even Monero recently started to add some (not-rate) limiting per IP: https://github.com/monero-project/monero/pull/9765

I do understand the middleware argument but with layers like `tokio-governor` it's not that much of a burden to add and maintain and I don't see a single use case where this wouldn't benefit against an eventual attack, as observed with the recent zero day usage on monerod public nodes.

@Boog900 thoughts?

# Action History
- Created by: hinto-janai | 2025-04-15T20:15:59+00:00
