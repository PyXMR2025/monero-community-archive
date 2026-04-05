---
title: Private file permissions by default
source_url: https://github.com/Cuprate/cuprate/issues/551
author: hinto-janai
assignees: []
labels:
- C-request
- E-easy
- E-help-wanted
- A-binaries
created_at: '2025-09-27T13:40:55+00:00'
updated_at: '2025-09-27T13:40:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Feature
`cuprated` creates files with global read/execute permissions (`rwxr-xr-x`), any other process running on the machine can read these files.

Certain libraries that create files (e.g. LMDB) may set their own `umask` although `cuprated` does not. It would be prudent to set a private global `umask` before creating files:

| umask | file permissions |
|-------|------------------|
| `027` | `rwxr-x---`      |
| `007` | `rwx------`      |

## Implementation
Windows will need a separate impl.

```rust
fn main() {
    // SAFETY: calling C.
    unsafe {
        libc::umask(0o027);
    }

    /* ... */
}
```

# Discussion History
# Action History
- Created by: hinto-janai | 2025-09-27T13:40:55+00:00
