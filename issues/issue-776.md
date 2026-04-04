---
title: 'simplewallet: stdout is not terminal output'
source_url: https://github.com/monero-project/monero/issues/776
author: fanatid
assignees: []
labels: []
created_at: '2016-03-29T19:48:38+00:00'
updated_at: '2016-05-10T12:34:53+00:00'
type: issue
status: closed
closed_at: '2016-05-10T12:34:53+00:00'
---

# Original Description
If run `simplewallet` when `stdout` and `stderr` is not terminal outputs (redirect to file for example), log messages is not flushed:

```
$ ./simplewallet --wallet-file 1 --password 1 --rpc-bind-port 18082 >stdout.log 2>&1
^Z
[1]+  Stopped
$ cat stdout.log
Creating the logger system
Monero 'Hydrogen Helix' (v0.9.3.0-0ee87e6)
Logging at log level 0 to /home/kirill/tmp/simplewallet.log
$ fg
^C
$ cat stdout.log
Creating the logger system
Monero 'Hydrogen Helix' (v0.9.3.0-0ee87e6)
Logging at log level 0 to /home/kirill/tmp/simplewallet.log
2016-Mar-29 22:45:31.051405 Loading wallet...
2016-Mar-29 22:45:31.095404 Loaded wallet keys file, with public address: 4AQEqg4oDFw6YM6L86CLvX26etwTKvN7gaN1fXzs18bm7TyEbpxYrHadLDY2n98m8z3zFMeg3FTaLHmJtGdJG7dSF31ny3q
2016-Mar-29 22:45:34.023976 Loaded ok
...
```

but without redirected, all ok:

```
$ ./simplewallet --wallet-file 1 --password 1 --rpc-bind-port 18082
Creating the logger system
Monero 'Hydrogen Helix' (v0.9.3.0-0ee87e6)
Logging at log level 0 to /home/kirill/tmp/simplewallet.log
2016-Mar-29 21:57:40.090158 Loading wallet...
2016-Mar-29 21:57:40.132003 Loaded wallet keys file, with public address: 4AQEqg4oDFw6YM6L86CLvX26etwTKvN7gaN1fXzs18bm7TyEbpxYrHadLDY2n98m8z3zFMeg3FTaLHmJtGdJG7dSF31ny3q
2016-Mar-29 21:57:43.112484 Loaded ok
...
```


# Discussion History
## tewinget | 2016-03-29T20:08:56+00:00
I'm not sure what the issue is here, can you be more explicit?

If I'm interpreting correctly, the expectation is that the first call to
`cat` there should print all of that stuff, but without some sense how much
time passed before Ctrl-Z, I can't say for sure that it should have.

On Tue, Mar 29, 2016 at 3:48 PM, Kirill Fomichev notifications@github.com
wrote:

> If run simplewallet when stdout and stderr is not terminal outputs
> (redirect to file for example), log messages is not flushed:
> 
> $ ./simplewallet --wallet-file 1 --password 1 --rpc-bind-port 18082 >stdout.log 2>&1
> ^Z
> [1]+  Stopped
> $ cat stdout.log
> Creating the logger system
> Monero 'Hydrogen Helix' (v0.9.3.0-0ee87e6)
> Logging at log level 0 to /home/kirill/tmp/simplewallet.log
> $ fg
> ^C
> $ cat stdout.log
> Creating the logger system
> Monero 'Hydrogen Helix' (v0.9.3.0-0ee87e6)
> Logging at log level 0 to /home/kirill/tmp/simplewallet.log
> 2016-Mar-29 22:45:31.051405 Loading wallet...
> 2016-Mar-29 22:45:31.095404 Loaded wallet keys file, with public address: 4AQEqg4oDFw6YM6L86CLvX26etwTKvN7gaN1fXzs18bm7TyEbpxYrHadLDY2n98m8z3zFMeg3FTaLHmJtGdJG7dSF31ny3q
> 2016-Mar-29 22:45:34.023976 Loaded ok
> 
> but without redirected, all ok:
> 
> $ ./simplewallet --wallet-file 1 --password 1 --rpc-bind-port 18082
> Creating the logger system
> Monero 'Hydrogen Helix' (v0.9.3.0-0ee87e6)
> Logging at log level 0 to /home/kirill/tmp/simplewallet.log
> 2016-Mar-29 21:57:40.090158 Loading wallet...
> 2016-Mar-29 21:57:40.132003 Loaded wallet keys file, with public address: 4AQEqg4oDFw6YM6L86CLvX26etwTKvN7gaN1fXzs18bm7TyEbpxYrHadLDY2n98m8z3zFMeg3FTaLHmJtGdJG7dSF31ny3q
> 2016-Mar-29 21:57:43.112484 Loaded ok
> ...
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/776

## 

Thomas Winget
Computer Engineering
Purdue University '12


## fanatid | 2016-03-29T20:12:25+00:00
@tewinget yes, you interpreting right
let say I press Ctrl-Z after 10s, loading wallet takes ~2s (for remote daemon)


## tewinget | 2016-03-29T20:16:19+00:00
Interesting.

On Tue, Mar 29, 2016 at 4:12 PM, Kirill Fomichev notifications@github.com
wrote:

> @tewinget https://github.com/tewinget yes, you interpreting right
> let say I press Ctrl-Z after 10s, loading wallet takes ~2s (for remote
> daemon)
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/776#issuecomment-203079343

## 

Thomas Winget
Computer Engineering
Purdue University '12


## antanst | 2016-03-30T06:53:36+00:00
I stumbled upon this issue some time ago when I tried to parse simplewallet's output. I ended up reading the logs instead. There's probably some kind of buffering going on.


## moneromooo-monero | 2016-03-31T12:55:28+00:00
Probably just needs a call to setvbuf to make it line buffered.


## moneromooo-monero | 2016-04-02T20:01:33+00:00
There doesn't seem to be an equivalent to setvbuf that allows line buffering, so I just flush cout.
https://github.com/monero-project/bitmonero/pull/787


## fluffypony | 2016-05-10T12:34:53+00:00
Fixed


# Action History
- Created by: fanatid | 2016-03-29T19:48:38+00:00
- Closed at: 2016-05-10T12:34:53+00:00
