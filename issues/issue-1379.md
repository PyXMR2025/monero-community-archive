---
title: 'Cuprate Meeting #101 - Tuesday, 2026-05-05, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1379
author: moo900
assignees: []
labels: []
created_at: '2026-04-28T18:59:23+00:00'
updated_at: '2026-05-05T19:13:20+00:00'
type: issue
status: closed
closed_at: '2026-05-05T19:13:22+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

1. Greetings
2. Updates: What is everyone working on?
3. Project: What is next for Cuprate?
4. Any other business

Previous meeting: #1376

# Discussion History
## MarkoPohlo | 2026-05-05T10:03:15+00:00
Would love to briefly discuss a formulated CCS proposal we've been working on, as discussed in last week's meeting. 

Palina (CTO) and Guy (formal methods engineer) will provide a short summary and ask the community for feedback/answer any technical questions.

## Boog900 | 2026-05-05T10:35:36+00:00
Sure, will add that to the agenda. You could post it here too, to give people a chance to read before the meeting, but if you would rather wait then that's ok.

## MarkoPohlo | 2026-05-05T12:14:29+00:00
Good idea, please see the below overview.

Cuprate Fuzzing
Ada Fuzzers and Compatibility Overview

Ada developed two fuzzing harnesses to fuzz over Monero.

Harness 1 (C++): Direct fuzzing with internal function calls

This harness directly instantiates monero's core_rpc_server object and calls into its internal handlers for the rpc methods with fuzzing data. The fuzzing utilities they created to do this are heavily coupled with the C++ data structures in the monero repository and so are not suitable to be adapted for fuzzing over Cuprate.
Ada developed the harness in this way because it can run without any inter-process communication or I/O, which is required by OSS-Fuzz to preserve determinism.

Harness 2 (Python): External RPC requests with full daemon

This harness launches the full monerod daemon as a sub-process and uses fuzzing utilities written in Python to submit RPC requests to the server's endpoints. This setup is well suited for fuzzing over Cuprate as it should be possible to replace monerod with cuprated and submit the same RPC requests from the Python fuzzer.

Python Harness Overview

https://github.com/AdaLogics/monero-e2e-fuzzing

Files

e2e.py

Contains the core logic for building, launching, fuzzing, and generating reports.

e2e_fuzzer.py

Contains all of the fuzzing utilities for generating fuzzed RPC requests and submitting them.

e2e_serialise.py

A utility for binary serialization of an RPC request for binary endpoints. Uses a serializer utility program that resides under monero_rpc_serializer/

Usage

The first step is to clone OSS-Fuzz in the root of the repo. They use the monero project in the OSS-Fuzz repository to build monerod with all of the instrumentation used for fuzzing (sanitizers and coverage collection).
After that, simply invoke e2e.py. It takes a few basic arguments to specify iteration count and directory locations, and then it handles everything needed to build, run, and write the report.

A Plan for Adapting the Python Harness to Cuprate

A checklist for implementing:

* Create a build target for cuprated with sanitizers and coverage collection instrumentation for fuzzing
* Change e2e.py to parameterize which server it launches so that cuprated can be launched instead of monerod
* Make sure e2e.py knows how to generate the coverage report for cuprated after fuzzing is over
* Add an option to launch monerod and cuprated and send the fuzzed requests to both, and compare the results. This is known as differential fuzzing, and will help assure that Cuprate is implemented correctly.

A Request for Feedback

The current Python fuzzer launches monerod with these parameters:

monerod \
  --offline \
  --regtest \
  --rpc-bind-port <port> \
  --confirm-external-bind \
  --disable-rpc-ban

The --offline and --regtest options help with launching monerod in a way that is suited for fuzzing.
It currently isn't clear if cuprated has the same capabilities. More investigation is needed, and feedback from the Cuprate team would be appreciated.


## moo900 | 2026-05-05T19:13:20+00:00
## Meeting logs
```
boog900: 1) greetings
```
```
redsh4de: hi!
```
```
gtrepta_rv: o/
```
```
palinatolmach: hey everyone!
```
```
boog900: I don't think syn is here today
```
```
boog900: 2) updates
```
```
boog900: Continuing to work on PRing my RPC changes, also began to relook at the FCMP stuff I started a while ago.
```
```
boog900: I added a regtest mode to help with testing RPC too
```
```
redsh4de: me: submitted two PRs for hardening folder permissions on windows, and for passing the ki vec created in consensus to cuprated, rebased existing PRs
```
```
gtrepta_rv: I wrote up a plan to get Ada's end to end fuzzer for `monerod` to work with `cuprated`
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: Here is that plan: https://github.com/monero-project/meta/issues/1379#issuecomment-4379087538
```
```
boog900: AFAICT this wouldn't be fuzzing consensus right?
```
```
gtrepta_rv: I'm not entirely sure. It tests against the RPC endpoints, so whatever those cover.
```
```
boog900: This was initally proposed as a consensus fuzzer, an RPC fuzzer wouldn't really work at the moment as the RPC interface is still being built
```
```
boog900: You would need to use the consensus crates API, so I don't think you would be able to reuse any monerod fuzzers.
```
```
palinatolmach: We'd be reaching consensus code via some endpoints (`send_raw_transaction` and `submitblock` are both covered by Ada Logics' harness), so we planned to suggest that this trial month's work would focus on standing up the harness - which means it'd inherit the RPC-reachable consensus surface from what's there in the `monerod` harness, with the best-effort valid-transaction generation done as time permits. 
```
```
gtrepta_rv: I see
```
```
palinatolmach: But that's fair, thank you for the feedback! Do you have a timeline for the RPC interface? Or a list of the supported endpoints?
```
```
palinatolmach: * But that's fair, thank you for the feedback! Do you have a timeline for the RPC interface? Or a list of the supported endpoints that you could share with us?
```
```
boog900: I think I would rather this focus on consensus rather than RPC, Ada's code just uses a random string for txs so it's never going to actually hit consensus.

We do have a list here: https://user.cuprate.org/rpc.html as for timeline it shouldn't be too long for most to be supported, It's what I am working on now.

```
```
boog900: Funding is currently quite slow: https://ccs.getmonero.org/funding-required/.
Especially for anything not to do with FCMP++. You can see Ada's second proposal here: https://donate.magicgrants.org/monero/projects/fuzzing-monero-2

What would be your guys rate for 1 months worth of work?

```
```
boog900: As I think that if it's around Ada's, it would be too much for Cuprate through the CCS at this current time  
```
```
palinatolmach: Got it, thank you! We could do structure-aware fuzzing with RPC calls which would hit the consensus code, but as you've mentioned Ada's fuzzer does just make random data, so we'd need to implement that. We'll check how far we can get with `monero-oxide` in a month, as you've suggested before, and will get back. 
```
```
palinatolmach: As for the rate, we can do a reduced rate of $22k for the trial month with one engineer working on it for 4 weeks. The standard rate for follow-on engagements is $35k per engineer month, but we can be flexible with scoping and pricing depending on a specific engagement. Any feedback on how this fits into CCS would be very appreciated.  
```
```
gtrepta_rv: I'm going to sign off here. Thanks for the feedback! Hopefully we can come back with something that's more lined up with what you want. The monero-oxide library looks like a very good resource for fuzzing the structures we would need, whether that's through internal function calls or through RPC calls.
```
```
boog900: yeah, monero-oxide will give you valid tx creation, but you would need to track all chain data. Also if you want to do invalid txs you would need to fork it.

I think that is similar to Ada's (their proposal is around 2 months). Being completely honest I think this task is too big to do in a short enough time to be
appetising for the community and core who approve CCS proposals.

I don't see them wanting to fund fuzzing work for us, when we are still in alpha and have no users. 

Ideally I would want some code to generate txs/blocks with those txs/blocks being sent both to monerod and cuprate's consensus to check for difference. Ideally it should make
invalid txs too. I think that would be a lot for a months worth of work though.
```
```
boog900: I'll end the meeting here, but we can keep discussing 
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-04-28T18:59:23+00:00
- Closed at: 2026-05-05T19:13:22+00:00
