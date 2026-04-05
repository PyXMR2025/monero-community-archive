---
title: Ubuntu 18 only runs 1/2 cpu
source_url: https://github.com/xmrig/xmrig/issues/1229
author: ghost
assignees: []
labels:
- question
created_at: '2019-10-09T07:19:29+00:00'
updated_at: '2019-12-22T19:27:43+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:27:43+00:00'
---

# Original Description
I have 48 cpu but only run 24/48
<img src="https://i.imgur.com/umuPcYf.jpg" />

Config
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "version": 1,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.hashvault.pro:7777",
            "user": "Test",
            "pass": "Ubuntu",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}

# Discussion History
## xmrig | 2019-10-09T08:11:46+00:00
What OS are you using? Please share result or `./xmrig --export-topology` and output of `lscpu` for some reason hwloc detects only half of L2 cache and it cause this issue.
Thank you.

## ghost | 2019-10-09T09:15:21+00:00
> What OS are you using? Please share result or `./xmrig --export-topology` and output of `lscpu` for some reason hwloc detects only half of L2 cache and it cause this issue.
> Thank you.

```xml
<topology version="2.0">
  <object type="Machine" os_index="0" cpuset="0x0000ffff,0xffffffff" complete_cpuset="0x0000ffff,0xffffffff" allowed_cpuset="0x0000ffff,0xffffffff" nodeset="0x00000003" complete_nodeset="0x00000003" allowed_nodeset="0x00000003" gp_index="1">
    <info name="DMIProductName" value="Virtual Machine"/>
    <info name="DMIProductVersion" value="7.0"/>
    <info name="DMIBoardVendor" value="Microsoft Corporation"/>
    <info name="DMIBoardName" value="Virtual Machine"/>
    <info name="DMIBoardVersion" value="7.0"/>
    <info name="DMIChassisVendor" value="Microsoft Corporation"/>
    <info name="DMIChassisType" value="3"/>
    <info name="DMIChassisVersion" value="7.0"/>
    <info name="DMIBIOSVendor" value="American Megatrends Inc."/>
    <info name="DMIBIOSVersion" value="090007 "/>
    <info name="DMIBIOSDate" value="06/02/2017"/>
    <info name="DMISysVendor" value="Microsoft Corporation"/>
    <info name="Backend" value="Linux"/>
    <info name="LinuxCgroup" value="/"/>
    <info name="OSName" value="Linux"/>
    <info name="OSRelease" value="5.0.0-1018-azure"/>
    <info name="OSVersion" value="#19~18.04.1-Ubuntu SMP Wed Aug 21 05:13:05 UTC 2019"/>
    <info name="HostName" value="myVPS2"/>
    <info name="Architecture" value="x86_64"/>
    <info name="hwlocVersion" value="2.0.4"/>
    <info name="ProcessName" value="xmrig"/>
    <object type="Package" os_index="0" cpuset="0x00ffffff" complete_cpuset="0x00ffffff" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="2">
      <info name="CPUVendor" value="GenuineIntel"/>
      <info name="CPUFamilyNumber" value="6"/>
      <info name="CPUModelNumber" value="85"/>
      <info name="CPUModel" value="Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz"/>
      <info name="CPUStepping" value="4"/>
      <object type="NUMANode" os_index="0" cpuset="0x00ffffff" complete_cpuset="0x00ffffff" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="126" local_memory="50654441472">
        <page_type size="4096" count="12334039"/>
        <page_type size="2097152" count="64"/>
        <page_type size="1073741824" count="0"/>
      </object>
      <object type="L3Cache" cpuset="0x00ffffff" complete_cpuset="0x00ffffff" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="7" cache_size="34603008" depth="3" cache_linesize="64" cache_associativity="11" cache_type="0">
        <info name="Inclusive" value="0"/>
        <object type="L2Cache" cpuset="0x00000003" complete_cpuset="0x00000003" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="6" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000003" complete_cpuset="0x00000003" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="5" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="0" cpuset="0x00000003" complete_cpuset="0x00000003" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="3">
              <object type="PU" os_index="0" cpuset="0x00000001" complete_cpuset="0x00000001" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="4"/>
              <object type="PU" os_index="1" cpuset="0x00000002" complete_cpuset="0x00000002" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="8"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x0000000c" complete_cpuset="0x0000000c" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="12" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x0000000c" complete_cpuset="0x0000000c" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="11" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="1" cpuset="0x0000000c" complete_cpuset="0x0000000c" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="9">
              <object type="PU" os_index="2" cpuset="0x00000004" complete_cpuset="0x00000004" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="10"/>
              <object type="PU" os_index="3" cpuset="0x00000008" complete_cpuset="0x00000008" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="13"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000030" complete_cpuset="0x00000030" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="17" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000030" complete_cpuset="0x00000030" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="16" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="2" cpuset="0x00000030" complete_cpuset="0x00000030" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="14">
              <object type="PU" os_index="4" cpuset="0x00000010" complete_cpuset="0x00000010" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="15"/>
              <object type="PU" os_index="5" cpuset="0x00000020" complete_cpuset="0x00000020" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="18"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x000000c0" complete_cpuset="0x000000c0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="22" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x000000c0" complete_cpuset="0x000000c0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="21" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="3" cpuset="0x000000c0" complete_cpuset="0x000000c0" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="19">
              <object type="PU" os_index="6" cpuset="0x00000040" complete_cpuset="0x00000040" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="20"/>
              <object type="PU" os_index="7" cpuset="0x00000080" complete_cpuset="0x00000080" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="23"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000300" complete_cpuset="0x00000300" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="27" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000300" complete_cpuset="0x00000300" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="26" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="4" cpuset="0x00000300" complete_cpuset="0x00000300" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="24">
              <object type="PU" os_index="8" cpuset="0x00000100" complete_cpuset="0x00000100" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="25"/>
              <object type="PU" os_index="9" cpuset="0x00000200" complete_cpuset="0x00000200" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="28"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000c00" complete_cpuset="0x00000c00" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="32" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000c00" complete_cpuset="0x00000c00" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="31" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="5" cpuset="0x00000c00" complete_cpuset="0x00000c00" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="29">
              <object type="PU" os_index="10" cpuset="0x00000400" complete_cpuset="0x00000400" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="30"/>
              <object type="PU" os_index="11" cpuset="0x00000800" complete_cpuset="0x00000800" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="33"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00003000" complete_cpuset="0x00003000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="37" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00003000" complete_cpuset="0x00003000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="36" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="6" cpuset="0x00003000" complete_cpuset="0x00003000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="34">
              <object type="PU" os_index="12" cpuset="0x00001000" complete_cpuset="0x00001000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="35"/>
              <object type="PU" os_index="13" cpuset="0x00002000" complete_cpuset="0x00002000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="38"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x0000c000" complete_cpuset="0x0000c000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="42" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x0000c000" complete_cpuset="0x0000c000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="41" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="7" cpuset="0x0000c000" complete_cpuset="0x0000c000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="39">
              <object type="PU" os_index="14" cpuset="0x00004000" complete_cpuset="0x00004000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="40"/>
              <object type="PU" os_index="15" cpuset="0x00008000" complete_cpuset="0x00008000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="43"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00030000" complete_cpuset="0x00030000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="47" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00030000" complete_cpuset="0x00030000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="46" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="8" cpuset="0x00030000" complete_cpuset="0x00030000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="44">
              <object type="PU" os_index="16" cpuset="0x00010000" complete_cpuset="0x00010000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="45"/>
              <object type="PU" os_index="17" cpuset="0x00020000" complete_cpuset="0x00020000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="48"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x000c0000" complete_cpuset="0x000c0000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="52" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x000c0000" complete_cpuset="0x000c0000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="51" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="9" cpuset="0x000c0000" complete_cpuset="0x000c0000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="49">
              <object type="PU" os_index="18" cpuset="0x00040000" complete_cpuset="0x00040000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="50"/>
              <object type="PU" os_index="19" cpuset="0x00080000" complete_cpuset="0x00080000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="53"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00300000" complete_cpuset="0x00300000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="57" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00300000" complete_cpuset="0x00300000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="56" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="10" cpuset="0x00300000" complete_cpuset="0x00300000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="54">
              <object type="PU" os_index="20" cpuset="0x00100000" complete_cpuset="0x00100000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="55"/>
              <object type="PU" os_index="21" cpuset="0x00200000" complete_cpuset="0x00200000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="58"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00c00000" complete_cpuset="0x00c00000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="62" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00c00000" complete_cpuset="0x00c00000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="61" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="11" cpuset="0x00c00000" complete_cpuset="0x00c00000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="59">
              <object type="PU" os_index="22" cpuset="0x00400000" complete_cpuset="0x00400000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="60"/>
              <object type="PU" os_index="23" cpuset="0x00800000" complete_cpuset="0x00800000" nodeset="0x00000001" complete_nodeset="0x00000001" gp_index="63"/>
            </object>
          </object>
        </object>
      </object>
    </object>
    <object type="Package" os_index="1" cpuset="0x0000ffff,0xff000000" complete_cpuset="0x0000ffff,0xff000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="64">
      <info name="CPUVendor" value="GenuineIntel"/>
      <info name="CPUFamilyNumber" value="6"/>
      <info name="CPUModelNumber" value="85"/>
      <info name="CPUModel" value="Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz"/>
      <info name="CPUStepping" value="4"/>
      <object type="NUMANode" os_index="1" cpuset="0x0000ffff,0xff000000" complete_cpuset="0x0000ffff,0xff000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="127" local_memory="50695892992">
        <page_type size="4096" count="12344159"/>
        <page_type size="2097152" count="64"/>
        <page_type size="1073741824" count="0"/>
      </object>
      <object type="L3Cache" cpuset="0x0000ffff,0xff000000" complete_cpuset="0x0000ffff,0xff000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="69" cache_size="34603008" depth="3" cache_linesize="64" cache_associativity="11" cache_type="0">
        <info name="Inclusive" value="0"/>
        <object type="L2Cache" cpuset="0x03000000" complete_cpuset="0x03000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="68" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x03000000" complete_cpuset="0x03000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="67" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="0" cpuset="0x03000000" complete_cpuset="0x03000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="65">
              <object type="PU" os_index="24" cpuset="0x01000000" complete_cpuset="0x01000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="66"/>
              <object type="PU" os_index="25" cpuset="0x02000000" complete_cpuset="0x02000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="70"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x0c000000" complete_cpuset="0x0c000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="74" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x0c000000" complete_cpuset="0x0c000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="73" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="1" cpuset="0x0c000000" complete_cpuset="0x0c000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="71">
              <object type="PU" os_index="26" cpuset="0x04000000" complete_cpuset="0x04000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="72"/>
              <object type="PU" os_index="27" cpuset="0x08000000" complete_cpuset="0x08000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="75"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x30000000" complete_cpuset="0x30000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="79" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x30000000" complete_cpuset="0x30000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="78" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="2" cpuset="0x30000000" complete_cpuset="0x30000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="76">
              <object type="PU" os_index="28" cpuset="0x10000000" complete_cpuset="0x10000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="77"/>
              <object type="PU" os_index="29" cpuset="0x20000000" complete_cpuset="0x20000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="80"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0xc0000000" complete_cpuset="0xc0000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="84" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0xc0000000" complete_cpuset="0xc0000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="83" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="3" cpuset="0xc0000000" complete_cpuset="0xc0000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="81">
              <object type="PU" os_index="30" cpuset="0x40000000" complete_cpuset="0x40000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="82"/>
              <object type="PU" os_index="31" cpuset="0x80000000" complete_cpuset="0x80000000" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="85"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000003,0x0" complete_cpuset="0x00000003,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="89" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000003,0x0" complete_cpuset="0x00000003,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="88" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="4" cpuset="0x00000003,0x0" complete_cpuset="0x00000003,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="86">
              <object type="PU" os_index="32" cpuset="0x00000001,0x0" complete_cpuset="0x00000001,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="87"/>
              <object type="PU" os_index="33" cpuset="0x00000002,0x0" complete_cpuset="0x00000002,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="90"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x0000000c,0x0" complete_cpuset="0x0000000c,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="94" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x0000000c,0x0" complete_cpuset="0x0000000c,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="93" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="5" cpuset="0x0000000c,0x0" complete_cpuset="0x0000000c,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="91">
              <object type="PU" os_index="34" cpuset="0x00000004,0x0" complete_cpuset="0x00000004,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="92"/>
              <object type="PU" os_index="35" cpuset="0x00000008,0x0" complete_cpuset="0x00000008,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="95"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000030,0x0" complete_cpuset="0x00000030,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="99" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000030,0x0" complete_cpuset="0x00000030,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="98" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="6" cpuset="0x00000030,0x0" complete_cpuset="0x00000030,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="96">
              <object type="PU" os_index="36" cpuset="0x00000010,0x0" complete_cpuset="0x00000010,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="97"/>
              <object type="PU" os_index="37" cpuset="0x00000020,0x0" complete_cpuset="0x00000020,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="100"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x000000c0,0x0" complete_cpuset="0x000000c0,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="104" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x000000c0,0x0" complete_cpuset="0x000000c0,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="103" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="7" cpuset="0x000000c0,0x0" complete_cpuset="0x000000c0,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="101">
              <object type="PU" os_index="38" cpuset="0x00000040,0x0" complete_cpuset="0x00000040,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="102"/>
              <object type="PU" os_index="39" cpuset="0x00000080,0x0" complete_cpuset="0x00000080,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="105"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000300,0x0" complete_cpuset="0x00000300,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="109" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000300,0x0" complete_cpuset="0x00000300,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="108" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="8" cpuset="0x00000300,0x0" complete_cpuset="0x00000300,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="106">
              <object type="PU" os_index="40" cpuset="0x00000100,0x0" complete_cpuset="0x00000100,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="107"/>
              <object type="PU" os_index="41" cpuset="0x00000200,0x0" complete_cpuset="0x00000200,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="110"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00000c00,0x0" complete_cpuset="0x00000c00,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="114" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00000c00,0x0" complete_cpuset="0x00000c00,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="113" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="9" cpuset="0x00000c00,0x0" complete_cpuset="0x00000c00,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="111">
              <object type="PU" os_index="42" cpuset="0x00000400,0x0" complete_cpuset="0x00000400,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="112"/>
              <object type="PU" os_index="43" cpuset="0x00000800,0x0" complete_cpuset="0x00000800,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="115"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x00003000,0x0" complete_cpuset="0x00003000,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="119" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x00003000,0x0" complete_cpuset="0x00003000,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="118" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="10" cpuset="0x00003000,0x0" complete_cpuset="0x00003000,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="116">
              <object type="PU" os_index="44" cpuset="0x00001000,0x0" complete_cpuset="0x00001000,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="117"/>
              <object type="PU" os_index="45" cpuset="0x00002000,0x0" complete_cpuset="0x00002000,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="120"/>
            </object>
          </object>
        </object>
        <object type="L2Cache" cpuset="0x0000c000,0x0" complete_cpuset="0x0000c000,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="124" cache_size="1048576" depth="2" cache_linesize="64" cache_associativity="16" cache_type="0">
          <info name="Inclusive" value="0"/>
          <object type="L1Cache" cpuset="0x0000c000,0x0" complete_cpuset="0x0000c000,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="123" cache_size="32768" depth="1" cache_linesize="64" cache_associativity="8" cache_type="1">
            <info name="Inclusive" value="0"/>
            <object type="Core" os_index="11" cpuset="0x0000c000,0x0" complete_cpuset="0x0000c000,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="121">
              <object type="PU" os_index="46" cpuset="0x00004000,0x0" complete_cpuset="0x00004000,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="122"/>
              <object type="PU" os_index="47" cpuset="0x00008000,0x0" complete_cpuset="0x00008000,0x0" nodeset="0x00000002" complete_nodeset="0x00000002" gp_index="125"/>
            </object>
          </object>
        </object>
      </object>
    </object>
  </object>
  <distances2 type="NUMANode" nbobjs="2" kind="5" indexing="os">
    <indexes length="4">0 1 </indexes>
    <u64values length="12">10 20 20 10 </u64values>
  </distances2>
</topology>
```

## ghost | 2019-10-09T09:16:34+00:00
@xmrig See help me. I use os Ubuntu 18.04 LTS.

## xmrig | 2019-10-09T10:26:56+00:00
You use virtual machine (Microsoft Azure) it means autoconfig may not work well, depends how precise hardware topology emulated.

Try add (or replace if miner already generated it) this profile to `cpu` object in your config:
```
"cn": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
```

It allow you use all 48 cores, but how it affect hashrate is unknown, it might drop, also mining violates TOS of this provider.

## ghost | 2019-10-09T14:34:41+00:00
> You use virtual machine (Microsoft Azure) it means autoconfig may not work well, depends how precise hardware topology emulated.
> 
> Try add (or replace if miner already generated it) this profile to `cpu` object in your config:
> 
> ```
> "cn": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
> ```
> 
> It allow you use all 48 cores, but how it affect hashrate is unknown, it might drop, also mining violates TOS of this provider.

The above configuration runs 48 cpu but the equivalent hashrate runs 24 cpu. Almost no effect.



## ghost | 2019-10-09T14:40:50+00:00
@xmrig Receive only 24C / 48T, picture marker.

<img src="https://i.imgur.com/00eGM4X.jpg" />

## xmrig | 2019-10-09T14:59:55+00:00
Seems you receive half of both CPUs (packages) and this is equal to single 8168 CPU so 24 threads is best configuration, nothing can do.
Thank you.

## ghost | 2019-10-09T15:04:52+00:00
> Seems you receive half of both CPUs (packages) and this is equal to single 8168 CPU so 24 threads is best configuration, nothing can do.
> Thank you.

Not true with vps 72 cpu, I can run with 36/72 cpu, and 32 cpu hashrate is also higher than 24 cpu.
It seems that it cannot run multithreading, it only runs 1 thread.
You can review this issue carefully.
Thanks.

## xmrig | 2019-10-09T15:22:36+00:00
cryptonight hashrate limited by CPU cache, not by cores, best configuration for single physical 8168 CPU is 24 threads, according topology I guess you receive `12C/24T + 12C/24T`, of course if you got 36 physical cores it will be better, but more expensive, also please note L3 cache shared with other users, so if they do CPU intensive tasks your hashrate will drop too.

## ghost | 2019-10-10T04:18:35+00:00
@xmrig After many trials. I discovered with the Xeon E series it runs full cpu. 
And with platinum xeon it only runs 1/2 cpu. Can this be fixed?
Thank.


## dd1982 | 2019-11-27T03:58:20+00:00
A bit OT maybe but I'm a bit curious about this one since I tried to use the same instance type for a compute heavy non-mining task and didn't get close to the results I expected. If it is the same instance, which I guess it is since I only know of one instance type on Azure with dual 8168's, then these instanses are supposed to give you 44 cores with hyperthreading turned off - guess 4 cores are reserved for the hypervisor. So either the topology gets it wrong or Microsoft has messed up the settings of these instances big time. If they're set up properly it would seem 44 threads should be the sweet spot. The results I got for multi-threaded solving of large sparce matrices interlaced with bursty single-threaded work loads under Windows 10 was abysmal and not much better than what a single i7 8850H achieves - so something definitely seems strange with these instance types.

# Action History
- Created by: ghost | 2019-10-09T07:19:29+00:00
- Closed at: 2019-12-22T19:27:43+00:00
