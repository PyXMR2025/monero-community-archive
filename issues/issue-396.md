---
title: '`cuprated` is buggy if STDIN pipe is not available'
source_url: https://github.com/Cuprate/cuprate/issues/396
author: hinto-janai
assignees: []
labels:
- C-bug
- A-binaries
created_at: '2025-03-10T20:47:09+00:00'
updated_at: '2025-03-23T00:57:30+00:00'
type: issue
status: closed
closed_at: '2025-03-23T00:57:29+00:00'
---

# Original Description
## Environment
All, [7d18098](https://github.com/Cuprate/cuprate/commit/7d18098b4ce17dea2bbd1f309bd36bcdd8f977a3).

## Bug
If STDIN is not available (e.g. docker/systemd setup), `cuprated` has buggy behavior.

## Expected behavior
Detection on when STDIN is not available.

## Steps to reproduce
1. Start `cuprated` as a normal systemd service or inside a docker container without STDIN
2. See buggy output (e.g. spamming of `help` message)

# Discussion History
## sethforprivacy | 2025-03-12T14:39:32+00:00
Note that you can workaround this and allow proper commands to be passed in the container by adding the following to a Docker Compose setup:

```yaml
    tty: true
    stdin_open: true
```

i.e.

```yaml
  cuprated:
    image: ghcr.io/hundehausen/cuprate-docker:latest
    container_name: cuprated
    restart: unless-stopped
    tty: true
    stdin_open: true
    volumes:
      - cuprated-data:/home/cuprate/.local/share/cuprate
      - ./Cuprated.toml:/home/cuprate/.config/cuprate/Cuprated.toml
    command: ["--config-file", "/home/cuprate/.config/cuprate/Cuprated.toml"]
```

# Action History
- Created by: hinto-janai | 2025-03-10T20:47:09+00:00
- Closed at: 2025-03-23T00:57:29+00:00
