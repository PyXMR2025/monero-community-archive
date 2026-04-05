---
title: AMD Ryzen Threadripper 3970X and XMRig/6.16.2 gcc/10.1.0 - > 11188.3 H/s Help
  pliase!
source_url: https://github.com/xmrig/xmrig/issues/2850
author: MaxMusienko
assignees: []
labels: []
created_at: '2021-12-31T11:28:37+00:00'
updated_at: '2022-01-11T06:19:50+00:00'
type: issue
status: closed
closed_at: '2022-01-11T06:19:50+00:00'
---

# Original Description
Hi all!

After visiting this site [https://xmrig.com/benchmark?cpu=AMD+Ryzen+Threadripper+3970X+32-Core+Processor](url) I thought about the fact that I have a low hashrate. Please tell me what am I doing wrong? How can I achieve a higher hashrate using my hardware settings in BIOS or config file? Thanks!

start file -> benchmark_1M.cmd in Windows 11 OS

* ABOUT        XMRig/6.16.2 gcc/10.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen Threadripper 3970X 32-Core Processor (1) 64-bit AES VM
                L2:16.0 MB L3:128.0 MB 32C/64T NUMA:1
 * MEMORY       11.0/127.9 GB (9%)
                DIMM_A0: 32 GB DDR4 @ 2400 MHz KF3200C16D4/32GX
                DIMM_A1: 32 GB DDR4 @ 2400 MHz KF3200C16D4/32GX
                DIMM 0: <empty>
                DIMM 1: <empty>
                DIMM_C0: 32 GB DDR4 @ 2400 MHz KF3200C16D4/32GX
                DIMM_C1: 32 GB DDR4 @ 2400 MHz KF3200C16D4/32GX
                DIMM 0: <empty>
                DIMM 1: <empty>
 * MOTHERBOARD  System manufacturer - System Product Name
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-12-31 13:50:16.992]  bench    start benchmark hashes 1M algo rx/0
[2021-12-31 13:50:16.992]  cpu      use argon2 implementation AVX2
[2021-12-31 13:50:18.032]  msr      register values for "ryzen_17h" preset have been set successfully (1041 ms)
[2021-12-31 13:50:18.033]  randomx  init dataset algo rx/0 (64 threads) seed 0000000000000000...
[2021-12-31 13:50:18.033]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2021-12-31 13./xmrig --export-topology:50:19.940]  randomx  dataset ready (1906 ms)
[2021-12-31 13:50:19.940]  cpu      use profile  rx  (64 threads) scratchpad 2048 KB
[2021-12-31 13:50:19.975]  cpu      READY threads 64/64 (64) huge pages 100% 64/64 memory 131072 KB (35 ms)
[2021-12-31 13:50:20.218]  bench    seed f6cfd28bf90a9da0229d6b8b8c6ed7390f3d940162b93a240a90e3413269b524
[2021-12-31 13:51:20.743]  miner    speed 10s/60s/15m 10982.0 11052.3 n/a H/s max 11188.3 H/s
[2021-12-31 13:51:20.744]  bench    67.15% 671476/1000000 (60.801s)
[2021-12-31 13:51:50.316]  bench    benchmark finished in 90.372 seconds (11065.4 h/s) hash sum = 74DE119038739A0C
[2021-12-31 13:51:50.612]  bench    benchmark submitted https://xmrig.com/benchmark/kFsne
[2021-12-31 13:51:50.612]  bench    press Ctrl+C to exit
[2021-12-31 13:51:50.698]  cpu      stopped (2 ms)

--export-topology

> 

`This XML file does not appear to have any style information associated with it. The document tree is shown below.
<topology version="2.0">
<object type="Machine" os_index="0" cpuset="0xffffffff,0xffffffff" complete_cpuset="0xffffffff,0xffffffff" allowed_cpuset="0xffffffff,0xffffffff" nodeset="0x00000001" complete_nodeset="0x00000001" allowed_nodeset="0x00000001" gp_index="1">
<info name="Backend" value="Windows"/>
<info name="OSName" value="Windows"/>
<info name="WindowsBuildEnvironment" value="MinGW"/>
<info name="OSRelease" value="10"/>
<info name="OSVersion" value="10.0.22000"/>
<info name="Hostname" value="DESKTOP-UJRGTD1"/>
<info name="Architecture" value="x86_64"/>
<info name="hwlocVersion" value="2.5.0"/>
<info name="ProcessName" value="xmrig.exe"/>
<object type="Package" cpuset="0xffffffff,0xffffffff" complete_cpuset="0xffffffff,0xffffffff" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="2">
<info name="CPUVendor" value="AuthenticAMD"/>
<info name="CPUFamilyNumber" value="23"/>
<info name="CPUModelNumber" value="49"/>
<info name="CPUModel" value="AMD Ryzen Threadripper 3970X 32-Core Processor "/>
<info name="CPUStepping" value="0"/>
<object type="NUMANode" os_index="0" cpuset="0xffffffff,0xffffffff" complete_cpuset="0xffffffff,0xffffffff" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="107" local_memory="125524717568">
<page_type size="4096" count="0"/>
</object>
<object type="L3Cache" cpuset="0x000000ff" complete_cpuset="0x000000ff" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="6" cache_size="16777216" depth="3" cache_linesize="64" cache_associativity="16" cache_type="0">
<info name="Inclusive" value="0"/>
<object type="L2Cache" cpuset="0x00000003" complete_cpuset="0x00000003" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="5" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00000003" complete_cpuset="0x00000003" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="4" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00000003" complete_cpuset="0x00000003" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="3">
<object type="PU" os_index="0" cpuset="0x00000001" complete_cpuset="0x00000001" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="109"/>
<object type="PU" os_index="1" cpuset="0x00000002" complete_cpuset="0x00000002" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="110"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x0000000c" complete_cpuset="0x0000000c" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="9" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x0000000c" complete_cpuset="0x0000000c" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="8" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x0000000c" complete_cpuset="0x0000000c" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="7">
<object type="PU" os_index="2" cpuset="0x00000004" complete_cpuset="0x00000004" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="111"/>
<object type="PU" os_index="3" cpuset="0x00000008" complete_cpuset="0x00000008" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="112"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x00000030" complete_cpuset="0x00000030" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="12" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00000030" complete_cpuset="0x00000030" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="11" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00000030" complete_cpuset="0x00000030" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="10">
<object type="PU" os_index="4" cpuset="0x00000010" complete_cpuset="0x00000010" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="113"/>
<object type="PU" os_index="5" cpuset="0x00000020" complete_cpuset="0x00000020" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="114"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x000000c0" complete_cpuset="0x000000c0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="15" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x000000c0" complete_cpuset="0x000000c0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="14" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x000000c0" complete_cpuset="0x000000c0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="13">
<object type="PU" os_index="6" cpuset="0x00000040" complete_cpuset="0x00000040" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="115"/>
<object type="PU" os_index="7" cpuset="0x00000080" complete_cpuset="0x00000080" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="116"/>
</object>
</object>
</object>
</object>
<object type="L3Cache" cpuset="0x0000ff00" complete_cpuset="0x0000ff00" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="19" cache_size="16777216" depth="3" cache_linesize="64" cache_associativity="16" cache_type="0">
<info name="Inclusive" value="0"/>
<object type="L2Cache" cpuset="0x00000300" complete_cpuset="0x00000300" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="18" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00000300" complete_cpuset="0x00000300" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="17" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00000300" complete_cpuset="0x00000300" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="16">
<object type="PU" os_index="8" cpuset="0x00000100" complete_cpuset="0x00000100" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="117"/>
<object type="PU" os_index="9" cpuset="0x00000200" complete_cpuset="0x00000200" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="118"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x00000c00" complete_cpuset="0x00000c00" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="22" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00000c00" complete_cpuset="0x00000c00" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="21" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00000c00" complete_cpuset="0x00000c00" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="20">
<object type="PU" os_index="10" cpuset="0x00000400" complete_cpuset="0x00000400" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="119"/>
<object type="PU" os_index="11" cpuset="0x00000800" complete_cpuset="0x00000800" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="120"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x00003000" complete_cpuset="0x00003000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="25" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00003000" complete_cpuset="0x00003000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="24" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00003000" complete_cpuset="0x00003000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="23">
<object type="PU" os_index="12" cpuset="0x00001000" complete_cpuset="0x00001000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="121"/>
<object type="PU" os_index="13" cpuset="0x00002000" complete_cpuset="0x00002000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="122"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x0000c000" complete_cpuset="0x0000c000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="28" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x0000c000" complete_cpuset="0x0000c000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="27" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x0000c000" complete_cpuset="0x0000c000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="26">
<object type="PU" os_index="14" cpuset="0x00004000" complete_cpuset="0x00004000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="123"/>
<object type="PU" os_index="15" cpuset="0x00008000" complete_cpuset="0x00008000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="124"/>
</object>
</object>
</object>
</object>
<object type="L3Cache" cpuset="0x00ff0000" complete_cpuset="0x00ff0000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="32" cache_size="16777216" depth="3" cache_linesize="64" cache_associativity="16" cache_type="0">
<info name="Inclusive" value="0"/>
<object type="L2Cache" cpuset="0x00030000" complete_cpuset="0x00030000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="31" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00030000" complete_cpuset="0x00030000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="30" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00030000" complete_cpuset="0x00030000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="29">
<object type="PU" os_index="16" cpuset="0x00010000" complete_cpuset="0x00010000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="125"/>
<object type="PU" os_index="17" cpuset="0x00020000" complete_cpuset="0x00020000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="126"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x000c0000" complete_cpuset="0x000c0000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="35" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x000c0000" complete_cpuset="0x000c0000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="34" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x000c0000" complete_cpuset="0x000c0000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="33">
<object type="PU" os_index="18" cpuset="0x00040000" complete_cpuset="0x00040000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="127"/>
<object type="PU" os_index="19" cpuset="0x00080000" complete_cpuset="0x00080000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="128"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x00300000" complete_cpuset="0x00300000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="38" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00300000" complete_cpuset="0x00300000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="37" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00300000" complete_cpuset="0x00300000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="36">
<object type="PU" os_index="20" cpuset="0x00100000" complete_cpuset="0x00100000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="129"/>
<object type="PU" os_index="21" cpuset="0x00200000" complete_cpuset="0x00200000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="130"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x00c00000" complete_cpuset="0x00c00000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="41" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00c00000" complete_cpuset="0x00c00000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="40" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00c00000" complete_cpuset="0x00c00000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="39">
<object type="PU" os_index="22" cpuset="0x00400000" complete_cpuset="0x00400000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="131"/>
<object type="PU" os_index="23" cpuset="0x00800000" complete_cpuset="0x00800000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="132"/>
</object>
</object>
</object>
</object>
<object type="L3Cache" cpuset="0xff000000" complete_cpuset="0xff000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="45" cache_size="16777216" depth="3" cache_linesize="64" cache_associativity="16" cache_type="0">
<info name="Inclusive" value="0"/>
<object type="L2Cache" cpuset="0x03000000" complete_cpuset="0x03000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="44" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x03000000" complete_cpuset="0x03000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="43" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x03000000" complete_cpuset="0x03000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="42">
<object type="PU" os_index="24" cpuset="0x01000000" complete_cpuset="0x01000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="133"/>
<object type="PU" os_index="25" cpuset="0x02000000" complete_cpuset="0x02000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="134"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x0c000000" complete_cpuset="0x0c000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="48" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x0c000000" complete_cpuset="0x0c000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="47" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x0c000000" complete_cpuset="0x0c000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="46">
<object type="PU" os_index="26" cpuset="0x04000000" complete_cpuset="0x04000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="135"/>
<object type="PU" os_index="27" cpuset="0x08000000" complete_cpuset="0x08000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="136"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x30000000" complete_cpuset="0x30000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="51" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x30000000" complete_cpuset="0x30000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="50" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x30000000" complete_cpuset="0x30000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="49">
<object type="PU" os_index="28" cpuset="0x10000000" complete_cpuset="0x10000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="137"/>
<object type="PU" os_index="29" cpuset="0x20000000" complete_cpuset="0x20000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="138"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0xc0000000" complete_cpuset="0xc0000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="54" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0xc0000000" complete_cpuset="0xc0000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="53" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0xc0000000" complete_cpuset="0xc0000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="52">
<object type="PU" os_index="30" cpuset="0x40000000" complete_cpuset="0x40000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="139"/>
<object type="PU" os_index="31" cpuset="0x80000000" complete_cpuset="0x80000000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="140"/>
</object>
</object>
</object>
</object>
<object type="L3Cache" cpuset="0x000000ff,0x0" complete_cpuset="0x000000ff,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="58" cache_size="16777216" depth="3" cache_linesize="64" cache_associativity="16" cache_type="0">
<info name="Inclusive" value="0"/>
<object type="L2Cache" cpuset="0x00000003,0x0" complete_cpuset="0x00000003,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="57" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00000003,0x0" complete_cpuset="0x00000003,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="56" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00000003,0x0" complete_cpuset="0x00000003,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="55">
<object type="PU" os_index="32" cpuset="0x00000001,0x0" complete_cpuset="0x00000001,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="141"/>
<object type="PU" os_index="33" cpuset="0x00000002,0x0" complete_cpuset="0x00000002,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="142"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x0000000c,0x0" complete_cpuset="0x0000000c,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="61" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x0000000c,0x0" complete_cpuset="0x0000000c,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="60" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x0000000c,0x0" complete_cpuset="0x0000000c,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="59">
<object type="PU" os_index="34" cpuset="0x00000004,0x0" complete_cpuset="0x00000004,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="143"/>
<object type="PU" os_index="35" cpuset="0x00000008,0x0" complete_cpuset="0x00000008,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="144"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x00000030,0x0" complete_cpuset="0x00000030,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="64" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00000030,0x0" complete_cpuset="0x00000030,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="63" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00000030,0x0" complete_cpuset="0x00000030,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="62">
<object type="PU" os_index="36" cpuset="0x00000010,0x0" complete_cpuset="0x00000010,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="145"/>
<object type="PU" os_index="37" cpuset="0x00000020,0x0" complete_cpuset="0x00000020,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="146"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x000000c0,0x0" complete_cpuset="0x000000c0,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="67" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x000000c0,0x0" complete_cpuset="0x000000c0,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="66" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x000000c0,0x0" complete_cpuset="0x000000c0,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="65">
<object type="PU" os_index="38" cpuset="0x00000040,0x0" complete_cpuset="0x00000040,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="147"/>
<object type="PU" os_index="39" cpuset="0x00000080,0x0" complete_cpuset="0x00000080,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="148"/>
</object>
</object>
</object>
</object>
<object type="L3Cache" cpuset="0x0000ff00,0x0" complete_cpuset="0x0000ff00,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="71" cache_size="16777216" depth="3" cache_linesize="64" cache_associativity="16" cache_type="0">
<info name="Inclusive" value="0"/>
<object type="L2Cache" cpuset="0x00000300,0x0" complete_cpuset="0x00000300,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="70" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00000300,0x0" complete_cpuset="0x00000300,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="69" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00000300,0x0" complete_cpuset="0x00000300,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="68">
<object type="PU" os_index="40" cpuset="0x00000100,0x0" complete_cpuset="0x00000100,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="149"/>
<object type="PU" os_index="41" cpuset="0x00000200,0x0" complete_cpuset="0x00000200,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="150"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x00000c00,0x0" complete_cpuset="0x00000c00,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="74" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00000c00,0x0" complete_cpuset="0x00000c00,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="73" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00000c00,0x0" complete_cpuset="0x00000c00,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="72">
<object type="PU" os_index="42" cpuset="0x00000400,0x0" complete_cpuset="0x00000400,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="151"/>
<object type="PU" os_index="43" cpuset="0x00000800,0x0" complete_cpuset="0x00000800,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="152"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x00003000,0x0" complete_cpuset="0x00003000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="77" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00003000,0x0" complete_cpuset="0x00003000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="76" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00003000,0x0" complete_cpuset="0x00003000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="75">
<object type="PU" os_index="44" cpuset="0x00001000,0x0" complete_cpuset="0x00001000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="153"/>
<object type="PU" os_index="45" cpuset="0x00002000,0x0" complete_cpuset="0x00002000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="154"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x0000c000,0x0" complete_cpuset="0x0000c000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="80" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x0000c000,0x0" complete_cpuset="0x0000c000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="79" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x0000c000,0x0" complete_cpuset="0x0000c000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="78">
<object type="PU" os_index="46" cpuset="0x00004000,0x0" complete_cpuset="0x00004000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="155"/>
<object type="PU" os_index="47" cpuset="0x00008000,0x0" complete_cpuset="0x00008000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="156"/>
</object>
</object>
</object>
</object>
<object type="L3Cache" cpuset="0x00ff0000,0x0" complete_cpuset="0x00ff0000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="84" cache_size="16777216" depth="3" cache_linesize="64" cache_associativity="16" cache_type="0">
<info name="Inclusive" value="0"/>
<object type="L2Cache" cpuset="0x00030000,0x0" complete_cpuset="0x00030000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="83" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00030000,0x0" complete_cpuset="0x00030000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="82" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00030000,0x0" complete_cpuset="0x00030000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="81">
<object type="PU" os_index="48" cpuset="0x00010000,0x0" complete_cpuset="0x00010000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="157"/>
<object type="PU" os_index="49" cpuset="0x00020000,0x0" complete_cpuset="0x00020000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="158"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x000c0000,0x0" complete_cpuset="0x000c0000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="87" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x000c0000,0x0" complete_cpuset="0x000c0000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="86" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x000c0000,0x0" complete_cpuset="0x000c0000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="85">
<object type="PU" os_index="50" cpuset="0x00040000,0x0" complete_cpuset="0x00040000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="159"/>
<object type="PU" os_index="51" cpuset="0x00080000,0x0" complete_cpuset="0x00080000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="160"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x00300000,0x0" complete_cpuset="0x00300000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="90" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00300000,0x0" complete_cpuset="0x00300000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="89" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00300000,0x0" complete_cpuset="0x00300000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="88">
<object type="PU" os_index="52" cpuset="0x00100000,0x0" complete_cpuset="0x00100000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="161"/>
<object type="PU" os_index="53" cpuset="0x00200000,0x0" complete_cpuset="0x00200000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="162"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x00c00000,0x0" complete_cpuset="0x00c00000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="93" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x00c00000,0x0" complete_cpuset="0x00c00000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="92" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x00c00000,0x0" complete_cpuset="0x00c00000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="91">
<object type="PU" os_index="54" cpuset="0x00400000,0x0" complete_cpuset="0x00400000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="163"/>
<object type="PU" os_index="55" cpuset="0x00800000,0x0" complete_cpuset="0x00800000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="164"/>
</object>
</object>
</object>
</object>
<object type="L3Cache" cpuset="0xff000000,0x0" complete_cpuset="0xff000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="97" cache_size="16777216" depth="3" cache_linesize="64" cache_associativity="16" cache_type="0">
<info name="Inclusive" value="0"/>
<object type="L2Cache" cpuset="0x03000000,0x0" complete_cpuset="0x03000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="96" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x03000000,0x0" complete_cpuset="0x03000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="95" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x03000000,0x0" complete_cpuset="0x03000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="94">
<object type="PU" os_index="56" cpuset="0x01000000,0x0" complete_cpuset="0x01000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="165"/>
<object type="PU" os_index="57" cpuset="0x02000000,0x0" complete_cpuset="0x02000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="166"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x0c000000,0x0" complete_cpuset="0x0c000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="100" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x0c000000,0x0" complete_cpuset="0x0c000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="99" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x0c000000,0x0" complete_cpuset="0x0c000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="98">
<object type="PU" os_index="58" cpuset="0x04000000,0x0" complete_cpuset="0x04000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="167"/>
<object type="PU" os_index="59" cpuset="0x08000000,0x0" complete_cpuset="0x08000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="168"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0x30000000,0x0" complete_cpuset="0x30000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="103" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0x30000000,0x0" complete_cpuset="0x30000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="102" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0x30000000,0x0" complete_cpuset="0x30000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="101">
<object type="PU" os_index="60" cpuset="0x10000000,0x0" complete_cpuset="0x10000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="169"/>
<object type="PU" os_index="61" cpuset="0x20000000,0x0" complete_cpuset="0x20000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="170"/>
</object>
</object>
</object>
<object type="L2Cache" cpuset="0xc0000000,0x0" complete_cpuset="0xc0000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="106" cache_size="524288" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
<info name="Inclusive" value="1"/>
<object type="L1Cache" cpuset="0xc0000000,0x0" complete_cpuset="0xc0000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="105" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
<info name="Inclusive" value="0"/>
<object type="Core" cpuset="0xc0000000,0x0" complete_cpuset="0xc0000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="104">
<object type="PU" os_index="62" cpuset="0x40000000,0x0" complete_cpuset="0x40000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="171"/>
<object type="PU" os_index="63" cpuset="0x80000000,0x0" complete_cpuset="0x80000000,0x0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="172"/>
</object>
</object>
</object>
</object>
</object>
</object>
<support name="discovery.pu"/>
<support name="discovery.numa"/>
<support name="discovery.numa_memory"/>
<support name="discovery.cpukind_efficiency"/>
<support name="cpubind.set_thisproc_cpubind"/>
<support name="cpubind.get_thisproc_cpubind"/>
<support name="cpubind.set_proc_cpubind"/>
<support name="cpubind.get_proc_cpubind"/>
<support name="cpubind.set_thisthread_cpubind"/>
<support name="cpubind.get_thisthread_cpubind"/>
<support name="cpubind.set_thread_cpubind"/>
<support name="cpubind.get_thread_cpubind"/>
<support name="cpubind.get_thisthread_last_cpu_location"/>
<support name="membind.set_thisproc_membind"/>
<support name="membind.get_thisproc_membind"/>
<support name="membind.set_proc_membind"/>
<support name="membind.get_proc_membind"/>
<support name="membind.set_thisthread_membind"/>
<support name="membind.get_thisthread_membind"/>
<support name="membind.alloc_membind"/>
<support name="membind.bind_membind"/>
<support name="membind.get_area_memlocation"/>
<support name="custom.exported_support"/>
<cpukind cpuset="0xffffffff,0xffffffff" forced_efficiency="0"/>
</topology>`



# Discussion History
## MaxMusienko | 2021-12-31T12:40:15+00:00
I noticed that I have a VM mode. This mode, as I understand it, affects the work with memory. VM mode may be due to the fact that I run XMRig on a Windows 11 computer using an RDP connection remotely?

## SChernykh | 2021-12-31T12:56:19+00:00
Problems with your setup:
- You use only 2 of the 4 memory channels (install your memory sticks into correct slots)
- Memory runs at 2400 MHz and probably with bad default timings
- VM mode, turn it off: https://www.techrepublic.com/article/how-to-disable-vbs-to-increase-windows-11-performance-and-why-you-shouldnt/

## MaxMusienko | 2022-01-01T00:05:19+00:00
Thanks for the advice!
I did as indicated in the instructions given by you. Turned off and restarted the computer. I went in and checked that this flag is in the off position. When XMRig starts, it states that it is running in VM mode. What else needs to be done to remove this mode? Thanks!
 * CPU          AMD Ryzen Threadripper 3970X 32-Core Processor (1) 64-bit AES **VM**

## Lonnegan | 2022-01-06T23:33:10+00:00
Perhaps you have installed the Hyper-V in the Windows features? In this case Windows itself runs virtualized.

## MaxMusienko | 2022-01-10T17:23:32+00:00
Hi all!

>You use only 2 of the 4 memory channels (install your memory sticks into correct slots) - **Fixed**
>Memory runs at 2400 MHz and probably with bad default timings - **Fixed** 
>VM mode, turn it off:- **Fixed**

To disable VM mode, I had to disable all virtualization options in the computer's BIOS.


## MaxMusienko | 2022-01-11T06:17:59+00:00
Hi
Many thanks to everyone for the advice and help. The question can be considered closed.

start file -> benchmark_1M.cmd in Windows 11 OS 

`* ABOUT        XMRig/6.16.2 gcc/10.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen Threadripper 3970X 32-Core Processor (1) 64-bit AES
                L2:16.0 MB L3:128.0 MB 32C/64T NUMA:1
 * MEMORY       6.2/127.9 GB (5%)
                DIMM 0: <empty>
                DIMM_A1: 32 GB DDR4 @ 3200 MHz KF3200C16D4/32GX
                DIMM 0: <empty>
                DIMM_B1: 32 GB DDR4 @ 3200 MHz KF3200C16D4/32GX
                DIMM 0: <empty>
                DIMM_C1: 32 GB DDR4 @ 3200 MHz KF3200C16D4/32GX
                DIMM 0: <empty>
                DIMM_D1: 32 GB DDR4 @ 3200 MHz KF3200C16D4/32GX
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - PRIME TRX40-PRO S
 * DONATE       0%
 * ASSEMBLY     auto:ryzen
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-01-11 09:11:23.397]  bench    start benchmark hashes 1M algo rx/0
[2022-01-11 09:11:23.399]  cpu      use argon2 implementation AVX2
[2022-01-11 09:11:24.450]  msr      register values for "ryzen_17h" preset have been set successfully (1050 ms)
[2022-01-11 09:11:24.450]  randomx  init dataset algo rx/0 (64 threads) seed 0000000000000000...
[2022-01-11 09:11:24.450]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2022-01-11 09:11:25.310]  randomx  dataset ready (860 ms)
[2022-01-11 09:11:25.310]  cpu      use profile  rx  (64 threads) scratchpad 2048 KB
[2022-01-11 09:11:25.336]  cpu      READY threads 64/64 (64) huge pages 100% 64/64 memory 131072 KB (26 ms)
[2022-01-11 09:11:25.585]  bench    seed 3b49a3d7ac3491d0051fa1111f5067bb6657cc5aa24bf2caca6ab9e265948f0b
[2022-01-11 09:11:56.930]  bench    benchmark finished in 31.617 seconds (31628.6 h/s) hash sum = F2139B48E0EA77CE
[2022-01-11 09:11:56.968]  cpu      stopped (1 ms)
[2022-01-11 09:11:57.211]  bench    benchmark submitted https://xmrig.com/benchmark/5Qbgvq
[2022-01-11 09:11:57.211]  bench    press Ctrl+C to exit
`

# Action History
- Created by: MaxMusienko | 2021-12-31T11:28:37+00:00
- Closed at: 2022-01-11T06:19:50+00:00
