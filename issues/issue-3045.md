---
title: stop shipping empty file monero-wallet-gui.AppImage
source_url: https://github.com/monero-project/monero-gui/issues/3045
author: adrelanos
assignees: []
labels: []
created_at: '2020-08-19T09:37:28+00:00'
updated_at: '2023-01-18T15:16:11+00:00'
type: issue
status: closed
closed_at: '2023-01-18T15:16:10+00:00'
---

# Original Description
`cat monero-wallet-gui.AppImage`

```
./monero-wallet-gui
```

I don't see any point for that? Could you please consider stopping to ship that file?

Causes a `lintian` warning.

```
W: monero-gui: executable-not-elf-or-script usr/bin/monero-wallet-gui.AppImage
N: 
N:    This executable file is not an ELF format binary, and does not start
N:    with the #! sequence that marks interpreted scripts. It might be a sh
N:    script that fails to name /bin/sh as its shell, or it may be incorrectly
N:    marked as executable. Sometimes upstream files developed on Windows are
N:    marked unnecessarily as executable on other systems.
N:    
N:    If you are using debhelper to build your package, running dh_fixperms
N:    will often correct this problem for you.
N:    
N:    Refer to Debian Policy Manual section 10.4 (Scripts) for details.
N:    
N:    Severity: normal, Certainty: certain
N:    
N:    Check: scripts, Type: binary
N:
```

# Discussion History
## selsta | 2020-08-19T10:11:30+00:00
It is a workaround for Ubuntu / Tails so that Monero GUI can be started from the file explorer. Directly double clicking the binary or a .sh file does not work.

## cassepipe | 2021-09-13T09:29:23+00:00
Did you consider making a genuine AppImage that can be integrated to the desktop ?

## selsta | 2023-01-18T15:16:10+00:00
Closing, please see my previous comment on why we keep the empty AppImage: https://github.com/monero-project/monero-gui/issues/3045#issuecomment-676082064

# Action History
- Created by: adrelanos | 2020-08-19T09:37:28+00:00
- Closed at: 2023-01-18T15:16:10+00:00
