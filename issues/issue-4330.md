---
title: Can't build for Windows using Docker on Debian
source_url: https://github.com/monero-project/monero-gui/issues/4330
author: everlyy
assignees: []
labels: []
created_at: '2024-07-24T14:02:10+00:00'
updated_at: '2024-07-26T12:15:38+00:00'
type: issue
status: closed
closed_at: '2024-07-26T12:15:37+00:00'
---

# Original Description
Hi, I'm trying to compile from source for windows using the instructions listed [here](https://github.com/monero-project/monero-gui#building-reproducible-windows-static-binaries-with-docker-any-os), but I'm getting a linking error when compiling.
In short it's complaining about not being able to find `libiconv`, `libiconv_open` and `libiconv_close`.
The full output is attached below.
[output.log](https://github.com/user-attachments/files/16363221/output.log)

Would be greatly appreciated if someone could help me!
Thanks in advance

# Discussion History
## everlyy | 2024-07-26T12:15:37+00:00
Fixed by completely deleting the repo and doing everything over again, not sure what was wrong but it works now!

# Action History
- Created by: everlyy | 2024-07-24T14:02:10+00:00
- Closed at: 2024-07-26T12:15:37+00:00
