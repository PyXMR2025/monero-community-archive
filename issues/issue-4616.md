---
title: '"Checking submodules" for miniupnp, unbound, and rapidjson during make states
  "No such file or directory" when these directories exist'
source_url: https://github.com/monero-project/monero/issues/4616
author: mmortal03
assignees: []
labels: []
created_at: '2018-10-16T11:46:13+00:00'
updated_at: '2018-10-26T21:25:02+00:00'
type: issue
status: closed
closed_at: '2018-10-26T21:25:02+00:00'
---

# Original Description
When making either Monero master or v0.13.0.3 on Windows in MSYS2 MinGW 64-bit (for instance, by running: make -j9 release-static-win64), I get the following output, even though these submodule directories properly exist (from having previously run a fresh: git clone --recursive https://github.com/monero-project/monero)

> -- Checking submodules
> /bin/bash: line 0: cd: C:/msys64/home/mmortal03/monero/external/miniupnp: No such file or directory
> /bin/bash: line 0: cd: C:/msys64/home/mmortal03/monero/external/unbound: No such file or directory
> /bin/bash: line 0: cd: C:/msys64/home/mmortal03/monero/external/rapidjson: No such file or directory
> 

In spite of this, I can still compile v0.13.0.3, so there's seemingly just something superficially wrong with the submodule checking syntax?

Testing the command from CMakeLists.txt outside of the make process directly on the MSYS2 commandline produces a result, not an error, so it's probably just something wrong with the syntax?

For example, running the following command results in no output from the part before the Boolean operator, and the proper result of the git command from after the Boolean operator:

bash -c "cd C:/msys64/home/mmortal03/monero/external/miniupnp && git rev-parse HEAD"


# Discussion History
## moneromooo-monero | 2018-10-16T11:49:45+00:00
<s>
Do you see files with this ?
ls C:/msys64/home/mmortal03/monero/external/miniupnp
</s>
Nevermind, your last sentence implies there are.

## mmortal03 | 2018-10-21T00:22:05+00:00
This will be fixed once #4620 is merged. Closing.

## xiphon | 2018-10-21T14:33:46+00:00
@mmortal03 
PS: I think you don't have to close the issue before it gets merged

## mmortal03 | 2018-10-21T19:55:01+00:00
I just didn't want to forget to close it later, but for discoverability reasons (others noticing the same thing) maybe it *should* stay open until it gets merged.

## moneromooo-monero | 2018-10-26T20:58:14+00:00
+resolved

# Action History
- Created by: mmortal03 | 2018-10-16T11:46:13+00:00
- Closed at: 2018-10-26T21:25:02+00:00
