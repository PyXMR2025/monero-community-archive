---
title: How to actually sweep_all?
source_url: https://github.com/monero-project/monero/issues/6237
author: ghost
assignees: []
labels: []
created_at: '2019-12-14T20:36:32+00:00'
updated_at: '2020-05-17T14:40:13+00:00'
type: issue
status: closed
closed_at: '2020-05-17T14:40:13+00:00'
---

# Original Description
Sounds like I have to do sweep_all (every single index I have). Is there a way to do all used indexes? I'd like a literal sweep_all command that sweeps the entire wallet.

# Discussion History
## moneromooo-monero | 2019-12-14T20:59:03+00:00
Sweep the entire wallet would link your different accounts, which would defeat the purpose of accounts, at least the privacy purpose. So no. For subaddresses, it should sweep all of them, so if it doesn't it looks like a bug in practice. Can you confirm whether you're asking about accounts or subaddresses within an account ?


## ghost | 2019-12-14T21:25:56+00:00
Thanks for getting back to me. I think it's just subaddresses, but maybe I'm mistaken.

This is what I'm doing for payments.

https://github.com/teran-mckinney/bitcoinacceptor-python/blob/master/bitcoinacceptor/__init__.py#L110

## moneromooo-monero | 2019-12-14T21:52:03+00:00
That line points at something that's unrelated AFAICT.

For your comments on the linked function, 64 bits is *way* too much indeed. 80 bytes per subaddress in RAM. The 200 is a default, and many people don't seem to get that it grows automatically as addresses are used.

## ghost | 2019-12-14T23:16:25+00:00
I don't think it's unrelated. I'm showing that it's using subaddresses and the same account index of 0.

https://monero-python.readthedocs.io/en/latest/wallet.html#monero.wallet.Wallet.get_address

I ended up using 200 as that was the default.

Either way, do you know there a way to sweep all of the subaddresses under the same account? Or is this not working how I think it is?

I appreciate your help, thank you.

## moneromooo-monero | 2019-12-15T00:25:08+00:00
Ah. Then it should sweep all I think. Are you using a simple "sweep_all ADDRESSHERE" command in monero-wallet-cli while account 0 is selected ? If not, give exact details.

## ghost | 2019-12-15T03:49:33+00:00
No, it just picks one of the subaccounts. And show_transfers has different account IDs.

Wonder if there's a bug in the code and it's giving different accounts and not different subaddresses?

## stoffu | 2019-12-16T04:22:50+00:00
@teran-mckinney 
> No, it just picks one of the subaccounts. And show_transfers has different account IDs.

That behavior is intentional; it's best privacy-wise to not spend outputs received by different subaddresses together, so the wallet randomly picks one index when sweeping all with the `subaddr_indices` field left unspecified:

https://github.com/monero-project/monero/blob/b4e1dc83d275f8ee9a8c12615cf952f05161c7a3/src/wallet/wallet2.cpp#L10038

#6241 adds an option to enable sweeping outputs received by all subaddresses within the same account for the wallet CLI and RPC.


## ghost | 2019-12-16T04:46:29+00:00
Thank you! I appreciate you writing a patch for this. Just confused by the name `sweep_all`.

Sounds like your patch will do the trick. I hope it makes it in.

## moneromooo-monero | 2019-12-16T12:16:40+00:00
I see now I had misread the code, sorry :)

## moneromooo-monero | 2020-05-17T14:40:13+00:00
That patch is now in master, closing.

# Action History
- Created by: ghost | 2019-12-14T20:36:32+00:00
- Closed at: 2020-05-17T14:40:13+00:00
