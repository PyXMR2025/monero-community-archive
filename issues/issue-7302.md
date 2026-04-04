---
title: Trezor Model T wallet refresh error
source_url: https://github.com/monero-project/monero/issues/7302
author: kurohi
assignees: []
labels: []
created_at: '2021-01-10T06:43:46+00:00'
updated_at: '2021-08-13T04:54:59+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:54:59+00:00'
---

# Original Description
Every time I try to refresh my wallet generated with Trezor I get an error after prompted to enter my password.
The command used in the monero-wallet-cli was: `./monero-wallet-cli --hw-device Trezor --wallet-file <wallet_file>`
Which starts refreshing as usual, but after reaching the earliest block, I get the following error:
```
Background mining enabled. Thank you for supporting the Monero network.
Starting refresh...
Enter password (output received): 
free(): invalid pointer
[1]    32432 IOT instruction  ./monero-wallet-cli --hw-device Trezor --wallet-file 
```
In monero-wallet-cli.log I have the following
```
2021-01-10 06:31:34.175	    7f51f72c7540	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
```

Tried recompiling monero several times now, but still was not able to fix this error. The Trezor firmware is 2.3.4 
Thanks a lot in advance

# Discussion History
## selsta | 2021-01-10T12:14:36+00:00
ping @ph4r05 

## ph4r05 | 2021-01-10T12:30:48+00:00
Thanks for info!

Unfortunately, log does not show anything. Can you pls increase loglevel to 4?

Which git commit ID are you compiling? Did you try also official compiler version? If yes, was it 0.17.1.9?

Thanks

## ph4r05 | 2021-01-10T12:33:12+00:00
Btw @selsta, pls did you try testing Trezor with the newest monero version by any chance? (2.3.4 T firmware) I was nit following recent updates.

Thanks!

## selsta | 2021-01-10T12:35:09+00:00
I’ll try to restore my wallet with latest firmware. I did not read any other reports about this issue.

## selsta | 2021-01-10T13:22:34+00:00
I did not have issues doing a full wallet refresh from height 0. @kurohi would recommend to test the official binaries to make sure it is not a compiler issue.

## moneromooo-monero | 2021-01-10T15:36:48+00:00
"free(): invalid pointer" means memory corruption somewhere. Running with ASAN will probably spot the first damage location. You can build with ASAN by adding "-D SANITIZE=ON" to the cmake (not make) command line. 

## kurohi | 2021-01-10T15:37:30+00:00
Thanks a lot for the fast reply. Tried running again with log-level 4 and in the last lines of the log got something suspicious:
```
2021-01-10 15:32:48.791     7f5537735540        TRACE   device.trezor   src/device_trezor/device_trezor_base.cpp:185
    Ask for LOCKING for device  in thread 
2021-01-10 15:32:48.791     7f5537735540        TRACE   device.trezor   src/device_trezor/device_trezor_base.cpp:187
    Device  LOCKed
```
I tried with versions v0.17.1.6 to v0.17.1.8 and releasev0.17 all with the same problem. I am now downloading the binaries and compiling the v0.17.1.9 to test with them


## kurohi | 2021-01-10T16:01:36+00:00
The problem did not occur with the precompiled monero-wallet-cli v0.17.1.9. So I think it might have to do with some mistake in my side when compiling
Could not compile the v0.17.1.9 with -D SANITIZE=ON due to undefined references. Will take a look on why this is happening

## moneromooo-monero | 2021-01-10T16:19:56+00:00
You might be missing libasan.

## selsta | 2021-08-13T04:54:59+00:00
No other reports about this also issue creator confirms it doesn't happen with official binaries. Closing.

# Action History
- Created by: kurohi | 2021-01-10T06:43:46+00:00
- Closed at: 2021-08-13T04:54:59+00:00
