---
title: Code Comment Inconsistency
source_url: https://github.com/Cuprate/cuprate/issues/381
author: YichiZhang0613
assignees: []
labels: []
created_at: '2025-02-09T07:47:06+00:00'
updated_at: '2025-02-27T15:19:14+00:00'
type: issue
status: closed
closed_at: '2025-02-27T15:19:14+00:00'
---

# Original Description
In cuprate-main/net/levin/src/message.rs, the comment indicates that the code will panic if  fragment_size <= 2 * HEADER_SIZE.
While the code panics if fragment_size * 2 < HEADER_SIZE
```rust
/// `fragment_size` must be more than 2 * [`HEADER_SIZE`] otherwise this will panic.
pub fn make_fragmented_messages<T: LevinBody>(
    protocol: &Protocol,
    fragment_size: usize,
    message: T,
) -> Result<Vec<Bucket<T::Command>>, BucketError> {
    assert!(
        fragment_size * 2 >= HEADER_SIZE,
        "Fragment size: {fragment_size}, is too small, must be at least {}",
        2 * HEADER_SIZE
    );
```

# Discussion History
# Action History
- Created by: YichiZhang0613 | 2025-02-09T07:47:06+00:00
- Closed at: 2025-02-27T15:19:14+00:00
