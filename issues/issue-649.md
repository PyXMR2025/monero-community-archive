---
title: Use 'nproc' to get usable number of CPUs
source_url: https://github.com/monero-project/monero-gui/issues/649
author: voidzero
assignees: []
labels:
- resolved
created_at: '2017-03-30T20:07:46+00:00'
updated_at: '2018-11-18T17:18:31+00:00'
type: issue
status: closed
closed_at: '2018-11-18T17:18:31+00:00'
---

# Original Description
For Linux, get_libwallet_api.sh and build_libwallet_api.sh currently learn the *total* amount of CPU cores by looking at /proc/cpuinfo. Better is to use the output of the `nproc` command, because the command returns the number of *available* cpu cores. For example, I have a CPU with 8 cores. However, I've programmed my X session to only use cores 2-7 by issuing `taskset -cp 2-7 $$` from my `.xinitrc`. That means that there are only 6 cores available which is returned correctly by `nproc` but is not reflected in /proc/cpuinfo.

This is less trivial than it seems from my example. If a user builds monero-core from an lxc (or docker) container, /proc/cpuinfo will also contain the total amount of cpus. But those environments often run in limited environments - those which have less CPUs available. If such run with 4 available cores, and make runs with `-j8` the build process actually slows down.

Therefore it would be advisable to use `nproc`.

Additionally `nproc --all` for the total number of CPUs / cores can be useful, for make's `-l` parameter. From `make(1)`:

```
-l [load], --load-average[=load]
     Specifies  that  no  new  jobs  (commands)  should  be
     started if there are others jobs running and the  load
     average  is  at  least load (a floating-point number).
     With no argument, removes a previous load limit.
```

So I suggest to use `nproc` for make's `-j` and use `nproc --all` for make's `-l`.

# Discussion History
## voidzero | 2017-03-30T20:11:26+00:00
One additional suggestion: prefixing the build process with `chrt -b 0` will also speed up the build process somewhat, because it changes the job scheduler from the default SCHED_OTHER scheduler to the SCHED_BATCH scheduler - which is intended for non-interactive processes. See `chrt(1)` for more info. Of course, this all only applies to Linux - not FreeBSD!

## ghost | 2017-03-31T00:42:59+00:00
Would you be interested in submitting a PR yourself? 

## voidzero | 2017-04-27T10:49:25+00:00
Trying to keep up with my old issues a bit better :-) yes I'll make a PR for this.

## erciccione | 2018-11-18T13:25:09+00:00
@voidzero Is this still valid?

## sanderfoobar | 2018-11-18T14:55:16+00:00
PR welkom voidzero :-)

+resolved

# Action History
- Created by: voidzero | 2017-03-30T20:07:46+00:00
- Closed at: 2018-11-18T17:18:31+00:00
