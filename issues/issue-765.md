---
title: Display descriptive titles on guide pages
source_url: https://github.com/monero-project/monero-site/issues/765
author: apertamono
assignees: []
labels: []
created_at: '2018-06-13T11:52:52+00:00'
updated_at: '2020-04-07T09:39:00+00:00'
type: issue
status: closed
closed_at: '2020-04-07T09:39:00+00:00'
---

# Original Description
The Developer Guides and many of the User Guides do not show at the top of the page which question they're answering. They start either without any heading, with a subheader like **Introduction** or with a summary of the question, like **Prove payments**. It's confusing that these pages don't clearly show what they're about, especially when new users are given a direct link to one of these pages to answer a question.

There is a title element which is used for the `<TITLE>` tag, but this is hardly visible in a modern tabbed browser or a mobile browser. @rehrar Could you use the same text in a visible `<H1>` or `<H2>` tag at the top of each page?

Such a change is conveniently beyond my capabilities, but I guess I could clean up any duplicate titles that resulted from this.

# Discussion History
## el00ruobuob | 2018-06-13T13:12:41+00:00
It could be usefull. That's something to add into the layout i believe, as it is done for blog posts. I could try to look at this later.

## rehrar | 2018-06-15T16:18:54+00:00
This will require a separate layout. I'll work on making it happen.

## erciccione | 2020-04-07T09:39:00+00:00
This issue is old and was discussed and closed on gitlab. Please reopen if you feel it's still relevant.

# Action History
- Created by: apertamono | 2018-06-13T11:52:52+00:00
- Closed at: 2020-04-07T09:39:00+00:00
