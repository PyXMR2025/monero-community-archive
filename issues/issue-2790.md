---
title: How to change the block chain file path to (default)
source_url: https://github.com/monero-project/monero-gui/issues/2790
author: ann61wang
assignees: []
labels: []
created_at: '2020-03-02T07:40:03+00:00'
updated_at: '2020-03-27T15:17:23+00:00'
type: issue
status: closed
closed_at: '2020-03-27T15:17:23+00:00'
---

# Original Description
When I change the block link path from the default to another path, I always get an error: the connected background process is not compatible with the current GUI wallet, and there is no select button when I want to change back to the default path.

Since I changed the default path, my background process has always been the following（It doesn't matter whether you're using simple mode or advanced mode）:

16382 ??         0:00.91 /Users/name/Downloads/monero-gui-v0.15.0.2/monero-wallet-gui.app/Contents/MacOS/monerod --detach --data-dir /Users/name/.bitmonero --bootstrap-daemon-address auto --no-sync --check-updates disabled --max-concurrency 4

My GUI wallet is the MAC version, so the default path is in the $Home/.bitmonero folder, but even if I manually set this path, it didn't solve the problem I'd been having. And even if I were to recreate a new wallet, it wouldn't help.

When creating a new wallet, the block link path shows the path I set instead of the word (default), and the background process is the same as above. How can I solve this problem?




# Discussion History
# Action History
- Created by: ann61wang | 2020-03-02T07:40:03+00:00
- Closed at: 2020-03-27T15:17:23+00:00
