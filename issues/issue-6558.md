---
title: 'Dockerfile: issue building eudev'
source_url: https://github.com/monero-project/monero/issues/6558
author: ghost
assignees: []
labels: []
created_at: '2020-05-19T07:42:05+00:00'
updated_at: '2022-02-19T04:35:45+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:35:44+00:00'
---

# Original Description
Building master with Docker yields:

```
Step 33/57 : RUN set -ex     && git clone https://github.com/gentoo/eudev -b ${UDEV_VERSION}     && cd eudev     && test `git rev-parse HEAD` = ${UDEV_HASH} || exit 1     && ./autogen.sh     && ./configure --disable-gudev --disable-introspection --disable-hwdb --disable-manpages --disable-shared     && make     && make install
 ---> Running in 6f2dec5b225d
+ git clone https://github.com/gentoo/eudev -b v3.2.8
Cloning into 'eudev'...
Note: checking out 'd69f3f28348123ab7fa0ebac63ec2fd16800c5e0'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

+ cd eudev
+ git rev-parse HEAD
+ test d69f3f28348123ab7fa0ebac63ec2fd16800c5e0 = d69f3f28348123ab7fa0ebac63ec2fd16800c5e0
+ ./autogen.sh
libtoolize: putting auxiliary files in '.'.
libtoolize: linking file './ltmain.sh'
libtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'm4'.
libtoolize: linking file 'm4/libtool.m4'
libtoolize: linking file 'm4/ltoptions.m4'
libtoolize: linking file 'm4/ltsugar.m4'
libtoolize: linking file 'm4/ltversion.m4'
libtoolize: linking file 'm4/lt~obsolete.m4'
configure.ac:6: installing './compile'
configure.ac:17: installing './config.guess'
configure.ac:17: installing './config.sub'
configure.ac:13: installing './install-sh'
configure.ac:13: installing './missing'
src/ata_id/Makefile.am: installing './depcomp'
parallel-tests: installing './test-driver'
http://docbook.sourceforge.net/release/xsl/current/html/titlepage.xsl:1: parser error : Document is empty
compilation error: file http://docbook.sourceforge.net/release/xsl/current/html/docbook.xsl line 67 element include
xsl:include : unable to load http://docbook.sourceforge.net/release/xsl/current/html/titlepage.xsl
The command '/bin/sh -c set -ex     && git clone https://github.com/gentoo/eudev -b ${UDEV_VERSION}     && cd eudev     && test `git rev-parse HEAD` = ${UDEV_HASH} || exit 1     && ./autogen.sh     && ./configure --disable-gudev --disable-introspection --disable-hwdb --disable-manpages --disable-shared     && make     && make install' returned a non-zero code: 5
```

# Discussion History
## moneromooo-monero | 2020-05-19T12:16:38+00:00
That looks like a transient error, the file is not empty when I get it here.

## ghost | 2020-05-19T14:28:57+00:00
Hm, tried to build the Dockerfile again, didn't work. Tried a different machine, same error. Grabbing the document with a browser does work. Then I ran requests through a HTTP proxy to see what it was doing, and then it worked.

I did notice one thing: it grabs 411 individual documents from docbook.sourceforge.net, taking nearly 5 minutes. That seems a bit inefficient. Maybe there is a flag that can be added to configure to optimize this?

## moneromooo-monero | 2020-05-19T14:51:08+00:00
Maybe some kind of limiter on sourceforge.net then. I'll leave answering the rest to someome who actually knows about docker :)

## normoes | 2020-08-05T10:44:25+00:00
I ran into the same issue today. Unfortunately not resolving itself.

I can also grab the files in a browser, but the builds fail all the time.


## normoes | 2020-08-06T15:52:18+00:00
I could resolve the issue by installing `docbook-xsl`.

Not sure why it worked before or was not working anymore, respectively

## selsta | 2022-02-19T04:35:44+00:00
Dockerfile has been updated.

# Action History
- Created by: ghost | 2020-05-19T07:42:05+00:00
- Closed at: 2022-02-19T04:35:44+00:00
