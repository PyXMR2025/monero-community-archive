---
title: 'Fails to build on Octa Core Cortex A53 - Android tablet T585 '
source_url: https://github.com/xmrig/xmrig/issues/2211
author: killamah
assignees: []
labels: []
created_at: '2021-03-25T22:21:11+00:00'
updated_at: '2021-04-12T13:47:19+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:47:19+00:00'
---

# Original Description
Hi i have error to make on **Octa Core Cortex A53** 

**cmake ..     done
make         get error something about 'maes'** 

If i add :

**cmake .. -DARM_TARGET=8 
make          get error : Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A**

So i try :

**cmake .. -DARM_TARGET=7 
make            Done ! xmrig Compiled but when i run it:**


**CPU       ARM Cortex A53 (1) 32-bit -AES**

then it's kill:

**Bus Error**

Sure because of bad CPU setting.
I see many guy that successfully compiled for Octa Core cpu.
Any help?

Thanks



# Discussion History
## Spudz76 | 2021-03-27T22:57:07+00:00
Must be a 64-bit OS with 64-bit compiler.  That error occurs when `__aarch64__` is not defined, which would happen if you are in 32-bit compiler.

Logic is [here](https://github.com/xmrig/xmrig/blob/master/src/crypto/cn/sse2neon.h#L122)

## killamah | 2021-03-28T08:58:13+00:00
Thanks , How i can do termux usinng GCC 64 compiler?

## Spudz76 | 2021-03-29T20:29:25+00:00
Unknown, would depend on your Android revision among ROM build, whether it's rooted, and other specs.

Compiling on the tablet may not be the best way, also consider finding a cross-compile toolchain for aarch64 with whichever Android SDK matches your ROM, on a regular Linux computer build xmrig there targeted for the other type of CPU, and then copy the binary over for execution on the tablet.  Tablet may not have enough memory and finding usable toolchain for install could be more difficult, and it must be slow compared to a desktop processor doing the compile work.

## killamah | 2021-03-29T21:06:17+00:00
Thanks 
I fix it by installing lineage OS 64bit. Now xmrig work great! Thanks

# Action History
- Created by: killamah | 2021-03-25T22:21:11+00:00
- Closed at: 2021-04-12T13:47:19+00:00
