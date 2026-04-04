---
title: setup onion service url for the CCS
source_url: https://github.com/monero-project/monero-site/issues/2216
author: plowsof
assignees: []
labels:
- 🧰 back end
created_at: '2024-01-01T11:56:21+00:00'
updated_at: '2025-11-15T09:15:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
ofrnxmr noted in -site that https://ccs.getmonero.org does not have an onion link and is behind cloudflare. lets fix that and allow people to obtain donation addresses anonymously from a trusted source

assigning myself

- [x] reach out to backend admin to setup onion service
- [ ] confirm onion service is up / running (automatically redirecting if possible)
- [ ] update [onion.txt](https://github.com/monero-project/monero-site/blob/master/onion.txt) with the new URL signed by binaryFate 

# Discussion History
## nahuhh | 2024-01-09T01:58:14+00:00
Perhaps can just KISS and use the existing onion by config nginx so these have proper endpoints

http://ccs.monerotoruzizulg5ttgat2emf4d6fbmiea25detrmmy7erypseyteyd.onion

http://repo.monerotoruzizulg5ttgat2emf4d6fbmiea25detrmmy7erypseyteyd.onion

## nahuhh | 2024-04-05T04:20:07+00:00
Bump

## librootorg | 2025-11-15T03:55:31+00:00
bump

## plowsof | 2025-11-15T07:02:29+00:00
Will chase this up again 

## nahuhh | 2025-11-15T09:15:09+00:00
> Will chase this up again 

fwiw. repo.* is likely not happening for technical reasons
ccs.* should though,

# Action History
- Created by: plowsof | 2024-01-01T11:56:21+00:00
