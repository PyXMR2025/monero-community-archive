---
title: 'sh: 0: Can''t open autogen.sh'
source_url: https://github.com/monero-project/monero/issues/8128
author: BlueCute
assignees: []
labels: []
created_at: '2022-01-03T04:35:16+00:00'
updated_at: '2022-01-03T05:59:31+00:00'
type: issue
status: closed
closed_at: '2022-01-03T05:58:37+00:00'
---

# Original Description
Hello,
i am trying to insall Monero on Multipool.


manually building wallets
source /etc/functions.sh
source /etc/multipool.conf
source $HOME/multipool/daemon_builder/.my.cnf
cd $STORAGE_ROOT/daemon_builder/temp_coin_builds
git clone GIT LINK
cd DIR
sh autogen.sh

After sh autogen.sh i got this error: sh: 0: Can't open autogen.sh
Just there is not such file..

Does the same with daemonbuilder too.
Any help will be great.

# Discussion History
## BlueCute | 2022-01-03T05:59:31+00:00
I understand that is not supported by that multipool.
I apologize for this

# Action History
- Created by: BlueCute | 2022-01-03T04:35:16+00:00
- Closed at: 2022-01-03T05:58:37+00:00
