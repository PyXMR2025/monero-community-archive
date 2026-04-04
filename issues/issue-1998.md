---
title: 'cannot stat ''/mingw64/bin/libicudt62.dll'': No such file or directory'
source_url: https://github.com/monero-project/monero-gui/issues/1998
author: fbmoose48
assignees: []
labels:
- resolved
created_at: '2019-03-08T15:16:59+00:00'
updated_at: '2019-04-23T18:27:46+00:00'
type: issue
status: closed
closed_at: '2019-04-23T18:27:46+00:00'
---

# Original Description
After the final 'make deploy' command this was returned:

cp: cannot stat '/mingw64/bin/libicudt62.dll': No such file or directory
make: *** [Makefile:441: deploy] Error 1
 and the monero-wallet-gui won't run. any ideas?


# Discussion History
## dEBRUYNE-1 | 2019-03-08T18:25:23+00:00
Which version of the icu files are present in your MingW64 directory? The make deploy script is looking for version 62, but you may have a higher version present. If so, you have to manually copy the required files:

https://github.com/monero-project/monero-gui/blob/master/windeploy_helper.sh#L19-L20

## fbmoose48 | 2019-03-08T19:50:26+00:00
My mysys64/mingw64/bin folder has libicu ** 61.dll files present. How would I go about updating them to libicu ** 62.dll? 

## dEBRUYNE-1 | 2019-03-09T08:19:30+00:00
You need to update your MSYS2 environment. Alternatively, you could copy the libicu ** 61.dll files to the build directory of the GUI, as, if I recall correctly, that should work fine. 

## dEBRUYNE-1 | 2019-04-23T18:21:42+00:00
I am doing some housekeeping and closing all old build relates issues, as they are probably not relevant anymore.



## dEBRUYNE-1 | 2019-04-23T18:21:46+00:00
+resolved

# Action History
- Created by: fbmoose48 | 2019-03-08T15:16:59+00:00
- Closed at: 2019-04-23T18:27:46+00:00
