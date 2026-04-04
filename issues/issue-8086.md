---
title: ' Feature request: show public key (stealth address) for each spent output
  under show_transfer'
source_url: https://github.com/monero-project/monero/issues/8086
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2021-11-26T20:33:19+00:00'
updated_at: '2021-11-26T20:33:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Related to https://git.featherwallet.org/feather/feather/issues/379

When querying the details of `show_transfer` (and `show_trasnfers`), monero-wallet-cli should additionally return the public key (stealth address) of the specific output sent to that address.

For example, suppose in txid with 16 outputs `52f114c0dfa11aded9ca8797b8e1d0c323f5c7da95a963925c83cc4ab22376b2` that 15 outputs went to 15 different addresses, and 1 output went back as change. It should be extremely obvious which output was sent to each of the recipients.

`<address 01> <public key / stealth address 01> <amount 01>`
`<address 02> <public key / stealth address 02> <amount 02>`
`<address 03> <public key / stealth address 03> <amount 03>`
`<address 04> <public key / stealth address 04> <amount 04>`
`<address 05> <public key / stealth address 05> <amount 05>`
`<address 06> <public key / stealth address 06> <amount 06>`
`<address 07> <public key / stealth address 07> <amount 07>`
`<address 08> <public key / stealth address 08> <amount 08>`
`<address 09> <public key / stealth address 09> <amount 09>`
`<address 10> <public key / stealth address 10> <amount 10>`
`<address 11> <public key / stealth address 11> <amount 11>`
`<address 12> <public key / stealth address 12> <amount 12>`
`<address 13> <public key / stealth address 13> <amount 13>`
`<address 14> <public key / stealth address 14> <amount 14>`
`<address 15> <public key / stealth address 15> <amount 15>`
`<address 16 (change)> <public key / stealth address 16> <amount 16>`

# Discussion History
# Action History
- Created by: SamsungGalaxyPlayer | 2021-11-26T20:33:19+00:00
