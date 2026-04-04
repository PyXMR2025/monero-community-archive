---
title: Moneropedia links are not indicated as such.
source_url: https://github.com/monero-project/monero-site/issues/247
author: jonathancross
assignees: []
labels: []
created_at: '2017-04-06T18:11:37+00:00'
updated_at: '2017-05-08T07:40:29+00:00'
type: issue
status: closed
closed_at: '2017-05-08T07:40:29+00:00'
---

# Original Description
Internal links in the moneropedia are styled exactly like the text so there is no indication that they are clickable.  Example: https://getmonero.org/knowledge-base/moneropedia/block

The CSS class below forces them to grey:
```css
.moneropedia {
  color: #505050;
}
```

If this color property is simply removed, we get nice links again:

![moneropedia-links](https://cloud.githubusercontent.com/assets/5115470/24769006/24d5986e-1b05-11e7-9cfb-fa69e6113728.png)


# Discussion History
## anonimal | 2017-04-06T18:30:38+00:00
Why not PR the change?

## jonathancross | 2017-04-07T11:44:51+00:00
I'd love to, but have not found the CSS.

This message in the README suggests it is not possible:
> since all static content (CSS/JS/images) is hosted in a separate, non-public repository, changes can be suggested via Github issues and we will cross-apply them to that repo, crediting you in the commit message



## fluffypony | 2017-04-07T12:11:00+00:00
@jonathancross that's changed, someone should update the README. CSS is in the monero-forum repo.

## jonathancross | 2017-04-07T18:52:55+00:00
@fluffypony Found it, thanks!
Will send over some PRs to update the README and fix this issue.

# Action History
- Created by: jonathancross | 2017-04-06T18:11:37+00:00
- Closed at: 2017-05-08T07:40:29+00:00
