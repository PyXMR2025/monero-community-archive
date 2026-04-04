---
title: cmake fails when gtest is installed on the system
source_url: https://github.com/monero-project/monero/issues/980
author: flounders
assignees: []
labels: []
created_at: '2016-08-23T14:24:11+00:00'
updated_at: '2016-09-01T16:17:45+00:00'
type: issue
status: closed
closed_at: '2016-09-01T16:17:45+00:00'
---

# Original Description
Everytime I try running just `make` I keep getting this:

```
-- outfile location is /home/swilliams/builds/bitmonero/build/release/lib/libwallet_merged.a
CMake Error at tests/CMakeLists.txt:90 (set_property):
  set_property could not find TARGET gtest.  Perhaps it has not yet been
  created.


-- Configuring incomplete, errors occurred!
See also "/home/swilliams/builds/bitmonero/build/release/CMakeFiles/CMakeOutput.log".
See also "/home/swilliams/builds/bitmonero/build/release/CMakeFiles/CMakeError.log".
```

Running `make debug` I was able to get a binary, but not with `make` by itself.

I've attached both files referenced. I'm using Arch Linux x86_64, I have all the dependencies installed.

[CMakeError.log.txt](https://github.com/monero-project/bitmonero/files/432636/CMakeError.log.txt)
[CMakeOutput.log.txt](https://github.com/monero-project/bitmonero/files/432637/CMakeOutput.log.txt)


# Discussion History
## radfish | 2016-08-23T14:53:36+00:00
Try `yaourt bitmonero-git` from AUR and compare.


## flounders | 2016-08-23T16:27:49+00:00
Same message again using yaourt to build it. I typically use aura and it has had issues too. I've attached the output below.

```
-- outfile location is /tmp/yaourt-tmp-swilliams/aur-bitmonero-git/src/bitmonero/build/lib/libwallet_merged.a
CMake Error at tests/CMakeLists.txt:90 (set_property):
  set_property could not find TARGET gtest.  Perhaps it has not yet been
  created.


-- Configuring incomplete, errors occurred!
See also "/tmp/yaourt-tmp-swilliams/aur-bitmonero-git/src/bitmonero/build/CMakeFiles/CMakeOutput.log".
See also "/tmp/yaourt-tmp-swilliams/aur-bitmonero-git/src/bitmonero/build/CMakeFiles/CMakeError.log".
```

[CMakeError.log.txt](https://github.com/monero-project/bitmonero/files/432988/CMakeError.log.txt)
[CMakeOutput.log.txt](https://github.com/monero-project/bitmonero/files/432989/CMakeOutput.log.txt)


## radfish | 2016-08-23T16:48:21+00:00
Could you please attach the full cmake output that you get on the console, not in the CMakeOutput file?
Remember to delete the build directory and re-run the command (or just start from scratch), so that cmake is not using any cached data.


## radfish | 2016-08-23T16:52:18+00:00
Also, do you have `gtest` package installed? If so, could you try uninstalling that package and retrying the build?


## flounders | 2016-08-23T18:50:26+00:00
It built after I removed gtest. Otherwise, it didn't seem to matter what I'd do.


## radfish | 2016-08-25T02:26:28+00:00
Could you please change the title to: cmake fails when gtest is installed on the system


## radfish | 2016-09-01T15:14:18+00:00
gtest patch merged, this can be closed


# Action History
- Created by: flounders | 2016-08-23T14:24:11+00:00
- Closed at: 2016-09-01T16:17:45+00:00
