---
title: System dependencies required for building Cuprate
source_url: https://github.com/Cuprate/cuprate/issues/172
author: hinto-janai
assignees: []
labels:
- C-discussion
created_at: '2024-06-19T01:12:51+00:00'
updated_at: '2025-08-14T00:23:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
This issue will track the system dependencies required for fresh systems to compile `cuprated`.

Eventually will be added to `README.md` and/or user book.

## All
- `git`
- Rust toolchain
- Compiler
- Linker

## Windows (MSVC)
- `cmake` (randomx-rs build script)

## macOS
TODO

## Linux
### Debian/Ubuntu
- `build-essentials`
- `cmake` (randomx-rs build script)

### Arch
- `base-devel`
- `cmake` (randomx-rs build script)

### Fedora
TODO

### Gentoo
TODO

### Alpine
TODO

## FreeBSD
TODO

# Discussion History
## sethforprivacy | 2025-03-02T12:22:30+00:00
It would also be good to have specific depdendencies for Alpine Linux and similar distros to simplify minimal Docker image builds.

## SyntheticBird45 | 2025-03-02T15:39:30+00:00
> It would also be good to have specific depdendencies for Alpine Linux and similar distros to simplify minimal Docker image builds.

sure, im using alpine myself.

## denmeh | 2025-08-14T00:23:33+00:00
On Fedora, I can successfully build with:

- `sudo dnf install pkgconf perl-FindBin perl-IPC-Cmd openssl-devel` — required for OpenSSL (based on [openssl crate documentation](https://docs.rs/openssl/latest/openssl/))
- `cmake`


# Action History
- Created by: hinto-janai | 2024-06-19T01:12:51+00:00
