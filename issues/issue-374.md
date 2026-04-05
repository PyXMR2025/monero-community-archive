---
title: Release rules & schedule for `cuprated`
source_url: https://github.com/Cuprate/cuprate/issues/374
author: hinto-janai
assignees: []
labels:
- A-binaries
created_at: '2025-01-21T18:01:46+00:00'
updated_at: '2025-11-03T18:07:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue tracks rules and information related to `cuprated` **alpha** releases.

These rules may be changed at any time.

## Versioning
The rules for `cuprated`'s versioning scheme.

`cuprated` versions follow [semantic versioning](https://semver.org).

- `0.0.x` represents alpha builds
- `0.x.0` represents beta builds
- `x.0.0` represents stable builds
- No stability guarantees are made until a `1.0.0` release

## Codenames
The rules for `cuprated` release codenames.

A release codename is: 
- A name of a metal (using the electrically conductive definition)
- Changed upon semantic version change, ignoring alpha builds (`0.0.x -> 0.x.0`, `0.x.0 -> x.0.0`, `x.0.0 -> y.0.0`)

## Killswitch
The rules for the [killswitch mechanism](https://github.com/Cuprate/cuprate/pull/365) in `cuprated` releases.

The killswitch must:
- Not activate before the next release is public
- Be removed prior to a stable release

## Schedule parameters
The currently followed parameters for `cuprated`'s release schedule.

| Parameter                 | Value | Description |
|---------------------------|-------|-------------|
| RELEASE_CYCLE_WEEK_LENGTH | 6 (was 4 from `0.0.1` to `0.0.3`) | The amount of weeks in-between releases.
| KILLSWITCH_GRACE_PERIOD   | 7     | The amount of days an old binary is allowed to stay online after a new release.

## Rule caveats
The exceptions to the above rules:

- If deemed appropriate, the release schedule can be broken to issue releases containing important fixes.
- If deemed appropriate, issuing releases with breaking changes (perhaps against semantic versioning) is allowed.

## Schedule
`cuprated`'s release schedule for the next year under the above rules.

| `cuprated` version | Release codename | Release date | Killswitch date | Killswitch timestamp |
|--------------------|------------------|--------------|-----------------|----------------------|
| 0.0.1              | Molybdenite      | 2025-03-12   | 2025-04-16      | 1744761600           |
| 0.0.2              | Molybdenite      | 2025-04-09   | 2025-05-14      | 1747180800           |
| 0.0.3              | Molybdenite      | 2025-05-07   | 2025-06-11      | 1749600000           |
| 0.0.4              | Molybdenite      | 2025-06-04   | 2025-07-23      | 1753228800
| 0.0.5              | Molybdenite      | 2025-07-16   | 2025-09-03      | 1756857600
| 0.0.6              | Molybdenite      | 2025-08-27   | 2025-10-15      | 1760486400
| 0.0.7              | Molybdenite      | 2025-10-08   | 2025-11-26      | 1764115200
| 0.0.8              | Molybdenite      | 2025-11-19   | 2026-01-07      | 1767744000
| 0.0.9              | Molybdenite      | 2025-12-31   | 2026-02-18      | 1771372800
| 0.1.0              | ?                | ????-??-??   | ?               | ?
| 1.0.0              | ?                | ????-??-??   | N/A             | N/A





# Discussion History
## hinto-janai | 2025-01-21T19:46:28+00:00
Generates alpha release info.

```bash
RELEASE_CYCLE_WEEK_LENGTH=6 KILLSWITCH_GRACE_PERIOD=7 cargo run
```

```rust
//! ```Cargo.toml
//! [package]
//! name = "generate_cuprate_release_info"
//! version = "0.2.0"
//! edition = "2024"
//!
//! [dependencies]
//! chrono = "*"
//! ``````

use std::env::var;

use chrono::{Datelike, Days, TimeZone, Utc};

fn main() {
    let mut date = Utc.with_ymd_and_hms(2025, 6, 4, 0, 0, 0).unwrap();

    let release_cycle_week_length = Days::new(
        7 * var("RELEASE_CYCLE_WEEK_LENGTH")
            .unwrap()
            .parse::<u64>()
            .unwrap(),
    );

    let killswitch_grace_period = Days::new(
        var("KILLSWITCH_GRACE_PERIOD")
            .unwrap()
            .parse::<u64>()
            .unwrap(),
    );

    for txt in [
        "| `cuprated` version | Release codename | Release date | Killswitch date | Killswitch timestamp |",
        "|--------------------|------------------|--------------|-----------------|----------------------|",
        "| 0.0.1              | Molybdenite      | 2025-03-12   | 2025-04-16      | 1744761600           |",
        "| 0.0.2              | Molybdenite      | 2025-04-09   | 2025-05-14      | 1747180800           |",
        "| 0.0.3              | Molybdenite      | 2025-05-07   | 2025-06-11      | 1749600000           |",
    ] {
        println!("{txt}");
    }

    for i in 4.. {
        if date.year() != 2025 {
            break;
        }

        let ks_date = date + release_cycle_week_length + killswitch_grace_period;
        let ks_timestamp = ks_date.timestamp();

        println!(
            "| 0.0.{i:<14} | Molybdenite      | {}   | {}      | {ks_timestamp}",
            date.format("%F"),
            ks_date.format("%F")
        );

        date = date + release_cycle_week_length;
    }

    for txt in [
        "| 0.1.0              | ?                | ????-??-??   | ?               | ?",
        "| 1.0.0              | ?                | ????-??-??   | N/A             | N/A",
    ] {
        println!("{txt}");
    }
}
```

## hinto-janai | 2025-05-27T21:02:52+00:00
Changed release cycle from 4 to 6 weeks, discussed here: https://github.com/monero-project/meta/issues/1203. 

## hinto-janai | 2025-11-03T18:07:15+00:00
Releases are now done whenever necessary instead of a fixed schedule and the killswitch is removed starting from `cuprated v0.0.8`.

Discussed here: https://github.com/monero-project/meta/issues/1280#issuecomment-3429009347.

# Action History
- Created by: hinto-janai | 2025-01-21T18:01:46+00:00
