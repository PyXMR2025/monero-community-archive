---
title: '[raspberrypi-4-4gb-ram] [monerod] Constantly fail downloading the chain at
  96-96%'
source_url: https://github.com/monero-project/monero/issues/7125
author: jscoobyced
assignees: []
labels: []
created_at: '2020-12-11T06:45:49+00:00'
updated_at: '2020-12-12T16:00:38+00:00'
type: issue
status: closed
closed_at: '2020-12-12T16:00:38+00:00'
---

# Original Description
I am using Ubuntu Core 20.10 on a Raspberry Pi 4 with 4GB of RAM. I have mounted an SSD (via USB 3) on `/opt` and the `monero` 
I have built from sources following the README, using these settings:
```
cmake -DNO_AES=ON
make
```
Then I am running the `monerod` using this command as a systemd service:
```
/opt/monero/current/bin/monerod --data-dir /opt/monero/.bitmonerod --non-interactive --enforce-dns-checkpointing --db-sync-mode=safe:sync --prep-blocks-threads 2
```
I have also tried simpler commands without the `--enforce-dns-checkpointing --db-sync-mode=safe:sync --prep-blocks-threads 2` part.
I have also enabled in `/etc/dphys-swapfile`:
```
CONF_MAXSWAP=2048
```
I have tried with more swap as well.

The download process goes well and after about 30 hours, I'm getting around 96% (sometimes 97%) and then it starts failing with this error (I have removed `2020-12-11 05:39:06.496	[P2P7]	INFO	stacktrace` beginning of each line for readability)
```
src/common/stack_trace.cpp:133	Exception: std::runtime_error
src/common/stack_trace.cpp:134	Unwound call stack:
src/common/stack_trace.cpp:172	    [1]  0x12c) [0xaaaad8602350]:__cxa_throw+0x12c) [0xaaaad8602350]
src/common/stack_trace.cpp:172	    [2]  0x6c) [0xaaaad8c0b1fc]:_Z21allocLargePagesMemorym+0x6c) [0xaaaad8c0b1fc]
src/common/stack_trace.cpp:172	    [3]  0x154) [0xaaaad8c01e24]:_alloc_cache+0x154) [0xaaaad8c01e24]
src/common/stack_trace.cpp:172	    [4]  0x21c) [0xaaaad8a13d3c]:_slow_hash+0x21c) [0xaaaad8a13d3c]
src/common/stack_trace.cpp:172	    [5]  0x124) [0xaaaad8a01a28]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmPKS7_i+0x124) [0xaaaad8a01a28]
src/common/stack_trace.cpp:172	    [6]  0x24) [0xaaaad8a01b84]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x24) [0xaaaad8a01b84]
src/common/stack_trace.cpp:172	    [7]  0xe4) [0xaaaad89b3168]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xe4) [0xaaaad89b3168]
```

Seeing the first error being around large pages memory, I tried to see what I can do about it, but couldn't. I've seen something around some huge page configuration in `sysctl` but I don't find any in my Ubuntu config.
I have followed the https://github.com/peanutsformonkeys/raspberry-monerod/blob/master/README.md and now trying to sync again after adding the `swapiness` to 0. I doubt it would do but hey, I'll try all recommended settings.

Anything else I can do? What can I do to not have this large page limitation?

# Discussion History
## moneromooo-monero | 2020-12-11T13:01:42+00:00
That's odd, this ought not to cause a failure. Try running with --log-level 4 (warning: *very* spammy), it's likely that there will be more logs after this, and the cause of the failure is unrelated to this large page message.

## jscoobyced | 2020-12-11T14:03:31+00:00
Thank you, going to try.

## moneromooo-monero | 2020-12-11T14:15:45+00:00
Also, check dmesg, it might just be the OOM killer.

## jscoobyced | 2020-12-11T15:01:06+00:00
The process doesn't die by the way, it keeps logging the error. It even seem to continue downloading but at much lower speed. I have restarted the download, I'll enable lvl 4 logging when it reaches 95% and see.

## moneromooo-monero | 2020-12-11T15:12:30+00:00
Ah, good. The slowness is because it start PoW checks, which it could skip for most of the chain. This can be closed I think, if it's working on your end ?

## jscoobyced | 2020-12-12T16:00:35+00:00
It failed again, but found the reason. I found in syslog that my SSD drive is disconnecting and reconnecting occasionally. It is attached to the RPi by a SSD HAT but maybe the monerod process is too intensive for it. I'll close this issue as not related to monerod. Thanks again for the suggestions.

# Action History
- Created by: jscoobyced | 2020-12-11T06:45:49+00:00
- Closed at: 2020-12-12T16:00:38+00:00
