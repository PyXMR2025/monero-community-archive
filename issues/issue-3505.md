---
title: 'GPU #0 COMPUTE ERROR   solution'
source_url: https://github.com/xmrig/xmrig/issues/3505
author: heimawsw
assignees: []
labels: []
created_at: '2024-07-02T04:02:48+00:00'
updated_at: '2025-06-28T10:32:05+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:32:05+00:00'
---

# Original Description
If you encounter a GPU #0 COMPUTE ERROR problem, you can change the config.json configuration to resolve it.


"rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 216,
                "bfactor": -1,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],


Significant modification：
"bfactor": -1,

After testing, it can run normally for a long time.




# Discussion History
# Action History
- Created by: heimawsw | 2024-07-02T04:02:48+00:00
- Closed at: 2025-06-28T10:32:05+00:00
