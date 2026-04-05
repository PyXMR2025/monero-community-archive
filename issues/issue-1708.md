---
title: How to remove the display of the program name at the top of the running window?
source_url: https://github.com/xmrig/xmrig/issues/1708
author: etsam
assignees: []
labels:
- enhancement
created_at: '2020-06-04T01:21:27+00:00'
updated_at: '2020-08-19T01:20:29+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:20:29+00:00'
---

# Original Description
May I ask the latest 5.11.2 version How to delete the XMRING+version number at the top of the running window?

After editing with resource_hacker, you can only modify the file attributes and remove the LOGO, and cannot delete the program name on the window, but version 5.3.0 does not have this trouble. Is there any way to remove it? Thank you!
![818](https://user-images.githubusercontent.com/24689501/83705347-42185080-a647-11ea-9a72-6859e4418d50.png)




# Discussion History
## xmrig | 2020-06-05T17:31:25+00:00
Without change source code is not possible remove this title.

Next beta version (6.0.1) will support `title` option (code already in evo branch) with following values:
* `"title": true` current behavior, default title: miner name + version.
* `"title": false` or `--no-title` disable this feature, same as old versions.
* `"title": "Custom title"` or `--title "Custom title"`.

## alex-s-m | 2020-06-29T05:31:07+00:00
а нельзя ли такую же опцию и для xmrig-proxy?

# Action History
- Created by: etsam | 2020-06-04T01:21:27+00:00
- Closed at: 2020-08-19T01:20:29+00:00
