---
title: config.json is mangling cpu only entries for rx/arq rx/wow on first run
source_url: https://github.com/xmrig/xmrig/issues/1574
author: mechanator
assignees: []
labels: []
created_at: '2020-03-03T05:24:11+00:00'
updated_at: '2020-08-29T04:51:47+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:51:47+00:00'
---

# Original Description
**Describe the bug**
Upon running xmrig with the stock, default config.json supplied the cpu thread determiner runs and changes the entries for the number of threads guessed.  The entries for algorithms rx/arq and rx/wow are changed.  It doesn't look like any threads are allocated an does not comply with json format. It is unknown how the miner application keeps on running anyway. 
If a user wants to add threads or configure the number, they have to manually edit the entire entry. 
This leads to numerous end user support calls and confusion since most miners are not experts in JSON format.  

**To Reproduce**
Unzip windows version of any flavor from version 5.1 onward. Run the application once. with the default config.json supplied.  Examine changes in config.json

**Expected behavior**
The estimate number of threads for rx/arq and rx/wow would be entered and formatted correctly in the config.json.  Also taking into account the scratchpad size of the rx/rq algo in respect to the  cpu in cache determines the number of the threads, cores, to assign.  Currently the number of threads is set to ? 

**Required data**
 - Miner log as text or screenshot. attached. shows result of json file changed with first tun of cpu only mining. Nothing to do with gpu config selected.
 - Config file or command line (without wallets)
 - OS: Windows 10. mvsc build or cuda build same result


![mangledconfigjson](https://user-images.githubusercontent.com/40085316/75745290-bdc2d400-5ccb-11ea-8056-79c9a976ea41.jpg)
[config.zip](https://github.com/xmrig/xmrig/files/4279370/config.zip)
mangled after first run with no editing of it.



# Discussion History
## mechanator | 2020-03-03T05:37:04+00:00
Also, the number of threads ran as default of 4 since the entry is wrong, is not representative of the 256KB cache scratchpad size. The miner application doesn't determine the number of threads/cores divided into the amount of cache available.
So for example a 6 core intel with 12 mb cache and 2 threads per core will nor be optimally used.
Or a Ryzen with 16 or 32 cores and ample enough cache size to double the number of threads.


## 382663 | 2020-03-04T23:47:37+00:00
xmrig -o pool.minexmr.com:4444 -u 47wcnDjCDdjATivqH9GjC92jH9Vng7LCBMMxFmTV1Ybf5227MXhyD2gXynLUa9zrh5aPMAnu5npeQ2tLy8Z4pH7461vk6uo

## Spudz76 | 2020-03-21T21:45:06+00:00
Looks fine, I don't see a problem?

using a string containing another name is just a link/reference to whatever `rx/wow` is set for, so `rx/arq` is using `[0,1,2,3]`

RandomX isn't as simple to size as CN was.  It scales based on L3/L2/L1 sizes not just total cache or number of cores, and will always leave some cores unused depending on how the CPU is wired (according to hwloc).

# Action History
- Created by: mechanator | 2020-03-03T05:24:11+00:00
- Closed at: 2020-08-29T04:51:47+00:00
