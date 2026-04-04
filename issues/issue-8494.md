---
title: monero-wallet-cli broken cli output
source_url: https://github.com/monero-project/monero/issues/8494
author: ghost
assignees: []
labels: []
created_at: '2022-08-10T15:07:19+00:00'
updated_at: '2025-01-26T00:22:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When I launch the monero cli application, the output is offset in weird ways, like badly formated. Backspace doesnt work either.
```
                                [wallet 45mRvR]:     e h help
[wallet 45mRvR]:                             
Important commands:

"welcome" - Show welcome message.
"help all" - Show the list of all available commands.
"help <command>" - Show a command's documentation.
"apropos <keyword>" - Show commands related to a keyword.

"wallet_info" - Show wallet main address and other info.
"balance" - Show balance.
"address all" - Show all addresses.
"address new" - Create new subaddress.
"transfer <address> <amount>" - Send XMR to an address.
"show_transfers [in|out|pending|failed|pool]" - Show transactions.
"sweep_all <address>" - Send whole balance to another wallet.
"seed" - Show secret 25 words that can be used to recover this wallet.
"refresh" - Synchronize wallet with the Monero network.
"status" - Check current status of wallet.
"version" - Check software version.
"exit" - Exit wallet.

"donate <amount>" - Donate XMR to the development team.

                                [wallet 45mRvR (out of sync)]: [wallet 45mRvR (out of sync)]: 
[wallet 45mRvR (out of sync)]:                                               [wallet 45mRvR (out of sync)]:     help      
[wallet 45mRvR (out of sync)]:                                               [wallet 45mRvR (out of sync)]:     help    
[wallet 45mRvR (out of sync)]:                                           Error: Unknown command 'he', try 'help'
                                              [wallet 45mRvR (out of sync)]:     
```

Version: Monero 'Fluorine Fermi' (v0.18.0.0-release)

If you need any more info let me know.

# Discussion History
## selsta | 2022-08-10T15:10:33+00:00
Which OS? How did you install it (package manager / website / self compiled)?

## ghost | 2022-08-10T15:26:19+00:00
@selsta Downloaded the offical 64bit binary package for linux

## selsta | 2022-08-10T16:41:52+00:00
Are you using tmux / screen? What is your `$TERM` set to? See also https://github.com/monero-project/monero/issues/6713

## ghost | 2022-08-10T19:01:11+00:00
TERM=rxvt-unicode-256color

I wasnt using tmux when creating this issue

## ghost | 2022-08-10T19:04:46+00:00
@selsta Thanks, running with `TERM=xterm ./monero-wallet-cli` did the trick. Although I think you guys should at least mark this somewhere in your repo as a bug or something cause this really is just a workaround. I wonder why this works though, what library is monero-cli using?

## selsta | 2022-08-10T19:08:12+00:00
We simply don't have fallback entries for it: https://github.com/monero-project/monero/blob/master/contrib/depends/patches/ncurses/fallback.c#L11

## selsta | 2022-08-10T20:51:19+00:00
Is rxvt-unicode-256color frequently used?

## ghost | 2022-08-13T21:48:06+00:00
@selsta Not sure if frequently, but it is used by rxvt-unicode a very popular alternative to xterm.

## diegorodriguezv | 2025-01-26T00:21:58+00:00
Same with alacritty through ssh.


# Action History
- Created by: ghost | 2022-08-10T15:07:19+00:00
