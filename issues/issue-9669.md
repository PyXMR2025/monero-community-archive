---
title: Build System Maintenance
source_url: https://github.com/monero-project/monero/issues/9669
author: tobtoht
assignees: []
labels:
- build system
created_at: '2025-01-02T19:11:37+00:00'
updated_at: '2026-08-12T14:20:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Guix

Time machine: June 20 2026

| Package  | Version | PR |
|----------|---------|------|
| gcc      | 15.2.0  |   |
| clang | 22.1.8 |  |
| glibc    | 2.27    | (#9207) |
| binutils | 2.44    | |
| cmake    | 3.31.8  | |
| rust | 1.93.0 |  |

See also: #9684.

### Regressions

- Python got re-introduced into the build environment via libxml (Guix commit: 3f1e7cc449ba443ea0c874be3c77b0fa32cbe660)

## Depends

| Package                                                           | Version        | Latest   | System | Desc      | CVEs                                                         | Split [0] | PR      |
|:------------------------------------------------------------------|:---------------|:---------|--------|-----------|:-------------------------------------------------------------|----------:|:--------|
| [android-ndk](https://developer.android.com/ndk/downloads)        | 27c (LTS)      | 27d      | -      | Toolchain | No                                                           |           |         |
| [boost](https://github.com/boostorg/boost)                        | 1.91.0-1         | 1.92.0  | b2     | Daemon    | No                                                           |       Yes |         |
| [darwin_sdk](https://developer.apple.com/xcode/)                  | 12.2           | 26.1.1   | -      | Toolchain | ?                                                            |           |         |
| [freebsd_base](https://archive.freebsd.org/old-releases/amd64/)   | 12.3           | 13.5 [2] | -      | Toolchain | ?                                                            |           | (#9667) |
| [hidapi](https://github.com/libusb/hidapi)                        | 0.15.0         | -        | cmake  | Wallet    | No                                                           |        No |         |
| [libsodium](https://github.com/jedisct1/libsodium)                | 1.0.18         | 1.0.22   | auto   | Daemon    | No                                                           |       Yes |         |
| [libusb](https://github.com/libusb/libusb)                        | 1.0.30         | -   | auto   | Wallet    | No                                                           |        No |         |
| [ncurses](https://ftp.gnu.org/gnu/ncurses/)                       | 6.1            | 6.6      | auto   | Daemon    | [Yes](https://repology.org/project/ncurses/cves?version=6.1) |        No |         |     
| [openssl](https://github.com/openssl/openssl)                     | 3.5.7 (LTS)    | -    | perl   | Daemon    | No                                                           |    Maybe? |          |
| [protobuf](https://github.com/protocolbuffers/protobuf)           | 21.12          | 35.1     | auto   | Wallet    | No                                                           |        No | (#9478) |
| [readline](https://ftp.gnu.org/gnu/readline/)                     | 8.0            | 8.3      | auto   | Daemon    | No                                                           |        No |         |
| [unbound](https://github.com/NLnetLabs/unbound)                   | 1.25.2         | 1.26.0   | auto   | Daemon    | No                                                           |    Maybe? |         |
| [zeromq](https://github.com/zeromq/libzmq)                        | 4.3.5          | -        | auto   | Daemon    | No                                                           |        No |         |


[0] Package introduces chain split risk
[2] Latest version we can update to (#9446).   

See also: #10222

## Submodules

| Submodule     | Version     | Latest | PR    |
|---------------|-------------|--------|-------|
| [gtest](https://github.com/google/googletest) | 1.17.0 | 1.18.0 |  |
| [rapidjson](https://github.com/Tencent/rapidjson)     | Feb 5 2025 | ?      |     |
| [randomx](https://github.com/tevador/RandomX)       | 1.2.2       | 2.0      |       |
| [supercop](https://github.com/monero-project/supercop/tree/monero)      | Aug 26 2020 | ?      |       |



# Discussion History
# Action History
- Created by: tobtoht | 2025-01-02T19:11:37+00:00
