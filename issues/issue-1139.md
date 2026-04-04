---
title: 'macOS High Sierra build error: ld: library not found for -lwallet_merged'
source_url: https://github.com/monero-project/monero-gui/issues/1139
author: bref2013
assignees: []
labels:
- resolved
created_at: '2018-02-25T05:03:08+00:00'
updated_at: '2018-07-04T10:36:28+00:00'
type: issue
status: closed
closed_at: '2018-07-04T10:36:28+00:00'
---

# Original Description
-F/usr/local/Cellar/qt/5.10.1/lib -L/Users/lee/Downloads/monero-gui-master/monero/lib -lwallet_merged -lepee -lunbound -leasylogging -lreadline -L/usr/local/lib -L/usr/local/opt/openssl/lib -L/usr/local/opt/boost/lib -lboost_serialization -lboost_thread-mt -lboost_system -lboost_date_time -lboost_filesystem -lboost_regex -lboost_chrono -lboost_program_options -lssl -lcrypto -ldl -framework QtQuick -framework QtGui -framework QtCore -framework DiskArbitration -framework IOKit -framework QtQml -framework QtNetwork -framework QtWidgets -framework OpenGL -framework AGL 
ld: library not found for -lwallet_merged
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [release/bin/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui] Error 1

macOS High Sierra 10.13.3 (17D47)
with brew install all the boost, openssl and so on.
there is one time generate app, but cannot the GUI wallet cannot link to daemon.

Is there any advice why can't compile the gui wallet?
thanks a lot ahead

# Discussion History
## NullPiotrException | 2018-03-01T13:56:19+00:00
Well, I had this error but I also had another one with "-lepee". Fixed that by adding more RAM to my VM. 1 GB -> 3 GB. Probably not the case if you're not using VM.

Generally I read somewhere that this error is a result of errors before. So maybe send output of the compilation to some file and check it for "error" and "fail" and try to fix the first one.

## BigslimVdub | 2018-03-05T18:50:19+00:00
I had this issue with AEON rebase gui using ver1.2 but it was fixed with v1.3 for high Sierra. 

## sanderfoobar | 2018-03-30T00:27:18+00:00
I believe this was resolved in monero-project/monero#3296. Could you verify by building latest master?

## dEBRUYNE-1 | 2018-07-04T08:30:02+00:00
Given the inactivity of this issue, I am going to close it. 

+resolved 

## dEBRUYNE-1 | 2018-07-04T08:37:38+00:00
+resolved

# Action History
- Created by: bref2013 | 2018-02-25T05:03:08+00:00
- Closed at: 2018-07-04T10:36:28+00:00
