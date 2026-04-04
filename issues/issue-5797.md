---
title: Version 0.14.1.2 cannot be transferred
source_url: https://github.com/monero-project/monero/issues/5797
author: singpenguin
assignees: []
labels: []
created_at: '2019-08-08T02:12:01+00:00'
updated_at: '2019-08-16T10:37:47+00:00'
type: issue
status: closed
closed_at: '2019-08-16T10:37:47+00:00'
---

# Original Description
Hi, I running the version 0.14.1.2, Calling the transfer interface succeeded, but the transaction did not broadcast.

DNS_PUBLIC=tcp ./monero-0.14.1.2/monero-wallet-rpc --rpc-bind-port 18088 --wallet-file walletfiles --password bepass --rpc-login username:pass


But the transfer was not successful. This is the log:

`
2019-08-07 15:43:54.807	W Using default public DNS server(s): 194.150.168.168, 80.67.169.40, 89.233.43.71, 109.69.8.51, 193.58.251.251 (TCP)
2019-08-07 15:43:54.807	I Using public DNS server(s): 194.150.168.168, 80.67.169.40, 89.233.43.71, 109.69.8.51, 193.58.251.251 (TCP)
2019-08-07 15:43:54.808	I adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2019-08-07 15:43:54.808	I adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2019-08-07 15:43:57.819	D DNSSEC not available for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:43:57.819	D DNSSEC validation failed for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:43:57.819	W WARNING: no two valid DNS TXT records were received
2019-08-07 15:43:57.840	W amount=0.999900000000, real_output=1, real_output_in_tx_index=0, indexes: 4958300 8313851 8731757 11245180 11585857 11639686 11667403 11692502 11702782 11708415 11709806
2019-08-07 15:43:57.845	W amount=0.999900000000, real_output=1, real_output_in_tx_index=0, indexes: 4958300 8313851 8731757 11245180 11585857 11639686 11667403 11692502 11702782 11708415 11709806
2019-08-07 15:43:57.852	D DNSSEC not available for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:43:57.852	D DNSSEC validation failed for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:43:57.852	W WARNING: no two valid DNS TXT records were received
2019-08-07 15:43:57.871	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 11656451 11688668 11690337 11696072 11704081 11706744 11707210 11707941 11708838 11710186
2019-08-07 15:43:57.871	W amount=0.001000000000, real_output=1, real_output_in_tx_index=0, indexes: 4413554 7737790 9275413 10763622 11431091 11519549 11676096 11676938 11708564 11709006 11709158
2019-08-07 15:43:57.881	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 11656451 11688668 11690337 11696072 11704081 11706744 11707210 11707941 11708838 11710186
2019-08-07 15:43:57.881	W amount=0.001000000000, real_output=1, real_output_in_tx_index=0, indexes: 4413554 7737790 9275413 10763622 11431091 11519549 11676096 11676938 11708564 11709006 11709158
2019-08-07 15:43:57.891	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 11656451 11688668 11690337 11696072 11704081 11706744 11707210 11707941 11708838 11710186
2019-08-07 15:43:57.891	W amount=0.001000000000, real_output=1, real_output_in_tx_index=0, indexes: 4413554 7737790 9275413 10763622 11431091 11519549 11676096 11676938 11708564 11709006 11709158
2019-08-07 15:43:58.010	W saving 1 transactions
`

When I use dns server 1.1.1.1, the log is :

`
2019-08-07 15:45:35.295	I Using public DNS server(s): 1.1.1.1 (TCP)
2019-08-07 15:45:35.295	I adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2019-08-07 15:45:35.295	I adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2019-08-07 15:45:35.388	D DNSSEC not available for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:45:35.388	D DNSSEC validation failed for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:45:35.388	W WARNING: no two valid DNS TXT records were received
2019-08-07 15:45:35.408	W amount=0.999900000000, real_output=1, real_output_in_tx_index=0, indexes: 3848503 8313851 11245181 11299200 11359614 11528757 11534333 11676846 11697399 11698285 11704698
2019-08-07 15:45:35.413	W amount=0.999900000000, real_output=1, real_output_in_tx_index=0, indexes: 3848503 8313851 11245181 11299200 11359614 11528757 11534333 11676846 11697399 11698285 11704698
2019-08-07 15:45:35.420	D DNSSEC not available for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:45:35.420	D DNSSEC validation failed for hostname: segheights.moneropulse.co, skipping.
2019-08-07 15:45:35.420	W WARNING: no two valid DNS TXT records were received
2019-08-07 15:45:35.439	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 9519728 11468139 11609384 11645011 11684263 11684711 11700936 11705246 11707929 11709547
2019-08-07 15:45:35.440	W amount=0.001000000000, real_output=0, real_output_in_tx_index=0, indexes: 7737790 10369379 11148819 11388922 11436692 11576977 11635159 11684823 11696765 11704580 11709649
2019-08-07 15:45:35.450	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 9519728 11468139 11609384 11645011 11684263 11684711 11700936 11705246 11707929 11709547
2019-08-07 15:45:35.450	W amount=0.001000000000, real_output=0, real_output_in_tx_index=0, indexes: 7737790 10369379 11148819 11388922 11436692 11576977 11635159 11684823 11696765 11704580 11709649
2019-08-07 15:45:35.460	W amount=0.999900000000, real_output=0, real_output_in_tx_index=0, indexes: 8313851 9519728 11468139 11609384 11645011 11684263 11684711 11700936 11705246 11707929 11709547
2019-08-07 15:45:35.460	W amount=0.001000000000, real_output=0, real_output_in_tx_index=0, indexes: 7737790 10369379 11148819 11388922 11436692 11576977 11635159 11684823 11696765 11704580 11709649
2019-08-07 15:45:35.578	W saving 1 transactions
`

It has been unsuccessful to send, it has been 2 weeks.
Thanks.

# Discussion History
## singpenguin | 2019-08-15T04:06:00+00:00
@luigi1111 can you help me? very thanks.

## dEBRUYNE-1 | 2019-08-15T20:32:02+00:00
Does it work with CLI v0.14.1.0? 

## singpenguin | 2019-08-16T10:37:47+00:00
it already solved. thanks.

# Action History
- Created by: singpenguin | 2019-08-08T02:12:01+00:00
- Closed at: 2019-08-16T10:37:47+00:00
