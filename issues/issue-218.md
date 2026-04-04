---
title: RPC rekt on/after "sweep unmixable"
source_url: https://github.com/monero-project/monero-gui/issues/218
author: sammy007
assignees: []
labels:
- resolved
created_at: '2016-11-26T20:56:14+00:00'
updated_at: '2017-08-07T20:40:08+00:00'
type: issue
status: closed
closed_at: '2017-08-07T20:40:08+00:00'
---

# Original Description
Pushed "sweep unmixable" -> "no connection to daemon, Please make sure...".

OS: OSX, monero v0.10.0, monero-core `26abdee`. Daemon is remote.

After I did it first time I even managed to restart `monerod` because `monero-core` failed to get block height on start after this error.


# Discussion History
## Jaqueeee | 2016-11-26T23:42:08+00:00
You say daemon is remote but you had to restart `monerod`? So it's your own remote daemon? If so, is it current master? Did you happen to see if the daemon crashed? There has been some reports about segfaults with current monerod master. 



## sammy007 | 2016-11-26T23:45:21+00:00
Daemon version is 0.10.0 (tag). No it didn't and I see no errors in logs. I just guessed that daemon is not ok and restarted it.

## Jaqueeee | 2016-11-26T23:53:08+00:00
ok. Did you build it yourself or did you use the official binaries?
If you can reproduce the crash/error, lldb debugger might give you some more info

If you're not familiar:
```
lldb monerod
run
(crash)
bt (to get backtrace)
```



## sammy007 | 2016-11-26T23:55:10+00:00
I will get back to it tomorrow and will try to reproduce and report. I am compiling both monerod and gui from source.

## Jaqueeee | 2016-11-26T23:59:10+00:00
ok. Thanks.
https://github.com/monero-project/monero/issues/1374 
https://github.com/monero-project/monero/issues/1377

## sammy007 | 2016-11-29T03:17:00+00:00
Well it kinda works with monero `master` branch. I can't reproduce node rpc break. Got busy cursor for a while after "No unmixable outputs" and also got "no connection to daemon" a couple of times. I am testing it via wifi, maybe something is wrong with timeout settings if there is a timeout specified on rpc call.


## medusadigital | 2017-04-18T08:54:22+00:00
can this be closed ? 

## medusadigital | 2017-08-07T20:38:08+00:00
closing this here until further notice

+resolved


# Action History
- Created by: sammy007 | 2016-11-26T20:56:14+00:00
- Closed at: 2017-08-07T20:40:08+00:00
