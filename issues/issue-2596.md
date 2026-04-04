---
title: 'First run: welcome page should be skipped after selecting language'
source_url: https://github.com/monero-project/monero-gui/issues/2596
author: rating89us
assignees: []
labels: []
created_at: '2019-12-15T16:55:44+00:00'
updated_at: '2019-12-20T04:46:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When Monero GUI runs for the first time and the user wants to change the language, four pages are being displayed before opening the main menu:
1) Welcome page (Language button + Continue button): click Language button
2) Language select page: click flag to select page
3) Welcome page again (Language button + Continue button): click Continue button
4) Mode selection page

But only three pages are necessary:
1) Welcome page (Language button + Continue button): click Language button
2) Language select page: click flag to select page
3) Mode selection page


# Discussion History
# Action History
- Created by: rating89us | 2019-12-15T16:55:44+00:00
