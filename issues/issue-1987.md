---
title: 1024 character limit on monero-wallet-cli commands (OSX)
source_url: https://github.com/monero-project/monero/issues/1987
author: knaccc
assignees: []
labels: []
created_at: '2017-04-17T08:39:09+00:00'
updated_at: '2018-12-07T12:57:09+00:00'
type: issue
status: closed
closed_at: '2018-12-07T12:57:09+00:00'
---

# Original Description
On OSX, no more characters can be entered beyond the first 1024. This prevents more than about 9 different payees with a single transaction.

# Discussion History
## moneromooo-monero | 2017-04-17T20:44:00+00:00
This works fine on Linux. The code still uses std::getline, as it always did. I don't see any mention of a limit in the documentation, and the buffer is a std::string, not a sized array.
So it looks like a Mac lower level thing.
Did it every work before on that same machine/OS ?

## knaccc | 2017-04-18T01:00:13+00:00
I just tried it on a prior version v0.10.0.0-release, and same problem.

## rockhouse | 2017-04-18T06:52:10+00:00
The problem is with the TTY line mode. It has a max line length and mac os seems to have a max line length of 1024.
See descriptions [here](http://stackoverflow.com/questions/14368168/how-to-cin-a-c-string-1024-characters-via-bash-shell), [here](https://unix.stackexchange.com/questions/204815/terminal-does-not-accept-pasted-or-typed-lines-of-more-than-1024-characters) and [here](https://superuser.com/questions/264407/macosx-10-6-7-cuts-off-stdin-at-1024-chars). 

Try to enter it with `CTRL+D`

## knaccc | 2017-04-18T09:54:51+00:00
Thanks, yes the ^D thing did work. Unfortunately, this means the wallet can no longer be used with rlwrap. 

FYI I'm using bash, which I think is the default (echo $SHELL outputs /bin/bash)

When using the bash command line normally, there is no limit. The limit only seems to apply once I start monero-wallet-cli

## hyc | 2017-09-20T20:49:15+00:00
Compat with rlwrap should be a non-issue now that readline is natively supported. Can we close this?

## knaccc | 2017-09-20T21:46:55+00:00
I just tested monero-wallet-cli on OSX (Monero 'Helium Hydra' v0.11.0.0-release) and I still encounter the 1024 char limit. This is without using rlwrap.

Btw I can't remember what the Ctrl-D trick was that I said that worked earlier in this thread. I tried pressing it while I was testing and I could not avoid the 1024 char limit.

## hyc | 2017-09-20T22:01:09+00:00
Was your binary built with readline support?

Either way, since the 1024 character limit is in the kernel's tty driver, not sure there's anything we should be doing with this.

## knaccc | 2017-09-21T05:46:52+00:00
I'm not using binaries I built myself, I'm just using the binaries I downloaded directly from the web site. 

I guess therefore that deciding whether to close this bug or not depends on whether it is deemed important to be able to send to more than 9 recipients in the same transaction in the CLI.

## hyc | 2017-09-21T07:02:45+00:00
I didn't ask whether you built them yourself. I asked whether it had readline support. Apparently the answer to that is no.

Fyi, readline doesn't use cooked terminal mode, so this problem would go away if readline was in use. Next question is why the official binaries aren't using readline on OSX. 

## moneromooo-monero | 2017-09-21T07:43:14+00:00
Probably because it's autodetected, and so fluffypony never realized it wasn't being picked up.

## selsta | 2018-12-07T12:52:24+00:00
macOS binaries use readline now, this can be closed.

## dEBRUYNE-1 | 2018-12-07T12:53:29+00:00
+resolved

# Action History
- Created by: knaccc | 2017-04-17T08:39:09+00:00
- Closed at: 2018-12-07T12:57:09+00:00
