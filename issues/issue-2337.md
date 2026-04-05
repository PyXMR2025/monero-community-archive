---
title: Auto changes in config.json after the first run
source_url: https://github.com/xmrig/xmrig/issues/2337
author: Peter-Liska
assignees: []
labels: []
created_at: '2021-05-02T11:33:40+00:00'
updated_at: '2021-05-02T18:57:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
After first run, the file config.json is automatically changed.
But some changes only look like changes, but there are no changes. It's little confusing.
For example
**"log-file": null,**
**"retries": 5,**
**"retry-pause": 5,**
only change their positions in file, but parameters remain the same.

**To Reproduce**
Download xmrig and run.
Compare original config.json and config.json after first run.

**Expected behavior**
Only real changes in config.json should occur.

**Required data**
 - OS: Windows 10

# Discussion History
## Spudz76 | 2021-05-02T17:58:23+00:00
Items are written in a particular order always.

If you want it to not change the file, put the items in the "correct" order to begin with? :)

## Peter-Liska | 2021-05-02T18:13:21+00:00
> If you want it to not change the file, put the items in the "correct" order to begin with? :)

Default order is set in releases: https://github.com/xmrig/xmrig/releases
User often changes only pools parameters.

Need to be in same order as it is changed after run:
https://github.com/xmrig/xmrig/blob/master/src/config.json



## GideonLight | 2021-05-02T18:57:58+00:00
Please can I mine with my android device with 6GB Ram and 125GB storage
data ? What do I need to start mining on my device connected to
unminable.com

On Sun, May 2, 2021, 7:13 PM Peter Liska ***@***.***> wrote:

> If you want it to not change the file, put the items in the "correct"
> order to begin with? :)
> Default order is set in releases: https://github.com/xmrig/xmrig/releases
> User often changes only pools parameters.
>
> Same order as it is changed after run:
> https://github.com/xmrig/xmrig/blob/master/src/config.json
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2337#issuecomment-830849186>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ATXSJE7OL64PQLF2YVAYB3TTLWI5NANCNFSM437J7PSA>
> .
>


# Action History
- Created by: Peter-Liska | 2021-05-02T11:33:40+00:00
