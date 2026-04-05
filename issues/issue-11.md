---
title: Need to examinate best approach towards QUIC Obfuscation
source_url: https://github.com/Cuprate/cuprate/issues/11
author: SyntheticBird45
assignees: []
labels:
- C-discussion
- E-help-wanted
created_at: '2023-03-20T21:25:18+00:00'
updated_at: '2024-05-27T01:00:58+00:00'
type: issue
status: closed
closed_at: '2023-12-17T14:02:38+00:00'
---

# Original Description
## Summary

edit: This protocol is named *Perovskite* (reference to the other material used with Cuprate)

One of the features of Cuprate is traffic obfuscation. While we'll certainly implement Levin encryption when it'll be ready, the external protocol (out of Tor) used between Cuprate peers is based on QUIC. This issue is to track down discussions surrounding the design of this protocol.

## Details

### Why QUIC and not another protocol ?

Majority of web communications are TLS-based and since web represent the majority of internet flow, it is legitimate to ask why using QUIC while TCP-based solutions exist. The three main reasons are the following :
- Web traffic is certainly the least suspicious type of activity on internet. Right now majority of websites & browsers use http/2. But http/3 will slowly in the future replace http/1-2 for its performance/security improvements. Therefore QUIC is preferable in the long-term.
- Performance is a concern. Handling QUIC connections is more efficient than TLS connections (because of handshakes). congestion algorithms are smarter, and multiplexing is native to the protocol. So the node will have less overhead for the same amount of connections.
- Mesh network these days (Tor, I2P...) all use TCP-based protocol, so by using a UDP-based protocl, we're less likely to get be *targeted*

### Original plans

The original plan was to implement this protocol using the [Quinn library](https://github.com/quinn-rs/quinn) because it is async (unlike Quiche from Cloudflare which is fairly low-level). It would have implemented the similar specifications to the proposal for Levin protocol from vtnerd : 
- Using Noise_IK handshake so all data sent is uniformly random (QUIC is notoriously known to be easy to fingerprint)
- Randomized offset to obfuscate size, between 0-8192 bytes.

From what I would add a time processing obfuscation with random offset between 0-50ms before sending back a packet.
But it's a bad idea, because for miners, these 50ms would certainly be precious.
So if you have any idea to improve randomness and reduce fingerprinting, please share it with us

### Another plan

Since then, I found out that WebTransport is an experimental protocol being actively stabilized for web browser. WebTransport is basically WebSocket for HTTP/3. A [library from mozilla exist](https://lib.rs/gh/mozilla/neqo/neqo-http3) with support for it. It could be a solution to make network traffic more *w e b*
Original RFC for WebTransport here : https://datatracker.ietf.org/doc/html/draft-ietf-webtrans-http3/

# Discussion History
## SyntheticBird45 | 2023-04-11T20:20:25+00:00
Update: We consider using a runtime generated certificate for using TLS 1.3 with QUIC. This will reduce node overhead by not using the Snow library for Noise protocol

## SyntheticBird45 | 2023-05-02T13:44:24+00:00
*Website fingerprinting on early QUIC traffic*
https://arxiv.org/abs/2101.11871

According to this paper there is 8 different parameters that can be used in order to fingerprint Monero network:
- unique packet size
- packet size count
- packet order
- inter-arrival time
- negative packets (number of packets in the other direction)
- cumulative size
- burst numbers/maxima length/mean length
- total transmission time

## kayabaNerve | 2023-12-16T22:40:00+00:00
@Boog900 Is this an active effort (to implement a brand new P2P network entirely instead of just matching Monero? I'd argue this should be closed for now/recast under the light of "Add support for experimental P2P network solutions" which don't yet lock down to QUIC/express it as an explicit need.

## Boog900 | 2023-12-17T14:02:38+00:00
Nope this is not an active effort, also just noting that there is a PR open to add p2p encryption to monerod which we will also implement in Cuprate.

# Action History
- Created by: SyntheticBird45 | 2023-03-20T21:25:18+00:00
- Closed at: 2023-12-17T14:02:38+00:00
