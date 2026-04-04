---
title: What's _mh_execute_header?
source_url: https://github.com/monero-project/monero/issues/1623
author: kenshi84
assignees: []
labels: []
created_at: '2017-01-23T15:21:14+00:00'
updated_at: '2022-04-28T07:32:27+00:00'
type: issue
status: closed
closed_at: '2017-08-22T09:44:28+00:00'
---

# Original Description
I'm trying debug build Monero on Mac and failing with the following error:

```
Undefined symbols for architecture x86_64:
  "__mh_execute_header", referenced from:
      _get_blocks_dat_start in libblocks.a(blockexports.c.o)
      _get_blocks_dat_size in libblocks.a(blockexports.c.o)
ld: symbol(s) not found for architecture x86_64
```

`_mh_execute_header` is only used in src/blocks/blockexports.c and only for the Mac build. The linker can somehow find the symbol in the release mode but not in the debug mode. This library looks a little unusual in that it appears to create object files directly from *.dat files. Can anyone please give me a hint?

# Discussion History
## moneromooo-monero | 2017-08-07T17:10:20+00:00
Is that fixed now ? :)

## kenshi84 | 2017-08-22T09:44:28+00:00
Yes, sorry for my late reply :)

## ggsoul | 2018-06-07T02:18:30+00:00
@kenshi84 I have the same error. How fixed?

## kenshi84 | 2018-06-08T02:23:23+00:00
I don't observe this issue anymore.

## KouMeanSun | 2022-04-28T07:32:27+00:00
how to do /

# Action History
- Created by: kenshi84 | 2017-01-23T15:21:14+00:00
- Closed at: 2017-08-22T09:44:28+00:00
