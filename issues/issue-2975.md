---
title: Improve multisig API to support web applications and automated payment systems
source_url: https://github.com/monero-project/monero/issues/2975
author: ghost
assignees: []
labels:
- proposal
created_at: '2017-12-20T16:36:39+00:00'
updated_at: '2018-07-09T05:58:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The following issues make using the multisignature features difficult for application developers:

* Multisigature wallets are not reusable for different participants e.g. Alice-Bob-Mary can conduct a multisignature transaction but when Alice-Jake-Steve want to conduct a multisignature transaction a new wallet must be created.
* Monitoring multiple multisignature wallets for incoming transfers requires loading wallet files and rescanning. Running multiple instances of `monero-wallet-rpc` looking for incoming payments is unlikely to scale effectively and process/file management places a larger burden on the application developer.

Ideally I think somehow being able to keep multiple multisignature addresses in a single wallet would be the best solution.

Ideally this would allow:

* creation of a multisignature address via the API as it stands.
* the ability to add more multisignature addresses using other participants (addresses could be listed using `address all` CLI and RPC calls - also returning details of participants etc).
* retrieving results of all transactions across all multisignature addresses using the `show_transfers` or `get_transfers` call along with details that help identify which address the transaction belongs to.
* `import_multisig_info/export_multisig_info` from any of the multiple multisig addresses by using an identifier.
* load, sign and submit transactions for any of the multiple multisig addresses by using an identifier.

It's likely that I've either: misunderstood current functionality, missed edge cases and/or preemptively created an issue of which the team is aware and has plans to fix. Therefore comments are encourage and I'd like to thank the team for their hard work shipping this feature.

# Discussion History
## stoffu | 2017-12-21T01:17:04+00:00
The `address all` command is specifically designed for displaying all subaddresses created so far for a given account. The subaddress scheme and the multisig scheme are technically entirely unrelated: each multisig wallet necessarily has a unique pair of view/spend keys, while all subaddresses are generated from the same pair of view/spend keys. Therefore, they shouldn't be mixed up in the software as well.

The idea of managing multiple multisig wallets is similar to that of managing multiple normal wallets. Currently, the software doesn't support handling multiple wallets within the same instance (i.e. you need to launch the program separately). This issue was already raised in the past multiple times (especially from the GUI side) and I do see some merit in such a capability, but implementing it seems to require substantial change to the current wallet code. I'm not sure how much priority is being put on this.




## ghost | 2017-12-21T02:58:09+00:00
>The address all command is specifically designed for displaying all subaddresses created so far for a given account. 

In that case it's probably appropriate to create a new `multisig_addresses` command or even roll out a new API to a new executable. I think though if multiple wallets is going to be supported at some point then it probably makes sense to support them for non-multisignature transactions as well.

>This issue was already raised in the past multiple times (especially from the GUI side) and I do see some merit in such a capability, but implementing it seems to require substantial change to the current wallet code.

I understand how monumental of a task it would be to do this. I just think the current API is difficult to work with unless done manually and will hamper adoption of this feature.

## emesik | 2017-12-27T14:07:39+00:00
There's a `wallet_dir` option you may use in wallet RPC server. It allows you to switch a running instance to a new wallet in the given directory, however you'll have to wait idly until it synchronizes.

I know this is not a solution, but a hint of a different approach with current tools.

## dEBRUYNE-1 | 2018-01-08T12:39:28+00:00
+proposal

## lessless | 2018-07-09T05:58:06+00:00
Being able to  to monitor multiple (multisignature) wallets through one RPC client would be fantastic. 
Although I do not understand what is the value of  making multisiganture wallets reusable and how will it work.
Requirement to create a new wallet for a new set of participants is extremely logical - I do not want anyone to be able to use my historical data to create new transaction. Or I'm loosing something here? 

# Action History
- Created by: ghost | 2017-12-20T16:36:39+00:00
