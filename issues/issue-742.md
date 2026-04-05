---
title: number of threads
source_url: https://github.com/xmrig/xmrig/issues/742
author: mahmoodn
assignees: []
labels: []
created_at: '2018-08-28T13:11:09+00:00'
updated_at: '2018-08-29T15:26:28+00:00'
type: issue
status: closed
closed_at: '2018-08-29T15:26:27+00:00'
---

# Original Description
By changing the number of threads in the json file, the hash rate is increased. It is expected then to see more cpu utilization. Isn't that?

However, a 90% cpu utilized process (one thread) is increased to 94% with four threads. Is that normal?

# Discussion History
## 2010phenix | 2018-08-28T13:18:37+00:00
if you ask question and open issues.... write complete info

## mahmoodn | 2018-08-28T13:40:54+00:00
I want to know what is the effect of the number of threads? If the number of threads is 4, then should I see 400% cpu utilization for one process? or 4 processes each 100% utilization? The following image shows the output of top command when xmrig is configured with 4 threads.

https://pasteboard.co/HBgJkfV.png

## mmahmoudian | 2018-08-29T10:27:52+00:00
@mahmoodn So clearly you are using xmrig-nvidia which runs on GPU and therefore the process is not detectable by `top` command. The CPU usage you see is most probably the process that distributes and aggregates the data to and from GPUs. In case you use the xmrig CPU version, you will see 400% in the `top`.

Having that said, you should have open such an issue in the [xmrig-nvidia](https://github.com/xmrig/xmrig-nvidia) repository.

## rtau | 2018-08-29T10:40:20+00:00
For your information, to see the GPU utilization, you may use `nvidia-smi`

## mahmoodn | 2018-08-29T15:26:27+00:00
Thank you. 

# Action History
- Created by: mahmoodn | 2018-08-28T13:11:09+00:00
- Closed at: 2018-08-29T15:26:27+00:00
