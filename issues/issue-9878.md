---
title: monero-wallet-cli should respect XDG Base Directory Specification
source_url: https://github.com/monero-project/monero/issues/9878
author: me-sam9
assignees: []
labels: []
created_at: '2025-03-31T18:33:11+00:00'
updated_at: '2025-06-03T14:07:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Using the `monero-wallet-cli` interface, will create and read files from the `$HOME` directory, called:

- `$HOME/{wallet-name}`
- `$HOME/{wallet-name}.keys`
- `$HOME/monero-wallet-cli.log`

I think they should be located in:

- `$XDG_DATA_HOME/monero/wallets/{wallet-name}`
- `$XDG_DATA_HOME/monero/wallets/{wallet-name}.keys`
- `$XDG_DATA_HOME/monero/log`

to respect the [XDG Base Directory Specification.](https://specifications.freedesktop.org/basedir-spec/latest/)

# Discussion History
## nahuhh | 2025-03-31T19:10:55+00:00
It doesnt use $HOME

it creates log file in the folder containing the binary, and wallet files in the working folder ($PWD)

## me-sam9 | 2025-03-31T20:38:19+00:00
I didn't notice that before, because I always called `monero-wallet-cli` from `$HOME`

Anyways, don't you think that behavior is kind of a mess?
I think we should have a default directory to store wallets, and `$XDG_DATA_HOME/monero/wallets`seems like the obvious choice
(and `$XDG_DATA_HOME/monero/log` file for logs)

## jeffro256 | 2025-04-01T05:26:17+00:00
> Anyways, don't you think that behavior is kind of a mess?

Besides the log files being relative to the binary position, this is the standard behavior for most Unix-style commands. `cat`, `ls`, `zip`, `python`, `g++`, `make`, `nemo`, `gpg`, `sftp`, `du`, etc (I could go on) all read/write files relative to the current working directory. Usually the only programs that *don't* are ones with a GUI, where the current working directory isn't all that relevant. You may notice that the standard you linked to comes from Freedesktop. From their website:

> Freedesktop.org is a project to work on interoperability and shared base technology for free-software desktop environments for the X Window System (X11) and Wayland on Linux and other Unix-like operating systems. 

`monero-wallet-cli` doesn't use X11 nor Wayland nor any other desktop/windowing system, so applying Freedesktop's standard doesn't make sense here. Additionally, changing the behavior of `monero-wallet-cli` to write files to a new pre-determined location will likely cause confusion, and may lead to lost funds.

## me-sam9 | 2025-04-01T14:56:59+00:00
> You may notice that the standard you linked to comes from Freedesktop. From their website:
> > Freedesktop.org is a project to work on interoperability and shared base technology for free-software desktop environments for the X Window System (X11) and Wayland on Linux and other Unix-like operating systems.
> `monero-wallet-cli` doesn't use X11 nor Wayland nor any other desktop/windowing system, so applying Freedesktop's standard doesn't make sense here.

Even though the website Freedesktop website says that, it doesnt mean the XDG Base Directory Spec in particular is only applicable for programs depending on X11 nor Wayland.
Also, it says "shared base technology" for these desktop environments based on X11 or Wayland.

Anyways, many command-line programs have decided to adopt this standard.

> this is the standard behavior for most Unix-style commands. `cat`, `ls`, `zip`, `python`, `g++`, `make`, `nemo`, `gpg`, `sftp`, `du`, etc (I could go on) all read/write files relative to the current working directory.

Many of these programs don't apply to the case.
it would be ridiculous for `ls` to print the directories in some `$XDG_*/{random-dir}`, because obviously you want most of the time to print the files and directories on the `pwd`.
`cat` and `zip` take a file path as an argument
`gpp` does, indeed, support the spec with an env variable as an optional feature for historical reasons.
same thing with `python`: https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUSERBASE

Also, those programs were written before the XDG Base Directory Spec.

Many famous command-line programs written before and after the spec have decided to adopt it.

For example, `curl`, `npm`, `ffmpeg`, `nano`, `vim`, `nvim`, `git` (its credentials, analogous to wallets, are stored in `$XDG_CONFIG_HOME/git/credentials`), `pass` (same thing as `git`. Passwords, analogous to wallets, can be stored optionally in `$XDG_DATA_HOME/pass`)

(I could go on)

> Additionally, changing the behavior of `monero-wallet-cli` to write files to a new pre-determined location will likely cause confusion, and may lead to lost funds.

I agree with this, but we could make an option, or and env variable to override this default behavior.

## TommyJerryMairo | 2025-06-03T14:03:46+00:00
After reading the source code, it seems like the Monero simplewallet, which is compiled into `monero-wallet-cli`, seeks the current working directory rather than the home directory for wallets and dumps logs if no command line options are provided. To solve this elegantly, I suggest a new command-line option `wallet-dir`, similar to `monero-wallet-rpc`, which can be configured through a config file. Moreover, it would be beneficial if the Monero simplewallet could adopt a default configuration file search path that respects some standards. 

# Action History
- Created by: me-sam9 | 2025-03-31T18:33:11+00:00
