---
title: '[Feature request] Initial sync throttle'
source_url: https://github.com/monero-project/monero-gui/issues/1783
author: Gingeropolous
assignees: []
labels:
- feature
created_at: '2018-12-05T15:56:38+00:00'
updated_at: '2019-09-01T11:36:30+00:00'
type: issue
status: closed
closed_at: '2019-09-01T11:36:30+00:00'
---

# Original Description
Monerod can really hog up resources during the initial sync. 

The CLI has all the flags necessary to do a little throttling. Perhaps there could be a checkbox during the getting started walkthrough screens that has these options, and it would autopopulate the daemon flag thing in that settings area.

Fast Sync - this would add no flags.
Medium Sync - this would add --limit-rate 1000 to the daemon flags. 1 MB/s is probably enough to throttle everything downstream to some extent. 
Slow Sync - this would add --limit-rate 500 and --max-concurrency 1. This would throttle the bandwidth and the CPU usage.

These could all be combined with the bootstrap-daemon flag as well to provide immediate functionality. 

# Discussion History
## sanderfoobar | 2019-02-08T14:25:27+00:00
+feature

## selsta | 2019-09-01T01:36:18+00:00
IMO quite a niche feature that adds unnecessary extra complexity. We already add the `--max-concurrency` flag so that the daemon only uses half of the threads available.

See here: https://github.com/monero-project/monero-gui/pull/1920

## Gingeropolous | 2019-09-01T11:36:30+00:00
sure.

# Action History
- Created by: Gingeropolous | 2018-12-05T15:56:38+00:00
- Closed at: 2019-09-01T11:36:30+00:00
