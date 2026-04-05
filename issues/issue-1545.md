---
title: Compile Xmrig tuned for Ryzen
source_url: https://github.com/xmrig/xmrig/issues/1545
author: Danny3
assignees: []
labels: []
created_at: '2020-02-10T06:01:08+00:00'
updated_at: '2020-08-29T04:59:38+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:59:38+00:00'
---

# Original Description
I have a few questions:
When Xmrig starts I can see the following line:
* Assembly       auto:ryzen

1. Is this optimization tuned for Zen / Zen+ / Zen2 or for all of them ?

I saw this article on Phoronix with some benchmarks:
https://www.phoronix.com/scan.php?page=article&item=amd-znver2-gcc9&num=1

2. If I want to tell GCC to compile the code optimized for Zen2 (Ryzen 3000), where can I specify this while building Xmrig?
Is it possible to modify one of the build commands for this, like?:
cmake .. -OPTIMIZE_FOR_ZEN2 or some other format here
In the article it seems to me that the flags were passed to GCC like this:
- -O3 -march=znver2: CXXFLAGS=-O3-march=znver2 CFLAGS=-O3-march=znver2
So, can I pass this to cmake.. to be passed to GCC or is some file where I can put it in and be read from there?

3. Since I'm compiling on the same computer where I will run the miner, do you think I can use something like:
-march=native
For the same optimizations or better for Zen2, instead of the longer line from above?

4. Do you already optimize the compiling as best as possible for Zen2 when I follow the normal build instruction you have documented and what I'm asking is useless ?

I'm hearing that GCCC 10 which should be released in the following months may bring even more optimization for Zen2, so I thought it's better to ask these questions.
Thank you!

# Discussion History
# Action History
- Created by: Danny3 | 2020-02-10T06:01:08+00:00
- Closed at: 2020-08-29T04:59:38+00:00
