---
title: Standardize file locations on Linux
source_url: https://github.com/monero-project/monero-gui/issues/2291
author: sanderfoobar
assignees: []
labels: []
created_at: '2019-07-16T17:18:35+00:00'
updated_at: '2022-12-19T06:43:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
GUI currently uses the following files and directories:

- Wallets are written to `~/Monero`
- Blockchain is written to `~/.bitmonero`
- GUI log is written to `~/.bitmonero/monero-wallet-gui.log`
- Configuration is written to `~/.config/monero-project/monero-core.conf`
- Desktop entry is written to `~/.local/share/applications/monero-gui.desktop`
- Cache is written to `~/.local/share/Trash/files/` and `~/.local/share/Trash/info/`

[Quoting rnhmjoj](https://github.com/monero-project/monero-gui/pull/2272#issuecomment-511321976)

> The idea of the XDG [spec](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html) is to allow the separation of configuration files, user generate data and cache files. The main advantage is that it makes the locations configurable; also it's easier backup by simply selecting the directory (like $XDG_DATA_HOME/monero), without worrying about excluding temporary files.

> I get the point about fragmentation but monero-gui is already using XDG_CACHE_HOME for the qml cache, and the log file certainly belong to this category. An "uninstall" procedure could simply be to delete:
> $XDG_{CACHE,DATA,CONFIG}_HOME/monero-project

This issue proposes to discuss that GUI related files could go into `$XDG_{CACHE,DATA,CONFIG}_HOME` (except for `~/.bitmonero`) so that it follows [the XDG spec](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).

# Discussion History
## sanderfoobar | 2019-07-16T17:33:04+00:00
I think an exception can also be made for the wallet directory, which currently is `~/Monero/wallets`. This would become `/home/dsc/.local/share/Monero/wallets` but I think that `~/Documents/Monero` is more appropriate.

@rnhmjoj thoughts?

## rnhmjoj | 2019-07-16T19:04:10+00:00
> I think an exception can also be made for the wallet directory

I agree, since users more often access the wallet it's better to keep the directory visible, so ~/Monero is fine in my opinion. Besides monero let you choose where to save the wallet at the start.

On my computer the cache and configuration files are
```
$XDG_CONFIG_HOME/monero-project/monero-core
$XDG_CACHE_HOME/monero-project/monero-core
```
so they seems already compliant. I would simplify `monero-project/monero-core` to just `monero`, which I think is a bit ugly. I suspect this is added by Qt when setting the company/project name.
The tricky part will be changing .bitmonero because it's also used by the monero daemon. 
Summing it up, I propose something like this:
```
$XDG_CONFIG_HOME/monero/ -> configuration files
$XDG_CACHE_HOME/monero/ -> qml cache, daemon and gui logs
$XDG_DATA_HOME/monero/ -> blockchain data
$HOME/Monero -> wallets
```

Anyway, if you intend to change the locations I'd suggest to implement a check for the old locations (like .bitmonero) and, if needed, move the content to the new location. This should make the transition painless. Also, thank you for considering the idea.


## colemickens | 2020-01-20T08:33:45+00:00
Maybe the wallet location could also be configurable with a line in one of the configuration files, as well.

## oxalica | 2021-05-20T11:30:58+00:00
GUI seems also leave `~/.shared-ringdb` in home. It should also be moved to `$XDG_DATA_HOME` or `$XDG_CACHE_HOME`.

## xeruf | 2021-10-26T07:15:05+00:00
That might belong into `XDG_STATE_HOME` now that that is out

## xeruf | 2021-10-26T07:19:14+00:00
`~/Documents/Monero` is definitely not an appropriate path for anything. I interact with many programs in `$XDG_DATA_HOME` regularly without issues.
At least use `XDG_DOCUMENTS_DIR` (obtainable via `xdg-user-dir DOCUMENTS`) as prefix then.

## tiritto | 2022-12-19T06:43:49+00:00
As of version 0.18.1.2, this is still an issue.

- `~/.bitmonero` is still created and `bitmonero.log` file is created within that folder, even despite monero-gui being started with `--log-file=/dev/null` launch option. I've decided to just discard logs as it's more convenient for me than doing dirty workarounds to apply XDG variables within monero-gui's .desktop file. Note that it's a different file from `monero-wallet-gui.log` that is no longer created at all after applying launch options.

- `~/.shared-ringdb` is still being created with seemingly no way to change it's location.

# Action History
- Created by: sanderfoobar | 2019-07-16T17:18:35+00:00
