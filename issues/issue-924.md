---
title: Change emoji icons to something more consistent
source_url: https://github.com/monero-project/monero-site/issues/924
author: erciccione
assignees: []
labels:
- 💬 discussion
created_at: '2020-04-12T09:42:39+00:00'
updated_at: '2021-05-22T02:40:27+00:00'
type: issue
status: closed
closed_at: '2021-05-22T02:40:27+00:00'
---

# Original Description
*This issue was created on gitlab and then migrated here. Only the original post was migrated, not the comments. Please take a look at the discussions on the original Gitlab issue before commenting here: https://repo.getmonero.org/monero-project/monero-site/-/issues/1075*

---
Emojis look different on each device and some can be ugly (for example the check on Chrome appears grey). Right now we use emojis for the developer guides page, FAQ and roadmap.

The options could be:

- Change emojis
- Use minimal black and white icons (https://icons.getbootstrap.com was pointed out as a possibility)
- Use pics (option that i discarded initially to not make the page heavier)
- https://primer.style/octicons/ (can be integrated with jekyll)

Voice your opinion.

# Discussion History
## ghost | 2021-04-05T22:48:04+00:00
So I think this is the complete list of what needs to be replaced.
`grep -rIE '"\\0.+"' monero-site/`

> monero-site/css/custom.css:  content: "\02714";
> monero-site/css/custom.css:  content: "\01F6A7";
> monero-site/css/custom.css:  content: "\01F9ED";
> monero-site/css/custom.css:  content: "\01F4C4";
> monero-site/css/custom.css:  content: "\01F310";
> monero-site/css/custom.css:  content: "\02714";
> monero-site/css/custom.css:  content: "\01F6A7";
> monero-site/css/custom.css:  content: "\01F9ED";

I suggest using SVGs from [OpenMoji](https://openmoji.org/). They're nice and can be downloaded separately too. Each comes with a black and white version, although I think pages like the roadmap look better with the colored ones. I think we should use only one source for consistency (eg. not a little from bootstrap and a little from openmoji), but the roadmap page + black and white bootstrap icons looks ugly and boring imo. Here's how it would look with openmojis.

![screen](https://user-images.githubusercontent.com/81592644/113634861-d7251500-966f-11eb-90b5-cf5936206253.jpg)


## erciccione | 2021-04-06T07:58:24+00:00
These icons look definitely nicer. The only drawbacks are that we need to add their license (CC BY-SA 4.0) and we add single svgs, which i preferred to avoid. But i think this is the best option we have for now. Let's see if there are other opinions.

## erciccione | 2021-05-15T09:34:04+00:00
Just opened #1628, which add OpenMoji images and fixes this issue.

# Action History
- Created by: erciccione | 2020-04-12T09:42:39+00:00
- Closed at: 2021-05-22T02:40:27+00:00
