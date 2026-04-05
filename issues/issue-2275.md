---
title: '"OPENCL       disabled (selected OpenCL platform NOT found)"'
source_url: https://github.com/xmrig/xmrig/issues/2275
author: lpgsaxd
assignees: []
labels: []
created_at: '2021-04-17T00:26:59+00:00'
updated_at: '2021-05-13T14:06:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Can't run with opencl
**Required data**
 - Miner log as text or screenshot
 "./xmrig -o monerohash.com:2222 -u wallet -k --opencl-devices 0 --opencl-loader libOpenCL.so --opencl-platform PowerVR Rogue"
or
"./xmrig -o monerohash.com:2222 -u wallet -k --opencl-devices 0 --opencl-loader libOpenCL.so --opencl-platform 'PowerVR Rogue' "
 - OS: android 10
 GPU PowerVR Rogue
![Screenshot_20210417-021841](https://user-images.githubusercontent.com/82686008/115096123-3282bd00-9f24-11eb-8dec-596c37af4664.png)
![Screenshot_20210417-022004](https://user-images.githubusercontent.com/82686008/115096139-3c0c2500-9f24-11eb-8ddb-0204a356279e.png)




# Discussion History
## Spudz76 | 2021-04-17T11:42:28+00:00
It substring searches the "Vendor" not the "Platform" string and it is case-sensitive.  So try `--opencl-platform=Imagination`

## lpgsaxd | 2021-04-17T13:47:25+00:00
> It substring searches the "Vendor" not the "Platform" string and it is case-sensitive. So try `--opencl-platform=Imagination`

Thanks
Now xmrig detects cpu, but now i have:
"opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 2181038080"
and Segmentation fault.


## Spudz76 | 2021-04-19T09:13:01+00:00
For RandomX algo family, the GPU must have more than 2GB memory...

## SChernykh | 2021-04-19T09:16:54+00:00
There's a `dataset_host` parameter available in config.json to enable mining on GPUs with <= 2GB memory, but running RandomX on a GPU is useless, especially on a weak mobile phone GPU.

## lpgsaxd | 2021-04-19T10:22:19+00:00
> There's a `dataset_host` parameter available in config.json to enable mining on GPUs with <= 2GB memory, but running RandomX on a GPU is useless, especially on a weak mobile phone GPU.

![Screenshot_20210419-122052](https://user-images.githubusercontent.com/82686008/115221332-d6798d80-a109-11eb-9f71-74beb39056c5.png)
![Screenshot_20210419-122107](https://user-images.githubusercontent.com/82686008/115221349-da0d1480-a109-11eb-87e7-c842c07dcc8e.png)
Doesn't work.

## clflush | 2021-04-24T14:04:06+00:00
better off using your opencl on other algos (not RandomX). 

## Saikatsaha1996 | 2021-05-13T14:06:08+00:00
![Screenshot_2021-05-13-19-34-38-654_com miui gallery](https://user-images.githubusercontent.com/72664192/118137058-64534a80-b422-11eb-88a0-fa59b3669287.jpg)
I am also got same error any solution for this ?..
Help me..

# Action History
- Created by: lpgsaxd | 2021-04-17T00:26:59+00:00
