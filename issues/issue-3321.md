---
title: Use Simple systemd Service Instead of Forking?
source_url: https://github.com/monero-project/monero/issues/3321
author: prikhi
assignees: []
labels: []
created_at: '2018-02-27T01:15:04+00:00'
updated_at: '2022-02-24T07:15:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently the [systemd service file](https://github.com/monero-project/monero/blob/master/utils/systemd/monerod.service) forks the monerod process. This requires storing the pid & log to external files.

By using `Type=simple` along with the `--non-interactive` flag for monerod, those files become unnecessary.

Reading the log would use `systemctl` & `journalctl` instead:

```
systemctl status monerod
journalctl -u monerod
```

If this is a desirable change, I can make a pull request with the necessary changes.


# Discussion History
## zone117x | 2018-03-05T01:19:05+00:00
Could you make a pull? Might facilitate more discussion at least. 

## tidux | 2022-02-23T04:30:32+00:00
This appears to have been completed at some point in the past.  Can the service file be shipped in the released binaries now?  I ended up hacking together my own `--non-interactive` service file because I didn't see one in the archive I downloaded, but there is an official one in this repository now.

## trasherdk | 2022-02-24T07:15:49+00:00
Shouldn't stuff like that be done by package maintainers?

# Action History
- Created by: prikhi | 2018-02-27T01:15:04+00:00
