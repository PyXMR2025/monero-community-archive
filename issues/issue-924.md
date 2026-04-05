---
title: Cryptonite-turtle threads not working
source_url: https://github.com/xmrig/xmrig/issues/924
author: Cexitime
assignees: []
labels: []
created_at: '2019-02-02T01:24:57+00:00'
updated_at: '2019-08-02T13:06:36+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:06:36+00:00'
---

# Original Description
Hi, 

Using -t --threads=1 on cryptonite-turtle doesnt work, when I changed algo back to -lite just to check, it started working, is the -t option broken for turtle?

looks like -max-cpu-usage=25 works

# Discussion History
## asylum119 | 2019-02-26T05:57:28+00:00
You did not set any threads for -t and are also using --threads=1 creating a conflict

Use -t 1 or --threads=1 but not both together in the same command

--algo=cn-pico/trtl works fine in latest release

Also I could be wrong but from memory max-cpu-usage is now depreciated

## DeadManWalkingTO | 2019-03-17T16:09:49+00:00

> 
> 
> You did not set any threads for -t and are also using --threads=1 creating a conflict
> 
> Use -t 1 or --threads=1 but not both together in the same command
> 
> --algo=cn-pico/trtl works fine in latest release
> 
> Also I could be wrong but from memory max-cpu-usage is now depreciated

Does the issue still exist?
Feedback please.
Thank you!

## asylum119 | 2019-07-02T03:15:35+00:00
> Does the issue still exist?
> Feedback please.
> Thank you!

OP was using commands incorrectly, I would say after this amount of time that this issue can be squashed

# Action History
- Created by: Cexitime | 2019-02-02T01:24:57+00:00
- Closed at: 2019-08-02T13:06:36+00:00
