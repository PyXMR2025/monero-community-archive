---
title: '"Failed to calculate TX prunable hash" in daemon hangs RPC wallet'
source_url: https://github.com/monero-project/monero/issues/5739
author: cotinco
assignees: []
labels: []
created_at: '2019-07-05T19:28:38+00:00'
updated_at: '2020-02-19T19:01:28+00:00'
type: issue
status: closed
closed_at: '2019-09-02T11:49:26+00:00'
---

# Original Description
Version v0.14.1.0 of rpc daemon sometimes gives error like
"019-07-05 19:16:19.634 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1014   Failed to calculate tx prunable hash
2019-07-05 19:16:19.634 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2019-07-05 19:16:19.634 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x10e) [0x5603066e92ae]:__cxa_throw+0x10e) [0x5603066e92ae]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2]  0x1f1) [0x56030678e0a1]:_ZN10cryptonote29get_transaction_prunable_hashERKNS_11transactionEPKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x1f1) [0x56030678e0a1]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0xcda) [0x56030649083a]:_ZN10cryptonote15core_rpc_server19on_get_transactionsERKN4epee10misc_utils11struct_initINS_28COMMAND_RPC_GET_TRANSACTIONS9request_tEEERNS3_INS4_10response_tEEEPKNS1_9net_utils23connection_context_baseE+0xcda) [0x56030649083a]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0x709d) [0x5603063b226d]:_ZN10cryptonote15core_rpc_server23handle_http_request_mapIN4epee9net_utils23connection_context_baseEEEbRKNS3_4http17http_request_infoERNS5_18http_response_infoERT_+0x709d) [0x5603063b226d]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0x1d1) [0x5603063de311]:_ZN10cryptonote15core_rpc_server19handle_http_requestERKN4epee9net_utils4http17http_request_infoERNS3_18http_response_infoERNS2_23connection_context_baseE+0x1d1) [0x5603063de311]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0xad) [0x56030638511d]:_ZN4epee9net_utils4http19http_custom_handlerINS0_23connection_context_baseEE14handle_requestERKNS1_17http_request_infoERNS1_18http_response_infoE+0xad) [0x56030638511d]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7]  0x13e) [0x56030632677e]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE32handle_request_and_send_responseERKNS1_17http_request_infoE+0x13e) [0x56030632677e]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8]  0x11b) [0x560306326bbb]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE27handle_retriving_query_bodyEv+0x11b) [0x560306326bbb]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9]  0x188) [0x5603063e2b08]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE14handle_buff_inERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x188) [0x5603063e2b08]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10]  0x3b) [0x5603063e33db]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE11handle_recvEPKvm+0x3b) [0x5603063e33db]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11]  0x204) [0x5603063e3644]:_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE11handle_readERKN5boost6system10error_codeEm+0x204) [0x5603063e3644]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12]  0x7a) [0x56030633b6ca]:_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSA_4http19http_custom_handlerINSA_23connection_context_baseEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISG_EEEEPFNS_3argILi1EEEvEPFNSR_ILi2EEEvEEEEESI_mEEEEvRPNS2_11strand_implERT_+0x7a) [0x56030633b6ca]
2019-07-05 19:16:19.636 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13]  0x69) [0x56030633b939]:_ZN5boost4asio6detail15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSA_4http19http_custom_handlerINSA_23connection_context_baseEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISG_EEEEPFNS_3argILi1EEEvEPFNSR_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEclISI_mEEvRKT_RKT0_+0x69) [0x56030633b939]
"

After that, rpc wallet becomes completely unusable. It just hangs on any rpc request.

Btw, there are also definitely some bugs in network p2p protocol of version 0.14.1.0 which hang operating incoming connections to "synchronizing" state from time to time, especially when those connections are exactly specified on the other side with --add-priority-node. Due to that bugs, I was forced to downgrade some of my nodes to 0.14.0.2 and probably will continue that process :(

Using Ubuntu 16.04/server, monero daemon&wallet are built from source, tests are ok.

# Discussion History
## moneromooo-monero | 2019-07-05T19:34:35+00:00
Is it fixed by https://github.com/monero-project/monero/pull/5634 ?

## moneromooo-monero | 2019-07-05T19:35:42+00:00
For the incoming connections thing, please file another bug with information on this.

## cotinco | 2019-07-05T19:46:22+00:00
> Is it fixed by #5634 ?

Thanks, applied #5634, will report if this issue will arise again.
About another issue, I'll describe it a bit later. I need some time to gather details from logs.

## nikitasius | 2019-07-05T19:47:11+00:00
i confirm. 0.14.1.0 have same issues
> Failed to calculate tx prunable hash

i will downgrade to 0.14.0.2
___
server have this error and wallet RPC dies (impossible to stop, till i stop the xmr server process).

## moneromooo-monero | 2019-07-05T21:15:37+00:00
If it still does, post the actual request you're making.

## nikitasius | 2019-07-05T21:34:58+00:00
> If it still does, post the actual request you're making.

in my case 0.14.1.0 was stucking while calling this:
```json
{"jsonrpc":"2.0","id":"0","method":"get_height"}
```

`id` not `0`. Just in example it's `0`.

## nikitasius | 2019-07-06T09:08:30+00:00
@moneromooo-monero in my case i had this issue only on mainnet.
Testnet server is working fine on 0.14.1.0.

## moneromooo-monero | 2019-07-07T15:50:29+00:00
Now that's very weird. get_height doesn't do anything with transactions... Something else is really messed up then.

When the RPC server is wedged like this, get an all thread stack trace:

gdb /path/to/binary PID
thread apply all bt

Replacing PID with the PID for the wedged server.

## normoes | 2019-08-19T09:28:21+00:00
Hey @moneromooo-monero,

We also experience these problems, so far on mainnet and stagenet when running `v0.14.1.2`.

Downgrading to `v0.14.0.2` exits with **db mismatch**.

Can I help you in any way? We have spare resources available to run patched versions of the daemon.

## moneromooo-monero | 2019-08-19T11:57:30+00:00
Did you use the patch above ?

## normoes | 2019-08-19T12:00:30+00:00
Didn't see that, sorry. I'll give it a try.

## normoes | 2019-08-19T12:05:50+00:00
@moneromooo-monero 

This means to deploy the monero `master` branch (https://github.com/monero-project/monero/pull/5634)?
Will it update the database when I was running `v0.14.1.2` previously?

## nikitasius | 2019-08-19T14:53:45+00:00
> Hey @moneromooo-monero,
> 
> We also experience these problems, so far on mainnet and stagenet when running `v0.14.1.2`.
> 
> Downgrading to `v0.14.0.2` exits with **db mismatch**.
> 
> Can I help you in any way? We have spare resources available to run patched versions of the daemon.

In my case i resynced whole DB and lost ~6 hours (due last 7% was extremely long).

## moneromooo-monero | 2019-08-19T15:28:56+00:00
Apply the patch on top of whatever you're using. The patch does not change the database format. If you use another branch, other patches might.

## normoes | 2019-08-19T15:55:10+00:00
Just to add some info here. For anyone who doesn't know that. You can add `.diff` or `.patch` to the URL of the pull request and it shows the raw diff or patch.

https://patch-diff.githubusercontent.com/raw/monero-project/monero/pull/5634.patch

source: https://stackoverflow.com/questions/6188591/download-github-pull-request-as-unified-diff

## nikitasius | 2019-08-20T11:42:42+00:00
@moneromooo-monero it work fine on older version.
0.14.1.2 have it fixed?

## moneromooo-monero | 2019-08-20T12:30:34+00:00
The PR page shows it was merged 6 days ago, so it was not in the latest release.

## normoes | 2019-08-20T13:50:15+00:00
Patch applied, thanks.

## moneromooo-monero | 2019-09-02T11:16:45+00:00
Can you confirm the patch fixed it ?

## normoes | 2019-09-02T11:32:29+00:00
We did not experience any further problems, since we patched the daemon.
So, I would say, it works better than before :)

In other words, yes, the patch seems to have fixed it.

## moneromooo-monero | 2019-09-02T11:44:56+00:00
Thanks

+resolved

## nikitasius | 2019-12-12T18:37:26+00:00
i have this error on v0.15.0.1-release

wallet not hangs, but it have those errors

## nikitasius | 2019-12-12T18:37:53+00:00
```
2019-12-04 10:20:01.385 W Detached blockchain on height 1981383, transfers detached 0, blocks detached 1
2019-12-04 20:59:44.768 E wrong number of additional derivations
2019-12-04 21:02:24.960 E wrong number of additional derivations
2019-12-04 21:06:25.221 E wrong number of additional derivations
2019-12-05 11:35:30.849 W Detaching blockchain on height 1982145
2019-12-05 11:35:30.877 W Detached blockchain on height 1982145, transfers detached 0, blocks detached 1
2019-12-08 19:59:03.424 E Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:03.425 E Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:03.425 E Failed to calculate transaction hash
2019-12-08 19:59:23.444 E Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:23.444 E Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:23.444 E Failed to calculate transaction hash
2019-12-08 19:59:43.461 E Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:43.461 E Cannot calculate the hash of a pruned transaction
2019-12-08 19:59:43.461 E Failed to calculate transaction hash
2019-12-08 20:00:03.477 E Cannot calculate the hash of a pruned transaction
2019-12-08 20:00:03.478 E Cannot calculate the hash of a pruned transaction
2019-12-08 20:00:03.478 E Failed to calculate transaction hash
```

## normoes | 2020-01-08T16:31:56+00:00
@moneromooo-monero 

We also see those errors.

Coincidentally, whenever they happen, our clients (that connect to the wallet RPC) die.

Could you maybe have another look at this, please?

## Kukks | 2020-02-19T12:57:54+00:00
I also get these errors when running 0.15.0.0.  Calling `get_transfer_by_txid` times out. 

## selsta | 2020-02-19T16:18:12+00:00
@Kukks Can you try latest CLI release (v0.15.0.1) ? Edit: Appears you might have to compile with https://github.com/monero-project/monero/pull/6268

## Kukks | 2020-02-19T19:01:28+00:00
> 
> 
> @Kukks Can you try latest CLI release (v0.15.0.1) ? Edit: Appears you might have to compile with #6268

Updated to 15.0.1 with same result
```
xmr_wallet_rpc   | 2020-02-19 18:59:18.469      E Cannot calculate the hash of a pruned transaction
xmr_wallet_rpc   | 2020-02-19 18:59:18.470      E Cannot calculate the hash of a pruned transaction
xmr_wallet_rpc   | 2020-02-19 18:59:18.470      E Failed to calculate transaction hash
```

This is for the BTCPay Server integration so I'll only use stable release builds. :) 

# Action History
- Created by: cotinco | 2019-07-05T19:28:38+00:00
- Closed at: 2019-09-02T11:49:26+00:00
