---
title: Varint description
source_url: https://github.com/monero-project/monero/issues/2340
author: KlausT
assignees: []
labels: []
created_at: '2017-08-24T16:06:28+00:00'
updated_at: '2020-02-11T11:45:17+00:00'
type: issue
status: closed
closed_at: '2018-01-08T13:48:31+00:00'
---

# Original Description
Could you please check if the description of varint is correct?
https://github.com/monero-project/monero/blob/master/src/common/varint.h#L38
It doesn't make sense to me. 
What happens when you want to encode 0x01ff01 to varint?


# Discussion History
## glv2 | 2017-08-24T16:48:20+00:00
This varint encoding is the same as the one used in protocol buffers (https://developers.google.com/protocol-buffers/docs/encoding#varints). The integers are stored in little-endian order, but by blocks of 7 bits (instead of 8). In each byte, bits 0 to 6 are bits from the integer, and bit 8 indicates if there are more bits to come (in the next byte) or not.

In the case of 0xff = 11111111
Split in blocks of 7 bits: 0000001 1111111
Bit 7 of the first byte is 1 to indicate that there is a second block, and bit 7 of the second block is 0 because there is no third block.
Block 0: 11111111
Block 1: 00000001

So the encoding of 0xff is "ff01".

Note: the varint encoding used by the portable binary archive serialization is different from this one


## KlausT | 2017-08-24T16:59:57+00:00
Ok, I see. So the description in varint.h is misleading.

## dEBRUYNE-1 | 2018-01-08T13:14:14+00:00
+resolved

## ghost | 2020-02-07T14:19:14+00:00
@glv2 can you explain the varint encoding used by the portable binary archive serialization please?

## glv2 | 2020-02-07T16:09:14+00:00
The portable binary archive serialization stores integers in little-endian order in a series of 1, 2, 4 or 8 bytes.
Here's some pseudo-C code explaining how the serialization works:

``` c
/* Constants used */
BYTE = 0
WORD = 1
DOUBLE_WORD = 2
QUAD_WORD = 3

/* Serialization rules */
if (n <= 64)
  return (uint8le) ((n << 2) | BYTE)
else if (n <= 16383)
  return (uint16le) ((n << 2) | WORD)
else if (n <= 1073741823)
  return (uint32le) ((n << 2) | DOUBLE_WORD)
else if (n <= 4611686018427387903)
  return (uint64le) ((n << 2) | QUAD_WORD)
else
  error "Too big to be serialized"
```


## ghost | 2020-02-07T17:04:16+00:00
@glv2 thanks for posting this. We are looking at how the serialisation of a tx prefix is done. If we examine the start of one of these prefixes:

**Json:**
", \"version\": 1, \"unlock_time\": 0, \"vin\": [ {\"key\": {\"amount\": 60, \"key_offsets\": [ 1825329], \"k_image\": \"e720408baa96934bca1f98b97aca884063075b5f7b52bdb84cac3b4ea5c5e875\"}}

**Hex of the serialised result (ie serialised prefix not json):**
010006023c01b1b46fe720408baa96934bca1f98b97aca884063075b5f7b52bdb84cac3b4ea5c5e875

**Broken up hex:**
01 version
00 unlock time
0602  something
3c amount
01b1b46f   offsets?
e720408baa96934bca1f98b97aca884063075b5f7b52bdb84cac3b4ea5c5e875   key image

So I have a few questions:

1. Why are version & unlock time & amount written verbatim in hex if they are varints? I see this behavior even for amount =100 (bigger than 64) for example
If i did what you said, for the version, I'd get:
((00000001 << 2) | BYTE ) = (00000100 | 00000000) = 00000100 = 04 (hex)

2. Do you happen to know what the four hex characters after unlock time are doing?

If I examine a different prefix with a higher amount I see this:
", \"version\": 1, \"unlock_time\": 0, \"vin\": [ {\"key\": {\"amount\": 10000, \"key_offsets\": [ 5163403], \"k_image\": \"13f5ab3b188583018ca283e89dc17fa47adc5db2d29febc2f45807a7b61429db\"}

01 version
00 unlock
0102904e018b93bb02  amount and offsets
13f5ab3b188583018ca283e89dc17fa47adc5db2d29febc2f45807a7b61429db key image

Amount=10000 as hex is 2710 which isn't present as hex. If i do n << 2 | 1, I then get 9c41 in hex, which isn't present in the string either.

Could you help shed some light on this? Many thanks for your help.

## glv2 | 2020-02-07T17:35:13+00:00
If I remember correctly, the serialization of transactions uses the protocol buffer varint encoding, not the portable binary archive one.

For the format of transactions, check https://monero.stackexchange.com/questions/3958/what-is-the-format-of-a-block-in-the-monero-blockchain or https://monero.stackexchange.com/questions/5664/size-requirements-for-different-pieces-of-a-monero-transaction.


## ghost | 2020-02-11T11:45:17+00:00
We figured this out and wrote a doc on it:
https://github.com/electroneum/electroneum/commit/9e08495a69493650d78a26967c37c70ce9a0fc69

# Action History
- Created by: KlausT | 2017-08-24T16:06:28+00:00
- Closed at: 2018-01-08T13:48:31+00:00
