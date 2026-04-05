---
title: 'Binary config '
source_url: https://github.com/Cuprate/cuprate/issues/246
author: Boog900
assignees: []
labels:
- C-discussion
- A-binaries
created_at: '2024-08-06T17:39:50+00:00'
updated_at: '2025-03-12T22:31:17+00:00'
type: issue
status: closed
closed_at: '2025-03-12T22:31:17+00:00'
---

# Original Description
## What

The binary config file and command line args. What config options we expose and how the config will be structured, one struct with the options to change or one struct madee up of all the config structs from the different components.

The first option would give us fine grain control of what users can change although it wouldn't be well structured with just one struct, the second option would be better if we want to expose everything. 


# Discussion History
## hinto-janai | 2025-03-11T23:32:00+00:00
@Boog900 can this be closed?

As of https://github.com/Cuprate/cuprate/commit/fcbf260747ff119d476b9109927e003b78773480 the second option was chosen:

> one struct madee up of all the config structs from the different components.

# Action History
- Created by: Boog900 | 2024-08-06T17:39:50+00:00
- Closed at: 2025-03-12T22:31:17+00:00
