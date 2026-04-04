---
title: Downloads page should have a source tarball
source_url: https://github.com/monero-project/monero-site/issues/902
author: erciccione
assignees: []
labels:
- downloads
- feature
created_at: '2020-04-12T09:06:31+00:00'
updated_at: '2021-05-04T16:57:47+00:00'
type: issue
status: closed
closed_at: '2021-05-04T16:57:47+00:00'
---

# Original Description
*Issue originally created by @asymptotically*

*This issue was created on gitlab and then migrated here. Only the original post was migrated, not the comments. Please take a look at the discussions on the original Gitlab issue before commenting here: https://repo.getmonero.org/monero-project/monero-site/-/issues/993*

---
It would be nice if the website had a tarball of the Monero source instead of directing users to GitHub. The tarballs and zips on GitHub release pages do not include submodules and cannot be used.

# Discussion History
## 00-matt | 2020-04-13T09:37:11+00:00
>We've always had a source tarball. It's used by the auto-updater when you build from source (instead of using a release). Here are the list of current tarballs in the downloads.getmonero.org/source/ directory -
>
>monero-gui-source-v0.11.0.0.tar.bz2
monero-gui-source-v0.15.0.1.tar.bz2
monero-source-v0.11.0.0.tar.bz2
monero-source-v0.11.1.0.tar.bz2
monero-source-v0.12.0.0.tar.bz2
monero-source-v0.12.3.0.tar.bz2
monero-source-v0.13.0.0.tar.bz2
monero-source-v0.13.0.1.tar.bz2
monero-source-v0.13.0.2.tar.bz2
monero-source-v0.13.0.4.tar.bz2
monero-source-v0.14.0.0.tar.bz2
monero-source-v0.14.0.2.tar.bz2
monero-source-v0.14.1.0.tar.bz2
monero-source-v0.14.1.2.tar.bz2
monero-source-v0.15.0.0.tar.bz2
monero-source-v0.15.0.1.tar.bz2
> -- https://repo.getmonero.org/monero-project/monero-site/-/issues/993#note_7760

I think it would be easy enough to add a link to these on the download page, but their checksums are not included in the signed `hashes.txt` file.

# Action History
- Created by: erciccione | 2020-04-12T09:06:31+00:00
- Closed at: 2021-05-04T16:57:47+00:00
