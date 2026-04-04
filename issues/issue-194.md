---
title: tries to write log files to the location of the executable
source_url: https://github.com/monero-project/monero/issues/194
author: iamsmooth
assignees: []
labels: []
created_at: '2014-12-05T05:26:08+00:00'
updated_at: '2015-05-31T11:48:43+00:00'
type: issue
status: closed
closed_at: '2015-05-31T11:48:43+00:00'
---

# Original Description
simplewallet (and maybe bitmonerod?) uses the location of the executable to store the log files. This might be normal for Windows, but is clearly broken for linux (where executable would normally go in some non-writeable bin) and probably mac too.

In the case of simplewallet it is reasonable for the log file to go the same place as the wallet file. bitmonerod might write its log file into .bitmonero although a package manager build should probably go to a standard log location, so there should be a build option for this.


# Discussion History
## sammy007 | 2014-12-05T05:29:47+00:00
I'd like to suggest naming pattern: <code>/wallet/file/location/{wallet_file_name}.log</code>


## tewinget | 2014-12-05T06:02:23+00:00
For _nix my goto is /var/log/_

As for Windows, not sure what the default is...

At any rate, very valid point(s).  Thanks.
On Dec 5, 2014 12:29 AM, "Sammy Libre" notifications@github.com wrote:

> I'd like to suggest naming pattern:
> /wallet/file/location/{wallet_file_name}.log
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/194#issuecomment-65749275
> .


## iamsmooth | 2014-12-05T06:06:57+00:00
/var/log certainly makes sense for bitmonerod, although for simplewallet there is something to be said for sammy's suggestion, since it is a user app and not a system app, plus that is the only way to get a history of transactions performed. No matter what though, putting it with the bin is definitely wrong for linux


## netmonk | 2014-12-05T09:53:04+00:00
would be interesting to add a --log-file options when running multiples instances on the same machine


## iamsmooth | 2014-12-05T10:04:20+00:00
Yes there should definitely be a log-file option. My earlier comments were about where the default should go.


## netmonk | 2014-12-05T10:26:33+00:00
/var/log sounds good :)


## netmonk | 2014-12-05T10:34:46+00:00
but should use syslog facility, to deal with write permission in /var/log.
So option should be provided to target which facility to use in syslog. 

Or the make install under root, should deal with file creation in /var/log and setting correct permission for running bitmonerod without root priviledges


## fluffypony | 2015-05-31T11:48:43+00:00
I believe this is fixed now with the latest batch of merges.


# Action History
- Created by: iamsmooth | 2014-12-05T05:26:08+00:00
- Closed at: 2015-05-31T11:48:43+00:00
