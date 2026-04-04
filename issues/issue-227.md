---
title: 'Wallet2: store wallet path as UTF-16 on windows. '
source_url: https://github.com/monero-project/monero-gui/issues/227
author: Jaqueeee
assignees: []
labels: []
created_at: '2016-11-29T16:35:09+00:00'
updated_at: '2016-11-29T16:36:28+00:00'
type: issue
status: closed
closed_at: '2016-11-29T16:36:28+00:00'
---

# Original Description
On Windows, wallet path need to be saved in UTF-16 to support non-ascii characters. https://github.com/monero-project/monero-core/issues/199

Proposed solution:
- Convert input strings from UTF-8 -> UTF-16 
- Port all std/boost::fstream to windows CreateFile() that accepts UTF-16 wchar_t as input

boost::fstream supports wstring input but not with Mingw:
https://svn.boost.org/trac/boost/ticket/9968

lmdb already solved this:
https://github.com/monero-project/monero/blob/master/external/db_drivers/liblmdb/mdb.c#L4802-L4810


# Discussion History
## Jaqueeee | 2016-11-29T16:36:28+00:00
wrong project :p

# Action History
- Created by: Jaqueeee | 2016-11-29T16:35:09+00:00
- Closed at: 2016-11-29T16:36:28+00:00
