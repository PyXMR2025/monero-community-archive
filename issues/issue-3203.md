---
title: XMRig doesnt mine with GPU. It displays N/A on first attempt and in second
  try, it cant find any opencl platform
source_url: https://github.com/xmrig/xmrig/issues/3203
author: ghost
assignees: []
labels: []
created_at: '2023-01-29T08:46:36+00:00'
updated_at: '2023-01-29T11:09:37+00:00'
type: issue
status: closed
closed_at: '2023-01-29T11:09:37+00:00'
---

# Original Description
**Describe the bug**
So
![image](https://user-images.githubusercontent.com/118899053/215314794-17f68987-c778-4180-8830-fd53cb03e191.png)
![image](https://user-images.githubusercontent.com/118899053/215314813-6bef6ce0-3b59-4b7b-bafa-af45dee6d13d.png)
As you can see, `[2023-01-29 08:13:15.763]  opencl   READY threads 2/2 (92455 ms)` occurs after pressing Ctrl + C. I thought at first I didnt wait enough so I rebooted and tried it again and again opencl READY threads i got after Ctrl +C.. When I try running xmrig again without rebooting.
The second try after Ctrl +C ing the first one always gives It fails to detect opencl on second try ` * OPENCL       disabled (no devices)`.
```
 * OPENCL       disabled (no devices)
 * CUDA         disabled
[2023-01-29 08:21:24.087]  net      xmrig.nanswap.com:3333 incompatible/disabled algorithm "rx/0" detected, reconnect
[2023-01-29 08:21:24.087]  net      xmrig.nanswap.com:3333 login error code: 6
[2023-01-29 08:21:29.325]  signal   Ctrl+C received, exiting
``` 
I tried using xmrig-amd 2.1 directly too but unfortunately it freezes for some reason

**To Reproduce**
I had dual boot kali-linux (debian based) and windows. I have only 6GB RAM, so I tried using kali linux to mine using GPU. Unfortunately, it runs out of memory and when I try to limit memory use so it doesnt freeze, it gets killed by OOM. So last night I downloaded Ubuntu Server 22.04 which consumes even less memory compared to GUI based linux. 
1) Downloaded and installed Ubuntu 22.04 (Triple boot)
2) It couldn't detect opencl and when I used xmrig-amd I found out there was no libOpencl.so therefore I followed these steps:
- apt install ocl-icd-opencl-dev and apt install opencl-headers
- add-apt-repository ppa:oibaf/graphics-drivers and apt update && apt full-upgrade -y
After this two install, xmrig-amd progressed but showed another error called clGetPlatformWorkers or something. Then I installed amdgpu-pro of 300MB using a script and finally everything started. Unfortunately I am getting N/A instead of H/s which I believe is due to GPU not being utilized at all rather than GPU power being too low.

**Expected behavior**
it shouldnt display N/A and display hashes

**Required data**
 - Miner log as text or screenshot: Already
 - Config file or command line (without wallets): `./xmrig -o xmrig.nanswap.com:3333 -a rx -k -u nano_1offh1u8yc7njsox3qqdjqfhdk3kf8tug5rfq8esipc1jbxhcuutdk3fxny6 -p x --opencl --no-cpu`
 - OS: Ubuntu
 - For GPU related issues: Not sure how to get this

**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2023-01-29T09:06:35+00:00
Need 2336+256MB+256MB = 2848MB GPU memory and you have 2484MB.

RandomX is designed to be terrible on GPUs, especially integrated video, it is only supported to prove it's slow.

You could try finding `"opencl"->"rx"->"dataset_host"` item in `config.json` and set it `true`, so that it shares the system RAM 2336MB dataset, but it will be even slower.

## ghost | 2023-01-29T09:21:08+00:00
Hmm it's still showing N/A despite setting dataset host to true. Opencl ready threads 2/2 is shown earlier though which wasn't the case earlier.  @Spudz76 

## SChernykh | 2023-01-29T09:28:40+00:00
> I tried using kali linux to mine using GPU

Big mistake. AMD drivers for Linux suck, try to do it on Windows. It will probably work with `dataset_host` if you use AMD Windows drivers from 2019-2020, and you will probably see 1-2 h/s hashrate. Don't mine RandomX with GPU.

## ghost | 2023-01-29T09:51:06+00:00
![image](https://user-images.githubusercontent.com/118899053/215318464-0b26dc19-56ac-46df-a786-755bd4ef79d1.png)
Looks like windows doesnt work well too @SChernykh 
It seems there is some problem with my GPU probably

## SChernykh | 2023-01-29T10:03:11+00:00
What did I tell you? AMD drivers from 2019-2020. And definitely not Windows 11.

## SChernykh | 2023-01-29T10:05:24+00:00
You can also try to set `"gcn_asm":false," in config.json, next to `dataset_host`

## SChernykh | 2023-01-29T10:19:20+00:00
As you can see, it can mine on AMD integrated GPU with the right drivers and on Windows 10. It's even the same GFX902 (Vega 8) as in your system.
![image](https://user-images.githubusercontent.com/15806605/215319721-a6c5e2c5-8712-463e-9afd-04957145a709.png)


# Action History
- Created by: ghost | 2023-01-29T08:46:36+00:00
- Closed at: 2023-01-29T11:09:37+00:00
