---
title: Proposal for improving configs
source_url: https://github.com/xmrig/xmrig/issues/1195
author: Amf1k
assignees: []
labels: []
created_at: '2019-09-25T10:18:09+00:00'
updated_at: '2021-04-12T15:54:25+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:54:25+00:00'
---

# Original Description
Hey. Maybe it makes sense to do so that Xmrig can work without the config file and run the settings that it saves to the file for the first time? And if you need fine-tuning, then generate a settings file (for example, add the --generate-config flag).

Is it also possible to fix the config file format? to make it more convenient and clear to configure the miner. In order for each device to be represented in the "opencl" object (of all AMD, NVIDIA, Intel platforms at once), whether it is enabled or not, and settings for each algorithm with any other information for each device separately.

The meaning of these two points is that you can quickly make a first start and the miner really becomes single-file and increase the flexibility of settings, if you really need it.

# Discussion History
## xmrig | 2019-09-25T10:50:53+00:00
Miner will not override config file if set `"autosave": false,`, OpenCL part created and optimized for AMD only, Intel platform useless, for NVIDIA CUDA is better solution. If you think you have better idea, better if show this idea as part of config in JSON format.
Thank you.

## Amf1k | 2019-09-25T11:04:35+00:00
Thanks for the answer. Can then limit the platform only to AMD, because I managed to start mining on Intel 630HD (~ 45-50 h\s).

Below I presented an example of the "opencl" object in the config
```
{
   "opencl":{
      "cache":true,
      "loader":null,
      "platform":"AMD",
      "devices":[
         {
            "index":0,
            "enabled": false,
            "algorithms":{
               "cn":{
                  "intensity":480,
                  "worksize":8,
                  "strided_index":[
                     1,
                     2
                  ],
                  "threads":[
                     -1,
                     -1
                  ],
                  "unroll":8
               },
               "rx":{
                  "intensity":192,
                  "worksize":8,
                  "threads":[
                     -1,
                     -1
                  ],
                  "bfactor":6,
                  "gcn_asm":true,
                  "dataset_host":false
               }
            }
         },
         {
            "index":1,
            "enabled": true,
            "algorithms":{
               "cn":{
                  "intensity":480,
                  "worksize":8,
                  "strided_index":[
                     1,
                     2
                  ],
                  "threads":[
                     -1,
                     -1
                  ],
                  "unroll":8
               },
               "rx":{
                  "intensity":192,
                  "worksize":8,
                  "threads":[
                     -1,
                     -1
                  ],
                  "bfactor":6,
                  "gcn_asm":true,
                  "dataset_host":false
               }
            }
         }
      ]
   }
}
```

# Action History
- Created by: Amf1k | 2019-09-25T10:18:09+00:00
- Closed at: 2021-04-12T15:54:25+00:00
