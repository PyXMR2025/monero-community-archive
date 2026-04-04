---
title: 'bitmonerod terminates with exception "boost: mutext lock failed in pthread_mutex_lock:
  Invalid argument"'
source_url: https://github.com/monero-project/monero/issues/874
author: radfish
assignees: []
labels: []
created_at: '2016-06-21T22:57:12+00:00'
updated_at: '2017-09-24T19:25:59+00:00'
type: issue
status: closed
closed_at: '2017-09-24T19:25:58+00:00'
---

# Original Description
Daemon crashes with this in `/tmp/bitmonero.daemon.stdout.stderr`:

```
info   {1}terminate called after throwing an instance of
'boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::lock_error> >'
what():  boost: mutex lock failed in pthread_mutex_lock: Invalid argument
```

Observed only when running with `--detach` from systemd service, but the bug is unlikely to be specific to that circumstance, it just happens to not be manifest otherwise. Also, not manifesting (even from systemd) on a different machine with no obvious differences (a slightly older build, but unlikely to have any relevant differences).

**Potential workaround**: add `max-concurrency=1` to config file or CLI.

commit: a645a3e5ff286d36837a6fb30210ba55548dc231
compiler flags: ~~-fno-strict-aliasing~~ (EDIT: no, I put it in wrong place, this build is without this flag)
linker flags: -fno-associative-math (otherwise get this unexpected warning, treated as error: ""warning: -fassociative-math disabled; other options take precedence")
ARMv7h, Arch Linux, gcc 6.1.1
boost 1.60.0 (official package from Arch repos)

Related? #373 #264 


# Discussion History
## moneromooo-monero | 2016-06-22T08:13:52+00:00
Do you have a stack trace to see where this is coming from ?


## radfish | 2017-09-24T19:25:58+00:00
Not seeing this any longer.

# Action History
- Created by: radfish | 2016-06-21T22:57:12+00:00
- Closed at: 2017-09-24T19:25:58+00:00
