---
title: '`cuprated --dry-run`'
source_url: https://github.com/Cuprate/cuprate/issues/442
author: hinto-janai
assignees: []
labels:
- C-request
- E-help-wanted
created_at: '2025-04-11T14:11:01+00:00'
updated_at: '2025-11-25T15:03:46+00:00'
type: issue
status: closed
closed_at: '2025-11-25T15:03:46+00:00'
---

# Original Description
## Feature
Add a `cuprated --dry-run` flag.

```
./cuprated --help

--dry-run        Test the configuration file and exit.
                 `cuprated` will check the configuration for
                 correct syntax and valid values, then print
                 the configuration and exit successfully without
                 starting. If any errors occur, they will be 
                 logged and `cuprated` and exit with an error code.
```

## How
Things that are tested:
- `Config` deserialization
- PATH permissions
- If ports can be binded to

Things that could be tested and aren't hard errors:
- If values are sane (e.g. `max_txpool_byte_size` is unrealistically large, system only has 10 threads but a value like 500 is present, etc) 
- Remaining disk space is too low
- Unrestricted RPC binded to `0.0.0.0`


## Why
https://en.wikipedia.org/wiki/Dry_run_(testing)

Useful for programs that have lots of side-effects after starting, e.g.:

- [`nginx -T`](https://nginx.org/en/docs/switches.html)
- [`cargo add --dry-run`](https://doc.rust-lang.org/cargo/commands/cargo-add.html#dependency-options)
- [`cargo install --dry-run`](https://doc.rust-lang.org/cargo/commands/cargo-update.html#update-options)
- [`cargo upload --dry-run`](https://doc.rust-lang.org/cargo/commands/cargo-publish.html#publish-options)
- [`docker compose --dry-run`](https://docs.docker.com/reference/cli/docker/compose/#options)

# Discussion History
# Action History
- Created by: hinto-janai | 2025-04-11T14:11:01+00:00
- Closed at: 2025-11-25T15:03:46+00:00
