---
title: Unable to build docker image
source_url: https://github.com/monero-project/monero/issues/9524
author: modernNeo
assignees: []
labels:
- reproduction needed
- more info needed
created_at: '2024-10-20T06:25:15+00:00'
updated_at: '2025-01-14T16:14:11+00:00'
type: issue
status: closed
closed_at: '2025-01-14T16:14:11+00:00'
---

# Original Description
```
$ docker build -t monero .
.
.
.
.
288.5 make[2]: Leaving directory '/src/contrib/depends/work/build/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src'
288.5 Staging protobuf...
288.5 make[2]: warning: jobserver unavailable: using -j1.  Add '+' to parent make rule.
288.5 make[2]: Entering directory '/src/contrib/depends/work/build/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf'
288.5  /usr/bin/install -c -m 644  google/protobuf/any.h google/protobuf/any.pb.h google/protobuf/api.pb.h google/protobuf/arena.h google/protobuf/arena_impl.h google/protobuf/arenastring.h google/protobuf/arenaz_sampler.h google/protobuf/descriptor.h google/protobuf/descriptor.pb.h google/protobuf/descriptor_database.h google/protobuf/duration.pb.h google/protobuf/dynamic_message.h google/protobuf/empty.pb.h google/protobuf/endian.h google/protobuf/explicitly_constructed.h google/protobuf/extension_set.h google/protobuf/extension_set_inl.h google/protobuf/field_access_listener.h google/protobuf/field_mask.pb.h google/protobuf/generated_enum_reflection.h google/protobuf/generated_enum_util.h google/protobuf/generated_message_bases.h google/protobuf/generated_message_reflection.h google/protobuf/generated_message_tctable_decl.h google/protobuf/generated_message_tctable_impl.h google/protobuf/generated_message_util.h google/protobuf/has_bits.h google/protobuf/implicit_weak_message.h google/protobuf/inlined_string_field.h google/protobuf/map.h google/protobuf/map_entry.h google/protobuf/map_entry_lite.h google/protobuf/map_field.h google/protobuf/map_field_inl.h google/protobuf/map_field_lite.h google/protobuf/map_type_handler.h google/protobuf/message.h google/protobuf/message_lite.h google/protobuf/metadata.h google/protobuf/metadata_lite.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/php'
288.5  /usr/bin/install -c -m 644  google/protobuf/compiler/php/php_generator.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/php'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler'
288.5  /usr/bin/install -c -m 644  google/protobuf/compiler/code_generator.h google/protobuf/compiler/command_line_interface.h google/protobuf/compiler/importer.h google/protobuf/compiler/parser.h google/protobuf/compiler/plugin.h google/protobuf/compiler/plugin.pb.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/objectivec'
288.5  /usr/bin/install -c -m 644  google/protobuf/compiler/objectivec/objectivec_generator.h google/protobuf/compiler/objectivec/objectivec_helpers.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/objectivec'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/cpp'
288.5  /usr/bin/install -c -m 644  google/protobuf/compiler/cpp/cpp_generator.h google/protobuf/compiler/cpp/file.h google/protobuf/compiler/cpp/generator.h google/protobuf/compiler/cpp/helpers.h google/protobuf/compiler/cpp/names.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/cpp'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/util'
288.5  /usr/bin/install -c -m 644  google/protobuf/util/delimited_message_util.h google/protobuf/util/field_comparator.h google/protobuf/util/field_mask_util.h google/protobuf/util/json_util.h google/protobuf/util/message_differencer.h google/protobuf/util/time_util.h google/protobuf/util/type_resolver.h google/protobuf/util/type_resolver_util.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/util'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/csharp'
288.5  /usr/bin/install -c -m 644  google/protobuf/compiler/csharp/csharp_doc_comment.h google/protobuf/compiler/csharp/csharp_generator.h google/protobuf/compiler/csharp/csharp_names.h google/protobuf/compiler/csharp/csharp_options.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/csharp'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/ruby'
288.5  /usr/bin/install -c -m 644  google/protobuf/compiler/ruby/ruby_generator.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/ruby'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/stubs'
288.5  /usr/bin/install -c -m 644  google/protobuf/stubs/bytestream.h google/protobuf/stubs/callback.h google/protobuf/stubs/casts.h google/protobuf/stubs/common.h google/protobuf/stubs/hash.h google/protobuf/stubs/logging.h google/protobuf/stubs/macros.h google/protobuf/stubs/map_util.h google/protobuf/stubs/mutex.h google/protobuf/stubs/once.h google/protobuf/stubs/platform_macros.h google/protobuf/stubs/port.h google/protobuf/stubs/status.h google/protobuf/stubs/stl_util.h google/protobuf/stubs/stringpiece.h google/protobuf/stubs/strutil.h google/protobuf/stubs/template_util.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/stubs'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf'
288.5  /usr/bin/install -c -m 644  google/protobuf/parse_context.h google/protobuf/port.h google/protobuf/port_def.inc google/protobuf/port_undef.inc google/protobuf/reflection.h google/protobuf/reflection_internal.h google/protobuf/reflection_ops.h google/protobuf/repeated_field.h google/protobuf/repeated_ptr_field.h google/protobuf/service.h google/protobuf/source_context.pb.h google/protobuf/struct.pb.h google/protobuf/text_format.h google/protobuf/timestamp.pb.h google/protobuf/type.pb.h google/protobuf/unknown_field_set.h google/protobuf/wire_format.h google/protobuf/wire_format_lite.h google/protobuf/wrappers.pb.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/io'
288.5  /usr/bin/install -c -m 644  google/protobuf/io/coded_stream.h google/protobuf/io/io_win32.h google/protobuf/io/printer.h google/protobuf/io/strtod.h google/protobuf/io/tokenizer.h google/protobuf/io/zero_copy_stream.h google/protobuf/io/zero_copy_stream_impl.h google/protobuf/io/zero_copy_stream_impl_lite.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/io'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/java'
288.5  /usr/bin/install -c -m 644  google/protobuf/compiler/java/generator.h google/protobuf/compiler/java/java_generator.h google/protobuf/compiler/java/kotlin_generator.h google/protobuf/compiler/java/names.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/java'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/python'
288.5  /usr/bin/install -c -m 644  google/protobuf/compiler/python/generator.h google/protobuf/compiler/python/pyi_generator.h google/protobuf/compiler/python/python_generator.h '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/include/google/protobuf/compiler/python'
288.5 make[2]: Leaving directory '/src/contrib/depends/work/build/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src'
288.5 make[2]: warning: jobserver unavailable: using -j1.  Add '+' to parent make rule.
288.5 make[2]: Entering directory '/src/contrib/depends/work/build/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d'
288.5  /usr/bin/mkdir -p '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/lib/pkgconfig'
288.5  /usr/bin/install -c -m 644 protobuf.pc protobuf-lite.pc '/src/contrib/depends/work/staging/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d/src/contrib/depends/x86_64-linux-gnu/lib/pkgconfig'
288.5 make[2]: Leaving directory '/src/contrib/depends/work/build/x86_64-linux-gnu/protobuf/21.12-9aeddd7937d'
288.6 Postprocessing protobuf...
288.6 Caching protobuf...
289.0 copying packages: native_protobuf boost openssl zeromq expat unbound sodium eudev ncurses readline hidapi protobuf libusb
289.0 to: /src/contrib/depends/x86_64-linux-gnu
290.0 make[1]: Leaving directory '/src/contrib/depends'
290.0 cd build/x86_64-linux-gnu/release && USE_DEVICE_TREZOR_MANDATORY=1 cmake -DCMAKE_TOOLCHAIN_FILE=/src/contrib/depends/x86_64-linux-gnu/share/toolchain.cmake ../../.. && make
290.1 -- CMake version 3.16.3
290.1 -- Could NOT find PythonInterp (missing: PYTHON_EXECUTABLE) 
290.1 -- The C compiler identification is GNU 9.4.0
290.1 -- The CXX compiler identification is GNU 9.4.0
290.1 -- Check for working C compiler: /usr/bin/gcc
290.2 -- Check for working C compiler: /usr/bin/gcc -- works
290.2 -- Detecting C compiler ABI info
290.2 -- Detecting C compiler ABI info - done
290.2 -- Detecting C compile features
290.2 -- Detecting C compile features - done
290.2 -- Check for working CXX compiler: /usr/bin/g++
290.2 -- Check for working CXX compiler: /usr/bin/g++ -- works
290.2 -- Detecting CXX compiler ABI info
290.3 -- Detecting CXX compiler ABI info - done
290.3 -- Detecting CXX compile features
290.3 -- Detecting CXX compile features - done
290.4 -- Found usable ccache: /usr/bin/ccache
290.4 -- The ASM compiler identification is GNU
290.4 -- Found assembler: /usr/bin/gcc
290.4 -- Looking for -Wl,--no-undefined linker flag
290.4 -- Looking for -Wl,--no-undefined linker flag - found
290.4 -- Looking for -Wl,-undefined,error linker flag
290.4 -- Looking for -Wl,-undefined,error linker flag - found
290.8 -- Building build tag linux-x64
290.8 -- Found Git: /usr/bin/git (found version "2.25.1") 
290.8 -- Checking submodules
290.8 -- Submodule 'external/miniupnp' is up-to-date
290.8 -- Submodule 'external/rapidjson' is up-to-date
290.8 -- Submodule 'external/trezor-common' is up-to-date
290.8 -- Submodule 'external/randomx' is up-to-date
290.8 -- Submodule 'external/supercop' is up-to-date
290.8 -- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
290.8 -- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
290.8 -- Building for a 64-bit system
290.8 -- Building internal libraries as static
290.8 -- Using LMDB as default DB type
290.8 -- Stack trace on exception disabled
290.8 -- Looking for pthread.h
290.8 -- Looking for pthread.h - found
290.8 -- Performing Test CMAKE_HAVE_LIBC_PTHREAD
290.8 -- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
290.8 -- Check if compiler accepts -pthread
290.9 -- Check if compiler accepts -pthread - yes
290.9 -- Found Threads: TRUE  
290.9 -- Performing Test _Werror__pthread_c
290.9 -- Performing Test _Werror__pthread_c - Success
290.9 -- Performing Test _Werror__pthread_cxx
291.0 -- Performing Test _Werror__pthread_cxx - Success
291.0 -- Found OpenSSL: /src/contrib/depends/x86_64-linux-gnu/lib/libcrypto.a   
291.0 -- Using OpenSSL include dir at /src/contrib/depends/x86_64-linux-gnu/include
291.0 -- Found HIDAPI: /src/contrib/depends/x86_64-linux-gnu/lib/libhidapi-libusb.a  
291.0 -- Looking for memset_s in c
291.0 -- Looking for memset_s in c - not found
291.0 -- Looking for explicit_bzero in c
291.1 -- Looking for explicit_bzero in c - found
291.1 -- Looking for strptime
291.1 -- Looking for strptime - found
291.1 -- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
291.1 -- Using in-tree miniupnpc
291.1 -- Looking for libunbound
291.1 -- Found libunbound include (unbound.h) in /src/contrib/depends/x86_64-linux-gnu/include
291.1 -- Found libunbound library
291.1 -- Using 64-bit LMDB from source tree
291.1 -- Looking for backtrace
291.2 -- Looking for backtrace - found
291.2 -- backtrace facility detected in default set of libraries
291.2 -- Backtrace_LIBRARY: 
291.2 -- Found Backtrace: /usr/include  
291.2 -- Performing Test _maes_cxx
291.2 -- Performing Test _maes_cxx - Success
291.2 -- Setting CXX flag -maes
291.2 -- Performing Test _maes_c
291.3 -- Performing Test _maes_c - Success
291.3 -- Setting C flag -maes
291.3 -- Performing Test HAVE_SSSE3
291.3 -- Performing Test HAVE_SSSE3 - Success
291.3 -- Performing Test HAVE_AVX2
291.3 -- Performing Test HAVE_AVX2 - Success
291.3 -- Performing Test HAVE_CXX_ATOMICS
291.4 -- Performing Test HAVE_CXX_ATOMICS - Success
291.4 -- Using HIDAPI include dir at /src/contrib/depends/x86_64-linux-gnu/include/hidapi
291.4 -- Could NOT find Protobuf (missing: Protobuf_DIR)
291.4 -- Found Protobuf: /src/contrib/depends/x86_64-linux-gnu/lib/libprotobuf.a (found version "3.21.12") 
291.4 CMake Error at cmake/CheckTrezor.cmake:28 (message):
291.4   Trezor: Python not found
291.4 
291.4   ==========================================================================
291.4 
291.4   [ERROR] To compile without Trezor support, set USE_DEVICE_TREZOR=OFF.  It
291.4   is possible both via cmake variable and environment variable, e.g.,
291.4   `USE_DEVICE_TREZOR=OFF make release`
291.4 
291.4   For more information, please check src/device_trezor/README.md
291.4 
291.4 Call Stack (most recent call first):
291.4   cmake/CheckTrezor.cmake:97 (trezor_fatal_msg)
291.4   CMakeLists.txt:709 (include)
291.4 
291.4 
291.4 -- Could NOT find PythonInterp (missing: PYTHON_EXECUTABLE) 
291.4 -- Configuring incomplete, errors occurred!
291.4 See also "/src/build/x86_64-linux-gnu/release/CMakeFiles/CMakeOutput.log".
291.4 See also "/src/build/x86_64-linux-gnu/release/CMakeFiles/CMakeError.log".
291.4 make: *** [Makefile:51: depends] Error 1
------
Dockerfile:26
--------------------
  25 |     ARG NPROC
  26 | >>> RUN set -ex && \
  27 | >>>     git submodule init && git submodule update && \
  28 | >>>     rm -rf build && \
  29 | >>>     if [ -z "$NPROC" ] ; \
  30 | >>>     then make -j$(nproc) depends target=x86_64-linux-gnu ; \
  31 | >>>     else make -j$NPROC depends target=x86_64-linux-gnu ; \
  32 | >>>     fi
  33 |     
--------------------
ERROR: failed to solve: process "/bin/sh -c set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z \"$NPROC\" ] ;     then make -j$(nproc) depends target=x86_64-linux-gnu ;     else make -j$NPROC depends target=x86_64-linux-gnu ;     fi" did not complete successfully: exit code: 2
```

```
$ git log -1
commit 893916ad091a92e765ce3241b94e706ad012b62a (HEAD -> master, origin/master, origin/HEAD)
Merge: 7df0d9bb8 89ad8ac8b
Author: luigi1111 <luigi1111w@gmail.com>
Date:   Mon Oct 14 10:17:10 2024 -0400

    Merge pull request #9435
    
    89ad8ac epee: string_tools: keep full path in cut_off_extension (tobtoht)
    c51ca53 epee: string_tools: remove dot from get_extension (tobtoht)

$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

```

# Discussion History
## NyanCod3r | 2024-10-26T15:57:27+00:00
They forgot some dependencies: 
   - Installed `libssl-dev` for OpenSSL.
   - Installed `libunbound-dev` for Unbound.
   - Installed `libboost-all-dev` for Boost.
   - Installed `libsodium-dev` for Sodium.
   - Installed `libzmq3-dev` for ZeroMQ.
I'll create a pull request.

## NyanCod3r | 2024-10-26T18:31:48+00:00
Ah no my bad, it was just missing python3.

## shaked8634 | 2024-12-25T11:57:44+00:00
Solved this by adding the Dockerfile: 
```Dockerfile
ENV USE_DEVICE_TREZOR=OFF
```

IMHO this should go into the official Dockerfile (or install Python)

## modernNeo | 2024-12-25T22:28:39+00:00
well how can we use the Dockerfile **with** trezor?

## shaked8634 | 2024-12-25T22:47:43+00:00
Good point. I'll check tomorrow how to solve it the other way around

## shaked8634 | 2024-12-26T12:16:40+00:00
I bumped the Ubuntu image and just installed python3 and now image seems to build and run. Can't check the specifics of Trezor's thought:
Note that to you need to set the desired UID (or remove it from the `useradd`):

```Dockerfile
# Multistage docker build, requires docker 17.05

# builder stage
FROM ubuntu:24.04 as builder

ENV USE_DEVICE_TREZOR=ON

RUN set -ex && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends --yes install \
        automake \
        autotools-dev \
        bsdmainutils \
        build-essential \
        ca-certificates \
        ccache \
        cmake \
        curl \
        git \
        libtool \
        pkg-config \
        gperf \
        python3

WORKDIR /src
RUN git clone -q --depth 1 https://github.com/monero-project/monero.git

ARG NPROC
ENV USE_DEVICE_TREZOR=OFF
RUN cd /src/monero && \
    set -ex && \
    git submodule init && git submodule update && \
    rm -rf build && \
    if [ -z "$NPROC" ] ; \
    then make -j$(nproc) depends target=x86_64-linux-gnu ; \
    else make -j$NPROC depends target=x86_64-linux-gnu ; \
    fi

# runtime stage
FROM ubuntu:24.04

ENV UID=10016

RUN set -ex && \
    apt-get update && \
    apt-get --no-install-recommends --yes install ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt

COPY --from=builder /src/monero/build/x86_64-linux-gnu/release/bin /usr/local/bin/

# Create monero user
RUN useradd --uid $UID --system --user-group monero && \
        mkdir -p /wallet /home/monero/.bitmonero && \
        chown -R monero:monero /home/monero/.bitmonero && \
        chown -R monero:monero /wallet

# Contains the blockchain
VOLUME /home/monero/.bitmonero

# Generate your wallet via accessing the container and run:
# cd /wallet
# monero-wallet-cli
VOLUME /wallet

EXPOSE 18080
EXPOSE 18081

# switch to user monero
USER monero

ENTRYPOINT ["monerod"]
CMD ["--p2p-bind-ip=0.0.0.0", "--p2p-bind-port=18080", "--rpc-bind-ip=0.0.0.0", "--rpc-bind-port=18081", "--non-interactive", "--confirm-external-bind"]
```

## tankf33der | 2025-01-05T12:35:03+00:00
lets close this issue if image successfully built.

## modernNeo | 2025-01-05T20:02:32+00:00
has the image been updated in the repo? if it hasn't the issue is still relevant imo

## shaked8634 | 2025-01-05T20:24:34+00:00
There's PR #9477 that should also solved this

## modernNeo | 2025-01-05T20:30:13+00:00
then this issue should not be closed until after that is merged imo

# Action History
- Created by: modernNeo | 2024-10-20T06:25:15+00:00
- Closed at: 2025-01-14T16:14:11+00:00
