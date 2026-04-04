---
title: Bintray is retired - Dockerfile.linux, android has broken bintray URL
source_url: https://github.com/monero-project/monero-gui/issues/3389
author: roundtheworldman
assignees: []
labels: []
created_at: '2021-04-12T17:56:09+00:00'
updated_at: '2021-04-29T18:16:20+00:00'
type: issue
status: closed
closed_at: '2021-04-29T18:16:20+00:00'
---

# Original Description
FYI Bintray is retired / sunset. I don't know all the details, but they have some info on this page.

This is effecting boost dependency @selsta @xiphon.

https://jfrog.com/blog/into-the-sunset-bintray-jcenter-gocenter-and-chartcenter/

> "April 12th, 26th, 2021 | We will have some short service  brown-outs to remind users about the services that are going away on May  1st. (Specific hours will be advertised in the Bintray status page.)"

> "May 1st, 2021 | Bintray services will no longer be  available. GoCenter, and ChartCenter services will no longer be available to non-Artifactory clients. (ConanCenter is not affected)."

`Dockerfile.linux` and `Dockerfile.android` contains lines like this:

```
RUN apt install -y wget && \
    wget https://dl.bintray.com/boostorg/release/1.73.0/source/boost_1_73_0.tar.gz && \
```

So trying to use, for example `Dockerfile.linux` results in 403 Forbidden errors like this now:
```
Selecting previously unselected package wget.
(Reading database ... 16223 files and directories currently installed.)
Preparing to unpack .../wget_1.17.1-1ubuntu1.5_amd64.deb ...
Unpacking wget (1.17.1-1ubuntu1.5) ...
Setting up wget (1.17.1-1ubuntu1.5) ...
--2021-04-12 17:41:11--  https://dl.bintray.com/boostorg/release/1.73.0/source/boost_1_73_0.tar.gz
Resolving dl.bintray.com (dl.bintray.com)... 35.156.125.116, 18.158.131.58
Connecting to dl.bintray.com (dl.bintray.com)|35.156.125.116|:443... connected.
HTTP request sent, awaiting response... 403 Forbidden
2021-04-12 17:41:11 ERROR 403: Forbidden.
```

# Discussion History
## roundtheworldman | 2021-04-12T18:00:04+00:00
May be a suitable replacement archive here:
https://github.com/boostorg/boost/archive/refs/tags/boost-1.73.0.tar.gz

More info:
https://github.com/boostorg/boost/releases 

# Action History
- Created by: roundtheworldman | 2021-04-12T17:56:09+00:00
- Closed at: 2021-04-29T18:16:20+00:00
