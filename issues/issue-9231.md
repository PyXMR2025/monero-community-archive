---
title: CLI wallet terminal lockscreen handler needs updating
source_url: https://github.com/monero-project/monero/issues/9231
author: tidux
assignees: []
labels:
- low priority
created_at: '2024-03-10T08:03:59+00:00'
updated_at: '2026-02-18T21:51:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Running the inside `tmux` results in garbled output if `TERM` is set to `tmux-256color` or `screen-256color`, both of which are valid on my system for various TUI applications including Emacs, Vim, and GNU Midnight Commander.  Running with the override `$ TERM=xterm-256color monero-wallet-cli` produces expected behavior. 

# Discussion History
## omurad | 2025-07-15T02:47:10+00:00
I was not able to reproduce this. Is there specific command that resulted in bad output?

```
user@devbox-vm:~/monero-x86_64-linux-gnu-v0.18.4.0$ uname -a
Linux devbox-vm 6.1.0-37-cloud-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.140-1 (2025-05-22) x86_64 GNU/Linux
user@devbox-vm:~/monero-x86_64-linux-gnu-v0.18.4.0$ echo $TERM
tmux-256color
user@devbox-vm:~/monero-x86_64-linux-gnu-v0.18.4.0$ ./monero-wallet-cli --daemon-address xmr-node.cakewallet.com:18081
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Fluorine Fermi' (v0.18.4.0-release)
Logging to ./monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): <redacted>
Wallet and key files found, loading...
Wallet password:
Opened wallet: <redacted>
**********************************************************************
Use the "help" command to see a simplified list of available commands.
Use "help all" to see the list of all available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Warning: using an untrusted daemon at xmr-node.cakewallet.com:18081
Using a third party daemon can be detrimental to your security and privacy
You are strongly encouraged to connect to the Monero network using your own daemon
If you or someone you trust are operating this daemon, you can use --trusted-daemon
Background mining not enabled. Run "set setup-background-mining 1" to change.
Starting refresh...
Height 87913 / 3455822
```

# Action History
- Created by: tidux | 2024-03-10T08:03:59+00:00
