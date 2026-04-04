---
title: Release source tarballs?
source_url: https://github.com/monero-project/monero-gui/issues/4186
author: WhyNotHugo
assignees: []
labels: []
created_at: '2023-06-04T13:26:46+00:00'
updated_at: '2023-06-05T16:27:52+00:00'
type: issue
status: closed
closed_at: '2023-06-05T01:14:06+00:00'
---

# Original Description
I'm trying to build the latest release. I see two release tarballs in [the release page](https://github.com/monero-project/monero-gui/releases/tag/v0.18.2.2):

The first is [monero-gui-linux-x64-v0.18.2.2.tar.bz2](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.18.2.2.tar.bz2). This seems to just include some x86_64 binaries for an unnamed distribution. These link to a lot of libraries, so won't work in any environment even slightly different from the build environment (and definitely won't work on anything that's not x86_64).

The second is [v0.18.2.2.tar.gz](https://github.com/monero-project/monero-gui/archive/refs/tags/v0.18.2.2.tar.gz), which seems to contain the source itself and should work on any distribution/architecture. However, trying to build this fails:

```
-- The C compiler identification is GNU 13.1.1
-- The CXX compiler identification is GNU 13.1.1
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Initiating compile using CMake 3.26.4
-- Found Git: /usr/bin/git (found version "2.40.1") 
-- Checking submodules
fatal: not a git repository (or any of the parent directories): .git
fatal: not a git repository (or any of the parent directories): .git
-- Submodule 'monero' is up-to-date
CMake Error at CMakeLists.txt:55 (add_subdirectory):
  The source directory

    /home/hugo/src/gitlab.alpinelinux.org/alpine/aports/testing/monero-gui/src/monero-gui-0.18.2.2/monero

  does not contain a CMakeLists.txt file.


-- Found Git: /usr/bin/git
CMake Error at cmake/VersionGui.cmake:40 (get_version_tag_from_git):
  Unknown CMake command "get_version_tag_from_git".
Call Stack (most recent call first):
  CMakeLists.txt:79 (include)


-- Configuring incomplete, errors occurred!
```

Looks like the cmake build script tries to extract the current version from git, but the tarball doesn't include any git metadata. Maybe these tarballs should include a `VERSION` file which includes the version for which they've been generated?

Are there any other release tarballs that should be used downstream, or should I just clone the git repository and build using the tag I want?



# Discussion History
## WhyNotHugo | 2023-06-04T13:28:21+00:00
From what I can tell, downstream distributions are just cloning from git and checking out the tag. E.g.: [the ArchLinux package](https://gitlab.archlinux.org/archlinux/packaging/packages/monero-gui/-/blob/main/PKGBUILD) does this.

I guess this might count as a feature request, but release tarballs would be super useful for downstream, both for end users to build this program and for distributions to package using that as a source.

## selsta | 2023-06-05T01:14:06+00:00
We offer the source code here:

- https://downloads.getmonero.org/gui/source
- https://downloads.getmonero.org/gui/monero-gui-source-v0.18.2.2.tar.bz2

> The second is [v0.18.2.2.tar.gz](https://github.com/monero-project/monero-gui/archive/refs/tags/v0.18.2.2.tar.gz), which seems to contain the source itself and should work on any distribution/architecture. However, trying to build this fails:

The source code on the GitHub release page is automatically generated from GitHub and doesn't contain submodules. We can't disable or change this.

Closing because the link above should solve your question, if not I'll reopen.

## WhyNotHugo | 2023-06-05T08:55:54+00:00
> The source code on the GitHub release page is automatically generated from GitHub and doesn't contain submodules. We can't disable or change this.

Oh, yeah, I didn't realise it was just a link to those. I've suffered from this anti-feature on some projects of my own too.

> Closing because the link above should solve your question, if not I'll reopen.

Yes, this answers my question, thanks. 

I don't think that there's any link to these tarballs in the README, nor on the releases page. So they're not easy to find.

## selsta | 2023-06-05T16:27:52+00:00
The source code is linked here: https://www.getmonero.org/downloads/

# Action History
- Created by: WhyNotHugo | 2023-06-04T13:26:46+00:00
- Closed at: 2023-06-05T01:14:06+00:00
