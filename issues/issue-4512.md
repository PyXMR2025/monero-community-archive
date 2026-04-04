---
title: '[v13] Ledger transfer doesn’t work sometimes (libhidapi)'
source_url: https://github.com/monero-project/monero/issues/4512
author: selsta
assignees: []
labels: []
created_at: '2018-10-07T18:05:52+00:00'
updated_at: '2018-10-21T23:49:07+00:00'
type: issue
status: closed
closed_at: '2018-10-20T19:16:56+00:00'
---

# Original Description
Since Ledger switched to libhidapi, sending on macOS fails sometimes.

There are two ways to reproduce the following error message.

`Error: unexpected error: Wrong Channel`

1. Waiting at the accept fee screen on the Ledger for ~10 seconds.
2. Accepting the fee without waiting, this will sometimes result in the above error and sometimes result in no error.

Here is the full console log:

```
[wallet xxx]: transfer xxx 0.1
Wallet password: 
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
Error: unexpected error: Wrong Channel
```

As written in (2), the issue only happens 50% of the time. I’ve found no real pattern behind it.

/cc @cslashm 

# Discussion History
## Zarkoob | 2018-10-08T04:49:40+00:00
Yes if I try and send I have to wait a bit for the ledger to come up with the info (bout 10-15 seconds). It works but you have to wait a bit. 

## selsta | 2018-10-08T17:22:46+00:00
@Zarkoob just to confirm, did you compile v13.0 and tested this? Having to wait for the Ledger is nothing unusual, I’m asking if someone is getting the same error as I do above.

## iDunk5400 | 2018-10-08T19:23:28+00:00
I was able to reproduce this on Windows on stagenet and mainnet. After the fee appears on the device screen, the wallet displays `Error: unexpected error: Wrong Channel` after a few seconds (~10 seconds). The fee remains displayed on the device.

## cslashm | 2018-10-08T19:31:05+00:00
Can someone log the `this->timeout` here: https://github.com/monero-project/monero/blob/release-v0.13/src/device/device_io_hid.cpp#L137

It looks like the call does note take into account this value, which should be 120000, aka 2 min.


## iDunk5400 | 2018-10-08T20:07:39+00:00
```
2018-10-08 20:02:48.087     7f6f1eab2bc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:03:04.559     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:03:07.960     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:03:08.084     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:03:08.182     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:03:08.237     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:03:52.466     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:03:52.565     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:03:52.833     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:00.706     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:00.812     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:00.953     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:00.969     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.064     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.284     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.374     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.479     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.493     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.620     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.732     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.740     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.874     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.923     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.970     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:01.976     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.212     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.455     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.471     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.476     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.495     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.785     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.791     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.807     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.810     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.813     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.829     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.836     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.853     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.856     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.859     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.862     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.877     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.884     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.900     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.903     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.906     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.909     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.924     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.931     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.948     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.951     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.954     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.957     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.972     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.979     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.996     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:02.999     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.002     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.005     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.020     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.027     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.043     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.046     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.049     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.052     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.067     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.074     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.091     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.094     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.097     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.100     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.115     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.122     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.139     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.142     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.145     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.148     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.163     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.170     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.186     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.189     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.192     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.195     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.210     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.217     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.234     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.237     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.240     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.243     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.258     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.265     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.282     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.285     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.288     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.291     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.306     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.313     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.329     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.334     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.427     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.544     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.673     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.697     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:03.806     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.025     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.116     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.220     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.235     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.362     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.474     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.482     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.622     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.666     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.712     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.718     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:04.954     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.069     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.074     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.079     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.101     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.403     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.409     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.412     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.427     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.430     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.434     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.451     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.455     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.458     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.461     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.476     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.481     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.498     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.502     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.505     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.508     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.524     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.528     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.546     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.550     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.553     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.556     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.572     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.576     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.594     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.598     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.601     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.604     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.619     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.624     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.641     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.645     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.648     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.651     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.667     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.671     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.689     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.693     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.696     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.699     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.714     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.718     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.737     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.741     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.744     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.747     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.762     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.767     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.784     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.788     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.791     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.794     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.810     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.815     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.832     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.836     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.839     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.842     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.857     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.862     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.880     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.884     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.887     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.890     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.905     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.909     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.927     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.936     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.953     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:05.956     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:06.049     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:06.166     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:06.295     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:06.319     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:06.428     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:06.648     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:06.738     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:06.841     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:06.857     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:06.984     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:07.097     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:07.104     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:07.244     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:07.287     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:07.334     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
2018-10-08 20:04:17.336     7f27c11acbc0        DEBUG   device.io       src/device/device_io_hid.cpp:138        this->timeout value is 10000
```


## Zarkoob | 2018-10-09T01:11:54+00:00
> @Zarkoob just to confirm, did you compile v13.0 and tested this? Having to wait for the Ledger is nothing unusual, I’m asking if someone is getting the same error as I do above.

I am finally able to get Monero 'Beryllium Bullet' (v0.13.0.1-rc-4b609ded) to compile. I'm Migrating blockchain from DB version 1 to 2 now so this will be a bit but then I will test with the ledger. 

@selsta I've seen where you changed the timeout value in device_ledger.cpp is that all we have to do? If so I will test shortly. 

## selsta | 2018-10-09T01:15:54+00:00
Yes, increasing the timeout seems to resolve this issue :)

## Zarkoob | 2018-10-09T01:47:44+00:00
Yes it does fix this issue for me @selsta . Do I just make a comment with "approve" on the other thread to show I tested this?

edit: Whops looks like I didn't run the right CLI. I'm getting a device not found error. Back to further testing.

## Zarkoob | 2018-10-09T02:05:08+00:00
So I can't get the newest version to notice the Ledger. 

Monero 'Lithium Luna' (v0.12.3.0-release) I can get "EXPORT VIEW KEY" on ledger.
Monero 'Beryllium Bullet' (v0.13.0.1-rc-4b609ded) I get Error: failed to load wallet: device not found: Ledger

## selsta | 2018-10-09T02:10:46+00:00
@Zarkoob did you install libhidapi using homebrew? If not, install it and recompile.

`brew install hidapi`

## Zarkoob | 2018-10-09T02:49:45+00:00
@selsta no I did not. Doing the brew install of hidapi worked! I'm on Monero 'Beryllium Bullet' (v0.13.0.1-rc-4b609ded) with the ledger and tested sending. It does take a bit of time for fee to show on the ledger but I'm **not** getting this timeout issue anymore with your changes from [here](https://github.com/monero-project/monero/pull/4535/commits/c716a331f34da4ce501674b33bdc0995cd599122) 



## cslashm | 2018-10-09T06:28:19+00:00
Super :)

On Tue, Oct 9, 2018 at 3:16 AM selsta <notifications@github.com> wrote:

> Yes, increasing the timeout seems to resolve this issue :)
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/4512#issuecomment-428027548>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AFOX8w4nQN7wbI3t-AdowSnTGrgxWyEzks5ui_jggaJpZM4XL9fH>
> .
>


-- 
C/M.


## selsta | 2018-10-09T21:42:03+00:00
From IRC, someone is still having this issue on macOS after increasing the timeout.

```
23:16 <antanst> selsta: Still doesn't work. After the fee confirmation, Ledger goes back to the app, instead of continuint to tx confirmation question. And after a few mins, the "unexpected error: Wrong Channel" error occurs in the cli wallet.
```

## moneromooo-monero | 2018-10-20T18:59:38+00:00
Believed fixed.

+resolved

## Zarkoob | 2018-10-21T23:49:05+00:00
Forgive me as I'm still new at this whole process but I'm trying to learn. To get the latest and most recent monero changes I went to the git page and found the Latest commit on the v0.13 release. 

I've done a 
`git checkout 4ad6b662837a5901c9f2deece43356f064d13f0f`
Made the program, changed to the resulting directory and did a version and then resulted in 
`Monero 'Beryllium Bullet' (v0.13.0.3-4ad6b662)`

**I assume it matches the git checkout as the 4ad6b662 matches the sha?**

After this I should be current with these merged changes to fix the ledger yes? If so then I **still** have this problem with ledger. 

I went into the /src files and did a compare to make sure they are the right ones with the proper changes and they are **there** before I did make/install.

@moneromooo-monero since  If I'm doing something wrong or can help in any way test for you all I'm happy to help. Thanks again!

# Action History
- Created by: selsta | 2018-10-07T18:05:52+00:00
- Closed at: 2018-10-20T19:16:56+00:00
