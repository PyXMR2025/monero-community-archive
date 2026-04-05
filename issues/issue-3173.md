---
title: xmrig disconnects from network whenever started
source_url: https://github.com/xmrig/xmrig/issues/3173
author: cryptoquick
assignees: []
labels:
- question
created_at: '2022-12-05T14:52:19+00:00'
updated_at: '2022-12-16T23:38:02+00:00'
type: issue
status: closed
closed_at: '2022-12-16T23:38:02+00:00'
---

# Original Description
## Describe the bug
Whenever I start xmrig, Gnome Desktop makes a sound to notify me that my USB ethernet adapter has been unplugged. Stopping xmrig immediately reconnects the network adapter. This works regardless of whether run with sudo or not.

## Required data

### Miner log as text or screenshot

Without sudo:

```
xmrig -c xmr-full.json                                                                                                                                                         3236ms  Mon Dec  5 07:47:00 2022
 * ABOUT        XMRig/6.18.1 gcc/12.2.0
 * LIBS         libuv/1.44.2 OpenSSL/3.0.7 hwloc/2.8.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 5950X 16-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       19.3/125.7 GB (15%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-12-05 07:47:55.320]  net      use pool pool.supportxmr.com:443 TLSv1.2 148.163.81.34
[2022-12-05 07:47:55.321]  net      fingerprint (SHA-256): "..."
[2022-12-05 07:47:55.321]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2770731 (62 tx)
[2022-12-05 07:47:55.321]  cpu      use argon2 implementation AVX2
[2022-12-05 07:47:55.323]  msr      cannot read MSR 0xc0011020
[2022-12-05 07:47:55.323]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2022-12-05 07:47:55.323]  randomx  init dataset algo rx/0 (32 threads) seed 869bcf05eba031cd...
[2022-12-05 07:47:55.478]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (155 ms)
[2022-12-05 07:47:56.634]  randomx  dataset ready (1156 ms)
[2022-12-05 07:47:56.634]  cpu      use profile  rx  (30 threads) scratchpad 2048 KB
[2022-12-05 07:47:56.647]  cpu      READY threads 30/30 (30) huge pages 100% 30/30 memory 61440 KB (13 ms)
[2022-12-05 07:47:58.524]  signal   Ctrl+C received, exiting
[2022-12-05 07:47:58.528]  cpu      stopped (3 ms)
```

With sudo:

```
sudo xmrig -c xmr-full.json                                                                                                                                                      9.4s  Mon Dec  5 07:46:55 2022
 * ABOUT        XMRig/6.18.1 gcc/12.2.0
 * LIBS         libuv/1.44.2 OpenSSL/3.0.7 hwloc/2.8.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 9 5950X 16-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       19.2/125.7 GB (15%)
                DIMM_A0: 32 GB DDR4 @ 3200 MHz KHX3200C16D4/32GX
                DIMM_A1: 32 GB DDR4 @ 3200 MHz KHX3200C16D4/32GX
                DIMM_B0: 32 GB DDR4 @ 3200 MHz KHX3200C16D4/32GX
                DIMM_B1: 32 GB DDR4 @ 3200 MHz KHX3200C16D4/32GX
 * MOTHERBOARD  Micro-Star International Co., Ltd. - MEG X570 GODLIKE (MS-7C34)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-12-05 07:46:57.421]  net      use pool pool.supportxmr.com:443 TLSv1.2 148.163.88.50
[2022-12-05 07:46:57.421]  net      fingerprint (SHA-256): "..."
[2022-12-05 07:46:57.421]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2770730 (71 tx)
[2022-12-05 07:46:57.421]  cpu      use argon2 implementation AVX2
[2022-12-05 07:46:57.422]  msr      register values for "ryzen_19h" preset have been set successfully (1 ms)
[2022-12-05 07:46:57.422]  randomx  init dataset algo rx/0 (32 threads) seed 869bcf05eba031cd...
[2022-12-05 07:46:57.593]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (171 ms)
[2022-12-05 07:46:58.810]  randomx  dataset ready (1217 ms)
[2022-12-05 07:46:58.810]  cpu      use profile  rx  (30 threads) scratchpad 2048 KB
[2022-12-05 07:46:58.833]  cpu      READY threads 30/30 (30) huge pages 100% 30/30 memory 61440 KB (23 ms)
[2022-12-05 07:47:00.419]  signal   Ctrl+C received, exiting
[2022-12-05 07:47:00.424]  cpu      stopped 
```

### Config file or command line (without wallets)

```
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 16, 1, 17, 2, 18, 3, 19, 4, 20, 5, 21, 6, 22, 7, 23, 8, 24, 9, 25, 10, 26, 11, 27, 12, 28, 13, 29, 14, 30, 15, 31],
        "astrobwt": [0, 16, 1, 17, 2, 18, 3, 19, 4, 20, 5, 21, 6, 22, 7, 23, 8, 24, 9, 25, 10, 26, 11, 27, 12, 28, 13, 29, 14, 30, 15, 31],
        "cn": [
            [1, 0],
            [1, 16],
            [1, 1],
            [1, 17],
            [1, 2],
            [1, 18],
            [1, 3],
            [1, 19],
            [1, 4],
            [1, 20],
            [1, 5],
            [1, 21],
            [1, 6],
            [1, 22],
            [1, 7],
            [1, 23],
            [1, 8],
            [1, 24],
            [1, 9],
            [1, 25],
            [1, 10],
            [1, 26],
            [1, 11],
            [1, 27],
            [1, 12],
            [1, 28],
            [1, 13],
            [1, 29],
            [1, 14],
            [1, 30],
            [1, 15],
            [1, 31]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15]
        ],
        "cn-lite": [
            [1, 0],
            [1, 16],
            [1, 1],
            [1, 17],
            [1, 2],
            [1, 18],
            [1, 3],
            [1, 19],
            [1, 4],
            [1, 20],
            [1, 5],
            [1, 21],
            [1, 6],
            [1, 22],
            [1, 7],
            [1, 23],
            [1, 8],
            [1, 24],
            [1, 9],
            [1, 25],
            [1, 10],
            [1, 26],
            [1, 11],
            [1, 27],
            [1, 12],
            [1, 28],
            [1, 13],
            [1, 29],
            [1, 14],
            [1, 30],
            [1, 15],
            [1, 31]
        ],
        "cn-pico": [
            [2, 0],
            [2, 16],
            [2, 1],
            [2, 17],
            [2, 2],
            [2, 18],
            [2, 3],
            [2, 19],
            [2, 4],
            [2, 20],
            [2, 5],
            [2, 21],
            [2, 6],
            [2, 22],
            [2, 7],
            [2, 23],
            [2, 8],
            [2, 24],
            [2, 9],
            [2, 25],
            [2, 10],
            [2, 26],
            [2, 11],
            [2, 27],
            [2, 12],
            [2, 28],
            [2, 13],
            [2, 29],
            [2, 14],
            [2, 30],
            [2, 15],
            [2, 31]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 16],
            [2, 1],
            [2, 17],
            [2, 2],
            [2, 18],
            [2, 3],
            [2, 19],
            [2, 4],
            [2, 20],
            [2, 5],
            [2, 21],
            [2, 6],
            [2, 22],
            [2, 7],
            [2, 23],
            [2, 8],
            [2, 24],
            [2, 9],
            [2, 25],
            [2, 10],
            [2, 26],
            [2, 11],
            [2, 27],
            [2, 12],
            [2, 28],
            [2, 13],
            [2, 29],
            [2, 14],
            [2, 30],
            [2, 15],
            [2, 31]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2],
            [8, 3],
            [8, 4],
            [8, 5],
            [8, 6],
            [8, 7],
            [8, 8],
            [8, 9],
            [8, 10],
            [8, 11],
            [8, 12],
            [8, 13],
            [8, 14],
            [8, 15]
        ],
        "rx": [0, 16, 1, 17, 2, 18, 3, 19, 4, 20, 5, 21, 6, 22, 7, 23, 8, 24, 9, 25, 10, 26, 11, 27, 12, 28, 13, 29, 14, 30],
        "rx/wow": [0, 16, 1, 17, 2, 18, 3, 19, 4, 20, 5, 21, 6, 22, 7, 23, 8, 24, 9, 25, 10, 26, 11, 27, 12, 28, 13, 29, 14, 30, 15],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.supportxmr.com:443",
            "user": "...",
            "pass": "...",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
```

### OS
Arch Linux
`uname -a`
```
Linux ... 6.0.11-zen1-1-zen #1 ZEN SMP PREEMPT_DYNAMIC Fri, 02 Dec 2022 17:25:29 +0000 x86_64 GNU/Linux
```

### Additional context

Section in journalctl at time of incident:

```
Dec 05 07:48:02 ... ModemManager[1114]: <info>  [base-manager] couldn't check support for device '/sys/devices/pci0000:00/0000:00:08.1/0000:31:00.3/usb6/6-3/6-3.2': not supported by any plugin
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0061] device (enp49...u2): carrier: link connected
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0065] device (enp49...u2): state change: unavailable -> disconnected (reason 'carrier-changed', sys-iface-state: 'managed')
Dec 05 07:48:03 ... kernel: IPv6: ADDRCONF(NETDEV_CHANGE): enp49...u2: link becomes ready
Dec 05 07:48:03 ... kernel: r8152 6-3.2:1.0 enp49...u2: carrier on
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0069] policy: auto-activating connection 'Wired connection 1' (8b71e586-...)
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0071] device (enp49...u2): Activation: starting connection 'Wired connection 1' (8b71e586-...)
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0072] device (enp49...u2): state change: disconnected -> prepare (reason 'none', sys-iface-state: 'managed')
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0073] manager: NetworkManager state is now CONNECTING
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0073] device (enp49...u2): state change: prepare -> config (reason 'none', sys-iface-state: 'managed')
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0074] device (enp49...u2): state change: config -> ip-config (reason 'none', sys-iface-state: 'managed')
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0077] dhcp4 (enp49...u2): activation: beginning transaction (timeout in 45 seconds)
Dec 05 07:48:03 ... avahi-daemon[1072]: Joining mDNS multicast group on interface enp49...u2.IPv6 with address ffff::...::ffff.
Dec 05 07:48:03 ... avahi-daemon[1072]: New relevant interface enp49...u2.IPv6 for mDNS.
Dec 05 07:48:03 ... avahi-daemon[1072]: Registering new address record for ffff::...::ffff on enp49...u2.*.
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0260] dhcp4 (enp49...u2): state changed new lease, address=192.168.1...
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0263] policy: set 'Wired connection 1' (enp49...u2) as default for IPv4 routing and DNS
Dec 05 07:48:03 ... avahi-daemon[1072]: Joining mDNS multicast group on interface enp49...u2.IPv4 with address 192.168.1....
Dec 05 07:48:03 ... avahi-daemon[1072]: New relevant interface enp49...u2.IPv4 for mDNS.
Dec 05 07:48:03 ... avahi-daemon[1072]: Registering new address record for 192.168.1... on enp49...u2.IPv4.
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0446] device (enp49...u2): state change: ip-config -> ip-check (reason 'none', sys-iface-state: 'managed')
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0464] device (enp49...u2): state change: ip-check -> secondaries (reason 'none', sys-iface-state: 'managed')
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0466] device (enp49...u2): state change: secondaries -> activated (reason 'none', sys-iface-state: 'managed')
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0468] manager: NetworkManager state is now CONNECTED_SITE
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.0470] device (enp49...u2): Activation: successful, device activated.
Dec 05 07:48:03 ... NetworkManager[1103]: <info>  [1670251683.3126] manager: NetworkManager state is now CONNECTED_GLOBAL
```

# Discussion History
## SChernykh | 2022-12-05T15:30:46+00:00
XMRig log doesn't show any disconnect. Does it keep mining normally after the sound? Try to set `"priority": 0,` in the config to run XMRig with low priority and reduce interference with other system programs.

## cryptoquick | 2022-12-13T03:35:24+00:00
It does not, it just disconnects from the internet and the program sits there, doing nothing. I have to kill the process and physically disconnect and reconnect my Ethernet adapter. With subsequent tries I don't have to physically reset the adapter, just using ctrl-C brings the internet back. Setting `"priority": 0,` in the `"cpu"` section doesn't help.

## Sstealther0101 | 2022-12-13T03:48:03+00:00
Same with me but idk even how to properly mine Im trying to sleep excuse
it's 5 :40 in morning here European time

On Tue, 13 Dec 2022, 05:35 Hunter Trujillo, ***@***.***>
wrote:

> It does not, it just disconnects from the internet and the program sits
> there, doing nothing. I have to kill the process and physically disconnect
> and reconnect my Ethernet adapter. With subsequent tries I don't have to
> physically reset the adapter, just using ctrl-C brings the internet back.
> Setting "priority": 0, in the "cpu" section doesn't help.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3173#issuecomment-1347698178>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/A4WBK452IPDLXGZ4DBV4CNDWM7VIPANCNFSM6AAAAAASULXJP4>
> .
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


## xmrig | 2022-12-13T14:12:23+00:00
Network applications can't detect unplugging of ethernet cable and likely the whole adapter. Down connection will be detected after submitting share or keepalive timeout whatever comes first. In the worst case it can take a few minutes.
Thank you.


## cryptoquick | 2022-12-15T04:42:25+00:00
> Network applications can't detect unplugging of ethernet cable and likely the whole adapter. Down connection will be detected after submitting share or keepalive timeout whatever comes first. In the worst case it can take a few minutes. Thank you.

That's irrelevant; starting xmrig disconnects me from the internet. I have to reset the adapter to get it reconnected, and only after killing xmrig.

## SChernykh | 2022-12-15T06:27:02+00:00
I can tell for sure xmrig doesn't have any code that messes with network adapters, and even if it had, it shouldn't be able to do this when it runs without `sudo`. There's something else on your system that's broken. Maybe any CPU-intensive task that uses all cores can do the same.

## cryptoquick | 2022-12-16T23:38:02+00:00
Well, I'm a Rust developer, I spin up all 32 on a regular basis and it hasn't been a problem. Anyway, I'm not really interested in Monero enough to dig deeper, so I guess I'll just close this.

# Action History
- Created by: cryptoquick | 2022-12-05T14:52:19+00:00
- Closed at: 2022-12-16T23:38:02+00:00
