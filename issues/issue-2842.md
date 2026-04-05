---
title: Mining Via Apple Silicon (M1) Tensor Cores
source_url: https://github.com/xmrig/xmrig/issues/2842
author: hilga007
assignees: []
labels: []
created_at: '2021-12-28T03:32:21+00:00'
updated_at: '2023-11-26T08:50:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
(A base model M1 MacBook has 8 CPU cores, 7 or 8 GPU cores/CUs and 16 "Neural Engine" or machine learning/tensor cores.)

[Apple's Github has Tensorflow Support for macOS in Alpha](https://github.com/apple/tensorflow_macos)

How can the 16 tensor cores be utilized via native Metal hardware acceleration drivers and TensorFlow plugins on macOS devices running ARM silicon? 

# Discussion History
## minisat0shi | 2023-11-26T07:18:32+00:00
Bump

## SChernykh | 2023-11-26T08:50:49+00:00
Tensor cores = ASIC for a single task. They can't be used for mining.

# Action History
- Created by: hilga007 | 2021-12-28T03:32:21+00:00
