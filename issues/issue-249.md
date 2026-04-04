---
title: Monero Missives podcasts deleted?
source_url: https://github.com/monero-project/monero-site/issues/249
author: jonathancross
assignees: []
labels: []
created_at: '2017-04-07T23:34:29+00:00'
updated_at: '2020-04-07T09:29:51+00:00'
type: issue
status: closed
closed_at: '2020-04-07T09:29:51+00:00'
---

# Original Description
It seems that all podcasts have been deleted, eg:
* http://traffic.libsyn.com/monero/Monero_Missives_Podcast_for_the_week_of_2016-06-20.mp3
* http://traffic.libsyn.com/monero/Monero_Missives_Podcast_for_the_week_of_2015-12-26.mp3
* http://traffic.libsyn.com/monero/Monero_Missives_Podcast_for_the_week_of_2015-09-14.mp3
* Etc...

I got the links off of the monero site.
Can these be restored, or are there backups somewhere?

# Discussion History
## serhack | 2017-05-28T16:35:40+00:00
Hello @jonathancross 
I was looking for these files, but I never found them :(


## jonathancross | 2017-05-29T18:59:08+00:00
I have no idea who was in charge of these, but they can [file a support ticket here](https://playerfm.freshdesk.com/support/tickets/new) if the takedown was not intentional.  If it **_was intentional_**, then the links should be removed from the website.


## QuickBASIC | 2017-09-16T14:16:11+00:00
@jonathancross I think you're mistaken. I don't believe they were hosted there, but instead were syndicated at last.fm. 

> Hi Mike.
> 
> I am sorry that the links to the episodes you specified are dead.
> 
> I tried opening them on my end and I got the following message:
> 
> "Error: 404 Not Found
> There was a problem processing your request!
> Details:
> 
> Attempting to load:
> http://traffic.libsyn.com/monero/Monero_Missives_Podcast_for_the_week_of_2016-06-20.mp3
> Previous URL:
> No Previous URL"
> 
> What I can suggest you to do is to reupload your podcast on a podcast hosting service, get an RSS feed and send it to us, if you want them displayed on our end.
> 
> I hope that this answers your question.
> 
> Cheers,
> Viktor
> Player FM

I think our best bet is going to be to get them from the original creator of the podcast or someone that downloaded them to listen to them and still have them somewhere.

www.libsyn.com costs $5/mo, so my assumption is that someone didn't pay the rent on the hosting. I don't know how the community is hosting large binary files, but if we don't already have hosting I'm assuming we could do a FFS to fund hosting if we find them.

## jonathancross | 2017-09-18T01:11:34+00:00
Hi @QuickBASIC, I don't know anything about the hosting of these files or syndication, just shooting in the dark here.  Trying to fix broken links on the website [like these](https://getmonero.org/2016/06/20/monero-missive-for-the-week-of-2016-06-20.html).  After you mentioned last.fm, I tried searching there, but only found a listing for 1 episode ([Monero Missives - Riccardo "fluffypony" Spagni and Gingeropolous](https://www.last.fm/music/Riccardo+%22fluffypony%22+Spagni+and+Gingeropolous/Monero+Missives)), but it cannot actually be downloaded / purchased.

@fluffypony Do you have copies of of these by chance?

## QuickBASIC | 2017-09-18T02:20:01+00:00
The other day on IRC @fluffypony said he had them and will figure out how to rehost them.

## QuickBASIC | 2017-10-23T11:43:03+00:00
+in progress
+blog

## erciccione | 2018-06-25T10:03:09+00:00
Any update on this issue? @fluffypony ?

## fluffypony | 2018-06-25T10:07:59+00:00
@erciccione sorry missed the earlier ping. I can rehost them on downloads.getmonero.org - thoughts on that? I'm also thinking of putting the whole downloads directory up on git so there's a mirror.

## erciccione | 2018-06-25T10:46:12+00:00
> I can rehost them on downloads.getmonero.org - thoughts on that?

Since i don't think it's necessary to create a dedicated section on getmonero for the podcasts, that sounds like the best option for me. The only conflict i see is that media.getmonero cease to have a reason to exist at this point (it's not active at the moment tho), epecially if we decide to move the videos in the 'Download' repo as well (referring to [#393 (comment)](https://github.com/monero-project/monero-site/issues/393#issuecomment-399901130))

> I'm also thinking of putting the whole downloads directory up on git so there's a mirror.

+1. I think this would be also beneficial for mirror websites (see [this reddit post](https://www.reddit.com/r/Monero/comments/8tio53/monero_really_needs_a_mirror_eepsite_like_right/)) who will be able to just link to the downloads directory, so that users will feel more confortable downloading from a repo maintained by the core team and not some random.

## fluffypony | 2018-06-25T10:49:25+00:00
@erciccione we can just CNAME media.getmonero to downloads.getmonero if we need to retain some links

## fluffypony | 2018-06-25T11:02:44+00:00
Can someone consolidate these into a new issue? Then we can also decide what we need to leave out via .gitignore

## erciccione | 2018-06-25T11:10:33+00:00
Then i don't see any other problem with that. yep, opening an issue right now @fluffypony 

## erciccione | 2018-06-25T11:20:56+00:00
@fluffypony #780 

## erciccione | 2020-04-07T09:29:51+00:00
This was tracked and then closed on gitlab.

# Action History
- Created by: jonathancross | 2017-04-07T23:34:29+00:00
- Closed at: 2020-04-07T09:29:51+00:00
