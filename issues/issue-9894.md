---
title: Docker warning "FromAsCasing"
source_url: https://github.com/monero-project/monero/issues/9894
author: menaceone
assignees: []
labels: []
created_at: '2025-04-06T20:38:09+00:00'
updated_at: '2025-04-23T16:01:33+00:00'
type: issue
status: closed
closed_at: '2025-04-23T16:01:33+00:00'
---

# Original Description
The Dockerfile contains inconsitent usage of upper/lower casing for keywords.
The "as" is lower case, everything else is upper case.
This results in a Docker warning:
```
1 warning found (use docker --debug to expand):
 - FromAsCasing: 'as' and 'FROM' keywords' casing do not match (line 4)
```


Steps to reproduce the behavior:

1. clone project
2. start Docker build
3. see warning



# Discussion History
# Action History
- Created by: menaceone | 2025-04-06T20:38:09+00:00
- Closed at: 2025-04-23T16:01:33+00:00
