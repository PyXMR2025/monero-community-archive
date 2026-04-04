---
title: Wallet.cpp error on windows build
source_url: https://github.com/monero-project/monero-gui/issues/3848
author: reemuru
assignees: []
labels: []
created_at: '2022-03-03T21:19:30+00:00'
updated_at: '2022-03-08T04:32:09+00:00'
type: issue
status: closed
closed_at: '2022-03-08T04:32:09+00:00'
---

# Original Description
This is my mistake. Since this #3828 was my first pull request doesn't look like workflows ever ran to catch this. Will patch today and update my forks to run ci.

<details>
<summary>
logs
</summary>
<code>
 D:/a/monero-gui/monero-gui/src/libwalletqt/Wallet.cpp:859:5: error: 'u_int64_t' was not declared in this scope; did you mean 'uint64_t'?
</code>
<br />
<code>
  859 |     u_int64_t total;
</code>
<br />
<code>
      |     ^~~~~~~~~
</code>
<br />
<code>
      |     uint64_t
</code>
<br/>
<code>
D:/a/monero-gui/monero-gui/src/libwalletqt/Wallet.cpp:860:14: error: expected ';' before 'spent'
</code>
<br/>
<code>
  860 |     u_int64_t spent;
</code>
</details>

# Discussion History
## selsta | 2022-03-04T00:58:11+00:00
I opened #3849, let's see if CI is green now.

# Action History
- Created by: reemuru | 2022-03-03T21:19:30+00:00
- Closed at: 2022-03-08T04:32:09+00:00
