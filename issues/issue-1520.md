---
title: '[PROPOSAL] Translations directory could be a git submodule'
source_url: https://github.com/monero-project/monero-gui/issues/1520
author: sanderfoobar
assignees: []
labels: []
created_at: '2018-07-25T05:03:05+00:00'
updated_at: '2018-07-30T10:51:03+00:00'
type: issue
status: closed
closed_at: '2018-07-30T01:56:44+00:00'
---

# Original Description
### what

Move `translations/` to it's own submodule.

### why

- Translation related issues/PRs will be detached from the monero-gui repo. This will create more breathing room for both parties.
- When it is its own repo, one may tailor it specifically for translations and provide documentation more effectively. Such a setup would be more comprehensible for GIT beginners, which translators often are **
- It could save luigi some merge work as @erciccione (or whoever would manage the repository), works independently.
- PRs will be merged faster**

** citation needed :-P

## cons

- For security, must ensure that only `*.ts` files will be modified during contributions. 
  - If necessary; an extra step could be taken that during the build process of `monero-gui` that removes any file that does not end with `(ts|md)`. 
- More moving parts in `monero-gui`. However, `monero` is already a submodule so adding one more should not be a problem.

All say aye' in favor.

```
< cryptochangement> I think that making translations a submodule is an excellent idea
```

# Discussion History
## sanderfoobar | 2018-07-30T01:56:44+00:00
I dont think anyone actually cares, closing :-P

## erciccione | 2018-07-30T10:51:03+00:00
Sorry i didn't have time to write a proper answer, will do it today. (i think it's a good idea, but i have some dubts)

# Action History
- Created by: sanderfoobar | 2018-07-25T05:03:05+00:00
- Closed at: 2018-07-30T01:56:44+00:00
