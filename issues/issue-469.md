---
title: CLI testing harness for `cuprated`
source_url: https://github.com/Cuprate/cuprate/issues/469
author: hinto-janai
assignees: []
labels:
- C-proposal
created_at: '2025-05-13T01:44:14+00:00'
updated_at: '2025-05-13T01:44:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
> [!NOTE]
> TODO

## What
CLI input/output testing harness for `cuprated`.

## Why
Assert various output/behavior is as expected across time.

TODO: long-running output testing e.g. asserting `Synchronised with the network` is eventually emitted.

## Where
Either `/tests/cli` or `/binaries/cli`.

Crate: `cuprate-test-cli`.

## How
`cuprate-test-cli`:

```rust
trait CliTest {
    // e.g. `["--help"]`
    fn flags() -> &'static [&'static str];

    /// # Panics
    /// Allowed to panic if test fails.
    fn test(stdout: String, stderr: String);
}

/* impl various cli tests */

const CUPRATED: &str = "target/debug/cuprated"; // or elsewhere

fn main() {
    let cli_tests = todo!();

    for test in cli_tests {
        let output = std::process::Command::new("cmd")
            .args([[CUPRATED, test.flags()]].concat())
            .output()
            .unwrap();

        test.test(output.stdout, output.stderr);
    }
}
```
CI:
```yaml
- name: CLI test
  run: cargo run --bin cuprate-test-cli
```

# Discussion History
# Action History
- Created by: hinto-janai | 2025-05-13T01:44:14+00:00
