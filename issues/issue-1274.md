---
title: 'Proposal: User-Friendly Denomination Names for Everyday Use (Cero & Nero)'
source_url: https://github.com/monero-project/meta/issues/1274
author: ElioDonato
assignees: []
labels:
- proposal
created_at: '2025-09-30T15:02:31+00:00'
updated_at: '2026-04-10T15:20:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# Summary
Introduce intuitive, everyday names for Monero denominations to improve usability for merchants and consumers. Propose "Cero" (0.01 XMR) as the main unit and "Nero" (0.0001 XMR) as the subunit.

# Problem
Current Monero displays (0.0130 XMR for a 3 CHF bread) are impractical for daily use. While technical SI units (millinero, piconero) exist, they lack the simplicity needed for commerce.

**Current situation:**
- 1 XMR ≈ 230 CHF (Sept 2025)
- 3 CHF bread = 0.0130 XMR ← too abstract
- Technical names (piconero, nanonero) are not merchant-friendly

# Proposed Solution

| Name | Value | At 230 CHF/XMR | Use Case |
|------|-------|----------------|----------|
| **Cero** | 0.01 XMR | 2.30 CHF | Main everyday unit |
| **Nero** | 0.0001 XMR | 0.023 CHF | Subunit (like cents/Rappen) |

**Conversion:**
- 1 XMR = 100 Cero = 10,000 Nero
- 1 Cero = 100 Nero

**Examples:**
- 3 CHF bread = **1.3 Cero** (instead of 0.0130 XMR)
- 50 CHF restaurant = **21.74 Cero**
- 2300 CHF rent = **1000 Cero** (or 10 XMR)

# Benefits
1. **Intuitive:** Similar to CHF/Rappen, EUR/Cent, USD/Cents
2. **Merchant-friendly:** Easy to price goods (1.5 Cero vs 0.0150 XMR)
3. **Brand consistency:** Names derive from "Monero"
4. **Flexible:** Works at any price point

# Discussion Points
- Are these names appropriate for the Monero community?
- Should wallets implement this as a display option?
- Other naming suggestions welcome

## Background Research
- SI units (millinero, piconero) established 2017 for technical use
- "Tacoshi" was proposed but changed to piconero for consistency
- No previous proposals found for everyday commerce names

---
**Note:** This is a UX/nomenclature proposal, not a protocol change. It aims to make Monero more accessible for real-world transactions.

# Discussion History
## PPPDUD | 2026-04-10T14:14:54+00:00
What about decinero and centinero instead, because those are decently-sized but still use the SI prefix system?

## nahuhh | 2026-04-10T15:19:51+00:00
> What about decinero and centinero instead, because those are decently-sized but still use the SI prefix system?

https://www.getmonero.org/resources/moneropedia/denominations.html

## PPPDUD | 2026-04-10T15:20:58+00:00
> > What about decinero and centinero instead, because those are decently-sized but still use the SI prefix system?
> 
> https://www.getmonero.org/resources/moneropedia/denominations.html

Nevermind.

# Action History
- Created by: ElioDonato | 2025-09-30T15:02:31+00:00
