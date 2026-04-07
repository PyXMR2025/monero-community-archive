---
title: Build System Maintenance
source_url: https://github.com/monero-project/monero/issues/9669
author: tobtoht
assignees: []
labels:
- build system
created_at: '2025-01-02T19:11:37+00:00'
updated_at: '2026-04-04T18:49:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Guix

Time machine: Feb 22 2026

| Package  | Version | PR |
|----------|---------|------|
| gcc      | 14.3.0  |  |
| clang | 19.1.7 |  |
| glibc    | 2.27    | (#9207) |
| binutils | 2.44    | |
| cmake    | 3.31.8  | |
| rust | n/a | (#9801) |

See also: #9684.

### Regressions

- Python got re-introduced into the build environment via libxml (Guix commit: 3f1e7cc449ba443ea0c874be3c77b0fa32cbe660)

## Depends

| Package      | Version | Latest     | System | CVEs                                                                             | Split [0] |  PR           |
|:-------------|:--------|:-----------|--------|:---------------------------------------------------------------------------------|-------------:|:-------------|
| [android-ndk](https://developer.android.com/ndk/downloads)  | 27c (LTS)     | 27d       | -      | No                                                                               |              |         |
| [boost](https://github.com/boostorg/boost)        | 1.89.0  | 1.90.0     | b2     | No                                                                               | Yes       |              |
| [darwin_sdk](https://developer.apple.com/xcode/)   | 12.2    | 26.1.1         | -      | ?                                                                                |              |              |
| [freebsd_base](https://archive.freebsd.org/old-releases/amd64/) | 12.3    | 13.5 [2]   | -      | ?                                                                                |               | (#9667)        |
| [hidapi](https://github.com/libusb/hidapi)       | 0.15.0  | -          | cmake  | No                                                                               | No        |               |
| [libsodium](https://github.com/jedisct1/libsodium)    | 1.0.18  | 1.0.21     | auto   | No                                                                               | Yes       |        |
| [libusb](https://github.com/libusb/libusb)       | 1.0.27  | 1.0.29          | auto   | No                                                                               | No        |              |
| [ncurses](https://ftp.gnu.org/gnu/ncurses/)      | 6.1     | 6.6        | auto   | [Yes](https://repology.org/project/ncurses/cves?version=6.1)                     | No        |              | [4]          |
| [openssl](https://github.com/openssl/openssl)      | 3.5.4 (LTS) | 3.5.5 | perl   | No | Maybe?    |  |
| [protobuf](https://github.com/protocolbuffers/protobuf)     | 21.12   | 34.0       | auto   | No                                                                               | No        |   (#9478)        |
| [readline](https://ftp.gnu.org/gnu/readline/)     | 8.0     | 8.3    | auto   | No                                                                               | No        | [4]          |
| [unbound](https://github.com/NLnetLabs/unbound)      | 1.22.0  | 1.24.2         | auto   | No                                                                               | Maybe?    |               |
| [zeromq](https://github.com/zeromq/libzmq)       | 4.3.5   | -          | auto   | No                                                                               | No        |               |


[0] Package introduces chain split risk
[2] Latest version we can update to (#9446).   
[4] I plan to PR a patch that replaces `ncurses` and `readline` with `linenoise`.

See also: #10222

## Submodules

| Submodule     | Version     | Latest | PR    |
|---------------|-------------|--------|-------|
| gtest | 1.15.2 | 1.17.0 | |
| miniupnp      | 2.2.1       | 2.3.3  |  (#10012)     |
| rapidjson     | Jul 3 2018  | ?      |       |
| randomx       | 1.2.1       | -      |       |
| supercop      | Aug 26 2020 | ?      |       |

## CMake

TBD

## Documentation

TBD


# Discussion History
# Action History
- Created by: tobtoht | 2025-01-02T19:11:37+00:00
