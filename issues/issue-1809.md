---
title: ARM8 Performance Optimization
source_url: https://github.com/xmrig/xmrig/issues/1809
author: Slurprmx
assignees: []
labels:
- bug
- arm
created_at: '2020-08-13T10:16:11+00:00'
updated_at: '2020-08-28T16:28:31+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:28:31+00:00'
---

# Original Description
Hi Guys,

I operating a 64 Core NEOVERSE Board mit 256 GB RAM under a centos 7: 

Architecture:        aarch64
Byte Order:          Little Endian
CPU(s):              64
On-line CPU(s) list: 0-63
Thread(s) per core:  1
Core(s) per socket:  64
Socket(s):           1
NUMA node(s):        1
Model:               1
BogoMIPS:            243.75
L1d cache:           64K
L1i cache:           64K
L2 cache:            1024K
L3 cache:            32768K
NUMA node0 CPU(s):   0-63
Flags:               fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp ssbs

XMRIG Info:
 * ABOUT        XMRig/6.3.1 gcc/7.3.1
 * LIBS         libuv/1.23.2 OpenSSL/1.0.2k hwloc/1.11.8
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARMv8 (1) x64 AES
                L2:64.0 MB L3:32.0 MB 64C/64T NUMA:1
 * MEMORY       3.6/251.9 GB (1%)
 * DONATE       1%
 * POOL #1      gulf.moneroocean.stream:10128 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled


I just wondering about the HS/s that the systems is archiving. Without any "setup" XMRIG only use 16 Cores of the system and with with the threads=64 command XMRIG use 64 Threads ands archives around 14000 hs/s which is which is not much. 
I tried to aczivate 1GB Pages but that runs into an error.

Any hints?

# Discussion History
## xmrig | 2020-08-13T11:49:45+00:00
1. Please show full output including pressing `h` to view per thread hashrate and make sure it mines the RandomX algorithm because you use a multi algorithm pool.
2. Instead of `threads=64` better specify it as array in config file `"rx": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63],`
3. Please share the result of `./xmrig --export-topology`. I have an idea why autoconfig is wrong, but I need to verify it also would be nice if you can check with new hwloc.

Thank you.


## Slurprmx | 2020-08-13T12:48:25+00:00
Here the process overview:

|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |       -1 |   222.1 |     n/a |     n/a |
|        1 |       -1 |   222.6 |     n/a |     n/a |
|        2 |       -1 |   222.8 |     n/a |     n/a |
|        3 |       -1 |   223.6 |     n/a |     n/a |
|        4 |       -1 |   223.7 |     n/a |     n/a |
|        5 |       -1 |   224.0 |     n/a |     n/a |
|        6 |       -1 |   224.0 |     n/a |     n/a |
|        7 |       -1 |   223.1 |     n/a |     n/a |
|        8 |       -1 |   222.9 |     n/a |     n/a |
|        9 |       -1 |   223.9 |     n/a |     n/a |
|       10 |       -1 |   224.0 |     n/a |     n/a |
|       11 |       -1 |   224.5 |     n/a |     n/a |
|       12 |       -1 |   224.5 |     n/a |     n/a |
|       13 |       -1 |   221.8 |     n/a |     n/a |
|       14 |       -1 |   221.8 |     n/a |     n/a |
|       15 |       -1 |   222.5 |     n/a |     n/a |
|       16 |       -1 |   222.4 |     n/a |     n/a |
|       17 |       -1 |   222.6 |     n/a |     n/a |
|       18 |       -1 |   222.9 |     n/a |     n/a |
|       19 |       -1 |   223.6 |     n/a |     n/a |
|       20 |       -1 |   223.8 |     n/a |     n/a |
|       21 |       -1 |   224.3 |     n/a |     n/a |
|       22 |       -1 |   224.3 |     n/a |     n/a |
|       23 |       -1 |   223.4 |     n/a |     n/a |
|       24 |       -1 |   223.4 |     n/a |     n/a |
|       25 |       -1 |   224.2 |     n/a |     n/a |
|       26 |       -1 |   224.1 |     n/a |     n/a |
|       27 |       -1 |   224.5 |     n/a |     n/a |
|       28 |       -1 |   224.6 |     n/a |     n/a |
|       29 |       -1 |   221.7 |     n/a |     n/a |
|       30 |       -1 |   221.7 |     n/a |     n/a |
|       31 |       -1 |   222.4 |     n/a |     n/a |
|       32 |       -1 |   222.2 |     n/a |     n/a |
|       33 |       -1 |   222.5 |     n/a |     n/a |
|       34 |       -1 |   222.6 |     n/a |     n/a |
|       35 |       -1 |   223.5 |     n/a |     n/a |
|       36 |       -1 |   223.5 |     n/a |     n/a |
|       37 |       -1 |   224.1 |     n/a |     n/a |
|       38 |       -1 |   224.1 |     n/a |     n/a |
|       39 |       -1 |   223.1 |     n/a |     n/a |
|       40 |       -1 |   223.1 |     n/a |     n/a |
|       41 |       -1 |   223.9 |     n/a |     n/a |
|       42 |       -1 |   224.0 |     n/a |     n/a |
|       43 |       -1 |   224.7 |     n/a |     n/a |
|       44 |       -1 |   224.4 |     n/a |     n/a |
|       45 |       -1 |   222.0 |     n/a |     n/a |
|       46 |       -1 |   221.9 |     n/a |     n/a |
|       47 |       -1 |   222.4 |     n/a |     n/a |
|       48 |       -1 |   222.3 |     n/a |     n/a |
|       49 |       -1 |   222.7 |     n/a |     n/a |
|       50 |       -1 |   223.0 |     n/a |     n/a |
|       51 |       -1 |   223.6 |     n/a |     n/a |
|       52 |       -1 |   223.7 |     n/a |     n/a |
|       53 |       -1 |   224.1 |     n/a |     n/a |
|       54 |       -1 |   224.0 |     n/a |     n/a |
|       55 |       -1 |   223.5 |     n/a |     n/a |
|       56 |       -1 |   223.5 |     n/a |     n/a |
|       57 |       -1 |   224.1 |     n/a |     n/a |
|       58 |       -1 |   224.2 |     n/a |     n/a |
|       59 |       -1 |   224.5 |     n/a |     n/a |
|       60 |       -1 |   224.5 |     n/a |     n/a |
|       61 |       -1 |   221.9 |     n/a |     n/a |
|       62 |       -1 |   222.0 |     n/a |     n/a |
|       63 |       -1 |   222.3 |     n/a |     n/a |
|        - |        - | 14291.6 |     n/a |     n/a |

## xmrig | 2020-08-13T13:07:54+00:00
Please provide all requested information and change the config, in addition you can also try to mine Wownero, it might perform much better.
Thank you.


## Slurprmx | 2020-08-13T13:15:52+00:00
I tried to change the settings with the json with the array and the RX setup. Same effect.
Here the topology export:


```
<?xml` version="1.0" encoding="UTF-8"?>
<!DOCTYPE topology SYSTEM "hwloc.dtd">
<topology>
  <object type="Machine" os_index="0" cpuset="0xffffffff,0xffffffff" complete_cpuset="0xffffffff,0xffffffff" online_cpuset="0xffffffff,0xffffffff" allowed_cpuset="0xffffffff,0xffffffff" local_memory="270475255808">
    <page_type size="4096" count="65402702"/>
    <page_type size="2097152" count="1233"/>
    <info name="DMIProductName" value="R281-T94"/>
    <info name="DMIProductVersion" value="1.0"/>
    <info name="DMIProductSerial" value="GAbe84a-92c5-e65f-677b-85b3d1484931"/>
    <info name="DMIProductUUID" value="GA2BE84A-92C5-E65F-677B-85B3D1484931"/>
    <info name="DMIBoardVendor" value="Gigabyte"/>
    <info name="DMIBoardName" value="Not Specified"/>
    <info name="DMIBoardVersion" value="Not Specified"/>
    <info name="DMIBoardSerial" value="Not Specified"/>
    <info name="DMIBoardAssetTag" value="i-0c0d62401cbffa91e"/>
    <info name="DMIChassisVendor" value="Gigabyte"/>
    <info name="DMIChassisType" value="1"/>
    <info name="DMIChassisVersion" value="Not Specified"/>
    <info name="DMIChassisSerial" value="Not Specified"/>
    <info name="DMIChassisAssetTag" value="Gigabyte"/>
    <info name="DMIBIOSVendor" value="Gigabyte"/>
    <info name="DMIBIOSVersion" value="1.0"/>
    <info name="DMIBIOSDate" value="10/16/2017"/>
    <info name="DMISysVendor" value="Gigabyte"/>
    <info name="Backend" value="Linux"/>
    <info name="LinuxCgroup" value="/"/>
    <info name="OSName" value="Linux"/>
    <info name="OSRelease" value="4.14.186-146.268.aarch64"/>
    <info name="OSVersion" value="#1 SMP Tue Jul 14 18:17:02 UTC 2020"/>
    <info name="HostName" value=""/>
    <info name="Architecture" value="aarch64"/>
    <info name="hwlocVersion" value="1.11.8"/>
    <info name="ProcessName" value="xmrig"/>
    <object type="Package" os_index="36" cpuset="0xffffffff,0xffffffff" complete_cpuset="0xffffffff,0xffffffff" online_cpuset="0xffffffff,0xffffffff" allowed_cpuset="0xffffffff,0xffffffff">
      <object type="Cache" cpuset="0xffffffff,0xffffffff" complete_cpuset="0xffffffff,0xffffffff" online_cpuset="0xffffffff,0xffffffff" allowed_cpuset="0xffffffff,0xffffffff" cache_size="33554432" depth="3" cache_linesize="64" cache_associativity="16" cache_type="0">
        <object type="Cache" cpuset="0x00000001" complete_cpuset="0x00000001" online_cpuset="0x00000001" allowed_cpuset="0x00000001" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000001" complete_cpuset="0x00000001" online_cpuset="0x00000001" allowed_cpuset="0x00000001" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="138" cpuset="0x00000001" complete_cpuset="0x00000001" online_cpuset="0x00000001" allowed_cpuset="0x00000001">
              <object type="PU" os_index="0" cpuset="0x00000001" complete_cpuset="0x00000001" online_cpuset="0x00000001" allowed_cpuset="0x00000001"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000002" complete_cpuset="0x00000002" online_cpuset="0x00000002" allowed_cpuset="0x00000002" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000002" complete_cpuset="0x00000002" online_cpuset="0x00000002" allowed_cpuset="0x00000002" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="262" cpuset="0x00000002" complete_cpuset="0x00000002" online_cpuset="0x00000002" allowed_cpuset="0x00000002">
              <object type="PU" os_index="1" cpuset="0x00000002" complete_cpuset="0x00000002" online_cpuset="0x00000002" allowed_cpuset="0x00000002"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000004" complete_cpuset="0x00000004" online_cpuset="0x00000004" allowed_cpuset="0x00000004" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000004" complete_cpuset="0x00000004" online_cpuset="0x00000004" allowed_cpuset="0x00000004" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="386" cpuset="0x00000004" complete_cpuset="0x00000004" online_cpuset="0x00000004" allowed_cpuset="0x00000004">
              <object type="PU" os_index="2" cpuset="0x00000004" complete_cpuset="0x00000004" online_cpuset="0x00000004" allowed_cpuset="0x00000004"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000008" complete_cpuset="0x00000008" online_cpuset="0x00000008" allowed_cpuset="0x00000008" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000008" complete_cpuset="0x00000008" online_cpuset="0x00000008" allowed_cpuset="0x00000008" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="510" cpuset="0x00000008" complete_cpuset="0x00000008" online_cpuset="0x00000008" allowed_cpuset="0x00000008">
              <object type="PU" os_index="3" cpuset="0x00000008" complete_cpuset="0x00000008" online_cpuset="0x00000008" allowed_cpuset="0x00000008"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000010" complete_cpuset="0x00000010" online_cpuset="0x00000010" allowed_cpuset="0x00000010" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000010" complete_cpuset="0x00000010" online_cpuset="0x00000010" allowed_cpuset="0x00000010" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="634" cpuset="0x00000010" complete_cpuset="0x00000010" online_cpuset="0x00000010" allowed_cpuset="0x00000010">
              <object type="PU" os_index="4" cpuset="0x00000010" complete_cpuset="0x00000010" online_cpuset="0x00000010" allowed_cpuset="0x00000010"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000020" complete_cpuset="0x00000020" online_cpuset="0x00000020" allowed_cpuset="0x00000020" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000020" complete_cpuset="0x00000020" online_cpuset="0x00000020" allowed_cpuset="0x00000020" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="758" cpuset="0x00000020" complete_cpuset="0x00000020" online_cpuset="0x00000020" allowed_cpuset="0x00000020">
              <object type="PU" os_index="5" cpuset="0x00000020" complete_cpuset="0x00000020" online_cpuset="0x00000020" allowed_cpuset="0x00000020"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000040" complete_cpuset="0x00000040" online_cpuset="0x00000040" allowed_cpuset="0x00000040" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000040" complete_cpuset="0x00000040" online_cpuset="0x00000040" allowed_cpuset="0x00000040" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="882" cpuset="0x00000040" complete_cpuset="0x00000040" online_cpuset="0x00000040" allowed_cpuset="0x00000040">
              <object type="PU" os_index="6" cpuset="0x00000040" complete_cpuset="0x00000040" online_cpuset="0x00000040" allowed_cpuset="0x00000040"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000080" complete_cpuset="0x00000080" online_cpuset="0x00000080" allowed_cpuset="0x00000080" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000080" complete_cpuset="0x00000080" online_cpuset="0x00000080" allowed_cpuset="0x00000080" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="1006" cpuset="0x00000080" complete_cpuset="0x00000080" online_cpuset="0x00000080" allowed_cpuset="0x00000080">
              <object type="PU" os_index="7" cpuset="0x00000080" complete_cpuset="0x00000080" online_cpuset="0x00000080" allowed_cpuset="0x00000080"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000100" complete_cpuset="0x00000100" online_cpuset="0x00000100" allowed_cpuset="0x00000100" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000100" complete_cpuset="0x00000100" online_cpuset="0x00000100" allowed_cpuset="0x00000100" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="1130" cpuset="0x00000100" complete_cpuset="0x00000100" online_cpuset="0x00000100" allowed_cpuset="0x00000100">
              <object type="PU" os_index="8" cpuset="0x00000100" complete_cpuset="0x00000100" online_cpuset="0x00000100" allowed_cpuset="0x00000100"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000200" complete_cpuset="0x00000200" online_cpuset="0x00000200" allowed_cpuset="0x00000200" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000200" complete_cpuset="0x00000200" online_cpuset="0x00000200" allowed_cpuset="0x00000200" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="1254" cpuset="0x00000200" complete_cpuset="0x00000200" online_cpuset="0x00000200" allowed_cpuset="0x00000200">
              <object type="PU" os_index="9" cpuset="0x00000200" complete_cpuset="0x00000200" online_cpuset="0x00000200" allowed_cpuset="0x00000200"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000400" complete_cpuset="0x00000400" online_cpuset="0x00000400" allowed_cpuset="0x00000400" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000400" complete_cpuset="0x00000400" online_cpuset="0x00000400" allowed_cpuset="0x00000400" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="1378" cpuset="0x00000400" complete_cpuset="0x00000400" online_cpuset="0x00000400" allowed_cpuset="0x00000400">
              <object type="PU" os_index="10" cpuset="0x00000400" complete_cpuset="0x00000400" online_cpuset="0x00000400" allowed_cpuset="0x00000400"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000800" complete_cpuset="0x00000800" online_cpuset="0x00000800" allowed_cpuset="0x00000800" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000800" complete_cpuset="0x00000800" online_cpuset="0x00000800" allowed_cpuset="0x00000800" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="1502" cpuset="0x00000800" complete_cpuset="0x00000800" online_cpuset="0x00000800" allowed_cpuset="0x00000800">
              <object type="PU" os_index="11" cpuset="0x00000800" complete_cpuset="0x00000800" online_cpuset="0x00000800" allowed_cpuset="0x00000800"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00001000" complete_cpuset="0x00001000" online_cpuset="0x00001000" allowed_cpuset="0x00001000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00001000" complete_cpuset="0x00001000" online_cpuset="0x00001000" allowed_cpuset="0x00001000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="1626" cpuset="0x00001000" complete_cpuset="0x00001000" online_cpuset="0x00001000" allowed_cpuset="0x00001000">
              <object type="PU" os_index="12" cpuset="0x00001000" complete_cpuset="0x00001000" online_cpuset="0x00001000" allowed_cpuset="0x00001000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00002000" complete_cpuset="0x00002000" online_cpuset="0x00002000" allowed_cpuset="0x00002000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00002000" complete_cpuset="0x00002000" online_cpuset="0x00002000" allowed_cpuset="0x00002000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="1750" cpuset="0x00002000" complete_cpuset="0x00002000" online_cpuset="0x00002000" allowed_cpuset="0x00002000">
              <object type="PU" os_index="13" cpuset="0x00002000" complete_cpuset="0x00002000" online_cpuset="0x00002000" allowed_cpuset="0x00002000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00004000" complete_cpuset="0x00004000" online_cpuset="0x00004000" allowed_cpuset="0x00004000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00004000" complete_cpuset="0x00004000" online_cpuset="0x00004000" allowed_cpuset="0x00004000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="1874" cpuset="0x00004000" complete_cpuset="0x00004000" online_cpuset="0x00004000" allowed_cpuset="0x00004000">
              <object type="PU" os_index="14" cpuset="0x00004000" complete_cpuset="0x00004000" online_cpuset="0x00004000" allowed_cpuset="0x00004000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00008000" complete_cpuset="0x00008000" online_cpuset="0x00008000" allowed_cpuset="0x00008000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00008000" complete_cpuset="0x00008000" online_cpuset="0x00008000" allowed_cpuset="0x00008000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="1998" cpuset="0x00008000" complete_cpuset="0x00008000" online_cpuset="0x00008000" allowed_cpuset="0x00008000">
              <object type="PU" os_index="15" cpuset="0x00008000" complete_cpuset="0x00008000" online_cpuset="0x00008000" allowed_cpuset="0x00008000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00010000" complete_cpuset="0x00010000" online_cpuset="0x00010000" allowed_cpuset="0x00010000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00010000" complete_cpuset="0x00010000" online_cpuset="0x00010000" allowed_cpuset="0x00010000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="2122" cpuset="0x00010000" complete_cpuset="0x00010000" online_cpuset="0x00010000" allowed_cpuset="0x00010000">
              <object type="PU" os_index="16" cpuset="0x00010000" complete_cpuset="0x00010000" online_cpuset="0x00010000" allowed_cpuset="0x00010000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00020000" complete_cpuset="0x00020000" online_cpuset="0x00020000" allowed_cpuset="0x00020000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00020000" complete_cpuset="0x00020000" online_cpuset="0x00020000" allowed_cpuset="0x00020000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="2246" cpuset="0x00020000" complete_cpuset="0x00020000" online_cpuset="0x00020000" allowed_cpuset="0x00020000">
              <object type="PU" os_index="17" cpuset="0x00020000" complete_cpuset="0x00020000" online_cpuset="0x00020000" allowed_cpuset="0x00020000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00040000" complete_cpuset="0x00040000" online_cpuset="0x00040000" allowed_cpuset="0x00040000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00040000" complete_cpuset="0x00040000" online_cpuset="0x00040000" allowed_cpuset="0x00040000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="2370" cpuset="0x00040000" complete_cpuset="0x00040000" online_cpuset="0x00040000" allowed_cpuset="0x00040000">
              <object type="PU" os_index="18" cpuset="0x00040000" complete_cpuset="0x00040000" online_cpuset="0x00040000" allowed_cpuset="0x00040000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00080000" complete_cpuset="0x00080000" online_cpuset="0x00080000" allowed_cpuset="0x00080000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00080000" complete_cpuset="0x00080000" online_cpuset="0x00080000" allowed_cpuset="0x00080000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="2494" cpuset="0x00080000" complete_cpuset="0x00080000" online_cpuset="0x00080000" allowed_cpuset="0x00080000">
              <object type="PU" os_index="19" cpuset="0x00080000" complete_cpuset="0x00080000" online_cpuset="0x00080000" allowed_cpuset="0x00080000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00100000" complete_cpuset="0x00100000" online_cpuset="0x00100000" allowed_cpuset="0x00100000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00100000" complete_cpuset="0x00100000" online_cpuset="0x00100000" allowed_cpuset="0x00100000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="2618" cpuset="0x00100000" complete_cpuset="0x00100000" online_cpuset="0x00100000" allowed_cpuset="0x00100000">
              <object type="PU" os_index="20" cpuset="0x00100000" complete_cpuset="0x00100000" online_cpuset="0x00100000" allowed_cpuset="0x00100000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00200000" complete_cpuset="0x00200000" online_cpuset="0x00200000" allowed_cpuset="0x00200000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00200000" complete_cpuset="0x00200000" online_cpuset="0x00200000" allowed_cpuset="0x00200000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="2742" cpuset="0x00200000" complete_cpuset="0x00200000" online_cpuset="0x00200000" allowed_cpuset="0x00200000">
              <object type="PU" os_index="21" cpuset="0x00200000" complete_cpuset="0x00200000" online_cpuset="0x00200000" allowed_cpuset="0x00200000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00400000" complete_cpuset="0x00400000" online_cpuset="0x00400000" allowed_cpuset="0x00400000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00400000" complete_cpuset="0x00400000" online_cpuset="0x00400000" allowed_cpuset="0x00400000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="2866" cpuset="0x00400000" complete_cpuset="0x00400000" online_cpuset="0x00400000" allowed_cpuset="0x00400000">
              <object type="PU" os_index="22" cpuset="0x00400000" complete_cpuset="0x00400000" online_cpuset="0x00400000" allowed_cpuset="0x00400000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00800000" complete_cpuset="0x00800000" online_cpuset="0x00800000" allowed_cpuset="0x00800000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00800000" complete_cpuset="0x00800000" online_cpuset="0x00800000" allowed_cpuset="0x00800000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="2990" cpuset="0x00800000" complete_cpuset="0x00800000" online_cpuset="0x00800000" allowed_cpuset="0x00800000">
              <object type="PU" os_index="23" cpuset="0x00800000" complete_cpuset="0x00800000" online_cpuset="0x00800000" allowed_cpuset="0x00800000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x01000000" complete_cpuset="0x01000000" online_cpuset="0x01000000" allowed_cpuset="0x01000000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x01000000" complete_cpuset="0x01000000" online_cpuset="0x01000000" allowed_cpuset="0x01000000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="3114" cpuset="0x01000000" complete_cpuset="0x01000000" online_cpuset="0x01000000" allowed_cpuset="0x01000000">
              <object type="PU" os_index="24" cpuset="0x01000000" complete_cpuset="0x01000000" online_cpuset="0x01000000" allowed_cpuset="0x01000000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x02000000" complete_cpuset="0x02000000" online_cpuset="0x02000000" allowed_cpuset="0x02000000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x02000000" complete_cpuset="0x02000000" online_cpuset="0x02000000" allowed_cpuset="0x02000000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="3238" cpuset="0x02000000" complete_cpuset="0x02000000" online_cpuset="0x02000000" allowed_cpuset="0x02000000">
              <object type="PU" os_index="25" cpuset="0x02000000" complete_cpuset="0x02000000" online_cpuset="0x02000000" allowed_cpuset="0x02000000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x04000000" complete_cpuset="0x04000000" online_cpuset="0x04000000" allowed_cpuset="0x04000000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x04000000" complete_cpuset="0x04000000" online_cpuset="0x04000000" allowed_cpuset="0x04000000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="3362" cpuset="0x04000000" complete_cpuset="0x04000000" online_cpuset="0x04000000" allowed_cpuset="0x04000000">
              <object type="PU" os_index="26" cpuset="0x04000000" complete_cpuset="0x04000000" online_cpuset="0x04000000" allowed_cpuset="0x04000000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x08000000" complete_cpuset="0x08000000" online_cpuset="0x08000000" allowed_cpuset="0x08000000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x08000000" complete_cpuset="0x08000000" online_cpuset="0x08000000" allowed_cpuset="0x08000000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="3486" cpuset="0x08000000" complete_cpuset="0x08000000" online_cpuset="0x08000000" allowed_cpuset="0x08000000">
              <object type="PU" os_index="27" cpuset="0x08000000" complete_cpuset="0x08000000" online_cpuset="0x08000000" allowed_cpuset="0x08000000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x10000000" complete_cpuset="0x10000000" online_cpuset="0x10000000" allowed_cpuset="0x10000000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x10000000" complete_cpuset="0x10000000" online_cpuset="0x10000000" allowed_cpuset="0x10000000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="3610" cpuset="0x10000000" complete_cpuset="0x10000000" online_cpuset="0x10000000" allowed_cpuset="0x10000000">
              <object type="PU" os_index="28" cpuset="0x10000000" complete_cpuset="0x10000000" online_cpuset="0x10000000" allowed_cpuset="0x10000000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x20000000" complete_cpuset="0x20000000" online_cpuset="0x20000000" allowed_cpuset="0x20000000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x20000000" complete_cpuset="0x20000000" online_cpuset="0x20000000" allowed_cpuset="0x20000000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="3734" cpuset="0x20000000" complete_cpuset="0x20000000" online_cpuset="0x20000000" allowed_cpuset="0x20000000">
              <object type="PU" os_index="29" cpuset="0x20000000" complete_cpuset="0x20000000" online_cpuset="0x20000000" allowed_cpuset="0x20000000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x40000000" complete_cpuset="0x40000000" online_cpuset="0x40000000" allowed_cpuset="0x40000000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x40000000" complete_cpuset="0x40000000" online_cpuset="0x40000000" allowed_cpuset="0x40000000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="3858" cpuset="0x40000000" complete_cpuset="0x40000000" online_cpuset="0x40000000" allowed_cpuset="0x40000000">
              <object type="PU" os_index="30" cpuset="0x40000000" complete_cpuset="0x40000000" online_cpuset="0x40000000" allowed_cpuset="0x40000000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x80000000" complete_cpuset="0x80000000" online_cpuset="0x80000000" allowed_cpuset="0x80000000" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x80000000" complete_cpuset="0x80000000" online_cpuset="0x80000000" allowed_cpuset="0x80000000" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="3982" cpuset="0x80000000" complete_cpuset="0x80000000" online_cpuset="0x80000000" allowed_cpuset="0x80000000">
              <object type="PU" os_index="31" cpuset="0x80000000" complete_cpuset="0x80000000" online_cpuset="0x80000000" allowed_cpuset="0x80000000"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000001,0x0" complete_cpuset="0x00000001,0x0" online_cpuset="0x00000001,0x0" allowed_cpuset="0x00000001,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000001,0x0" complete_cpuset="0x00000001,0x0" online_cpuset="0x00000001,0x0" allowed_cpuset="0x00000001,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="4106" cpuset="0x00000001,0x0" complete_cpuset="0x00000001,0x0" online_cpuset="0x00000001,0x0" allowed_cpuset="0x00000001,0x0">
              <object type="PU" os_index="32" cpuset="0x00000001,0x0" complete_cpuset="0x00000001,0x0" online_cpuset="0x00000001,0x0" allowed_cpuset="0x00000001,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000002,0x0" complete_cpuset="0x00000002,0x0" online_cpuset="0x00000002,0x0" allowed_cpuset="0x00000002,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000002,0x0" complete_cpuset="0x00000002,0x0" online_cpuset="0x00000002,0x0" allowed_cpuset="0x00000002,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="4230" cpuset="0x00000002,0x0" complete_cpuset="0x00000002,0x0" online_cpuset="0x00000002,0x0" allowed_cpuset="0x00000002,0x0">
              <object type="PU" os_index="33" cpuset="0x00000002,0x0" complete_cpuset="0x00000002,0x0" online_cpuset="0x00000002,0x0" allowed_cpuset="0x00000002,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000004,0x0" complete_cpuset="0x00000004,0x0" online_cpuset="0x00000004,0x0" allowed_cpuset="0x00000004,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000004,0x0" complete_cpuset="0x00000004,0x0" online_cpuset="0x00000004,0x0" allowed_cpuset="0x00000004,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="4354" cpuset="0x00000004,0x0" complete_cpuset="0x00000004,0x0" online_cpuset="0x00000004,0x0" allowed_cpuset="0x00000004,0x0">
              <object type="PU" os_index="34" cpuset="0x00000004,0x0" complete_cpuset="0x00000004,0x0" online_cpuset="0x00000004,0x0" allowed_cpuset="0x00000004,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000008,0x0" complete_cpuset="0x00000008,0x0" online_cpuset="0x00000008,0x0" allowed_cpuset="0x00000008,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000008,0x0" complete_cpuset="0x00000008,0x0" online_cpuset="0x00000008,0x0" allowed_cpuset="0x00000008,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="4478" cpuset="0x00000008,0x0" complete_cpuset="0x00000008,0x0" online_cpuset="0x00000008,0x0" allowed_cpuset="0x00000008,0x0">
              <object type="PU" os_index="35" cpuset="0x00000008,0x0" complete_cpuset="0x00000008,0x0" online_cpuset="0x00000008,0x0" allowed_cpuset="0x00000008,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000010,0x0" complete_cpuset="0x00000010,0x0" online_cpuset="0x00000010,0x0" allowed_cpuset="0x00000010,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000010,0x0" complete_cpuset="0x00000010,0x0" online_cpuset="0x00000010,0x0" allowed_cpuset="0x00000010,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="4602" cpuset="0x00000010,0x0" complete_cpuset="0x00000010,0x0" online_cpuset="0x00000010,0x0" allowed_cpuset="0x00000010,0x0">
              <object type="PU" os_index="36" cpuset="0x00000010,0x0" complete_cpuset="0x00000010,0x0" online_cpuset="0x00000010,0x0" allowed_cpuset="0x00000010,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000020,0x0" complete_cpuset="0x00000020,0x0" online_cpuset="0x00000020,0x0" allowed_cpuset="0x00000020,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000020,0x0" complete_cpuset="0x00000020,0x0" online_cpuset="0x00000020,0x0" allowed_cpuset="0x00000020,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="4726" cpuset="0x00000020,0x0" complete_cpuset="0x00000020,0x0" online_cpuset="0x00000020,0x0" allowed_cpuset="0x00000020,0x0">
              <object type="PU" os_index="37" cpuset="0x00000020,0x0" complete_cpuset="0x00000020,0x0" online_cpuset="0x00000020,0x0" allowed_cpuset="0x00000020,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000040,0x0" complete_cpuset="0x00000040,0x0" online_cpuset="0x00000040,0x0" allowed_cpuset="0x00000040,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000040,0x0" complete_cpuset="0x00000040,0x0" online_cpuset="0x00000040,0x0" allowed_cpuset="0x00000040,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="4850" cpuset="0x00000040,0x0" complete_cpuset="0x00000040,0x0" online_cpuset="0x00000040,0x0" allowed_cpuset="0x00000040,0x0">
              <object type="PU" os_index="38" cpuset="0x00000040,0x0" complete_cpuset="0x00000040,0x0" online_cpuset="0x00000040,0x0" allowed_cpuset="0x00000040,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000080,0x0" complete_cpuset="0x00000080,0x0" online_cpuset="0x00000080,0x0" allowed_cpuset="0x00000080,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000080,0x0" complete_cpuset="0x00000080,0x0" online_cpuset="0x00000080,0x0" allowed_cpuset="0x00000080,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="4974" cpuset="0x00000080,0x0" complete_cpuset="0x00000080,0x0" online_cpuset="0x00000080,0x0" allowed_cpuset="0x00000080,0x0">
              <object type="PU" os_index="39" cpuset="0x00000080,0x0" complete_cpuset="0x00000080,0x0" online_cpuset="0x00000080,0x0" allowed_cpuset="0x00000080,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000100,0x0" complete_cpuset="0x00000100,0x0" online_cpuset="0x00000100,0x0" allowed_cpuset="0x00000100,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000100,0x0" complete_cpuset="0x00000100,0x0" online_cpuset="0x00000100,0x0" allowed_cpuset="0x00000100,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="5098" cpuset="0x00000100,0x0" complete_cpuset="0x00000100,0x0" online_cpuset="0x00000100,0x0" allowed_cpuset="0x00000100,0x0">
              <object type="PU" os_index="40" cpuset="0x00000100,0x0" complete_cpuset="0x00000100,0x0" online_cpuset="0x00000100,0x0" allowed_cpuset="0x00000100,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000200,0x0" complete_cpuset="0x00000200,0x0" online_cpuset="0x00000200,0x0" allowed_cpuset="0x00000200,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000200,0x0" complete_cpuset="0x00000200,0x0" online_cpuset="0x00000200,0x0" allowed_cpuset="0x00000200,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="5222" cpuset="0x00000200,0x0" complete_cpuset="0x00000200,0x0" online_cpuset="0x00000200,0x0" allowed_cpuset="0x00000200,0x0">
              <object type="PU" os_index="41" cpuset="0x00000200,0x0" complete_cpuset="0x00000200,0x0" online_cpuset="0x00000200,0x0" allowed_cpuset="0x00000200,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000400,0x0" complete_cpuset="0x00000400,0x0" online_cpuset="0x00000400,0x0" allowed_cpuset="0x00000400,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000400,0x0" complete_cpuset="0x00000400,0x0" online_cpuset="0x00000400,0x0" allowed_cpuset="0x00000400,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="5346" cpuset="0x00000400,0x0" complete_cpuset="0x00000400,0x0" online_cpuset="0x00000400,0x0" allowed_cpuset="0x00000400,0x0">
              <object type="PU" os_index="42" cpuset="0x00000400,0x0" complete_cpuset="0x00000400,0x0" online_cpuset="0x00000400,0x0" allowed_cpuset="0x00000400,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00000800,0x0" complete_cpuset="0x00000800,0x0" online_cpuset="0x00000800,0x0" allowed_cpuset="0x00000800,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00000800,0x0" complete_cpuset="0x00000800,0x0" online_cpuset="0x00000800,0x0" allowed_cpuset="0x00000800,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="5470" cpuset="0x00000800,0x0" complete_cpuset="0x00000800,0x0" online_cpuset="0x00000800,0x0" allowed_cpuset="0x00000800,0x0">
              <object type="PU" os_index="43" cpuset="0x00000800,0x0" complete_cpuset="0x00000800,0x0" online_cpuset="0x00000800,0x0" allowed_cpuset="0x00000800,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00001000,0x0" complete_cpuset="0x00001000,0x0" online_cpuset="0x00001000,0x0" allowed_cpuset="0x00001000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00001000,0x0" complete_cpuset="0x00001000,0x0" online_cpuset="0x00001000,0x0" allowed_cpuset="0x00001000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="5594" cpuset="0x00001000,0x0" complete_cpuset="0x00001000,0x0" online_cpuset="0x00001000,0x0" allowed_cpuset="0x00001000,0x0">
              <object type="PU" os_index="44" cpuset="0x00001000,0x0" complete_cpuset="0x00001000,0x0" online_cpuset="0x00001000,0x0" allowed_cpuset="0x00001000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00002000,0x0" complete_cpuset="0x00002000,0x0" online_cpuset="0x00002000,0x0" allowed_cpuset="0x00002000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00002000,0x0" complete_cpuset="0x00002000,0x0" online_cpuset="0x00002000,0x0" allowed_cpuset="0x00002000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="5718" cpuset="0x00002000,0x0" complete_cpuset="0x00002000,0x0" online_cpuset="0x00002000,0x0" allowed_cpuset="0x00002000,0x0">
              <object type="PU" os_index="45" cpuset="0x00002000,0x0" complete_cpuset="0x00002000,0x0" online_cpuset="0x00002000,0x0" allowed_cpuset="0x00002000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00004000,0x0" complete_cpuset="0x00004000,0x0" online_cpuset="0x00004000,0x0" allowed_cpuset="0x00004000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00004000,0x0" complete_cpuset="0x00004000,0x0" online_cpuset="0x00004000,0x0" allowed_cpuset="0x00004000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="5842" cpuset="0x00004000,0x0" complete_cpuset="0x00004000,0x0" online_cpuset="0x00004000,0x0" allowed_cpuset="0x00004000,0x0">
              <object type="PU" os_index="46" cpuset="0x00004000,0x0" complete_cpuset="0x00004000,0x0" online_cpuset="0x00004000,0x0" allowed_cpuset="0x00004000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00008000,0x0" complete_cpuset="0x00008000,0x0" online_cpuset="0x00008000,0x0" allowed_cpuset="0x00008000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00008000,0x0" complete_cpuset="0x00008000,0x0" online_cpuset="0x00008000,0x0" allowed_cpuset="0x00008000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="5966" cpuset="0x00008000,0x0" complete_cpuset="0x00008000,0x0" online_cpuset="0x00008000,0x0" allowed_cpuset="0x00008000,0x0">
              <object type="PU" os_index="47" cpuset="0x00008000,0x0" complete_cpuset="0x00008000,0x0" online_cpuset="0x00008000,0x0" allowed_cpuset="0x00008000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00010000,0x0" complete_cpuset="0x00010000,0x0" online_cpuset="0x00010000,0x0" allowed_cpuset="0x00010000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00010000,0x0" complete_cpuset="0x00010000,0x0" online_cpuset="0x00010000,0x0" allowed_cpuset="0x00010000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="6090" cpuset="0x00010000,0x0" complete_cpuset="0x00010000,0x0" online_cpuset="0x00010000,0x0" allowed_cpuset="0x00010000,0x0">
              <object type="PU" os_index="48" cpuset="0x00010000,0x0" complete_cpuset="0x00010000,0x0" online_cpuset="0x00010000,0x0" allowed_cpuset="0x00010000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00020000,0x0" complete_cpuset="0x00020000,0x0" online_cpuset="0x00020000,0x0" allowed_cpuset="0x00020000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00020000,0x0" complete_cpuset="0x00020000,0x0" online_cpuset="0x00020000,0x0" allowed_cpuset="0x00020000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="6214" cpuset="0x00020000,0x0" complete_cpuset="0x00020000,0x0" online_cpuset="0x00020000,0x0" allowed_cpuset="0x00020000,0x0">
              <object type="PU" os_index="49" cpuset="0x00020000,0x0" complete_cpuset="0x00020000,0x0" online_cpuset="0x00020000,0x0" allowed_cpuset="0x00020000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00040000,0x0" complete_cpuset="0x00040000,0x0" online_cpuset="0x00040000,0x0" allowed_cpuset="0x00040000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00040000,0x0" complete_cpuset="0x00040000,0x0" online_cpuset="0x00040000,0x0" allowed_cpuset="0x00040000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="6338" cpuset="0x00040000,0x0" complete_cpuset="0x00040000,0x0" online_cpuset="0x00040000,0x0" allowed_cpuset="0x00040000,0x0">
              <object type="PU" os_index="50" cpuset="0x00040000,0x0" complete_cpuset="0x00040000,0x0" online_cpuset="0x00040000,0x0" allowed_cpuset="0x00040000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00080000,0x0" complete_cpuset="0x00080000,0x0" online_cpuset="0x00080000,0x0" allowed_cpuset="0x00080000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00080000,0x0" complete_cpuset="0x00080000,0x0" online_cpuset="0x00080000,0x0" allowed_cpuset="0x00080000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="6462" cpuset="0x00080000,0x0" complete_cpuset="0x00080000,0x0" online_cpuset="0x00080000,0x0" allowed_cpuset="0x00080000,0x0">
              <object type="PU" os_index="51" cpuset="0x00080000,0x0" complete_cpuset="0x00080000,0x0" online_cpuset="0x00080000,0x0" allowed_cpuset="0x00080000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00100000,0x0" complete_cpuset="0x00100000,0x0" online_cpuset="0x00100000,0x0" allowed_cpuset="0x00100000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00100000,0x0" complete_cpuset="0x00100000,0x0" online_cpuset="0x00100000,0x0" allowed_cpuset="0x00100000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="6586" cpuset="0x00100000,0x0" complete_cpuset="0x00100000,0x0" online_cpuset="0x00100000,0x0" allowed_cpuset="0x00100000,0x0">
              <object type="PU" os_index="52" cpuset="0x00100000,0x0" complete_cpuset="0x00100000,0x0" online_cpuset="0x00100000,0x0" allowed_cpuset="0x00100000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00200000,0x0" complete_cpuset="0x00200000,0x0" online_cpuset="0x00200000,0x0" allowed_cpuset="0x00200000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00200000,0x0" complete_cpuset="0x00200000,0x0" online_cpuset="0x00200000,0x0" allowed_cpuset="0x00200000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="6710" cpuset="0x00200000,0x0" complete_cpuset="0x00200000,0x0" online_cpuset="0x00200000,0x0" allowed_cpuset="0x00200000,0x0">
              <object type="PU" os_index="53" cpuset="0x00200000,0x0" complete_cpuset="0x00200000,0x0" online_cpuset="0x00200000,0x0" allowed_cpuset="0x00200000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00400000,0x0" complete_cpuset="0x00400000,0x0" online_cpuset="0x00400000,0x0" allowed_cpuset="0x00400000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00400000,0x0" complete_cpuset="0x00400000,0x0" online_cpuset="0x00400000,0x0" allowed_cpuset="0x00400000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="6834" cpuset="0x00400000,0x0" complete_cpuset="0x00400000,0x0" online_cpuset="0x00400000,0x0" allowed_cpuset="0x00400000,0x0">
              <object type="PU" os_index="54" cpuset="0x00400000,0x0" complete_cpuset="0x00400000,0x0" online_cpuset="0x00400000,0x0" allowed_cpuset="0x00400000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x00800000,0x0" complete_cpuset="0x00800000,0x0" online_cpuset="0x00800000,0x0" allowed_cpuset="0x00800000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x00800000,0x0" complete_cpuset="0x00800000,0x0" online_cpuset="0x00800000,0x0" allowed_cpuset="0x00800000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="6958" cpuset="0x00800000,0x0" complete_cpuset="0x00800000,0x0" online_cpuset="0x00800000,0x0" allowed_cpuset="0x00800000,0x0">
              <object type="PU" os_index="55" cpuset="0x00800000,0x0" complete_cpuset="0x00800000,0x0" online_cpuset="0x00800000,0x0" allowed_cpuset="0x00800000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x01000000,0x0" complete_cpuset="0x01000000,0x0" online_cpuset="0x01000000,0x0" allowed_cpuset="0x01000000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x01000000,0x0" complete_cpuset="0x01000000,0x0" online_cpuset="0x01000000,0x0" allowed_cpuset="0x01000000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="7082" cpuset="0x01000000,0x0" complete_cpuset="0x01000000,0x0" online_cpuset="0x01000000,0x0" allowed_cpuset="0x01000000,0x0">
              <object type="PU" os_index="56" cpuset="0x01000000,0x0" complete_cpuset="0x01000000,0x0" online_cpuset="0x01000000,0x0" allowed_cpuset="0x01000000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x02000000,0x0" complete_cpuset="0x02000000,0x0" online_cpuset="0x02000000,0x0" allowed_cpuset="0x02000000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x02000000,0x0" complete_cpuset="0x02000000,0x0" online_cpuset="0x02000000,0x0" allowed_cpuset="0x02000000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="7206" cpuset="0x02000000,0x0" complete_cpuset="0x02000000,0x0" online_cpuset="0x02000000,0x0" allowed_cpuset="0x02000000,0x0">
              <object type="PU" os_index="57" cpuset="0x02000000,0x0" complete_cpuset="0x02000000,0x0" online_cpuset="0x02000000,0x0" allowed_cpuset="0x02000000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x04000000,0x0" complete_cpuset="0x04000000,0x0" online_cpuset="0x04000000,0x0" allowed_cpuset="0x04000000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x04000000,0x0" complete_cpuset="0x04000000,0x0" online_cpuset="0x04000000,0x0" allowed_cpuset="0x04000000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="7330" cpuset="0x04000000,0x0" complete_cpuset="0x04000000,0x0" online_cpuset="0x04000000,0x0" allowed_cpuset="0x04000000,0x0">
              <object type="PU" os_index="58" cpuset="0x04000000,0x0" complete_cpuset="0x04000000,0x0" online_cpuset="0x04000000,0x0" allowed_cpuset="0x04000000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x08000000,0x0" complete_cpuset="0x08000000,0x0" online_cpuset="0x08000000,0x0" allowed_cpuset="0x08000000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x08000000,0x0" complete_cpuset="0x08000000,0x0" online_cpuset="0x08000000,0x0" allowed_cpuset="0x08000000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="7454" cpuset="0x08000000,0x0" complete_cpuset="0x08000000,0x0" online_cpuset="0x08000000,0x0" allowed_cpuset="0x08000000,0x0">
              <object type="PU" os_index="59" cpuset="0x08000000,0x0" complete_cpuset="0x08000000,0x0" online_cpuset="0x08000000,0x0" allowed_cpuset="0x08000000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x10000000,0x0" complete_cpuset="0x10000000,0x0" online_cpuset="0x10000000,0x0" allowed_cpuset="0x10000000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x10000000,0x0" complete_cpuset="0x10000000,0x0" online_cpuset="0x10000000,0x0" allowed_cpuset="0x10000000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="7578" cpuset="0x10000000,0x0" complete_cpuset="0x10000000,0x0" online_cpuset="0x10000000,0x0" allowed_cpuset="0x10000000,0x0">
              <object type="PU" os_index="60" cpuset="0x10000000,0x0" complete_cpuset="0x10000000,0x0" online_cpuset="0x10000000,0x0" allowed_cpuset="0x10000000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x20000000,0x0" complete_cpuset="0x20000000,0x0" online_cpuset="0x20000000,0x0" allowed_cpuset="0x20000000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x20000000,0x0" complete_cpuset="0x20000000,0x0" online_cpuset="0x20000000,0x0" allowed_cpuset="0x20000000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="7702" cpuset="0x20000000,0x0" complete_cpuset="0x20000000,0x0" online_cpuset="0x20000000,0x0" allowed_cpuset="0x20000000,0x0">
              <object type="PU" os_index="61" cpuset="0x20000000,0x0" complete_cpuset="0x20000000,0x0" online_cpuset="0x20000000,0x0" allowed_cpuset="0x20000000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x40000000,0x0" complete_cpuset="0x40000000,0x0" online_cpuset="0x40000000,0x0" allowed_cpuset="0x40000000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x40000000,0x0" complete_cpuset="0x40000000,0x0" online_cpuset="0x40000000,0x0" allowed_cpuset="0x40000000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="7826" cpuset="0x40000000,0x0" complete_cpuset="0x40000000,0x0" online_cpuset="0x40000000,0x0" allowed_cpuset="0x40000000,0x0">
              <object type="PU" os_index="62" cpuset="0x40000000,0x0" complete_cpuset="0x40000000,0x0" online_cpuset="0x40000000,0x0" allowed_cpuset="0x40000000,0x0"/>
            </object>
          </object>
        </object>
        <object type="Cache" cpuset="0x80000000,0x0" complete_cpuset="0x80000000,0x0" online_cpuset="0x80000000,0x0" allowed_cpuset="0x80000000,0x0" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="8" cache_type="0">
          <object type="Cache" cpuset="0x80000000,0x0" complete_cpuset="0x80000000,0x0" online_cpuset="0x80000000,0x0" allowed_cpuset="0x80000000,0x0" cache_size="65536" depth="1" cache_linesize="64" cache_associativity="4" cache_type="1">
            <object type="Core" os_index="7950" cpuset="0x80000000,0x0" complete_cpuset="0x80000000,0x0" online_cpuset="0x80000000,0x0" allowed_cpuset="0x80000000,0x0">
              <object type="PU" os_index="63" cpuset="0x80000000,0x0" complete_cpuset="0x80000000,0x0" online_cpuset="0x80000000,0x0" allowed_cpuset="0x80000000,0x0"/>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
</topology>

```

## Lonnegan | 2020-08-13T14:47:12+00:00
> I just wondering about the HS/s that the systems is archiving. Without any "setup" XMRIG only use 16 Cores of the system
> Any hints?

That's normal. RandomX works with 2 MB scratchpad size per thread. To mine fast, it's ideal to hold the scratchpads in the caches. Your ARM cpu has only 32 MB of L3 cache. That's just enough for 16 threads. That's why xmrig chooses 16 threads, not 64.

If you set 64 threads manually, the system has to access DRAM all the time, which is much slower than cache accesses.

14 KH/s is not so bad for an ARM cpu. You can't compare it with an AMD EPYC! Modern AMD and Intel archs have much higher IPC than ARM. Your 14 KH/s are round about the performance of one Ryzen 9 3900X 12c/24t, which is not bad. An AMD EPYC 7V12 e.g. with 64c/128t ist around 56 KH/s.

Wownero has got a scratchpad size of just 1 MB, so you can mine with 32 threads without having to access the slow DRAM.

## SChernykh | 2020-08-13T15:20:35+00:00
> Wownero has got a scratchpad size of just 1 MB, so you can mine with 32 threads without having to access the slow DRAM.

He has 64 core CPU, each core with 1 MB L2 cache. Wownero is perfect for this, I think it'll be much more than 14300 h/s. But even with 2 MB scratchpad, 1 MB cache per core helps a lot because the most accessed part of RandomX scratchpad is only 256 KB in size, so it only translates to probably 2-3x more DRAM accesses.

P.S. 14300 h/s is the highest hashrate I've ever seen on any ARM CPU, so really there's nothing to complain about.

## Lonnegan | 2020-08-13T15:29:13+00:00
> > Wownero has got a scratchpad size of just 1 MB, so you can mine with 32 threads without having to access the slow DRAM.
> 
> He has 64 core CPU, each core with 1 MB L2 cache. Wownero is perfect for this

Yes, you are right! Just looked at the L3 cache. Wow, yes, Wownero would fit into the L2 cache of each core, so you can run 64 threads. That's perfect for this CPU. Please post the hashrate here, I'm interested in! 👍 

## xmrig | 2020-08-13T15:32:43+00:00
@Slurprmx also how many memory channels do you use?
@Lonnegan hwloc did't report L2 cache inclusive or not, so it locked only to L3 too, 16 threads is a bug.


## Lonnegan | 2020-08-13T15:46:19+00:00
I'm not the expert in ARM server systems, but I've found the string "R281-T94" in the dump. Is it that system then?
https://www.gigabyte.com/ARM-Server/R281-T94-rev-100/sp#sp

So it's not one CPU with 64 cores, but two Marvell® ThunderX2® CN9980 ARM processors with 32 cores each. But xmrig says "NUMA node(s): 1". Either ThunderX2 doesn't support ccNUMA or the detection is wrong and there are 2 NUMA nodes.

And if it is that system, the detection of L1 and L2 cache is wrong, too. CN9980 doesn't have 1 MB L2 each core, but only 256 KB:
https://www.marvell.com/content/dam/marvell/en/public-collateral/server-processors/marvell-server-processors-thunderx-cn99xx-product-brief-2019.pdf
https://en.wikichip.org/wiki/cavium/thunderx2/cn9980

## xmrig | 2020-08-13T23:59:07+00:00
This is very likely a `m6g.metal` instance https://aws.amazon.com/ec2/instance-types/m6/

## xmrig | 2020-08-16T04:24:42+00:00
Wownero hashrate is 20888 h/s

## xmrig | 2020-08-20T06:48:17+00:00
Auto configuration fixed https://github.com/xmrig/xmrig/releases/tag/v6.3.2
Thank you.

# Action History
- Created by: Slurprmx | 2020-08-13T10:16:11+00:00
- Closed at: 2020-08-28T16:28:31+00:00
