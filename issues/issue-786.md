---
title: xmrig-2.8.1 compile failed on Centos 5.8
source_url: https://github.com/xmrig/xmrig/issues/786
author: eddiewang927
assignees: []
labels: []
created_at: '2018-10-09T05:30:32+00:00'
updated_at: '2018-11-05T14:25:55+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:25:55+00:00'
---

# Original Description
[root@Linux build]# cmake3 -DWITH_HTTPD=OFF -DUV_LIBRARY=/libuv/lib/libuv.a ..
-- Configuring done
-- Generating done
-- Build files have been written to: /opt/xmrig-2.8.1/build
[root@Linux build]# make
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/cnv2_main_loop.S.o
/opt/xmrig-2.8.1/src/crypto/asm/cnv2_main_loop_ivybridge.inc: Assembler messages:
/opt/xmrig-2.8.1/src/crypto/asm/cnv2_main_loop_ivybridge.inc:65: Error: no such instruction: `aesenc xmm6,xmm7'
/opt/xmrig-2.8.1/src/crypto/asm/cnv2_main_loop_ryzen.inc:63: Error: no such instruction: `aesenc xmm5,xmm6'
/opt/xmrig-2.8.1/src/crypto/asm/cnv2_double_main_loop_sandybridge.inc:109: Error: no such instruction: `aesenc xmm9,xmm2'
/opt/xmrig-2.8.1/src/crypto/asm/cnv2_double_main_loop_sandybridge.inc:135: Error: no such instruction: `aesenc xmm10,xmm11'
make[2]: *** [CMakeFiles/xmrig-asm.dir/src/crypto/asm/cnv2_main_loop.S.o] Error 1
make[1]: *** [CMakeFiles/xmrig-asm.dir/all] Error 2
make: *** [all] Error 2


# Discussion History
## xmrig | 2018-10-09T08:20:06+00:00
What version of your compiler?

# Action History
- Created by: eddiewang927 | 2018-10-09T05:30:32+00:00
- Closed at: 2018-11-05T14:25:55+00:00
