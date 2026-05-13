---
title: Use Simple systemd Service Instead of Forking?
source_url: https://github.com/monero-project/monero/issues/3321
author: prikhi
assignees: []
labels: []
created_at: '2018-02-27T01:15:04+00:00'
updated_at: '2026-05-11T09:08:08+00:00'
type: issue
status: closed
closed_at: '2026-05-11T09:08:08+00:00'
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

## x64x2 | 2026-05-11T02:32:43+00:00
systemd is cancer, thats like going for ferrari instead of volvo 1984 model.

## plowsof | 2026-05-11T06:37:54+00:00
Can be closed as completed 

# Action History
- Created by: prikhi | 2018-02-27T01:15:04+00:00
- Closed at: 2026-05-11T09:08:08+00:00
