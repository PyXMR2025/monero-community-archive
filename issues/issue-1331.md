---
title: 'ocl_generic_rx_generator.cpp: config->ScratchpadL3_Size random value'
source_url: https://github.com/xmrig/xmrig/issues/1331
author: komatom
assignees: []
labels: []
created_at: '2019-11-29T13:29:23+00:00'
updated_at: '2019-11-30T11:28:50+00:00'
type: issue
status: closed
closed_at: '2019-11-30T11:28:50+00:00'
---

# Original Description
This below is output of inialization of ocl_generic_rx_generator.cpp:

device_mem and dataset_mem are in Megabytes.
per_thead is in bytes

Is it normal config->ScratchpadL3_Size to varies between 2129920, 1081344 and 294912 for the different cards, which btw are the same model

`
const auto config      = RxAlgo::base(algorithm);
const uint32_t per_thread_mem = config->ScratchpadL3_Size + 32768;
`

===========
device mem: 4096 : dataset_mem: 2207
per_thread: 2129920

device mem: 4096 : dataset_mem: 2207
per_thread: 2129920

device mem: 4096 : dataset_mem: 2207
per_thread: 2129920

device mem: 4096 : dataset_mem: 2207
per_thread: 1081344

device mem: 4096 : dataset_mem: 2207
per_thread: 1081344

device mem: 4096 : dataset_mem: 2207
per_thread: 1081344

device mem: 4096 : dataset_mem: 2207
per_thread: 1081344

device mem: 4096 : dataset_mem: 2207
per_thread: 1081344

device mem: 4096 : dataset_mem: 2207
per_thread: 1081344

device mem: 4096 : dataset_mem: 2207
per_thread: 1081344

device mem: 4096 : dataset_mem: 2207
per_thread: 1081344

device mem: 4096 : dataset_mem: 2207
per_thread: 294912

device mem: 4096 : dataset_mem: 2207
per_thread: 294912

device mem: 4096 : dataset_mem: 2207
per_thread: 294912

device mem: 4096 : dataset_mem: 2207
per_thread: 294912

device mem: 4096 : dataset_mem: 2207
per_thread: 294912

device mem: 4096 : dataset_mem: 2207
per_thread: 294912

device mem: 4096 : dataset_mem: 2207
per_thread: 294912

device mem: 4096 : dataset_mem: 2207
per_thread: 294912



# Discussion History
## SChernykh | 2019-11-29T14:11:32+00:00
These are per thread requirements for rx/0, rx/wow, rx/arq algorithms. It configures them one after another.

## komatom | 2019-11-30T11:28:50+00:00
Thanks, for clarifying. 

# Action History
- Created by: komatom | 2019-11-29T13:29:23+00:00
- Closed at: 2019-11-30T11:28:50+00:00
