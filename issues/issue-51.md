---
title: Investigating usage of minitrace instead of tokio-tracing
source_url: https://github.com/Cuprate/cuprate/issues/51
author: SyntheticBird45
assignees: []
labels:
- C-discussion
- C-optimization
created_at: '2024-02-04T22:02:04+00:00'
updated_at: '2024-05-27T00:56:33+00:00'
type: issue
status: closed
closed_at: '2024-02-06T20:49:06+00:00'
---

# Original Description
Recently a library just made the show on r/rust, called `minitrace`: https://reddit.com/r/rust/comments/1abbyc9/announcing_minitrace_06_a_modern_alternative_of/
https://github.com/tikv/minitrace-rust
https://crates.io/crates/minitrace

It is marketed as extremely fast and provide the following benchmark: 
https://github.com/tikv/minitrace-rust/blob/master/etc/img/benchmark-arch.svg

The sensible difference with tokio-tracing is that there are no Span level, only a global level. But in the way that we use tracing it shouldn't change something. It is not a drop-in-replacement.

# Discussion History
## SyntheticBird45 | 2024-02-06T20:49:00+00:00
This library can't be used for logging as we intend. It is intended for structured tracing that get consumed by other, online collectors such as Jeager or OpenTelemetry. It is indeed far more performant but we should first rely on working logging infrastructure first

# Action History
- Created by: SyntheticBird45 | 2024-02-04T22:02:04+00:00
- Closed at: 2024-02-06T20:49:06+00:00
