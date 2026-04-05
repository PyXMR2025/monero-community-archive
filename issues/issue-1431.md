---
title: Build Issues using DEPS v4.0
source_url: https://github.com/xmrig/xmrig/issues/1431
author: BKdilse
assignees: []
labels:
- question
created_at: '2019-12-16T10:04:46+00:00'
updated_at: '2019-12-16T15:13:18+00:00'
type: issue
status: closed
closed_at: '2019-12-16T15:13:17+00:00'
---

# Original Description
Hi,

Using Visual Studio 2019 for the build.  Same procedure works if I use the DEPS v3.5, but 4.0 is giving the following errors:

```
"C:\Data\Stuff\XMRig\xmrig-master\build\xmrig.sln" (default target) (1) ->
       "C:\Data\Stuff\XMRig\xmrig-master\build\xmrig.vcxproj.metaproj" (default target) (11) ->
       "C:\Data\Stuff\XMRig\xmrig-master\build\xmrig.vcxproj" (default target) (20) ->
       (Link target) ->
         LINK : fatal error C1047: The object or library file 'xmrig.dir\Release\CpuLaunchData.obj' was created wi
       th an older compiler than other objects; rebuild old objects and libraries [C:\Data\Stuff\XMRig\xmrig-maste
       r\build\xmrig.vcxproj]
         LINK : fatal error LNK1257: code generation failed [C:\Data\Stuff\XMRig\xmrig-master\build\xmrig.vcxproj]
```

# Discussion History
## xmrig | 2019-12-16T11:14:23+00:00
deps 4.0 works with Visual Studio 2019 16.**4**.x, seems you use earlier version.
Thank you.

## BKdilse | 2019-12-16T12:11:52+00:00
Definitely using Professional 2019.

EDIT: I'm on 16.3, let me update and try again.

## BKdilse | 2019-12-16T15:13:17+00:00
I can confirm, by updating VS 2019 to v16.4.1 has resolved the compile issue.

Thanks again for your prompt response, and guidance.

# Action History
- Created by: BKdilse | 2019-12-16T10:04:46+00:00
- Closed at: 2019-12-16T15:13:17+00:00
