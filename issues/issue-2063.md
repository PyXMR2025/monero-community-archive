---
title: Incorrect memory configuration displayed for Intel E5 2670 v2 system
source_url: https://github.com/xmrig/xmrig/issues/2063
author: BillGatesIII
assignees: []
labels: []
created_at: '2021-01-27T20:27:23+00:00'
updated_at: '2021-01-28T17:07:20+00:00'
type: issue
status: closed
closed_at: '2021-01-28T17:07:20+00:00'
---

# Original Description
With version 6.8 the console displays information about the memory modules. I have one computer where this information is incorrect.

```
user@e5-2670v2:~$  * ABOUT        XMRig/6.8.0 gcc/9.3.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2670 v2 @ 2.50GHz (2) 64-bit AES
                L2:5.0 MB L3:50.0 MB 20C/40T NUMA:1
 * MEMORY       3.7/7.7 GB (48%)
                Node0_Dimm0: <empty>
                Node0_Dimm1: <empty>
                Node0_Dimm2: 2 GB DDR3 @ 1600 MHz 9965472-006.A
                Node0_Dimm3: 2 GB DDR3 @ 1600 MHz 9965472-006.A
 * MOTHERBOARD    - Intel X79
 * DONATE       1%
 * ASSEMBLY     auto:intel
```
As you can see, the total memory is about 8 GB which is correct because there are 4 DIMMS of 2 GB installed but the output says Node0_Dimm0 and 1 are empty.

Because dmidecode also provides incorrect information my guess is that it is not something you can fix?

```
sudo dmidecode --type memory
# dmidecode 3.2
Getting SMBIOS data from sysfs.
SMBIOS 2.7 present.

Handle 0x002D, DMI type 16, 23 bytes
Physical Memory Array
        Location: System Board Or Motherboard
        Use: System Memory
        Error Correction Type: Multi-bit ECC
        Maximum Capacity: 96 GB
        Error Information Handle: Not Provided
        Number Of Devices: 4

Handle 0x002F, DMI type 17, 34 bytes
Memory Device
        Array Handle: 0x002D
        Error Information Handle: Not Provided
        Total Width: 72 bits
        Data Width: 64 bits
        Size: No Module Installed
        Form Factor: DIMM
        Set: None
        Locator: Node0_Dimm0
        Bank Locator: Node0_Bank0
        Type: Unknown
        Type Detail: Synchronous
        Speed: Unknown
        Manufacturer: Dimm0_Manufacturer
        Serial Number: Dimm0_SerNum
        Asset Tag: Dimm0_AssetTag
        Part Number: Dimm0_PartNum
        Rank: Unknown
        Configured Memory Speed: Unknown

Handle 0x0031, DMI type 17, 34 bytes
Memory Device
        Array Handle: 0x002D
        Error Information Handle: Not Provided
        Total Width: 72 bits
        Data Width: 64 bits
        Size: No Module Installed
        Form Factor: DIMM
        Set: None
        Locator: Node0_Dimm1
        Bank Locator: Node0_Bank0
        Type: Unknown
        Type Detail: Synchronous
        Speed: Unknown
        Manufacturer: Dimm1_Manufacturer
        Serial Number: Dimm1_SerNum
        Asset Tag: Dimm1_AssetTag
        Part Number: Dimm1_PartNum
        Rank: Unknown
        Configured Memory Speed: Unknown

Handle 0x0033, DMI type 17, 34 bytes
Memory Device
        Array Handle: 0x002D
        Error Information Handle: Not Provided
        Total Width: 72 bits
        Data Width: 64 bits
        Size: 2048 MB
        Form Factor: DIMM
        Set: None
        Locator: Node0_Dimm2
        Bank Locator: Node0_Bank0
        Type: DDR3
        Type Detail: Unbuffered (Unregistered)
        Speed: 1600 MT/s
        Manufacturer: Undefined         
        Serial Number: 4802F077    
        Asset Tag: Dimm2_AssetTag
        Part Number: 9965472-006.A
        Rank: 2
        Configured Memory Speed: 1600 MT/s

Handle 0x0035, DMI type 17, 34 bytes
Memory Device
        Array Handle: 0x002D
        Error Information Handle: Not Provided
        Total Width: 72 bits
        Data Width: 64 bits
        Size: 2048 MB
        Form Factor: DIMM
        Set: None
        Locator: Node0_Dimm3
        Bank Locator: Node0_Bank0
        Type: DDR3
        Type Detail: Unbuffered (Unregistered)
        Speed: 1600 MT/s
        Manufacturer: Undefined         
        Serial Number: 4802F077    
        Asset Tag: Dimm3_AssetTag
        Part Number: 9965472-006.A
        Rank: 2
        Configured Memory Speed: 1600 MT/s

Handle 0x0037, DMI type 16, 23 bytes
Physical Memory Array
        Location: System Board Or Motherboard
        Use: System Memory
        Error Correction Type: Multi-bit ECC
        Maximum Capacity: 96 GB
        Error Information Handle: Not Provided
        Number Of Devices: 0
```
Here some information about the os.
```
  Operating System: Debian GNU/Linux 10 (buster)
            Kernel: Linux 4.19.0-10-amd64
      Architecture: x86-64
```

# Discussion History
## xmrig | 2021-01-27T21:23:09+00:00
Sadly but if DMI provides wrong information, there is no way to fix it. I guess motherboard has at least 8 memory slots and 2 remaining modules placed in `Node1_Dimm2` and `Node1_Dimm3`, but for some reason (bug?) the second NUMA node is missing in the DMI.
Thank you.

## BillGatesIII | 2021-01-28T17:07:19+00:00
Clear. Thanks.

# Action History
- Created by: BillGatesIII | 2021-01-27T20:27:23+00:00
- Closed at: 2021-01-28T17:07:20+00:00
