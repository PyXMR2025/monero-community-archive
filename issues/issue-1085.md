---
title: 'Cuprate Meeting #24 - Tuesday, 2024-10-08, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1085
author: moo900
assignees: []
labels: []
created_at: '2024-10-01T18:48:33+00:00'
updated_at: '2024-10-08T18:33:19+00:00'
type: issue
status: closed
closed_at: '2024-10-08T18:33:19+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- Any other business

Previous meeting with logs: #1081

# Discussion History
## moo900 | 2024-10-08T18:33:18+00:00
## Meeting logs
```
boog900: meeting time! https://github.com/monero-project/meta/issues/1085
```
```
boog900: 1) Greetings 
```
```
hinto: hello
```
```
asurar0: Hello
```
```
boog900: 2) Updates 
```
```
boog900: Me: I finished up the blockchain manager PR, started work on `cuprated` config/args and the p2p protocol handler 
```
```
boog900: planning to work on the tx-pool over the next week
```
```
hinto: me: started working on `benches/` https://github.com/Cuprate/cuprate/pull/196
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
hinto: > <@asurar0:monero.social> Hello, 
> I was wondering if the [issue #235](https://github.com/Cuprate/cuprate/issues/235) is specific to the database or if it also affects other areas within Cuprate. If it's the latter, I'd be more than happy to contribute a pull request to address the issue.

this can be used anywhere where conditional static assertions need to be made, it's not specific to `cuprate-database`, there could be other places where they could be used
```
```
asurar0: > <@hinto:monero.social> this can be used anywhere where conditional static assertions need to be made, it's not specific to `cuprate-database`, there could be other places where they could be used

Understood.
```
```
boog900: anything anyone wants to discuss in this meeting?
```
```
asurar0: Is there any fuzzing strategy planned for Cuprate in the long-term ?
```
```
boog900: I am planning to massively extend current testing now that we can generate valid txs without needing to make RPC calls/hardcode data.
```
```
boog900: We already have fuzz testing in some form using `proptest` 
```
```
boog900: like in `epee-encoding` we are using `proptest` like a fuzzer.
```
```
boog900: Is that what you mean?
```
```
asurar0: I was specifically inquiring about network payload fuzzing, particularly for RPC and P2P utilizing external tools. I appreciate the update that tests are being expanded and that epee already incorporates fuzzing capabilities.
```
```
boog900: yeah building out dedicated fuzz tests using actual fuzzers could be a good idea 
```
```
asurar0: Would you like me to open an issue on your repository ?
```
```
boog900: yeah If you want to
```
```
boog900: I think we can end the meeting here 
```
```
boog900: Thanks everyone!
```
```
m-relay: <s​neurlax> I assume cuprated is the best branch for, well, cuprated? my immediate goal is to wrap cuprated for usage over ffi as a proof of concept
```
```
boog900: what would wrapping cuprated look like, just running the binary or trying to call internal components? 
```
```
m-relay: <s​neurlax> just running the binary.  I had assumed any internal components I needed would need to be wrapped for usage over ffi
```
```
boog900: ok you would want the `cuprated-startup` branch, this one has a working binary.
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2024-10-01T18:48:33+00:00
- Closed at: 2024-10-08T18:33:19+00:00
