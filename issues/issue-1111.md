---
title: Remove ability to select database type from 10.0 upwards?
source_url: https://github.com/monero-project/monero/issues/1111
author: ghost
assignees: []
labels: []
created_at: '2016-09-20T22:26:30+00:00'
updated_at: '2016-09-29T19:53:49+00:00'
type: issue
status: closed
closed_at: '2016-09-29T19:53:49+00:00'
---

# Original Description
I still note that the system allows us to select Berkeley DB

```
# default database:
# should be lmdb for testing, memory for production still
# set(DATABASE memory)
```

Is it pretty straight forward to remove this option and leave us with just LMDB? 

I don't mind tinkering if so.


# Discussion History
## radfish | 2016-09-21T02:24:14+00:00
If approved, please remember to drop libdb from README deps section, too.


## ghost | 2016-09-21T22:13:54+00:00
So...a couple of questions:
1. Can blockchain_export be deprecated for v.10 because we're not going to be format shifting any more? 
2. Are we set on LMDB for the foreseeable future, meaning that if we wish to add a new database type 10 years down the line somebody else can look back at the old code repo for hints, or should I leave in all the appropriate hooks for selecting different database types...which will add (admittedly tiny) unnecessary overhead with a couple of variables stored in memory during compilation, but might make people wonder why bits were just commented out...and then of course excluded code decays over time etc.


## radfish | 2016-09-22T03:05:45+00:00
On Wed, Sep 21, 2016 at 03:13:57PM -0700, NanoAkron wrote:

> So...can blockchain_export be deprecated for v.10 because we're not going to be format shifting? 

Isn't export useful regardless of internal format? For example, to
distribute .raw on the website?


## moneromooo-monero | 2016-09-22T18:54:43+00:00
Keep blockchain_export as radfish said, and we want to support other db backends, even though we have just lmdb now.


## ghost | 2016-09-22T19:19:28+00:00
@moneromooo-monero OK, that means basically leaving everything intact except reporting the database selection in CMakeLists.txt

Should be pretty straightforward really.


## radfish | 2016-09-23T00:46:36+00:00
On Thu, Sep 22, 2016 at 12:19:31PM -0700, NanoAkron wrote:

> @moneromooo-monero OK, that means basically leaving everything intact except reporting the database selection in CMakeLists.txt

Agreed if it's not already reporting the DB being used.

Btw, also consider tweaking those couple messages in cmake to not say
"could not find... X using Y". Instead, rephase to just "using Y"
because the current messages look like an error but are not an error.
I think there are ~3 messages like these now.


## moneromooo-monero | 2016-09-24T12:26:48+00:00
If not too late, I think it's be better to leave the db selection stuff, but have only LMDB as an option. This will avoid having to redo it once another backend gets added. If it's too late, then fair enough, it can be revived later.


## ghost | 2016-09-29T19:53:49+00:00
I'm not going to tackle this just yet so will close the issue to improve the signal-to-noise a bit.


# Action History
- Created by: ghost | 2016-09-20T22:26:30+00:00
- Closed at: 2016-09-29T19:53:49+00:00
