---
title: Fix currency amount formatting
source_url: https://github.com/monero-project/monero-site/issues/2163
author: getsnoopy
assignees: []
labels: []
created_at: '2023-05-06T23:47:19+00:00'
updated_at: '2024-07-09T10:17:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It seems like throughout the website (and the videos), currency amounts are formatted with the quantity first and the currency code following it (e.g., `5 XMR`), [which is incorrect](https://en.wikipedia.org/wiki/ISO_4217#Code_position_in_amount_formatting). In English, all currency amounts are formatted with currency symbols and codes which precede the quantity, with symbols being unspaced (e.g., `$5`, `US$5`) and codes being spaced (e.g., `USD 5`). Seeing as the homepage itself says "It's a Currency: Use It!", this should be fixed so that it's consistent with all other currencies.

# Discussion History
## erciccione | 2023-05-07T08:27:54+00:00
Usually, the currency symbol user for Monero (ɱ) is used the ways you suggest (e.g. `ɱ1.5`). Considering that English is the only major language using code first and sum after, while all the other major latin languages put the amount first and the code after (so we would need to use a structure for english and a different structure for all other languages), i would just stick with the current structure, which is also the most commonly used.

## getsnoopy | 2023-05-07T15:01:08+00:00
Well it is incorrect in English, so it should be fixed (in the same way Arabic is the only major RTL language in the languages we support, but we wouldn't be using LTR for it just because every other language doesn't use it). There wouldn't need to be a different "structure" at all; we could just have an i18n entry that provides the correct formatted currency for the current language, which would have `XMR %s` or the like for English and other languages which use this format, and `%s XMR` for the rest.

## erciccione | 2023-05-08T11:50:29+00:00
Even if not technically correct for the English language, `N XMR` is the most commonly used structure and immediately recognized by most, so we could keep it as it is. Even more so if we consider that the current structure is already correct for all languages except English. If this is considered an issue worth working on, PRs are welcome.

## plowsof | 2024-07-09T10:17:25+00:00
ive just assumed "N XMR" or "ɱXMR" is universal for all cryptocurrencies / hadn't given it much thought

# Action History
- Created by: getsnoopy | 2023-05-06T23:47:19+00:00
