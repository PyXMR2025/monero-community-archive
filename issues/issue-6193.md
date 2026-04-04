---
title: Where can I find the password for wallets created by generate_from_keys?
source_url: https://github.com/monero-project/monero/issues/6193
author: normoes
assignees: []
labels: []
created_at: '2019-11-28T12:36:09+00:00'
updated_at: '2019-11-29T07:23:34+00:00'
type: issue
status: closed
closed_at: '2019-11-29T07:23:34+00:00'
---

# Original Description
I start the Monero RPC basically like this:
```
monero-wallet-rpc --stagenet --disable-rpc-login --wallet-dir /monero/wallets
```

I create a watch-only wallet like this:
```
curl -i -X POST http://localhost:38083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"generate_from_keys", "params":{"viewkey":"c007....", "address":"57P8...", "filename": "wallet", "password": "empty"}}'
```

I tried it with and without `, "password": "empty"`.

That call returns a valid response in both cases:
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "address": "57P8...",
    "info": "Watch-only wallet has been generated successfully."
  }
}
```

The problem is, I cannot use the wallets created that way, since I don't know the password.
Using the CLI or the RPC just returns:
> Error: failed to load wallet: invalid password

# Discussion History
## normoes | 2019-11-28T12:37:40+00:00
You can find the related code [here](https://github.com/monero-project/monero/blob/master/src/wallet/wallet_rpc_server.cpp#L3436).

## normoes | 2019-11-28T12:40:21+00:00
Also this method seems quite buggy to me.

I experience this issue https://github.com/monero-project/monero/issues/5852.

Also the Monero RPC just stops responding when generating a wallet using the same file name.



## moneromooo-monero | 2019-11-28T13:21:55+00:00
I'm not sure what you're saying between:
- I forgot the passord
- I know the password, but it does not work when reopening the wallet

If the former: you're suppose to keep the password if you want to reuse it. The wallet doesn't keep it in some alternate place, it'd defeat the purpose.
If the latter: are you using non 7 bit ASCII characters in the password ?

I'll check the filename reuse hang.


## normoes | 2019-11-28T13:25:02+00:00
I tried both ways, with and without password using `generate_from_keys`.
The password I explicitly specified is the string `empty` in the second example.

I expected:
 * To not need a password in case I don't set one.
 * or to use `empty` as password, if set.

Neither works. I did not forget the password.


## moneromooo-monero | 2019-11-28T13:35:44+00:00
I generated a testnet wallet from my main test wallet using the generate_from_keys RPC, using a simple 7 bit ASCII password. Worked.
I close it, and tried to open it with monero-wallet-cli. Worked.
I exited monero-wallet-cli, and tried to generate it again, with the same parameters. Errored with:
AssertionError: {u'jsonrpc': u'2.0', u'id': u'0', u'error': {u'message': u'Wallet already exists.', u'code': -1}}

So it looks like you're doing odd things.
Note that monero-wallet-rpc might have been busy scanning your wallet for a while, that could cause a hang till it's done if it's got a lot to refresh.

Double check passwords.

## normoes | 2019-11-28T13:36:54+00:00
Ok,I'll check again. Thanks for testing.

## moneromooo-monero | 2019-11-28T13:57:21+00:00
I noticed you were using a view only wallet. I had tried a full wallet. I just tried a view only one and it also worked.

## normoes | 2019-11-28T14:18:50+00:00
OK.
I created the wallet:
```
curl -i -X POST http://localhost:38083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"generate_from_keys", "params":{"viewkey":"c007...", "address":"57P...", "filename": "test1", "password": "p"}}'
```

Doing it again now returns the proper message `Wallet already exists.`.

And then tried to open the wallet:
```
curl -i -X POST http://localhost:38083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"open_wallet", "params": {"filename": "test1", "password":"p"}}'
```

with the following result:
```
{
  "error": {
    "code": -1,
    "message": "Failed to open wallet"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```

and the Monero RPC:
```
2019-11-28 14:12:40.090	I Generating SSL certificate
2019-11-28 14:12:40.670	I Generating SSL certificate
2019-11-28 14:12:41.593	E !r. THROW EXCEPTION: error::invalid_password
```

---


Is this the right way to pass a password (`"password": "p"`)?
Not passing a password like done above also returns `invalid password` when trying to open the wallet with an empty password.

## normoes | 2019-11-28T14:40:50+00:00
I can successfully open already existing wallets using `open_wallet` .

## moneromooo-monero | 2019-11-28T14:57:16+00:00
Yes.

## moneromooo-monero | 2019-11-28T14:57:48+00:00
I tried your command above, with changed viewkey and address and port, and it works.

## moneromooo-monero | 2019-11-28T15:09:01+00:00
Upload a monero-wallet-rpc level 2 log I guess. Might show something interesting.

## normoes | 2019-11-28T15:14:16+00:00
Here you can find a `level=4` log.
1) I created the wallet using `generate_from_keys`
2) I tried to open it.

https://bin.privacytools.io/?fd9303ed1411fa82#Vyw8mU6FKpx/YT59oobTYfWsteJct0g/1cKXMZOh5rw=

Edit:

Please ignore the daemon settings, they default to testnet values, but the daemon is not used at this point.

## moneromooo-monero | 2019-11-28T15:15:55+00:00
This wants javascript.

## normoes | 2019-11-28T15:17:08+00:00
Sorry:
https://paste.debian.net/1118396/

## moneromooo-monero | 2019-11-28T15:30:02+00:00
Try with this: https://paste.debian.net/hidden/6f0bf05f/

## normoes | 2019-11-28T17:50:45+00:00
I tried it again: https://paste.debian.net/hidden/fcba442c/
Same procedure:
1) `generate_from_keys`
2) `open_wallet`

And I definitely use the same password.

## normoes | 2019-11-28T17:59:33+00:00
You know what..
I tried to generate the wallet with the **public** viewkey. This results in the above situation.

I just now tried it with the **secret** viewkey, that worked.

I guess, I am missing some basic knowledge about cryptography?

## dEBRUYNE-1 | 2019-11-28T18:22:16+00:00
View-only wallet requires the private view key in order to be able to look for transactions belonging to your wallet. Put differently, it is required to decrypt the shared secret. 

## moneromooo-monero | 2019-11-28T18:29:20+00:00
Better error for this case:

https://github.com/monero-project/monero/pull/6194

## normoes | 2019-11-29T07:23:31+00:00
Well, thanks a lot for the explanation and the help.

# Action History
- Created by: normoes | 2019-11-28T12:36:09+00:00
- Closed at: 2019-11-29T07:23:34+00:00
