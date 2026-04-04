---
title: monero-wallet-cli - Crash on macOS(Arm or x64)
source_url: https://github.com/monero-project/monero/issues/8453
author: realityworks
assignees: []
labels: []
created_at: '2022-07-22T05:32:14+00:00'
updated_at: '2022-08-25T23:09:49+00:00'
type: issue
status: closed
closed_at: '2022-08-25T23:09:49+00:00'
---

# Original Description
While trying to start the refresh, it seems it just won't do anything but crash : 

```
monero-wallet-cli(7051,0x308a28000) malloc: Incorrect checksum for freed object 0x7fb9811c7888: probably modified after being freed.
Corrupt value: 0xf2ecab05a6f0f362
monero-wallet-cli(7051,0x308a28000) malloc: *** set a breakpoint in malloc_error_break to debug
```

I also get an error like this : 
```
monero-wallet-cli(7696,0x203fe22c0) malloc: tiny_free_list_remove_ptr: Internal invariant broken (prev ptr of next): ptr=0x7fce52fc7350, next_prev=0x0
monero-wallet-cli(7696,0x203fe22c0) malloc: *** set a breakpoint in malloc_error_break to debug
```

All I am doing is running the daemon in the background as usual.

The only change is I am running macOS (13.0) Ventura.

Any idea what's happening? Do I need to rebuild my Database?

I hav tried version 18 and 17.3.2 and both produce the same results after reading a number of inputs.

# Discussion History
## selsta | 2022-07-22T08:41:05+00:00
Since this only happens on Ventura and Ventura is still in beta it's unclear at this point if this is a monero bug or not. We already found a different Ventura bug and reported it to Apple.

For now we will wait for the next beta first before we spend a huge time debugging something that's possibly an OS bug.

## selsta | 2022-08-08T18:52:32+00:00
@realityworks Can you update to the latest beta and try adding `--max-concurrency` with the amount of CPU cores you have?

## selsta | 2022-08-25T20:33:31+00:00
This appears to be fixed in Ventura beta 6.

# Action History
- Created by: realityworks | 2022-07-22T05:32:14+00:00
- Closed at: 2022-08-25T23:09:49+00:00
