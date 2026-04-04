---
title: file access to data-dir is not checked
source_url: https://github.com/monero-project/monero/issues/8151
author: DavidBruchmann
assignees: []
labels: []
created_at: '2022-01-22T12:15:35+00:00'
updated_at: '2024-06-27T07:45:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
File access to data-dir is not checked and the leads to missing or wrong log-messages.
On some level something like this can be logged and shown in cli:
```
ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
```
and after changing some access rights but not sufficient, only the info about opening is shown:
```
INFO	global	src/cryptonote_core/cryptonote_core.cpp:517	Loading blockchain from folder G:\___MONERO___\lmdb ...
```
In both case the culprit is only getting visible by an adjusted bat-file with the additional failing parameter ('--data-dir' ):
```
REM Execute the Monero daemon and then stay with window open after it exits
"C:\Program Files\Monero GUI Wallet\monerod.exe" --data-dir="G:\___MONERO___"
PAUSE
```
executing this, shows at least the response "Access denied"
```
MINGW64 /c/Program Files/Monero GUI Wallet
$ ./monero-daemon.bat

C:\Program Files\Monero GUI Wallet>REM Execute the Monero daemon and then stay with window open after it exits

C:\Program Files\Monero GUI Wallet>"C:\Program Files\Monero GUI Wallet\monerod.exe" --data-dir="G:\___MONERO___"
Access is denied.

C:\Program Files\Monero GUI Wallet>PAUSE
```

Access rights in windows are a pain for me and concerning this I couldn't solve the issue yet, but at least correct error-messages would have reduced the pain.  Therefore I also can't describe in detail what I did to shift from error-message one to the lapidary info-message, I changed several details and neither can recall everyone nor I know which one might be responsible that the net-work-message disappeared. At least I never changed anything which was really related to the network but concerning access rights and users.   
The strange thing is that I had access in the beginning when I entered the new path in the gui, but opening it again after shutting down wasn't possible anymore. but this is another problem and might need another git-issue.

This issue might be related to #6533 and #3874.
It might also related to many or all issues that can be found with the search for "data-dir".

# Discussion History
## thoran | 2023-02-02T10:56:06+00:00
I found the error quote confusing also. While I suspected that the directory not being writable was the issue, I nonetheless appreciate that this issue was here to confirm those suspicions.

## ttkdigital | 2024-06-27T07:45:32+00:00
I agree this error was SO confusing - had me chasing my tail for weeks to be honest. THIS post, while horrified that he was using standard windows setup and doing everything on C:, led to a solution. So while I had the gui running I could not get it to work. I created a bat as described and ran that in command window - and finally got the "access denied" error instead of the meaningless could not connect to Florin message. Saved the bat, setup a shortcut to open the command window as authenticator and opened it - BOOM working for the first time in AGES. Thanks for your input @DavidBruchmann , really appreciate it ;)

# Action History
- Created by: DavidBruchmann | 2022-01-22T12:15:35+00:00
