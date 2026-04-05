---
title: Is possible to include config when build?
source_url: https://github.com/xmrig/xmrig/issues/957
author: MasterDeflate
assignees:
- xmrig
labels:
- enhancement
created_at: '2019-02-27T21:18:53+00:00'
updated_at: '2026-01-22T05:17:45+00:00'
type: issue
status: closed
closed_at: '2019-03-06T13:24:02+00:00'
---

# Original Description
Is possible to build it with config inside without using the external config.json?

# Discussion History
## MasterDeflate | 2019-02-27T21:47:08+00:00
I change the m_pools.push_back inside of src at Pools.cpp but it still ask for config.json


## Meyer01 | 2019-02-28T04:58:56+00:00
It's possible. Look how it done in previous versions in https://github.com/RansomFuck/MODRIG for example. Insert command line args inside code.


## MasterDeflate | 2019-02-28T18:49:52+00:00
@Meyer01 if you know how to do it why not explain which files need to be changed? I check this link which you gived me, but its configured for Windows that one, also im trying this on Linux, and this version is older so the new one has  other stuf, i tried using only Pools.cpp at src/base/net/ i put my config but after compile it ask for the config file? can you give me explaination which files do i need and what to change to not ask for config and just use my wallet+pool inside of it?

Example i used Pools.cpp in this way:
xmrig::Pool &xmrig::Pools::current()
{
    if (m_data.empty()) {
m_data.push_back(Pool("pool", 3333, "wallet", "x"));
    }

    return m_data.back();
}

## Meyer01 | 2019-03-01T10:32:53+00:00
xmrig.cpp

Use argv to insert command line options. Thats all



## Meyer01 | 2019-03-01T19:54:39+00:00
http://www.cplusplus.com/articles/DEN36Up4/    read this to better undrestanding argc and argv
And after that look to the link i give you before
https://github.com/RansomFuck/MODRIG/blob/master/src/xmrig.cpp
206    static char * dreams[] = { frst, scnd, urejds, mkdjd, mkwei3 };
207    App FUcker(5, dreams);

In that example argc is 5 and argv is "frst, scnd, urejds, mkdjd, mkwei3"


## xmrig | 2019-03-02T06:21:42+00:00
This feature added to [dev](https://github.com/xmrig/xmrig/commits/dev) branch.

How to use:

1. Use cmake option `-DWITH_EMBEDDED_CONFIG=ON` to enable this feature.
2. Edit/replace config sample in code https://github.com/xmrig/xmrig/blob/master/src/core/config/Config_default.h#L31
3. Recompile the miner.

Please note embedded config used only if miner fails to load external configuration from file or command line.
Also fixed bug: `m_enabled` field was uninitialized in Pool class.

## xmrig | 2019-03-06T13:24:02+00:00
v2.14.0 released https://github.com/xmrig/xmrig/releases/tag/v2.14.0

## MasterDeflate | 2019-03-09T18:51:50+00:00
Nice this worked, btw is possible to add a worker name but to use random number or word something?

## Vip4pt | 2019-04-24T21:00:16+00:00
How to confuse the built-in configuration?

## cnecrea | 2021-12-23T00:34:13+00:00
> This feature added to [dev](https://github.com/xmrig/xmrig/commits/dev) branch.
> 
> How to use:
> 
> 1. Use cmake option `-DWITH_EMBEDDED_CONFIG=ON` to enable this feature.
> 2. Edit/replace config sample in code https://github.com/xmrig/xmrig/blob/master/src/core/config/Config_default.h#L31
> 3. Recompile the miner.
> 
> Please note embedded config used only if miner fails to load external configuration from file or command line. Also fixed bug: `m_enabled` field was uninitialized in Pool class.

Hi there,

I made this, it works but after I finish compile it, works fine but there are some lines that i want to make them disappear (ONLY LINES WITH "unable to open"):
```
root@xmr:~/xmrig# ./xmrig
[2021-12-23 00:33:21.427] unable to open "/root/xmrig/config.json".
[2021-12-23 00:33:21.428] unable to open "/root/.xmrig.json".
[2021-12-23 00:33:21.428] unable to open "/root/.config/xmrig.json".
* ABOUT        XMRig/6.16.2 gcc/10.2.1
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel Xeon Processor (Cascadelake) (1) 64-bit AES VM
                L2:8.0 MB L3:16.0 MB 2C/4T NUMA:1
 * MEMORY       3.8/7.8 GB (49%)


```

Can some one help me with this? Thanks!


--- later edit.

solved, thanks anyway!

## calojohn806 | 2023-11-17T07:39:00+00:00
how do you solve that

## Dingtaiqi | 2024-01-08T12:27:32+00:00
> how do you solve that

肯定是去删了对应的输出啊，虽然没什么用

## unixboris | 2025-10-14T13:26:04+00:00
> how do you solve that

Just comment this section:

        chain.addFile(Process::location(Process::DataLocation, "config.json"));
        if (read(chain, config)) {
            return config.release();
        }

        chain.addFile(Process::location(Process::HomeLocation,  "." APP_ID ".json"));
        if (read(chain, config)) {
            return config.release();
        }

        chain.addFile(Process::location(Process::HomeLocation, ".config" XMRIG_DIR_SEPARATOR APP_ID ".json"));
        if (read(chain, config)) {
            return config.release();
        }


in Base.cpp

## albertico123 | 2026-01-22T05:17:45+00:00
he is using ./xmrig simple without argument, how can i do this? i deleted output from Base.cpp and modified also Config_default.h but i cant reach to detele the arguments, i wish to make it simple as he did ./xmrig but at the moment i should use a fail argument to start the embedded, he starting it without argument or fail argument

# Action History
- Created by: MasterDeflate | 2019-02-27T21:18:53+00:00
- Closed at: 2019-03-06T13:24:02+00:00
