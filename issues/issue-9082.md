---
title: Algorithm for getting Mnemonic Seed from 256-bitsHexadecimal Seed
source_url: https://github.com/monero-project/monero/issues/9082
author: developergames2d
assignees: []
labels:
- question
- low priority
created_at: '2023-11-29T18:40:38+00:00'
updated_at: '2023-12-16T03:03:32+00:00'
type: issue
status: closed
closed_at: '2023-12-15T19:27:07+00:00'
---

# Original Description
How to get Mnemonic Seed from 256 bits of Hexadecimal Seed?
For example, on https://xmr.llcoins.net/addresstests.html I can to fill the Hexadecimal Seed field, push "Gen 1."-button and get Mnemonic Seed.
I search the algorithm (text or C++-function without many libraries, maybe using only some function for getting hash to add check-bytes to the end (Keccak-256 as I understand)).
For example, for BTC (24 words from 256 bits) answer is "1. Get SHA256. 2. Put the first byte to the end. 3. Cut this 33 bytes into 24 11-bits words. 4. Get each word from bip39 wordlist.".

# Discussion History
## Joysan78 | 2023-11-30T11:16:05+00:00
Tnx I'll try that😊

## moneromooo-monero | 2023-12-12T14:02:23+00:00
bytes_to_words in src/mnemonics/electrum-words.cpp
From a comment in that function:
// 4 bytes -> 3 words.  8 digits base 16 -> 3 digits base 1626

## developergames2d | 2023-12-15T15:57:36+00:00
> bytes_to_words in src/mnemonics/electrum-words.cpp From a comment in that function: // 4 bytes -> 3 words. 8 digits base 16 -> 3 digits base 1626

I have 32 bytes. You give me the algorithm for 32 / 4 * 3 = 24 words. How can to get the 25-th word?

## selsta | 2023-12-15T16:13:14+00:00
The last word is a checksum.

https://monero.stackexchange.com/questions/874/what-is-the-checksum-at-the-end-of-a-mnemonic-seed

## developergames2d | 2023-12-15T16:19:22+00:00
> The last word is a checksum.
> 
> https://monero.stackexchange.com/questions/874/what-is-the-checksum-at-the-end-of-a-mnemonic-seed

Example (for 0-private key):
abbey x24:

The string which we feed to CRC32 will be:
abbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabb
and the result of CRC32 performed on it will be 0xb038cd80 = 2956512640. 2956512640 mod 24 is 16, not 0 (index of abbey is 0, this is right last word for 0-private key).

## moneromooo-monero | 2023-12-15T16:25:22+00:00
There is no CRC32 involved.
abb is 0. So abbabbabbabb is 0x00000000.

## developergames2d | 2023-12-15T16:30:58+00:00
> There is no CRC32 involved. abb is 0. So abbabbabbabb is 0x00000000.

For WHAT we calculate CRC32? The string "abbabbabb..."?

## developergames2d | 2023-12-15T16:50:48+00:00
> There is no CRC32 involved. abb is 0. So abbabbabbabb is 0x00000000.

In example for "skirting trash phase buckets apology gags sedan coffee vinegar else fifteen pitched idled gorilla siren cucumber urban junk vastness laboratory rift rhino situated taxi" we calculated CRC32 for string "skitraphabucapogagsedcofvinelsfifpitidlgorsircucurbjunvaslabrifrhisittax". This is 1790087523 mod 24 is 3. Ok. But for "abbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabb" I can't get 0, only 16 (2956512640 mod 24).

## selsta | 2023-12-15T18:01:58+00:00
It means the 16th word (starts with 0) of the seed is the checksum -> abbey. The checksum can only be abbey because all words from 0 to 23 are abbey.

## developergames2d | 2023-12-15T19:25:36+00:00
> It means the 16th word (starts with 0) of the seed is the checksum -> abbey. The checksum can only be abbey because all words from 0 to 23 are abbey.

Thank you!

## developergames2d | 2023-12-16T02:57:41+00:00
It turns out that the maximum number of combinations of seed phrases is 1626^24 more than hexes (2^256) by about 7%, i.e. it is better to randomly select 24 words and then get the 25th than to get 24 words out of 64-hexadecimal number...
The maximum of hexadecimal seed is FFFFFFFF_16 x 6 -> 4294967295_10 x 6 -> (1624,807,489)_1626 x 6 -> "zones listen foamy zones listen foamy zones listen foamy zones listen foamy zones listen foamy zones listen foamy zones listen foamy zones listen foamy". And 25th word is zones. Whereas the "maximum" phrase is "zoom"x25...

## developergames2d | 2023-12-16T03:02:59+00:00
> It turns out that the maximum number of combinations of seed phrases is 1626^24 more than hexes (2^256) by about 7%, i.e. it is better to randomly select 24 words and then get the 25th than to get 24 words out of 64-hexadecimal number... The maximum of hexadecimal seed is FFFFFFFF_16 x 6 -> 4294967295_10 x 6 -> (1624,807,489)_1626 x 6 -> "zones listen foamy zones listen foamy zones listen foamy zones listen foamy zones listen foamy zones listen foamy zones listen foamy zones listen foamy". And 25th word is zones. Whereas the "maximum" phrase is "zoom"x25...

It turns out that about 7% of the seeds have one Private spend key and addresses (as pairs, much less common are threes etc.).

# Action History
- Created by: developergames2d | 2023-11-29T18:40:38+00:00
- Closed at: 2023-12-15T19:27:07+00:00
