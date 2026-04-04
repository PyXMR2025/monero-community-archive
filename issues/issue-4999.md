---
title: 'monero-wallet-rpc error in finalize_multisig '
source_url: https://github.com/monero-project/monero/issues/4999
author: jacoblyles
assignees: []
labels: []
created_at: '2018-12-19T19:30:56+00:00'
updated_at: '2018-12-21T22:10:24+00:00'
type: issue
status: closed
closed_at: '2018-12-21T22:10:24+00:00'
---

# Original Description
Release is Monero 'Beryllium Bullet' (v0.13.0.4-release) on Mac OSX.

I am trying to run the `finalize_mulitisig` step when making a 2 of 3 mulitisignature wallet. It succeeds using the `monero-wallet-cli` command line, but it fails when trying to do the same through `monero-wallet-rpc`

I am supplying the parameter
` {"mulitisig_info": ["MultisigxV1YquNAruLtrCVxKkLPpTmi2egFT28xX6QVhuTWWHBoJ72P4jptUht69mM88NDbHcUTpetBF9zv3qmKKyQ56M3HX7VY8T2CyXpbgoeqSgs6yifZrik9XUaAQADo777MwuNqa8WgBMJYeqG23E1S8joSA3Bah62pCuL7jPdFF8x8TWX2foPV12FGPpvYWPCdUwffjVSwXZhx5dH3YucePWCNBaKWZrb", "MultisigxV1jWjoEfJUnQGXNfohRZ9oBQKdytqaEMXxvd3ASUbxptWvPNncwhqiLM24iY8YYPadci9kDJrMiue9y5eteqTDCBGHY8T2CyXpbgoeqSgs6yifZrik9XUaAQADo777MwuNqa8WCYDq3KrtJ1XC4YSaMB6bw3SBwrXar1KisUgK8vhvUdpFS2LjNDrSbn2X6c4PenaEV4WXFcYwvWxcYLune5tWATND"]}`

And the response is

`{'error': {'code': -33, 'message': 'Needs multisig info from more participants'}, 'id': '0', 'jsonrpc': '2.0'}`

However, when I run the following command at the `monero-wallet-cli`, it succeeds:

`finalize_multisig MultisigxV1YquNAruLtrCVxKkLPpTmi2egFT28xX6QVhuTWWHBoJ72P4jptUht69mM88NDbHcUTpetBF9zv3qmKKyQ56M3HX7VY8T2CyXpbgoeqSgs6yifZrik9XUaAQADo777MwuNqa8WgBMJYeqG23E1S8joSA3Bah62pCuL7jPdFF8x8TWX2foPV12FGPpvYWPCdUwffjVSwXZhx5dH3YucePWCNBaKWZrb MultisigxV1jWjoEfJUnQGXNfohRZ9oBQKdytqaEMXxvd3ASUbxptWvPNncwhqiLM24iY8YYPadci9kDJrMiue9y5eteqTDCBGHY8T2CyXpbgoeqSgs6yifZrik9XUaAQADo777MwuNqa8WCYDq3KrtJ1XC4YSaMB6bw3SBwrXar1KisUgK8vhvUdpFS2LjNDrSbn2X6c4PenaEV4WXFcYwvWxcYLune5tWATND`

# Discussion History
## naughtyfox | 2018-12-21T15:54:27+00:00
Could you please provide us with full request-response log?

## naughtyfox | 2018-12-21T16:58:05+00:00
Just tried to reproduce it. 
**1**. Created 3 new wallets and started `monero-wallet-rpc` with the following commands:
```sh
./monero-wallet-rpc --daemon-address=monero-stage.exan.tech:38081 --trusted-daemon --password=123 --stagenet --rpc-bind-port=1025 --disable-rpc-login --wallet-file=1
```
```sh
./monero-wallet-rpc --daemon-address=monero-stage.exan.tech:38081 --trusted-daemon --password=123 --stagenet --rpc-bind-port=1026 --disable-rpc-login --wallet-file=2
```
```sh
./monero-wallet-rpc --daemon-address=monero-stage.exan.tech:38081 --trusted-daemon --password=123 --stagenet --rpc-bind-port=1027 --disable-rpc-login --wallet-file=3
```

**2**. Created 2/3 multisig wallet with json rpc api. Here is the log:
```
wallet 1:
{"jsonrpc": "2.0", "method": "prepare_multisig", "id": 1}
->
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "multisig_info": "MultisigV123Xx2ifTafNCoXpJeGyCw1R2hHpFgyv7cdzvj7Uux2MjdohX9Vt1QJVgdfp2zzQff9arML2E63bkk6eC7vLpvNCVap3UHoQdntohaQp5Gji3gXP2vyxAV4cvuiagbeLhs1aQZzo7ANdnnVcKXEMLEtvr7TEySSLRnzVV5ZE8gRYXjtxP"
    }
}

wallet 2:
{"jsonrpc": "2.0", "method": "prepare_multisig", "id": 1}
->
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "multisig_info": "MultisigV1LwYhuvJWENmdRkYT8BkzngRZGfTt15nEaSzf1oe4Qq4mP25W9CHszxeD4ZeJdbK6GkH9EFsKfuVB3U7taYvtEYj4V8JVsvybuUVYCkmAza5nesMPz2XqjQc5xNt6KTGBCeH4Z8LfX1m6ibQcyQknJphc47gDognemLH71auz8R8B5T23"
    }
}

wallet 3:
{"jsonrpc": "2.0", "method": "prepare_multisig", "id": 1}
->
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "multisig_info": "MultisigV13A8SuAMTkFwWAR2XL5ne4q8Z4RtyEXpw6EpWiuJ1avnXFtME78nYLJUX4SMSUr2a8xFxEtEhyqZGHd3jvPvmBJHJAqXk6Z2Zr7rgHVZsF3a6wNhfAaeDhU9kA4w5quGkYpVjDFQUUFK7L1TSdU4T4AT2Yicc7KHVWnntCR9VmX3yVjj2"
    }
}
===================
wallet 1:
{"jsonrpc": "2.0", 
"method": "make_multisig", 
"params": {
	"multisig_info": ["MultisigV1LwYhuvJWENmdRkYT8BkzngRZGfTt15nEaSzf1oe4Qq4mP25W9CHszxeD4ZeJdbK6GkH9EFsKfuVB3U7taYvtEYj4V8JVsvybuUVYCkmAza5nesMPz2XqjQc5xNt6KTGBCeH4Z8LfX1m6ibQcyQknJphc47gDognemLH71auz8R8B5T23", "MultisigV13A8SuAMTkFwWAR2XL5ne4q8Z4RtyEXpw6EpWiuJ1avnXFtME78nYLJUX4SMSUr2a8xFxEtEhyqZGHd3jvPvmBJHJAqXk6Z2Zr7rgHVZsF3a6wNhfAaeDhU9kA4w5quGkYpVjDFQUUFK7L1TSdU4T4AT2Yicc7KHVWnntCR9VmX3yVjj2"],
	"threshold": 2,
	"password": "123"
},
"id": 1}
->
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "address": "51sLpF8fWaK11111111111111111111111111111111116hUVejwnnZaYvGvYL5eiYdwdbn5ffdrN96FMmRKiJwdFahF6kf",
        "multisig_info": "MultisigxV1aFiBjG3Ha9jbbmQ6hXuD2ibi6jUDiBUu8DVMRWHbLTSZ55a1xM8qKKoKH1ErKVSFBJKt1ATPVamevCX4bqnT4Sn31L9TQW4ZASehyxqfJjcRs7QjeFsfKHqbiKSrXyVLq4Mw6Fp6BWpUzx2f6VBbStLxC6LMxc4RKaCm1GjwWKc8FbyAWTbvEYJ9mWFXm8pz3LsUn3VRSwBgMyDgsCN2Ax2CPbAo"
    }
}

wallet 2:
{"jsonrpc": "2.0", 
"method": "make_multisig", 
"params": {
	"multisig_info": ["MultisigV123Xx2ifTafNCoXpJeGyCw1R2hHpFgyv7cdzvj7Uux2MjdohX9Vt1QJVgdfp2zzQff9arML2E63bkk6eC7vLpvNCVap3UHoQdntohaQp5Gji3gXP2vyxAV4cvuiagbeLhs1aQZzo7ANdnnVcKXEMLEtvr7TEySSLRnzVV5ZE8gRYXjtxP", "MultisigV13A8SuAMTkFwWAR2XL5ne4q8Z4RtyEXpw6EpWiuJ1avnXFtME78nYLJUX4SMSUr2a8xFxEtEhyqZGHd3jvPvmBJHJAqXk6Z2Zr7rgHVZsF3a6wNhfAaeDhU9kA4w5quGkYpVjDFQUUFK7L1TSdU4T4AT2Yicc7KHVWnntCR9VmX3yVjj2"],
	"threshold": 2,
	"password": "123"
},
"id": 1}
->
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "address": "51sLpF8fWaK11111111111111111111111111111111116hUVejwnnZaYvGvYL5eiYdwdbn5ffdrN96FMmRKiJwdFahF6kf",
        "multisig_info": "MultisigxV1ZSRa5KBD6y32nTFbKSgxUweX1w7QomiJ2TToarTcFUes55a1xM8qKKoKH1ErKVSFBJKt1ATPVamevCX4bqnT4Sn3c7ZtATM6abPVkRccQ7aZzdjofMbgUur6F5qi1V3xPxkRWS8mxferscZTPUxsQAApQkEtoWnnrqddj3F4sAdKPQxCgVwtP6S4xTh7ajuTkQZrFiC2YgtoqmipxhmFnQYo8H1h"
    }
}

wallet 3:
{"jsonrpc": "2.0", 
"method": "make_multisig", 
"params": {
	"multisig_info": ["MultisigV123Xx2ifTafNCoXpJeGyCw1R2hHpFgyv7cdzvj7Uux2MjdohX9Vt1QJVgdfp2zzQff9arML2E63bkk6eC7vLpvNCVap3UHoQdntohaQp5Gji3gXP2vyxAV4cvuiagbeLhs1aQZzo7ANdnnVcKXEMLEtvr7TEySSLRnzVV5ZE8gRYXjtxP", "MultisigV1LwYhuvJWENmdRkYT8BkzngRZGfTt15nEaSzf1oe4Qq4mP25W9CHszxeD4ZeJdbK6GkH9EFsKfuVB3U7taYvtEYj4V8JVsvybuUVYCkmAza5nesMPz2XqjQc5xNt6KTGBCeH4Z8LfX1m6ibQcyQknJphc47gDognemLH71auz8R8B5T23"],
	"threshold": 2,
	"password": "123"
},
"id": 1}
->
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "address": "51sLpF8fWaK11111111111111111111111111111111116hUVejwnnZaYvGvYL5eiYdwdbn5ffdrN96FMmRKiJwdFahF6kf",
        "multisig_info": "MultisigxV1D87ikc4UGNs7oVRvnSwLTfdDMPLcFfkufMsBiCm435oE1L9TQW4ZASehyxqfJjcRs7QjeFsfKHqbiKSrXyVLq4Mwc7ZtATM6abPVkRccQ7aZzdjofMbgUur6F5qi1V3xPxkRAya5Te8dVCkPxYxHPzdN4DKLni4e9YVUGegWwZHDGWuMUGJQXG9YUVEZDqMfnLvoaqCTpDQN31rKG7TvqCSVRNKe"
    }
}

========================================

wallet 1:
{"jsonrpc": "2.0", 
"method": "finalize_multisig", 
"params": {
	"multisig_info": ["MultisigxV1ZSRa5KBD6y32nTFbKSgxUweX1w7QomiJ2TToarTcFUes55a1xM8qKKoKH1ErKVSFBJKt1ATPVamevCX4bqnT4Sn3c7ZtATM6abPVkRccQ7aZzdjofMbgUur6F5qi1V3xPxkRWS8mxferscZTPUxsQAApQkEtoWnnrqddj3F4sAdKPQxCgVwtP6S4xTh7ajuTkQZrFiC2YgtoqmipxhmFnQYo8H1h", "MultisigxV1D87ikc4UGNs7oVRvnSwLTfdDMPLcFfkufMsBiCm435oE1L9TQW4ZASehyxqfJjcRs7QjeFsfKHqbiKSrXyVLq4Mwc7ZtATM6abPVkRccQ7aZzdjofMbgUur6F5qi1V3xPxkRAya5Te8dVCkPxYxHPzdN4DKLni4e9YVUGegWwZHDGWuMUGJQXG9YUVEZDqMfnLvoaqCTpDQN31rKG7TvqCSVRNKe"],
	"password": "123"
},
"id": 1}
->
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "address": "58F2pcGYn8EVdDBqAt1Xp2EJNj8Qim16qLPdNdLUwTHv3GpDg9PMhGHaYvGvYL5eiYdwdbn5ffdrN96FMmRKiJwdFb5wcDi"
    }
}

wallet 2:
{"jsonrpc": "2.0", 
"method": "finalize_multisig", 
"params": {
	"multisig_info": ["MultisigxV1aFiBjG3Ha9jbbmQ6hXuD2ibi6jUDiBUu8DVMRWHbLTSZ55a1xM8qKKoKH1ErKVSFBJKt1ATPVamevCX4bqnT4Sn31L9TQW4ZASehyxqfJjcRs7QjeFsfKHqbiKSrXyVLq4Mw6Fp6BWpUzx2f6VBbStLxC6LMxc4RKaCm1GjwWKc8FbyAWTbvEYJ9mWFXm8pz3LsUn3VRSwBgMyDgsCN2Ax2CPbAo", "MultisigxV1D87ikc4UGNs7oVRvnSwLTfdDMPLcFfkufMsBiCm435oE1L9TQW4ZASehyxqfJjcRs7QjeFsfKHqbiKSrXyVLq4Mwc7ZtATM6abPVkRccQ7aZzdjofMbgUur6F5qi1V3xPxkRAya5Te8dVCkPxYxHPzdN4DKLni4e9YVUGegWwZHDGWuMUGJQXG9YUVEZDqMfnLvoaqCTpDQN31rKG7TvqCSVRNKe"],
	"password": "123"
},
"id": 1}
->
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "address": "58F2pcGYn8EVdDBqAt1Xp2EJNj8Qim16qLPdNdLUwTHv3GpDg9PMhGHaYvGvYL5eiYdwdbn5ffdrN96FMmRKiJwdFb5wcDi"
    }
}

wallet 3:
{"jsonrpc": "2.0", 
"method": "finalize_multisig", 
"params": {
	"multisig_info": ["MultisigxV1aFiBjG3Ha9jbbmQ6hXuD2ibi6jUDiBUu8DVMRWHbLTSZ55a1xM8qKKoKH1ErKVSFBJKt1ATPVamevCX4bqnT4Sn31L9TQW4ZASehyxqfJjcRs7QjeFsfKHqbiKSrXyVLq4Mw6Fp6BWpUzx2f6VBbStLxC6LMxc4RKaCm1GjwWKc8FbyAWTbvEYJ9mWFXm8pz3LsUn3VRSwBgMyDgsCN2Ax2CPbAo", "MultisigxV1ZSRa5KBD6y32nTFbKSgxUweX1w7QomiJ2TToarTcFUes55a1xM8qKKoKH1ErKVSFBJKt1ATPVamevCX4bqnT4Sn3c7ZtATM6abPVkRccQ7aZzdjofMbgUur6F5qi1V3xPxkRWS8mxferscZTPUxsQAApQkEtoWnnrqddj3F4sAdKPQxCgVwtP6S4xTh7ajuTkQZrFiC2YgtoqmipxhmFnQYo8H1h"],
	"password": "123"
},
"id": 1}
->
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "address": "58F2pcGYn8EVdDBqAt1Xp2EJNj8Qim16qLPdNdLUwTHv3GpDg9PMhGHaYvGvYL5eiYdwdbn5ffdrN96FMmRKiJwdFb5wcDi"
    }
}
```

**3**. Opened each wallet with `monero-wallet-cli` and checked the address:
```
$ ./monero-wallet-cli --daemon-address=monero-stage.exan.tech:38081 --trusted-daemon --password=123 --stagenet --wallet-file=1
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Beryllium Bullet' (v0.13.0.4-1c4524961)
Logging to ./monero-wallet-cli.log
WARNING: You may not have a high enough lockable memory limit, see ulimit -l
Opened 2/3 multisig wallet: 58F2pcGYn8EVdDBqAt1Xp2EJNj8Qim16qLPdNdLUwTHv3GpDg9PMhGHaYvGvYL5eiYdwdbn5ffdrN96FMmRKiJwdFb5wcDi
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 3                                
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 58F2pc        0.000000000000        0.000000000000       Primary account
----------------------------------------------------------------------------------
          Total        0.000000000000        0.000000000000
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000000000, unlocked balance: 0.000000000000
Background refresh thread started
[wallet 58F2pc]: address
0  58F2pcGYn8EVdDBqAt1Xp2EJNj8Qim16qLPdNdLUwTHv3GpDg9PMhGHaYvGvYL5eiYdwdbn5ffdrN96FMmRKiJwdFb5wcDi  Primary address 
```

```
$ ./monero-wallet-cli --daemon-address=monero-stage.exan.tech:38081 --trusted-daemon --password=123 --stagenet --wallet-file=2
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Beryllium Bullet' (v0.13.0.4-1c4524961)
Logging to ./monero-wallet-cli.log
WARNING: You may not have a high enough lockable memory limit, see ulimit -l
Opened 2/3 multisig wallet: 58F2pcGYn8EVdDBqAt1Xp2EJNj8Qim16qLPdNdLUwTHv3GpDg9PMhGHaYvGvYL5eiYdwdbn5ffdrN96FMmRKiJwdFb5wcDi
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 5                                
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 58F2pc        0.000000000000        0.000000000000       Primary account
----------------------------------------------------------------------------------
          Total        0.000000000000        0.000000000000
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000000000, unlocked balance: 0.000000000000
Background refresh thread started
[wallet 58F2pc]: address
0  58F2pcGYn8EVdDBqAt1Xp2EJNj8Qim16qLPdNdLUwTHv3GpDg9PMhGHaYvGvYL5eiYdwdbn5ffdrN96FMmRKiJwdFb5wcDi  Primary address
```

```
$ ./monero-wallet-cli --daemon-address=monero-stage.exan.tech:38081 --trusted-daemon --password=123 --stagenet --wallet-file=3
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Beryllium Bullet' (v0.13.0.4-1c4524961)
Logging to ./monero-wallet-cli.log
WARNING: You may not have a high enough lockable memory limit, see ulimit -l
Opened 2/3 multisig wallet: 58F2pcGYn8EVdDBqAt1Xp2EJNj8Qim16qLPdNdLUwTHv3GpDg9PMhGHaYvGvYL5eiYdwdbn5ffdrN96FMmRKiJwdFb5wcDi
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 6                                
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 58F2pc        0.000000000000        0.000000000000       Primary account
----------------------------------------------------------------------------------
          Total        0.000000000000        0.000000000000
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000000000, unlocked balance: 0.000000000000
Background refresh thread started
```

It looks like everything works on `master`. 

Please check if you use API the same way

## jacoblyles | 2018-12-21T19:09:16+00:00
I'm on commit ed54ac8fdfe332c4ec6b9fd9331024d862ecad51, which is current HEAD

I compile and run on Mac OS 10.14.2

my command line is:
`monero-wallet-rpc --rpc-bind-port 1100 --wallet-dir data/4999 --detach --disable-rpc-login`

here is my request and response log

```
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "create_wallet",
    "params": {
        "filename": "wallet_0",
        "language": "English",
        "password": ""
    }
}
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {}
}



{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "create_wallet",
    "params": {
        "filename": "wallet_1",
        "language": "English",
        "password": ""
    }
}
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {}
}



{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "create_wallet",
    "params": {
        "filename": "wallet_2",
        "language": "English",
        "password": ""
    }
}
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {}
}


wallet_0:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "prepare_multisig"
}  -->
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "multisig_info": "MultisigV1Yn98ryT9jgsFL3U49UBfZi8Jq9ZGEoFK6CkvmvnvSncu42MVZycBeNniga8VnYKLJVMmKGYvwMShCc5KkbfWc52cTXHdnHD8STw1dgQ9PHnbDCfmcMBDTjC85HwdgTWcQUFiUfd4K6SBwszZxGgb4491yqUvEC2j3oc2D93kNHsnJRVT"
    }
}


wallet 1:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "prepare_multisig"
} -->
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "multisig_info": "MultisigV1c7GHy6jwdVLiWLZnarLyHjfrzKhPpJKc55xh5rshWUxwFQQnddoNHzFWeeNsimv4JLN25KgLERcD9in4mPPwanXS1VPDsxN89r2B7kgpPujQFvCjtaFev1LjT8FBnFR9yFDN5Xbx2PULRssj5ffUiPYKhzUVxKKfYDgdYBjk5453nUSh"
    }
}


wallet 2:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "prepare_multisig"
} -->
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "multisig_info": "MultisigV1eiX8aV1XHHvSnU4PtESmysM9eYZW88FHi7nkz17P9g448KdsQcuT2LPXRe76umZigSZXrtwXyRN41Kj9qF3JyUhSPrXQqncHL4ZHubUJe2H9ChcMWLmVKerLYDuVUnVQfRqg4KUhqCu7u3eLz6i4VsD2JWLSaPbXuxnwRS7imnx6zQc8"
    }
}


wallet 0:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "make_multisig",
    "params": {
        "multisig_info": [
            "MultisigV1c7GHy6jwdVLiWLZnarLyHjfrzKhPpJKc55xh5rshWUxwFQQnddoNHzFWeeNsimv4JLN25KgLERcD9in4mPPwanXS1VPDsxN89r2B7kgpPujQFvCjtaFev1LjT8FBnFR9yFDN5Xbx2PULRssj5ffUiPYKhzUVxKKfYDgdYBjk5453nUSh",
            "MultisigV1eiX8aV1XHHvSnU4PtESmysM9eYZW88FHi7nkz17P9g448KdsQcuT2LPXRe76umZigSZXrtwXyRN41Kj9qF3JyUhSPrXQqncHL4ZHubUJe2H9ChcMWLmVKerLYDuVUnVQfRqg4KUhqCu7u3eLz6i4VsD2JWLSaPbXuxnwRS7imnx6zQc8"
        ],
        "threshold": 2,
        "password": null
    }
} -->
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "address": "41fJjQDhryD1111111111111111111111111111111111218EZ7gutmTJhPHgmvrJZiSquGhHDpMKUsghDqBdfHo8sJEJ7S",
        "multisig_info": "MultisigxV1XHtT7CRfah9Mn18yfm9weQSEQZZjNfFAMatczjAgWn6v2WLKfJ2AdsPCDbeFH8xqpiMALRcZdTdNwa6sM1egDSbPXvgDSygZVAgTqSyhBbVSbUCR5k61UEeBy6kG9Cnt9MTgUBCgWxHd2FEgALb89imwcM5Y2Y4RmB5n9VbWoJ4WZWv9bJgLeZxapctSP1sudwctm69nf5ZcaKrRXMxY9tsMqELZ"
    }
}


wallet 1:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "make_multisig",
    "params": {
        "multisig_info": [
            "MultisigV1Yn98ryT9jgsFL3U49UBfZi8Jq9ZGEoFK6CkvmvnvSncu42MVZycBeNniga8VnYKLJVMmKGYvwMShCc5KkbfWc52cTXHdnHD8STw1dgQ9PHnbDCfmcMBDTjC85HwdgTWcQUFiUfd4K6SBwszZxGgb4491yqUvEC2j3oc2D93kNHsnJRVT",
            "MultisigV1eiX8aV1XHHvSnU4PtESmysM9eYZW88FHi7nkz17P9g448KdsQcuT2LPXRe76umZigSZXrtwXyRN41Kj9qF3JyUhSPrXQqncHL4ZHubUJe2H9ChcMWLmVKerLYDuVUnVQfRqg4KUhqCu7u3eLz6i4VsD2JWLSaPbXuxnwRS7imnx6zQc8"
        ],
        "threshold": 2,
        "password": null
    }
} --> 
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "address": "41fJjQDhryD1111111111111111111111111111111111218EZ7gutmTJhPHgmvrJZiSquGhHDpMKUsghDqBdfHo8sJEJ7S",
        "multisig_info": "MultisigxV1bEggEqJLkgN2YkeEWmSdmYixUwHPmxNUvUD13mhdeLLP2WLKfJ2AdsPCDbeFH8xqpiMALRcZdTdNwa6sM1egDSbPQ7rPnVTeVCTKqHSAPbEiEaHbSvGGX6c7gfG5mAiqX937fcep3kQmrwBavF9R2iEfe4eKmFAmuXG5tTaS9eRygLoYXtQQ6zHcwmgCSWtvT3gcTtQ6vHyUKXtAuUQkZPjZwhKY"
    }
}


wallet 2:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "make_multisig",
    "params": {
        "multisig_info": [
            "MultisigV1Yn98ryT9jgsFL3U49UBfZi8Jq9ZGEoFK6CkvmvnvSncu42MVZycBeNniga8VnYKLJVMmKGYvwMShCc5KkbfWc52cTXHdnHD8STw1dgQ9PHnbDCfmcMBDTjC85HwdgTWcQUFiUfd4K6SBwszZxGgb4491yqUvEC2j3oc2D93kNHsnJRVT",
            "MultisigV1c7GHy6jwdVLiWLZnarLyHjfrzKhPpJKc55xh5rshWUxwFQQnddoNHzFWeeNsimv4JLN25KgLERcD9in4mPPwanXS1VPDsxN89r2B7kgpPujQFvCjtaFev1LjT8FBnFR9yFDN5Xbx2PULRssj5ffUiPYKhzUVxKKfYDgdYBjk5453nUSh"
        ],
        "threshold": 2,
        "password": null
    }
} -->
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "address": "41fJjQDhryD1111111111111111111111111111111111218EZ7gutmTJhPHgmvrJZiSquGhHDpMKUsghDqBdfHo8sJEJ7S",
        "multisig_info": "MultisigxV1ZV2TDDU4sLMWMjvhRk7fXSiJEzdyj6wW1iSt2YidkRM3XvgDSygZVAgTqSyhBbVSbUCR5k61UEeBy6kG9Cnt9MTgQ7rPnVTeVCTKqHSAPbEiEaHbSvGGX6c7gfG5mAiqX937UoeeYc2cXQUYCH5RL5iXnN5CpdHyzaEcwFp5Z5PJ3Pfz5nyVxascF4gG41kHREna7x39RsApSKgj7e5bXPBRw3Jr"
    }
}


wallet 0:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "finalize_multisig",
    "params": {
        "mulitisig_info": [
            "MultisigxV1bEggEqJLkgN2YkeEWmSdmYixUwHPmxNUvUD13mhdeLLP2WLKfJ2AdsPCDbeFH8xqpiMALRcZdTdNwa6sM1egDSbPQ7rPnVTeVCTKqHSAPbEiEaHbSvGGX6c7gfG5mAiqX937fcep3kQmrwBavF9R2iEfe4eKmFAmuXG5tTaS9eRygLoYXtQQ6zHcwmgCSWtvT3gcTtQ6vHyUKXtAuUQkZPjZwhKY",
            "MultisigxV1ZV2TDDU4sLMWMjvhRk7fXSiJEzdyj6wW1iSt2YidkRM3XvgDSygZVAgTqSyhBbVSbUCR5k61UEeBy6kG9Cnt9MTgQ7rPnVTeVCTKqHSAPbEiEaHbSvGGX6c7gfG5mAiqX937UoeeYc2cXQUYCH5RL5iXnN5CpdHyzaEcwFp5Z5PJ3Pfz5nyVxascF4gG41kHREna7x39RsApSKgj7e5bXPBRw3Jr"
        ]
    }
} -->
{
    "error": {
        "code": -33,
        "message": "Needs multisig info from more participants"
    },
    "id": "0",
    "jsonrpc": "2.0"
}


wallet 1:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "finalize_multisig",
    "params": {
        "mulitisig_info": [
            "MultisigxV1XHtT7CRfah9Mn18yfm9weQSEQZZjNfFAMatczjAgWn6v2WLKfJ2AdsPCDbeFH8xqpiMALRcZdTdNwa6sM1egDSbPXvgDSygZVAgTqSyhBbVSbUCR5k61UEeBy6kG9Cnt9MTgUBCgWxHd2FEgALb89imwcM5Y2Y4RmB5n9VbWoJ4WZWv9bJgLeZxapctSP1sudwctm69nf5ZcaKrRXMxY9tsMqELZ",
            "MultisigxV1ZV2TDDU4sLMWMjvhRk7fXSiJEzdyj6wW1iSt2YidkRM3XvgDSygZVAgTqSyhBbVSbUCR5k61UEeBy6kG9Cnt9MTgQ7rPnVTeVCTKqHSAPbEiEaHbSvGGX6c7gfG5mAiqX937UoeeYc2cXQUYCH5RL5iXnN5CpdHyzaEcwFp5Z5PJ3Pfz5nyVxascF4gG41kHREna7x39RsApSKgj7e5bXPBRw3Jr"
        ]
    }
} -->
{
    "error": {
        "code": -33,
        "message": "Needs multisig info from more participants"
    },
    "id": "0",
    "jsonrpc": "2.0"
}


wallet 2:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "finalize_multisig",
    "params": {
        "mulitisig_info": [
            "MultisigxV1XHtT7CRfah9Mn18yfm9weQSEQZZjNfFAMatczjAgWn6v2WLKfJ2AdsPCDbeFH8xqpiMALRcZdTdNwa6sM1egDSbPXvgDSygZVAgTqSyhBbVSbUCR5k61UEeBy6kG9Cnt9MTgUBCgWxHd2FEgALb89imwcM5Y2Y4RmB5n9VbWoJ4WZWv9bJgLeZxapctSP1sudwctm69nf5ZcaKrRXMxY9tsMqELZ",
            "MultisigxV1bEggEqJLkgN2YkeEWmSdmYixUwHPmxNUvUD13mhdeLLP2WLKfJ2AdsPCDbeFH8xqpiMALRcZdTdNwa6sM1egDSbPQ7rPnVTeVCTKqHSAPbEiEaHbSvGGX6c7gfG5mAiqX937fcep3kQmrwBavF9R2iEfe4eKmFAmuXG5tTaS9eRygLoYXtQQ6zHcwmgCSWtvT3gcTtQ6vHyUKXtAuUQkZPjZwhKY"
        ]
    }
}  -->
{
    "error": {
        "code": -33,
        "message": "Needs multisig info from more participants"
    },
    "id": "0",
    "jsonrpc": "2.0"
}


wallet 0:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "is_multisig"
} -->
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "multisig": true,
        "ready": false,
        "threshold": 2,
        "total": 3
    }
}


wallet 1:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "is_multisig"
} -->
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "multisig": true,
        "ready": false,
        "threshold": 2,
        "total": 3
    }
}


wallet 2:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "is_multisig"
} -->
{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "multisig": true,
        "ready": false,
        "threshold": 2,
        "total": 3
    }
}
```





## moneromooo-monero | 2018-12-21T19:59:14+00:00
<pre>
wallet 1:
{
    "jsonrpc": "2.0",
    "id": "0",
    "method": "finalize_multisig",
    "params": {
        "mulitisig_info": [
            "MultisigxV1XHtT7CRfah9Mn18yfm9weQSEQZZjNfFAMatczjAgWn6v2WLKfJ2AdsPCDbeFH8xqpiMALRcZdTdNwa6sM1egDSbPXvgDSygZVAgTqSyhBbVSbUCR5k61UEeBy6kG9Cnt9MTgUBCgWxHd2FEgALb89imwcM5Y2Y4RmB5n9VbWoJ4WZWv9bJgLeZxapctSP1sudwctm69nf5ZcaKrRXMxY9tsMqELZ",
            "MultisigxV1ZV2TDDU4sLMWMjvhRk7fXSiJEzdyj6wW1iSt2YidkRM3XvgDSygZVAgTqSyhBbVSbUCR5k61UEeBy6kG9Cnt9MTgQ7rPnVTeVCTKqHSAPbEiEaHbSvGGX6c7gfG5mAiqX937UoeeYc2cXQUYCH5RL5iXnN5CpdHyzaEcwFp5Z5PJ3Pfz5nyVxascF4gG41kHREna7x39RsApSKgj7e5bXPBRw3Jr"
        ]
    }
} -->
{
    "error": {
        "code": -33,
        "message": "Needs multisig info from more participants"
    },
    "id": "0",
    "jsonrpc": "2.0"
}
</pre>

multisig_info (typo), it's seeing multisig info for no wallets (unless it's a typo just in the transcript).


## jacoblyles | 2018-12-21T22:10:24+00:00
Yep, the problem was on my end. Thanks. 

# Action History
- Created by: jacoblyles | 2018-12-19T19:30:56+00:00
- Closed at: 2018-12-21T22:10:24+00:00
