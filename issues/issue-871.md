---
title: '@lang_tag_(en,es,fr,it,pl,ar) showing while building with jekyll'
source_url: https://github.com/monero-project/monero-site/issues/871
author: lh1008
assignees: []
labels: []
created_at: '2018-09-04T15:19:18+00:00'
updated_at: '2020-04-07T09:45:21+00:00'
type: issue
status: closed
closed_at: '2020-04-07T09:45:21+00:00'
---

# Original Description
Hi guys,

I caught the tag while building the website through jekyll. I thought I had messed something up (I hadn't done anything, but was about too), so I erased my fork and did a clean clone in a different directory using the direct url(https://github.com/monero-project/monero-site.git)  and found out that the tag was still showing up. I showed this to @el00ruobuob and now creating the issue. I was not able to fix it, I'm still learning how to work through the website code. 

The tag is displaying in the "Recent News/All posts"(http://127.0.0.1:4000/blog/) and in the "Press-kit" (http://127.0.0.1:4000/press-kit/) sections and all languages are displaying the same issue. 

http://127.0.0.1:4000/es/blog/ - @lang_tag_es
http://127.0.0.1:4000/it/blog/ - @lang_tag_it
http://127.0.0.1:4000/pl/blog/ - @lang_tag_pl
http://127.0.0.1:4000/fr/blog/ - @lang_tag_fr
http://127.0.0.1:4000/ar/blog/ - @lang_tag_ar

http://127.0.0.1:4000/es/press-kit/ - @lang_tag_es
http://127.0.0.1:4000/it/press-kit/ - @lang_tag_it
http://127.0.0.1:4000/pl/press-kit/ - @lang_tag_pl
http://127.0.0.1:4000/fr/press-kit/ - @lang_tag_fr
http://127.0.0.1:4000/ar/press-kit/ - @lang_tag_ar

I will share the images of the en and other two languages, blog and press-kit, sections so you can see the tag. In the blog section, is in the center just above the first log, and in the press-kit, displays itself in the left side of the screen, just below "Monero Press Kit".

![en_blog](https://user-images.githubusercontent.com/7443480/45039956-6f773b00-b02a-11e8-8c60-36106bed16cf.png)

![es_blog](https://user-images.githubusercontent.com/7443480/45039966-743bef00-b02a-11e8-88fe-12d4f6d27583.png)

![en_press](https://user-images.githubusercontent.com/7443480/45040464-af8aed80-b02b-11e8-8c5e-bfa113f100c5.png)

![fr_press](https://user-images.githubusercontent.com/7443480/45040475-b285de00-b02b-11e8-9d0f-37c25a59ab60.png)


Thank you a lot for your reading.

# Discussion History
## el00ruobuob | 2018-09-04T15:23:28+00:00
Should be solved by #869

# Action History
- Created by: lh1008 | 2018-09-04T15:19:18+00:00
- Closed at: 2020-04-07T09:45:21+00:00
