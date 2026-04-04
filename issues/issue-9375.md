---
title: Trezor Safe 3 passphrase entry fails on host with long/special passphrases
source_url: https://github.com/monero-project/monero/issues/9375
author: lobster-kerouac
assignees: []
labels:
- bug
created_at: '2024-06-20T22:56:57+00:00'
updated_at: '2024-11-26T12:03:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The Trezor Safe 3 device supports an additional passphrase when creating a wallet. With the official monero software (GUI or CLI) there is the option to input the passphrase either on the device itself or using the keyboard on the host computer. 

There appears to be a bug when entering the password on the host computer: any passphrase over 10 (I think, see below) characters, or containing certain special characters, causes the operation to fail with `Error: failed to load wallet: Cannot get a device address`. This feels like a bug in the wallet software not correctly parsing the input.

I have tested this with the GUI and CLI versions of the Mac software and the CLI version of the linux software. All give the same result. The same bug exists both when trying to generate a new wallet or when accessing an existing wallet. In all cases entering the passphrase on the device itself works.

Examples of passphrases that work: "foo", "Foo", "Foo Bar", "12345678", "Foo.Bar", "aaaaaaaaa" (9 a's)
Examples of passphrases that DON'T work: "FooBar$%", "123456789", "aaaaaaaaaa" (10 a's)

# Discussion History
## selsta | 2024-06-20T22:59:16+00:00
@ph4r05 any idea here?

## lobster-kerouac | 2024-11-07T20:06:09+00:00
Any clues here? I'm happy to take a crack at this, but I'd probably need some help getting pointed in the right direction.

## plowsof | 2024-11-21T18:51:14+00:00
With Trezor Model T 10 a's works fine (both fine when entered on the device and host). Need someone to reproduce with a trezor safe 3

## blob42 | 2024-11-26T12:03:48+00:00
@plowsof I can confirm same issue with safe 3. Long passphrase fails with same error. Anyway I can help debug the issue ? I'm not a cpp guru but can find my ways around.

# Action History
- Created by: lobster-kerouac | 2024-06-20T22:56:57+00:00
