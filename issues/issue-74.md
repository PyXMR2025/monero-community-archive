---
title: xmrig on FPGA or Jetson or Raspberry
source_url: https://github.com/xmrig/xmrig/issues/74
author: gigahashes
assignees: []
labels: []
created_at: '2017-08-29T15:13:42+00:00'
updated_at: '2017-10-02T12:01:49+00:00'
type: issue
status: closed
closed_at: '2017-10-02T12:01:49+00:00'
---

# Original Description
Has anyone tried running xmrig on Nvidia Jetson TK1? or any other FPGA or Raspberry Pi boards? Please share your experience? Is it worth while? The whole idea is to bring down the mining cost. thanks

# Discussion History
## atarate | 2017-09-06T21:21:04+00:00
Require 2 MB L3 cache per thread to run the miner along with the support for AES-NI Instruction set.
This is very uncommon in FPGAs and Rasberry Pi Boards. Don't Know about Nvidia Jetson TK1 as never used it.
CPU Mining with ARM is possible but requires a lot of work.

# Action History
- Created by: gigahashes | 2017-08-29T15:13:42+00:00
- Closed at: 2017-10-02T12:01:49+00:00
