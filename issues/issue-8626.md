---
title: Poor DX with `export_outputs` with `import_outputs` methods
source_url: https://github.com/monero-project/monero/issues/8626
author: evercraze
assignees: []
labels: []
created_at: '2022-10-25T09:06:19+00:00'
updated_at: '2022-11-03T23:28:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
For offline signing, I am using `export_outputs` on a hot wallet and saturating a cold wallet by calling `import_outputs`.
The catch is that the wallet total output count is massive, and in an attempt to make it robust, I do chunking with undocumented parameters in `export_outputs` (start, count). 

However, I observe poor DX in the method combination.

The `export_outputs` [method](https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#export_outputs) returns hexed blob data where the structure is `offset + total output count + outputs` (output count corresponds to the count param), see [wallet2.cpp#L13296](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L13296).

In turn, calling the `import_outputs` [method](https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#import_outputs), the response is numeric `num_imported`.
My own expectations are that `num_imported` is the imported output count - the amount that came from `export_outputs` count or less when it's the last run, BUT in reality the `num_imported` value is equal to the `total output count` from the `export_outputs` response. And it's done intentionally in [wallet2.cpp#L13397](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L13397) by returning the wallet total output count that was resized during the import on [wallet2.cpp#L13327](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L13327) and [wallet2.cpp#L13342](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L13342).

I would expect that the `num_imported` response could be used to verify the import command worked as expected, and it should always be less than or equal to the count or throw an error. In short, close experience to the SQL offset & limit concept.

Pseudocode 
```
start = 0 
count = 100
while (num_imported > count) {
   outputs = export_outputs(all = true, start, count)
   num_imported = import_outputs(outputs)
   start += num_imported
}
```

# Discussion History
## plowsof | 2022-10-30T13:43:01+00:00
Im currently tinkering with this myself, please see the functional tests in the commit these params where added  https://github.com/monero-project/monero/commit/0cbf5571d3ccd07c81d33b05dd23b2ac9c777c3b

## evercraze | 2022-11-02T07:31:09+00:00
I would say the biggest issue is that there is no way to find out the total output count and iterate over known number of outputs. Judging by the functional test, there is a loop with known a output count https://github.com/monero-project/monero/commit/0cbf5571d3ccd07c81d33b05dd23b2ac9c777c3b#diff-94a7c03c6f20df0978f9f76505f75d4115fccfc83875ad2b88f4d5280226fbebR104  
Such knowledge can't be obtained using only RPC calls. However, maybe I am missing some specific RPC method.
In the case if some method with total output count do exist then I can overcome the issue described in https://github.com/monero-project/monero/issues/8625 too.

## plowsof | 2022-11-03T00:38:56+00:00
would it be get_transfers ( in + out ) as the total number of outputs? *Ignore, i am not sure, this would need to be used in combination with get_transfer_by_txid too hm

## plowsof | 2022-11-03T23:28:50+00:00
I used the error to 'find the number of outputs' chunk forward until error, step back, then creep forward by 1 until you reach the 'real' end.
Hopefully someone can tell us the 'real' answer :( 
https://gist.github.com/plowsof/bf2bf82d40a275cf0b6bb22a0a5da8ba

# Action History
- Created by: evercraze | 2022-10-25T09:06:19+00:00
