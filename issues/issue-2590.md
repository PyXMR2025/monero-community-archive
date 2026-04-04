---
title: '"Sorry, you have been blocked"'
source_url: https://github.com/monero-project/monero-site/issues/2590
author: libertoxxx
assignees: []
labels: []
created_at: '2026-01-25T19:17:54+00:00'
updated_at: '2026-03-06T18:22:38+00:00'
type: issue
status: closed
closed_at: '2026-03-06T18:22:38+00:00'
---

# Original Description
This is what I see when I visit getmonero.org:

[![getmonero-org-403-Forbidden.png](https://i.postimg.cc/cLZ4TJNQ/getmonero-org-403-Forbidden.png)](https://postimg.cc/1fCQ3sXt)

Browser: Firefox + Resist Fingerprinting enabled + uBlock Origin.

No VPN, residential IP. Website works fine with vanilla Chrome.

Correct me if I'm wrong, but this appears to be a PerimeterX / Human Security WAF block page.

I have been visiting getmonero.org for many years with this browser setup and this is the first time I've ever seen this.

# Discussion History
## plowsof | 2026-01-25T21:43:18+00:00
getmonero is behind cloudflare, but i couldn't reproduce with firefox + resist fingerprinting + ublock origin

## libertoxxx | 2026-01-26T00:29:07+00:00
I'm quite sure this is a block by a PerimeterX Web Server (PWS). Here are the response headers (potentially identifying info redacted):

```
HTTP/2 403 
date: Mon, 26 Jan 2026 00:XX:XX GMT
content-type: text/html
via: 0.0 PS-SEA-XXX
server: PWS/8.3.1.0.8
x-px: ht PS-SEA-XXX
x-ws-request-id: XXX_PS-SEA-XXX
ws-action: bot
cache-control: no-store
content-encoding: gzip
X-Firefox-Spdy: h2
```

Can also be reproduced with wget:

```
wget https://www.getmonero.org
--2026-01-26 00:00:00--  https://www.getmonero.org/
Resolving www.getmonero.org (www.getmonero.org)... 138.113.62.19, 66.114.53.22
Connecting to www.getmonero.org (www.getmonero.org)|138.113.62.19|:443... connected.
HTTP request sent, awaiting response... 403 Forbidden
2026-01-26 00:00:00 ERROR 403: Forbidden.
```

## nahuhh | 2026-01-26T05:25:10+00:00
Hm. 

`curl -s https://www.getmonero.org` = blocked (using tor), but i am able to load it in tor browser.

Can you try in tor browser?

## any1here | 2026-01-27T12:07:06+00:00
Having WebGL disabled on LibreWolf (default setting) triggers this. If WebGL is enabled, it avoids the block.

## kasualkeef | 2026-01-29T13:26:32+00:00
I am also seeing this problem. I can load the website fine in browser but get "Sorry, you have been blocked" when I use curl.

I have a CI-CD pipeline that builds an XMR node container image which uses `curl` to pull the [hashes](https://getmonero.org/downloads/hashes.txt) for download verification.

## lkraider | 2026-02-26T00:54:02+00:00
Same here, trying to fetch hashes.txt using curl but getting this blocked page instead. Any mirror for the hashes.txt download?

## nahuhh | 2026-02-26T02:44:09+00:00
> Any mirror for the hashes.txt download?

yes, right here on github


https://raw.githubusercontent.com/monero-project/monero-site/refs/heads/master/downloads/hashes.txt


## cariad | 2026-02-28T08:15:56+00:00
`curl` works for me if I change the user agent:

```bash
curl https://www.getmonero.org/downloads/hashes.txt --user-agent "Mozilla/5.0 (X11; Linux i686; rv:148.0) Gecko/20100101 Firefox/148.0"
```

## kasualkeef | 2026-03-02T15:24:38+00:00
Hmm, it seems to just work now (regardless of setting the user agent)...

## plowsof | 2026-03-02T15:52:16+00:00
>[05:12](https://libera.monerologs.net/monero-site/20260302#c658984) binaryFate
it's not from cloudflare, it's from our CDN. They have made that change unilaterally and I can't find anything in any setting explaining this. I have contacted them
>[05:12](https://libera.monerologs.net/monero-site/20260302#c658985) binaryFate
in the meantime you can curl web.getmonero.org
>[05:30](https://libera.monerologs.net/monero-site/20260302#c658989) binaryFate
also seems simply specifying a different user-agent with curl is sufficient

# Action History
- Created by: libertoxxx | 2026-01-25T19:17:54+00:00
- Closed at: 2026-03-06T18:22:38+00:00
