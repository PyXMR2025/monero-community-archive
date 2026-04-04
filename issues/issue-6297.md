---
title: monero-wallet-rpc lost transaction
source_url: https://github.com/monero-project/monero/issues/6297
author: xinyijun
assignees: []
labels: []
created_at: '2020-01-17T10:30:14+00:00'
updated_at: '2022-02-19T04:42:17+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:42:17+00:00'
---

# Original Description
We have a wallet with dozens of thousands addresses, recently one user report that his deposit is not recorded. After some investigation, we found we lost the transaction, please help to investigate it. Thanks.

1. Related transaction:
transaction hash: **fd3c1ed7cf69a085c1c3309a63143ef577a4aa6684d80ab0b7f5b9b9342cb8b9**
to address: **8BSmATdC5om2BwxNFBoXkUa2hN8SYKoWmDw5BBJpNEakica1nh2RHVtSBR2NZpccocVCooNmrRho21quPbzaReRHDsz8q1H**
transaction key: **64ad5215d1e849aa3429da7f315052ce9a196da5491257ecbf0b652ce2b3e401**
block height: **2011462**

2. when we tried to get transfers by post following data to the wallet, we got empty response:
`{
  "jsonrpc":"2.0",
  "id":"0",
  "method":"get_transfers",
  "params":{
    "in": true,
    "out": true,
    "pending": true,
    "pool": true,
    "failed": true,
    "filter_by_height":true,
    "min_height": 2011461,
    "max_height":2011463
  }
}`

3. when we post the following data to **another wallet** to verify the transaction reported by the user:
`{
	"jsonrpc":"2.0",
	"id":"0",
	"method":"check_tx_key",
	"params":
	{
		"txid":"fd3c1ed7cf69a085c1c3309a63143ef577a4aa6684d80ab0b7f5b9b9342cb8b9",
		"tx_key":"64ad5215d1e849aa3429da7f315052ce9a196da5491257ecbf0b652ce2b3e401",
		"address":"8BSmATdC5om2BwxNFBoXkUa2hN8SYKoWmDw5BBJpNEakica1nh2RHVtSBR2NZpccocVCooNmrRho21quPbzaReRHDsz8q1H"
	}
}`
we got response:
`{
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "confirmations": 1607,
        "in_pool": false,
        "received": 200000000000
    }
}`

4. I'm sure the address **8BSmATdC5om2BwxNFBoXkUa2hN8SYKoWmDw5BBJpNEakica1nh2RHVtSBR2NZpccocVCooNmrRho21quPbzaReRHDsz8q1H** belongs to the wallet

5. _./monero-wallet-rpc --version_
Monero 'Carbon Chamaeleon' (v0.15.0.1-release)



# Discussion History
## xinyijun | 2020-01-17T10:45:48+00:00
In addition, we never recover the wallet after creation.

## moneromooo-monero | 2020-01-17T14:56:13+00:00
Do you generate the subaddresses in that wallet ? Or another instance (ie, hot wallet) ?

## xinyijun | 2020-01-20T02:02:48+00:00
> Do you generate the subaddresses in that wallet ? Or another instance (ie, hot wallet) ?

Yes, we generate a lot of subaddresses in that wallet by post data `{"jsonrpc":"2.0","id":"0","method":"create_address","params":{"account_index":0}}`,  only one wallet contain the address(we never recover wallet).

## moneromooo-monero | 2020-01-20T13:00:45+00:00
Did the wallet crash at some point, or did you kill it without saving, resulting in it having to rescan part of the chain on reload ? 
If this is the case and there's a long set of addresses without deposit, it could be it's that the wallet did not search for long enough. This case would be fixed by using a larger subaddress lookahead (see "set" in monero-wallet-cli) and using rescan_bc.


## xinyijun | 2020-01-21T03:52:53+00:00
Thanks. The wallet never crash(we have monitor and would be alerted if crash), after creating of subaddresses, we don't kill it. The address_index of the subaddress(of which deposit lost at height 2011462) is 1041, but another subaddress(address_index 1038) has already received deposit at height 2011436.

## moneromooo-monero | 2020-01-21T12:57:18+00:00
Did you receive a deposit on a subaddress with a higher address_index than 1041 ?

## moneromooo-monero | 2020-01-21T13:53:17+00:00
Also, run monero-wallet-cli on that wallet (you will need to either stop monero-wallet-rpc temporarily or make a copy of the wallet files first), and run:

set

Then make a note of the value of the "subaddress-lookahead" setting and post it.

Then:

account switch N     (replace N with the account which has the address to which the tx is missing)

Then:

address all

Then note whether the list includes the address in question (ie the subaddress_index is in the list and corresponds to the expected address).

## xinyijun | 2020-01-22T12:48:08+00:00
Ok, but I can't check the value until Feb. 3rd because it's Chinese Spring Festival now. I'm sure the wallet includes the address in question, I made a testing deposit to the address after and the wallet did receive the deposit. Thanks.

## xinyijun | 2020-01-22T14:05:07+00:00
> Did you receive a deposit on a subaddress with a higher address_index than 1041 ?

Yes, the highest address_index is 3998 currently, before height 2011462, the highest address_index is 2373.

## moneromooo-monero | 2020-01-22T14:38:12+00:00
OK. Did I understand right that:

Customer made a deposit to subaddress S, the wallet did not see it.
You then made a deposit to the same subaddress S, and the wallet saw it ?

If I understood right, then you do not need to do the checks I asked for above.

## xinyijun | 2020-01-23T08:40:11+00:00
> OK. Did I understand right that:
> 
> Customer made a deposit to subaddress S, the wallet did not see it.
> You then made a deposit to the same subaddress S, and the wallet saw it ?
> 
> If I understood right, then you do not need to do the checks I asked for above.

Yes, your understood is right.

## moneromooo-monero | 2020-01-23T12:40:45+00:00
In the wallet logs, do you have a line saying:
Height 2011462, txid \<fd3c1ed7cf69a085c1c3309a63143ef577a4aa6684d80ab0b7f5b9b9342cb8b9\>, 0.200000000000, idx 0/1041
(might be a bit different, but for that height and txid).

## xinyijun | 2020-01-26T09:53:51+00:00
> In the wallet logs, do you have a line saying:
> Height 2011462, txid <fd3c1ed7cf69a085c1c3309a63143ef577a4aa6684d80ab0b7f5b9b9342cb8b9>, 0.200000000000, idx 0/1041
> (might be a bit different, but for that height and txid).

Thanks, I'll check it when I'm back to work.

## xinyijun | 2020-04-21T10:01:22+00:00
I checked the log and only found this:
_grep fd3c1ed7cf69a085c1c3309a63143ef577a4aa6684d80ab0b7f5b9b9342cb8b9 \*.log\*_
rpc.log-2020-01-17-02-47-29:2020-01-15 01:58:31.181	[RPC0]	INFO	wallet.wallet2	src/wallet/wallet2.cpp:2948	Found new pool tx: \<fd3c1ed7cf69a085c1c3309a63143ef577a4aa6684d80ab0b7f5b9b9342cb8b9\>

Please help to investigate it, thanks.

## moneromooo-monero | 2020-04-24T17:41:51+00:00
What are the dozen lines of the log after the line you posted ?

## xinyijun | 2020-04-30T07:20:07+00:00
_grep -B 30 -A 30 fd3c1ed7cf69a085c1c3309a63143ef577a4aa6684d80ab0b7f5b9b9342cb8b9 *.log* > transaction_lost_log.txt_
please see the attachment for the output.
[transaction_lost_log.txt](https://github.com/monero-project/monero/files/4556702/transaction_lost_log.txt)


## moneromooo-monero | 2020-05-01T21:20:49+00:00
No errors or interesting traces, so it's hard to know what went wrong unfortunately.
If you restore from seed (on a temporary file), do you see that transaction being processed normally ?

## xinyijun | 2020-05-13T06:38:28+00:00
Thanks, I will try to do this, but I don't know whether risk control department allows to do this.

## selsta | 2022-02-19T04:42:17+00:00
Resolved, see #7531

# Action History
- Created by: xinyijun | 2020-01-17T10:30:14+00:00
- Closed at: 2022-02-19T04:42:17+00:00
