---
title: '[bug] in cn_slow_hash function, jh_hash cause the bug'
source_url: https://github.com/monero-project/monero/issues/9041
author: nkysg
assignees: []
labels: []
created_at: '2023-10-27T05:41:45+00:00'
updated_at: '2023-11-06T14:33:54+00:00'
type: issue
status: closed
closed_at: '2023-11-06T14:33:54+00:00'
---

# Original Description
I find that there is a bug in cn_slow_hash. When I compiled code use gcc 11.4 on ubuntu22. The compiler flag O2 and O3 get different results. The reason is caused by jh_hash. This is the code in [main.c](https://github.com/nkysg/jh-function-issue/blob/monero/src/main.c)
```c
#include <stdio.h>
#include "jh.h"
int main() {
        unsigned char input[] = "\xd6\xa1\x1a\x43\x1f\xd5\x6d\xc2\x9c\x59\x27\x32\x8e\x83\xee\xf1\x15\x90\x36\x2b"
                       "\x70\xae\xf4\x92\xf1\x2c\x44\x9b\xde\x65\x7b\x4e\x3a\xc4\xe1\x58\x16\x31\x46\x13"
                       "\xca\x73\x39\xd1\x52\x29\x4b\x18\x5e\xd8\x67\x09\xac\xc1\x26\x62\x59\x58\x0d\x4a"
                       "\xba\x72\x9d\x37\xc7\x33\xa8\x9e\xb1\x5e\xa9\x1b\x28\xbb\xe4\x9b\xd1\x51\xcb\x1b"
                       "\x94\x7b\xb2\x39\xc4\xff\x10\xcf\xe2\x4a\xa0\x5f\x31\xa8\xcd\xb8\xe7\x13\x45\xea"
                       "\x45\xcf\xfe\xff\x6b\xbf\x9d\x2c\x7f\xe5\x8f\x13\xf1\x90\xb2\x92\x1a\x53\x1f\xb6"
                       "\x58\x41\x22\x1d\x3e\x3e\x84\x83\x83\x0a\x9b\x4a\x9c\x2e\x28\x43\xe7\x4d\xb1\x79"
                       "\x2c\x73\x9d\x3e\xe2\x7a\x97\x3b\x61\xc8\x38\xf3\x00\xa5\x49\x51\xcf\x8a\xc5\xfe"
                       "\x99\xc2\xce\xd0\x5d\x8b\x4c\xff\xa2\x0a\x24\xf8\x4d\xba\x4a\x45\x28\xb2\xb2\xcf"
                       "\x03\x5a\xe5\xb0\x6b\x49\xf1\x23\x64\xfc\xb5\x77\x6d\xb3\x69\x2b\xfb\x6f\x02\x9d";

        unsigned char output[32] = {'\0'};
        jh_hash(32 * 8, input, sizeof(input) * 8, output);

	//output should be 0xea252e4fe0d223d17925f61058e2809da4896f12db26fce35faa5534575b8ce0
        printf("0x");
        for (int i = 0; i < 32; i++) {
                printf("%02x",output[i]);
        }
        printf("\n");
        return 0;
}
```
the Makefile is this https://github.com/nkysg/jh-function-issue/blob/monero/src/Makefile
```
main2:
	gcc -O2 -c jh.c -o jh2.o
	gcc -O2 -c main.c -o main2.o
	gcc main2.o jh2.o -o main2
main3:
	gcc -O3 -c jh.c -o jh3.o
	gcc -O3 -c main.c -o main3.o
	gcc main3.o jh3.o -o main3
clean:
	rm -f main2 main3  *.o
```
run ./main2 it print 0xea252e4fe0d223d17925f61058e2809da4896f12db26fce35faa5534575b8ce0
run ./main3 it print 0x48e84a3a785b8d5038d46c46ad4a09e2b8e019a6a8450acec7f36851c8dab0a7

the fact is that monero jh.c is same code as https://www3.ntu.edu.sg/home/wuhj/research/jh/jh_ansi_opt64.h. I have tested the https://www3.ntu.edu.sg/home/wuhj/research/jh/jh_sse2_opt64.h compile use O2 and O3 the result is same. 
The test code is in this https://github.com/nkysg/jh-function-issue/tree/monero. If anyone has a plan to fix this bug. Thanks.

# Discussion History
## SChernykh | 2023-10-27T11:58:17+00:00
This is a compiler bug, because gcc 9.4.0 compiles it correctly:
```
root@Ubuntu-2004-focal-64-minimal-hwe ~/jh # ls -la
total 44
drwxr-xr-x 2 root root  4096 Oct 27 13:56 .
drwx------ 8 root root  4096 Oct 27 13:55 ..
-rw-r--r-- 1 root root 25746 Aug 27  2021 jh.c
-rw-r--r-- 1 root root   849 Aug 27  2021 jh.h
-rw-r--r-- 1 root root  1489 Oct 27 13:55 main.c
root@Ubuntu-2004-focal-64-minimal-hwe ~/jh # gcc -O3 *.c -o test
root@Ubuntu-2004-focal-64-minimal-hwe ~/jh # ./test
0xea252e4fe0d223d17925f61058e2809da4896f12db26fce35faa5534575b8ce0
root@Ubuntu-2004-focal-64-minimal-hwe ~/jh # gcc -Ofast *.c -o test
root@Ubuntu-2004-focal-64-minimal-hwe ~/jh # ./test
0xea252e4fe0d223d17925f61058e2809da4896f12db26fce35faa5534575b8ce0
root@Ubuntu-2004-focal-64-minimal-hwe ~/jh # gcc --version
gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

## SChernykh | 2023-10-27T12:01:01+00:00
Incorrect result for gcc 11.4.0 confirmed:
```
root@Ubuntu-2004-focal-64-minimal-hwe ~/jh # gcc-11 -O3 *.c -o test
root@Ubuntu-2004-focal-64-minimal-hwe ~/jh # ./test
0x48e84a3a785b8d5038d46c46ad4a09e2b8e019a6a8450acec7f36851c8dab0a7
root@Ubuntu-2004-focal-64-minimal-hwe ~/jh # gcc-11 --version
gcc-11 (Ubuntu 11.4.0-2ubuntu1~20.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

## SChernykh | 2023-10-27T12:02:57+00:00
If I compile with UB sanitizer, the error magically disappears, and no undefined behavior is found:
```
root@Ubuntu-2004-focal-64-minimal-hwe ~/jh # gcc-11 -O3 *.c -o test -fsanitize=undefined
root@Ubuntu-2004-focal-64-minimal-hwe ~/jh # ./test
0xea252e4fe0d223d17925f61058e2809da4896f12db26fce35faa5534575b8ce0
```
So it's a compiler bug.

## SChernykh | 2023-10-27T12:12:17+00:00
Ok, I found the old fix I did for XMRig: https://github.com/xmrig/xmrig/commit/75c57f7563b974060088a868bdde1f70fc6dcf82

This is now in #9042 and #9043


## nkysg | 2023-10-27T13:47:17+00:00
@SChernykh Thanks for your fix.

## nkysg | 2023-10-27T14:46:14+00:00
I have seen https://www3.ntu.edu.sg/home/wuhj/research/jh/jh_sse2_opt64.h is optimize for sse2 and it 3 times faster. Do you have a plan to support it ? @SChernykh  thanks!

## SChernykh | 2023-10-27T15:05:09+00:00
There is no point to optimize this part of the code. Even when Cryptonight was Monero's PoW, this function accounted for < 0.1% of the hashing time, at best. Right now Cryptonight is only used as a key derivation function (KDF) for wallet files.

# Action History
- Created by: nkysg | 2023-10-27T05:41:45+00:00
- Closed at: 2023-11-06T14:33:54+00:00
