---
title: How to import transaction history partially?
source_url: https://github.com/monero-project/monero-gui/issues/4400
author: pacifism628
assignees: []
labels: []
created_at: '2025-01-14T22:46:19+00:00'
updated_at: '2025-02-07T01:55:13+00:00'
type: issue
status: closed
closed_at: '2025-02-07T01:55:13+00:00'
---

# Original Description
Monero GUI 18.3.4 on Windows 11 and Ubuntu 22.04.
Usually I run Monero GUI on my Windows PC, but I switched to Ubuntu for a couple of months, using the same wallet. Now I moved back to Windows, synchronized the wallet (remote node) and realized that those transactions placed on Ubuntu are not fully visible on Windows, e.g. `Unknown recipient` and no `TX key`. As I understand, that's not a bug, but an intentional behavior.
So, how to import transaction history from Ubuntu to Windows? Do I need to do something in CLI or what?

# Discussion History
## plowsof | 2025-01-14T23:37:54+00:00
you will need to bring the wallet cache file over (which contains that info). wallet_name.keys (the keys file, naturally) and wallet_name (the cache) should be in your wallet file folder which on windows is Documents\Monero\Wallets. Paste the cache to your ubuntu machine inside the /home/username/Monero/wallets 

## pacifism628 | 2025-01-15T01:45:35+00:00
> you will need to bring the wallet cache file over (which contains that info). wallet_name.keys (the keys file, naturally) and wallet_name (the cache) should be in your wallet file folder which on windows is Documents\Monero\Wallets. Paste the cache to your ubuntu machine inside the /home/username/Monero/wallets

Thanks for the response. I know there is an option just to send the files from `wallets` directory. However, on my Ubuntu there are also some transactions with `Unknown recipient` and no `TX key`, so I'm looking for a method to merge the files from the both PCs in a way that all the cached transactions will be fully visible. Any options to manually edit those binary files?

## selsta | 2025-01-15T16:36:31+00:00
Manually merging them together is not possible, or at least there is no tool for it.

# Action History
- Created by: pacifism628 | 2025-01-14T22:46:19+00:00
- Closed at: 2025-02-07T01:55:13+00:00
