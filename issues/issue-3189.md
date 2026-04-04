---
title: link to monero hashes.txt outdated
source_url: https://github.com/monero-project/monero-gui/issues/3189
author: adrelanos
assignees: []
labels: []
created_at: '2020-10-22T11:06:44+00:00'
updated_at: '2021-01-17T16:57:58+00:00'
type: issue
status: closed
closed_at: '2021-01-17T16:57:57+00:00'
---

# Original Description
`https://web.archive.org/web/20201022105210/https://github.com/monero-project/monero-gui/releases/tag/v0.17.1.1` links to `https://getmonero.org/downloads/hashes.txt` which then redirects to `https://web.getmonero.org/downloads/hashes.txt`.

This makes it a bit harder to web archive these links.

If the location change is permanent, please consider updating that link for the next release.

# Discussion History
## xiphon | 2021-01-15T11:05:33+00:00
Please submit this to https://github.com/monero-project/monero-site/ repository.

## adrelanos | 2021-01-15T11:11:38+00:00
https://github.com/monero-project/monero-site/issues/1419

## xiphon | 2021-01-15T11:16:32+00:00
Thanks.

## erciccione | 2021-01-15T11:39:43+00:00
This is unrelated to monero-site, since it's about the github release notes: https://github.com/monero-project/monero-gui/releases/tag/v0.17.1.1 

We correctly link to `www.getmonero` from the blog posts (even if the URL displayed is `https://getmonero.org/downloads/hashes.txt `, and yes, that should be fixed regardless)

## xiphon | 2021-01-15T11:44:20+00:00
> This is unrelated to monero-site, since it's about the github release notes: https://github.com/monero-project/monero-gui/releases/tag/v0.17.1.1

@adrelanos  @erciccione 

Sorry, i misread web archive URL, thought it was getmonero.org page cache.

Reopened.

## erciccione | 2021-01-15T11:44:31+00:00
@selsta @binaryfate FYI ^ the link in the release notes will need to be fixed in the future

## binaryFate | 2021-01-15T20:40:23+00:00
Opinion on updating the link to `https://web.getmonero.org/downloads/hashes.txt` in latest release (v0.17.1.9) notes?
(I wouldn't edit older ones at this stage anyway).

## xiphon | 2021-01-15T22:47:06+00:00
We just change the link, not the hashes, thus sounds good to me.

## erciccione | 2021-01-16T08:37:47+00:00
> Opinion on updating the link to https://web.getmonero.org/downloads/hashes.txt in latest release (v0.17.1.9) notes?

The correct url is `https://www.getmonero.org/downloads/hashes.txt` and yes, sounds good to me as well.

## binaryFate | 2021-01-16T14:57:55+00:00
> The correct url is `https://www.getmonero.org/downloads/hashes.txt` and yes, sounds good to me as well.

Thanks, done

## erciccione | 2021-01-17T16:57:57+00:00
Hashes are fixed. I'd say this is resolved.

# Action History
- Created by: adrelanos | 2020-10-22T11:06:44+00:00
- Closed at: 2021-01-17T16:57:57+00:00
