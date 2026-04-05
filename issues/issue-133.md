---
title: FCMP++ fork activation logs from stressnet block 2847330
source_url: https://github.com/seraphis-migration/monero/issues/133
author: runatyr1
assignees: []
labels: []
created_at: '2025-10-03T19:42:23+00:00'
updated_at: '2025-10-04T17:05:33+00:00'
type: issue
status: closed
closed_at: '2025-10-04T17:05:33+00:00'
---

# Original Description
Informational issue, logs collected during FCMP++ fork in release [v0.19.0.0-alpha.1](https://github.com/seraphis-migration/monero/releases/tag/v0.19.0.0-alpha.1) - i thought it might be useful for the devs.

** Findings **
  - Fork block: 2847330 (hash: 05ae51dbc1ed7c5b8b4471f156205f8522213c5a9070e4ca740e33321bd80e5a)
  - Pre-computation started at block 2847321 (9 blocks ahead)
  - Log message: "Growing tree usable once block 2847330 is in the chain"
  - Curve tree operations completed successfully
  - Log growth: ~2.26 MB/min at trace level

  - [Link of log file with tracing](http://94.130.18.159:30080/share/kE2KP7L1)

** Check findings in the log **
  ```bash
  # Pre-computation phase (block 2847321, preparing for 2847330)
  grep -a -n -A 10 "Growing tree usable once block 2847330" monerod.log

  # Fork block received (block 2847330 arrival)
  grep --color -a -n -A 10 "NOTIFY_NEW_FLUFFY_BLOCK.*height 2847330"

  # Fork block successfully added
   grep --color -a -n -A 10 "HEIGHT 2847330, difficulty" monerod.log

  # Curve tree metadata saved for fork block
  grep --color -a -n -A 10 "Saving tree meta for block idx 2847330" monerod.log
  ```

** systemd service config **
  ```bash
[Unit]
Description=Monero FCMP++ Stressnet Node
After=network.target

[Service]
User=user1
Group=user1
Type=forking
ExecStart=/binaries/monerod-fcmp-stressnet \
    --detach \
    --testnet \
    --prune-blockchain \
    --data-dir=/monero_stressnet \
    --log-level=4 \
    --log-file=/monero_stressnet/monerod.log \
    --max-log-file-size=20485760000 #20gb \
    --rpc-bind-ip=0.0.0.0 \
    --rpc-bind-port=28081 \
    --p2p-bind-ip=0.0.0.0 \
    --p2p-bind-port=28080 \
    --confirm-external-bind \
    --limit-rate-up=5000 \
    --limit-rate-down=15000 \
    --pidfile=/monero_stressnet/monerod.pid \
    --zmq-rpc-bind-ip=0.0.0.0 \
    --zmq-rpc-bind-port=28083 \
    --zmq-pub=tcp://127.0.0.1:28084

# Basic process management
Restart=always
RestartSec=10

# Only essential security
NoNewPrivileges=true

# Resource limits
LimitNOFILE=65536

# Logging
StandardOutput=journal
StandardError=journal
SyslogIdentifier=monerod-fcmp-stressnet

[Install]
WantedBy=multi-user.target
```

# Discussion History
## j-berman | 2025-10-04T17:05:33+00:00
Thanks

# Action History
- Created by: runatyr1 | 2025-10-03T19:42:23+00:00
- Closed at: 2025-10-04T17:05:33+00:00
