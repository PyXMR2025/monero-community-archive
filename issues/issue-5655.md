---
title: Segfault when saying "No" to restoring from current estimated block height
  (possibly Trezor-related)
source_url: https://github.com/monero-project/monero/issues/5655
author: fullmetalScience
assignees: []
labels: []
created_at: '2019-06-16T17:27:11+00:00'
updated_at: '2021-07-21T23:34:59+00:00'
type: issue
status: closed
closed_at: '2021-07-21T23:34:59+00:00'
---

# Original Description
    Is this okay? (Y/Yes/N/No): N
    [1] 28951 segmentation fault (core dumped) monero-wallet-cli --log-file=`mktemp` --trusted-daemon --hw-device=Trezor

Stacktrace: [gdb_when_saying_No.txt](https://github.com/monero-project/monero/files/3294371/gdb_when_saying_No.txt)

# Discussion History
## fullmetalScience | 2019-06-16T21:53:33+00:00

[gdb_when_saying_No_2.txt](https://github.com/monero-project/monero/files/3294674/gdb_when_saying_No_2.txt)

Here's the backtrace from **after** applying [your patch](https://paste.debian.net/hidden/2a92b7c2/).

## moneromooo-monero | 2019-06-17T11:21:22+00:00
What does it log though ? :)

## ph4r05 | 2019-06-17T11:28:14+00:00
Thanks for the report. The bug may manifest itself when using Trezor but from the log it seems the crash is triggered by `http_simple_client_template` by some response returned by the Trezor bridge. The bug may be in the http client code handling http responses.

## moneromooo-monero | 2021-07-21T23:34:54+00:00
Same as https://github.com/monero-project/monero/issues/7784

# Action History
- Created by: fullmetalScience | 2019-06-16T17:27:11+00:00
- Closed at: 2021-07-21T23:34:59+00:00
