---
title: Should we be using expect()?
source_url: https://github.com/Cuprate/cuprate/issues/27
author: dan-da
assignees: []
labels:
- C-discussion
created_at: '2023-09-05T06:25:29+00:00'
updated_at: '2024-05-27T00:58:17+00:00'
type: issue
status: closed
closed_at: '2023-10-06T19:51:41+00:00'
---

# Original Description
I'm opening this issue to start a discussion about writing functions that can panic.  I would hope to adopt a no-panic policy, for a more robust codebase.

Commentary:

In my projects I generally avoid use of unwrap/expect -- especially for any code that might possibly be used by other projects... eg anything that might eventually be published on crates.io.

While I might judge it is ok to unexpectedly terminate *my* application, I should not make that choice for other developers.  Instead, its better to define errors with *thiserror* and return them.   The sooner this is done the better, as otherwise a huge pile of code can be written that depends on an API that does not return a Result/Error when it should and changing the huge pile above can be problematic.

Observation:

This project is using expect() in some public fn, such as:

https://github.com/Cuprate/cuprate/blob/59e7e0b4e8daf700b47a6be20a2e3c8a8c68bd74/common/src/pruning.rs#L142

Question:

Is it intended that cuprate, or any sub-components in this repo will be published as a crate for other developers to use?     Or is it intended as end-user application/server?

In both cases I would recommend to get rid of unwrap/expect() wherever possible and instead return Result.   Even if cuprate code is not intended to be used as a library, probably someone will eventually extract some of it for that purpose.    Further, even as a standalone executable, it can be more robust if it recovers from and logs errors rather than panic exiting.

For discussion:

What is, or should be, the cuprate policy with regards to writing and using functions that can panic?

Would we consider:
a) refactoring to get rid of all existing expect(), unwrap(), panic()
b) adding clippy checks to deny expect, unwrap, panic in new code?

btw, I am willing to work on pull-requests for both a and b.

# Discussion History
## Boog900 | 2023-09-05T17:41:38+00:00
Yes parts of Cuprate will be usable in other crates.

Currently I have been using panics in 3 main places: obvious programmer mistakes, unrecoverable bugs and when I know the panic won't be reached.

what I mean by `obvious programmer mistakes` is mistakes that a programmer can only make on purpose, like responding to a request with completely wrong data, for example:

https://github.com/Cuprate/cuprate/blob/42548f733da7594fbde5b382ad12a3541a8c95bb/consensus/src/hardforks.rs#L220-L227

If the database responds with a block even though we requested the ChainHeight this will panic.

`unrecoverable bugs` will only effect Cuprate specific sections.

`when I know the panic won't be reached` This is why I used a panic in the section you gave as an example.


Altough I agree we should try limit the amount of panics we use, I do believe they have there place so don't want to ban them completely. Maybe a ban of `unwrap` would be ok, forcing people to explain why they are using a panic in a `expect` instead
 

## kayabaNerve | 2023-09-07T13:23:57+00:00
Panics should only be used on invariants.

A database responding with a non-ChainHeight to a ChainHeight is an invariant.

An invalid block having already been marked valid, which could be an unrecoverable bug (no example provided from boog), would be an invariant.

```rs
            if block_height + CRYPTONOTE_PRUNING_TIP_BLOCKS >= blockchain_height {
                // If we are within `CRYPTONOTE_PRUNING_TIP_BLOCKS` of the chain we should
                // not prune blocks.
                return Ok(block_height);
            }
            let seed_log_stripes = self
                .get_log_stripes()
                .unwrap_or(CRYPTONOTE_PRUNING_LOG_STRIPES);
            let block_pruning_stripe = get_block_pruning_stripe(block_height, blockchain_height, seed_log_stripes)
                .expect("We just checked if `block_height + CRYPTONOTE_PRUNING_TIP_BLOCKS >= blockchain_height`");
```

Not having a pruning stripe, when there should always be a pruning stripe for blocks with insufficient depth, is an invariant (though this should be clearly documented).

Obscuring invariants into Results sounds prone to unsafe behavior. Panicking is sane.

# Action History
- Created by: dan-da | 2023-09-05T06:25:29+00:00
- Closed at: 2023-10-06T19:51:41+00:00
