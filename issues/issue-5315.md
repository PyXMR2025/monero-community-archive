---
title: clear screen command
source_url: https://github.com/monero-project/monero/issues/5315
author: maogo
assignees: []
labels: []
created_at: '2019-03-19T14:47:10+00:00'
updated_at: '2019-07-24T03:14:08+00:00'
type: issue
status: closed
closed_at: '2019-03-19T15:02:31+00:00'
---

# Original Description
When print too much , how to clear ，
Like "CLS" command in DOS,  already exists or not?
 

# Discussion History
## moneromooo-monero | 2019-03-19T14:50:48+00:00
"clear" on bash/sh.

In monero tools themselves, no. But since it's multitasking nowadays, you can just run monerod in a shell and do other stuff in others. You can use the --log-level option if you want less logs too, though 
I think that's not really what you're asking.

# Action History
- Created by: maogo | 2019-03-19T14:47:10+00:00
- Closed at: 2019-03-19T15:02:31+00:00
