---
title: fs::test::path_sanity_check fails
source_url: https://github.com/Cuprate/cuprate/issues/610
author: An-anonymous-coder
assignees: []
labels:
- C-bug
created_at: '2026-05-07T21:10:27+00:00'
updated_at: '2026-05-07T21:10:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Here is the setup I have:
[VSCodium](https://vscodium.com/) is [installed as a Flatpak](https://flathub.org/en/apps/com.vscodium.codium) on [secureblue](https://secureblue.dev/) which is based on [Fedora Atomic](https://fedoraproject.org/atomic-desktops/). 

`cargo test` fails `fs::test::path_sanity_check` because of line 299 in `./helper/src/fs.rs`
```rust
...
            assert!(path.ends_with(expected));
...
```
The issue is that it's checking for incorrect path ends (line 292-294) because of the way Atomic distros and Flatpaks handle file paths:
`/var/home/username/.var/app/com.vscodium.codium/cache/cuprate` does not end with `.cache/cuprate`
`/var/home/username/.var/app/com.vscodium.codium/config/cuprate` does not end with `.config/cuprate`
`/var/home/username/.var/app/com.vscodium.codium/data/cuprate` does not end with `.local/share/cuprate`

The simplest solution would be to just remove the test, but more complex logic could be implemented to do more thorough checks.

# Discussion History
# Action History
- Created by: An-anonymous-coder | 2026-05-07T21:10:27+00:00
