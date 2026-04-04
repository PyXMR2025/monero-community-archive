---
title: 'Testnet: "Error: Reason: fee too low" in cold sign transfer'
source_url: https://github.com/monero-project/monero/issues/4115
author: zhongqiuwood
assignees: []
labels: []
created_at: '2018-07-09T11:55:38+00:00'
updated_at: '2018-07-16T23:25:01+00:00'
type: issue
status: closed
closed_at: '2018-07-16T23:25:01+00:00'
---

# Original Description
## Background
This happened to me in testnet, not sure if it does in mainnet.

I was asked for more fee by cold sign transfer than a normally direct transfer.

I've successfully transfered 0.02 xmr coin from A address to B address by normally direct transfer:  `transfer unimportant A1puKBLCKkdgB8D2LkGzQPYU8mYjVohwEgoAqcLKjQ2PCgAci6T5wMsVHhXekcPP7sEYqkR4KBGddAbErMTJhd737f9oAAD 0.02`

However I was told "Error: Reason: fee too low" if cold sign transfer in used by following steps with **the same transfer fee**:
```
1. In hot wallet: ` transfer unimportant A1puKBLCKkdgB8D2LkGzQPYU8mYjVohwEgoAqcLKjQ2PCgAci6T5wMsVHhXekcPP7sEYqkR4KBGddAbErMTJhd737f9oAAD 0.02`
2. Copy unsigned_monero_tx to cold wallet and then execute command in  cold wallet : `sign_transfer`
3. Copy signed_monero_tx to hot wallet and then execute in hot wallet: `submit_transfer`
4. Then I was told `Error: transaction <124cbc56d8aea47704c8a1aedd39398a6d1878e0664f0745a5739119b55a5a73> was rejected by daemon with status: Failed
Error: Reason: fee too low`
```

## Normally direct transfer ouput
```
[wallet 9u7McB]: transfer unimportant A1puKBLCKkdgB8D2LkGzQPYU8mYjVohwEgoAqcLKjQ2PCgAci6T5wMsVHhXekcPP7sEYqkR4KBGddAbErMTJhd737f9oAAD 0.02
Wallet password:
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y

Transaction 1/1:
Spending from address index 0
Sending 0.020000000000.  The transaction fee is 0.000868020000
Is this okay?  (Y/Yes/N/No): y
Transaction successfully submitted, transaction <fee3fe65807f3467825e089f555ff38ce4f1e03ff33f1840625b6c441575d64d>
You can check its status by using the `show_transfers` command.

```

## Cold sign transfer ouput
```
########################
## generate unsigned_monero_tx
$ ./monero-wallet-cli --testnet --daemon-address localhost:28081 --log-level 4 --password 1 --wallet-file /Users/yanpeiling/.bitmonero/key/viewkeywallet/yplviewkeywallet --command transfer unimportant A1puKBLCKkdgB8D2LkGzQPYU8mYjVohwEgoAqcLKjQ2PCgAci6T5wMsVHhXekcPP7sEYqkR4KBGddAbErMTJhd737f9oAAD 0.02
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Lithium Luna' (v0.12.0.0-master-release)
Logging to /Users/yanpeiling/Downloads/software/develop/coin/xmr/monero-v0.12.0.0/monero-wallet-cli.log
Opened watch-only wallet: 9sXXpRtxYgh5yMYexKccr4dx35JM8rc1e8M7UDBfFCQmSgau1mQxTLk3j8MStt4CCnd8C99BGTw9uQ4DqhwtKq8r32pBpxe
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Wallet password:
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y

Transaction 1/1:
Spending from address index 0
Sending 0.020000000000.  The transaction fee is 0.000867990000
Is this okay?  (Y/Yes/N/No): y
Unsigned transaction(s) successfully written to file: unsigned_monero_tx




########################
## sign_transfer
[yanpeiling:~/.bitmonero/key/viewkeywallet]$ ./monero-wallet-cli --testnet 
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Lithium Luna' (v0.12.0.0-master-release)
Logging to /Users/yanpeiling/Downloads/software/develop/coin/xmr/monero-v0.12.0.0/monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): /Users/yanpeiling/.bitmonero/key/viewkeywallet/yanpeiling
Wallet and key files found, loading...
Wallet password:
Opened wallet: 9sXXpRtxYgh5yMYexKccr4dx35JM8rc1e8M7UDBfFCQmSgau1mQxTLk3j8MStt4CCnd8C99BGTw9uQ4DqhwtKq8r32pBpxe
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 2
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 9sXXpR     1607.152883133920     1607.152883133920       Primary account
----------------------------------------------------------------------------------
          Total     1607.152883133920     1607.152883133920
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 1607.152883133920, unlocked balance: 1607.152883133920
Background refresh thread started
[wallet 9sXXpR]: sign_transfer
Wallet password:
Loaded 1 transactions, for 15.300536930859, fee 0.000867990000, sending 0.020000000000 to A1puKBLCKkdgB8D2LkGzQPYU8mYjVohwEgoAqcLKjQ2PCgAci6T5wMsVHhXekcPP7sEYqkR4KBGddAbErMTJhd737f9oAAD, 15.279668940859 change to 9sXXpRtxYgh5yMYexKccr4dx35JM8rc1e8M7UDBfFCQmSgau1mQxTLk3j8MStt4CCnd8C99BGTw9uQ4DqhwtKq8r32pBpxe, with min ring size 7, no payment ID. 73 outputs to import. Is this okay? (Y/Yes/N/No): y
Transaction successfully signed to file signed_monero_tx, txid 124cbc56d8aea47704c8a1aedd39398a6d1878e0664f0745a5739119b55a5a73




########################
## submit_transfer
[wallet 9sXXpR]: submit_transfer
Loaded 1 transactions, for 15.300536930859, fee 0.000867990000, sending 0.020000000000 to A1puKBLCKkdgB8D2LkGzQPYU8mYjVohwEgoAqcLKjQ2PCgAci6T5wMsVHhXekcPP7sEYqkR4KBGddAbErMTJhd737f9oAAD, 15.279668940859 change to 9sXXpRtxYgh5yMYexKccr4dx35JM8rc1e8M7UDBfFCQmSgau1mQxTLk3j8MStt4CCnd8C99BGTw9uQ4DqhwtKq8r32pBpxe, with min ring size 7, no payment ID. 73 key images to import. Is this okay? (Y/Yes/N/No): y
Error: transaction <124cbc56d8aea47704c8a1aedd39398a6d1878e0664f0745a5739119b55a5a73> was rejected by daemon with status: Failed
Error: Reason: fee too low

```



# Discussion History
## moneromooo-monero | 2018-07-09T12:56:56+00:00
Did you try with up to date code ? This is supposed to be fixed in d7a6b72c15f898c45a71831cca04cf0fc968ad91.

## zhongqiuwood | 2018-07-09T14:25:32+00:00
Thank you. Let me try to see if the fix made it 👍 

## zhongqiuwood | 2018-07-10T06:42:23+00:00
Hi @moneromooo-monero, still not woking by using v0.12.3.0 `https://github.com/monero-project/monero/releases/tag/v0.12.3.0` that was released after the fix [d7a6b72](https://github.com/monero-project/monero/commit/d7a6b72c15f898c45a71831cca04cf0fc968ad91)

Detail:
```
########################################
## show version
[yanpeiling:...ro-github/build/release/bin]$ ./monero-wallet-cli --version                                                                                                                (master)
Monero 'Lithium Luna' (v0.12.3.0-release)



########################################
## use hot wallet to generate unsigned_monero_tx
[yanpeiling:...ro-github/build/release/bin]$ ./monero-wallet-cli --testnet --daemon-address localhost:28081 --log-level 4 --password 1 --wallet-file /Users/yanpeiling/.bitmonero/key/viewkeywallet/yplviewkeywallet --command transfer unimportant A1puKBLCKkdgB8D2LkGzQPYU8mYjVohwEgoAqcLKjQ2PCgAci6T5wMsVHhXekcPP7sEYqkR4KBGddAbErMTJhd737f9oAAD 0.02  (master)
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on an another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Lithium Luna' (v0.12.3.0-release)
Logging to ./monero-wallet-cli.log
Opened watch-only wallet: 9sXXpRtxYgh5yMYexKccr4dx35JM8rc1e8M7UDBfFCQmSgau1mQxTLk3j8MStt4CCnd8C99BGTw9uQ4DqhwtKq8r32pBpxe
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Wallet password:
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y

Transaction 1/1:
Spending from address index 0
Sending 0.020000000000.  The transaction fee is 0.000867630000
Is this okay?  (Y/Yes/N/No): y
Unsigned transaction(s) successfully written to file: unsigned_monero_tx


########################################
## use cold wallet to sign the tx
[yanpeiling:...ro-github/build/release/bin]$ ./monero-wallet-cli --testnet                                                                                                                                                                                                                                                                                (master)
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on an another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Lithium Luna' (v0.12.3.0-release)
Logging to ./monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): /Users/yanpeiling/.bitmonero/key/viewkeywallet/yanpeiling
Wallet and key files found, loading...
Wallet password:
Opened wallet: 9sXXpRtxYgh5yMYexKccr4dx35JM8rc1e8M7UDBfFCQmSgau1mQxTLk3j8MStt4CCnd8C99BGTw9uQ4DqhwtKq8r32pBpxe
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 215
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 9sXXpR     1607.152883133920     1607.152883133920       Primary account
----------------------------------------------------------------------------------
          Total     1607.152883133920     1607.152883133920
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 1607.152883133920, unlocked balance: 1607.152883133920
Background refresh thread started

[wallet 9sXXpR]: sign_transfer
Wallet password:
Loaded 1 transactions, for 15.300536930859, fee 0.000867630000, sending 0.020000000000 to A1puKBLCKkdgB8D2LkGzQPYU8mYjVohwEgoAqcLKjQ2PCgAci6T5wMsVHhXekcPP7sEYqkR4KBGddAbErMTJhd737f9oAAD, 15.279669300859 change to 9sXXpRtxYgh5yMYexKccr4dx35JM8rc1e8M7UDBfFCQmSgau1mQxTLk3j8MStt4CCnd8C99BGTw9uQ4DqhwtKq8r32pBpxe, with min ring size 7, no payment ID. 73 outputs to import. Is this okay? (Y/Yes/N/No): y
Transaction successfully signed to file signed_monero_tx, txid 71be7e6bdf4c9ba40fd80b18343a209e5decdfdcd465803b7390bb926be0826f




########################################
## use hot wallet to submit_transfer
[yanpeiling:...ro-github/build/release/bin]$ ./monero-wallet-cli --testnet                                                                                                                                                                                                                                                                                (master)
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on an another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Lithium Luna' (v0.12.3.0-release)
Logging to ./monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): /Users/yanpeiling/.bitmonero/key/viewkeywallet/yplviewkeywallet
Wallet and key files found, loading...
Wallet password:
Opened watch-only wallet: 9sXXpRtxYgh5yMYexKccr4dx35JM8rc1e8M7UDBfFCQmSgau1mQxTLk3j8MStt4CCnd8C99BGTw9uQ4DqhwtKq8r32pBpxe
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 139
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 9sXXpR     1695.356762752805     1695.356762752805       Primary account
----------------------------------------------------------------------------------
          Total     1695.356762752805     1695.356762752805
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 1695.356762752805, unlocked balance: 1695.356762752805
Background refresh thread started

[wallet 9sXXpR]: submit_transfer
Loaded 1 transactions, for 15.300536930859, fee 0.000867630000, sending 0.020000000000 to A1puKBLCKkdgB8D2LkGzQPYU8mYjVohwEgoAqcLKjQ2PCgAci6T5wMsVHhXekcPP7sEYqkR4KBGddAbErMTJhd737f9oAAD, 15.279669300859 change to 9sXXpRtxYgh5yMYexKccr4dx35JM8rc1e8M7UDBfFCQmSgau1mQxTLk3j8MStt4CCnd8C99BGTw9uQ4DqhwtKq8r32pBpxe, with min ring size 7, no payment ID. 73 key images to import. Is this okay? (Y/Yes/N/No): y
Error: transaction <71be7e6bdf4c9ba40fd80b18343a209e5decdfdcd465803b7390bb926be0826f> was rejected by daemon with status: Failed
Error: Reason: fee too low
```


## moneromooo-monero | 2018-07-10T10:38:37+00:00
If you're using the v0.12.3.0 tag, this does not seem to include that patch. Can you check again ?

## qzhongwood | 2018-07-11T00:57:44+00:00
@moneromooo-monero Many thanks. The master branch code works!

## moneromooo-monero | 2018-07-16T23:20:34+00:00
+resolved

# Action History
- Created by: zhongqiuwood | 2018-07-09T11:55:38+00:00
- Closed at: 2018-07-16T23:25:01+00:00
