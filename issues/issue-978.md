---
title: Remove all JavaScript tracking (Piwik, Matomo)
source_url: https://github.com/monero-project/monero-site/issues/978
author: selsta
assignees: []
labels:
- 💬 discussion
created_at: '2020-05-13T10:56:55+00:00'
updated_at: '2020-07-28T02:36:03+00:00'
type: issue
status: closed
closed_at: '2020-07-28T02:36:03+00:00'
---

# Original Description
Monero as a a privacy coin should lead by example and remove all JavaScript tracking from their website.

Basic analytics can be extracted from webserver logs, Matomo even supports this: https://matomo.org/log-analytics/

# Discussion History
## erciccione | 2020-05-13T11:41:02+00:00
Important to note that Matomo hasn't been working for some time (#945).

I would find very useful to have info about what people visit on getmonero, the language they speak and where the people come from (meaning, what website directed them to getmonero.org), so to be able to make aimed changes and improvements to the website.

If these info can be retrieved from server logs using Matomo (and from a quick look, seems like it does), i agree with removing all JS based tracking, otherwise better discuss an alternative.

## selsta | 2020-05-13T12:31:48+00:00
> I would find very useful to have info about what people visit on getmonero, the language they speak and where the people come from (meaning, what website directed them to getmonero.org), so to be able to make aimed changes and improvements to the website.

All of this should be possible with log parsing.

## erciccione | 2020-06-12T08:18:53+00:00
@danrmiller could you set up Matomo to only use the server logs?

# Action History
- Created by: selsta | 2020-05-13T10:56:55+00:00
- Closed at: 2020-07-28T02:36:03+00:00
