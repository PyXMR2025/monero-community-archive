---
title: question about the block-header size and format…
source_url: https://github.com/monero-project/monero/issues/3302
author: aotto1968
assignees: []
labels:
- invalid
created_at: '2018-02-21T17:49:19+00:00'
updated_at: '2018-02-21T20:50:53+00:00'
type: issue
status: closed
closed_at: '2018-02-21T20:48:48+00:00'
---

# Original Description
Hi, I have a problem to understand the **block-header**… 

from https://github.com/monero-project/monero/blob/f7b9f44c1b0d53170fd7f53d37fc67648f3247a2/src/cryptonote_basic/cryptonote_basic.h#L349

```
struct block_header
  {
    uint8_t major_version;
    uint8_t minor_version;  // now used as a voting mechanism, rather than how this particular block is built
    uint64_t timestamp;
    crypto::hash  prev_id;
    uint32_t nonce;

    BEGIN_SERIALIZE()
      VARINT_FIELD(major_version)
      VARINT_FIELD(minor_version)
      VARINT_FIELD(timestamp)
      FIELD(prev_id)
      FIELD(nonce)
    END_SERIALIZE()
  };
```
I'nervous about the block header… because in xmr-stak I see the offset for the _nonce_ at…__39__
```
    for ( int i = 0; i < sizeof (uint32_t ); ++i )
        ( ( (char *) input ) + 39 )[i] = ( (char*) ( &nonce ) )[i]; //take care of pointer alignment
```
my question was… _where the __39__ came from…???_

1. `crypto::hash  prev_id` == 32

```
namespace crypto {
…
#pragma pack(push, 1)
  POD_CLASS hash {
    char data[HASH_SIZE];
  };
  POD_CLASS hash8 {
    char data[8];
  };
#pragma pack(pop)
```
with `HASH_SIZE` = 32
```
enum {
  HASH_SIZE = 32,
  HASH_DATA_AREA = 136
};
```
now let's calculate…
1. 1+1+8+32=42 … bad
2. 1+1+4+32=38 … better

Question: 

1. is `timestamp` a 64 bit ore a 32 bit integer ?
2. 38 is close to 39… I still missing ONE byte ?

an INPUT example (from the pool server) was…
```
{"id":1,"jsonrpc":"2.0","error":null,"result":{"id":"657852c7-f380-4443-a7f7-370dc95fa5b8","job":{"blob":"0606f4f5b5d4052445a23e03f10eb90d078d137a97ed6b00b552f6c9372455cee1b576bdc2d5af00000000a671fa55dda8b18d35fa8ed530a3aa315733acd3102f0bc35edf2b68b1fcf3a70b","job_id":"ZirQM2sk2asWsqYjf141UpO537kI","target":"711b0d00","id":"657852c7-f380-4443-a7f7-370dc95fa5b8"},"status":"OK"}}
```
the `blob` seems to be the binary package with…

`0606` seems to be mayor:minor… and the next 4 or 8 bytes should be the timestamp… right ?


# Discussion History
## moneromooo-monero | 2018-02-21T20:43:40+00:00
Versions and timestamps are varints. See src/common/varint.h. 39 is just where the nonce ends up being with current timestamps, and is a bit of a hack which works for a fair amount of time still.

However, this is a bug tracker, not a help desk so I'll close this. See monero.stackexchange.com for more info.

+invalid


## aotto1968 | 2018-02-21T20:47:36+00:00
what a hell… (varint)…
```
 * The representation of varints is rather odd. The first bit of each
 * octet is significant, it represents wheter there is another part
 * waiting to be read. For example 0x8002 would return 0x200, even
 * though 0x02 does not have its msb set. The actual way they are read
 * is as follows: Strip the msb of each byte, then from left to right,
 * read in what remains, placing it in reverse, into the buffer. Thus,
 * the following bit stream: 0xff02 would return 0x027f. 0xff turns
 * into 0x7f, is placed on the beggining of the buffer, then 0x02 is
 * unchanged, since its msb is not set, and placed at the end of the
 * buffer.
```


# Action History
- Created by: aotto1968 | 2018-02-21T17:49:19+00:00
- Closed at: 2018-02-21T20:48:48+00:00
