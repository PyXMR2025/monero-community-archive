---
title: Double bottomed private keys to prevent quantum attacks without losing efficiency
source_url: https://github.com/monero-project/monero/issues/8418
author: ghost
assignees: []
labels: []
created_at: '2022-07-05T12:31:35+00:00'
updated_at: '2023-10-28T11:48:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Quantum Computers are not coming anytime soon, but when they do come, we're completely fucked. It's not worth switching to quantum resistant cryptography yet, because it's not efficient yet. Here's my idea how to not be completely fucked when the quantum computers arrive.
1. Use wallet seed to generate a quantum resistant keypair
2. Use the quantum resistant public key like wallet seed would normally be used

This way, when quantum computers arrive and everyone's private keys are revealed, the blockchain can be paused and the supply redistributed to the quantum resistant public keys derived from the revealed private keys on a new quantum resistant blockchain.
This solution would require everyone making a new wallet, but this could be implemented along with Seraphis which would require new wallets anyway.

# Discussion History
## UkoeHB | 2022-07-06T03:14:05+00:00
Would this approach lock you into a particular quantum resistance scheme?

## tevador | 2022-07-06T16:04:54+00:00
Interesting idea, but the problem is that a quantum attacker would not care about your private keys. They would simply calculate the discrete logarithm of the point `H` used in the amount commitments, which would allow them to undetectably create arbitrary amounts of Monero out of thin air.

To prevent this attack, we would need something like a [switch commitment](https://eprint.iacr.org/2017/237.pdf) for the amounts.

## d4f5409d | 2023-09-20T13:21:15+00:00
There is a [YouTube video](https://www.youtube.com/watch?v=rGae-vCD_Vo) that explains the possibilities about quantum computers and Monero.

## JosiahBSharkey | 2023-10-28T11:48:54+00:00
I have already been attacked with a quantum computer probably by the NSA because my opsec is so good they can't spy on me without hacking me so they think I am a spy or a criminal I had malware installed on my computer over ssh that was running behind tor authorized client it took them a month to break multiple ed25519 keys consistently this happened multiple times it is completely insane to think post quantum crypto doesn't need to be implemented now or that using a post quantum key as a seed for broken crypto is a good solution especially for a privacy coin post quantum crypto should have been implemented years ago when the attacks weren't already possible or even better before the first release because then all transactions would be private instead of being as transparent as Bitcoin to any nation state with enough money quantum computers that can break this aren't a future technology they exist now

# Action History
- Created by: ghost | 2022-07-05T12:31:35+00:00
