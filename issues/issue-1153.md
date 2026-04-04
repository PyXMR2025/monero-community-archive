---
title: --rpc-bind-port fails when using --generate-new-wallet
source_url: https://github.com/monero-project/monero/issues/1153
author: athanclark
assignees: []
labels: []
created_at: '2016-09-30T23:36:48+00:00'
updated_at: '2017-08-12T20:18:12+00:00'
type: issue
status: closed
closed_at: '2017-08-12T20:18:12+00:00'
---

# Original Description
The `--rpc-bind-ip` argument works fine though. You can reproduce the error on v0.10 with the following:

``` bash
monero-wallet-cli \
  --generate-new-wallet="foo" \
  --rpc-bind-port="18082"
```

and get the following error:

```
Creating the logger system
Monero 'Wolfram Warptangent' (v0.10.0.0-release)
Logging at log level 0 to /home/athan/dev/moneybit/hmonero/monero-wallet-cli.log
2016-Sep-30 16:35:37.040799 Error: Wallet password not set.
Error: Wallet password not set.
```

Likewise, you can run this:

``` bash
monero-wallet-cli \
  --generate-new-wallet="foo" \
  --rpc-bind-port="18082" \
  --password="asdf"
```

to get (approximately) this error:

```
Creating the logger system
Monero 'Wolfram Warptangent' (v0.10.0.0-release)
Logging at log level 0 to /home/athan/dev/moneybit/hmonero/monero-wallet-cli.log
2016-Sep-30 16:36:37.293480 Loading wallet...
2016-Sep-30 16:36:37.293557 ERROR /home/athan/dev/monero/src/wallet/wallet2.cpp:1850 e || !exists. THROW EXCEPTION: error::file_not_found
2016-Sep-30 16:36:37.293649 /home/athan/dev/monero/src/wallet/wallet2.cpp:1850:N5tools5error15file_error_baseILi1EEE: file not found ".keys"
2016-Sep-30 16:36:37.293728 Exception: tools::error::file_error_base<1>
2016-Sep-30 16:36:37.293776 Unwinded call stack:
2016-Sep-30 16:36:37.294522      1                  0x726a00 __cxa_throw + 0x70
2016-Sep-30 16:36:37.295095      2                  0x75fd9a void tools::error::throw_wallet_ex<tools::error::file_error_base<1>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1306] + 0x25a
2016-Sep-30 16:36:37.295590      3                  0x533d6d tools::wallet2::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0xddd
2016-Sep-30 16:36:37.296170      4                  0x4968f5 main + 0x1bc5
2016-Sep-30 16:36:37.296781      5                  0x7f0498b35830 __libc_start_main + 0xf0
2016-Sep-30 16:36:37.297329      6                  0x4a8859 _start + 0x29
2016-Sep-30 16:36:37.297945      7                  0x0
2016-Sep-30 16:36:37.298234 ERROR /home/athan/dev/monero/src/simplewallet/simplewallet.cpp:3901 Wallet initialization failed: file not found ".keys"
```


# Discussion History
## moneromooo-monero | 2016-10-01T09:14:29+00:00
I'm not sure what's the best way to do it here. Create with an empty password ?


## moneromooo-monero | 2016-10-01T16:15:30+00:00
To be clear: --rpc-bind-port is "go to RPC mode", so we can't actually prompt for stuff when this is used. We might not even have a console.


## athanclark | 2016-10-01T22:06:16+00:00
You don't think it would be possible / intended? When running `monero-wallet-cli --wallet-file=foo --log-file=foo.log --rpc-bind-port=...`, the stdout doesn't detach, and differs from the log file.


## moneromooo-monero | 2016-10-02T09:43:41+00:00
There is no stdin parsing in RPC mode.
I think if you want to create a wallet, supply --password (or --password-file). Creating a passwordless wallet if there is no password sounds like too easy to make a plaintext wallet without meaning to.


## athanclark | 2016-10-03T02:44:08+00:00
But even if there is a password supplied, there's a really nasty error (the second one) - that's what I'm drawing attention to. But I think I understand - if enough arguments are supplied (disregarding the language field for the mnemonic), then there isn't a need to parse stdin


## moneromooo-monero | 2016-10-15T15:52:28+00:00
You're right, I'd focused on the first part, but the second part is different. The RPC mode ignores the generate-new-wallet argument. That'll have to be fixed.


## moneromooo-monero | 2017-08-12T20:07:55+00:00
monero-wallet-cli and monero-wallet-rpc are now two separate binaries. monero-wallet-cli does not know about --rpc-bind-port, while monero-wallet-rpc does not know about --generate-new-wallet. So that fixes this bug as a side effect.

+resolved

# Action History
- Created by: athanclark | 2016-09-30T23:36:48+00:00
- Closed at: 2017-08-12T20:18:12+00:00
