---
title: bitmonerod doesn't exit gracefully.
source_url: https://github.com/monero-project/monero/issues/223
author: oranjuice
assignees: []
labels: []
created_at: '2015-02-09T10:02:06+00:00'
updated_at: '2015-11-24T14:45:39+00:00'
type: issue
status: closed
closed_at: '2015-11-24T14:45:39+00:00'
---

# Original Description
When I enter "exit", it sometimes gets stuck at
"Stop signal sent"
and sometimes at "Node stopped".

I usually have to kill the process and free the ports myself.


# Discussion History
## fluffypony | 2015-03-26T14:57:44+00:00
@tewinget is this fixed in https://github.com/monero-project/bitmonero/pull/245 do you think?


## tewinget | 2015-03-26T17:11:49+00:00
Technically yes, but smooth raised a couple concerns about that pr last
night.  Needs further discussion.
On Mar 26, 2015 10:57 AM, "Riccardo Spagni" notifications@github.com
wrote:

> @tewinget https://github.com/tewinget is this fixed in #245
> https://github.com/monero-project/bitmonero/pull/245 do you think?
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/223#issuecomment-86552205
> .


## fluffypony | 2015-11-24T14:45:39+00:00
Mostly fixed, will need to watch to see if it continues to occur


# Action History
- Created by: oranjuice | 2015-02-09T10:02:06+00:00
- Closed at: 2015-11-24T14:45:39+00:00
