---
title: Precompiled binaries for OSX - errors.
source_url: https://github.com/monero-project/monero/issues/1658
author: silverdr
assignees: []
labels: []
created_at: '2017-02-01T11:21:28+00:00'
updated_at: '2017-02-01T20:25:49+00:00'
type: issue
status: closed
closed_at: '2017-02-01T20:25:49+00:00'
---

# Original Description
The downloaded archive "monero.mac.x64.v0-10-1-0.tar.bz2", checksummed to `447cebae257864b3706a8622f495bfd9fae780a6b277e1e31ac83bef7bc855c6` gives the following error messages upon invoking `monero-wallet-cli`:

```
$ monero-wallet-cli --daemon-host <daemon-host-hostname> --wallet-file=<path-to-wallet-file>
Monero 'Wolfram Warptangent' (v0.10.1.0-release)
Logging at log level 0 to /Users/silverdr/monero-wallet-cli.log
Password: ***********************
monero-wallet-cli(2832,0x7fff78e3f000) malloc: *** mach_vm_map(size=7809639168886382592) failed (error code=3)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
monero-wallet-cli(2832,0x7fff78e3f000) malloc: *** mach_vm_map(size=5471673553619697664) failed (error code=3)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
Error: failed to load wallet: std::bad_alloc
```

`<daemon-host-name>` and `<path-to-wallet-file>` are both valid

Binary compiled from sources (with lots of warnings) seem to correctly initialize and open the wallet file with the very same command line.

OS version is: 10.11.6 (15G1217)



# Discussion History
## Jaqueeee | 2017-02-01T11:34:06+00:00
Wallets opened with recent builds and the binaries bundled with the beta GUI will have their cache converted to a new portable format. The new format is not backward compatible.  If you have opened this wallet with a recent build prior to this, it will not work with the 0.10.1 binaries. As a workaround you could move/rename the wallet cache file to rebuild the cache. 
http://monero.stackexchange.com/questions/3122/how-do-i-delete-the-wallet-cache/3123

## silverdr | 2017-02-01T19:42:23+00:00
That might explain. I opened the same wallet with my own build first. But - since my own build generated a lot of warnings during building - I wanted to try an official binary, which I expected to be better built/tested. I'll try to clear the cache as you suggest.

## silverdr | 2017-02-01T20:25:49+00:00
That solved the problem. Thank you.

# Action History
- Created by: silverdr | 2017-02-01T11:21:28+00:00
- Closed at: 2017-02-01T20:25:49+00:00
