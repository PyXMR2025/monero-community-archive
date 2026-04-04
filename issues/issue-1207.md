---
title: 'Cuprate Meeting #57 - Tuesday, 2025-05-27, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1207
author: moo900
assignees: []
labels: []
created_at: '2025-05-20T19:06:27+00:00'
updated_at: '2025-05-27T18:55:59+00:00'
type: issue
status: closed
closed_at: '2025-05-27T18:55:59+00:00'
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

Previous meeting: #1203

# Discussion History
## moo900 | 2025-05-27T18:55:58+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
syntheticbird: hi
```
```
syntheticbird: also moooooooooooooooo
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
syntheticbird: Me: Addressing latest review on my Onion addressing and Tor zone definition PR. Actually reading proptest manual. Also implemented onion checksum verification
```
```
boog900: me: worked on fixing some issues with the tx-pool manger, also just started working on the fuzz PR again 
```
```
hinto: me: still trying to fix windows builds
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
syntheticbird: I crave for RPC
```
```
boog900: does reverting to windows-gnu fix builds? 
```
```
hinto: update on fuzzing, none have crashed yet, `oxide_tx`:

#54224487123: cov: 1167 ft: 3931 corp: 602 exec/s: 16798 oom/timeout/crash: 0/0/0 time: 1112692s job: 11222 dft_time: 0

```
```
hinto: I am unsure although I would assume so
```
```
boog900: you can also look through cuprate - I have used proptest a few times in different places 
```
```
hinto: I think there are 2 options: take time to revert to `windows-gnu` or skip windows builds until the linker issue is fixed upstream (both in `randomx-rs` and rust)
```
```
boog900: https://github.com/tari-project/randomx-rs/commits/development/
```
```
boog900: looks already dond 
```
```
boog900: * looks already done
```
```
boog900: have you tried that yet?
```
```
hinto: ... no
```
```
syntheticbird: Yep but with onion checksumming comes some difficulties with generating valid addresses with random pubkey, at least in a proptest manner. but I'm trying to figure this out
```
```
boog900: it doesn't have to test the valid case - we already have tests for that, its just to test with random input 
```
```
boog900: I think it would have caught the panic I found 
```
```
boog900: obviously you could tests valid cases as well but yeah that would be harder 
```
```
syntheticbird: there is a 0.001528% chance of checksum collision
```
```
boog900: I'll merge it into our fork 
```
```
syntheticbird: I'll just do the invalid in a first time. Thx for notating this
```
```
boog900: it doesn't look like we check checksums?
```
```
syntheticbird: ^
```
```
syntheticbird: i just added it
```
```
boog900: ah I still think it is unnecessary 
```
```
boog900: does it add a dep?
```
```
hinto: ok, the main `Cargo.toml` must be updated as well
```
```
syntheticbird: right now it adds `base32`, but it would have been added to the workspace with `arti` anyway
```
```
hinto: I'll test the build and give an update after meeting
```
```
boog900: still a new dep, which wasn't needed for that crate :(
```
```
boog900: I still don't think this is needed at all and is just a waste of CPU cycles 
```
```
syntheticbird: i'm gonna add a PR soon on serpahis-migration/monero for it.
```
```
syntheticbird: It's nothing
```
```
boog900: its an added dep now 
```
```
hinto: fyi the release is in 8 days, so that's a hard deadilne for 423/451 merge if `v0.0.4` is to contain RPC
```
```
syntheticbird: I was talking of CPU cycles, but i think that's ok we can survive that.
```
```
boog900: I strongly think this is really pointless, its extra code, extra work (although minimal) and now an extra dep
```
```
boog900: to provide NO extra protection 
```
```
boog900: https://github.com/Cuprate/cuprate/pull/481#discussion_r2105379406
```
```
boog900: for context 
```
```
syntheticbird: I just think we should do thing the correct way, and it's not protection now but might become on in the future if we decide to ban peers relaying incorrect address.
```
```
syntheticbird: with checksum verification we're only accepting valid ones
```
```
boog900: valid semantically sure. Someone can still throw unreachable addresses around the network 
```
```
boog900: also is it valid? we would need to check these are valid Ed25519 points for full validity right?
```
```
boog900: For our use case this is no more correct 
```
```
syntheticbird: Sure. But your comment was about the ability to create invalid addresses regardless of the character check. I think this is crazy to accept arbitrary utf-8 within our addressbook and relay to peer
```
```
syntheticbird: * Sure. But your comment was about the ability to create invalid addresses regardless of the character check. I think this is crazy to accept arbitrary utf-8 within our addressbook and relay that to peers
```
```
boog900: we wouldn't relay it to peers, it would go in the grey list unless reachable 
```
```
syntheticbird: that's true.
```
```
syntheticbird: also true.
```
```
syntheticbird: I would like to at least keep the character check because storing arbitrary utf-8 and then pass it to the resolver is ridiculous imo
```
```
syntheticbird: I can also see the very funny `gray_peerlist` command suddenly passing escape character 
```
```
boog900: `OnionAddr`'s `domain` field is `pub`. It makes no guarantees on its content.
```
```
syntheticbird: `// 56 characters encoded onion v2 domain without the .onion suffix`
```
```
syntheticbird: should be `///`
```
```
boog900: words mean nothing, the code does not guarantees it 
```
```
boog900: * words mean nothing, the code does not guarantee it 
```
```
syntheticbird: I can remove the `pub` then
```
```
boog900: that would solve that
```
```
syntheticbird: alright, so i remove `pub` and checksum (since we don't verify ed25519 pubkey point) and we keep the character check to avoid arbitrary utf-8
```
```
syntheticbird: is that good?
```
```
boog900: yeah I am ok with that 
```
```
boog900: hinto: do you have an opinion on this: https://github.com/Cuprate/cuprate/pull/481#discussion_r2091643518
```
```
syntheticbird: Fwiw I removed it in my local branch. I still prefer it as an enum tho
```
```
syntheticbird: forgot to thumbs up
```
```
syntheticbird: I replaced it with some documentation at the top
```
```
boog900: ah ok 👍️
```
```
hinto: I think this type already exists: https://github.com/Cuprate/cuprate/blob/main/types/types/src/address_type.rs#L65
```
```
syntheticbird: OH
```
```
boog900: shit 
```
```
hinto: it's exposed in RPC
```
```
syntheticbird: LMAO thx
```
```
hinto: from inner p2p stuff
```
```
boog900: yeah we already pull types in too 
```
```
boog900: so yeah just use that
```
```
syntheticbird: sgtm
```
```
boog900: anything else to discuss today?
```
```
syntheticbird: yes
```
```
syntheticbird: regarding review of RPC PRs
```
```
syntheticbird: can I help ? I'm not sure this would be accelerating things tho
```
```
hinto: help in a specific way? review on any PR would always be good
```
```
syntheticbird: yeah i mean reviewing open PR. Ultimately boog have to give the final approval but i believe you are busy
```
```
boog900: I'll review it after I rebase our randomX fork in a bit 
```
```
hinto: 423/451 need approval
```
```
hinto: from this CCS update: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/543, the plan for RPC as a whole is:

1. RPC server (423, done)
2. Connect RPC handlers to RPC server (450)
3. Enable endpoints known to work (future PR)
4. Finish compatability testing harness (422)
5. Enable individual endpoints as they are tested (future PRs)
```
```
hinto: 3) will be soon, probably before `v0.0.4`, that will be approval as well although it is mostly just adding `.endpoint()` to the existing RPC server
```
```
hinto: 4) will be bigger and would benefit more from actual usage testing
```
```
hinto: 5) will probably be 1 PR per endpoint
```
```
hinto: all of those will need review/approval
```
```
syntheticbird: Re: 5, 1 PR per endpoint sounds... tiresome. Maybe small groups instead?
```
```
boog900: will 3 be enough for wallets? 
```
```
hinto: yup sure
```
```
syntheticbird: Re: 4 by actual usage testing you mean production testing?
```
```
hinto: in the biggest batch possible
```
```
syntheticbird: * Re: 4 by actual usage testing you mean production workload?
```
```
hinto: no, I want both of you to use `cuprate-rpc-compat` and become familiar with it such that I'm not the only one available for RPC fixes
```
```
syntheticbird: roger that
```
```
boog900: hinto?
```
```
boog900: or do you not know
```
```
hinto: definitely not
```
```
boog900: ah ok
```
```
syntheticbird: My disappointment is immeasurable, and my day is ruined.
```
```
syntheticbird: /jk
```
```
hinto: we could enable every endpoint from the start, although that would probably lead to even more disappointment 
```
```
boog900: yeah better not
```
```
boog900: anything else for today?
```
```
syntheticbird: nothing from me
```
```
boog900: ok we can end here, thanks everyone!
```
```
syntheticbird: thanks
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-05-20T19:06:27+00:00
- Closed at: 2025-05-27T18:55:59+00:00
