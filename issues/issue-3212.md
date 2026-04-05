---
title: xmrig 6.19.0 fails to compile on 32bit systems with clang15
source_url: https://github.com/xmrig/xmrig/issues/3212
author: ehaupt
assignees: []
labels:
- bug
created_at: '2023-02-17T09:20:01+00:00'
updated_at: '2025-06-16T19:59:04+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:59:03+00:00'
---

# Original Description
**Describe the bug**
FreeBSD recently imported llvm15 to the main branch. CI detected that xmrig 6.19.0 fails to compile on 32bit systems with clang15. It builds fine with clang14 on 32bit systems.

**To Reproduce**
Build xmrig 6.19.0 with clang15.

**Expected behavior**
Expect the port to compile.

**Required data**
Full build log: https://lists.freebsd.org/archives/freebsd-pkg-fallout/2023-February/324703.html

# Discussion History
## SChernykh | 2023-02-19T08:45:46+00:00
https://github.com/xmrig/xmrig/pull/3213 should fix the error from this build log, but I can't check for other errors since I don't know how to setup this. Is there any FreeBSD dev release iso for this?

## ehaupt | 2023-02-19T09:55:47+00:00
Thank you. https://github.com/xmrig/xmrig/pull/3213 solves the issue.

If you like to test against FreeBSD, I recommend downloading a VM from https://download.freebsd.org/snapshots/VM-IMAGES/14.0-CURRENT/

The easiest way to get started would be:

- install bash and git
```
pkg intall -y bash git
```

- Change from quarterly to the latest pkg repository:
```
mkdir -p /usr/local/etc/pkg/repos/
echo 'FreeBSD: { url: "http://pkg0.fra.freebsd.org/${ABI}/latest" }' \
        > /usr/local/etc/pkg/repos/FreeBSD.conf
```

- Upgrade everything to latest:
```
pkg upgrade -y
```

- Get the latest ports tree:
```
git clone https://git.FreeBSD.org/ports.git /usr/ports
```

- Save the following script to /root/bin/inst-missing
```
#!/usr/bin/env bash

repo="${1:-FreeBSD}"
missingmk=/tmp/.missing.mk

cat << 'EOF' > ${missingmk}
# hack for inadequacy of 'missing-packages'
missing-packages-without-version:
        @_packages=$$(${PKG_INFO} -aq); \
        for dir in $$(${ALL-DEPENDS-LIST}); do \
                _p=$$(cd $$dir; ${MAKE} -VPKGBASE); \
                if ! $$(${ECHO_CMD} $${_packages} | ${GREP} -q $${_p}); then \
                        ${ECHO_CMD} $${_p}; \
                fi; \
        done
EOF

pkg update
make -f Makefile -f ${missingmk} missing-packages-without-version | xargs pkg install -y -r "${repo}"
```

- Make it executable:
```
chmod a+x /root/bin/inst-missing
```

- Go to the xmrig port and invoke the `inst-missing` script in order to install all dependencies via pkg:
```
cd /usr/ports/net-p2p/xmrig
inst-missing
```

- From here on you have all dependencies installed

# Action History
- Created by: ehaupt | 2023-02-17T09:20:01+00:00
- Closed at: 2025-06-16T19:59:03+00:00
