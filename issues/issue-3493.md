---
title: '`CL_OUT_OF_HOST_MEMORY` when run as systemd service'
source_url: https://github.com/xmrig/xmrig/issues/3493
author: shtrophic
assignees: []
labels: []
created_at: '2024-06-04T06:08:48+00:00'
updated_at: '2025-06-28T10:33:04+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:33:04+00:00'
---

# Original Description
**Describe the bug**
Xmrig opencl errors when run as a systemd service. This error does not occur when not run as a systemd service, e.g. in a terminal.

**To Reproduce**
Run xmrig as a systemd service:
```service
[Unit]
Description=Nice XMRig Daemon
After=network-online.target

[Service]
Type=forking
ExecStart=/usr/bin/xmrig --opencl -u x+300000 -o 1.2.3.4:1234 --background --syslog
LimitNICE=19
Restart=on-failure
RestartSec=20s
StartLimitInterval=30min
StartLimitBurst=30

[Install]
WantedBy=multi-user.target
```

**Expected behavior**
GPU utilization

**Required data**
 - XMRig version
```
XMRig 6.21.2
 built on May 18 2024 with GCC 14.1.1
 features: 64-bit AES

libuv/1.48.0
OpenSSL/3.3.0
hwloc/2.10.0
```
 - OS: Arch Linux
 - For GPU related issues: 
```
$ clinfo
Number of platforms:                             2
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP.dbg (3602.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 3.0
  Platform Name:                                 rusticl
  Platform Vendor:                               Mesa/X.org
  Platform Extensions:                           cl_khr_byte_addressable_store cl_khr_create_command_queue cl_khr_expect_assume cl_khr_extended_versioning cl_khr_icd cl_khr_il_program cl_khr_spirv_no_integer_wrap_decoration cl_khr_suggested_local_work_size


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    AMD Radeon RX 6700 XT
  Device Topology:                               PCI[ B#45, D#0, F#0 ]
  Max compute units:                             20
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
  Max work group size:                           256
  Preferred vector width char:                   4
  Preferred vector width short:                  2
  Preferred vector width int:                    1
  Preferred vector width long:                   1
  Preferred vector width float:                  1
  Preferred vector width double:                 1
  Native vector width char:                      4
  Native vector width short:                     2
  Native vector width int:                       1
  Native vector width long:                      1
  Native vector width float:                     1
  Native vector width double:                    1
  Max clock frequency:                           2855Mhz
  Address bits:                                  64
  Max memory allocation:                         10937905968
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            16384
  Max image 3D height:                           16384
  Max image 3D depth:                            8192
  Max samplers within kernel:                    16
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     Yes
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               128
  Cache size:                                    16384
  Global memory size:                            12868124672
  Constant buffer size:                          10937905968
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          2347971376
  Max global variable size:                      10937905968
  Max global variable preferred total size:      12868124672
  Max read/write image args:                     64
  Max on device events:                          1024
  Queue on device max size:                      8388608
  Max on device queues:                          1
  Queue on device preferred size:                262144
  SVM capabilities:
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     32
  Error correction support:                      0
  Unified memory for Host and Device:            0
  Profiling timer resolution:                    1
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:
    Execute OpenCL kernels:                      Yes
    Execute native function:                     No
  Queue on Host properties:
    Out-of-Order:                                No
    Profiling :                                  Yes
  Queue on Device properties:
    Out-of-Order:                                Yes
    Profiling :                                  Yes
  Platform ID:                                   0x761ab2c05010
  Name:                                          gfx1030
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                3602.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 2.0
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program


  Platform Name:                                 rusticl
Number of devices:                               0
```


**Additional context**
```log
opencl   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 2d:00.0 |       320 |     8 |    640 | AMD Radeon RX 6700 XT (gfx1031)
|  1 |   0 | 2d:00.0 |       320 |     8 |    640 | AMD Radeon RX 6700 XT (gfx1031)
opencl   error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clCreateBuffer with buffer size 2181038080
opencl   error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clCreateBuffer with buffer size 2181038080
opencl   error CL_OUT_OF_HOST_MEMORY when calling clCreateCommandQueueWithProperties
opencl   thread #0 failed with error CL_OUT_OF_HOST_MEMORY
opencl   thread #0 self-test failed
opencl   error CL_OUT_OF_HOST_MEMORY when calling clCreateCommandQueueWithProperties
opencl   thread #1 failed with error CL_OUT_OF_HOST_MEMORY
opencl   thread #1 self-test failed
opencl   disabled (failed to start threads)
```

I have 32GB host memory.


# Discussion History
## Spudz76 | 2024-06-04T13:27:23+00:00
Add `LimitMEMLOCK=12GB` to the `[Service]` section.

## shtrophic | 2024-06-04T16:12:05+00:00
Thanks. I've tried that (albeit with `12000000000` since systemd doesn't like the `GB` suffix), but I still get the same error.

## Spudz76 | 2024-06-04T17:40:22+00:00
Dunno, Debian based distros work fine with that and have always accepted "GB".  Dig around in the systemd service defaults, Arch probably locked some extra stuff down.

For ref, relevant bits of `systemctl show` from a Ubuntu systemd:
```
Version=249.11-0ubuntu3.12
Features=+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT +GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY -P11KIT -QRENCODE +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified
Architecture=x86-64
...
DefaultTimerAccuracyUSec=1min
DefaultTimeoutStartUSec=1min 30s
DefaultTimeoutStopUSec=10s
DefaultTimeoutAbortUSec=10s
DefaultRestartUSec=100ms
DefaultStartLimitIntervalUSec=10s
DefaultStartLimitBurst=5
DefaultCPUAccounting=yes
DefaultBlockIOAccounting=no
DefaultMemoryAccounting=yes
DefaultTasksAccounting=yes
DefaultLimitCPU=infinity
DefaultLimitCPUSoft=infinity
DefaultLimitFSIZE=infinity
DefaultLimitFSIZESoft=infinity
DefaultLimitDATA=infinity
DefaultLimitDATASoft=infinity
DefaultLimitSTACK=infinity
DefaultLimitSTACKSoft=8388608
DefaultLimitCORE=infinity
DefaultLimitCORESoft=0
DefaultLimitRSS=infinity
DefaultLimitRSSSoft=infinity
DefaultLimitNOFILE=524288
DefaultLimitNOFILESoft=1024
DefaultLimitAS=infinity
DefaultLimitASSoft=infinity
DefaultLimitNPROC=168376
DefaultLimitNPROCSoft=168376
DefaultLimitMEMLOCK=65536
DefaultLimitMEMLOCKSoft=65536
DefaultLimitLOCKS=infinity
DefaultLimitLOCKSSoft=infinity
DefaultLimitSIGPENDING=168376
DefaultLimitSIGPENDINGSoft=168376
DefaultLimitMSGQUEUE=819200
DefaultLimitMSGQUEUESoft=819200
DefaultLimitNICE=0
DefaultLimitNICESoft=0
DefaultLimitRTPRIO=0
DefaultLimitRTPRIOSoft=0
DefaultLimitRTTIME=infinity
DefaultLimitRTTIMESoft=infinity
DefaultTasksMax=50512
TimerSlackNSec=50000
DefaultOOMPolicy=stop
```

Would bet some of the `infinity` items have a limit in Arch.

# Action History
- Created by: shtrophic | 2024-06-04T06:08:48+00:00
- Closed at: 2025-06-28T10:33:04+00:00
