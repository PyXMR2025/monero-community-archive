---
title: Redesign and 301 redirects
source_url: https://github.com/monero-project/monero-site/issues/290
author: peronero
assignees: []
labels: []
created_at: '2017-06-30T17:06:54+00:00'
updated_at: '2017-07-06T19:43:01+00:00'
type: issue
status: closed
closed_at: '2017-07-06T19:43:01+00:00'
---

# Original Description
Issue to flag that to ensure retaining "SEO juice" and avoid breaking external links where someone has linked to an old page, the site will need 301 redirects in place when the redesign goes live, from old URLs to new ones and/or pertinent pages where pages have been consolidated and/or deprecated. 

This is typically done by cataloging existing pages and mapping them to the new ones, and implemented in the configs in the webserver but can also be done via META refresh tags in placeholder pages as a crude hack.


# Discussion History
## rehrar | 2017-07-04T18:57:26+00:00
/knowledge-base/user-guides -> /resources/user-guides
/knowledge-base/developer-guides -> /resources/developer-guides
/knowledge-base/moneropedia -> /resources/moneropedia
/getting-started/contribute.html -> /get-started/contributing/
/getting-started/accepting.html -> /get-started/accepting/
/getting-started/merchants.html -> /community/merchants/
/getting-started/running.html -> /get-started/using/
/knowledge-base/people.html -> /community/team/
/knowledge-base/open-alias.html -> /the-monero-project/
/knowledge-base/about.html -> /resources/about/


## ghost | 2017-07-05T18:09:30+00:00
I would suggest adding a 301 from /home to /. It appears a few sites, including [Monero Blocks](https://moneroblocks.info/richlist), link directly to /home instead of the root.

## fluffypony | 2017-07-06T19:43:01+00:00
Done, nginx config below:

```
    rewrite ^/home / permanent;
    rewrite ^/knowledge-base/user-guides /resources/user-guides permanent;
    rewrite ^/knowledge-base/developer-guides /resources/developer-guides permanent;
    rewrite ^/knowledge-base/moneropedia /resources/moneropedia permanent;
    rewrite ^/getting-started/donate /get-started/contributing/ permanent;
    rewrite ^/getting-started/accepting /get-started/accepting/ permanent;
    rewrite ^/getting-started/merchants /community/merchants/ permanent;
    rewrite ^/getting-started/running /get-started/using/ permanent;
    rewrite ^/knowledge-base/people /community/team/ permanent;
    rewrite ^/knowledge-base/open-alias /the-monero-project/ permanent;
    rewrite ^/knowledge-base/about /resources/about/ permanent;
```

# Action History
- Created by: peronero | 2017-06-30T17:06:54+00:00
- Closed at: 2017-07-06T19:43:01+00:00
