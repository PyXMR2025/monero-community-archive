---
title: 'Inconsistent language code: Esperanto flag uses full name instead of ISO 639-1
  code ‘eo’'
source_url: https://github.com/monero-project/monero-gui/issues/4383
author: BaksiLi
assignees: []
labels: []
created_at: '2024-12-12T01:01:23+00:00'
updated_at: '2025-02-27T19:11:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The language flag for Esperanto (`lang/flags/esperanto.png`) is inconsistently named compared to other language flags in the same directory.

Current state:
- File is named `esperanto.png` (full language name)
- Other language flags use ISO 639-1 two-letter codes (e.g., `gb.png`, `fr.png`)

Expected state:
- File should be named `eo.png` (using ISO 639-1 code for Esperanto)

Reference:
- ISO 639-1 code for Esperanto is "eo"
- [ISO 639-1 Language Codes Reference](https://www.loc.gov/standards/iso639-2/php/English_list.php)



# Discussion History
## BaksiLi | 2024-12-12T02:20:58+00:00
BTW, https://translate.getmonero.org/engage/monero/ seems down, Error 502

## jermanuts | 2025-02-27T19:11:46+00:00
Yes, this issue have been for years, no one stepped up to fix Weblate yet.

# Action History
- Created by: BaksiLi | 2024-12-12T01:01:23+00:00
