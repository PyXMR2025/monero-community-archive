---
title: Build Dependencies
source_url: https://github.com/monero-project/monero/issues/9684
author: tobtoht
assignees: []
labels:
- build system
created_at: '2025-01-07T12:51:00+00:00'
updated_at: '2026-02-04T11:43:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Complete list of build dependencies (excluding package definitions in `depends`) for Linux release builds.

### Stats
| | Jan 7, 2025 |                               Jul 10, 2025 | Nov 5, 2025 | Feb 4, 2026 |
|--|-----:|-----------------------------------------:|--------:|----:|
|Commit| 2e8a128c752a3cee2a0bee43b3c15ae7ec344792| 804d8cf6dad5031ca786beb0cef5c35ee521cd72| fc812cdc14225d2ee961af3ba53f5dd89e8cfd33|e77e3fafd079cd9e9b8e755937127693ea2cb327 |
|Total graph edges|11247|                                    7870 | 7726 | 7715 |
|Total store items (\*) |1372|                                     990 | 987 | 984 |
|Total packages|267|                                       209 | 202 | 200 |
|Excluding bootstrap| 212|                                     154 | 147 | 145 |
|Environment only| 83|                                       66 | 67 | 66 |

(\*) Includes derivations, builders, grafts, patches, and source archives.

### Build

'Build Env.' indicates if a package is included in the release build environment.
| Package | Version | Build Env. |
|--------|----------|-----|
|autoconf|2.69||
|autoconf-wrapper|2.69||
|automake|1.16.5||
|automake|1.17||
|bash|5.2.37|Yes|
|bash-minimal|5.2.37|Yes|
|bash-static|5.2.37|Yes|
|bdb|6.2.32||
|binutils|2.44|Yes|
|binutils-cross-x86_64-linux-gnu|2.44|Yes|
|bison|3.8.2||
|bzip2|1.0.8|Yes|
|c-ares|1.34.4||
|check|0.15.2||
|cmake-minimal|3.31.8|Yes|
|coreutils|9.1|Yes|
|coreutils-minimal|9.1|Yes|
|cunit|2.1-3||
|curl|8.6.0|Yes|
|datefudge|1.27||
|diffutils|3.12|Yes|
|ed|1.21|Yes|
|elfutils|0.192||
|expat|2.7.1|Yes|
|file|5.46||
|findutils|4.10.0|Yes|
|flex|2.6.4||
|font-dejavu|2.37||
|fontconfig-minimal|2.14.0||
|freetype|2.13.3||
|gawk|5.3.0|Yes|
|gcc|14.3.0|Yes|
|gcc-cross-sans-libc-x86_64-linux-gnu|14.3.0||
|gcc-cross-x86_64-linux-gnu|14.3.0|Yes|
|gcc-toolchain|14.3.0|Yes|
|gdbm|1.25||
|gettext-minimal|0.23.1||
|git-minimal|2.51.0|Yes|
|glibc|2.41|Yes|
|glibc-cross-x86_64-linux-gnu|2.27|Yes|
|glibc-intermediate|2.41||
|glibc-utf8-locales|2.41||
|gmp|6.3.0|Yes|
|gnutls|3.8.3|Yes|
|gperf|3.3||
|grep|3.11|Yes|
|guile|3.0.9|Yes|
|guile-gnutls|5.0.1||
|guile-json|4.7.3||
|guile-lzlib|0.3.0||
|gzip|1.14|Yes|
|help2man|1.49.2||
|iproute2|6.4.0||
|iptables|1.8.11||
|isl|0.24|Yes|
|jansson|2.14||
|jemalloc|5.3.0||
|jsoncpp|1.9.6|Yes|
|ld-wrapper|0|Yes|
|ld-wrapper-x86_64-linux-gnu|0|Yes|
|libarchive|3.7.7|Yes|
|libev|4.33||
|libffi|3.4.6|Yes|
|libfontenc|1.1.8||
|libgc|8.2.8|Yes|
|libidn|1.43||
|libidn2|2.3.7|Yes|
|libltdl|2.4.7||
|libmnl|1.0.5||
|libnftnl|1.2.8||
|libpng|1.6.39||
|libpsl|0.21.5|Yes|
|libsigsegv|2.14||
|libstdc++|14.3.0|Yes|
|libstdc++-headers|14.3.0||
|libtasn1|4.20.0|Yes|
|libtool|2.4.7||
|libunistring|1.3|Yes|
|libuv|1.44.2|Yes|
|libx11|1.8.12||
|libxau|1.0.12||
|libxcb|1.17.0||
|libxcrypt|4.4.38|Yes|
|libxdmcp|1.1.5||
|libxext|1.3.6||
|libxft|2.3.8||
|libxml2|2.14.6|Yes|
|libxrender|0.9.12||
|linux-libre-headers|6.12.17|Yes|
|linux-libre-headers-cross-x86_64-linux-gnu|6.1.155|Yes|
|lzip|1.25||
|lzlib|1.13||
|lzo|2.10||
|m4|1.4.19||
|make|4.2.1||
|make|4.4.1|Yes|
|meson|1.9.0||
|mit-krb5|1.21|Yes|
|mkfontdir|1.0.7||
|mkfontscale|1.2.3||
|mpc|1.3.1|Yes|
|mpfr|4.2.2|Yes|
|ncurses|6.2.20210619|Yes|
|net-base|5.3||
|net-tools|1.60-0.479bb4a||
|nettle|3.10.1|Yes|
|nghttp2|1.58.0|Yes|
|ninja|1.13.1||
|openssl|3.0.8|Yes|
|p11-kit|0.24.1|Yes|
|patch|2.7.6||
|patch|2.8|Yes|
|pcre2|10.42|Yes|
|perl|5.36.0|Yes|
|perl-gettext|1.07||
|pkg-config|0.29.2|Yes|
|python|3.11.11||
|python-minimal|3.11.11||
|python-minimal|3.11.14|Yes|
|python-minimal-wrapper|3.11.11||
|python-setuptools|80.9.0||
|python-wrapper|3.11.11||
|re2c|4.2||
|readline|8.2.13|Yes|
|rhash|1.4.3|Yes|
|sed|4.9|Yes|
|socat|1.7.4.4||
|sqlite|3.39.3||
|tar|1.35|Yes|
|tcl|8.6.12||
|texinfo|6.8||
|tk|8.6.12||
|tzdata|2025a||
|unzip|6.0||
|util-linux|2.40.4||
|util-macros|1.20.2||
|which|2.21|Yes|
|x86_64-linux-gnu-toolchain|14.3.0|Yes|
|xcb-proto|1.17.0||
|xorgproto|2024.1||
|xtrans|1.5.2||
|xz|5.4.5|Yes|
|zip|3.0||
|zlib|1.3.1|Yes|
|zstd|1.5.6|Yes|

### Bootstrap

| Package | Version |
|--------|----------|
|bash-mesboot|5.2.37|
|binutils-cross-boot0|2.44|
|binutils-mesboot|2.20.1a|
|binutils-mesboot0|2.20.1a|
|binutils-mesboot1|2.20.1a|
|bison-boot0|3.8.2|
|bootar|1b|
|bootstrap-binaries|0|
|bzip2-boot0|1.0.8|
|cmake-bootstrap|3.31.8|
|coreutils-boot0|9.1|
|coreutils-mesboot|9.1|
|diffutils-boot0|3.12|
|file-boot0|5.46|
|findutils-boot0|4.10.0|
|gash-boot|0.3.1|
|gash-utils-boot|0.2.0|
|gawk-boot0|5.3.0|
|gawk-mesboot|3.1.8|
|gcc-core-mesboot0|2.95.3|
|gcc-cross-boot0|14.3.0|
|gcc-cross-boot0-wrapped|14.3.0|
|gcc-mesboot|4.9.4|
|gcc-mesboot-wrapper|4.9.4|
|gcc-mesboot0|2.95.3|
|gcc-mesboot1|4.6.4|
|gcc-mesboot1-wrapper|4.6.4|
|gettext-boot0|0.19.8.1|
|glibc-headers-mesboot|2.16.0|
|glibc-mesboot|2.16.0|
|glibc-mesboot0|2.2.5|
|grep-mesboot|3.11|
|gzip-mesboot|1.2.4|
|ld-wrapper-boot0|0|
|ld-wrapper-boot3|0|
|libstdc++-boot0|4.9.4|
|linux-libre-headers-bootstrap|0|
|m4-boot0|1.4.19|
|make-boot0|4.4.1|
|make-mesboot|3.82|
|make-mesboot0|3.80|
|mes-boot|0.25.1|
|mesboot-headers|0.25.1|
|patch-boot0|2.7.6|
|patch-mesboot|2.5.9|
|perl-boot0|5.36.0|
|python-boot0|3.5.9|
|sed-boot0|4.9|
|sed-mesboot|4.8|
|stage0-posix|1.6.0|
|tar-boot0|1.35|
|tar-mesboot|1.35|
|tcc-boot|0.9.27|
|tcc-boot0|0.9.26-1149-g46a75d0c|
|xz-mesboot|5.4.5|

---

Building `x86_64-linux-gnu` on `x86_64` @ e77e3fafd079cd9e9b8e755937127693ea2cb327.

```
PROFILE = (dc1k3086w9bammrjq9q2yqinfd2qssz6-profile, qk58h5mal4pn346fnlhvlb6zmw3khr3p-profile.drv)
```

# Discussion History
# Action History
- Created by: tobtoht | 2025-01-07T12:51:00+00:00
