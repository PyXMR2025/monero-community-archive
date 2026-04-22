---
title: '[beta] release ci: make PR after pushing new hashes'
source_url: https://github.com/monero-project/monero-site/issues/2624
author: plowsof
assignees: []
labels: []
created_at: '2026-04-20T14:19:34+00:00'
updated_at: '2026-04-21T17:27:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The workflow has created a PR on my branch successfully @ https://github.com/plowsof/monero-site/pull/50 , afaict we at least need the default branch set to beta, i was just sanity checking that the PR actually works

- [x] https://github.com/monero-project/monero-site/blob/35f88dae2777f35a0477f11bbd223c7dab1e2f54/.github/workflows/download-hashes.yml#L323
- [x] https://github.com/monero-project/monero-site/blob/35f88dae2777f35a0477f11bbd223c7dab1e2f54/.github/workflows/download-hashes.yml#L443
- [x] pnpm/action-setup@v4 -> 6 breaks something
    - ERR_PNPM_BROKEN_LOCKFILE  The lockfile at "/home/runner/work/monero-site/monero-site/pnpm-lock.yaml" is broken: expected a single document in the stream, but found more
- [ ] https://github.com/monero-project/monero-site/pull/2628
- [ ] https://github.com/monero-project/monero-site/pull/2617
- [ ] bump to v5
- [ ] bump lints 

# Discussion History
## plowsof | 2026-04-21T11:05:14+00:00
lint build validate , update actions warning. i had some whitespace failing and had to manually confirm what the issue was

- added patch for beta https://github.com/plowsof/monero-site/commit/a839f0af7e786c871d6a5afb6608a1b4f67fc166 
    -  pnpm/action-setup@v4 -> 6 breaks something
- added the hashes in https://github.com/plowsof/monero-site/pull/58
    - create PR skipped successfully

- merge hashes into beta running workflow https://github.com/plowsof/monero-site/actions/runs/24718587495
- PR made by action https://github.com/plowsof/monero-site/pull/59



## plowsof | 2026-04-21T15:41:26+00:00
https://github.com/pnpm/action-setup/issues/228 tldr maybe v5 works 

## plowsof | 2026-04-21T17:25:00+00:00
v5 works, no warnings, hopefully its fixed when we need it, final answer

# Action History
- Created by: plowsof | 2026-04-20T14:19:34+00:00
