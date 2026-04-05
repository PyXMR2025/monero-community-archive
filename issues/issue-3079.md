---
title: '"unknown node or service"'
source_url: https://github.com/xmrig/xmrig/issues/3079
author: swaggerooni
assignees: []
labels: []
created_at: '2022-06-27T22:26:01+00:00'
updated_at: '2025-06-20T11:03:07+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:03:07+00:00'
---

# Original Description
There's a found called 'start.cmd' that has my wallet address on it, went I click on it, it shows this error 
![Screenshot 2022-06-27 231808](https://user-images.githubusercontent.com/42319486/176045817-39922c93-2778-46e9-a915-1fef066f40ca.png)

When I try to mine in feather wallet it says this (im a noob pls help)
![Screenshot 2022-06-27 232040](https://user-images.githubusercontent.com/42319486/176045921-a6cbd49e-b47f-4b18-b7af-6ac910ac11c7.png)


# Discussion History
## SChernykh | 2022-06-28T08:34:42+00:00
`node.xmr.to` probably doesn't work anymore. As for the second error, check that your xmrig folder is in antivirus exceptions.

## swaggerooni | 2022-06-28T10:33:42+00:00
I changed to 127.0.0.1 and it says "connection refused"

![image](https://user-images.githubusercontent.com/42319486/176157261-4141016c-69fb-4750-a76c-c1cc348827fc.png)

put folder in exceptions and it still happens 
![image](https://user-images.githubusercontent.com/42319486/176158094-90a16ee7-959e-41fb-87ee-63cbb4597821.png)

![image](https://user-images.githubusercontent.com/42319486/176158371-6b61856a-7017-4d75-8802-0032b5f10397.png)



## SChernykh | 2022-06-28T10:38:56+00:00
Do you run your Monero node locally? You can only get connection refused if it's not running.

## swaggerooni | 2022-06-28T10:43:50+00:00
I have no idea

It's also saying this 
![image](https://user-images.githubusercontent.com/42319486/176159829-b3f34569-d78e-4218-b204-acd0e3b38f0b.png)


## SChernykh | 2022-06-28T10:48:16+00:00
Your xmrig command line in feather wallet is incorrect. When you connect to 127.0.0.1:18081 it's solo mining, so you must have `--daemon` in the command line and you need to remove `--tls`.

## swaggerooni | 2022-06-28T10:54:11+00:00
I already did

![image](https://user-images.githubusercontent.com/42319486/176162083-80d4ba5d-00c6-4621-85c1-44836f5159c5.png)


## AaronLG3249 | 2024-10-01T11:08:11+00:00
```
oem@AaronLG-750TDA:~$ xmrig
 * ABOUT        XMRig/6.21.1 gcc/13.2.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.48.0 OpenSSL/3.0.13 hwloc/2.10.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz (1) 64-bit AES
                L2:5.0 MB L3:12.0 MB 4C/8T NUMA:1...
 * MEMORY       4.3/15.3 GB (28%)
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      ### **donate.v2.xmrig.com:5555 algo auto**
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-10-01 06:40:14.378]  net      donate.v2.xmrig.com:5555 DNS error: "unknown node or service"
[2024-10-01 06:40:16.378]  net      donate.v2.xmrig.com:5555 DNS error: "unknown node or service"
```

im mining through a proxy server--192.0.0.1:8000 or DIRECT-76-SM-A136U-PdaNet:8000@192.0.0.1---

neither json files has the donate.v2.xmrig.com:5555 urls in them........so why even try to connect????

```
{
        
       "id": "XMRig",
        "worker-id": "AaronLG3249",=wallet_address",
          
    "http": "192.0.0.1",
        "enabled": true,
        "host": "192.0.0.1",
        "port": "8000",
        "access-token": null,
        "restricted": true,
        "autosave": true,
        "background": true,
        "colors": true,
        "title": true,

    "autosave": true,
            
            "algo": "kawpow",
            "url": "stratum.ravenminer.com:3838",
            "user": "wallet_address",
            "pass": "x",
            "tls": false,
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": true,
        "hw-aes": true,
        "priority": 1,
        "memory-pool": true,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 4, 1, 5, 2, 6, 3, 7],
        "cn": [[1, 0], [1, 1], [1, 2], [1, 3], [1, 6], [1, 7]],
        "cn-heavy": [[1, 0], [1, 1], [1, 2]],
        "cn-lite": [[1, 0], [1, 4], [1, 1], [1, 5], [1, 2], [1, 6], [1, 3], [1, 7]],
        "cn-pico": [[2, 0], [2, 4], [2, 1], [2, 5], [2, 2], [2, 6], [2, 3], [2, 7]],
        "cn/upx2": [[2, 0], [2, 4], [2, 1], [2, 5], [2, 2], [2, 6], [2, 3], [2, 7]],
        "ghostrider": [[8, 0], [8, 1], [8, 2], [8, 3]],
        "rx": [0, 1, 2, 3, 6, 7],
        "rx/wow": [0, 4, 1, 5, 2, 6, 3, 7],
        "cn-lite/0": true,
        "cn/0": true,
        "rx/arq": true,
        "rx/keva": true,
         "rx/row": true,
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
    },  "log-file": true,
"pool_list": [
    {
        "pool_address": "fastpool.xyz:10056",
        "wallet_address": ,
        "rig_id": "AaronLG3249",
        "pool_password": "x",
        "use_nicehash": false,
        "use_tls": true,
        "tls_fingerprint": "",
        "pool_weight": 1
    },
],
"currency": "monero",
            "algo": "RandomX",
            "url": "fastpool.xyz:10056",
            "user": "wallet_address",
            "pass": null,
            "tls": false,
            "keepalive": true,
            "nicehash": true,

     "enabled": true,
        "tls": true,
     "sni": false,
       "tls-fingerprint": null,
        "daemon": false,
         "socks5": "192.168.49.1",
          "self-select": null,
           "submit-to-origin": false,
                  
            "algo": "ghostrider",
            "coin": "XMR",
            "url": "fastpool.xyz",
            "port": "10056",
            "user": "wallet_address",
            "pass": null,
            "rig-id": "AaronLG3249",
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": "192.168.49.1",
            "self-select": null,
            "submit-to-origin": false,
         
            "algo": "cn-pico",
            "coin": "XMR",
            "url": "fastpool.xyz",
            "port": "1056",
            "user": "wallet_address",
            "pass": null,
            "rig-id": "AaronLG3249",
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": "192.168.49.1",
            "self-select": null,
            "submit-to-origin": false,
        
            "algo": "argon2",
            "coin": "XMR",
            "url": "fastpool.xyz",
            "port": "10056",
            "user": "wallet_address",
            "pass": null,
            "rig-id": "AaronLG3249",
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": "192.168.49.1",
            "self-select": null,
            "submit-to-origin": false,
        
            "algo": "rx/wow",
            "coin": "XMR",
            "url": "fastpool.xyx",
            "port": "10056",
            "user": "wallet_address",
            "pass": null,
            "rig-id": "AaronLG3249",
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": "192.168.49.1",
            "self-select": null,
            "submit-to-origin": false,
        
            "algo": "cn-heavy",
            "coin": "XMR",
            "url": "fastpool.xyx",
            "port": "10056",
            "user": "wallet_address",
            "pass": null,
            "rig-id": "AaronLG3249",
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": "19.1668.49.1",
            "self-select": null,
            "submit-to-origin": false,
        
            "algo": "cn/upx2",
            "coin": "XMR",
            "url": "fastpool,xyz",
            "port": "10056",
            "user": "wallet_address",
            "pass": null,
            "rig-id": "AaronLG3249",
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": "192.168.449.1",
            "self-select": null,
            "submit-to-origin": false,
        
            "algo": "rx/0",
            "coin": "XMR",
            "url": "fastpool.xyz",
            "port": "10056",
            "user": "wallet_address",
            "pass": null,
            "rig-id": "AaronLG3249",
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": "192.168.49.1",
            "self-select": null,
            "submit-to-origin": false,
        
            "algo": "cn",
            "coin": "XMR",
            "url": "fastpool.xyz",
            "port": "10056",
            "user": "wallet_address",
            "pass": null,
            "rig-id": "AaronLG3249",
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": "192.168.49.1",
            "self-select": null,
            "submit-to-origin": false,
        
            "algo": "ghostrider",
            "coin": "XMR",
            "url": "fastpool.xyz",
            "port": "10056",
            "user": "wallet_address",
            "pass": null,
            "rig-id": "AaronLG3249",
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": "192.168.49.1",
            "self-select": null,
            "submit-to-origin": false,
        

    "retries": 10,
    "retry-pause": 10,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": true,
  
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null,
    },
    "dns": {
        "ipv6": false,
        "ttl": 30,
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
```
json ip=
2600:387:15:321c::3
port=64154
host=2600:387:15:321c::3
public=
Ipv4=12.75.226.67
iPv6=2600:387:15:321c::3

too many ip's and ports options i use an app on my android for bootleg hotspot, which make it a proxy server, that hides usage from carrier.....
 i have 11th gen Intel  i7  multicore
Intel Corporation TigerLake-LP GT2 [Iris Xe Graphics]
Intel Corporation DG1 [Iris Xe MAX Graphics]
no amd or any opencl or cuda compatible-----cpu only

-----im new to this so whats the issue please??????

# Action History
- Created by: swaggerooni | 2022-06-27T22:26:01+00:00
- Closed at: 2025-06-20T11:03:07+00:00
