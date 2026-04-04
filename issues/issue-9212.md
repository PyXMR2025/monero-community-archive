---
title: '`race_condition` failing randomly'
source_url: https://github.com/monero-project/monero/issues/9212
author: '0xFFFC0000'
assignees: []
labels:
- bug
- question
- important
- discussion
created_at: '2024-03-02T10:44:20+00:00'
updated_at: '2024-03-02T20:37:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have noticed recently that the `race_condition` test fails randomly. Here is a list of runs that have failed, some of these are even document-only PRs:


1. https://github.com/monero-project/monero/actions/runs/8032901697/job/21944925602
2. https://github.com/monero-project/monero/actions/runs/8070978087/job/22050319484
3. https://github.com/monero-project/monero/actions/runs/8121455963/job/22200074675
4. https://github.com/monero-project/monero/actions/runs/8031392481/job/21941541359
5. https://github.com/monero-project/monero/actions/runs/8031412684/job/21942084680
6. https://github.com/monero-project/monero/actions/runs/8070978087/job/22050319484
7. https://github.com/monero-project/monero/actions/runs/8032901697/job/21944925602
8. https://github.com/monero-project/monero/actions/runs/7993111361/job/21828933742


In the meantime I have left my PC to run `unit_tests` indefinitely under the debugger with the parameters:

```
--gtest_break_on_failure --gtest_filter=-apply_permutation*:AddressFromTXT*:base58*:bulletproofs*:decompose_amount_into_digits_test*:device*:checkpoints_is_alternative_block_allowed*:bulletproof*:canonical_amounts*:bootstrap_node_selector*:chacha8*:block_reward_and_last_block_weights*:block_reward_and_current_block_weight*:block_reward_and_already_generated_coins*:socks*:DNSResolver*:DNS_PUBLIC*:DNS*:uri*:test_epee_connection*:ringct*:zmq*:reader_writer_lock*:sha256*:multisig*:logging*:select_outputs --gtest_repeat=-1
```

But so far no luck.

In case anyone has any info on this, I appreciate it if shares it. 

# Discussion History
## 0xFFFC0000 | 2024-03-02T20:17:43+00:00
This bug happens rarely. The reason for this bug is if `join` throws an exception (due to low-level blocking of the thread) and is not successful here [1] to end the thread. That `worker` thread will be alive. Once leaving the scope, the error will happen [2]. 

`io_context.stopped()` returns `false` for the cases that `race_condition` error happens, showing that `io_context`  has not stopped.  As the screenshot shows.

![image](https://github.com/monero-project/monero/assets/136067098/75a07209-c6d0-4e00-a121-97505f58a2c4)


In an ordinary run, where there are no errors, `io_context.stopped()` returns `true`.  Look at the screenshot at the end of this comment.

This one-line PR will solve this problem [3].

1. https://github.com/0xFFFC0000/monero/pull/6/commits/c0b0742c89ae54cddd0c33b5bb2689acfa8be9fb#diff-0058af414c774eb3a4a62a610caba46f573f690c45a4a5dda734e9d7bcefad4aR1115
2. https://stackoverflow.com/a/7989043
3. https://github.com/0xFFFC0000/monero/pull/6


This is debug info from a correct run which does not result in `race_condition`: 

![image](https://github.com/monero-project/monero/assets/136067098/dbad63c9-07dc-458f-8eec-f9f03ee67370)




# Action History
- Created by: 0xFFFC0000 | 2024-03-02T10:44:20+00:00
