---
title: 'Logging '
source_url: https://github.com/Cuprate/cuprate/issues/163
author: Boog900
assignees: []
labels:
- C-discussion
created_at: '2024-06-13T21:16:36+00:00'
updated_at: '2024-06-16T19:55:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What

Currently we using tracing for logging, this issue is to start formalizing what should be logged, and at what level/ target. 

## Why

Currently logging isn't very structured and it's hard to follow, in certain places it's too verbose and in others it's nonexistent. 

---

### Should we change the `target`?

From the tracing docs:

> A [target](https://docs.rs/tracing/latest/tracing/struct.Metadata.html#method.target), a string that categorizes part of the system where the span or event occurred. The tracing macros default to using the module path where the span or event originated as the target, but it may be overridden.

IMO the module path is not something that needs to be exposed to the end user trying to filter logs, we could probably create better, more descriptive targets.

### What should be logged and at what level?

Currently I have just been just been logging at whatever level I think is best at that time, which means the vast majority of logs are at the `debug` level. 

Although `What should be logged and at what level` is dependent on the specific subsection and it would be pretty difficulty to try make a scheme that covers everything, we could make rough guidelines.

### When should a `Span` be created and at what level?

### Where should we log to?

This is probably an answered question (terminal with an option to log to a file) but thought I would include it here anyway. 





# Discussion History
## hinto-janai | 2024-06-16T19:42:11+00:00
Another open question:

### API stability
Log output is (for better or worse) an API for users (e.g. `grep`).

- Should we stabilize certain lines? How will this be enforced?
- Should we ignore this and label output forever unstable?
- Somewhere in the middle?

## SyntheticBird45 | 2024-06-16T19:55:41+00:00
Imo: Anything that is of `Level::INFO` and `Level::WARNING` should be stable. The rest is unstable forever.

# Action History
- Created by: Boog900 | 2024-06-13T21:16:36+00:00
