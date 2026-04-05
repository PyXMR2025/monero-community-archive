---
title: '"restricted": true'
source_url: https://github.com/xmrig/xmrig/issues/802
author: snipeTR
assignees: []
labels:
- enhancement
- review later
created_at: '2018-10-15T18:14:31+00:00'
updated_at: '2021-04-12T15:58:44+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:58:44+00:00'
---

# Original Description
The config.json file must have the config.json.md file and enter detailed information about the data and options in it.

# Discussion History
## xmrig | 2018-10-16T06:40:57+00:00
Good idea.

## snipeTR | 2018-10-16T11:07:01+00:00
> Good idea.

there md file 

`{
    :small_red_triangle_down:"algo": "cryptonight",
     :red_circle:**specify the algorithm to use cryptonight cryptonight-lite cryptonight-heavy:red_circle:**
    "api": { 
        :small_red_triangle_down:"port": 0,
         :red_circle:**port for the miner API https://github.com/xmrig/xmrig/wiki/API :red_circle:**
        :small_red_triangle_down:"access-token": null,
         :red_circle:**access token for API:red_circle:**
        :small_red_triangle_down:"id": null,
         :red_circle:**custom instance ID for API:red_circle:**
        :small_red_triangle_down:"worker-id": null,
         :red_circle:**custom worker-id for API:red_circle:**
        :small_red_triangle_down:"ipv6": false,
         :red_circle:**enable IPv6 support for API:red_circle:**
        :small_red_triangle_down:"restricted": true
         :red_circle:**enable full remote access (only if API token set):red_circle:**
    },
    :small_red_triangle_down:"asm": true,
     :red_circle:**ASM code for cn/2, possible values: auto, none, intel, ryzen.:red_circle:**
    :small_red_triangle_down:"autosave": true,
     :red_circle:**miner will override config file with suggested settings in advanced format for easy tuning:red_circle:**
    :small_red_triangle_down:"av": 0,
     :red_circle:**algorithm variation, 0 auto select:red_circle:**
    :small_red_triangle_down:"background": false,
     :red_circle:**true to run the miner in the background:red_circle:**
    :small_red_triangle_down:"colors": true,
     :red_circle:**false to disable colored output:red_circle:**
    :small_red_triangle_down:"cpu-affinity": null,
     :red_circle:**set process affinity to CPU core(s), mask "0x3" for cores 0 and 1:red_circle:**
    :small_red_triangle_down:"cpu-priority": null,
     :red_circle:**set process priority (0 idle, 2 normal to 5 highest):red_circle:**
    :small_red_triangle_down:"donate-level": 5,
     :red_circle:**donate level, mininum 1%:red_circle:**
    :small_red_triangle_down:"huge-pages": true,
     :red_circle:**Windows it always fail, because of memory fragmentation and many other reasons.:red_circle:**
    :small_red_triangle_down:"hw-aes": null,
     :red_circle:**hw-aes works only in Advanced threads mode.:red_circle:**
    :small_red_triangle_down:"log-file": null,
     :red_circle:**log all output to a file, example: "c:/some/path/xmrig.log":red_circle:**
    :small_red_triangle_down:"max-cpu-usage": 75,
     :red_circle:**maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.:red_circle:**
    "pools": [
        {
            :small_red_triangle_down:"url": "donate.v2.xmrig.com:3333",
             :red_circle:**URL of mining server:red_circle:**
            :small_red_triangle_down:"user": "YOUR_WALLET_ADDRESS",
             :red_circle:**username for mining server:red_circle:**
            :small_red_triangle_down:"pass": "x",
             :red_circle:**password for mining server:red_circle:**
            :small_red_triangle_down:"rig-id": null,
             :red_circle:**rig identifier for pool-side statistics (needs pool support):red_circle:**
            :small_red_triangle_down:"nicehash": false,
             :red_circle:**enable nicehash/xmrig-proxy support:red_circle:**
            :small_red_triangle_down:"keepalive": false,
             :red_circle:**send keepalived for prevent timeout (need pool support):red_circle:**
            :small_red_triangle_down:"variant": -1,
             :red_circle:**algorithm PoW variant (0=auto, 1,2):red_circle:**
            :small_red_triangle_down:"tls": false,
             :red_circle:**TLS connection enable/disable (need pool support):red_circle:**
            :small_red_triangle_down:"tls-fingerprint": null
             :red_circle:**TLS connection fingerprint:red_circle:**
        }
    ],
    :small_red_triangle_down:"print-time": 60,
     :red_circle:**print hashrate report every N seconds (max 3600):red_circle:**
    :small_red_triangle_down:"retries": 5,
     :red_circle:**number of times to retry before switch to backup server:red_circle:**
    :small_red_triangle_down:"retry-pause": 5,
     :red_circle:**time to pause between retries:red_circle:**
    :small_red_triangle_down:"safe": false,
     :red_circle:**true to safe adjust threads and av settings for current CPU:red_circle:**
    :small_red_triangle_down:"threads": null,
     :red_circle:**number of miner threads ("all" max threads):red_circle:**
    :small_red_triangle_down:"user-agent": null,
     :red_circle:**set custom user-agent string for pool:red_circle:**
    :small_red_triangle_down:"syslog": false,
     :red_circle:**use system log for output messages:red_circle:**
    :small_red_triangle_down:"watch": false
     :red_circle:**i tink watch config.json change:red_circle:**
		:small_red_triangle_down:"threads": [
		:red_circle:***low_power_mode* number between 1 and 5 or boolean, false equal to 1 and true equal to 2.:red_circle:**
		:red_circle:**When set to a number N greater than 1, this mode will increase the cache:red_circle:**
		:red_circle:**usage and single thread performance by N times. *affine_to_cpu* This can be either false :red_circle:**
		:red_circle:**(no affinity), or the CPU core number.:red_circle:**
        {"low_power_mode": true,  "affine_to_cpu": 0 }, 
        {"low_power_mode": false, "affine_to_cpu": 1 },
        {"low_power_mode": 1,     "affine_to_cpu": 2 }, 
        {"low_power_mode": 3,     "affine_to_cpu": false } 
]

}`

## snipeTR | 2018-10-16T11:10:19+00:00
{
    "algo": "cryptonight",:arrow_right:**specify the algorithm to use cryptonight cryptonight-lite cryptonight-heavy**
    "api": { 
        "port": 0,:arrow_right:**port for the miner API https://github.com/xmrig/xmrig/wiki/API**
        "access-token": null,:arrow_right:**access token for API**
        "id": null,:arrow_right:**custom instance ID for API**
        "worker-id": null,:arrow_right:**custom worker-id for API**
        "ipv6": false,:arrow_right:**enable IPv6 support for API**
        "restricted": true:arrow_right:**enable full remote access (only if API token set)**
    },
    "asm": true,:arrow_right:**ASM code for cn/2, possible values: auto, none, intel, ryzen.**
    "autosave": true,:arrow_right:**miner will override config file with suggested settings in advanced format for easy tuning**
    "av": 0,:arrow_right:**algorithm variation, 0 auto select**
    "background": false,:arrow_right:**true to run the miner in the background**
    "colors": true,:arrow_right:**false to disable colored output**
    "cpu-affinity": null,:arrow_right:**set process affinity to CPU core(s), mask "0x3" for cores 0 and 1**
    "cpu-priority": null,:arrow_right:**set process priority (0 idle, 2 normal to 5 highest)**
    "donate-level": 5,:arrow_right:**donate level, mininum 1%**
    "huge-pages": true,:arrow_right:**Windows it always fail, because of memory fragmentation and many other reasons.**
    "hw-aes": null,:arrow_right:**hw-aes works only in Advanced threads mode.**
    "log-file": null,:arrow_right:**log all output to a file, example: "c:/some/path/xmrig.log"**
    "max-cpu-usage": 75,:arrow_right:**maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.**
    "pools": [
        {
            "url": "donate.v2.xmrig.com:3333",:arrow_right:**URL of mining server**
            "user": "YOUR_WALLET_ADDRESS",:arrow_right:**username for mining server**
            "pass": "x",:arrow_right:**password for mining server**
            "rig-id": null,
            "nicehash": false,:arrow_right:**enable nicehash/xmrig-proxy support**
            "keepalive": false,:arrow_right:**send keepalived for prevent timeout (need pool support)**
            "variant": -1,:arrow_right:**algorithm PoW variant (0=auto, 1,2)**
            "tls": false,:arrow_right:**TLS connection enable/disable (need pool support)**
            "tls-fingerprint": null:arrow_right:**TLS connection fingerprint**
        }
    ],
    "print-time": 60,:arrow_right:**print hashrate report every N seconds (max 3600)**
    "retries": 5,:arrow_right:**number of times to retry before switch to backup server**
    "retry-pause": 5,:arrow_right:**time to pause between retries**
    "safe": false,:arrow_right:**true to safe adjust threads and av settings for current CPU**
    "threads": null,:arrow_right:**number of miner threads ("all" max threads)**
    "user-agent": null,:arrow_right:**set custom user-agent string for pool**
    "syslog": false,:arrow_right:**use system log for output messages**
    "watch": false:arrow_right:**i tink watch config.json change**
		"threads": [
		:arrow_right:***low_power_mode* number between 1 and 5 or boolean, false equal to 1 and true equal to 2.**
		:arrow_right:**When set to a number N greater than 1, this mode will increase the cache**
		:arrow_right:**usage and single thread performance by N times. *affine_to_cpu* This can be either false:arrow_right:**
		:arrow_right:**(no affinity), or the CPU core number.**
        {"low_power_mode": true,  "affine_to_cpu": 0 },
        {"low_power_mode": false, "affine_to_cpu": 1 },
        {"low_power_mode": 1,     "affine_to_cpu": 2 },
        {"low_power_mode": 3,     "affine_to_cpu": false }
]
}

## 2010phenix | 2018-10-17T11:38:01+00:00
snipeTR, make patch or pull request ;)

## snipeTR | 2020-06-08T09:55:59+00:00
review

## snipeTR | 2020-09-11T20:27:47+00:00
review

## Technetium1 | 2021-02-20T06:32:18+00:00
@snipeTR this seems sufficiently covered by https://github.com/xmrig/xmrig/commit/f302b4b0ef2ba9d6052bab50fe238210eeb204b6

## xmrig | 2021-02-20T06:48:09+00:00
Documentation for all config options is almost done https://xmrig.com/docs/miner/config 

# Action History
- Created by: snipeTR | 2018-10-15T18:14:31+00:00
- Closed at: 2021-04-12T15:58:44+00:00
