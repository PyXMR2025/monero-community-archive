---
title: To `disk`, or not to `disk`
source_url: https://github.com/Cuprate/cuprate/issues/48
author: hinto-janai
assignees: []
labels:
- C-discussion
created_at: '2023-12-19T19:19:04+00:00'
updated_at: '2024-05-27T00:56:51+00:00'
type: issue
status: closed
closed_at: '2024-02-18T16:40:40+00:00'
---

# Original Description
## What
How will Cuprate associate (de)serializable data with locations on disk?

If https://github.com/Cuprate/cuprate/issues/46 is the "where", then this is the "how".

Concrete example: `cuprate` wants to read/write `cuprate.toml` to/from disk, how do we obtain that PATH?

Options, from least-invasive to most-invasive:
- Ad-hoc PATH creation where needed, [Monero-style](https://github.com/monero-project/monero/blob/ac02af92867590ca80b2779a7bbeafa99ff94dcb/src/p2p/net_node.inl#L136)
- [`dirs`](https://docs.rs/dirs) combined with `const` PATH end nodes (`dirs::config_dir() += "cuprate.toml"`), maybe saved into a `OnceLock` for easy global referencing
- [`disk`](https://docs.rs/disk)

## To [`disk`](https://docs.rs/disk)...
The library `disk` allows for associations of data types (`struct`, `enum`) with locations on disk (`~/.config/cuprate/cuprate.toml`).

It has (de)serialization as well, so a `struct` can be directly created/saved from disk with:
```rust
// create a `Config` instance from disk.
let config: Config = Config::from_file()?;

// write it to disk.
config.save()?;
```
This works because it "knows" where to look, because we define it:
```rust
// This maps to:
//
// | OS      | PATH                                                            |
// |---------|-----------------------------------------------------------------|
// | Windows | `C:\Users\Alice\AppData\Roaming\Cuprate\cuprate.toml`           |
// | macOS   | `/Users/Alice/Library/Application Support/Cuprate/cuprate.toml` |
// | Linux   | `/home/alice/.config/cuprate/cuprate.toml`                      |
//
//  format  struct  OS location  project folder    sub-dirs  file name (.toml is implied)
//    v     v       v                   v          v         v     
disk::toml!(Config, disk::Dir::Config, "Cuprate", "", "cuprate");
#[derive(Serialize,Deserialize)]
struct Config { /* ... */ }
```
This library "works" but is rough around the edges as seen with the `macro_rules!()` instead of a proper `#[derive()]`.

The main question is if this path should even be taken, as opposed to (de)serializing ourselves and using `std::fs::write(path, &data)` to every file we'd like to make on a per-case basis (possibly more reasonable if we only need to manage a few). Off the top of my head, there is:
- Config file
- Crash file
- Documentation location
- Cache files
- Log files
- Certificate/key files
- Database
- Misc state, e.g `p2pstate.bin`

The benefit of this library is:
- Everything is defined right on-top of the data in a single declarative line
- Many file formats supported (`bincode`, `toml`, `json`, etc)
- (De)serialization is abstracted, no `serde_json` or `toml_edit`, just `save()` and `from_file()`
- Bad input safety guards (compile-time error on bad input, `panic!()` on dangerous operations at runtime)
- OS differences are abstracted away
- Many other [nice to haves](https://docs.rs/disk/latest/disk/trait.Toml.html#provided-methods)

Making `disk` "production-ready" would take some time.

## ...or not to [`disk`](https://docs.rs/disk)
Immediate counter-argument:
- This is an overly complicated abstraction (aka, way too much "magic")

`disk` is a [macro-heavy mess](https://docs.rs/disk/latest/src/disk/common.rs.html#1045) internally, and will be more so when it moves to `#[proc_macro]`. If I were to get hit by a bus, or leave Cuprate, maintenance of `disk` would be very painful. Compile errors (from editing internals, not user-facing) from one of these macros causes walls of unreadable text.

I don't want Cuprate to be dependent on any sole person, so I'm slightly on the side of just doing all of this manually, i.e:
- `dirs` +
- `const PATH` +
- `serde_json`/`toml_edit`/whatever_format +
- `std::fs::read/write`
- for each file, at each call-site

# Discussion History
## Boog900 | 2023-12-24T18:25:39+00:00
I agree, I think Cuprate should go the manual route.

Also can `disk` even handle dynamic paths, I couldn't see anyway to do this, if it can't and we went with `disk` it would mean users wouldn't be able to specify custom paths

## hinto-janai | 2023-12-25T00:19:12+00:00
https://docs.rs/disk/latest/disk/trait.Toml.html#method.from_path

```rust
// Uses pre-defined location.
let config: Config = Config::from_file()?;

// Uses arbitrary path.
let config: Config = Config::from_path("/any/path")?;
```

## SyntheticBird45 | 2024-02-02T19:08:11+00:00
I agree with @Boog900 we should go manual route since it would give us fine control on when and how we write on disk. No need to add more dependencies for something that don't require so much work

## hinto-janai | 2024-02-18T16:40:40+00:00
Going the manual route.

I will find an opportunity to re-write `disk` someday...

# Action History
- Created by: hinto-janai | 2023-12-19T19:19:04+00:00
- Closed at: 2024-02-18T16:40:40+00:00
