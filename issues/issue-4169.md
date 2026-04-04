---
title: '[Bug] Receive - Subaddress index/label does not update when switching to account
  with no such defined subaddress'
source_url: https://github.com/monero-project/monero-gui/issues/4169
author: recursivenomad
assignees: []
labels:
- bug
created_at: '2023-05-03T20:59:50+00:00'
updated_at: '2023-05-11T20:31:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Thank you for working on this privacy-first project!

As I am organizing some of my accounts into receiving subaddresses, I have encountered unexpected behaviour - In the Receive tab, if I select a subaddress for an account, switch to a separate account which does not have a subaddress defined at that previously selected index, and then view this fewer-subaddressed-account's Receive tab, I am incorrectly shown the index of the previously selected subaddress along with "(no label)".  The address shown matches that of the Primary address on the newly selected account.

That description is a bit of "word soup", so please don't hesitate to ask if you need any clarification on what I am describing here 🙂

![monero-gui-subaddress-a](https://user-images.githubusercontent.com/128114789/236047604-42caf503-c0d0-4b64-9ddf-eff97e3efa8e.png)

![monero-gui-subaddress-b](https://user-images.githubusercontent.com/128114789/236047628-5c9a656d-e821-45b2-8e82-ddc936e64642.png)


# Discussion History
# Action History
- Created by: recursivenomad | 2023-05-03T20:59:50+00:00
