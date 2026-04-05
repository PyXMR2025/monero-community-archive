---
title: Issue with xmrig Compilation and Execution Stability on windows
source_url: https://github.com/xmrig/xmrig/issues/3457
author: makalamaba
assignees: []
labels: []
created_at: '2024-04-03T07:34:27+00:00'
updated_at: '2024-11-22T09:16:54+00:00'
type: issue
status: closed
closed_at: '2024-11-22T09:16:54+00:00'
---

# Original Description
I am writing to report two persistent issues that I have encountered while compiling and running the xmrig application. Despite updating dependent libraries, these problems continue to affect the program's functionality across different compilers.

Issue 1: After successfully compiling and running xmrig, the program consistently hangs following the display of its version information. The duration of this hang varies significantly, ranging from approximately one minute to indefinite periods exceeding ten minutes or more. This unexpected freeze prevents the application from proceeding with its intended operation.

Issue 2: In instances where the application manages to progress beyond the version info stage, it displays successful allocation of memory pages and creation of processes but abruptly terminates abnormally. Initially, I suspected compatibility issues or bugs in external dependencies such as openssl, libuv, and hwloc. However, even after updating these libraries to their latest versions, the problem persists.

Furthermore, I have recompiled the software using both Microsoft Visual C++ (MSVC 2022) and the GNU Compiler Collection (GCC 13.2.0), yet the aforementioned issues remain unresolved under both environments.

Could you kindly look into these matters to help identify the root cause and provide guidance on potential solutions? Detailed log files or any additional diagnostic information can be furnished upon request.
![image](https://github.com/xmrig/xmrig/assets/142157372/04eaa596-5a71-4c53-954e-85380f03da70)


My OS is windows 21H2
CMakeLists.txt is as follows
```
option(WITH_HWLOC           "Enable hwloc support" ON)
option(WITH_CN_LITE         "Enable CryptoNight-Lite algorithms family" ON)
option(WITH_CN_HEAVY        "Enable CryptoNight-Heavy algorithms family" ON)
option(WITH_CN_PICO         "Enable CryptoNight-Pico algorithm" ON)
option(WITH_CN_FEMTO        "Enable CryptoNight-UPX2 algorithm" ON)
option(WITH_RANDOMX         "Enable RandomX algorithms family" ON)
option(WITH_ARGON2          "Enable Argon2 algorithms family" ON)
option(WITH_KAWPOW          "Enable KawPow algorithms family" ON)
option(WITH_GHOSTRIDER      "Enable GhostRider algorithm" ON)
option(WITH_HTTP            "Enable HTTP protocol support (client/server)" OFF)
option(WITH_DEBUG_LOG       "Enable debug log output" OFF)
option(WITH_TLS             "Enable OpenSSL support" ON)
option(WITH_ASM             "Enable ASM PoW implementations" OFF)
option(WITH_MSR             "Enable MSR mod & 1st-gen Ryzen fix" OFF)
option(WITH_ENV_VARS        "Enable environment variables support in config file" OFF)
option(WITH_EMBEDDED_CONFIG "Enable internal embedded JSON config" ON)
option(WITH_OPENCL          "Enable OpenCL backend" OFF)
set(WITH_OPENCL_VERSION 200 CACHE STRING "Target OpenCL version")
set_property(CACHE WITH_OPENCL_VERSION PROPERTY STRINGS 120 200 210 220)
option(WITH_CUDA            "Enable CUDA backend" OFF)
option(WITH_NVML            "Enable NVML (NVIDIA Management Library) support (only if CUDA backend enabled)" ON)
option(WITH_ADL             "Enable ADL (AMD Display Library) or sysfs support (only if OpenCL backend enabled)" ON)
option(WITH_STRICT_CACHE    "Enable strict checks for OpenCL cache" OFF)
option(WITH_INTERLEAVE_DEBUG_LOG "Enable debug log for threads interleave" OFF)
option(WITH_PROFILING       "Enable profiling for developers" OFF)
option(WITH_SSE4_1          "Enable SSE 4.1 for Blake2" ON)
option(WITH_AVX2            "Enable AVX2 for Blake2" ON)
option(WITH_VAES            "Enable VAES instructions for Cryptonight" ON)
option(WITH_BENCHMARK       "Enable builtin RandomX benchmark and stress test" ON)
option(WITH_SECURE_JIT      "Enable secure access to JIT memory" OFF)
option(WITH_DMI             "Enable DMI/SMBIOS reader" OFF)

option(BUILD_STATIC         "Build static binary" ON)
option(ARM_V8               "Force ARMv8 (64 bit) architecture, use with caution if automatic detection fails, but you sure it may work" OFF)
option(ARM_V7               "Force ARMv7 (32 bit) architecture, use with caution if automatic detection fails, but you sure it may work" OFF)
option(HWLOC_DEBUG          "Enable hwloc debug helpers and log" OFF)
```

Thank you for your attention and assistance with this issue.

# Discussion History
## makalamaba | 2024-04-03T07:37:42+00:00
I tried changing CMAKE options like ASM, MSR and some algorithms but the problem still exists

## SChernykh | 2024-04-03T07:52:50+00:00
You need to set `WITH_ASM` to `ON`, because right now it forces RandomX to not use JIT (you have `-JIT` in red in XMRig log).

## headygains | 2024-05-03T05:09:30+00:00
@makalamaba did that resolve your issue?

# Action History
- Created by: makalamaba | 2024-04-03T07:34:27+00:00
- Closed at: 2024-11-22T09:16:54+00:00
