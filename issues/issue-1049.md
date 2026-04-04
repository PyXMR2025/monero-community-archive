---
title: Build native GUI clients
source_url: https://github.com/monero-project/monero-gui/issues/1049
author: rex4539
assignees: []
labels:
- wontfix
created_at: '2017-12-26T11:53:49+00:00'
updated_at: '2018-01-13T02:53:38+00:00'
type: issue
status: closed
closed_at: '2018-01-11T13:36:13+00:00'
---

# Original Description
The current situation with the QT ports is convenient, I can understand, but performance is slooooowwww...

I propose native GUI clients using a modern, fast and cross platform language. I suggest the use of [Swift](https://swift.org/about/#swiftorg-and-open-source).

The result is a modern looking and responsive client with feature parity that runs on Linux, macOS and [Windows](https://github.com/apple/swift/blob/master/docs/Windows.md).

# Discussion History
## gboelter | 2017-12-28T03:27:30+00:00
You are right, we really should have a 'modern looking and responsive client'. The current client looks and runs like Software during the time of Windows 3.11!

And this - believe me - is not the fault of Qt. If have written many applications in Qt and they all are very fast. 

## alexeyneu | 2017-12-28T13:10:10+00:00
As you know qt use  pthreads under windows. It's not about performance for sure 

## rex4539 | 2017-12-28T13:19:03+00:00
I personally use a Mac and performance feels slow.

## gboelter | 2017-12-29T02:52:09+00:00
What I mean is, Qt is not an excuse for slow performance in this case. Take a look at Karbo Wallet - https://karbo.io/ - it's Qt-based too but it's nicely designed and very fast compared with Monero.

And BTW, when I see all the issues here, I can't believe the developers are really good ...

## Jaqueeee | 2017-12-29T23:21:59+00:00
The GUI is slow when the daemon and wallet are syncing because they are using lots of CPU and disk I/o when validating the blockchain. It’s not related to Qt. Are you experiencing a slow GUI after everything is synced?

## alexeyneu | 2017-12-30T01:23:58+00:00
it is related to qt . i can answer about windows case ,it's really low-grade stuff overall ,both qt itself and this gui code. i didnt test remote procedure calls impact on performance but what i could say for sure : if just pipeline monero-wallet-cli in winapi and bundle it with pipelined monerod you'll have a fast app. I already have monerod dealt with in this style and engine holds heavy loads without wait rings( known as hourglass ) and others.

## fluffypony | 2018-01-03T14:15:46+00:00
@alexeyneu great stuff - looking forward to your pull request!

## medusadigital | 2018-01-11T13:28:46+00:00
the monero-gui project barely has recources to do anything and ofc no capacity to build a new client. 

closing issue here.


## medusadigital | 2018-01-11T13:29:26+00:00
+wontfix

## alexeyneu | 2018-01-12T18:08:14+00:00
Is this moron(stoffu) part of a crew?Another one is his bf as i understand

## stoffu | 2018-01-13T02:53:38+00:00
> Is this moron(stoffu) part of a crew?

I'm a researcher at Monero Research Lab.


# Action History
- Created by: rex4539 | 2017-12-26T11:53:49+00:00
- Closed at: 2018-01-11T13:36:13+00:00
