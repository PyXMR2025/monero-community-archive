---
title: 'CPU warning: "can''t bind memory"'
source_url: https://github.com/xmrig/xmrig/issues/1226
author: kocimiros
assignees: []
labels: []
created_at: '2019-10-08T10:19:14+00:00'
updated_at: '2022-06-10T16:22:27+00:00'
type: issue
status: closed
closed_at: '2019-10-13T18:33:29+00:00'
---

# Original Description
Have this issue, when use first 4 cores (0,1,2,3) - everything is fine,
when I use 0,1,2,3,4,5,6,7 , first 4 are ok, but the rest has lower hashrate 


[2019-10-08 12:18:34.228] speed 10s/60s/15m 4236.1 n/a n/a H/s max 4236.3 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   599.2 |     n/a |     n/a |
|        1 |        1 |   599.5 |     n/a |     n/a |
|        2 |        2 |   580.4 |     n/a |     n/a |
|        3 |        3 |   599.5 |     n/a |     n/a |
|        4 |        4 |   464.5 |     n/a |     n/a |
|        5 |        5 |   464.5 |     n/a |     n/a |
|        6 |        6 |   464.4 |     n/a |     n/a |
|        7 |        7 |   463.9 |     n/a |     n/a |
|        - |        - |  4235.8 |     n/a |     n/a |
[2019-10-08 12:18:35.449] speed 10s/60s/15m 4235.8 n/a n/a H/s max 4236.7 H/s




INIT:

root@32-23:~/xmrig-4.2.1-beta# ./xmrig
 * ABOUT        XMRig/4.2.1-beta gcc/5.4.0
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * CPU          AMD Ryzen Threadripper 1900X 8-Core Processor (1) x64 AES
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:2
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      randomx-benchmark.xmrig.com:7777 coin monero
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
[2019-10-08 12:16:30.378] use pool randomx-benchmark.xmrig.com:7777  178.128.242.134
[2019-10-08 12:16:30.378] new job from randomx-benchmark.xmrig.com:7777 diff 2468369 algo rx/0 height 1317217
[2019-10-08 12:16:30.378]  rx   init dataset algo rx/0 (8 threads) seed 7732942c23511530...
[2019-10-08 12:16:30.383]  rx   #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-10-08 12:16:30.710]  rx   #0 allocate done huge pages 1168/1168 100% +JIT (332 ms)
[2019-10-08 12:16:35.965]  rx   #0 init done 1/1 (5586 ms)
[2019-10-08 12:16:35.965]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2019-10-08 12:16:35.993] CPU #04 warning: "can't bind memory"
[2019-10-08 12:16:35.993] CPU #05 warning: "can't bind memory"
[2019-10-08 12:16:35.993] CPU #07 warning: "can't bind memory"
[2019-10-08 12:16:35.993] CPU #06 warning: "can't bind memory"
[2019-10-08 12:16:35.994]  cpu  READY threads 8/8 (8) huge pages 8/8 100% memory 16384 KB (29 ms)


# Discussion History
## kocimiros | 2019-10-08T10:20:59+00:00
When I used indexes {0,1,2,3,8,9,10,11} from topology.xml,, there was no error CPU WARNING, but hashrate dropped to 1480h/s

I also tried to disable numa, didn't help



## xmrig | 2019-10-08T12:57:09+00:00
Please share `topology.xml` and warning `can't bind memory` usually means this NUMA node has no local memory, if you use only 2 memory sticks, try move one to another slot, both die inside CPU package should have at least 1 channel of memory.
Thank you.

## kocimiros | 2019-10-08T15:56:23+00:00
Topology.xml

```

<!DOCTYPE topology SYSTEM "hwloc2.dtd">
<topology version="2.0">
  <object type="Machine" os_index="0" cpuset="0x0000ffff" complete_cpuset="0x0000ffff" allowed_cpuset="0x0000ffff" nodeset="0x00000001" complete_nodeset="0x00000003" allowed_nodeset="0x00000001" gp_index="1">
    <info name="DMIProductName" value="To Be Filled By O.E.M."/>
    <info name="DMIProductVersion" value="To Be Filled By O.E.M."/>
    <info name="DMIProductSerial" value="To Be Filled By O.E.M."/>
    <info name="DMIProductUUID" value="03000200-0400-0500-0006-000700080009"/>
    <info name="DMIBoardVendor" value="ASRock"/>
    <info name="DMIBoardName" value="X399 Taichi"/>
    <info name="DMIBoardVersion" value=""/>
    <info name="DMIBoardSerial" value="M80-AA007900205"/>
    <info name="DMIBoardAssetTag" value=""/>
    <info name="DMIChassisVendor" value="Default string"/>
    <info name="DMIChassisType" value="3"/>
    <info name="DMIChassisVersion" value="Default string"/>
    <info name="DMIChassisSerial" value="Default string"/>
    <info name="DMIChassisAssetTag" value="Default string"/>
    <info name="DMIBIOSVendor" value="American Megatrends Inc."/>
    <info name="DMIBIOSVersion" value="P1.50"/>
    <info name="DMIBIOSDate" value="09/05/2017"/>
    <info name="DMISysVendor" value="To Be Filled By O.E.M."/>
    <info name="Backend" value="Linux"/>
    <info name="LinuxCgroup" value="/"/>
    <info name="OSName" value="Linux"/>
    <info name="OSRelease" value="4.15.0-58-generic"/>
    <info name="OSVersion" value="#64-Ubuntu SMP Tue Aug 6 11:12:41 UTC 2019"/>
    <info name="HostName" value="32-23"/>
    <info name="Architecture" value="x86_64"/>
    <info name="hwlocVersion" value="2.0.4"/>
    <info name="ProcessName" value="xmrig"/>
    <object type="Package" os_index="0" cpuset="0x0000ffff" complete_cpuset="0x0000ffff" nodeset="0x00000001" complete_nodeset="0x00000003" gp_index="2">
      <info name="CPUVendor" value="AuthenticAMD"/>
      <info name="CPUFamilyNumber" value="23"/>
      <info name="CPUModelNumber" value="1"/>
      <info name="CPUModel" value="AMD Ryzen Threadripper 1900X 8-Core Processor  "/>
      <info name="CPUStepping" value="1"/>
      <object type="L3Cache" cpuset="0x00000f0f" complete_cpuset="0x00000f0f" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="7" cache_size="8388608" depth="3" cache_linesize="64" cache_associativity="16" cache_type="0">
        <info name="Inclusive" value="0"/>
        <object type="NUMANode" os_index="0" cpuset="0x00000f0f" complete_cpuset="0x00000f0f" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="45" local_memory="16736944128">
          <page_type size="4096" count="2038168"/>
          <page_type size="2097152" count="4000"/>
          <page_type size="1073741824" count="0"/>
        </object>
        <object type="L2Cache" cpuset="0x00000101" complete_cpuset="0x00000101" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="6" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <info name="Inclusive" value="1"/>
          <object type="L1Cache" cpuset="0x00000101" complete_cpuset="0x00000101" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="5" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="0" cpuset="0x00000101" complete_cpuset="0x00000101" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="3">
              <object type="PU" os_index="0" cpuset="0x00000001" complete_cpuset="0x00000001" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="4"/>
              <object type="PU" os_index="8" cpuset="0x00000100" complete_cpuset="0x00000100" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="37"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000202" complete_cpuset="0x00000202" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="11" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <info name="Inclusive" value="1"/>
          <object type="L1Cache" cpuset="0x00000202" complete_cpuset="0x00000202" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="10" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="1" cpuset="0x00000202" complete_cpuset="0x00000202" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="8">
              <object type="PU" os_index="1" cpuset="0x00000002" complete_cpuset="0x00000002" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="9"/>
              <object type="PU" os_index="9" cpuset="0x00000200" complete_cpuset="0x00000200" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="38"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000404" complete_cpuset="0x00000404" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="15" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <info name="Inclusive" value="1"/>
          <object type="L1Cache" cpuset="0x00000404" complete_cpuset="0x00000404" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="14" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="2" cpuset="0x00000404" complete_cpuset="0x00000404" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="12">
              <object type="PU" os_index="2" cpuset="0x00000004" complete_cpuset="0x00000004" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="13"/>
              <object type="PU" os_index="10" cpuset="0x00000400" complete_cpuset="0x00000400" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="39"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000808" complete_cpuset="0x00000808" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="19" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <info name="Inclusive" value="1"/>
          <object type="L1Cache" cpuset="0x00000808" complete_cpuset="0x00000808" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="18" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="3" cpuset="0x00000808" complete_cpuset="0x00000808" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="16">
              <object type="PU" os_index="3" cpuset="0x00000008" complete_cpuset="0x00000008" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="17"/>
              <object type="PU" os_index="11" cpuset="0x00000800" complete_cpuset="0x00000800" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="40"/>
            </object>
          </object>
        </object>
      </object>
      <object type="L3Cache" cpuset="0x0000f0f0" complete_cpuset="0x0000f0f0" nodeset="0x0" complete_nodeset="0x00000002" gp_index="24" cache_size="8388608" depth="3" cache_linesize="64" cache_associativity="16" cache_type="0">
        <info name="Inclusive" value="0"/>
        <object type="L2Cache" cpuset="0x00001010" complete_cpuset="0x00001010" nodeset="0x0" complete_nodeset="0x00000002" gp_index="23" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <info name="Inclusive" value="1"/>
          <object type="L1Cache" cpuset="0x00001010" complete_cpuset="0x00001010" nodeset="0x0" complete_nodeset="0x00000002" gp_index="22" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="8" cpuset="0x00001010" complete_cpuset="0x00001010" nodeset="0x0" complete_nodeset="0x00000002" gp_index="20">
              <object type="PU" os_index="4" cpuset="0x00000010" complete_cpuset="0x00000010" nodeset="0x0" complete_nodeset="0x00000002" gp_index="21"/>
              <object type="PU" os_index="12" cpuset="0x00001000" complete_cpuset="0x00001000" nodeset="0x0" complete_nodeset="0x00000002" gp_index="41"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00002020" complete_cpuset="0x00002020" nodeset="0x0" complete_nodeset="0x00000002" gp_index="28" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <info name="Inclusive" value="1"/>
          <object type="L1Cache" cpuset="0x00002020" complete_cpuset="0x00002020" nodeset="0x0" complete_nodeset="0x00000002" gp_index="27" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="9" cpuset="0x00002020" complete_cpuset="0x00002020" nodeset="0x0" complete_nodeset="0x00000002" gp_index="25">
              <object type="PU" os_index="5" cpuset="0x00000020" complete_cpuset="0x00000020" nodeset="0x0" complete_nodeset="0x00000002" gp_index="26"/>
              <object type="PU" os_index="13" cpuset="0x00002000" complete_cpuset="0x00002000" nodeset="0x0" complete_nodeset="0x00000002" gp_index="42"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00004040" complete_cpuset="0x00004040" nodeset="0x0" complete_nodeset="0x00000002" gp_index="32" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <info name="Inclusive" value="1"/>
          <object type="L1Cache" cpuset="0x00004040" complete_cpuset="0x00004040" nodeset="0x0" complete_nodeset="0x00000002" gp_index="31" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="10" cpuset="0x00004040" complete_cpuset="0x00004040" nodeset="0x0" complete_nodeset="0x00000002" gp_index="29">
              <object type="PU" os_index="6" cpuset="0x00000040" complete_cpuset="0x00000040" nodeset="0x0" complete_nodeset="0x00000002" gp_index="30"/>
              <object type="PU" os_index="14" cpuset="0x00004000" complete_cpuset="0x00004000" nodeset="0x0" complete_nodeset="0x00000002" gp_index="43"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00008080" complete_cpuset="0x00008080" nodeset="0x0" complete_nodeset="0x00000002" gp_index="36" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <info name="Inclusive" value="1"/>
          <object type="L1Cache" cpuset="0x00008080" complete_cpuset="0x00008080" nodeset="0x0" complete_nodeset="0x00000002" gp_index="35" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="11" cpuset="0x00008080" complete_cpuset="0x00008080" nodeset="0x0" complete_nodeset="0x00000002" gp_index="33">
              <object type="PU" os_index="7" cpuset="0x00000080" complete_cpuset="0x00000080" nodeset="0x0" complete_nodeset="0x00000002" gp_index="34"/>
              <object type="PU" os_index="15" cpuset="0x00008000" complete_cpuset="0x00008000" nodeset="0x0" complete_nodeset="0x00000002" gp_index="44"/>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
</topology>

```

## kocimiros | 2019-10-13T18:33:23+00:00
Thanks, It helped (moving the RAM stick) 

## lexo-mfleuti | 2022-06-10T16:22:26+00:00
I fiddled with this now for several hours and the solution is most probably not software related. I documented it here:
https://www.lexo.ch/blog/2022/06/solved-xmrig-cpu-xx-warning-cant-bind-memory-xmrig-does-not-run-on-all-cpu-cores/

Hope this helps!

# Action History
- Created by: kocimiros | 2019-10-08T10:19:14+00:00
- Closed at: 2019-10-13T18:33:29+00:00
