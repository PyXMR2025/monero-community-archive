---
title: Different balance between rpc and cli wallet on stagenet
source_url: https://github.com/monero-project/monero/issues/5475
author: Lafudoci
assignees: []
labels:
- invalid
created_at: '2019-04-21T09:25:41+00:00'
updated_at: '2019-04-21T15:41:21+00:00'
type: issue
status: closed
closed_at: '2019-04-21T15:41:21+00:00'
---

# Original Description
Using 0.13 branch `Monero 'Boron Butterfly' (v0.14.0.2-8039b8d9)`

CLI result:
```
Opened wallet: 54met3zKz82aisZhYYwKTPUJvCLfyDFuVRpcoM24DKabY2wfN63x1d5HWqr8QvzeY2a13ScJuVFQsbC5GgRBpTXfEEoPGgv
...
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 129335.775859628002, unlocked balance: 129072.841896183588
```

RPC result:
```
{
    'balance': 59255280680460286,
    'multisig_import_needed': False,
    'per_subaddress': [
    {
        'address': '54met3zKz82aisZhYYwKTPUJvCLfyDFuVRpcoM24DKabY2wfN63x1d5HWqr8QvzeY2a13ScJuVFQsbC5GgRBpTXfEEoPGgv',
        'address_index': 0,
        'balance': 59255280680460286,
        'label': 'Primary account',
        'num_unspent_outputs': 55,
        'unlocked_balance': 59255280680460286
    }],
    'unlocked_balance': 59255280680460286
}
```
When rpc says no unlock balance after spending, I can still spend on cli wallet. To me the cli seems more make sensible, it's stagenet mining wallet so there's lots outputs. But rpc often shows not enough outputs to spend. That's why I found this issue.

# Discussion History
## moneromooo-monero | 2019-04-21T09:34:53+00:00
Are you really sure the RPC wallet is up to date ?

## moneromooo-monero | 2019-04-21T09:35:37+00:00
ie, call the refresh RPC on it to make sure.

## Lafudoci | 2019-04-21T09:47:18+00:00
> ie, call the refresh RPC on it to make sure.
Here is the refresh result:
```
{'id': '0', 'jsonrpc': '2.0', 'result': {'blocks_fetched': 0, 'received_money': False}}
```
And the balance is still the same

## moneromooo-monero | 2019-04-21T09:54:48+00:00
Can you share the wallet keys and cache files ? Like upload to github ?

## Lafudoci | 2019-04-21T10:03:51+00:00
> Can you share the wallet keys and cache files ? Like upload to github ?

I have tried deleting cache file many times, but no effect. I'll provide the rpc and cli files and maybe PM you the password by IRC?

## moneromooo-monero | 2019-04-21T10:07:22+00:00
Can you also send me the RPC request ?

## Lafudoci | 2019-04-21T10:18:33+00:00
> Can you also send me the RPC request ?

https://github.com/Lafudoci/hexo-xmrtw/tree/gh-pages/other/issue5475
Are these what you need?

## moneromooo-monero | 2019-04-21T10:22:41+00:00
I meant the JSON you sent to get the result above.

## moneromooo-monero | 2019-04-21T10:23:42+00:00
Nevermind, looks like it's all there, thanks.

## moneromooo-monero | 2019-04-21T13:00:14+00:00
The wallet you use for RPC is set to refresh-type=no-coinbase, so it's not seeing incoming coinbase.

## Lafudoci | 2019-04-21T13:47:17+00:00
> The wallet you use for RPC is set to refresh-type=no-coinbase, so it's not seeing incoming coinbase.

Oh, I remenber it's for the exchange vulnerability event. So should recover it now? It seems the bug has been patched in 0.14? But I don't know if it's also in the v0.13 branch? Didn't expect this setting has bad effect on rpc.

## moneromooo-monero | 2019-04-21T14:22:10+00:00
It's fixed in 0.14.0.2 and in the 0.13 branch. The fix has the same effects in rpc and non rpc.

## Lafudoci | 2019-04-21T14:30:21+00:00
I simply replace the rpc's key with cli one, re-sync the cache. It seems resolved now. But I don't know if this issue is expected behavior. If it is, this issue could be closed, thank you.
```
{
    'id': '0',
    'jsonrpc': '2.0',
    'result':
    {
        'balance': 129335775859628002,
        'multisig_import_needed': False,
        'per_subaddress': [
        {
            'address': '54met3zKz82aisZhYYwKTPUJvCLfyDFuVRpcoM24DKabY2wfN63x1d5HWqr8QvzeY2a13ScJuVFQsbC5GgRBpTXfEEoPGgv',
            'address_index': 0,
            'balance': 129335775859628002,
            'label': 'Primary account',
            'num_unspent_outputs': 3414,
            'unlocked_balance': 129335775859628002
        }],
        'unlocked_balance': 129335775859628002
    }
}
```


## moneromooo-monero | 2019-04-21T15:38:10+00:00
Well, you told it to ignore coinbase transactions, so it ignored them. It's expected.

+invalid


# Action History
- Created by: Lafudoci | 2019-04-21T09:25:41+00:00
- Closed at: 2019-04-21T15:41:21+00:00
