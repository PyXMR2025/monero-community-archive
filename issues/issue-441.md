---
title: Print configuration before starting
source_url: https://github.com/Cuprate/cuprate/issues/441
author: hinto-janai
assignees: []
labels:
- C-request
- E-easy
- E-help-wanted
created_at: '2025-04-11T13:30:44+00:00'
updated_at: '2025-05-08T12:53:31+00:00'
type: issue
status: closed
closed_at: '2025-05-08T12:53:31+00:00'
---

# Original Description
## Feature
`monerod` logs useful info when initializing things, e.g. P2P port, RPC port, etc.

`cuprated` could do all of this and more if it logged its configuration:

https://github.com/Cuprate/cuprate/blob/eceb74f183c6124931dbe10491db259f60272f3f/binaries/cuprated/src/config.rs#L105-L151

with something like `info!("Configuration: {config}")` before starting, somewhere after the logging init:

https://github.com/Cuprate/cuprate/blob/eceb74f183c6124931dbe10491db259f60272f3f/binaries/cuprated/src/main.rs#L57-L63


# Discussion History
# Action History
- Created by: hinto-janai | 2025-04-11T13:30:44+00:00
- Closed at: 2025-05-08T12:53:31+00:00
