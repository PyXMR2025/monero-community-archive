---
title: 'merchants: add TrustSwap to Swappers section'
source_url: https://github.com/monero-project/monero-site/issues/2672
author: James2421
assignees: []
labels: []
created_at: '2026-06-16T00:28:37+00:00'
updated_at: '2026-06-29T00:11:34+00:00'
type: issue
status: closed
closed_at: '2026-06-29T00:11:34+00:00'
---

# Original Description
## Request
Please add TrustSwap to the **Swappers** section on the Merchants & Exchanges page:
https://www.getmonero.org/community/merchants/

## Service
- **Name:** TrustSwap
- **URL:** https://trustswap.io
- **Type:** Non-custodial instant crypto swap (Swappers)

## Monero support
- XMR supported (BTC ↔ XMR, USDT ↔ XMR, and other pairs via instant swap)
- No registration, no KYC for standard swaps
- Non-custodial — funds go wallet-to-wallet

## Privacy
- No IP logging
- Transaction logs auto-deleted after 24 hours
- No analytics/tracking cookies

## Links
- Website: https://trustswap.io
- FAQ: https://trustswap.io/faq.html
- Privacy: https://trustswap.io/privacy-policy.html
- Terms: https://trustswap.io/terms-of-use.html
- Support: support@trustswap.io

## Note
TrustSwap is an **independent brand and website**, not a redirect to StealthEX. StealthEX may already be listed separately; TrustSwap operates its own frontend, support, and privacy policies.

## Suggested code change
File: `community/merchants/index.md` — add under Swappers `<ul>`:
```html
<li><a href="https://trustswap.io/">TrustSwap</a></li>

# Discussion History
# Action History
- Created by: James2421 | 2026-06-16T00:28:37+00:00
- Closed at: 2026-06-29T00:11:34+00:00
