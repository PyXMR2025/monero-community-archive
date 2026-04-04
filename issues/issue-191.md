---
title: Crash on Mac 10.12.1
source_url: https://github.com/monero-project/monero-gui/issues/191
author: dternyak
assignees: []
labels: []
created_at: '2016-11-19T21:44:28+00:00'
updated_at: '2017-01-10T19:52:53+00:00'
type: issue
status: closed
closed_at: '2017-01-10T15:06:02+00:00'
---

# Original Description
[This](http://imgur.com/a/bmyV3) album created by a user on [reddit](https://www.reddit.com/r/Monero/comments/5dujei/monero_gui_build_3_macos_unofficial_build_of/da7ekz0/?context=3&st=ivpqord5&sh=d0bf3529) shows a crash on Mac. 

It seems like there is a dependency on QT - it should be included in the binary so that users don't need to have it installed externally. 

Another report:
   - Termination Reason: DYLD, [0x1] Library missing 
   - Application Specific Information: dyld: launch, loading dependent libraries
Dyld Error Message: Library not loaded: @rpath/QtQuick.framework/Versions/5/QtQuick Referenced from: /private/var/folders/*/monero-core.app/Contents/MacOS/monero-core Reason: image not found

# Discussion History
## dEBRUYNE-1 | 2016-11-20T00:58:29+00:00
Are we certain the binary distributed by Vertp was built correctly by him?


## dternyak | 2016-11-20T01:21:13+00:00
Well there's not much that can go wrong when building it, and I can confirm it works on macOs when QT is installed. Just a simple `bash build.sh` after `./get_libwallet_api.sh`


## Jaqueeee | 2016-11-20T12:58:44+00:00
There are some extra steps involved when deploying for platforms that don't have the dependencies installed (i.e. boost, openssl). The boost brew package also needs to be custom built to support older hardware. Same issue we had on older windows machines. I'll update the docs when i've sorted this out. 


## Jaqueeee | 2016-11-21T20:25:49+00:00
@dternyak 
Could you try this build?
https://www.dropbox.com/s/it6woiru9nf5s2v/monero-core-osx-jaquee.zip?dl=0
sha1 ad7cb969e7a7dcf47610ef8a92eee90bdb836e2e

Update 161121 - with all open PR's except #188
https://www.dropbox.com/s/u5uljx9aqcyhttg/monero-core-osx-161121-jaquee.zip?dl=0
sha1 6f2c740e138e6191b81f2f35e6c3809e03813fb8

## dternyak | 2016-11-22T01:21:29+00:00
@sfinkz Can you confirm you do not have QT installed on your machine? 

## sfinkz | 2016-11-22T01:36:52+00:00
@dternyak I am sorry, Indeed I have. Will remove the message.

## dternyak | 2016-11-22T01:52:06+00:00
@sfinkz No need to remove your message, the bug simply appears only when a user does not have QT installed on their system, so that is what we are trying to test. 

## medusadigital | 2016-11-23T15:16:50+00:00
ok so the open question of mac deployment seems to be solved ? 

## dternyak | 2016-11-23T16:24:56+00:00
@medusadigital I'd like to see a PR with updated build instructions before I mark this issue as closed, do you agree @Jaqueeee ?

## Jaqueeee | 2016-11-23T18:34:24+00:00
Agreed @dternyak 

## Jaqueeee | 2017-01-10T19:52:53+00:00
Sorry, I never updated those instructions. But not sure if it's a good idea to clutter the Readme with deploy instructions anyway. 

# Action History
- Created by: dternyak | 2016-11-19T21:44:28+00:00
- Closed at: 2017-01-10T15:06:02+00:00
