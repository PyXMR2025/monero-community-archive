---
title: 'Discussion: i8n/weblate translation'
source_url: https://github.com/monero-project/monero-docs/issues/12
author: dan-is-not-the-man
assignees: []
labels: []
created_at: '2024-08-04T00:58:27+00:00'
updated_at: '2024-08-11T22:35:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Created this to discussion to keep track of folder structure for i8n and weblate.

Current pr for folder structure layout #8 

`Please note`: folder name inside the language e.g. fr has to match the `eng` if you dont have the markdown file in the folder e.g https://github.com/dan-is-not-the-man/monero-docs/blob/i8n-test/docs/fr/accepting-monero/overview.md

# Discussion History
## nahuhh | 2024-08-04T02:27:03+00:00
It can technically be different, but for simplicity, its easier to keep non-localized filenames (same as english) 

## plowsof | 2024-08-11T22:35:21+00:00
weblate detects the proposed structure (i confirmed this on a self hosted instance), the po4a config files function correctly also so it should be ok as-is 

# Action History
- Created by: dan-is-not-the-man | 2024-08-04T00:58:27+00:00
