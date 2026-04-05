---
title: Deprecating `x86_64-apple-darwin`
source_url: https://github.com/Cuprate/cuprate/issues/552
author: hinto-janai
assignees: []
labels:
- C-discussion
- E-easy
- E-help-wanted
created_at: '2025-09-30T17:40:19+00:00'
updated_at: '2025-11-26T19:40:03+00:00'
type: issue
status: closed
closed_at: '2025-11-26T19:40:03+00:00'
---

# Original Description
## What
Apple, GitHub, and Rust are deprecating support for x64 macOS:
- https://github.blog/changelog/2025-07-11-upcoming-changes-to-macos-hosted-runners-macos-latest-migration-and-xcode-support-policy-updates/#macos-13-is-closing-down 
- https://blog.rust-lang.org/2025/09/18/Rust-1.90.0/#demoting-x86-64-apple-darwin-to-tier-2-with-host-tools

Cuprate will have to update CI and the user book:

https://github.com/Cuprate/cuprate/blob/267c98bcd8a62d70e450905266d05f809a1c2161/.github/workflows/ci.yml#L101

https://github.com/Cuprate/cuprate/blob/267c98bcd8a62d70e450905266d05f809a1c2161/books/user/src/getting-started/download.md?plain=1#L7

# Discussion History
# Action History
- Created by: hinto-janai | 2025-09-30T17:40:19+00:00
- Closed at: 2025-11-26T19:40:03+00:00
