---
title: 'Test fails: notify.works'
source_url: https://github.com/monero-project/monero/issues/5261
author: vicsn
assignees: []
labels: []
created_at: '2019-03-09T08:26:45+00:00'
updated_at: '2019-03-09T17:38:55+00:00'
type: issue
status: closed
closed_at: '2019-03-09T17:38:55+00:00'
---

# Original Description
The notify test fails for me. You can invoke it via: `./tests/unit_tests/unit_tests --gtest_filter=notify.works`

It looks like I need to add an executable file `[build_folder]/tests/unit_tests/test_notifier` which should then point to the given temporary file `name_template`. Do you have a template for the test_notifier, and could this be placed in e.g. `monero/tests/unit_tests` to ensure people have access to it?

# Discussion History
## moneromooo-monero | 2019-03-09T09:33:37+00:00
Which platform, and what commit hash ?

## vicsn | 2019-03-09T17:16:09+00:00
Platform: Ubuntu 18.0.4.2, 64 bit, Intel i7
Commit hash (current master): `49afbd0c53d29656689f319c7d3543204ead4e59`

## moneromooo-monero | 2019-03-09T17:25:48+00:00
How did you build it ?
What is the output of: find build -name test_notifier

## vicsn | 2019-03-09T17:38:55+00:00
Brilliant, I should've seen the test_notifier executable earlier in CMakelists.txt 

I assumed it was a shell script and was taking a shortcut by building using `make -jx unit_tests`, which caused the test_notifier not to be built. 

# Action History
- Created by: vicsn | 2019-03-09T08:26:45+00:00
- Closed at: 2019-03-09T17:38:55+00:00
