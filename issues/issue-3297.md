---
title: save_watch_only does not display password prompts properly
source_url: https://github.com/monero-project/monero/issues/3297
author: nasaWelder
assignees: []
labels: []
created_at: '2018-02-19T22:11:00+00:00'
updated_at: '2018-03-05T17:18:00+00:00'
type: issue
status: closed
closed_at: '2018-03-05T17:18:00+00:00'
---

# Original Description
with Monero 'Helium Hydra' (v0.11.1.0-master-d4e728c) the [wallet 9wXvk8 (no daemon)]: is covering the password prompt so it only displays after hitting "enter" again. below is a sad animation.

    [wallet 9wXvk8 (no daemon)]: save_watch_only
    ----------------------------------------------------------------------
    [wallet 9wXvk8 (no daemon)]: save_watch_only 
    [wallet 9wXvk8 (no daemon)]:
    ----------------------------------------------------------------------
    [wallet 9wXvk8 (no daemon)]: save_watch_only 
    Password for new watch-only wallet:  
    [wallet 9wXvk8 (no daemon)]:
    ----------------------------------------------------------------------
    [wallet 9wXvk8 (no daemon)]: save_watch_only
    Password for new watch-only wallet: 
    Confirm password:
    [wallet 9wXvk8 (no daemon)]:
    ----------------------------------------------------------------------
    [wallet 9wXvk8 (no daemon)]: save_watch_only
    Password for new watch-only wallet:
    Confirm password: 
    Passwords do not match! Please try again.
    [wallet 9wXvk8 (no daemon)]:
    ----------------------------------------------------------------------
    [wallet 9wXvk8 (no daemon)]: save_watch_only 
    Password for new watch-only wallet:
    Confirm password:
    Passwords do not match! Please try again.
    Password for new watch-only wallet:
    [wallet 9wXvk8 (no daemon)]:
    ----------------------------------------------------------------------
    [wallet 9wXvk8 (no daemon)]: save_watch_only
    Password for new watch-only wallet: 
    Confirm password:
    Passwords do not match! Please try again.
    Password for new watch-only wallet:
    Confirm password:
    [wallet 9wXvk8 (no daemon)]:



# Discussion History
# Action History
- Created by: nasaWelder | 2018-02-19T22:11:00+00:00
- Closed at: 2018-03-05T17:18:00+00:00
