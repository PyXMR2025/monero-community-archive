---
title: Please support skipping network-related tests
source_url: https://github.com/monero-project/monero/issues/4026
author: jonassmedegaard
assignees: []
labels: []
created_at: '2018-06-19T10:19:14+00:00'
updated_at: '2018-06-19T11:57:10+00:00'
type: issue
status: closed
closed_at: '2018-06-19T11:57:10+00:00'
---

# Original Description
Hi,

Two tests in the testsuite - <tests/unit_tests/address_from_url.cpp> and <tests/unit_tests/dns_resolver.cpp> - depend on network access.

Some build environments - Debian build daemons in particular - deliberately have no network access to ensure reproducibility.

Please support skipping network-related tests - preferably using an environment flag, so that same precompiled tests are possible to be easily rerun in another environment.

# Discussion History
## moneromooo-monero | 2018-06-19T11:50:48+00:00
You can do this with the --gtest_filter option, or the GTEST_FILTER env var.


## jonassmedegaard | 2018-06-19T11:57:10+00:00
oh. Sorry for turning this into a support channel, that was unintended! Clearly there's no issue, then.

# Action History
- Created by: jonassmedegaard | 2018-06-19T10:19:14+00:00
- Closed at: 2018-06-19T11:57:10+00:00
