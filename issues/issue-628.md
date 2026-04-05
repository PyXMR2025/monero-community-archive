---
title: Ubuntu PPA - Up for grabs
source_url: https://github.com/xmrig/xmrig/issues/628
author: ghost
assignees: []
labels:
- review later
created_at: '2018-05-14T05:03:00+00:00'
updated_at: '2019-08-02T13:21:24+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:21:24+00:00'
---

# Original Description
```bash
sudo add-apt-repository ppa:gr1d/miners
sudo apt-get update
sudo apt install xmrig
```


Hello, I threw together some source for a ubuntu PPA if you guys want to release on apt.

Go here:

https://launchpad.net/~gr1d/+archive/ubuntu/miners/+packages

Hit the triangle next to xmrig

download the .tar.gz

Then follow these instructions:

http://packaging.ubuntu.com/html/getting-set-up.html

http://packaging.ubuntu.com/html/packaging-new-software.html

**Just be careful with file permissions, make sure to update and edit the copyright files in debian/ and control files in debian/ and put your pool into the src/net/strategy/DonateStrategy.cpp file.

Also update the xmrig.1 manpage. Just be very careful not to touch the file permissions and don't use sudo... at all.**

**The known bugs are the manpage, it gets a error saying some sort of formatting is incorrect. And the changelog has no bug-close so it throws a warning on lintian as well.**


I'll happily take a donation of bbscoin:

```fySxx5vnVwS9tvfNqjxfm8MQmqmvUgzYgAMD3xuUmLRTfZrDXHsTSDQcDchJyDv6hDMYQFHEA6J5Y38htYLroBvk2qg5sYZdj```


# Discussion History
# Action History
- Created by: ghost | 2018-05-14T05:03:00+00:00
- Closed at: 2019-08-02T13:21:24+00:00
