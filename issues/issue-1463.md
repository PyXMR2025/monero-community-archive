---
title: DB sync modes
source_url: https://github.com/monero-project/monero/issues/1463
author: luigi1111
assignees: []
labels: []
created_at: '2016-12-16T15:02:58+00:00'
updated_at: '2017-04-17T14:16:56+00:00'
type: issue
status: closed
closed_at: '2017-04-17T14:16:55+00:00'
---

# Original Description
safe/fast when why how etc.

(Continues #706 )

# Discussion History
## iamsmooth | 2016-12-22T22:42:45+00:00
It was pointed out that it is hard to tell when the DB is synced in order to switch to safe mode.

I don't think this is a huge issue because we probably don't ever want to use unsafe modes after the first sync. If you have previously synced and have a non-corrupt DB stored locally, you probably don't want to corrupt it (and need a full resync to recover) by having a catch-up sync fail (people who really do want this can use some advanced setting).

So I'd suggest something like using a fast/unsafe mode on first open when creating a new DB. After that always use a safe mode. (Again, advanced settings are possible for people who know what they are doing and want them.)


## ghost | 2016-12-23T10:11:04+00:00
@hyc, what do you think?

## hyc | 2016-12-23T15:40:32+00:00
Sounds OK to me. I'll think about how to patch that in. Basically we would only allow unsafe if the DB is empty on open. Just need to detect a non-default command-line setting.

But this only helps someone who has stopped and restarted their daemon. We still want to know sync has finished, for a daemon that's been left running.

## iamsmooth | 2016-12-25T02:38:51+00:00
> We still want to know sync has finished, for a daemon that's been left running.

Yes I thought about that at first and didn't come up with anything great. Maybe switch unconditionally after 24 hours? Switch on the first occurrence of elapsed time between new blocks added to the DB >2 minutes?

## moneromooo-monero | 2016-12-26T11:50:34+00:00
I'd say when a block is added to the database, that's not from a sync call. This means the blockchain's top block at the time was the same as what miners were mining on.

## iamsmooth | 2016-12-26T18:53:18+00:00
Sure that seems doable, though it might require changing the interfaces a bit to pass down a "syncing" flag.

## hyc | 2016-12-26T19:15:11+00:00
just for reference, I'm timing a few different approaches to sync-from-scratch. Will see how big a perf difference there is. On a server with HDD, so this is going quite slowly so far.

## hyc | 2017-02-21T01:05:25+00:00
I believe the default sync mode is pretty safe now with PR #1506. Should probably close this issue.

## dternyak | 2017-04-16T23:13:52+00:00
Bump @luigi1111 @fluffypony - trying to help close resolved issues. 

## luigi1111 | 2017-04-17T14:16:55+00:00
Closing (see #1506).

# Action History
- Created by: luigi1111 | 2016-12-16T15:02:58+00:00
- Closed at: 2017-04-17T14:16:55+00:00
