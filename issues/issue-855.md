---
title: License issue distributing XMRig binary linked with OpenSSL
source_url: https://github.com/xmrig/xmrig/issues/855
author: Low-power
assignees: []
labels:
- bug
created_at: '2018-10-30T02:28:58+00:00'
updated_at: '2021-04-12T15:55:32+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:55:32+00:00'
---

# Original Description
XMRig is under `GPL-3+`, which is incompatible with the OpenSSL license; without an OpenSSL linking exception from the copyright holder, then it seems that I have no right to distribute the XMRig binary if that is linked with OpenSSL libraries.

# Discussion History
## xmrig | 2018-10-30T04:36:01+00:00
Seems OpenSSL licensing is complicated thing, so what exactly I should do?
Thank you.

## Low-power | 2018-10-30T10:11:47+00:00
According to https://www.gnu.org/licenses/gpl-faq.html#GPLIncompatibleLibs the copyright holder can add a 'linking exception' via 'Additional Terms' in section 7 of GPL-3; thus allowing others to distribute binaries linked with OpenSSL.
However from 'README.md' I learned this program may be fork of cpuminer-multi (license GPL-2+); if so and the original author isn't you, all authors must agree as well to add such an additional term.

## xmrig | 2018-10-30T12:41:42+00:00
cpuminer-multi fork available in [classic](https://github.com/xmrig/xmrig/commits/classic) branch, since v1 miner was rewritten on C++/libuv instead of plain C.

## Low-power | 2018-10-30T13:42:48+00:00
So assume you are the only copyright holder of program, things now easier.

> If you wrote the whole program yourself, then assuming your employer or school does not claim the copyright, you are the copyright holder—so you can authorize the exception.

You can put the following texts to the license header of all sources files that you license under GPL-3 and/or the program's license information output:

> Additional permission under GNU GPL version 3 section 7

> If you modify this Program, or any covered work, by linking or combining it with OpenSSL, containing parts covered by the terms of OpenSSL license and SSLeay license, the licensors of this Program grant you additional permission to convey the resulting work. Corresponding Source for a non-source form of such a combination shall include the source code for the parts of OpenSSL used as well as that of the covered work.

Anyways it is your decision on how to grant this additional permission to others. See https://www.gnu.org/licenses/gpl-faq.html#GPLIncompatibleLibs for more information.


## Low-power | 2018-10-30T13:46:17+00:00
But still, make sure everyone in the copyright lines in all GPL licensed source files agree, before add such text.

# Action History
- Created by: Low-power | 2018-10-30T02:28:58+00:00
- Closed at: 2021-04-12T15:55:32+00:00
