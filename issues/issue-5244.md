---
title: 'Failed sending transaction: ge_frombytes_vartime failed at 286'
source_url: https://github.com/monero-project/monero/issues/5244
author: gituser
assignees: []
labels: []
created_at: '2019-03-07T01:11:08+00:00'
updated_at: '2019-03-21T13:33:49+00:00'
type: issue
status: closed
closed_at: '2019-03-21T13:33:49+00:00'
---

# Original Description
Hi. 

After updating to `v0.14.0.1` one of the transactions failed for some reason with the error:
`ge_frombytes_vartime failed at 286`

I've found related issue - https://github.com/monero-project/monero/issues/1971 not quite sure if it's the same so I'm creating a new one.

Not sure why or what could be wrong as it happened for the first time after the update, no monero has been spent though in the result.

Also might be related - https://github.com/monero-project/monero/issues/4766#issuecomment-470333731 

After setting the `ulimit -l $((64*1048576))`, restarting wallet-rpc and re-sending the transaction it all worked just fine and transaction has been created.

The recipient is a regular monero address.

The log of wallet-rpc is below:
[Log](https://paste.fedoraproject.org/paste/KO16Fyw6j9J7vqGpNvlefA/raw)

# Discussion History
## moneromooo-monero | 2019-03-07T09:45:49+00:00
It looks like the problem is that your transaction picked an output on the chain with an invalid public key. This means someone sent an invalid monero tx at some point, and you tried to include it in a ring, and ring creation failed since that output is invalid. This is one of the lines where you replaced a number with "some number". These are not your outputs, but the ones the wallet selected to use as part of your ring. If you want to share them, I can write some code to fetch them and verify that one of them is indeed invalid.

The "Error locking page" errors are unrelated, and are not fatal.


## gituser | 2019-03-07T12:18:06+00:00
@moneromooo-monero  There you go:

[log](https://paste.fedoraproject.org/paste/EADTuJCrk7TBTa3WE1bu7w/raw)

## moneromooo-monero | 2019-03-07T14:23:57+00:00
Indeed, you picked 8950023, with pubkey cf631ae3691888e0d858e79bd6b37f1915493789bab4f85cf12bf001d4d86a04, which is not in the main subgroup. I will patch the wallet so these are automatically discarded.

## moneromooo-monero | 2019-03-07T16:02:33+00:00
https://github.com/monero-project/monero/pull/5248

## gituser | 2019-03-13T13:03:57+00:00
Happy to close this issue once this goes into the new release and there is a confirmation that fix is working.

Thanks.

## moneromooo-monero | 2019-03-21T13:25:51+00:00
+resolved

# Action History
- Created by: gituser | 2019-03-07T01:11:08+00:00
- Closed at: 2019-03-21T13:33:49+00:00
