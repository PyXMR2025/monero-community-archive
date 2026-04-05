---
title: illegal instruction
source_url: https://github.com/xmrig/xmrig/issues/749
author: PowaBanga
assignees:
- xmrig
labels:
- arm
created_at: '2018-09-09T14:12:42+00:00'
updated_at: '2019-08-08T19:09:32+00:00'
type: issue
status: closed
closed_at: '2019-02-03T20:05:34+00:00'
---

# Original Description
hi,
I installed xmrig on archlinux via Aur, on my raspberrypi 3b+ armv7,
I did this config file from [config.xmrig.com](https://config.xmrig.com/xmrig/result/7FRUHyr2k6zFoohZ5q4DuocpX2GaPmsTS8xRV2fjdjXRDAdhWDaECv8T7ADvVmEXcDxVNFmoMt8D4oTSzcUBEbH6gzn5fJ6przjQguZ27umjKDXi8NxAXM1JJbAEZoVMDYAnxSzmxxf9PKH34QqK5K134Q2ARM2nqFvHAVuLGprqe5LbCzovfa1eADH8FPS6izHwW5kxEvYchQbHt9QKg5ScPTsoSB8LoBiWLV9mkGBFCNXcJj6qjgR6nnWBDS2YybfX3gAth3BXworTRLAtqF9HEsuyZdNtpKGeAWQpV7fG4V5gxQYgMs5GA2kte2i28vS2axsDr3UjpRJMR8LgHYQhCxbdKsEtfn)
```
{
    "algo": "cryptonight",
    "api": {
        "port": 8182,
        "access-token": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-priority": null,
    "donate-level": 5,
    "log-file": null,
    "max-cpu-usage": 75,
    "pools": [
        {
            "url": "pool.monero.hashvault.pro:3333",
            "user": "45aGznNPx7pPfSB2WdDzxqWxgSxf2uBZzMEnJofWzkJMayEQqhefkdm6W3CCoBVmxi4bKkmv2XkpD2Azn1whZ46AAMPbaDF",
            "pass": "x",
            "keepalive": true,
            "nicehash": false,
            "variant": 1
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "syslog": false,
    "threads": null
}
```
And, when i launch it, i have that : 

```
[powabanga@RaspberryPi ~]$ xmrig --config=/home/powabanga/.xmrig/config.json
 * VERSIONS     XMRig/2.6.4 libuv/1.23.0 gcc/8.2.0
 * CPU          Unknown (1) x64 AES-NI
 * THREADS      4, cryptonight, av=0, donate=5%
 * POOL #1      pool.monero.hashvault.pro:3333 variant 1
 * API BIND     0.0.0.0:8182
 * COMMANDS     hashrate, pause, resume
Illegal instruction (core dumped)

```

Does anybody can explain to me what is wrong with me ?


# Discussion History
## 2010phenix | 2018-09-10T11:19:32+00:00
make and post more info about your CPU " Unknown (1) x64 AES-NI"

## xmrig | 2018-09-10T14:07:35+00:00
Raspberry Pi does not support hardware AES and the miner does not support detection of this at runtime, so you need to manually disable use of hardware AES via option `av`.

```json
{
  ...
  "av": 3,
  ...
}
```

## lhirlimann | 2018-10-31T21:20:22+00:00
Sample code for detection https://community.arm.com/android-community/b/android/posts/runtime-detection-of-cpu-features-on-an-armv8-a-cpu

## xmrig | 2018-11-05T14:15:04+00:00
@lhirlimann thank you looks good.

## xmrig | 2019-02-03T20:05:34+00:00
Fixed. Thank you.

## sjefkedansplaat | 2019-08-08T19:09:32+00:00
Since I have the same problem with the illegal instruction as above.

Below the config.json and the cpu cat

running distro Raspbian buster lite from 2019-07-10
```{
    "algo": "cryptonight-light",
    "api": {
        "port": 3333,
        "access-token": "null",
        "worker-id": "pi2brig",
        "ipv6": false,
        "restricted": false
    },
    "av": 3,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": null,
    "donate-level": 5,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": null,
    "max-cpu-usage": 50,
    "pools": [{
		"url": "pool.aeon.hashvault.pro:3333",
		"user": "here is my wallet id",
		"pass": "here is my pass",
		"keepalive": true,
		"nicehash": false,
		"rig-id": null,
		"variant": -1,
		"enabled": true,
		"tls": false,
		"tls-fingerprint": null
	}],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "threads": [
        {
            "low_power_mode": 1,
            "affine_to_cpu": 0
        }
    ],
    "user-agent": null,
    "syslog": false,
    "watch": false
}



cat /proc/cpuinfo
processor	: 0
model name	: ARMv7 Processor rev 5 (v7l)
BogoMIPS	: 38.40
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 5

processor	: 1
model name	: ARMv7 Processor rev 5 (v7l)
BogoMIPS	: 38.40
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 5

processor	: 2
model name	: ARMv7 Processor rev 5 (v7l)
BogoMIPS	: 38.40
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 5

processor	: 3
model name	: ARMv7 Processor rev 5 (v7l)
BogoMIPS	: 38.40
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 5

Hardware	: BCM2835
Revision	: a01041
Serial		: 00000000aa969b87```

# Action History
- Created by: PowaBanga | 2018-09-09T14:12:42+00:00
- Closed at: 2019-02-03T20:05:34+00:00
