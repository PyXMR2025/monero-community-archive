---
title: _config.yml baseurl differs from live URL
source_url: https://github.com/monero-project/monero-site/issues/1023
author: Samuel-Pedraza
assignees: []
labels:
- UX
- wontfix
created_at: '2020-06-02T00:54:50+00:00'
updated_at: '2020-06-03T21:29:06+00:00'
type: issue
status: closed
closed_at: '2020-06-03T21:29:06+00:00'
---

# Original Description
The baseurl defined in _config.yml differs from the live URL, which causes all the links in the navbar to be formatted:

`https://getmonero.org/example-url/
`

instead of

`https://web.getmonero.org/example-url/
`

This causes every link to return a 301 status code, instead of a 200 status code.

Is it a good idea to change it? Or is there a better reason to just leave it?

Thanks

# Discussion History
## erciccione | 2020-06-02T12:03:05+00:00
IIRC that's on purpose. `web.getmonero` was confusing and looked scammy to some people (like `ww.getmonero`). I dont see a reason to change it.

## Samuel-Pedraza | 2020-06-02T17:56:59+00:00
Eric - I'm just having some trouble understanding what the original intent of having web.getmonero.com on the main website if it looks scammy?

Additionally, I know that from an SEO perspective on web.getmonero.org, it would be considered best practice to link to the place that these pages exist, not rely on 301 redirects to get there.

I apologize if this isn't the medium to ask these questions - I'm not really sure where else to go with them.

Thanks

## erciccione | 2020-06-03T12:11:59+00:00
Honestly i don't remember why we were using web.getmonero.org, but iirc it was related to cloudflare.

I suggest you to join `#monero-site` on Freenode, matrix and other platforms. That's a better place for questions than this issue tracker :)

## Samuel-Pedraza | 2020-06-03T21:29:06+00:00
Great, thanks!

# Action History
- Created by: Samuel-Pedraza | 2020-06-02T00:54:50+00:00
- Closed at: 2020-06-03T21:29:06+00:00
