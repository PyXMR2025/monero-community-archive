---
title: Build fails on Pinebook Pro - aarch64 running Manjaro
source_url: https://github.com/monero-project/monero/issues/7900
author: Dendrocalamus64
assignees: []
labels: []
created_at: '2021-08-27T09:15:07+00:00'
updated_at: '2021-08-31T17:29:48+00:00'
type: issue
status: closed
closed_at: '2021-08-31T17:29:48+00:00'
---

# Original Description
It built successfully last year.  Now it fails building tests/unit_tests/wipeable_string.cpp with,
`/usr/include/boost/optional/optional.hpp:1596:3: error: static assertion failed: If you want to output boost::optional, include header <boost/optional/optional_io.hpp>                           
 1596 |   BOOST_STATIC_ASSERT_MSG(sizeof(CharType) == 0, "If you want to output boost::optional, include header <boost/optional/optional_io.hpp>"); `

Changing the include from <boost/optional/optional.hpp> to <boost/optional/optional_io.hpp> doesn't fix it, then it starts saying,
`/usr/include/boost/optional/optional_io.hpp:47:21: error: no match for ‘operator<<’ (operand types are ‘std::basic_ostream<char>’ and ‘const epee::wipeable_string’)`

It's similar to this bug on another project:
[REQUIRE/CHECK not compatible with boost::optional](https://github.com/catchorg/Catch2/issues/1135)

# Discussion History
## selsta | 2021-08-27T12:58:41+00:00
Which branch / tag did you check out?

## Dendrocalamus64 | 2021-08-27T15:17:52+00:00
v0.17.2.0, commit f6e63ef260e795aacd408c28008398785b84103a.

Manjaro doesn't yet have aarch64 binaries for all of its packages.  I'm trying to use the current Manjaro PKGBUILD file, which they get from Arch Linux, with the build architecture changed from x86_64 to aarch64, and that's the version it checks out.

## Dendrocalamus64 | 2021-08-28T13:12:54+00:00
I tried the build instructions on this project's top page, and building that way does work for me.

The Arch wiki says,
[Makepkg fails, but make succeeds](https://wiki.archlinux.org/title/makepkg#Makepkg_fails,_but_make_succeeds)
>If something manually compiles using make, but fails through makepkg, it is almost certainly because /etc/makepkg.conf sets a compilation variable to something reasonable that usually works, but that what you are compiling is incompatible with.

So, next I'll figure out what build options are necessary to reproduce the error.

## selsta | 2021-08-28T13:14:57+00:00
release-v0.17 branch contains a fix for your reported issue, it's not included in v0.17.2.0 tag

## Dendrocalamus64 | 2021-08-31T17:29:48+00:00
Oh, I see it.
67ba733de173008a94e6fcb1b4bf8549acbe81ec, merged into release-v0.17 in pull request #7825 on Aug 27.

If I apply that patch to wipeable_string.cpp, it builds successfully.  Thank you!

# Action History
- Created by: Dendrocalamus64 | 2021-08-27T09:15:07+00:00
- Closed at: 2021-08-31T17:29:48+00:00
