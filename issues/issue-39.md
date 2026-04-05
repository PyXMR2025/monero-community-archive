---
title: Reproducible builds
source_url: https://github.com/Cuprate/cuprate/issues/39
author: hinto-janai
assignees: []
labels:
- C-discussion
- C-feature
created_at: '2023-12-04T21:31:16+00:00'
updated_at: '2025-05-13T18:11:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
This is a discussion on reproducible builds for Cuprate.

Similar to https://github.com/monero-project/gitian.sigs, this would allow anyone to deterministically build Cuprate binaries.

This process would also be used for the public release binaries, as Monero does.

## How
A few options:

### `gitian`
The [gitian process](https://github.com/monero-project/monero/blob/master/contrib/gitian/README.md) similar to Monero's.

### Docker with deterministic environment
See https://github.com/serai-dex/serai/blob/develop/orchestration/runtime/Dockerfile.

### `guix`
See https://github.com/Cuprate/cuprate/issues/470.

# Discussion History
## kayabaNerve | 2023-12-16T22:37:32+00:00
https://github.com/serai-dex/serai/blob/develop/orchestration/runtime/Dockerfile is a direct Dockerfile, no gitian needed, to create a deterministic environment.

An additional note I have to contribute is host architecture will impact the build process.

## hinto-janai | 2025-05-13T02:20:29+00:00
Closing in favor of https://github.com/Cuprate/cuprate/issues/470.

## kayabaNerve | 2025-05-13T13:23:35+00:00
Shouldn't this remain open until reproducible builds exist?

I understand the preference for achieving reproducible builds via bootstrappable builds. Bootstrappable builds alone doesn't guarantee reproducibility (even if guix specifically may), and this issue isn't completed.

I think simply citing the latest relevant issue would be better.

# Action History
- Created by: hinto-janai | 2023-12-04T21:31:16+00:00
