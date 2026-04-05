---
title: Code Comment Inconsistency
source_url: https://github.com/Cuprate/cuprate/issues/346
author: YichiZhang0613
assignees: []
labels: []
created_at: '2024-11-21T14:52:14+00:00'
updated_at: '2024-11-21T22:32:50+00:00'
type: issue
status: closed
closed_at: '2024-11-21T22:32:50+00:00'
---

# Original Description
In cuprate/storage/blockchain/src/ops/block.rs, "panic if `block.height` is not != [`chain_height`]" means code will panic if block.height == chain_height, while the code will panic if block.height != chain_height
```rust
/// # Panics
/// This function will panic if:
/// - `block.height > u32::MAX` (not normally possible)
/// - `block.height` is not != [`chain_height`]
pub fn add_block(
    block: &VerifiedBlockInformation,
    tables: &mut impl TablesMut,
) -> Result<(), RuntimeError> {
   ......
    assert_eq!(
        block.height, chain_height,
        "block.height ({}) != chain_height ({})",
        block.height, chain_height,
    );
```
In cuprate/cryptonight/src/util.rs, the comment should be `start + LEN > array.as_mut().len()`
```rust
/// # Panics
/// Panics if `start + LEN > array.as_ref().len()`.
#[inline]
pub(crate) fn subarray_mut<T: AsMut<[U]> + ?Sized, U, const LEN: usize>(
    array: &mut T,
    start: usize,
) -> &mut [U; LEN] {
    (&mut array.as_mut()[start..start + LEN])
        .try_into()
        .unwrap()
}
```

# Discussion History
## hinto-janai | 2024-11-21T21:50:01+00:00
Thanks, fixed in #347.

# Action History
- Created by: YichiZhang0613 | 2024-11-21T14:52:14+00:00
- Closed at: 2024-11-21T22:32:50+00:00
