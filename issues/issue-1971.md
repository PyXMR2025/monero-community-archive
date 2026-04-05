---
title: Cannot disable fee option
source_url: https://github.com/xmrig/xmrig/issues/1971
author: RedxLus
assignees: []
labels: []
created_at: '2020-12-08T17:01:33+00:00'
updated_at: '2020-12-09T15:47:36+00:00'
type: issue
status: closed
closed_at: '2020-12-09T15:47:36+00:00'
---

# Original Description
**Describe the bug**
The fee option cannot be disabled when the code is built from source

**To Reproduce**
Follow https://xmrig.com/docs/miner/build/windows and edit xmrig ->src -> donate.h

`constexpr const int kDefaultDonateLevel = 0;`
`constexpr const int kMinimumDonateLevel = 0;`


**Expected behavior**
That my earnings do not have that wave. I want to make a donation but I need to see my earnings on a stable basis.

![n](https://user-images.githubusercontent.com/15265490/101516078-57b45d00-397f-11eb-9ba0-beee99609346.png)



# Discussion History
## Lonnegan | 2020-12-09T08:37:52+00:00
Funny. You complain to the developer of the software that you cannot deactivate the developer fee. ROFL

## RedxLus | 2020-12-09T15:31:49+00:00
> Funny. You complain to the developer of the software that you cannot deactivate the developer fee. ROFL

Of course. This program is under the GNU General Public License v3.0. So changes can be made to the source code. If a change is made and it doesn't work as it should, it's called a bug. That is precisely why it is called open source.

## SChernykh | 2020-12-09T15:37:05+00:00
You probably need to edit your config.json too

# Action History
- Created by: RedxLus | 2020-12-08T17:01:33+00:00
- Closed at: 2020-12-09T15:47:36+00:00
