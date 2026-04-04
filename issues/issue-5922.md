---
title: Locked due to inactivity - password is required - On wallet with no password
source_url: https://github.com/monero-project/monero/issues/5922
author: trasherdk
assignees: []
labels:
- duplicate
created_at: '2019-09-22T11:35:29+00:00'
updated_at: '2019-09-25T17:49:37+00:00'
type: issue
status: closed
closed_at: '2019-09-25T17:49:37+00:00'
---

# Original Description
Running a few wallet cli and rpc in screen sessions on testnet, I noticed high CPU usage
on that server. It turns out that the 2 `monero-wallet-cli` is both looping like crazy,
with the below output.

Attaching to the screen session, and hitting [ENTER] stops the loop, for whatever
time the `idle` timeout is at.

Those 2 are throwaway test wallets, and there is no password set.

```
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.

Wallet password: 
[wallet 9wiAxp]:
```


# Discussion History
## moneromooo-monero | 2019-09-22T12:29:05+00:00
Is that a duplicate of #5719 ?

## trasherdk | 2019-09-22T15:41:45+00:00
No, not same situation.  Well, I'm still running in screen, but.

Before, the password prompt came when receiving funds.  
Now, it's a idle lock something.

When run in screen it looks like this:
```
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.

Wallet password: 
[wallet 9zwQfv]: set ask-password never
Wallet password: Error: failed to read wallet password
[wallet 9zwQfv]:                
```
When run in bash, no  screen, it looks like this:
```
 ____________________________________________   
/ I locked your Monero wallet to protect you \
\ while you were away                        /
 --------------------------------------------
        \   (__)
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||


Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: 
[wallet 9wiAxp]: set ask-password never
Wallet password: 
[wallet 9wiAxp]:                
```
I don't know what `set ask-password never` is supposed to do, because I'm prompted for a password anyway.

I guess, I'm missing a `set idle-timeout 0` command :)

EDIT: I forgot. I'm running `Monero 'Boron Butterfly' (v0.14.1.2-2c171a9b0)` (master).

## moneromooo-monero | 2019-09-22T16:26:02+00:00
ask-password is for the "ask before a command that spends or similar". The lock screen is buggy if ask-password isn't set, I'll fix. As you found, disable it with idle-timeout.

## trasherdk | 2019-09-23T02:18:17+00:00
Well, I didn't find `idle-timeout`, but after diving into `./src/simplewallet/simplewallet.cpp:3437` 
I found `CHECK_SIMPLE_VARIABLE("inactivity-lock-timeout",...`.

This setting is not shown by `help set` command, and is not accepted as a command line parameter.

While this setting works, when invoked in a `not screen session`, it does not have any effect in a `screen session`.
```
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.

Wallet password: 
[wallet 9zwQfv]:                
[wallet 9zwQfv]: set inactivity-lock-timeout 0
Wallet password: Error: failed to read wallet password
```


## moneromooo-monero | 2019-09-23T11:11:40+00:00
Ah so it's the same bug after all...
If you set the idle timeout to 0 *while not using screen*, it works fine afterwards in screen right (except it can't read passwords) ?

## trasherdk | 2019-09-23T11:28:11+00:00
The `set inactivity-lock-timeout 0` works when launching `monero-wallet-cli` on commandline, no screen involved.

When launching the same command with `screen -S name -d -m bash -c` prepended, it doesn't work.


## moneromooo-monero | 2019-09-23T11:31:07+00:00
Yes, but after it's set, you don't get the lock screen while in screen, right ?

## trasherdk | 2019-09-23T11:37:11+00:00
When in screen, I don't get the lock screen, just the 
```
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
```
scrolling up the screen like crazy. Maybe 100 lines per second.
It stops when I hit ENTER.

Also, when in screen the
```
[wallet 9zwQfv]: set inactivity-lock-timeout 0
Wallet password: Error: failed to read wallet password
```
has no effect. On next timeout the `Locked due to inactivity` start again.


## moneromooo-monero | 2019-09-23T11:38:32+00:00
Very weird. When you are in screen, if you type "set", what is the value of the timeout ?

## trasherdk | 2019-09-23T11:46:21+00:00
`inactivity-lock-timeout = 90`
```
[wallet 9zwQfv]: set inactivity-lock-timeout 0
Wallet password: Error: failed to read wallet password
```
After `set inactivity-lock-timeout 0` it's still `inactivity-lock-timeout = 90`


## moneromooo-monero | 2019-09-23T11:48:20+00:00
You've set the timeout while not in screen, right ?

## trasherdk | 2019-09-23T11:51:24+00:00
So, I actually get the lock screen at some point:
```
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.

Wallet password: 
 ____________________________________________   
/ I locked your Monero wallet to protect you \
\ while you were away                        /
 --------------------------------------------
        \   (__)
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||


Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
Locked due to inactivity. The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
```


## trasherdk | 2019-09-23T11:55:18+00:00
Is it a persistent variable/setting?

While NOT in screen, `inactivity-lock-timeout = 90`
`set inactivity-lock-timeout 0`
`inactivity-lock-timeout = 0`


## trasherdk | 2019-09-23T11:58:13+00:00
Hmm, now back in screen `inactivity-lock-timeout = 0` so it appears to be persistent :)
Let's see what happens....

## moneromooo-monero | 2019-09-23T12:01:32+00:00
It is persistent, that's why the password is needed as it writes back to the keys file.

## trasherdk | 2019-09-23T12:04:52+00:00
Okay, but what's up with the (in screen):
```
[wallet 9zwQfv]: set inactivity-lock-timeout 0
Wallet password: Error: failed to read wallet password
```


## moneromooo-monero | 2019-09-23T12:10:16+00:00
Is it different from the previous bug ?

## trasherdk | 2019-09-23T12:30:05+00:00
I don't know. It might be.
I'm unable to set `inactivity-lock-timeout`.
I'm prompted for a password, but doesn't wait to get one.

This could be a command line parameter. The password is available already from the start.
`monero-wallet-cli --testnet --password '' --wallet-file ...`

## hyc | 2019-09-23T15:09:29+00:00
You're starting the CLI incorrectly. 

> When launching the same command with `screen -S name -d -m bash -c` prepended, it doesn't work.  

You're using "bash -c" which tells bash to fire off a one-shot process without a tty attached. That's why the CLI's attempts to read from stdin are failing. Don't do that. This is not a wallet bug.

## trasherdk | 2019-09-23T15:21:47+00:00
This one is probably related.
When making a transfer, I paste the receiving address into the terminal, like this:
A **NON** screen session:
```
[wallet 9wiAxp]: transfer 9zwQfvQvvLrBURLrmw4rS61n8hWMXgijdGf8e7e6Q7EWR7WCKenAqsYQHto7dymD2KP4Wh5Sym5DoX5FTXCYdMomGzGPMzW9zwQfvQvvLrBURLrmw4rS61n8hWMXgijdGf8e7e6Q7EWR7WCKenAqsYQHto7dymD2KP4Wh5Sym5DoX5FTXCYdMomGzGPMzW
```
A screen session: (before paste address)
```
[wallet 9zwQfv]: wallet_info    
Filename: /home/crypto/local/build/build-monero-pool/data/testnet/wallets/miner-wallet
Description: <Not set>
Address: 9zwQfvQvvLrBURLrmw4rS61n8hWMXgijdGf8e7e6Q7EWR7WCKenAqsYQHto7dymD2KP4Wh5Sym5DoX5FTXCYdMomGzGPMzW
Type: Normal
Network type: Testnet
[wallet 9zwQfv]: transfer       
```
A screen session: (after paste address)
```
[wallet 9zwQfv]: wallet_info    
Filename: /home/crypto/local/build/build-monero-pool/data/testnet/wallets/miner-wallet
Description: <Not set>
Address: 9zwQfvQvvLrBURLrmw4rS61n8hWMXgijdGf8e7e6Q7EWR7WCKenAqsYQHto7dymD2KP4Wh5Sym5DoX5FTXCYdMomGzGPMzW
Type: Normal
Network type: Testnet
RM5DVrFyBJ3fRz1Kn9NZWfUE8anRJt6psJ6jAH3N8|9DDVqvJQmtaWKDe1QJN59nu3KDg4YUkbSE3ASes 
----------------------------------curser-^
```
So my bet is on either readline, ncurses or termcap getting screwed by screen.


## trasherdk | 2019-09-23T15:29:25+00:00
@hyc It's the same behavior with, or without, the `bash -c` part. I've tried.

From `man bash`
```
-c        If  the  -c option is present, then commands are read from the first non-
         option argument command_string.  If there are arguments  after  the  com‐
         mand_string,  they  are  assigned  to the positional parameters, starting
```

## hyc | 2019-09-23T16:14:33+00:00
Fwiw, when I try this the wallet-cli immediately exits when it fails to read the password.
E.g.,
````
screen -S wal1 -d -m ./monero-wallet-cli --testnet
screen -x
````
````
strace -p <wallet-cli PID>
strace: Process 11887 attached
read(0, 0x55d6a881dcd0, 1024)           = ? ERESTARTSYS (To be restarted if SA_RESTART is set)
--- SIGWINCH {si_signo=SIGWINCH, si_code=SI_KERNEL} ---
read(0, "testnet1\n", 1024)             = 9
ioctl(0, TIOCGWINSZ, {ws_row=40, ws_col=100, ws_xpixel=0, ws_ypixel=0}) = 0
ioctl(0, TIOCSWINSZ, {ws_row=40, ws_col=100, ws_xpixel=0, ws_ypixel=0}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, SNDCTL_TMR_STOP or TCSETSW, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
stat("testnet1.keys", {st_mode=S_IFREG|0600, st_size=1428, ...}) = 0
stat("testnet1", {st_mode=S_IFREG|0600, st_size=4708631, ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, SNDCTL_TMR_STOP or TCSETSW, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
write(1, "Wallet and key files found, load"..., 39) = 39
ioctl(0, TIOCGWINSZ, {ws_row=40, ws_col=100, ws_xpixel=0, ws_ypixel=0}) = 0
ioctl(0, TIOCSWINSZ, {ws_row=40, ws_col=100, ws_xpixel=0, ws_ypixel=0}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, SNDCTL_TMR_STOP or TCSETSW, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
stat("testnet1.keys", {st_mode=S_IFREG|0600, st_size=1428, ...}) = 0
stat("testnet1", {st_mode=S_IFREG|0600, st_size=4708631, ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, SNDCTL_TMR_STOP or TCSETSW, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
write(1, "Wallet password: ", 17)       = 17
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, SNDCTL_TMR_START or TCSETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
read(0, "", 1024)                       = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, SNDCTL_TMR_START or TCSETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(1, TCGETS, {B9600 opost isig icanon echo ...}) = 0
write(1, "\33[1;31mError: failed to read wal"..., 48) = 48
write(1, "\n", 1)                       = 1
ioctl(0, TIOCGWINSZ, {ws_row=40, ws_col=100, ws_xpixel=0, ws_ypixel=0}) = 0
ioctl(0, TIOCSWINSZ, {ws_row=40, ws_col=100, ws_xpixel=0, ws_ypixel=0}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, SNDCTL_TMR_STOP or TCSETSW, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
futex(0x7ffd24b8aa88, FUTEX_WAKE_PRIVATE, 1) = 1
futex(0x7ffd24b8aa38, FUTEX_WAKE_PRIVATE, 1) = 1
futex(0x7f20192b29d0, FUTEX_WAIT, 11888, NULL) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, SNDCTL_TMR_STOP or TCSETSW, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
futex(0x7ffd24b89f70, FUTEX_WAKE_PRIVATE, 1) = 0
futex(0x7ffd24b8a080, FUTEX_WAKE_PRIVATE, 1) = 0
munlock(0x7ffd24b8a000, 4096)           = 0
futex(0x7ffd24b8a930, FUTEX_WAKE_PRIVATE, 1) = 0
futex(0x7ffd24b8aa40, FUTEX_WAKE_PRIVATE, 1) = 0
munlock(0x55d6a7ee0000, 4096)           = 0
exit_group(1)                           = ?
+++ exited with 1 +++
````
When `screen -x` attaches to the session I have a prompt for the wallet filename, which I enter. After that the screen session terminates immediately, so strace was the only way to find out what it was doing.

## trasherdk | 2019-09-23T16:24:52+00:00
Try the same, but with `--wallet-file` and `--password` on the launch.

## hyc | 2019-09-23T16:26:18+00:00
This testnet wallet has no password. If I specify the `--wallet-file` there is no prompt for the filename, and the cli immediately fails to read password and exits.

OK, so I added `--password ''` and now I'm seeing what you're reporting.


## hyc | 2019-09-23T16:30:45+00:00
Strange, in this strace, it isn't even trying to read.
````
write(1, "Wallet password: ", 17)       = 17
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, SNDCTL_TMR_START or TCSETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, SNDCTL_TMR_START or TCSETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
write(1, "\33[1;31mError: failed to read wal"..., 48) = 48
write(1, "\n", 1)                       = 1
write(1, "Locked due to inactivity. The wa"..., 81) = 81
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
write(1, "Wallet password: ", 17)       = 17
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, SNDCTL_TMR_START or TCSETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, SNDCTL_TMR_START or TCSETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
write(1, "\33[1;31mError: failed to read wal"..., 48) = 48
write(1, "\n", 1)                       = 1
write(1, "Locked due to inactivity. The wa"..., 81) = 81
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
write(1, "Wallet password: ", 17)       = 17
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, SNDCTL_TMR_START or TCSETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig -icanon -echo ...}) = 0
ioctl(0, SNDCTL_TMR_START or TCSETS, {B9600 opost isig icanon echo ...}) = 0
ioctl(0, TCGETS, {B9600 opost isig icanon echo ...}) = 0
write(1, "\33[1;31mError: failed to read wal"..., 48) = 48
write(1, "\n", 1)                       = 1
````
over and over and over

## moneromooo-monero | 2019-09-24T10:56:13+00:00
I created a wallet, set password to empty, set ask-password to never, wait for lock unlock. It works fine. So this bug is exactly the same as the previous one AFAICT (running in screen prevents password from being read). If you think it is not the case, explain precisely why, otherwise I'll close as duplicate,

## trasherdk | 2019-09-25T16:46:56+00:00
I'm not qualified to determine if it's the same. I'll take your word for it.

This problem was bypassed by opening the wallet in `wallet-cli`, and setting `inactivity-lock-timeout 0`.


## moneromooo-monero | 2019-09-25T17:45:58+00:00
OK, it looks like the same thing to me. Reopen if it's still buggy after the first one gets fixed.

+duplicate

# Action History
- Created by: trasherdk | 2019-09-22T11:35:29+00:00
- Closed at: 2019-09-25T17:49:37+00:00
