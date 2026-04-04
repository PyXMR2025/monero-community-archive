---
title: monero wallet rpc shows unlocked balance as 0 and thus does not let to transfer
  monero testnet coins.While monero cli shows and lets transfer monero
source_url: https://github.com/monero-project/monero/issues/4140
author: alishaagupta
assignees: []
labels: []
created_at: '2018-07-16T09:50:44+00:00'
updated_at: '2022-04-08T15:06:10+00:00'
type: issue
status: closed
closed_at: '2022-04-08T15:06:10+00:00'
---

# Original Description
No description

# Discussion History
## moneromooo-monero | 2018-07-16T22:06:16+00:00
Give more information if you expect a fix.

## onemanstartup | 2018-07-24T01:39:11+00:00
I think I have the same problem. 
I'm running 12.3 in docker on stagenet

This is from monero--wallet-cli
```
[wallet 558ku6]: bc_height
125190
[wallet 558ku6]: save_bc
Blockchain saved
[wallet 558ku6]: refresh
Starting refresh...
Refresh done, blocks received: 0
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 906.558650097797, unlocked balance: 705.968161020493
[wallet 558ku6]: account
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 558ku6      906.558650097797      705.968161020493       Primary account
----------------------------------------------------------------------------------
          Total      906.558650097797      705.968161020493
[wallet 558ku6]: address
0  558ku6ge3D4eEbHDtbXRLjAinFvLxSPReGFyEnFVEhKkAUoKB9FxVstgCdiFykGqdTUfYswpxWc6SiTJeX7471iwCD35Zbf  Primary address (used)
```

This is from rpc
```
❯ curl --digest \
-u username:password \
-X post \
-d '{"jsonrpc":"2.0", "id":"10", "method":"getbalance"}' \
 -H 'content-type: application/json' \
http://localhost:8082/json_rpc
{
  "id": "10",
  "jsonrpc": "2.0",
  "result": {
    "balance": 85709893623951,
    "multisig_import_needed": false,
    "per_subaddress": [{
      "address": "558ku6ge3D4eEbHDtbXRLjAinFvLxSPReGFyEnFVEhKkAUoKB9FxVstgCdiFykGqdTUfYswpxWc6SiTJeX7471iwCD35Zbf",
      "address_index": 0,
      "balance": 85709893623951,
      "label": "Primary account",
      "num_unspent_outputs": 3,
      "unlocked_balance": 0
    }],
    "unlocked_balance": 0
  }
}
```

## stoffu | 2018-07-24T05:11:47+00:00
@onemanstartup 
I cannot reproduce the same behavior:
```
Opened wallet: 5A7Gv4ywGavExAC6BVnXCPGR6J3wimLSFbq2wfMLqokK67cx8bhQnJZg27G6yACiFS8rTogBMhx62D3HEDJ2Ka2JEHVW29N
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
Refresh done, blocks received: 0                                
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 5A7Gv4        1.885147890000        1.000000000000       Primary account
----------------------------------------------------------------------------------
          Total        1.885147890000        1.000000000000
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 1.885147890000, unlocked balance: 1.000000000000
Background refresh thread started
[wallet 5A7Gv4]: balance detail
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 1.885147890000, unlocked balance: 1.000000000000
Balance per address:
        Address               Balance      Unlocked balance Outputs                 Label
       0 5A7Gv4        0.885147890000        0.000000000000       0       Primary account
       1 78D8vi        1.000000000000        1.000000000000       1    (Untitled address)
```
RPC `getbalance` response:
```
curl -X POST http://127.0.0.1:38083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getbalance","params":{"account_index":0}}' -H'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "balance": 1885147890000,
    "multisig_import_needed": false,
    "per_subaddress": [{
      "address": "5A7Gv4ywGavExAC6BVnXCPGR6J3wimLSFbq2wfMLqokK67cx8bhQnJZg27G6yACiFS8rTogBMhx62D3HEDJ2Ka2JEHVW29N",
      "address_index": 0,
      "balance": 885147890000,
      "label": "Primary account",
      "num_unspent_outputs": 0,
      "unlocked_balance": 0
    },{
      "address": "78D8vi9AcQxjTNv2xjhzaej39d6XgPc3X7Ggo65nLKUPjouqd6nDcJGCQciUoHsrHRXScqPh5B1wMPZrWTu6afDbDags4Kq",
      "address_index": 1,
      "balance": 1000000000000,
      "label": "(Untitled address)",
      "num_unspent_outputs": 1,
      "unlocked_balance": 1000000000000
    }],
    "unlocked_balance": 1000000000000
  }
}
```
What do you get if you type `balance detail` in the CLI?


## onemanstartup | 2018-07-24T13:53:37+00:00
@stoffu I tried incoming_transfers and there difference too. In rpc it shows only last 3 incoming transfers. I made refresh in wallet-rpc-cli if that information any helpful


balance detail:

```
[wallet 558ku6]: balance detail
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 906.558650097797, unlocked balance: 906.558650097797
Balance per address:
        Address               Balance      Unlocked balance Outputs                 Label
       0 558ku6      905.558650097797      905.558650097797      34       Primary account
      15 77h1FD        1.000000000000        1.000000000000       1
```

```
[wallet 558ku6]: incoming_transfers
               amount   spent    unlocked  ringct    global index                                                               tx id      addr index
      10.000000000000       F    unlocked  RingCT           77124  <c56d5be0bd335a2a087f13c2ec7b6209c5b4569ea5d5bdc69fac3126c03a2d01>               0
      29.826147061324       F    unlocked  RingCT           77161  <f3e069875e865dcd92dc2a6c44c74711213ad1544f8ca892b6309f50a250c87c>               0
      29.826090172463       F    unlocked  RingCT           77162  <35ad6ac958aaeb9dcf654a43c62295c6d039597f0082a4afd9713bdeeb9fdee5>               0
       1.000000000000       F    unlocked  RingCT          112386  <fe42002a556a7f53bf4eced6bc1c627cd0ab77f3d11e76dbc530545bfc244dd6>              15
       1.000000000000       F    unlocked  RingCT          113390  <de98e0f9a4da6113140e2dd16d751769acd37adb6185f8b9c06a3c569b1375e8>               0
      28.789167051209       F    unlocked  RingCT          113885  <179910f18199da51b769093a147552aeba78b84362258264333af6f2aa308379>               0
      28.795863429253       F    unlocked  RingCT          113972  <b1f67e6b4ad88072aab7b1fa63e30f4a20db394416a413c192c9f29b62673d42>               0
      28.580755728233       F    unlocked  RingCT          114059  <060f8feabc8c48b0fe0d92326f3c6bbdd4de7d243a80bd99fe77017a714f9623>               0
      28.580592188149       F    unlocked  RingCT          114118  <826e825cd86f935af7bccface9c397a49d7f3d4b1cddb8665ecf3466c011f3ad>               0
      28.580428649000       F    unlocked  RingCT          114177  <4658e9025d6302acccb67a3b75bee889c52ebfd18757bd222b1d379ea87a0ea2>               0
      28.580265110788       F    unlocked  RingCT          114236  <7f3ed78154560e83280ce0c6e7282feea786ee2b9e41ff89ac620525cde843fb>               0
       1.000000000000       F    unlocked  RingCT          114296  <8f02b2fcb5d9c3e52ae6d0ad085a6c682b1cdd5c322a7da08aa42875a8e06514>               0
      28.579011348912       F    unlocked  RingCT          114765  <a8b6634785e635f87a013722511aa148424ba886dc7bf5e2d9c190ece64f7181>               0
      28.775896355464       F    unlocked  RingCT          115094  <0003c63b7f52b9c8365f0025e84bd8ae9601f120e55fb8327d2a223babb30384>               0
      28.775732830664       F    unlocked  RingCT          115181  <3ad840b0e93fafa46922e49948daea922cdd7be9a5250d1e07eed79b81de59b8>               0
      28.797280021613       F    unlocked  RingCT          115949  <fbc2b2f1cd15c6dbe9f4532999fbf92bdc56b9caa8e700241b2e6b389b973c36>               0
      28.797171010381       F    unlocked  RingCT          116013  <618fd1d41458751a9b7d687953975506d8e90e216aaa5b9f2d14133c9dc57451>               0
      28.797063929566       F    unlocked  RingCT          116077  <69c5c8adc9131da5c3c213a06f1ce096707ceab85976749144baa3a41992f30a>               0
      28.875824819166       F    unlocked  RingCT          116152  <90b2fa2062af138285b01237f75472a929f01034ac8494eac9e569184888bfe5>               0
      28.886536081704       F    unlocked  RingCT          116711  <b42b8c853edb237da788f8280e7aa94cb7528a23d7f988c32d02b7c996fe58bd>               0
      28.883056388011       F    unlocked  RingCT          116754  <82eeeb260a8b6f3f06685e2e88b0cb57e945901779ce0128bc4b5b6231555f3c>               0
      28.872718514423       F    unlocked  RingCT          116797  <54cfe03d2ed850d7535df1dac5ed1af74dc26852beb3993f3c8fc185cde7c69b>               0
      28.880974871144       F    unlocked  RingCT          117485  <e62e637591305cd386de322eeffd53abc14ab729196f5f82d74a20d915116bdf>               0
      28.896489178495       F    unlocked  RingCT          117872  <2084c68c189755245e6438cf397c7fac00e8230e2798518e5818507459c97287>               0
      28.895896724470       F    unlocked  RingCT          118345  <09783d8c005ebd283caff6cbac8c41e31102191b5ef6d5235c77a8a036cf2207>               0
      28.895629866798       F    unlocked  RingCT          118560  <e549ad787bab74260059f4dc16a7cb94dd9286d695b19c8e3b81294d49b8e744>               0
      28.899893841725       F    unlocked  RingCT          118781  <3ce833099aa25d307923458b1bcdf05a67ba31449a1e44502a61c845b237648f>               0
      28.899675847538       F    unlocked  RingCT          118969  <61365568a5911343422c4fa8b49cc56b68bb3bd5abdf91666c225c1e97b097ae>               0
      28.770282984172       F    unlocked  RingCT          119235  <0b50753dd0fd2caa240fc02915263eebe329d1fe3784040a02ddfe6a631cb73a>               0
      28.770064994139       F    unlocked  RingCT          119351  <fa7b3bc9a167b1e0e6775aea35ce8a0ca9538b2f0c91aec94f2e05ce5c5fde67>               0
      28.769465530124       F    unlocked  RingCT          119670  <6cf73e6d36a319994707182a12df7cb5729a0a7429f59829ff4ff2dec900925d>               0
      28.570781944918       F    unlocked  RingCT          119882  <28acc896bdb30bc9038b653aafc92405799724d2bbbe5bb7a44c0923966c0623>               0
      28.570454979826       F    unlocked  RingCT          119888  <d501f9a8d8ce2752e219a30c33d52f7facc91c0906fe53a276e72bf61994a09a>               0
      28.569746568296       F    unlocked  RingCT          119901  <549bafb742f8bbdeed920c8d07c6c83d154e8cc7977f743d66c19f2b27ed6b08>               0
      28.569692075829       F    unlocked  RingCT          119902  <10737875b7b4d49c66c0a42b25813c2efde21f2bb28068f8da529251e2cefde6>               0
[wallet 558ku6]:
```

```
❯ curl --digest \
-X post \
-d '{"jsonrpc":"2.0", "id":"10", "method":"incoming_transfers", "params": {"transfer_type": "all"}}' \
 -H 'content-type: application/json' \
http://localhost:8082/json_rpc
{
  "id": "10",
  "jsonrpc": "2.0",
  "result": {
    "transfers": [{
      "amount": 28570454979826,
      "global_index": 119888,
      "key_image": "",
      "spent": false,
      "subaddr_index": 0,
      "tx_hash": "d501f9a8d8ce2752e219a30c33d52f7facc91c0906fe53a276e72bf61994a09a",
      "tx_size": 84
    },{
      "amount": 28569746568296,
      "global_index": 119901,
      "key_image": "",
      "spent": false,
      "subaddr_index": 0,
      "tx_hash": "549bafb742f8bbdeed920c8d07c6c83d154e8cc7977f743d66c19f2b27ed6b08",
      "tx_size": 84
    },{
      "amount": 28569692075829,
      "global_index": 119902,
      "key_image": "",
      "spent": false,
      "subaddr_index": 0,
      "tx_hash": "10737875b7b4d49c66c0a42b25813c2efde21f2bb28068f8da529251e2cefde6",
      "tx_size": 84
    }]
  }
}
```


## stoffu | 2018-07-31T12:42:38+00:00
Your result is indeed very strange. Please try restoring the same wallet into a different file using the seed and see if the same issue can be observed.

## moneromooo-monero | 2018-07-31T12:52:29+00:00
And keep the current cache file in case it's needed later to debug.

## onemanstartup | 2018-08-01T11:38:51+00:00
I fixed this by deleting db and resync. Not the best way to deal with problem I know, but I don't have enough knowledge about monero yet to dig deeper. thanks.

## stoffu | 2018-08-07T00:48:35+00:00
It seems strange to me that your issue was fixed by deleting the db and resyncing, because the record of incoming transfers on which the RPC `incoming_transfers` is based is stored in the wallet cache, not in the blockchain db.

Or did you mean deleting the wallet cache and rescanning the blockchain? (The blockchain db file is named `~/.bitmonero/lmdb/data.mdb`, while the wallet cache file is named `mywallet` where your wallet keys are stored in `mywallet.keys`.)

## moneromooo-monero | 2018-08-07T18:21:10+00:00
Since you said this is testnet, could you upload the keys file and cache file somewhere ? I can then try it and see what's wrong.

## moneromooo-monero | 2018-08-17T15:07:48+00:00
ping

## moneromooo-monero | 2018-10-26T09:20:45+00:00
ping ? :)

## selsta | 2022-04-08T15:06:10+00:00
No reply, closing.

# Action History
- Created by: alishaagupta | 2018-07-16T09:50:44+00:00
- Closed at: 2022-04-08T15:06:10+00:00
