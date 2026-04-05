---
title: Database backend hot-swapping methods
source_url: https://github.com/Cuprate/cuprate/issues/209
author: hinto-janai
assignees:
- jomuel
labels:
- A-storage
- C-discussion
created_at: '2024-07-01T16:52:54+00:00'
updated_at: '2024-07-09T14:01:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
Currently, `cuprate_database`'s backend can be changed by _compiling_ it with different feature flags, i.e.:

```bash
cargo build --features {heed,redb}
```

This issue is for discussing various methods `cuprate_database` could use to hot-swap backends at _runtime_.

## Why
This would allow end-users to choose a backend at runtime, e.g. via config or CLI.

## Method 1: `dyn Env`
The concrete object that represents the database environment is `cuprate_database::ConcreteEnv`.

This is a non-generic object; it's just a struct with some internals that switch depending on the backend feature flag.

This struct implements `trait Env`, the database environment trait, from where all other database operations can occur.

Passing around a `dyn Env` that all backends implement would solve these issues but there's a few problems:
1. `trait Env` is not [object-safe](https://doc.rust-lang.org/reference/items/traits.html#object-safety) because...
2. It uses associated types/constants because...
3. It must specify certain concrete types (e.g. the transaction type) because...
4. `Env`'s are only compatible with their own types

For example, even though `heed::RoTxn` and `redb::ReadTransaction` both implement `trait TxRo`, you cannot pass a `heed::RoTxn` to `redb` and expect it to work. This means it cannot be object safe, and that types are not compatible with each other.

Another problem is performance; `dyn` will dynamically dispatch at runtime _for each_ call, this compounds as the other traits (`TxRo`, `DatabaseRo`, etc) will probably have to be behind `dyn` as well.

### Pros
- Uses the type system
- Most maintainable

### Cons
- Slowest method
- Probably not possible without large changes

## Method 2: `enum` for each `trait`
This is the same idea `dyn`, except there is a concrete `enum` that defines all backends.

There would have to be an `enum` for each `trait` and the backend's specific type, e.g.:

```rust
enum EnvEnum {
	Heed(heed::Env),
	Redb(redb::Database),
}

enum TxRoEnum<'a> {
	Heed(heed::RoTxn<'a>),
	Redb(redb::ReadTransaction),
}

/* continue for each trait */
```

and `cuprate_database` would expose `EnvEnum` where users would have to `match` at every layer.

### Pros
- Faster than `dyn`
- Doesn't run into the object safety problem

### Cons
- Terrible maintainability
- Terrible usability

## Method 3: Branching at the high level
Another method is shifting the responsibility for "hot-swapping" upwards, i.e. instead of making `cuprate_database` hot-swap, the crates building on-top will do so.

This comes with the pro that the "branch" to determine which backend is used only needs to be done once.

The con is that _each_ crate building on-top must take on this responsibility (although, there's only 2 currently, `cuprate-blockchain` and `cuprate-txpool`).

For example, `cuprate_blockchain::service` could look something like this:
```rust
// storage/blockchain/src/service/free.rs
pub fn init(config: Config) -> Result<(DatabaseReadHandle, DatabaseWriteHandle), InitError> {
    let db = if config.backend == Backend::Heed {
        /* init heed backend */
    } else {
        /* init redb backend */
    };

    /* spawn threadpool with backend */
}

// storage/blockchain/src/service/read.rs
pub struct DatabaseReadHandle {
    // old field
    // env: Arc<ConcreteEnv>,

    // new field
    spawn_fn: fn(BCReadRequest) -> InfallibleOneshotReceiver,
}
```

- The blockchain read/write handle now only holds a function pointer that spawns some work to be done inside the `rayon` threadpool, instead of owning the `Env` itself
- Each handler function would have to take in `<E: Env>` instead of `ConcreteEnv`

### Pros
- Fastest method (one branch at `init()`)

### Problems
- Who owns the `Arc<Env>` now? `rayon` doesn't have custom storage, recreating handler logic for `rayon` threads instead of as-needed spawning means we lose (or have to re-create) `rayon` work stealing logic

# Discussion History
## Boog900 | 2024-07-06T00:22:30+00:00
> Who owns the Arc<Env> now? rayon doesn't have custom storage, recreating handler logic for rayon threads instead of as-needed spawning means we lose (or have to re-create) rayon work stealing logic

If we were instead to make the type:

```rust
// storage/blockchain/src/service/read.rs
pub struct DatabaseReadHandle {
    // old field
    // env: Arc<ConcreteEnv>,

    // new field
    spawn_fn: Box<dyn Fn(BCReadRequest) -> InfallibleOneshotReceiver>,
}
```

Then we could make the closure hold the `Arc<Env>`.


## jomuel | 2024-07-06T08:32:46+00:00
As discussed with @Boog900, I'd like to pick this up. I'd review the code today or tomorrow and then discuss further details with you in the Cuprate group chat.

## Boog900 | 2024-07-09T14:01:48+00:00
I had another idea that is pretty much an extension of method 3, but solves the issue of binary bloat.

- Remove `ConcreteEnv` and replace all usages with `<E: Env>`.
- Expose the `heed` and `redb` backends `Env` in `cuprate_database` but under feature flags that are not enabled by default.
- `cuprate_blockchain` Would also have feature flags for different DB backends, however these feature flags give you the ability to swap to that DB, it does not force its usage.
- `cuprate_blockchain` would then start the chosen backend like described by hinto, if a backend is chosen that hasn't been enabled by the feature flags the `init` function should panic.
 

# Action History
- Created by: hinto-janai | 2024-07-01T16:52:54+00:00
