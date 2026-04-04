---
title: '[release-v0.17] Docker build failing'
source_url: https://github.com/monero-project/monero/issues/7015
author: jaredweinfurtner
assignees: []
labels: []
created_at: '2020-11-12T13:06:38+00:00'
updated_at: '2020-11-12T14:33:00+00:00'
type: issue
status: closed
closed_at: '2020-11-12T14:33:00+00:00'
---

# Original Description
**OS**: Ubuntu 18.04 LTS
**Version**: release-v0.17
**Command**: `docker build -t local/monero:20201112 .`

Fails at step 33/57:
```
Step 33/57 : RUN set -ex     && git clone https://github.com/gentoo/eudev -b ${UDEV_VERSION}     && cd eudev     && test `git rev-parse HEAD` = ${UDEV_HASH} || exit 1     && ./autogen.sh     && ./configure --disable-gudev --disable-introspection --disable-hwdb --disable-manpages --disable-shared     && make     && make install
 ---> Running in c20070c7cb9f
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
http://docbook.sourceforge.net/release/xsl/current/common/l10n.xsl:570: parser error : AttValue: ' expected
http://docbook.sourceforge.net/release/xsl/current/common/l10n.xsl:570: parser error : attributes construct error
http://docbook.sourceforge.net/release/xsl/current/common/l10n.xsl:570: parser error : Couldn't find end of Start Tag param line 570
http://docbook.sourceforge.net/release/xsl/current/common/l10n.xsl:570: parser error : Premature end of data in tag template line 567
http://docbook.sourceforge.net/release/xsl/current/common/l10n.xsl:570: parser error : Premature end of data in tag stylesheet line 2
compilation error: file http://docbook.sourceforge.net/release/xsl/current/html/docbook.xsl line 26 element include
xsl:include : unable to load http://docbook.sourceforge.net/release/xsl/current/common/l10n.xsl
http://docbook.sourceforge.net/release/xsl/current/common/utility.xsl:262: parser error : Couldn't find end of Start Tag when line 262
http://docbook.sourceforge.net/release/xsl/current/common/utility.xsl:262: parser error : Premature end of data in tag choose line 261
http://docbook.sourceforge.net/release/xsl/current/common/utility.xsl:262: parser error : Premature end of data in tag template line 254
http://docbook.sourceforge.net/release/xsl/current/common/utility.xsl:262: parser error : Premature end of data in tag stylesheet line 2
compilation error: file http://docbook.sourceforge.net/release/xsl/current/html/docbook.xsl line 28 element include
xsl:include : unable to load http://docbook.sourceforge.net/release/xsl/current/common/utility.xsl
http://docbook.sourceforge.net/release/xsl/current/html/lists.xsl:1276: parser error : StartTag: invalid element name
http://docbook.sourceforge.net/release/xsl/current/html/lists.xsl:1276: parser error : Premature end of data in tag template line 1274
http://docbook.sourceforge.net/release/xsl/current/html/lists.xsl:1276: parser error : Premature end of data in tag stylesheet line 2
compilation error: file http://docbook.sourceforge.net/release/xsl/current/html/docbook.xsl line 38 element include
xsl:include : unable to load http://docbook.sourceforge.net/release/xsl/current/html/lists.xsl
http://docbook.sourceforge.net/release/xsl/current/html/htmltbl.xsl:117: parser error : AttValue: ' expected
http://docbook.sourceforge.net/release/xsl/current/html/htmltbl.xsl:117: parser error : attributes construct error
http://docbook.sourceforge.net/release/xsl/current/html/htmltbl.xsl:117: parser error : Couldn't find end of Start Tag when line 117
http://docbook.sourceforge.net/release/xsl/current/html/htmltbl.xsl:117: parser error : Premature end of data in tag choose line 114
http://docbook.sourceforge.net/release/xsl/current/html/htmltbl.xsl:117: parser error : Premature end of data in tag attribute line 112
http://docbook.sourceforge.net/release/xsl/current/html/htmltbl.xsl:117: parser error : Premature end of data in tag template line 111
http://docbook.sourceforge.net/release/xsl/current/html/htmltbl.xsl:117: parser error : Premature end of data in tag stylesheet line 2
compilation error: file http://docbook.sourceforge.net/release/xsl/current/html/docbook.xsl line 45 element include
xsl:include : unable to load http://docbook.sourceforge.net/release/xsl/current/html/htmltbl.xsl
http://docbook.sourceforge.net/release/xsl/current/html/its.xsl:89: parser error : Premature end of data in tag template line 87
http://docbook.sourceforge.net/release/xsl/current/html/its.xsl:89: parser error : Premature end of data in tag stylesheet line 2
compilation error: file http://docbook.sourceforge.net/release/xsl/current/html/docbook.xsl line 50 element include
xsl:include : unable to load http://docbook.sourceforge.net/release/xsl/current/html/its.xsl
http://docbook.sourceforge.net/release/xsl/current/html/keywords.xsl:30: parser error : AttValue: ' expected
http://docbook.sourceforge.net/release/xsl/current/html/keywords.xsl:30: parser error : attributes construct error
http://docbook.sourceforge.net/release/xsl/current/html/keywords.xsl:30: parser error : Couldn't find end of Start Tag if line 30
http://docbook.sourceforge.net/release/xsl/current/html/keywords.xsl:30: parser error : Premature end of data in tag template line 28
http://docbook.sourceforge.net/release/xsl/current/html/keywords.xsl:30: parser error : Premature end of data in tag stylesheet line 2
compilation error: file http://docbook.sourceforge.net/release/xsl/current/html/docbook.xsl line 52 element include
xsl:include : unable to load http://docbook.sourceforge.net/release/xsl/current/html/keywords.xsl
http://docbook.sourceforge.net/release/xsl/current/html/division.xsl:203: parser error : Specification mandate value for attribute n
http://docbook.sourceforge.net/release/xsl/current/html/division.xsl:203: parser error : attributes construct error
http://docbook.sourceforge.net/release/xsl/current/html/division.xsl:203: parser error : Couldn't find end of Start Tag with-param line 203
http://docbook.sourceforge.net/release/xsl/current/html/division.xsl:203: parser error : Premature end of data in tag call-template line 201
http://docbook.sourceforge.net/release/xsl/current/html/division.xsl:203: parser error : Premature end of data in tag h1 line 199
http://docbook.sourceforge.net/release/xsl/current/html/division.xsl:203: parser error : Premature end of data in tag template line 196
http://docbook.sourceforge.net/release/xsl/current/html/division.xsl:203: parser error : Premature end of data in tag stylesheet line 2
compilation error: file http://docbook.sourceforge.net/release/xsl/current/html/docbook.xsl line 53 element include
xsl:include : unable to load http://docbook.sourceforge.net/release/xsl/current/html/division.xsl
http://docbook.sourceforge.net/release/xsl/current/html/annotations.xsl:159: parser error : Specification mandate value for attribute t
http://docbook.sourceforge.net/release/xsl/current/html/annotations.xsl:159: parser error : attributes construct error
http://docbook.sourceforge.net/release/xsl/current/html/annotations.xsl:159: parser error : Couldn't find end of Start Tag when line 159
http://docbook.sourceforge.net/release/xsl/current/html/annotations.xsl:159: parser error : Premature end of data in tag choose line 158
http://docbook.sourceforge.net/release/xsl/current/html/annotations.xsl:159: parser error : Premature end of data in tag div line 157
http://docbook.sourceforge.net/release/xsl/current/html/annotations.xsl:159: parser error : Premature end of data in tag template line 156
http://docbook.sourceforge.net/release/xsl/current/html/annotations.xsl:159: parser error : Premature end of data in tag stylesheet line 2
compilation error: file http://docbook.sourceforge.net/release/xsl/current/html/docbook.xsl line 73 element include
xsl:include : unable to load http://docbook.sourceforge.net/release/xsl/current/html/annotations.xsl
http://docbook.sourceforge.net/release/xsl/current/manpages/utility.xsl:545: parser error : Couldn't find end of Start Tag va line 545
http://docbook.sourceforge.net/release/xsl/current/manpages/utility.xsl:545: parser error : Premature end of data in tag template line 542
http://docbook.sourceforge.net/release/xsl/current/manpages/utility.xsl:545: parser error : Premature end of data in tag stylesheet line 2
compilation error: file http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl line 31 element include
xsl:include : unable to load http://docbook.sourceforge.net/release/xsl/current/manpages/utility.xsl
http://docbook.sourceforge.net/release/xsl/current/manpages/lists.xsl:595: parser error : StartTag: invalid element name
http://docbook.sourceforge.net/release/xsl/current/manpages/lists.xsl:595: parser error : Premature end of data in tag stylesheet line 2
compilation error: file http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl line 38 element include
xsl:include : unable to load http://docbook.sourceforge.net/release/xsl/current/manpages/lists.xsl
The command '/bin/sh -c set -ex     && git clone https://github.com/gentoo/eudev -b ${UDEV_VERSION}     && cd eudev     && test `git rev-parse HEAD` = ${UDEV_HASH} || exit 1     && ./autogen.sh     && ./configure --disable-gudev --disable-introspection --disable-hwdb --disable-manpages --disable-shared     && make     && make install' returned a non-zero code: 5
```


# Discussion History
## jaredweinfurtner | 2020-11-12T13:34:03+00:00
Shouldn't the `--disable-manpages` prevent all of doc building?


## jaredweinfurtner | 2020-11-12T14:33:00+00:00
Seemed as though there was an issue with sourceforge.net.  I switched to a USA VPN and it worked no issue.  

# Action History
- Created by: jaredweinfurtner | 2020-11-12T13:06:38+00:00
- Closed at: 2020-11-12T14:33:00+00:00
