---
title: tests fail on arch with fresh clone
source_url: https://github.com/monero-project/monero/issues/1702
author: Silur
assignees: []
labels:
- invalid
created_at: '2017-02-09T16:31:45+00:00'
updated_at: '2017-08-08T21:59:59+00:00'
type: issue
status: closed
closed_at: '2017-08-08T11:54:16+00:00'
---

# Original Description
```
>make
.....
[  PASSED  ] 674 tests.
[  FAILED  ] 4 tests, listed below:
[  FAILED  ] Serialization.portability_wallet
[  FAILED  ] Serialization.portability_outputs
[  FAILED  ] Serialization.portability_unsigned_tx
[  FAILED  ] Serialization.portability_signed_tx

Linux 4.9.7-1-ARCH #1 SMP PREEMPT Wed Feb 1 19:33:40 CET 2017 x86_64 GNU/Linux
```



# Discussion History
## moneromooo-monero | 2017-02-09T17:06:58+00:00
Look up a bit, there will be the actual lines where a check fails for these. Please post those.

## Silur | 2017-02-10T12:17:11+00:00
`2017-02-10 13:13:46.307 [SRV_MAIN]      ERROR   cn      src/cryptonote_core/cryptonote_basic_impl.cpp:105       Block cumulative size is too big: 40001, expected less than 40000`
`2017-02-10 13:13:46.307 [SRV_MAIN]      ERROR   cn      src/cryptonote_core/cryptonote_basic_impl.cpp:105       Block cumulative size is too big: 280001, expected less than 280000`
this error causes each fail, with different numbers

## moneromooo-monero | 2017-02-10T14:16:44+00:00
These may be normal. I'm talking about assertion failures in the tests you mentioned.


## moneromooo-monero | 2017-02-20T09:23:14+00:00
For the record, another arch user reports those tests passed.

## Silur | 2017-02-20T13:20:25+00:00
checking it again

## jtorbicki | 2017-04-01T10:13:32+00:00
I have the same problem. All 4 failed assertions are caused by similar issue. For instance the first one:
Serialization.cpp:684: Failure
Value of: r
  Actual: false
Expected: true
This is caused because this file is NOT found: 
string wallet_file = epee::string_tools::get_current_module_folder() + "/../../../../tests/data/wallet_9svHk1";

There is also a warning in the output: file not found "tests/unit_tests/../../../../tests/data/wallet_9svHk1.keys" 

It might mean that the result of this function call: epee::string_tools::get_current_module_folder() does not get very well with so many ../../../../ :)

## moneromooo-monero | 2017-04-01T14:28:07+00:00
When this happens, what is:
- the command line used
- the directory you are running it from


## jtorbicki | 2017-04-01T14:58:36+00:00
@moneromooo-monero after your comment I did some digging and I guess the problem is with the AUR package which is arch specific. I suspect this line to be causing troubles (66): https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=bitmonero-git#n66
Probably tests should be executed from different location?

## danrmiller | 2017-04-02T09:45:31+00:00
@jtorbicki Have you generated the test wallets and followed the configuration according to this document:

https://github.com/monero-project/monero/blob/master/tests/libwallet_api_tests/scripts/README.md

## moneromooo-monero | 2017-04-02T11:44:54+00:00
From that file, the problem seems to be that the build tree root is build, rather than build/release. So there's one less directory to back up to find the data files.

## moneromooo-monero | 2017-04-02T11:46:28+00:00
I did not know about that README. Those things should really be done automatically by the tests.

## danrmiller | 2017-04-02T11:59:12+00:00
Sorry, it seems I didn't look closely enough and that configuration doesn't apply to the unit tests mentioned in this issue. But I agree that libwallet tests configuration could be done automatically by the build.

## moneromooo-monero | 2017-08-08T11:45:25+00:00
This is a problem with the AUR script itself. The author will fix it when trying the tests. Please report it there.

+invalid
+resolved

## anonimal | 2017-08-08T21:59:59+00:00
@jakoblind why are you using that package? It's barely maintained and the maintainer refuses to remove it. Try https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=monero.

JFTR, as noted in the package:
```
# NOTE:
#   Our latest issue appears makepkg related:
#     "file not found "tests/unit_tests/../../../../tests/data/wallet_9svHk1.keys"
#   As noted in #monero-dev:
#     2017-02-24 anonimal        Not to defend Arch or this strange makepkg issue, but for a unit-test like that, IMHO I think the stream should be decoupled from file handling so that the unit-test can process the stream directly. Then, wallet*.keys can be put into hex form within the unit file.
```

# Action History
- Created by: Silur | 2017-02-09T16:31:45+00:00
- Closed at: 2017-08-08T11:54:16+00:00
