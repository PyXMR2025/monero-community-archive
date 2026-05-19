---
title: Tracking Issue for Cuprate as a library
source_url: https://github.com/Cuprate/cuprate/issues/616
author: redsh4de
assignees: []
labels:
- C-tracking-issue
created_at: '2026-05-18T10:05:42+00:00'
updated_at: '2026-05-19T06:59:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What
This is a tracking issue for turning cuprated into a embeddable library with error propagation.

### Steps
- [x] #592 
- [ ] Error propagation and panic removal
    - #585 
    - #586 
    - #590 
- [ ] Clean up `launch()` by adding subsystem `start()` steps in each module
- [ ] Add node event streaming

### Related
- #516 
- #554 

# Discussion History
# Action History
- Created by: redsh4de | 2026-05-18T10:05:42+00:00
