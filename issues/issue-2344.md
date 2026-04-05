---
title: Pools per backend
source_url: https://github.com/xmrig/xmrig/issues/2344
author: matheusbach
assignees: []
labels: []
created_at: '2021-05-04T18:46:30+00:00'
updated_at: '2021-12-04T13:38:41+00:00'
type: issue
status: closed
closed_at: '2021-12-04T13:38:41+00:00'
---

# Original Description
Currently the pools in the ```config.json``` file are used for all backends (cpu, cuda, opencl)
However, this limits the user to be able to mine only in one pool and one algorithm for all devices. As performance is different between algorithms and devices, it may be interesting to modify the software so that the user can define which pools are for each device.

We currently have something like:
```
{
[...]
   "cpu": {
       "enabled": true
       }
   },
   "opencl": {
       "enabled": false
   },
   "cuda": {
       "enabled": false
   },
   "pools": [
       {
           "algo": null,
           "coin": "monero",
           "url": "my_randomX_pool: port",
           "user": "pool_user",
           "enabled": true,
       },
       {
           another_pools
       },
 [...]
```
 
I suggest adding a new parameter in the pool, being like:
 
 ````
{
[...]
   "pools": [
       {
           "algo": null,
           "coin": "monero",
           "url": "my_randomX_pool: port",
           "user": "pool_user",
           "enabled": true,
           "backends": [cpu, cuda, amd]
       },
       {
           another_pools
       },
 [...]
````
 
 backends = null or [] (default) >> all backends selected
 backends = [cpu, opencl] >> only CPU and AMD GPUs will mine in this pool

# Discussion History
## Spudz76 | 2021-05-05T05:57:13+00:00
Run multiple xmrigs.

## matheusbach | 2021-12-02T12:24:08+00:00
> Run multiple xmrigs.

In addition to the worst organization, could this affect mining performance?


## Spudz76 | 2021-12-02T15:23:29+00:00
Best organization, since GPUs are entirely different than GPUs unless you're running the same algo.  Also when the GPU hangs or crashes out, it won't stop your CPU mining, because they are separate.  Same the other way around but the CPU backend rarely crashes.

No it doesn't unless you run the CPU one with priority 5 (aka nice -19) or something silly.  It's identical to if they were sharing one mainloop but two stratum loops and everything else.  The mainloop is light work so any apparent duplication of resources is not severe.

Set the GPU one with all the CPU speedups turned off then it doesn't need hugepages and all that, reducing the footprint on resources (none of that helps with GPU-only anyway).

# Action History
- Created by: matheusbach | 2021-05-04T18:46:30+00:00
- Closed at: 2021-12-04T13:38:41+00:00
