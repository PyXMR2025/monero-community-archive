---
title: 'Hangouts: Add Monero.town'
source_url: https://github.com/monero-project/monero-site/issues/2350
author: HardenedSteel
assignees: []
labels: []
created_at: '2024-08-17T07:27:57+00:00'
updated_at: '2024-08-18T14:24:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
add monero.town lemmy instance to hangouts page

# Discussion History
## rottenwheel | 2024-08-17T07:49:41+00:00
Instance runs behind Cloudflare, which means federation works on a whitelist mode. Some people have complained about not being able to visit town when on Tor browser.

https://0xacab.org/dCF/deCloudflare/-/blob/master/readme/en.md

https://redlib.zaggy.nl/r/Monero/comments/1e3rmw5/new_cmonero_community_set_up_at/

## nahuhh | 2024-08-17T07:59:41+00:00
Tor working for me now

## HardenedSteel | 2024-08-17T10:15:48+00:00
isn't getmonero.org already behind the cloudflare?

## nahuhh | 2024-08-17T13:37:20+00:00
Yes

## rottenwheel | 2024-08-17T14:33:15+00:00
> isn't getmonero.org already behind the cloudflare?

Yes, you can imagine what I think of that. 🤷‍♂️
I'm not alone either. 

## monerobull | 2024-08-17T15:12:10+00:00
> which means federation works on a whitelist mode

This is false. I don't know why the instance you are on hasn't federated in 3 months but other instances have no issues.

## rottenwheel | 2024-08-17T18:53:59+00:00
> > which means federation works on a whitelist mode
> 
> This is false. I don't know why the instance you are on hasn't federated in 3 months but other instances have no issues.

Care to explain this [message](https://matrix.to/#/!WzzKmkfUkXPHFERgvm:matrix.org/$SiPV8XoWCGcWBxRoFcHhU93BF-I9hNZcI6yoUHeGtL4?via=matrix.org&via=monero.social&via=libera.chat), then? 

IRC: https://libera.monerologs.net/monero-community/20240715#c398496

While we're at it, why do lemmy.cafe's posts don't show up on .town/c/monero, but lemmy.zip's do? Hint: .zip is behind CF, cafe isn't.

## rottenwheel | 2024-08-17T18:58:13+00:00
Yet more messages written by you, alluding to such whitelist, this one is more recent than the one above. False much, eh? Quoting Monero's GitLab [comment](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/481#note_25594):

> Btw do you want to mod on monero.town? There is very little to do because of the whitelist but 

## monerobull | 2024-08-18T14:24:15+00:00
> > > which means federation works on a whitelist mode
> > 
> > 
> > This is false. I don't know why the instance you are on hasn't federated in 3 months but other instances have no issues.
> 
> Care to explain this [message](https://matrix.to/#/!WzzKmkfUkXPHFERgvm:matrix.org/$SiPV8XoWCGcWBxRoFcHhU93BF-I9hNZcI6yoUHeGtL4?via=matrix.org&via=monero.social&via=libera.chat), then?
> 
> IRC: https://libera.monerologs.net/monero-community/20240715#c398496
> 
> While we're at it, why do lemmy.cafe's posts don't show up on .town/c/monero, but lemmy.zip's do? Hint: .zip is behind CF, cafe isn't.

I was wrong about the federation not working, it was the cloudflare captcha that breaks it, not cloudflare itself. 



> Yet more messages written by you, alluding to such whitelist, this one is more recent than the one above. False much, eh? Quoting Monero's GitLab [comment](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/481#note_25594):
> 
> > Btw do you want to mod on monero.town? There is very little to do because of the whitelist but

This is completely unrelated and talking about the sign-up whitelist that prevents bot accounts and helps keeping the instance alive.

# Action History
- Created by: HardenedSteel | 2024-08-17T07:27:57+00:00
