---
title: How can i change gpu usage?
source_url: https://github.com/xmrig/xmrig/issues/2901
author: ozansenyurt
assignees: []
labels: []
created_at: '2022-01-26T08:45:32+00:00'
updated_at: '2022-01-26T09:40:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, i want to set gpu usage from %100 to %50. I guess i can set it with source code but i couldn't find the main loop of the process. I want to set a "thread sleep" line if i can find it. Help me please, what can i do?

# Discussion History
## Spudz76 | 2022-01-26T09:21:07+00:00
Miner main loop sends an entire job run to GPU, then it runs the whole thing at full speed then replies with the result of that entire batch.

There is no way to sleep a GPU, only reduce job size and increase delay of main thread sending next job (to leave some idle time between, and spaces between more often).

These options are `bfactor` and `bsleep`, or how many subdivisions to chop each job into (factor) and how long in milliseconds to sleep between those jobs.  However bsleep only does anything on Windows as far as I know.  And both are only available in the CUDA backend (not OpenCL).  There is no way to throttle OpenCL other than reduce intensity.

## ozansenyurt | 2022-01-26T09:30:57+00:00
Thank you for your awesome help, i have another question then: How can i change intensity of gpu? Is there a way really? Thanks again

## ozansenyurt | 2022-01-26T09:40:36+00:00
by the way i just want to play games when it during mining with gpu. Is there another way to slow down the program or change priority, let me know.

# Action History
- Created by: ozansenyurt | 2022-01-26T08:45:32+00:00
