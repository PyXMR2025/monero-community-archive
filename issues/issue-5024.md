---
title: Write a test about cn_serialize and cn_deserialize for bulletproof failed.
source_url: https://github.com/monero-project/monero/issues/5024
author: woshidadashi
assignees: []
labels:
- invalid
created_at: '2018-12-28T12:17:27+00:00'
updated_at: '2019-01-01T15:01:01+00:00'
type: issue
status: closed
closed_at: '2019-01-01T15:01:01+00:00'
---

# Original Description
I write a test case for cn_serialize and cn_deserialize for bulletproof, but this case failed, is there any problem about the code?
`TEST (bulletproofs, valid_random) {
   
        rct::Bulletproof proof = bulletproof_PROVE(crypto::rand<uint64_t>(), rct::skGen());
        std::string strString = serilizationProofs::cn_serialize(proof);
        rct::Bulletproof proofAfterDeser;
        serilizationProofs::cn_deserialize(strString, proofAfterDeser);
        GTEST_ASSERT_EQ(rct::bulletproof_VERIFY(proofAfterDeser), true);
    
}`

# Discussion History
## moneromooo-monero | 2018-12-28T12:19:47+00:00
Wrong repo ? serilizationProofs::cn_serialize is not monero code.

## woshidadashi | 2018-12-28T12:31:26+00:00
Yes, it is. It is on the path monero/src/device_trezor/trezor/protocol.hpp

## woshidadashi | 2018-12-28T12:32:23+00:00
serilizationProofs:: is just copy it to test file and rename the namespace

## moneromooo-monero | 2018-12-28T13:20:52+00:00
I see a protocol::cn_deserialize there. If that's what you're using, then bulletproofs are not self contained, they drop some data which can be recovered from the rest of the transaction (for blockchain space reasons). See expand_transaction_1.

## woshidadashi | 2018-12-29T02:13:10+00:00
OK, thanks. I know what you mean.

## moneromooo-monero | 2019-01-01T14:56:51+00:00
Not a bug (though admittedly confusing).

+invalid


# Action History
- Created by: woshidadashi | 2018-12-28T12:17:27+00:00
- Closed at: 2019-01-01T15:01:01+00:00
