---
title: Easylogger in monero-wallet-cli doesn't like invalid entries
source_url: https://github.com/monero-project/monero/issues/1977
author: ghost
assignees: []
labels: []
created_at: '2017-04-14T23:30:49+00:00'
updated_at: '2017-04-22T15:07:50+00:00'
type: issue
status: closed
closed_at: '2017-04-22T15:07:50+00:00'
---

# Original Description
Example:

```
nodey@odroidc2:~$ monero-wallet-cli --version
Monero 'Wolfram Warptangent' (v0.10.3.1-9ed496b)
```

versus handling of purposely mis-spelled 'versino'

```
nodey@odroidc2:~$ monero-wallet-cli --versino
2017-04-15 00:29:29,790 DEBUG [default] [nodey@unknown-host] [void tools::log_stack_trace(const char*)] [/home/nodey/monero/src/common/stack_trace.cpp:119] Logger [stacktrace] is not registered yet!
2017-04-15 00:29:29,790 DEBUG [default] [nodey@unknown-host] [void tools::log_stack_trace(const char*)] [/home/nodey/monero/src/common/stack_trace.cpp:120] Logger [stacktrace] is not registered yet!
2017-04-15 00:29:29,794 DEBUG [default] [nodey@unknown-host] [void tools::log_stack_trace(const char*)] [/home/nodey/monero/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-04-15 00:29:29,795 DEBUG [default] [nodey@unknown-host] [void tools::log_stack_trace(const char*)] [/home/nodey/monero/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-04-15 00:29:29,795 DEBUG [default] [nodey@unknown-host] [void tools::log_stack_trace(const char*)] [/home/nodey/monero/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-04-15 00:29:29,795 DEBUG [default] [nodey@unknown-host] [void tools::log_stack_trace(const char*)] [/home/nodey/monero/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-04-15 00:29:29,795 DEBUG [default] [nodey@unknown-host] [void tools::log_stack_trace(const char*)] [/home/nodey/monero/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-04-15 00:29:29,795 DEBUG [default] [nodey@unknown-host] [void tools::log_stack_trace(const char*)] [/home/nodey/monero/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-04-15 00:29:29,795 DEBUG [default] [nodey@unknown-host] [void tools::log_stack_trace(const char*)] [/home/nodey/monero/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-04-15 00:29:29,795 DEBUG [default] [nodey@unknown-host] [void tools::log_stack_trace(const char*)] [/home/nodey/monero/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
2017-04-15 00:29:29,795 DEBUG [default] [nodey@unknown-host] [void tools::log_stack_trace(const char*)] [/home/nodey/monero/src/common/stack_trace.cpp:158] Logger [stacktrace] is not registered yet!
Failed to parse arguments: unrecognised option '--versino'
```

# Discussion History
## moneromooo-monero | 2017-04-16T09:53:45+00:00
It happens when something is logged before the logger is initialized. But some command line options are needed to initialize the logger (eg, --log-file). I guess I could just kill that warning in easylogging itself though...

## ghost | 2017-04-18T00:11:00+00:00
Why is it failing to initialise when passed invalid command line options but not valid ones? Something to do with the internal startup sequence?

## moneromooo-monero | 2017-04-18T08:09:18+00:00
It is not failing to initialize. It is not initialized yet, as per my previous comment. The command line error handling tries to log something before it is initialized, though.

## moneromooo-monero | 2017-04-22T11:17:48+00:00
https://github.com/monero-project/monero/pull/1997

## ghost | 2017-04-22T15:07:50+00:00
Thanks! Will close. 

# Action History
- Created by: ghost | 2017-04-14T23:30:49+00:00
- Closed at: 2017-04-22T15:07:50+00:00
