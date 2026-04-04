---
title: Static build
source_url: https://github.com/monero-project/monero-gui/issues/909
author: danrmiller
assignees: []
labels: []
created_at: '2017-10-20T15:11:24+00:00'
updated_at: '2018-11-20T03:39:41+00:00'
type: issue
status: closed
closed_at: '2018-11-20T03:39:41+00:00'
---

# Original Description
Configure the static build target to produce a statically linked binary.

Are there differences from other software like the daemon that are reasons this shouldn't be done for the GUI? 

Of course building a binary that dynamically links to shared libs can still be chosen when that option is preferred.

For the MS Windows build, these are the 3rd-party libraries that it seems another party is building and we are distributing via https://getmonero.org/downloads. I don't think we have figured out and included appropriate license notices for these files yet either, so I thought it might be better to figure out which we actually use first.

https://github.com/monero-project/monero-core/blob/master/windeploy_helper.sh 

--- 
* libicuuc57.dll, libicuin57.dll, libicudt57.dll (libicuucd57.dll, libicuind57.dll, libicudtd57.dll for debug)

* libgcc_s_seh-1.dll (libgcc_s_dw2-1.dll for 32-bit)  

* zlib1.dll, libwinpthread-1.dll, libtiff-5.dll, libstdc++-6.dll, libpng16-16.dll, libpcre16-0.dll, libpcre-1.dll,  libmng-2.dll, liblzma-5.dll, liblcms2-2.dll, libjpeg-8.dll, libjasper-1.dll, libintl-8.dll, libiconv-2.dll, libharfbuzz-0.dll, libgraphite2.dll, libglib-2.0-0.dll, libfreetype-6.dll, libbz2-1.dll

Libjasper hasn't been included since the last release because it wasn't on the machine the maintainer built on and no error was given. But I haven't seen anyone mention it so likely that one isn't needed and can just be removed. #900 

---
 
For the linux build, it seems to be QT plugins we are including:

https://build.getmonero.org/builders/monero-core-ubuntu-amd64/builds/947/steps/deploy/logs/stdio

I'll try to research this, but maybe someone knows if this is the ideal way to handle this or not.









# Discussion History
## radfish | 2017-10-20T16:02:09+00:00
On Linux build, linking should be dynamic by default. For reasons of
security updates, consistency on the system, and memory efficiency. Debian
would not accept a statically-linked package, for example.

On Win, iirc, daemon builds statically by default in msys, so same can be done
for the GUI.


## danrmiller | 2017-10-20T16:31:55+00:00
Thanks radfish.
I don't want to change the existing dynamic build. The issue is that when the "release-static" BUILD_TYPE is given to [build.sh](https://github.com/monero-project/monero-core/blob/master/build.sh) it doesn't seem to produce a static build as expected. 

I would at least expect some of these libs such as libboost_filesystem and libboost_system to be statically linked on a static build.

```
$ ldd monero-wallet-gui 
        linux-vdso.so.1 =>  (0x00007fff28de6000)
        libxcb-glx.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-glx.so.0 (0x00007f6de3195000)
        libX11-xcb.so.1 => /usr/lib/x86_64-linux-gnu/libX11-xcb.so.1 (0x00007f6de2f93000)
        libxcb.so.1 => /usr/lib/x86_64-linux-gnu/libxcb.so.1 (0x00007f6de2d70000)
        libfontconfig.so.1 => /usr/lib/x86_64-linux-gnu/libfontconfig.so.1 (0x00007f6de2b2d000)
        libfreetype.so.6 => /usr/lib/x86_64-linux-gnu/libfreetype.so.6 (0x00007f6de2883000)
        libX11.so.6 => /usr/lib/x86_64-linux-gnu/libX11.so.6 (0x00007f6de2548000)
        libEGL.so.1 => /usr/lib/x86_64-linux-gnu/mesa-egl/libEGL.so.1 (0x00007f6de230f000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f6de210b000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f6de1f02000)
        libGL.so.1 => /usr/lib/x86_64-linux-gnu/mesa/libGL.so.1 (0x00007f6de1c90000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f6de1a73000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f6de1769000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f6de139f000)
        /lib64/ld-linux-x86-64.so.2 (0x000056554e552000)
        libXau.so.6 => /usr/lib/x86_64-linux-gnu/libXau.so.6 (0x00007f6de119b000)
        libXdmcp.so.6 => /usr/lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007f6de0f94000)
        libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007f6de0d6b000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f6de0b51000)
        libpng12.so.0 => /lib/x86_64-linux-gnu/libpng12.so.0 (0x00007f6de092b000)
        libxcb-dri2.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-dri2.so.0 (0x00007f6de0726000)
        libxcb-dri3.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-dri3.so.0 (0x00007f6de0523000)
        libxcb-present.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-present.so.0 (0x00007f6de031f000)
        libxcb-xfixes.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-xfixes.so.0 (0x00007f6de0117000)
        libxcb-sync.so.1 => /usr/lib/x86_64-linux-gnu/libxcb-sync.so.1 (0x00007f6ddff10000)
        libxshmfence.so.1 => /usr/lib/x86_64-linux-gnu/libxshmfence.so.1 (0x00007f6ddfd0c000)
        libwayland-client.so.0 => /usr/lib/x86_64-linux-gnu/libwayland-client.so.0 (0x00007f6ddfafd000)
        libwayland-server.so.0 => /usr/lib/x86_64-linux-gnu/libwayland-server.so.0 (0x00007f6ddf8eb000)
        libgbm.so.1 => /usr/lib/x86_64-linux-gnu/libgbm.so.1 (0x00007f6ddf6dd000)
        libmirclient.so.9 => /usr/lib/x86_64-linux-gnu/libmirclient.so.9 (0x00007f6ddf436000)
        libdrm.so.2 => /usr/lib/x86_64-linux-gnu/libdrm.so.2 (0x00007f6ddf225000)
        libglapi.so.0 => /usr/lib/x86_64-linux-gnu/libglapi.so.0 (0x00007f6ddeff5000)
        libXext.so.6 => /usr/lib/x86_64-linux-gnu/libXext.so.6 (0x00007f6ddede3000)
        libXdamage.so.1 => /usr/lib/x86_64-linux-gnu/libXdamage.so.1 (0x00007f6ddebe0000)
        libXfixes.so.3 => /usr/lib/x86_64-linux-gnu/libXfixes.so.3 (0x00007f6dde9d9000)
        libXxf86vm.so.1 => /usr/lib/x86_64-linux-gnu/libXxf86vm.so.1 (0x00007f6dde7d3000)
        libffi.so.6 => /usr/lib/x86_64-linux-gnu/libffi.so.6 (0x00007f6dde5ca000)
        libxkbcommon.so.0 => /usr/lib/x86_64-linux-gnu/libxkbcommon.so.0 (0x00007f6dde38b000)
        libmircommon.so.7 => /usr/lib/x86_64-linux-gnu/libmircommon.so.7 (0x00007f6dde143000)
        libmirprotobuf.so.3 => /usr/lib/x86_64-linux-gnu/libmirprotobuf.so.3 (0x00007f6ddded1000)
        libcapnp-0.5.3.so => /usr/lib/x86_64-linux-gnu/libcapnp-0.5.3.so (0x00007f6dddc49000)
        libmircore.so.1 => /usr/lib/x86_64-linux-gnu/libmircore.so.1 (0x00007f6ddda40000)
        libboost_system.so.1.58.0 => /usr/lib/x86_64-linux-gnu/libboost_system.so.1.58.0 (0x00007f6ddd83b000)
        libprotobuf-lite.so.9 => /usr/lib/x86_64-linux-gnu/libprotobuf-lite.so.9 (0x00007f6ddd60a000)
        libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f6ddd288000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f6ddd071000)
        libboost_filesystem.so.1.58.0 => /usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.58.0 (0x00007f6ddce59000)
        libkj-0.5.3.so => /usr/lib/x86_64-linux-gnu/libkj-0.5.3.so (0x00007f6ddcc2f000)
```

## erciccione | 2018-11-18T13:59:09+00:00
@danrmiller is this still valid or can be closed?

## danrmiller | 2018-11-20T03:39:41+00:00
Can be closed.

# Action History
- Created by: danrmiller | 2017-10-20T15:11:24+00:00
- Closed at: 2018-11-20T03:39:41+00:00
