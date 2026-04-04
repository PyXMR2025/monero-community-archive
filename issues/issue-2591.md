---
title: beta.monerodevs.org text container max-width
source_url: https://github.com/monero-project/monero-site/issues/2591
author: slrslr
assignees: []
labels: []
created_at: '2026-01-27T13:19:17+00:00'
updated_at: '2026-01-27T13:19:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
On the top in the middle of the page https://beta.monerodevs.org/ is a Monero logo element, where web browser shows (right click, Inspect element):

`<p class="lead" data-astro-cid-myoznovw=""> Private, decentralized cryptocurrency that keeps your finances confidential and secure. </p>`

max-width: 50ch;

I can modify it to:
max-width: 30ch;

it makes the text fit the circle, which looks better (it does not leak the vault - unless resized to a low resolution screens possibly)

# Discussion History
# Action History
- Created by: slrslr | 2026-01-27T13:19:17+00:00
