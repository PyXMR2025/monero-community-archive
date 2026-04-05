---
title: dev branch xmrig not failover to backup pool
source_url: https://github.com/xmrig/xmrig/issues/3210
author: stiluddclanward
assignees: []
labels: []
created_at: '2023-02-10T02:37:39+00:00'
updated_at: '2025-06-18T22:48:20+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:48:20+00:00'
---

# Original Description
**Describe the bug**
I build xmrig from source in ubuntu，I use dev branch because i want compile with my config file
change the default config file xmrig/src/core/config/Config_default.h
change xmrig/src/base/kernel/Base.cpp。delete content below
133         chain.addFile(Process::location(Process::DataLocation, "config.json"));
134         if (read(chain, config)) {
135             return config.release();
136         }
137 
138         chain.addFile(Process::location(Process::HomeLocation,  "." APP_ID ".json"));
139         if (read(chain, config)) {
140             return config.release();
141         }
142 
143         chain.addFile(Process::location(Process::HomeLocation, ".config" XMRIG_DIR_SEPARATOR APP_ID ".json"));
144         if (read(chain, config)) {
145             return config.release();
146         }


then build command
cmake .. -DXMRIG_DEPS=scripts/deps -DWITH_EMBEDDED_CONFIG=ON -DBUILD_STATIC=ON -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF -DWITH_CN_FEMTO=OFF -DWITH_ARGON2=OFF -DWITH_KAWPOW=OFF -DWITH_GHOSTRIDER=OFF


xmrig/src/core/config/Config_default.h content
/* XMRig
 * Copyright (c) 2018-2021 SChernykh   <https://github.com/SChernykh>
 * Copyright (c) 2016-2021 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
 *
 *   This program is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, either version 3 of the License, or
 *   (at your option) any later version.
 *
 *   This program is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with this program. If not, see <http://www.gnu.org/licenses/>.
 */


#ifndef XMRIG_CONFIG_DEFAULT_H
#define XMRIG_CONFIG_DEFAULT_H


namespace xmrig {


// This feature require CMake option: -DWITH_EMBEDDED_CONFIG=ON
#ifdef XMRIG_FEATURE_EMBEDDED_CONFIG
const static char *default_config =
R"===(
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
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "monero",
            "url": "xmr-us-east1.nanopool.org:14444",
            "user": "86cZbRQA56a5XkZTCfqj44YMoLU1KRc3n1rfHv6sdRia93fgWgtQPfo5hb1o1KHMv2C3qJrG5GqYTUCUBKTAmF2n2V4KSwe",
            "rig-id": null,
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        },
		{
            "algo": "rx/0",
            "coin": "monero",
            "url": "xmr-asia1.nanopool.org:14444",
            "user": "86cZbRQA56a5XkZTCfqj44YMoLU1KRc3n1rfHv6sdRia93fgWgtQPfo5hb1o1KHMv2C3qJrG5GqYTUCUBKTAmF2n2V4KSwe",
            "rig-id": null,
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }	
    ],
    "log-file": null,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "retries": 5,
    "retry-pause": 5,
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
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
)===";
#endif


} // namespace xmrig


#endif /* XMRIG_CONFIG_DEFAULT_H */


when i run xmrig ，first pool can't connect，It not failover to my backup pool

xmrig run log below

root@vultr:~/xmrig/build# ./xmrig
 * ABOUT        XMRig/6.19.1-dev gcc/9.4.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel Core Processor (Broadwell, no TSX, IBRS) (1) 64-bit AES VM
                L2:4.0 MB L3:16.0 MB 1C/1T NUMA:1
 * MEMORY       0.5/1.0 GB (56%)
                DIMM 0: 1 GB RAM @ 0 MHz DIMM 0
 * MOTHERBOARD  Vultr - VC2
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr-us-east1.nanopool.org:14444 coin Monero
 * POOL #2      xmr-asia1.nanopool.org:14444 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
[2023-02-10 02:26:08.587]  net      xmr-us-east1.nanopool.org:14444 127.0.0.1 connect error: "connection refused"
[2023-02-10 02:26:14.579]  net      xmr-us-east1.nanopool.org:14444 127.0.0.1 connect error: "connection refused"
[2023-02-10 02:26:19.584]  net      xmr-us-east1.nanopool.org:14444 127.0.0.1 connect error: "connection refused"
[2023-02-10 02:26:24.590]  net      xmr-us-east1.nanopool.org:14444 127.0.0.1 connect error: "connection refused"
[2023-02-10 02:26:29.595]  net      xmr-us-east1.nanopool.org:14444 127.0.0.1 connect error: "connection refused"
Segmentation fault (core dumped)



**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
# Action History
- Created by: stiluddclanward | 2023-02-10T02:37:39+00:00
- Closed at: 2025-06-18T22:48:20+00:00
