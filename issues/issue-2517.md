---
title: Please provide 'install' and 'uninstall' make targets
source_url: https://github.com/monero-project/monero/issues/2517
author: diederikdehaas
assignees: []
labels:
- proposal
created_at: '2017-09-24T01:18:21+00:00'
updated_at: '2020-12-28T07:58:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Having the option to do `make uninstall` and `make install` would be great to upgrade monero binaries when compiling from source.
The current instructions do work, but I like to keep (running) binaries and source code separated.
$PATH normally already contains `/usr/local/bin` so I guess that would also simplify instructions.


# Discussion History
## omtinez | 2017-11-23T03:38:26+00:00
`make install` already exists, but if you compile using the shared libs option then the binaries installed fail to start...

## dEBRUYNE-1 | 2018-01-08T12:38:25+00:00
+proposal

## gavriilos | 2018-09-21T23:55:51+00:00
Please fix `make install` to cater for shared libraries. As @omtinez points out, the binaries fail to start because the `.so` files are not dealt with. Right now I am using an ugly workaround. After finishing compilation I do:

```bash
sudo make install
sudo mkdir -p /usr/local/lib/monero
find . -iname "*.so*" -exec sudo cp '{}' /usr/local/lib/monero/ \;
sudo patchelf --set-rpath /usr/local/lib/monero /usr/local/bin/monerod
```
Note: you'll have to repeat the last command for every other monero executable you wish to run, such as `monero-wallet-cli`.

## telans | 2020-12-28T07:58:21+00:00
Any updates to this? I would expect CMake to install what's built. Thanks.

# Action History
- Created by: diederikdehaas | 2017-09-24T01:18:21+00:00
