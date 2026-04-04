---
title: This wallet is multisig, and multisig is disabled on exchange_multisig_keys
source_url: https://github.com/monero-project/monero/issues/9488
author: zbder
assignees: []
labels:
- question
created_at: '2024-09-22T10:57:01+00:00'
updated_at: '2024-10-01T12:23:40+00:00'
type: issue
status: closed
closed_at: '2024-10-01T12:23:40+00:00'
---

# Original Description
I am trying to create a new wallet and make it run a few multisig  commands using rpc but i cant get beyond this point.

`Code`
> $createResult = make_multisig_request('create_wallet', [
    'filename' => $walletName,
    'password' => $walletPass,
    'language' => 'English'
]);
$createResult = make_multisig_request('open_wallet', [ 'filename' => $walletName, 'password' => $walletPass ]);
$prepareMultisig = make_multisig_request('prepare_multisig');
$prepareMultisig = json_decode($prepareMultisig, true);
$myMultisigKey = $prepareMultisig['result']['multisig_info'];
$makeMultisig = make_multisig_request('make_multisig', [
    'threshold' => 2,
    'password' => $walletPass,
    'multisig_info' => [
        'Example from second party',
        'Example from third party'
    ]
]);
// Until here it works super fine but on exchange_multisig_keys i get the error message listed below
$makeMultisig = make_multisig_request('exchange_multisig_keys', [
     'multisig_info' => [
        'Example from second party',
        'Example from third party'
    ]
]);

"This wallet is multisig, and multisig is disabled. Multisig is an experimental feature and may have bugs. Things that could go wrong include: funds sent to a multisig wallet can't be spent at all, can only be spent with the participation of a malicious group member, or can be stolen by a malicious group member. You can enable it by running this once in monero-wallet-cli: set enable-multisig-experimental 1"

When i manually run "monero-wallet-cli: set enable-multisig-experimental 1", it also allows me to use the command without issues but i seemingly cannot make it working without manually running it, when i use shell_exec or a bash script it says the .keys file would be used by another programm - when i run it manually it works fine. I also cannot set that from rpc, also tried to run close_wallet from rpc before but it doesnt work either. Also tried to add enable-multisig-experimental=1 in the monerod.conf which seems to have no effect and also tried this "Wallet: disable multisig by default, enable with --enable-multisig-experimental (#[8328](https://github.com/monero-project/monero/pull/8328))" but seemingly it does not exist in 0.18.3.4 anymore and i have no idea how to bypass this issue anymore - did anyone make the same experience and may have a helpful hint for me ?

# Discussion History
## zbder | 2024-09-23T14:17:05+00:00
Solved it.

## 0xFFFC0000 | 2024-10-01T12:22:34+00:00
> Solved it.

I would appreciate it if in your spare time write how you solved it, in case later someone founds this specific page. 


I am closing this issue. But please feel free to comment. 

# Action History
- Created by: zbder | 2024-09-22T10:57:01+00:00
- Closed at: 2024-10-01T12:23:40+00:00
