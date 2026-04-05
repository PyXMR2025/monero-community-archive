---
title: 2.99.x cn/pico hashrate drop
source_url: https://github.com/xmrig/xmrig/issues/1105
author: fadatsai
assignees: []
labels:
- bug
created_at: '2019-08-07T09:39:31+00:00'
updated_at: '2019-08-09T09:45:34+00:00'
type: issue
status: closed
closed_at: '2019-08-09T09:45:34+00:00'
---

# Original Description
When I mining TRTL use version 2.14.1, I can set "low_power_mode:2" to get a higher hashrate, but I can't set low_power_mode on 2.99.x

-----------------------------------------------------------------------------
2.14.1 Hashrate 31KH/s
* ABOUT XMRig/2.14.1 gcc/5.2.1 * LIBS libuv/1.23.2 OpenSSL/1.0.1e
* CPU Intel(R) Xeon(R) Gold 6146 CPU @ 3.20GHz (1) x64 AES AVX2
* CPU L2/L3 12.0 MB/24.8 MB * THREADS 24, cryptonight-pico/trtl
* ASSEMBLY auto:intel * POOL #1 1.1.1.1:9999 variant trtl
* COMMANDS hashrate, pause, resume 
[2019-08-07 17:29:14] READY   **(CPU) threads 24(48)** huge pages 24/24 100% memory 12288 KB
[2019-08-07 17:31:18] speed 10s/60s/15m **30999.6 31029.6 n/a H/s max 31293.9 H/s**
-------------------------------------------------------------------------------
2.99.0  Hashrate 17KH/s
 * ABOUT        XMRig/2.99.0-beta gcc/7.3.1
 * LIBS         libuv/1.23.2 OpenSSL/1.0.1e
 * CPU          Intel(R) Xeon(R) Gold 6146 CPU @ 3.20GHz (1) x64 AES AVX2
 * CPU L2/L3    12.0 MB/24.8 MB
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      1.1.1.1:9999 algo auto
 * COMMANDS     hashrate, pause, resume
[2019-08-07 17:33:03.427] CPU use profile  cn-pico  (24 threads) scratchpad 256 KB
[2019-08-07 17:33:03.446] CPU **READY threads 24(24)** huge pages 24/24 100% memory 6144 KB (19 ms)
[2019-08-07 17:34:03.653] speed 10s/60s/15m  **17510.2 n/a n/a H/s max 17935.3 H/s**


# Discussion History
## xmrig | 2019-08-07T10:12:36+00:00
Please update to recent version 2.99.4 with hwloc, remove `cpu` object from config to allow new version fill it again, then transform `cn-pico` object from short format to long https://github.com/xmrig/xmrig/blob/evo/doc/CPU.md `"intensity": 2,` is equivalent of `"low_power_mode:2"` or paste it here, I transform it for you, because right now no simple way to do it.

Also please run `./xmrig --export-topology` and attach `topology.xml` to this issue, it helps improve autoconfig.
Thank you.

## xmrig | 2019-08-07T17:27:05+00:00
Done https://github.com/xmrig/xmrig/commit/9a842a593b2d7a0148a6bdfb77e584c3af2064b4 new version (2.99.5) will use low_power_mode:2 by default for this algorithm, but request about topology.xml is still actual.
Thank you.

## fadatsai | 2019-08-08T02:36:43+00:00
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topology SYSTEM "hwloc2.dtd">
<topology version="2.0">
  <object type="Machine" os_index="0" cpuset="0x00ffffff" complete_cpuset="0x00ffffff" allowed_cpuset="0x00ffffff" nodeset="0x00000001" complete_nodeset="0x00000001" allowed_nodeset="0x00000001" gp_index="1">

    <object type="NUMANode" os_index="0" cpuset="0x00ffffff" complete_cpuset="0x00ffffff" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="102" local_memory="410779004928">
      <page_type size="4096" count="99632483"/>
      <page_type size="2097152" count="1280"/>
    </object>
    <object type="Package" os_index="0" cpuset="0x00555555" complete_cpuset="0x00555555" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="2">
      <info name="CPUVendor" value="GenuineIntel"/>
      <info name="CPUFamilyNumber" value="6"/>
      <info name="CPUModelNumber" value="85"/>
      <info name="CPUModel" value="Intel(R) Xeon(R) Gold 6146 CPU @ 3.20GHz"/>
      <info name="CPUStepping" value="4"/>
      <object type="L3Cache" cpuset="0x00555555" complete_cpuset="0x00555555" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="7" cache_size="25952256" depth="3" cache_linesize="64" cache_associativity="11" cache_type="0">
        <info name="Inclusive" value="0"/>
        <object type="L2Cache" cpuset="0x00000001" complete_cpuset="0x00000001" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="6" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000001" complete_cpuset="0x00000001" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="5" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="0" cpuset="0x00000001" complete_cpuset="0x00000001" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="3">
              <object type="PU" os_index="0" cpuset="0x00000001" complete_cpuset="0x00000001" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="4"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000004" complete_cpuset="0x00000004" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="17" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000004" complete_cpuset="0x00000004" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="16" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="4" cpuset="0x00000004" complete_cpuset="0x00000004" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="14">
              <object type="PU" os_index="2" cpuset="0x00000004" complete_cpuset="0x00000004" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="15"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000010" complete_cpuset="0x00000010" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="25" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000010" complete_cpuset="0x00000010" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="24" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="1" cpuset="0x00000010" complete_cpuset="0x00000010" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="22">
              <object type="PU" os_index="4" cpuset="0x00000010" complete_cpuset="0x00000010" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="23"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000040" complete_cpuset="0x00000040" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="33" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000040" complete_cpuset="0x00000040" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="32" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="3" cpuset="0x00000040" complete_cpuset="0x00000040" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="30">
              <object type="PU" os_index="6" cpuset="0x00000040" complete_cpuset="0x00000040" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="31"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000100" complete_cpuset="0x00000100" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="41" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000100" complete_cpuset="0x00000100" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="40" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="2" cpuset="0x00000100" complete_cpuset="0x00000100" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="38">
              <object type="PU" os_index="8" cpuset="0x00000100" complete_cpuset="0x00000100" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="39"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000400" complete_cpuset="0x00000400" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="49" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000400" complete_cpuset="0x00000400" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="48" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="10" cpuset="0x00000400" complete_cpuset="0x00000400" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="46">
              <object type="PU" os_index="10" cpuset="0x00000400" complete_cpuset="0x00000400" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="47"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00001000" complete_cpuset="0x00001000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="57" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00001000" complete_cpuset="0x00001000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="56" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="9" cpuset="0x00001000" complete_cpuset="0x00001000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="54">
              <object type="PU" os_index="12" cpuset="0x00001000" complete_cpuset="0x00001000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="55"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00004000" complete_cpuset="0x00004000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="65" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00004000" complete_cpuset="0x00004000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="64" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="19" cpuset="0x00004000" complete_cpuset="0x00004000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="62">
              <object type="PU" os_index="14" cpuset="0x00004000" complete_cpuset="0x00004000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="63"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00010000" complete_cpuset="0x00010000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="73" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00010000" complete_cpuset="0x00010000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="72" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="16" cpuset="0x00010000" complete_cpuset="0x00010000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="70">
              <object type="PU" os_index="16" cpuset="0x00010000" complete_cpuset="0x00010000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="71"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00040000" complete_cpuset="0x00040000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="81" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00040000" complete_cpuset="0x00040000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="80" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="18" cpuset="0x00040000" complete_cpuset="0x00040000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="78">
              <object type="PU" os_index="18" cpuset="0x00040000" complete_cpuset="0x00040000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="79"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00100000" complete_cpuset="0x00100000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="89" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00100000" complete_cpuset="0x00100000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="88" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="25" cpuset="0x00100000" complete_cpuset="0x00100000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="86">
              <object type="PU" os_index="20" cpuset="0x00100000" complete_cpuset="0x00100000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="87"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00400000" complete_cpuset="0x00400000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="97" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00400000" complete_cpuset="0x00400000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="96" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="26" cpuset="0x00400000" complete_cpuset="0x00400000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="94">
              <object type="PU" os_index="22" cpuset="0x00400000" complete_cpuset="0x00400000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="95"/>
            </object>
          </object>
        </object>
      </object>
    </object>
    <object type="Package" os_index="1" cpuset="0x00aaaaaa" complete_cpuset="0x00aaaaaa" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="8">
      <info name="CPUVendor" value="GenuineIntel"/>
      <info name="CPUFamilyNumber" value="6"/>
      <info name="CPUModelNumber" value="85"/>
      <info name="CPUModel" value="Intel(R) Xeon(R) Gold 6146 CPU @ 3.20GHz"/>
      <info name="CPUStepping" value="4"/>
      <object type="L3Cache" cpuset="0x00aaaaaa" complete_cpuset="0x00aaaaaa" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="13" cache_size="25952256" depth="3" cache_linesize="64" cache_associativity="11" cache_type="0">
        <info name="Inclusive" value="0"/>
        <object type="L2Cache" cpuset="0x00000002" complete_cpuset="0x00000002" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="12" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000002" complete_cpuset="0x00000002" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="11" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="0" cpuset="0x00000002" complete_cpuset="0x00000002" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="9">
              <object type="PU" os_index="1" cpuset="0x00000002" complete_cpuset="0x00000002" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="10"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000008" complete_cpuset="0x00000008" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="21" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000008" complete_cpuset="0x00000008" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="20" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="4" cpuset="0x00000008" complete_cpuset="0x00000008" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="18">
              <object type="PU" os_index="3" cpuset="0x00000008" complete_cpuset="0x00000008" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="19"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000020" complete_cpuset="0x00000020" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="29" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000020" complete_cpuset="0x00000020" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="28" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="1" cpuset="0x00000020" complete_cpuset="0x00000020" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="26">
              <object type="PU" os_index="5" cpuset="0x00000020" complete_cpuset="0x00000020" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="27"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000080" complete_cpuset="0x00000080" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="37" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000080" complete_cpuset="0x00000080" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="36" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="3" cpuset="0x00000080" complete_cpuset="0x00000080" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="34">
              <object type="PU" os_index="7" cpuset="0x00000080" complete_cpuset="0x00000080" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="35"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000200" complete_cpuset="0x00000200" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="45" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000200" complete_cpuset="0x00000200" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="44" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="2" cpuset="0x00000200" complete_cpuset="0x00000200" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="42">
              <object type="PU" os_index="9" cpuset="0x00000200" complete_cpuset="0x00000200" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="43"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000800" complete_cpuset="0x00000800" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="53" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000800" complete_cpuset="0x00000800" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="52" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="11" cpuset="0x00000800" complete_cpuset="0x00000800" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="50">
              <object type="PU" os_index="11" cpuset="0x00000800" complete_cpuset="0x00000800" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="51"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00002000" complete_cpuset="0x00002000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="61" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00002000" complete_cpuset="0x00002000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="60" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="8" cpuset="0x00002000" complete_cpuset="0x00002000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="58">
              <object type="PU" os_index="13" cpuset="0x00002000" complete_cpuset="0x00002000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="59"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00008000" complete_cpuset="0x00008000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="69" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00008000" complete_cpuset="0x00008000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="68" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="9" cpuset="0x00008000" complete_cpuset="0x00008000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="66">
              <object type="PU" os_index="15" cpuset="0x00008000" complete_cpuset="0x00008000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="67"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00020000" complete_cpuset="0x00020000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="77" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00020000" complete_cpuset="0x00020000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="76" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="17" cpuset="0x00020000" complete_cpuset="0x00020000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="74">
              <object type="PU" os_index="17" cpuset="0x00020000" complete_cpuset="0x00020000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="75"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00080000" complete_cpuset="0x00080000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="85" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00080000" complete_cpuset="0x00080000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="84" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="20" cpuset="0x00080000" complete_cpuset="0x00080000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="82">
              <object type="PU" os_index="19" cpuset="0x00080000" complete_cpuset="0x00080000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="83"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00200000" complete_cpuset="0x00200000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="93" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00200000" complete_cpuset="0x00200000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="92" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="18" cpuset="0x00200000" complete_cpuset="0x00200000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="90">
              <object type="PU" os_index="21" cpuset="0x00200000" complete_cpuset="0x00200000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="91"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00800000" complete_cpuset="0x00800000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="101" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00800000" complete_cpuset="0x00800000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="100" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="19" cpuset="0x00800000" complete_cpuset="0x00800000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="98">
              <object type="PU" os_index="23" cpuset="0x00800000" complete_cpuset="0x00800000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="99"/>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
</topology>

```

## fadatsai | 2019-08-08T02:55:41+00:00
I try 2.99.5-evo set intensity 2, trtl hashrate has return to normal.
BTW, Does rx/wow support intensity 2? I got "warning: "intensity 2 not supported for rx/wow algorithm" after set intensity 2



## xmrig | 2019-08-08T05:13:21+00:00
All RandomX variants including rx/wow as well, not support intensity above 1.
Thank you.

## xmrig | 2019-08-08T06:17:11+00:00
2 suggestions:
1. If you enable hyper threading you can run 48 threads, it should increase hashrate.
2. If you will mine RandomX in future better to enable NUMA support.

## xmrig | 2019-08-09T09:45:34+00:00
v2.99.5-beta released https://github.com/xmrig/xmrig/releases/tag/v2.99.5-beta

# Action History
- Created by: fadatsai | 2019-08-07T09:39:31+00:00
- Closed at: 2019-08-09T09:45:34+00:00
