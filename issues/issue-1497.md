---
title: AMD Threadripper 2990WX only 10Kh/s and can only use 18 threads
source_url: https://github.com/xmrig/xmrig/issues/1497
author: PredatorOCX
assignees: []
labels: []
created_at: '2020-01-12T21:00:30+00:00'
updated_at: '2021-04-12T15:03:35+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:03:35+00:00'
---

# Original Description
Hi, i have been struggling with my setup but i cannot figure it out properly i guess, i saw a hashrate of 16 Kh/s over at monero benchmarks using a Threadripper 2990WX as the one i own, locked at 3 GHz

I cannot get past my hashrate above 10300 h/s no matter what i do, i saw it working once at 11000 h/s, but trying to improve i broke it down and never reached that performance again

i have tried with B-Die RAM up to 3200 Mhz, but it's even worse..

My main concern is that the xmrig (latest version - 5.5.0.) seems to works best with 18 threads, if i add anymore threads to the json config it will drop the hashrate, i tried everything i could figure out, i'm with tight timings from Rzyen Calculator already, but my guess is there must be something wrong in my JSON configuration

Any tip?   

# Discussion History
## PredatorOCX | 2020-01-12T21:14:29+00:00
my config

 "autosave": true,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 18],
            [1, 20],
            [1, 22],
            [1, 24],
            [1, 26],
            [1, 28],
            [1, 30],
            [1, 32],
            [1, 34],
            [1, 36],
            [1, 38],
            [1, 40],
            [1, 42],
            [1, 44],
            [1, 46],
            [1, 48],
            [1, 50],
            [1, 52],
            [1, 54],
            [1, 56],
            [1, 58],
            [1, 60],
            [1, 62]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 8],
            [1, 10],
            [1, 16],
            [1, 18],
            [1, 24],
            [1, 26],
            [1, 32],
            [1, 34],
            [1, 40],
            [1, 42],
            [1, 48],
            [1, 50],
            [1, 56],
            [1, 58]
        ],
        "cn-lite": [
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
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31]
            
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27],
            [2, 28],
            [2, 29],
            [2, 30]
            
        ],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow"

i think something in the cn-pico/heavy/etc might be worng? i changed the numbers in RX because i noticed that disabling SMT (using 32 cores/32 threads) in BIOS gave better results

## SChernykh | 2020-01-13T09:39:40+00:00
Is your Threadripper in Creator mode of Gaming mode? You need to switch to Creator mode.

## PredatorOCX | 2020-01-13T11:41:27+00:00
Yes, thank you for your reply
It is already under creator mode with Ryzen Master, i forgot to mention that

## PredatorOCX | 2020-01-14T13:10:02+00:00
Well somehow i'm pulling 18 Kh/s now :)

I played a little bit with the config file, removed the cn/lite/pico/heavy "extra threads" , then added from 0 to 31 cores on "rx" and all of a sudden i'm mining at 18 Kh/s, i won't touch anything else xD

I noticed it likes the more RAM the better? i'm using right now 64 GB of RAM 84x 16 GB sticks with dual rank) , even though they are not great performers and maxing out at 2800 MHz CAS 14, tightend with Ryzen Calculator.



## fontave | 2020-01-15T14:33:02+00:00
> Well somehow i'm pulling 18 Kh/s now :)
> 
> I played a little bit with the config file, removed the cn/lite/pico/heavy "extra threads" , then added from 0 to 31 cores on "rx" and all of a sudden i'm mining at 18 Kh/s, i won't touch anything else xD
> 
> I noticed it likes the more RAM the better? i'm using right now 64 GB of RAM 84x 16 GB sticks with dual rank) , even though they are not great performers and maxing out at 2800 MHz CAS 14, tightend with Ryzen Calculator.

Hi PredatorOCX
I Try to same option,but I  just get 12Kh/s, can you share config file to me,thank you very much~


## PredatorOCX | 2020-01-15T16:10:42+00:00

> Hi PredatorOCX
> I Try to same option,but I just get 12Kh/s, can you share config file to me,thank you very much~

Of course :)

Here you go

{
    "api": {
        "id": true,
        "worker-id": true
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
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 18],
            [1, 20],
            [1, 22],
            [1, 24],
            [1, 26],
            [1, 28],
            [1, 30],
            [1, 32],
            [1, 34]           
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 8],
            [1, 10],
            [1, 16],
            [1, 18],
            [1, 24],
            [1, 26],
            [1, 32],
            [1, 34],
            [1, 40],
            [1, 42],
            [1, 48],
            [1, 50],
            [1, 56],
            [1, 58]
        ],
        "cn-lite": [
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
            [1, 15],
            [1, 16],
            [1, 17]
                       
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17]
                       
        ],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD"
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "monero",
            "url": "xmr-eu1.nanopool.org:14444",
            "user": "---",
            "pass": "--@gmail.com",
            "rig-id": true,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "verbose": 0,
    "watch": true

## PredatorOCX | 2020-01-15T16:12:49+00:00
> 
> 
> > Well somehow i'm pulling 18 Kh/s now :)
> > I played a little bit with the config file, removed the cn/lite/pico/heavy "extra threads" , then added from 0 to 31 cores on "rx" and all of a sudden i'm mining at 18 Kh/s, i won't touch anything else xD
> > I noticed it likes the more RAM the better? i'm using right now 64 GB of RAM 84x 16 GB sticks with dual rank) , even though they are not great performers and maxing out at 2800 MHz CAS 14, tightend with Ryzen Calculator.
> 
> Hi PredatorOCX
> I Try to same option,but I just get 12Kh/s, can you share config file to me,thank you very much~

Also, bear in mind to DISABLE any option of 4G above in bios (cryptos), and for me disabling the SMT worked best, 32c / 32t

RAM is very important as well, frecuency and/or timings

## fontave | 2020-01-15T16:31:27+00:00
> > > Well somehow i'm pulling 18 Kh/s now :)
> > > I played a little bit with the config file, removed the cn/lite/pico/heavy "extra threads" , then added from 0 to 31 cores on "rx" and all of a sudden i'm mining at 18 Kh/s, i won't touch anything else xD
> > > I noticed it likes the more RAM the better? i'm using right now 64 GB of RAM 84x 16 GB sticks with dual rank) , even though they are not great performers and maxing out at 2800 MHz CAS 14, tightend with Ryzen Calculator.
> > 
> > 
> > Hi PredatorOCX
> > I Try to same option,but I just get 12Kh/s, can you share config file to me,thank you very much~
> 
> Also, bear in mind to DISABLE any option of 4G above in bios (cryptos), and for me disabling the SMT worked best, 32c / 32t
> 
> RAM is very important as well, frecuency and/or timings

got it ,thank you~

## PredatorOCX | 2020-01-15T16:36:50+00:00
> got it ,thank you~

You're welcome :)

Let us know if it works good for you


# Action History
- Created by: PredatorOCX | 2020-01-12T21:00:30+00:00
- Closed at: 2021-04-12T15:03:35+00:00
