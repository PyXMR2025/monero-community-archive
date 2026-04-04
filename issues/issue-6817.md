---
title: 'proposal: supporting adoption with another URI handler, RFC 8905'
source_url: https://github.com/monero-project/monero/issues/6817
author: vv01f
assignees: []
labels: []
created_at: '2020-09-14T16:01:42+00:00'
updated_at: '2020-09-15T05:33:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[RFC 8905](https://www.rfc-editor.org/rfc/authors/rfc8905.html) describes a currency agnostic URI handler. The initiative comes from the payment transport layer project (my wording) [GNU Taler](https://taler.net/). They openly prefer "real banks" and legal tender (fiat) currencies and question some properties of cryptocurrencies while emphasizing payments on such a payment network should be private while promoting centralized on- and off-ramps.

I suggest to specify the URI handling for `payto://monero/` to be early on added to the [GANA](https://gana.gnunet.org/) (GNUnet e.V., "GNUnet Assigned Numbers Authority", April 2020) registry for the payment target "monero". This way if applications implement that standard they also might support monero.

The "official URI spec"[¹] is named but not to be found other than [on a wiki](https://monero.fandom.com/wiki/URI_formatting) (also [on GitHub](https://github.com/monero-project/monero/wiki/URI-Formatting)) or in source; that could be fixed in passing.

[¹]: https://monerodocs.org/interacting/monero-wallet-rpc-reference/#make_uri

Any early objection/comment how or why (not) this should be approached and what form to utilize?
Is there any things that could be addressed incidentally?

# Discussion History
## iamamyth | 2020-09-15T01:19:15+00:00
I suppose the question would be whether this proposal creates any kind of maintenance burden. If you're volunteering to add Monero to the registry, and that's all the needed work, then it doesn't seem objectionable to me. Otherwise, in my view, it's just a distraction, because:

1. Literally nothing uses Taler:
    > We are aware of several businesses running exploratory projects or having developed working prototypes. We are also in discussions with several regular banks as well as several central banks about the project. That said, there are currently no products in the market yet, and we believe this would be premature given the state of the project (see also our bugtracker for a list of open issues).
    [https://taler.net/en/faq.html](https://taler.net/en/faq.html)

2. The linked RFC isn't a standards-track document, and could easily change substantially before finalization:

    > This document is not an Internet Standards Track specification; it is published for informational purposes.
    >
    > This is a contribution to the RFC Series, independently of any other RFC stream. The RFC Editor has chosen to publish this document at its discretion and makes no statement about its value for implementation or deployment. Documents approved for publication by the RFC Editor are not candidates for any level of Internet Standard; see Section 2 of RFC 7841.
    [https://www.rfc-editor.org/rfc/authors/rfc8905.html](https://www.rfc-editor.org/rfc/authors/rfc8905.html)

## vv01f | 2020-09-15T05:33:41+00:00
The risk for maintenance in my eyes is limited to changes from the side of the Monero Project if need be for additional parameters.

As for changes of the RFC it would make things simpler to increase or lift the arbitrary limit of 8 decimals as Monero uses 12 currently. This could be circumvented if there was either an alternative notation or unit. The first (e.g. 1e-12 for scientific notation) does not seem more user friendly than typing many zeroes and the latter is not fitting in the currency definitions available. Currently I would prefer a direct correction of that limit in the RFC which might be considered after the registry lists examples that blow up the limit.  

# Action History
- Created by: vv01f | 2020-09-14T16:01:42+00:00
