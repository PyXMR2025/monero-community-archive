---
title: Parsing not well formatted /etc/libccid_Info.plist causes invalid pointer error.
source_url: https://github.com/monero-project/monero/issues/4157
author: dannywillems
assignees: []
labels: []
created_at: '2018-07-20T11:34:22+00:00'
updated_at: '2018-10-09T11:16:57+00:00'
type: issue
status: closed
closed_at: '2018-10-09T11:16:57+00:00'
---

# Original Description
By mistake, I added two lines instead of one in one section of `/etc/libccid_Info.plist`, and i got this error.
```
➜  monero ./monero-wallet-cli --generate-from-device MoneroWallet --subaddress-lookahead 3:200
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.                                                                                                                       
WARNING: Do not reuse your Monero keys on an another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.
                                         
Monero 'Lithium Luna' (v0.12.2.0-release)
Logging to ./monero-wallet-cli.log  
Enter a new password for the wallet:
Confirm password:                                                                                                                 
*** Error in `./monero-wallet-cli': munmap_chunk(): invalid pointer: 0x00007fffc1b47480 ***                                                                                                                              ======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x777e5)[0x7f0942a067e5]                                                                        
/lib/x86_64-linux-gnu/libc.so.6(cfree+0x1a8)[0x7f0942a13698]                                                         
/lib/x86_64-linux-gnu/libpcsclite.so.1(SCardFreeMemory+0x1d)[0x7f09434872bd]
./monero-wallet-cli(_ZN2hw6ledger13device_ledger7connectEv+0x6f4)[0x559c9ee26b04]
./monero-wallet-cli(_ZN10cryptonote12account_base18create_from_deviceERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x1f8)[0x559c9edf7378]
./monero-wallet-cli(_ZN5tools7wallet27restoreERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERKN4epee15wipeable_stringES8_+0x23b)[0x559c9ebbcb6b]
./monero-wallet-cli(_ZN10cryptonote13simple_wallet10new_walletERKN5boost15program_options13variables_mapERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0xf4)[0x559c9ea630e4]
./monero-wallet-cli(_ZN10cryptonote13simple_wallet4initERKN5boost15program_options13variables_mapE+0x190c)[0x559c9ea7b1bc]
./monero-wallet-cli(main+0x355)[0x559c9ea38af5]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf0)[0x7f09429af830]
./monero-wallet-cli(_start+0x29)[0x559c9ea458c9]                        
======= Memory map: ========  
559c9e63a000-559c9f3bd000 r-xp 00000000 00:2c 7090873                    /home/danny/nodes/monero/monero-gui-v0.12.2.0/monero-wallet-cli
559c9f5bd000-559c9f605000 r--p 00d83000 00:2c 7090873                    /home/danny/nodes/monero/monero-gui-v0.12.2.0/monero-wallet-cli
559c9f605000-559c9f620000 rw-p 00dcb000 00:2c 7090873                    /home/danny/nodes/monero/monero-gui-v0.12.2.0/monero-wallet-cli
559c9f620000-559c9f659000 rw-p 00000000 00:00 0                                                                                                 
559c9fa0d000-559c9fb73000 rw-p 00000000 00:00 0                          [heap]
7f0941750000-7f0941766000 r-xp 00000000 fc:01 30675344                   /lib/x86_64-linux-gnu/libgcc_s.so.1
7f0941766000-7f0941965000 ---p 00016000 fc:01 30675344                   /lib/x86_64-linux-gnu/libgcc_s.so.1
7f0941965000-7f0941966000 rw-p 00015000 fc:01 30675344                   /lib/x86_64-linux-gnu/libgcc_s.so.1
7f0941966000-7f0941a66000 r--s 00000000 00:2c 23596262                   /home/danny/.shared-ringdb/data.mdb
7f0941a66000-7f0941e68000 rw-p 00000000 00:00 0                                                                                   
7f0941e68000-7f0941e69000 ---p 00000000 00:00 0
7f0941e69000-7f0942669000 rw-p 00000000 00:00 0
7f0942669000-7f094298f000 r--p 00000000 fc:01 12061994                   /usr/lib/locale/locale-archive
7f094298f000-7f0942b4f000 r-xp 00000000 fc:01 30676421                   /lib/x86_64-linux-gnu/libc-2.23.so
7f0942b4f000-7f0942d4f000 ---p 001c0000 fc:01 30676421                   /lib/x86_64-linux-gnu/libc-2.23.so
7f0942d4f000-7f0942d53000 r--p 001c0000 fc:01 30676421                   /lib/x86_64-linux-gnu/libc-2.23.so
7f0942d53000-7f0942d55000 rw-p 001c4000 fc:01 30676421                   /lib/x86_64-linux-gnu/libc-2.23.so
7f0942d55000-7f0942d59000 rw-p 00000000 00:00 0
7f0942d59000-7f0942d71000 r-xp 00000000 fc:01 30676420                   /lib/x86_64-linux-gnu/libpthread-2.23.so
7f0942d71000-7f0942f70000 ---p 00018000 fc:01 30676420                   /lib/x86_64-linux-gnu/libpthread-2.23.so
7f0942f70000-7f0942f71000 r--p 00017000 fc:01 30676420                   /lib/x86_64-linux-gnu/libpthread-2.23.so
7f0942f71000-7f0942f72000 rw-p 00018000 fc:01 30676420                   /lib/x86_64-linux-gnu/libpthread-2.23.so
7f0942f72000-7f0942f76000 rw-p 00000000 00:00 0
7f0942f76000-7f094307e000 r-xp 00000000 fc:01 30671051                   /lib/x86_64-linux-gnu/libm-2.23.so
7f094307e000-7f094327d000 ---p 00108000 fc:01 30671051                   /lib/x86_64-linux-gnu/libm-2.23.so
7f094327d000-7f094327e000 r--p 00107000 fc:01 30671051                   /lib/x86_64-linux-gnu/libm-2.23.so
7f094327e000-7f094327f000 rw-p 00108000 fc:01 30671051                   /lib/x86_64-linux-gnu/libm-2.23.so
7f094327f000-7f0943282000 r-xp 00000000 fc:01 30676423                   /lib/x86_64-linux-gnu/libdl-2.23.so
7f0943282000-7f0943481000 ---p 00003000 fc:01 30676423                   /lib/x86_64-linux-gnu/libdl-2.23.so
7f0943481000-7f0943482000 r--p 00002000 fc:01 30676423                   /lib/x86_64-linux-gnu/libdl-2.23.so
7f0943482000-7f0943483000 rw-p 00003000 fc:01 30676423                   /lib/x86_64-linux-gnu/libdl-2.23.so
7f0943483000-7f094348d000 r-xp 00000000 fc:01 30675407                   /lib/x86_64-linux-gnu/libpcsclite.so.1.0.0
7f094348d000-7f094368c000 ---p 0000a000 fc:01 30675407                   /lib/x86_64-linux-gnu/libpcsclite.so.1.0.0
7f094368c000-7f094368d000 r--p 00009000 fc:01 30675407                   /lib/x86_64-linux-gnu/libpcsclite.so.1.0.0
7f094368d000-7f094368e000 rw-p 0000a000 fc:01 30675407                   /lib/x86_64-linux-gnu/libpcsclite.so.1.0.0
7f094368e000-7f09436b4000 r-xp 00000000 fc:01 30676419                   /lib/x86_64-linux-gnu/ld-2.23.so
7f0943789000-7f094388f000 rw-p 00000000 00:00 0
7f09438b0000-7f09438b1000 rw-p 00000000 00:00 0
7f09438b1000-7f09438b3000 rw-s 00000000 00:2c 23595145                   /home/danny/.shared-ringdb/lock.mdb
7f09438b3000-7f09438b4000 r--p 00025000 fc:01 30676419                   /lib/x86_64-linux-gnu/ld-2.23.so
7f09438b4000-7f09438b5000 rw-p 00026000 fc:01 30676419                   /lib/x86_64-linux-gnu/ld-2.23.so
7f09438b5000-7f09438b6000 rw-p 00000000 00:00 0
7fffc1b2c000-7fffc1b52000 rw-p 00000000 00:00 0                          [stack]
7fffc1b79000-7fffc1b7c000 r--p 00000000 00:00 0                          [vvar]
7fffc1b7c000-7fffc1b7e000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
[1]    6768 abort (core dumped)  ./monero-wallet-cli --generate-from-device MoneroWallet --subaddress-lookahea
```

# Discussion History
## moneromooo-monero | 2018-07-20T12:40:18+00:00
Please report to the libpcsclite bug tracker (don't know where that is offhand though).

## dannywillems | 2018-07-20T13:50:24+00:00
@moneromooo-monero reported here https://github.com/LudovicRousseau/PCSC/issues/43

## moneromooo-monero | 2018-08-16T19:07:55+00:00
Can you please supply the info upstream requested to they can debug it ?

## moneromooo-monero | 2018-10-09T11:09:57+00:00
libpcsc-lite is now gone, replace by libhidapi.

I'll close this since it is no longer applicable to monero, but upstream would like to get the information requested in https://github.com/LudovicRousseau/PCSC/issues/43 to debug further since it appears to be independent of monero.

+resolved


# Action History
- Created by: dannywillems | 2018-07-20T11:34:22+00:00
- Closed at: 2018-10-09T11:16:57+00:00
