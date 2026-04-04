---
title: Many core_tests not currently passing
source_url: https://github.com/monero-project/monero/issues/8386
author: paulshapiro
assignees: []
labels: []
created_at: '2022-06-14T23:41:14+00:00'
updated_at: '2022-06-16T08:46:45+00:00'
type: issue
status: closed
closed_at: '2022-06-16T01:06:42+00:00'
---

# Original Description
Mainline master as of and probably earlier than 9750e1fa103539b3e533455500610aae76e253a5 has core_tests with multiple failures and error logs.

In `.../debug/tests/core_tests`...

`$ env CTEST_OUTPUT_ON_FAILURE=1 ctest --verbose`

yields, e.g...

`E get_pruned_transaction_weight does not support v1 txes`

```E [gen_chain_switch_1::check_split_not_switched] failed: "((8ULL) * ((uint64_t)1000000000000)) == get_balance(m_recipient_account_1, chain, mtx)", 8000000000000 != 1000000000000
1: E #TEST# Failed gen_chain_switch_1
```

```E gen_ring_signature_2 generation failed: what=couldn't fill transaction sources
1: E #TEST# Failed gen_ring_signature_2
```

```1: E Block with id: <483b7971e4fadeb0e92d7e9fc57d6a8025c0e360504220239d0088a819793b9d> has incorrect miner transaction```

```1: E wrong variant type: N10cryptonote19txout_to_tagged_keyE, expected txout_to_key in transaction id=<285877225d445652ddf686470fb3b5cff2b1867fb805bfb526a0b5903a8bc3a4>
1: E miner transaction has invalid output type(s) in block <b5bcf21533b9346fc15ed7baeafc4861012e2139e162cd1fd433f7d5ec1624ef>
1: E Block with id: <b5bcf21533b9346fc15ed7baeafc4861012e2139e162cd1fd433f7d5ec1624ef> failed to pass prevalidation
```

```1: E Failed to find tx_meta in txpool
1: E Block with id: <16da127c3105ce8757a6adae05abb3ef873805f5621730db229602c3ccfc85f0> has at least one unknown transaction with id: <0000000000000000000000000000000000000000000000000000000000000000>
```

Etc.

Lots of the core tests cases implement critical tx construction unit testing among other things so this was a blocker for me. I figure this issue'd be in current discourse but I'm also a little out of the loop. Is it just my env, or...?

# Discussion History
## selsta | 2022-06-14T23:43:03+00:00
We run all tests on every commit, if a large part of core tests fail than it might be something with your dev environment?

## paulshapiro | 2022-06-14T23:43:33+00:00
And tests are not currently failing?

## selsta | 2022-06-14T23:44:38+00:00
Everything green currently, no failed tests. Some functional tests fail rarely but core tests should never fail.

## paulshapiro | 2022-06-14T23:45:00+00:00
Hrm thanks. Looks like my mistake

## selsta | 2022-06-14T23:45:30+00:00
Can you try to run them on a different machine maybe?

## paulshapiro | 2022-06-14T23:46:47+00:00
I could start a VPS and try. I'll clean build here first.

## paulshapiro | 2022-06-14T23:53:53+00:00
Waiting on recompile. If this doesn't work I'll also try `ccache --clear` as I recently installed it.

## paulshapiro | 2022-06-15T21:39:18+00:00
Okay, initially I noted I had a stale build, but having deleted `build/*` and `ccache --clear`, I'm still seeing a number of errors in a verbose core_tests:

1: 	E get_pruned_transaction_weight does not support v1 txes

1:    E Timestamp of block with id: <fca99ebdfd433a06cde2789c5216adc83c5636ac73e8f06352eb3e5f275a8617>, 1338226140, less than median of last 60 blocks, 1338226170
1: 	E Block with id: <fca99ebdfd433a06cde2789c5216adc83c5636ac73e8f06352eb3e5f275a8617>
1: 	E has invalid timestamp: 1338226140


1:	E coinbase transaction transaction has the wrong unlock time=1338235200, expected 61
1: 	E Block with id: <da8f45690b6bad1163fcdc6ce736efeb36007f67ea29b2c9825780b634fb6b44> failed to pass prevalidation


1: 	E Block recognized as orphaned and rejected, id = <0a9894ef7eabe8ab72df9cef99272b23afe7668f03187ae46703887779654116>, height 1, parent in alt 0, parent in main 0 (parent <5604f1424e81093c9892f2745edbbb73d2bcdba24d620f202d5d62c1a5fec32a>, current top <5704f1424e81093c9892f2745edbbb73d2bcdba24d620f202d5d62c1a5fec32a>, chain height 1)


1: 	E Block with id: <bfcea5b76f4d259da9585b469b112feab8b3a4c0c2f5dd01cb61a7edbe0cbb70>
1: 	E does not have enough proof of work: <9ec3a2f617c746af7a47f4180ff6e532f65adfb8b777b781581680cd28a70d32> at height 3, unexpected difficulty: 60


1: 	E Failed to parse block from blob

1: 	E Block with id: <79cb8766a37a94bc4955f65faad67bd4d154c766f52406741f93b6cbfceb6749> has incorrect miner transaction

1: 	E coinbase transaction spend too much money (35.184338534400). Block reward is 17.592169267200(17.592169267200+0.000000000000), cumulative_block_weight 80
1: 	E Block with id: <96a0791c6ebf2681de8b4e95de1c9e1a2a3368b920959eb15154f74ea9987686> has incorrect miner transaction


1: 	E wrong variant type: N10cryptonote12txout_to_keyE, expected txout_to_tagged_key in transaction id=<4f66e16b28d6d81a1bed5d66f50b6524ea993fc5eed5a7d50236e284d7548f99>
1: 	E miner transaction has invalid output type(s) in block <809638f927d80c90f9ca018f2687e84d45cae0190fe16ec5974680e60c7c67ea>
1: 	E Block with id: <809638f927d80c90f9ca018f2687e84d45cae0190fe16ec5974680e60c7c67ea> failed to pass prevalidation


1: 	E Failed to find tx_meta in txpool
1: 	E Block with id: <7ab8a3a3df3bfb6237a950cfb7fe4fd8f954b9b20388f212bed9c976bccf889f> has at least one unknown transaction with id: <0000000000000000000000000000000000000000000000000000000000000000>


Halp!

## moneromooo-monero | 2022-06-15T21:46:00+00:00
Did you modify any of the code ?

## paulshapiro | 2022-06-15T21:51:02+00:00
Initially, yes, but I've gone back to master HEAD and did the above clean build.

## moneromooo-monero | 2022-06-15T21:52:40+00:00
Can you run this:
```
./build/wherever/tests/core_tests/core_tests --generate-and-play-test-data --filter gen_chain_switch_1
```

This is one of the tests you list as failing.

## paulshapiro | 2022-06-15T21:55:59+00:00
Fwiw, option is "`generate_and_play_test_data`" (underscores). 

Test is reported as succeeding ("`#TEST# Succeeded gen_chain_switch_1`"), but that does log multiple of the aforementioned `E get_pruned_transaction_weight does not support v1 txes`.


## selsta | 2022-06-15T21:57:19+00:00
Might be working as intended if the test is testing for something to fail?

## paulshapiro | 2022-06-15T21:57:38+00:00
I'd have to check the other more obviously "erroring" tests to see if they also report success

@selsta could be

## selsta | 2022-06-15T21:58:25+00:00
If the test itself is reporting as succeeding then everything is good.

## paulshapiro | 2022-06-15T21:58:43+00:00
Thats why I would like to check the other tests. Few mins..

## paulshapiro | 2022-06-15T21:59:01+00:00
(Basically I need to know how to tell if I break things with code changes later)

## paulshapiro | 2022-06-15T22:01:56+00:00
So, question:

```		E coinbase transaction transaction has the wrong unlock time=1338223800, expected 61
E coinbase transaction transaction has the wrong unlock time=1338223800, expected 61
	E Block with id: <1eb7eba1cb4a9576c392610f711c523385469582920861824c86ce1ef9a98295> failed to pass prevalidation
	D Pruning not enabled, nothing to do
	I === EVENT # 2: callback_entry check_block_purged
	I #TEST# Succeeded gen_block_unlock_time_is_timestamp_in_past
```

Is this the correct ~ending output for  `...../core_tests --generate_and_play_test_data --filter gen_block_unlock_time_is_timestamp_in_past`?

This is a test that has a name that doesn't at least obviously indicate it's looking for a failure.

## moneromooo-monero | 2022-06-15T22:16:00+00:00
Yes. It'd say something like "Failed" otherwise.
About the specific "get_pruned_transaction_weight does not support v1 txes", it might be failing on another reason than the expected one, or maybe it's something that does not impact the test. I do not know off the top of my head, you'll have to look at it in detail.

## paulshapiro | 2022-06-15T22:20:33+00:00
I wonder if the lines output around the same time as the view tags tests are intended, for example, to include errors

```1: D Invalidating block template cache
1: I === EVENT # 1: cryptonote::block
1: D [get_estimated_batch_size] m_height: 1  block_start: 0  block_stop: 0
1: D estimated average block size for batch: 4096
1: D calculated batch size: 92160000
1: D increase size: 536870912
1: D DB map size:     1073741824
1: D Space used:      77824
1: D Space remaining: 1073664000
1: D Size threshold:  92160000
1: D Percent used: 0.0072  Percent threshold: 90.0000
1: D block_batches: 0
1: D Miner tx hash: <285877225d445652ddf686470fb3b5cff2b1867fb805bfb526a0b5903a8bc3a4>
1: E wrong variant type: N10cryptonote19txout_to_tagged_keyE, expected txout_to_key in transaction id=<285877225d445652ddf686470fb3b5cff2b1867fb805bfb526a0b5903a8bc3a4>
1: E miner transaction has invalid output type(s) in block <b5bcf21533b9346fc15ed7baeafc4861012e2139e162cd1fd433f7d5ec1624ef>
1: E Block with id: <b5bcf21533b9346fc15ed7baeafc4861012e2139e162cd1fd433f7d5ec1624ef> failed to pass prevalidation
1: D Pruning not enabled, nothing to do
1: I === EVENT # 2: callback_entry check_block_purged
1: 	I #TEST# Succeeded gen_block_miner_tx_out_has_view_tag_before_hf_view_tags
1: 	I Loading blockchain from folder /Users/paul/.bitmonero/fake/lmdb ...
```

## moneromooo-monero | 2022-06-15T22:23:13+00:00
Sounds probable. You don't want to allow view tags before the fork AFAICT.

## paulshapiro | 2022-06-15T22:24:16+00:00
Just running the tests though

## paulshapiro | 2022-06-15T23:29:16+00:00
Just realized that second one was not a good example

This one doesn't seem like it would expect a failure:

```: 	I === EVENT # 62: cryptonote::block
1: 	D [get_estimated_batch_size] m_height: 62  block_start: 0  block_stop: 61
1: 	D estimated average block size for batch: 4096
1: 	D calculated batch size: 92160000
1: 	D increase size: 536870912
1: 	D DB map size:     1073741824
1: 	D Space used:      401408
1: 	D Space remaining: 1073340416
1: 	D Size threshold:  92160000
1: 	D Percent used: 0.0374  Percent threshold: 90.0000
1: 	D block_batches: 0
1: 	E Failed to parse block from blob
1: 	D Pruning not enabled, nothing to do
1: 	I === EVENT # 63: callback_entry check_block_purged
1: 	I #TEST# Succeeded gen_block_miner_tx_with_txin_to_key
```

I think if the error logs were intended, others would see them too, no?

Edit: I need to isolate which one was actually failing still

## paulshapiro | 2022-06-16T00:31:07+00:00
Still waiting on all unfiltered core tests in order to figure out which one actually failed but seeing lots of errors

This one for example seems a bit.. uncertain

```	I === EVENT # 62: cryptonote::transaction
	E Unexpected output target type found: N10cryptonote15txout_to_scriptE
	E Failed to get output public key (output type: N10cryptonote15txout_to_scriptE), in transaction id=<bc760ea0012a99746d8e2583631584919818d2d10743b2e85ee3a729bd67a898>
	E tx with invalid outputs, rejected for tx id= <bc760ea0012a99746d8e2583631584919818d2d10743b2e85ee3a729bd67a898>
	I WRONG TRANSACTION BLOB, Failed to check tx <bc760ea0012a99746d8e2583631584919818d2d10743b2e85ee3a729bd67a898> semantic, rejected
	I === EVENT # 63: callback_entry mark_invalid_tx
	I === EVENT # 64: cryptonote::transaction
	E Unexpected output target type found: N10cryptonote19txout_to_scripthashE
	E Failed to get output public key (output type: N10cryptonote19txout_to_scripthashE), in transaction id=<1a332c4cc175a7443752068a7956f780ce56799822741dfdee1843d02be7dc17>
	E tx with invalid outputs, rejected for tx id= <1a332c4cc175a7443752068a7956f780ce56799822741dfdee1843d02be7dc17>
	I WRONG TRANSACTION BLOB, Failed to check tx <1a332c4cc175a7443752068a7956f780ce56799822741dfdee1843d02be7dc17> semantic, rejected
	I #TEST# Succeeded gen_tx_output_is_not_txout_to_key
```

## paulshapiro | 2022-06-16T01:06:42+00:00
OK well as hoped, core tests actually all 'succeeded' on that clean build.


## moneromooo-monero | 2022-06-16T08:46:45+00:00
Core tests have that annoying property that when it expects something high level to fail, it does not know what exact error happened at a low level. So if it tries to, as above, shove a tx which a "txout_to_scripthash" output, which is invalid, and it fails, it's happy, but will not notice if the failure was due to, say, out of memory somewhere. It is hard to fix without bubbling back up all error reasons (or parsing its own logs).

# Action History
- Created by: paulshapiro | 2022-06-14T23:41:14+00:00
- Closed at: 2022-06-16T01:06:42+00:00
