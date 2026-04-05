---
title: CPU Core utilization on Intel CPU leads to lower hashrate
source_url: https://github.com/xmrig/xmrig/issues/3728
author: mathbreed
assignees: []
labels: []
created_at: '2025-11-01T15:36:50+00:00'
updated_at: '2025-11-02T09:58:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Tested on Intel Core 120U
Mining with threads 0,1,2,3 (all threads on the big cores, 1300H/s) gives better hashrate than mining with 9 threads (0,2,4,5,6,7,8,9,10, 900H/s).

OS: Fedora


# Discussion History
## SChernykh | 2025-11-01T16:47:48+00:00
Can you run `./xmrig --export-topology` and attach the generated XML file here?

## mathbreed | 2025-11-02T02:01:00+00:00
Sure. Generic information about PC has been removed.
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topology SYSTEM "hwloc2.dtd">
<topology version="2.0">
  <object type="Machine" os_index="0" cpuset="0x00000fff" complete_cpuset="0x00000fff" allowed_cpuset="0x00000fff" nodeset="0x00000001" complete_nodeset="0x00000001" allowed_nodeset="0x00000001" gp_index="1">
<info name="Backend" value="Linux"/>
    <info name="LinuxCgroup" value="/user.slice/user-1000.slice/user@1000.service/app.slice/ptyxis-spawn-e7ef07f5-f6a7-4f22-9942-56d9b149a527.scope"/>
    <info name="OSName" value="Linux"/>
    <info name="OSRelease" value="6.17.5-200.fc42.x86_64"/>
    <info name="OSVersion" value="#1 SMP PREEMPT_DYNAMIC Fri Oct 24 14:10:01 UTC 2025"/>
    <info name="HostName" value="secureblue"/>
    <info name="Architecture" value="x86_64"/>
    <info name="hwlocVersion" value="2.12.1"/>
    <info name="ProcessName" value="xmrig"/>
    <object type="Package" os_index="0" cpuset="0x00000fff" complete_cpuset="0x00000fff" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="3">
      <info name="CPUVendor" value="GenuineIntel"/>
      <info name="CPUFamilyNumber" value="6"/>
      <info name="CPUModelNumber" value="186"/>
      <info name="CPUModel" value="Intel(R) Core(TM) 5 120U"/>
      <info name="CPUStepping" value="3"/>
      <object type="NUMANode" os_index="0" cpuset="0x00000fff" complete_cpuset="0x00000fff" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="45" local_memory="33351151616">
        <page_type size="4096" count="7374371"/>
        <page_type size="2097152" count="1500"/>
        <page_type size="1073741824" count="0"/>
      </object>
      <object type="L3Cache" os_index="0" cpuset="0x00000fff" complete_cpuset="0x00000fff" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="9" cache_size="12582912" depth="3" cache_linesize="64" cache_associativity="12" cache_type="0">
        <info name="Inclusive" value="0"/>
        <object type="L2Cache" os_index="0" cpuset="0x00000003" complete_cpuset="0x00000003" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="8" cache_size="1310720" depth="2" cache_linesize="64" cache_associativity="10" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" os_index="0" cpuset="0x00000003" complete_cpuset="0x00000003" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="7" cache_size="49152" depth="1" cache_linesize="64" cache_associativity="12" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="0" cpuset="0x00000003" complete_cpuset="0x00000003" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="2">
              <object type="PU" os_index="0" cpuset="0x00000001" complete_cpuset="0x00000001" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="6"/>
              <object type="PU" os_index="1" cpuset="0x00000002" complete_cpuset="0x00000002" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="10"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" os_index="1" cpuset="0x0000000c" complete_cpuset="0x0000000c" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="15" cache_size="1310720" depth="2" cache_linesize="64" cache_associativity="10" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" os_index="4" cpuset="0x0000000c" complete_cpuset="0x0000000c" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="14" cache_size="49152" depth="1" cache_linesize="64" cache_associativity="12" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="4" cpuset="0x0000000c" complete_cpuset="0x0000000c" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="11">
              <object type="PU" os_index="2" cpuset="0x00000004" complete_cpuset="0x00000004" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="13"/>
              <object type="PU" os_index="3" cpuset="0x00000008" complete_cpuset="0x00000008" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="16"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" os_index="2" cpuset="0x000000f0" complete_cpuset="0x000000f0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="21" cache_size="2097152" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" os_index="8" cpuset="0x00000010" complete_cpuset="0x00000010" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="20" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="8" cpuset="0x00000010" complete_cpuset="0x00000010" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="17">
              <object type="PU" os_index="4" cpuset="0x00000010" complete_cpuset="0x00000010" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="19"/>
            </object>
          </object>
          <object type="L1Cache" os_index="9" cpuset="0x00000020" complete_cpuset="0x00000020" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="24" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="9" cpuset="0x00000020" complete_cpuset="0x00000020" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="22">
              <object type="PU" os_index="5" cpuset="0x00000020" complete_cpuset="0x00000020" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="23"/>
            </object>
          </object>
          <object type="L1Cache" os_index="10" cpuset="0x00000040" complete_cpuset="0x00000040" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="27" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="10" cpuset="0x00000040" complete_cpuset="0x00000040" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="25">
              <object type="PU" os_index="6" cpuset="0x00000040" complete_cpuset="0x00000040" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="26"/>
            </object>
          </object>
          <object type="L1Cache" os_index="11" cpuset="0x00000080" complete_cpuset="0x00000080" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="30" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="11" cpuset="0x00000080" complete_cpuset="0x00000080" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="28">
              <object type="PU" os_index="7" cpuset="0x00000080" complete_cpuset="0x00000080" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="29"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" os_index="3" cpuset="0x00000f00" complete_cpuset="0x00000f00" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="35" cache_size="2097152" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" os_index="12" cpuset="0x00000100" complete_cpuset="0x00000100" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="34" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="12" cpuset="0x00000100" complete_cpuset="0x00000100" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="31">
              <object type="PU" os_index="8" cpuset="0x00000100" complete_cpuset="0x00000100" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="33"/>
            </object>
          </object>
          <object type="L1Cache" os_index="13" cpuset="0x00000200" complete_cpuset="0x00000200" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="38" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="13" cpuset="0x00000200" complete_cpuset="0x00000200" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="36">
              <object type="PU" os_index="9" cpuset="0x00000200" complete_cpuset="0x00000200" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="37"/>
            </object>
          </object>
          <object type="L1Cache" os_index="14" cpuset="0x00000400" complete_cpuset="0x00000400" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="41" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="14" cpuset="0x00000400" complete_cpuset="0x00000400" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="39">
              <object type="PU" os_index="10" cpuset="0x00000400" complete_cpuset="0x00000400" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="40"/>
            </object>
          </object>
          <object type="L1Cache" os_index="15" cpuset="0x00000800" complete_cpuset="0x00000800" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="44" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="15" cpuset="0x00000800" complete_cpuset="0x00000800" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="42">
              <object type="PU" os_index="11" cpuset="0x00000800" complete_cpuset="0x00000800" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="43"/>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <support name="discovery.pu"/>
  <support name="discovery.numa"/>
  <support name="discovery.numa_memory"/>
  <support name="discovery.disallowed_pu"/>
  <support name="discovery.disallowed_numa"/>
  <support name="discovery.cpukind_efficiency"/>
  <support name="cpubind.set_thisproc_cpubind"/>
  <support name="cpubind.get_thisproc_cpubind"/>
  <support name="cpubind.set_proc_cpubind"/>
  <support name="cpubind.get_proc_cpubind"/>
  <support name="cpubind.set_thisthread_cpubind"/>
  <support name="cpubind.get_thisthread_cpubind"/>
  <support name="cpubind.set_thread_cpubind"/>
  <support name="cpubind.get_thread_cpubind"/>
  <support name="cpubind.get_thisproc_last_cpu_location"/>
  <support name="cpubind.get_proc_last_cpu_location"/>
  <support name="cpubind.get_thisthread_last_cpu_location"/>
  <support name="membind.set_thisthread_membind"/>
  <support name="membind.get_thisthread_membind"/>
  <support name="membind.set_area_membind"/>
  <support name="membind.get_area_membind"/>
  <support name="membind.alloc_membind"/>
  <support name="membind.firsttouch_membind"/>
  <support name="membind.bind_membind"/>
  <support name="membind.interleave_membind"/>
  <support name="membind.weighted_interleave_membind"/>
  <support name="membind.migrate_membind"/>
  <support name="membind.get_area_memlocation"/>
  <support name="custom.exported_support"/>
  <cpukind cpuset="0x00000ff0" forced_efficiency="0">
    <info name="FrequencyMaxMHz" value="3800"/>
    <info name="FrequencyBaseMHz" value="900"/>
    <info name="LinuxCapacity" value="1024"/>
    <info name="CoreType" value="IntelAtom"/>
  </cpukind>
  <cpukind cpuset="0x0000000f" forced_efficiency="0">
    <info name="FrequencyMaxMHz" value="5000"/>
    <info name="FrequencyBaseMHz" value="1400"/>
    <info name="LinuxCapacity" value="1024"/>
    <info name="CoreType" value="IntelCore"/>
  </cpukind>
</topology>
```

## mathbreed | 2025-11-02T06:01:28+00:00
@SChernykh Additional Information:
I am running `xmrig` on `secureblue`, a "linux distro" with hardened C memory allocator. So the hashrate is lower than that on vanilla fedora. I had 1.36kH/s with 9 threads on vanilla fedora, but I believe we will see the same hashrate boost after adjusting the cpu utilization on either platform.

On `secureblue`, I get 1.32kH/s with 5 threads (all threads on big cores plus one of the efficiency core) and the `powersave` cpu scaling governor. With the `performance` governor, 3.05kH/s is achieved with 8 threads (all threads on big cores are used, rather than the default one thread per big core), still higher than the default 2.95kH/s with 9 threads. 

## SChernykh | 2025-11-02T09:03:56+00:00
It's very hard to get the optimal auto-config for this kind of mixed core CPU, especially when it's power limited and core performance per watt information is not available to XMRig. But the general idea is that 1 thread on a big core is better than 1 thread on an efficient core?

## mathbreed | 2025-11-02T09:58:55+00:00
I do understand. A good default for Intel laptop CPUs seems to be "all threads on big cores + 1 or 2 efficiency core(s)" (5 cores in this case). This would give the optimal result when `powersave` governor is used, and ~85% of optimal result (2.52kH/s) with `performance` governor (do note that, due to thermal restrictions, the frequency of the CPU will eventually be lowered). A simple mechanism that detects the postfix of the CPU and triggers this behaviour should do.

Also, it would be nice to inform users that "cache size / 2MB = number of threads to use" is no longer true since so many just stick to the defaults.

# Action History
- Created by: mathbreed | 2025-11-01T15:36:50+00:00
