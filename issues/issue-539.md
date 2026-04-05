---
title: Make the database service have a Tx interface
source_url: https://github.com/Cuprate/cuprate/issues/539
author: Boog900
assignees: []
labels:
- A-storage
- C-proposal
created_at: '2025-08-28T15:37:57+00:00'
updated_at: '2025-08-28T15:37:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

## What
Currently the database services have a interface that allows a single request at a time, creating a db tx each time it is called. Instead you should first need to call a function to start a DB tx before doing any calls.

## Why
Makes keeping the DB state consistent easier, often multiple requests are needed and we need to make sure each request stays in sync. 

## Where
the database service and and users.




# Discussion History
# Action History
- Created by: Boog900 | 2025-08-28T15:37:57+00:00
