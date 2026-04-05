---
title: 4x CPU AMD 6380 - Mine on 56 instead of 64 cores
source_url: https://github.com/xmrig/xmrig/issues/1349
author: floriangrousset
assignees: []
labels:
- randomx
created_at: '2019-12-01T01:46:59+00:00'
updated_at: '2021-04-12T15:16:13+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:16:13+00:00'
---

# Original Description
I'm running xmrig with basic standard configuration just for the pool and the wallet on a freshly installed Linux 16.04 LTS. It mine and work fine except that it only runs on 56 of the 64 total cores of the system. See on the following screenshot stating:
`rx   init datasets algo rx/0 (64 threads)`
But then later:
`cpu  use profile  rx  (56 threads) scratchpad 2048 KB`
`cpu  READY threads 56/56 (56) huge pages 0% 0/56 memory 114688 KB`

It's a Blade server BL685C G7 with 4x AMD 6380 so 16 cores x4 = total 64 cores.
I have 2 systems installed the exact same way and this is experienced on both systems.
Any idea on what to test? I can compile with specific flags or anything else if needed to diagnose.
Thanks.

<img width="1168" alt="Screen Shot 2019-11-30 at 7 39 20 PM" src="https://user-images.githubusercontent.com/2507085/69908143-6b5ed800-13a9-11ea-8285-e89b8e88007b.png">


# Discussion History
## xmrig | 2019-12-01T02:02:14+00:00
These Opterons always pain, 56 threads comes from cache size `64 + 48 / 2`, according CPU specification should be 64 MB total L3 cache, but system reports only 48 MB and it pretty common for these CPUs.

Also you need reserve 10000 hugepages.
Thank you.

## xmrig | 2019-12-01T12:23:43+00:00
Please check this link https://forums.anandtech.com/threads/how-to-disable-ht-assist-on-opteron-6200-series.2552739/ after whole L3 available, need to remove current 56 threads configuration to allow miner create new 64 threads.
Thank you.

## floriangrousset | 2019-12-01T18:46:31+00:00
Thanks a lot for the prompt reply @xmrig.

First, changing the hugepage from the 128 default to 10000 changed a lot, now mining at 10700H/s and I don't have the memory allocation error message anymore.

`root@Blade5:~# cat /proc/meminfo | grep HugePages_Total`
`HugePages_Total:     128`
`root@Blade5:~# sudo sysctl -w vm.nr_hugepages=10000`
`vm.nr_hugepages = 10000`
`root@Blade5:~# cat /proc/meminfo | grep HugePages_Total`
`HugePages_Total:   10000`

Now on the HyperTransport bit, I'm struggling more. I found some documentation explaining what it is on the AMD processors, eg https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-c02160131

<img width="677" alt="HyperTransport" src="https://user-images.githubusercontent.com/2507085/69918476-1322e700-1438-11ea-9ac6-0b6aab559fe5.png">

I was hoping to see a HT or Probe reference in the BIOS of the server but unfortunately didn't find anything. I'm on the latest A20 revision of the HP ProLiant BIOS for the BL685c G7.

The closest enough menu I found is the one on the screenshot below.

<img width="1090" alt="BIOS" src="https://user-images.githubusercontent.com/2507085/69918443-a9a2d880-1437-11ea-8aaa-6b132c784065.png">

Any help from anyone who had already disabled the HyperTransport on an AMD processor? Maybe some tool to run from Linux after boot to turn HT off? Any idea welcome! Thanks.


## kio3i0j9024vkoenio | 2019-12-04T03:13:44+00:00
HT-Assist takes 2MB of L3 Cache per Numa Node. Thus you will lose 4MB of the 16MB L3 Cache per 62xx/63xx 16-core Opteron. So rather than having 64MB of L3 Cache on your 4x 6380 Opterons you end up with only the 48MB that you are seeing.

On Dell R815 Servers there is an option to disable "HT Assist" and regain the lost 16 MB L3 cache.

On Supermicro Servers there is no option to disable "HT Assist" so those will servers also lose 4MB L3 Cache per Opteron.

As for your HP Server look under the Processor Options to see if there is an option to disable "HT Assist".

## floriangrousset | 2019-12-04T14:46:14+00:00
Thank you @kio3i0j9024vkoenio for the clarification.
 After checking, I don't see anything to be able to disable HT-Assist in the HP BIOS I'm on, even tho it's the latest version.
I'll keep looking for what I can find. Thanks for the help.


## kio3i0j9024vkoenio | 2019-12-04T14:52:34+00:00
After much searching myself I too am at the conclusion that HP (along with SuperMicro) do not have options to disable "HT-Assist".

It seems that Dell is the only vendor that allows the user to disable "HT-Assist"

## floriangrousset | 2019-12-04T21:50:24+00:00
Yeah I didn't find anything neither. That's highly frustrating considering I have a 8 blades x 4 CPU x supposedly 16 cores. I'll have only 448 cores left working with xmrig instead of the 512 available. I'll have to live with that, or rewrite a BIOS/find a custom legit one that has HT-Assist. Anyways... Thanks again for your feedback.

## floriangrousset | 2019-12-05T15:02:57+00:00
Update: an HPE support ticket advice to update the System ROM BIOS to a version after Dec 2012. https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-c03700733

> System ROM revisions prior to December 2012 do not include the portion of the L3 cache used for AMD HT Assist when reporting the L3 Cache size. For example, an HP ProLiant DL385p Gen8 server with an AMD Opteron series 6200 or 6300 processor will indicate there is 12MB of L3 cache when the processor actually contains 16MB.

> This is only a reporting issue and has no impact on the operation of the server. The processor is properly enabled to use all L3 cache. If there is a concern about the amount of cache reported, update to a System ROM version dated December 2012 (or later). System ROM revisions dated December 2012 and later will always indicate the amount of L3 cache available on the processor.

Unfortunately, still bad luck here as that just fixes reporting/displaying of the 16MB on each CPU on the BIOS screen. It's not a solution for disabling HT-Assist from the HP BIOS. I'm still looking for a solution.

# Action History
- Created by: floriangrousset | 2019-12-01T01:46:59+00:00
- Closed at: 2021-04-12T15:16:13+00:00
