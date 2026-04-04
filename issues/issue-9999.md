---
title: Openmonero build fails on 0.18.4.0 version
source_url: https://github.com/monero-project/monero/issues/9999
author: ruslan-y
assignees: []
labels: []
created_at: '2025-07-15T14:50:30+00:00'
updated_at: '2025-12-19T01:03:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, there!

I'm trying to build OpenMonero inside a Docker container based on ubuntu:20.04, with Monero cloned at **v0.18.4.0**

The build breaks at around 37% when compiling Account.cpp from xmregcore, with the following error:
```
/opt/monero/contrib/epee/include/span.h:165:24: error: static assertion failed: type must be trivially copyable
  165 |     static_assert(std::is_trivially_copyable<T>(), "type must be trivially copyable");
      |                        ^~~~~~~~~~~~~~~~~~~~~~~~~~
```


<details><summary>My Dockerfile</summary>

```
FROM ubuntu:20.04 as xmrbuild

ARG COIN_VERSION

RUN set -o errexit -o nounset && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get upgrade -y -q

RUN set -o errexit -o nounset && \
    export DEBIAN_FRONTEND=noninteractive && \
    export NPROC=$(nproc) && \
    echo "Number of processors: $NPROC" && \
    apt-get install -y -q --no-install-recommends \
    build-essential \
    ca-certificates \
    ccache \
    cmake \
    curl \
    doxygen \
    git \
    graphviz \
    libboost-all-dev \
    libboost-chrono-dev \
    libboost-date-time-dev \
    libboost-filesystem-dev \
    libboost-locale-dev \
    libboost-program-options-dev \
    libboost-regex-dev \
    libboost-serialization-dev \
    libboost-system-dev \
    libboost-thread-dev \
    libcurl4-openssl-dev \
    libexpat1-dev \
    libgtest-dev \
    libhidapi-dev \
    libhidapi-libusb0 \
    libldns-dev \
    liblzma-dev \
    libmysql++-dev \
    libpgm-dev \
    libprotobuf-dev \
    libreadline6-dev \
    libsodium-dev \
    libssl-dev \
    libudev-dev \
    libunbound-dev \
    libunwind8-dev \
    libusb-1.0-0-dev \
    libzmq3-dev \
    miniupnpc \
    net-tools \
    pkg-config \
    protobuf-compiler \
    python3 \
    qttools5-dev-tools \
    wget \
    && rm -rf /var/cache/apt/

WORKDIR /opt

RUN git clone --recursive https://github.com/moneroexamples/openmonero.git
RUN git clone --recursive -b v${COIN_VERSION} https://github.com/monero-project/monero.git

RUN cd monero/ && USE_SINGLE_BUILDDIR=1 make -j $NPROC

RUN mkdir openmonero/build \
    && cd openmonero/build \
    && cmake -DMONERO_DIR=/opt/monero ..

# add command 1 & command 2
# command 1
RUN cd openmonero/ext/restbed \
    && mkdir build && cd build \
    && cmake .. \
    && make -j $NPROC install
    
# command 2
RUN cp -r openmonero/ext/restbed/distribution/. openmonero/build/distribution/

RUN cd openmonero/build \
    && make -j $NPROC

ENTRYPOINT [ "/opt/openmonero/build/openmonero" ]
```

</details>


<details><summary>Full logs of building</summary>

```
Step 11/13 : RUN cp -r openmonero/ext/restbed/distribution/. openmonero/build/distribution/
 ---> Running in 2a4b639e640d
Removing intermediate container 2a4b639e640d
 ---> a0f995514003
Step 12/13 : RUN cd openmonero/build     && make -j $NPROC
 ---> Running in 4afaf2fcd8c8
Scanning dependencies of target restbed
[  3%] Creating directories for 'restbed'
Scanning dependencies of target myxrmcore
[  6%] Building CXX object src/xmregcore/src/CMakeFiles/myxrmcore.dir/MicroCore.cpp.o
[  9%] Building CXX object src/xmregcore/src/CMakeFiles/myxrmcore.dir/UniversalIdentifier.cpp.o
[ 12%] Building CXX object src/xmregcore/src/CMakeFiles/myxrmcore.dir/Account.cpp.o
[ 15%] Building CXX object src/xmregcore/src/CMakeFiles/myxrmcore.dir/tools.cpp.o
[ 18%] No download step for 'restbed'
[ 21%] No update step for 'restbed'
[ 25%] No patch step for 'restbed'
[ 28%] Performing configure step for 'restbed'
-- The CXX compiler identification is GNU 9.4.0
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
   Copyright 2013-2017, Corvusoft Ltd, All Rights Reserved.
-- Found ASIO include at: /opt/openmonero/ext/restbed/dependency/asio/asio/include
-- Found Kashmir include at: /opt/openmonero/ext/restbed/dependency/kashmir
-- Configuring done
-- Generating done
-- Build files have been written to: /opt/openmonero/build/restbed_build/src/restbed-build
[ 31%] Performing build step for 'restbed'
Scanning dependencies of target restbed
[  9%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/uri.cpp.o
[  9%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/rule.cpp.o
[ 19%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/session.cpp.o
[ 19%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/service.cpp.o
[ 23%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/session_manager.cpp.o
[ 33%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/detail/http_impl.cpp.o
[ 33%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/detail/socket_impl.cpp.o
[ 38%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/string.cpp.o
[ 42%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/request.cpp.o
[ 47%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/settings.cpp.o
[ 57%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/http.cpp.o
[ 57%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/resource.cpp.o
[ 61%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/detail/service_impl.cpp.o
[ 66%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/response.cpp.o
[ 71%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/detail/web_socket_impl.cpp.o
[ 76%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/ssl_settings.cpp.o
[ 80%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/detail/session_impl.cpp.o
[ 90%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/web_socket_message.cpp.o
[ 90%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/web_socket.cpp.o
[ 95%] Building CXX object CMakeFiles/restbed.dir/source/corvusoft/restbed/detail/web_socket_manager_impl.cpp.o
[100%] Linking CXX static library librestbed.a
[100%] Built target restbed
In file included from /opt/monero/contrib/epee/include/byte_slice.h:37,
                 from /opt/monero/contrib/epee/include/net/net_utils_base.h:37,
                 from /opt/monero/contrib/epee/include/net/net_helper.h:48,
                 from /opt/monero/contrib/epee/include/net/http_client.h:40,
                 from /opt/openmonero/src/xmregcore/src/monero_headers.h:22,
                 from /opt/openmonero/src/xmregcore/src/Account.h:3,
                 from /opt/openmonero/src/xmregcore/src/Account.cpp:1:
/opt/monero/contrib/epee/include/span.h: In instantiation of 'epee::span<const unsigned char> epee::as_byte_span(const T&) [with T = epee::mlocked<tools::scrubbed<crypto::ec_scalar> >]':
/opt/monero/contrib/epee/include/string_tools.h:93:39:   required from 'std::string epee::string_tools::pod_to_hex(const t_pod_type&) [with t_pod_type = epee::mlocked<tools::scrubbed<crypto::ec_scalar> >; std::string = std::__cxx11::basic_string<char>]'
/opt/openmonero/src/xmregcore/src/Account.h:69:42:   required from here
/opt/monero/contrib/epee/include/span.h:165:24: error: static assertion failed: type must be trivially copyable
  165 |     static_assert(std::is_trivially_copyable<T>(), "type must be trivially copyable");
      |                        ^~~~~~~~~~~~~~~~~~~~~~~~~~
[ 34%] Performing install step for 'restbed'
[100%] Built target restbed
Install the project...
-- Install configuration: ""
-- Installing: /opt/openmonero/build/distribution/include/restbed
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/uri.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/byte.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/http.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/rule.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/common.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/string.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/logger.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/request.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/service.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/session.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/settings.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/response.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/resource.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/web_socket.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/status_code.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/ssl_settings.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/context_value.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/session_manager.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/web_socket_message.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/context_placeholder.hpp
-- Installing: /opt/openmonero/build/distribution/include/corvusoft/restbed/context_placeholder_base.hpp
-- Installing: /opt/openmonero/build/distribution/library/librestbed.a
[ 37%] Completed 'restbed'
In file included from /opt/monero/contrib/epee/include/byte_slice.h:37,
                 from /opt/monero/contrib/epee/include/net/net_utils_base.h:37,
                 from /opt/monero/contrib/epee/include/net/net_helper.h:48,
                 from /opt/monero/contrib/epee/include/net/http_client.h:40,
                 from /opt/openmonero/src/xmregcore/src/monero_headers.h:22,
                 from /opt/openmonero/src/xmregcore/src/MicroCore.h:8,
                 from /opt/openmonero/src/xmregcore/src/UniversalIdentifier.hpp:3,
                 from /opt/openmonero/src/xmregcore/src/UniversalIdentifier.cpp:1:
/opt/monero/contrib/epee/include/span.h: In instantiation of 'epee::span<const unsigned char> epee::as_byte_span(const T&) [with T = epee::mlocked<tools::scrubbed<crypto::ec_scalar> >]':
/opt/monero/contrib/epee/include/string_tools.h:93:39:   required from 'std::string epee::string_tools::pod_to_hex(const t_pod_type&) [with t_pod_type = epee::mlocked<tools::scrubbed<crypto::ec_scalar> >; std::string = std::__cxx11::basic_string<char>]'
/opt/openmonero/src/xmregcore/src/Account.h:69:42:   required from here
/opt/monero/contrib/epee/include/span.h:165:24: error: static assertion failed: type must be trivially copyable
  165 |     static_assert(std::is_trivially_copyable<T>(), "type must be trivially copyable");
      |                        ^~~~~~~~~~~~~~~~~~~~~~~~~~
[ 37%] Built target restbed
make[2]: *** [src/xmregcore/src/CMakeFiles/myxrmcore.dir/build.make:102: src/xmregcore/src/CMakeFiles/myxrmcore.dir/Account.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[2]: *** [src/xmregcore/src/CMakeFiles/myxrmcore.dir/build.make:89: src/xmregcore/src/CMakeFiles/myxrmcore.dir/UniversalIdentifier.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:242: src/xmregcore/src/CMakeFiles/myxrmcore.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
The command '/bin/sh -c cd openmonero/build     && make -j $NPROC' returned a non-zero code: 2

Cleaning up project directory and file based variables
00:01
ERROR: Job failed: exit code 2
```

</details>

Same problem on ubuntu:22.04.

On previous version **0.18.3.4** build works fine.


# Discussion History
## nahuhh | 2025-07-15T15:22:50+00:00
Open issue on openmonero repo?

either way, thx for report

note: probably related to this pr https://github.com/monero-project/monero/pull/9462

## ruslan-y | 2025-07-15T15:31:36+00:00
> Open issue on openmonero repo?

yes, [created](https://github.com/moneroexamples/openmonero/issues/185)

## ruslan-y | 2025-07-15T19:28:08+00:00
@selsta  Why did you close this issue?

## selsta | 2025-07-15T19:29:04+00:00
It's an openmonero issue, not a monero issue if I understand it correctly. Otherwise I can reopen it.

## ruslan-y | 2025-07-15T19:30:48+00:00
It's a related problem. Reopen it please.

## nahuhh | 2025-07-15T19:34:58+00:00
@ruslan-y its not a monero issue. Openmonero needs to be updated

Meaning, there is nothing to fix on monero end. Openmonero needs to adapt their codebase to the pr i linked above

Example: onion explorer had a similar incompatibility
Fixed here: https://github.com/moneroexamples/onion-monero-blockchain-explorer/commit/9ea7a13b00b997de24d0dd51b9d0fc49f6a15d2e

Pinging @jeffro256 

## jeffro256 | 2025-07-16T05:14:00+00:00
Openmonero has a lot of breakages with the current Monero core repo. One of its main dependencies, xmegcore, hasn't been updated in almost 4 years. It currently has a PR, open for 3 years, to support view tags and other HF 15 stuff that hasn't been merged yet. There's not much we can do unless you can contact @moneroexamples about it.

## nahuhh | 2025-07-20T21:59:41+00:00
@ruslan-y close?

## FabriLluvia | 2025-12-19T01:03:21+00:00
> > Open issue on openmonero repo?
> 
> yes, [created](https://github.com/moneroexamples/openmonero/issues/185)

Close this issue, as you created one on OpenMonero.

# Action History
- Created by: ruslan-y | 2025-07-15T14:50:30+00:00
