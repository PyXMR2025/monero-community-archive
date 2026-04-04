---
title: 'transfer failed:"message": "no connection to daemon"'
source_url: https://github.com/monero-project/monero/issues/4255
author: carrie143
assignees: []
labels: []
created_at: '2018-08-14T07:00:48+00:00'
updated_at: '2019-04-14T10:17:17+00:00'
type: issue
status: closed
closed_at: '2019-04-14T10:17:17+00:00'
---

# Original Description
1.I run the"./monerod  --rpc-bind-ip=127.0.0.1 --rpc-bind-port=18081 --detach" to run the daemon
2.I run the "./monero-wallet-rpc --wallet-file test-wallet--password xxxx --rpc-bind-port 18083 --disable-rpc-login" to start the rpc service,
3.then I use the rpc to send monero and get balance of the wallet,the result is follow:
#######
root@iZrj978np1rga9wqa14xcsZ:~# curl -X POST http://127.0.0.1:18083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"**transfer**","params":{"destinations":[{"amount":100000000000,"address":"492xPwbbNuP5JNZK6nsuYDfGFC8BbiCsUbbqHKWb5rsUSp38Ex3hH9JXG3bCEbkkH7eDq1YE3qfdJNaXSrnW8tN5LeZFcsd"}],"mixin":4,"get_tx_key": true}}' -H 'Content-Type: application/json'
{
  "error": {
    "code": -38,
    "message": "**no connection to daemon**"
  },
  "id": "0",
  "jsonrpc": "2.0"
}

root@iZrj978np1rga9wqa14xcsZ:~ curl -X POST http://127.0.0.1:18083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"**getbalance**","paras":{"account_index":0}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "balance": 635758360000,
    "multisig_import_needed": false,
    "per_subaddress": [{
      "address": "46WZeVXxqCjXssS8mKpVm4cvapyR9jT7YG5p9ANUj15bQUcmASSHq2U4uEUcovBCVkD6Bu7Vdshn6ZJDnvSKgszvEus1Wqp",
      "address_index": 0,
      "balance": **635758360000**,
      "label": "Primary account",
      "num_unspent_outputs": 1,
      "unlocked_balance": 635758360000
    }],
    "unlocked_balance": 635758360000
  }
}root@iZrj978np1rga9wqa14xcsZ:~

**what I want to know is that I can get the balance,it proves that wallet service run correctly and connected the daemon,why transfer failed with "no connection to daemon"?**



# Discussion History
## moneromooo-monero | 2018-08-14T07:53:30+00:00
Which version of monero ?

"paras" is a typo, you should be using "params".

getbalance does not need to connect to a daemon.

The daemon might be busy syncing.

4 is too low a mixin, the minimum is currently 6 (except for special cases).

## carrie143 | 2018-08-14T08:07:20+00:00
1.monero version is "Monero 'Lithium Luna' (v0.12.2.0-release)"
2.I try to set "mixin":6,then to transfer,still get the error,and I feel strange that It takes half an hour to return results “no connection to daemon”，why it take so long?

## moneromooo-monero | 2018-08-14T08:08:53+00:00
What is the output of "status" in monerod ?

## carrie143 | 2018-08-14T08:16:28+00:00
![e](https://user-images.githubusercontent.com/24546264/44080023-5af7f15e-9fdd-11e8-8c18-c9fdc80a0d73.png)


## moneromooo-monero | 2018-08-14T12:36:10+00:00
From the machine running the wallet:
telnet 127.0.0.1 18081
Does this connect ?


## carrie143 | 2018-08-15T02:42:50+00:00
connected:
![r](https://user-images.githubusercontent.com/24546264/44128869-e9ba216a-a077-11e8-9d41-3c6b0335e98f.png)


## moneromooo-monero | 2018-08-15T07:02:35+00:00
Probably a timeout then. Try 0.12.3.0, this fixed some timeout issues.

## moneromooo-monero | 2018-09-14T12:04:50+00:00
Current master also has faster RPC used in transfer calls. That should help if it was due to this.


## moneromooo-monero | 2019-04-14T10:13:58+00:00
Most likely fixed. Some RPCs were taking quite some time, causing the wallet to time out.
Please reopen if it still happens.

+resolved


# Action History
- Created by: carrie143 | 2018-08-14T07:00:48+00:00
- Closed at: 2019-04-14T10:17:17+00:00
