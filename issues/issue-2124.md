---
title: bug when displaying tags on blog posts
source_url: https://github.com/monero-project/monero-site/issues/2124
author: erciccione
assignees: []
labels:
- blog
- bug
created_at: '2023-02-02T10:10:44+00:00'
updated_at: '2023-03-14T14:31:42+00:00'
type: issue
status: closed
closed_at: '2023-03-14T14:31:42+00:00'
---

# Original Description
![Screenshot_20230202_100231](https://user-images.githubusercontent.com/28106476/216295409-b174eb90-19de-454e-a0e2-01e90a3a72bb.png) 
(from https://www.getmonero.org/2023/02/02/seraphis-jamtis-developer-opportunities.html)

There is some problem while looping through the tags of a post.  I might have an idea of why, as it could be related to the trimming of blog post tags done some years ago.

# Discussion History
## plowsof | 2023-02-02T12:05:04+00:00
I should have noticed this in review, i vaguely remember glancing at those tags and assuming it was a problem on my end and then focused on the content of the blog post. After investigating, it is just a simple case of 'forgetting to add the tags'. the reason for the duplication is: 

For every tag in tags.yml, if the slug == "Community" then append the tag.
https://github.com/monero-project/monero-site/blob/2efb6619b9883767d5a4acd3de21b507a53daba3/_layouts/post.html#L10

Because the other tags do not exist to change the variable, "Community" just gets appended each time (the correct number of times for how many tags there are). so nothing nefarious is happening here, just a slip up. #2125 


# Action History
- Created by: erciccione | 2023-02-02T10:10:44+00:00
- Closed at: 2023-03-14T14:31:42+00:00
