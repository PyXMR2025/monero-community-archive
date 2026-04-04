---
title: Can't join bridged IRC channels via Matrix using the links on Hangouts page
source_url: https://github.com/monero-project/monero-site/issues/1828
author: bitlamas
assignees: []
labels: []
created_at: '2021-09-13T18:57:18+00:00'
updated_at: '2021-10-05T07:43:16+00:00'
type: issue
status: closed
closed_at: '2021-10-04T16:55:25+00:00'
---

# Original Description
I'm not sure if this is really an issue, but I was unable to access any of the bridged IRC channels via Matrix using the URLs available on the website.
For example, according to the [/community/hangouts/](https://www.getmonero.org/community/hangouts/) page, to access #monero-markets via Matrix, the link redirects me to a matrix.to page, with the code `!WzzKmkfUkXPHFERgvm:monero.social`.
When I try to join the room using the command `/join !WzzKmkfUkXPHFERgvm:monero.social`, I get a `No known servers` error. When trying to connect using `/join #monero-markets:libera.chat` the client joined the room correctly.
Is this because my Matrix account was not made on monero.social?
If so, maybe it would be interesting to add the alternative command to connect to rooms, as some people might have Matrix accounts from other servers, including matrix.org itself.
Anyway, I'm fairly new using Matrix so maybe this is not an issue.

# Discussion History
## erciccione | 2021-09-14T08:05:12+00:00
This is expected behaviour. The matrix links will be opened by your locally installed matrix interface (like Element). If you haven't one, it will redirect you to the web-based Element.

> When I try to join the room using the command /join !WzzKmkfUkXPHFERgvm:monero.social, I get a No known servers error. 

This is expected.

> When trying to connect using /join #monero-markets:libera.chat the client joined the room correctly.

Note that using that address you are accessing the room through the libera matrix server (you are connecting to IRC). If you are a matrix user you want to use a matrix homeserver. For example for monero-markets should be `#monero-markets:monero.social`

## bitlamas | 2021-10-04T17:19:23+00:00
Sorry for commenting on this issue right after you closed it. I didn't get or missed the notification from your initial reply and only got one now.
I believe the expected behaviour might wrongly assume users will use Element, in case the actual instructions work with that client. Here is the step by step of my experience when using another matrix client (Nheko):

1. Open the Hangouts homepage and click the _Matrix_ icon next to the #matrix channel.
2. It takes me to the matrix.to web page with a list of possible clients to use to connect to the channel.
3. I click on Nheko, which opens a new page instructing me to type `/join !psOvWRiQkyosOPKvaO:monero.social`.
4. I open Nheko and type` /join !psOvWRiQkyosOPKvaO:monero.social`, which returns me the `No known servers error`.

And that's the end of it. There are no further instructions such as "try typing `/join #monero:monero.social`" (which works and is the actual solution). The only way I could find this information was by you informing me on this Github issue. I imagine other users could stumble upon the same issue and simply find no recourse on how to join the channel using a different client that is not Element.

> The matrix links will be opened by your locally installed matrix interface (like Element). If you haven't one, it will redirect you to the web-based Element.

I don't use Element, the link does not open my local matrix client, and it doesn't take me to web-based Element, it takes me to a list of possible clients to use to connect to the channel and even after choosing the correct client the connection string does not work. Maybe this is out of reach for you since it's managed by matrix.to (I'm assuming) but I wanted to at least document what is my experience using a different client.



## erciccione | 2021-10-05T07:43:16+00:00
> I click on Nheko, which opens a new page instructing me to type /join !psOvWRiQkyosOPKvaO:monero.social.

That sounds like a problem of your matrix client, which should be able to parse that room id and show it to you in the readable form (#monero:monero.social). I don't think there is much we can do here, best would probably be to let the developers of your client know about the issue. If there is something we can do to workaround the issue, please let us know.

# Action History
- Created by: bitlamas | 2021-09-13T18:57:18+00:00
- Closed at: 2021-10-04T16:55:25+00:00
