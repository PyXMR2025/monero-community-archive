---
title: Selected language not persisted on MacOS
source_url: https://github.com/monero-project/monero-gui/issues/246
author: ghost
assignees: []
labels: []
created_at: '2016-12-07T06:28:16+00:00'
updated_at: '2017-05-11T05:54:01+00:00'
type: issue
status: closed
closed_at: '2017-05-11T05:54:01+00:00'
---

# Original Description
Selecting a language in the language wizard page is not persisted on MacOS (tested with 10.11.6). The Qt settings are persisted in the MacOS user `defaults` with the domain `org.getmonero.monero-core`:

```
$ defaults read org.getmonero.monero-core
{
    ...
    locale = "en_US";
}
```

If I open the UI, change the language to German, and close the UI, the `locale` value is still `en_US`. Manually changing the `locale` value to `de` has the desired effect:

```
$ defaults write org.getmonero.monero-core locale de
```

The UI now uses the German translations.

This bug has also been reported in #164 

# Discussion History
## ghost | 2017-03-29T03:51:43+00:00
@maitscha Can this issue be closed?

# Action History
- Created by: ghost | 2016-12-07T06:28:16+00:00
- Closed at: 2017-05-11T05:54:01+00:00
