---
title: v0.18.4.6-RC1
type: release
source_url: https://github.com/MrCyjaneK/monero_c/releases/tag/v0.18.4.6-RC1
author: MrCyjaneK
tag_name: v0.18.4.6-RC1
published_at: '2026-03-13T13:00:36+00:00'
---

# Version: v0.18.4.6-RC1

# Release Notes

# v0.18.4.6-RC1

This release brings many changes

## Good new updates

`monero`, `zano` and `wownero` got updated to latest stable versions.

## New contrib/depends

We no longer depend on forked monero's contrib/depends - instead we depend on simplybs, for now contrib/depends API is there with a small wrapper.

## New release structure

Library names are now corrected, from 

`${triplet}_{,lib}${coin}_libwallet2_api_c.${suffix}`

to a more uniform `${triplet}/lib${coin}_wallet2_api_c.${suffix}`

## Almost reproducible builds

When targeting x86_64-linux-gnu the only difference in binary is the git tag embedded as a part of build process, soon we will have fully reproducible builds.


Other than that everything is the same, monero.dart is updated, there's new C test suite happening and few other things I probably forgot about.