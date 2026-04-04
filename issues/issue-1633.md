---
title: .daemon_lock not deleted after monerod exit
source_url: https://github.com/monero-project/monero/issues/1633
author: ghost
assignees: []
labels: []
created_at: '2017-01-25T23:50:21+00:00'
updated_at: '2017-02-19T03:53:51+00:00'
type: issue
status: closed
closed_at: '2017-02-19T03:53:51+00:00'
---

# Original Description
As per title. Each time I exit, I still find `.daemon_lock` in my `.bitmonero` directory.

# Discussion History
## IPGlider | 2017-01-26T17:20:04+00:00
There is no _need_ to remove the file on exit, it is created each time the daemon starts if it does not exists and a lock acquired over it if there is none already, otherwise the daemon does not start.

Should it be deleted?


## ghost | 2017-01-26T20:29:20+00:00
So if the file already exists when the daemon starts, is there any risk it will not acquire the lock and therefore malfunction?

## IPGlider | 2017-01-27T11:42:43+00:00
Doesn't seem so.

`boost::interprocess::file_lock`[0] is being used. I have tested it and works.

[0] http://www.boost.org/doc/libs/1_44_0/doc/html/boost/interprocess/file_lock.html

## moneromooo-monero | 2017-01-27T20:42:56+00:00
It's not the file that serves as a lock, it's a file lock on the file. When the process does, the file lock is automatically released by the kernel, so it's safe against crashes.

Now, for the sake of cleanliness, it could certainly be removed, yes.

## ghost | 2017-01-28T13:15:38+00:00
What function would I call to delete a file? 

## moneromooo-monero | 2017-01-28T14:37:29+00:00
    r = boost::filesystem::remove(old_file);
    if (!r) {
      LOG_ERROR("error removing file: " << old_file);
    }


## vtnerd | 2017-01-28T15:45:45+00:00
The interface to this function is confusing BTW. The boolean return code indicates whether the file existed. `remove(std::string)` throws on filesystem errors (permissions, etc.), and `remove(std::string, boost::system::error_code)` returns errors via the code object.

## ghost | 2017-01-29T12:25:15+00:00
Urgh...I'm guessing since we had permission to create and write to the file, that removing it would also be ok?

## moneromooo-monero | 2017-01-29T12:46:41+00:00
Usually, yes :)

## ghost | 2017-01-29T23:58:32+00:00
I've tried my best but I can't figure out how to refer to the filename in the code. I've tried `db_lock` and `lock_path.string()` without luck :(

## hyc | 2017-02-06T02:38:28+00:00
This problem is going to disappear soon. As of PR#1506 it's now possible for multiple daemons to run concurrently from the same DB. Currently the daemons would still overwrite each other's poolstate and p2pstate files, so that still needs to be adjusted. (I believe PR#1641 solves that now.) With everything out of the way we won't need the daemon_lock any more.

This way we can have separate daemons on multiple ports using the same DB. (E.g., one for public access with restricted rpc, and one for private access. Or one on clearnet and one on TOR. Or all of the above.)

Also, we'll probably move the poolstate into its own LMDB database so it can also be safely shared between multiple daemons. 

## ghost | 2017-02-06T07:49:06+00:00
@hyc Oooh...nice. Do you know who is doing the work?

## hyc | 2017-02-06T08:53:11+00:00
I'll be looking into the mempool in LMDB. As of now things should already work if you comment out the daemon_lock. Each daemon will be using its own pool, so it's not optimal. Also, @IPGlider reported a DB conflict after some hours of running so it needs some more testing and investigation.

## hyc | 2017-02-06T10:30:53+00:00
I take that back - it will not work smoothly in its current state. The daemons screw each other up if one does a map resize, the other should notice it but doesn't.

## hyc | 2017-02-07T19:16:30+00:00
Turns out that my previous map resize problem was that I was running a 32bit daemon and a 64bit daemon on the same DB. This doesn't work on Linux because mutexes aren't structured the same way btw 32bit and 64bit glibc. (It would work fine on just about every other platform LMDB supports though.) Running two 64bit daemons together is no problem.

## ghost | 2017-02-19T03:53:51+00:00
Fixed by PR #1748

# Action History
- Created by: ghost | 2017-01-25T23:50:21+00:00
- Closed at: 2017-02-19T03:53:51+00:00
