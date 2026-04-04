---
title: DB_FORCESYNC in bdb implementation not found
source_url: https://github.com/monero-project/monero/issues/262
author: arnuschky
assignees: []
labels: []
created_at: '2015-04-12T15:05:14+00:00'
updated_at: '2015-05-16T05:05:53+00:00'
type: issue
status: closed
closed_at: '2015-04-12T22:48:42+00:00'
---

# Original Description
Changes committed in e7391a411372cabbefe3fd46ba667c21cf1fa3b6 do not compile with Berkeley DB 4.8.30 (default on Ubuntu 14.04) as DB_NOSYNC is missing. No idea which version of bdb is required.

 _"In multiple threads of control, each thread of control opens a database environment and the database handles within it. When you close each database handle using the DbEnv::close() method, by default, the database is not synchronized and is similar to calling the Db::close(DB_NOSYNC) method. This is to avoid unncessary database synchronization when there are multiple environment handles open. To ensure all open database handles are synchronized when you close the last environment handle, set the flag parameter value of the DbEnv::close() method to DB_FORCESYNC. This is similar to calling the Db::close(0) method to close each database handle."_

So apparently at this point safest would be to call `Db::close(0)` and take the hit of multiple syncs.


# Discussion History
## arnuschky | 2015-04-12T16:00:10+00:00
I got  this with libdb 4.8 provided by the bitcoin project.


## tewinget | 2015-04-12T22:41:21+00:00
I guess the versions on Arch and mingw are newer/different.  I'll have a
look, thanks.

On Sun, Apr 12, 2015 at 12:00 PM, arnuschky notifications@github.com
wrote:

> I got this with libdb 4.8 provided by the bitcoin project.
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/262#issuecomment-92083454
> .

## 

Thomas Winget
Computer Engineering
Purdue University '12


## arnuschky | 2015-04-12T22:48:42+00:00
Works fine with 5.3 provided by Ubuntu default. I was just me having the 4.8 packages installed for bitcoin. I guess we can close this issue in favor or #263 


## molecular | 2015-05-16T05:05:53+00:00
Running into this with gentoo. bdb-4.8.30 is latest stable in gentoo.


# Action History
- Created by: arnuschky | 2015-04-12T15:05:14+00:00
- Closed at: 2015-04-12T22:48:42+00:00
