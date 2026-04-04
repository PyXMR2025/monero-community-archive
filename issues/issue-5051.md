---
title: SubAddress  lable wrong encoding
source_url: https://github.com/monero-project/monero/issues/5051
author: maogo
assignees: []
labels: []
created_at: '2019-01-08T16:51:48+00:00'
updated_at: '2019-01-08T18:30:37+00:00'
type: issue
status: closed
closed_at: '2019-01-08T18:30:37+00:00'
---

# Original Description
CLI wallet  type in: address all

When the SubAddress  lable is Chinese  will be unintelligible text and command are no longer effective.

"壹"  "贰"  “叁”

# Discussion History
## moneromooo-monero | 2019-01-08T17:04:02+00:00
Seems to work here:

[wallet 8BC1cR (no daemon)]: address all
0  8BC1cRnTXpGFA7KZhsFkdQVa2m6C4di1KFCP8BiRK7KQUcGZjf5SwCEV41qEqoquutNQvPjPzNtEDSHHLrcQWBguV5kHwbE  Primary address 
1  87WwBXP74fJQHqhRbMNTetFWshbEvXY9R3Jt8Fkjfja4PLQNMhRaCWMBEohhv4KLebCAYrGa7erGpCgS2GmspfKpT5qTQrH  贰 
2  89nbH9dbdB48EiJSX9tTq612kBxB96TQk6yUJhdjfLQwHDiMzgjMi9dCoapDjoWB1r8mFoEnjkXrLZdSdE1LQLxrRkJGkX6  "壹" "贰" “叁” 
3  87iVhaNmd4R2HsN9ZEe9pDh39NWRQrFPiBiyP39mstMSTxvNChNgM1JZZrpwPWH6dV9q4fq22HnvXMjinjdoTuDvR7G2z8B  壹 贰 叁 


Are you using Windows ? Are you using current master ? If yes and no, try current master, there were fixes to Unicode.


## maogo | 2019-01-08T18:30:37+00:00
thank you, its win10 pro and  just upgrading to the latest but it doesn't work. I close this
1  873z8Mvg1hgD2nZGb9Ffcug8x7xaMBHsvhsLzak9fXfDKU3d3APvHrS651DDXgyU5qZCy4SbEax1acf1hc5RXvrG58Zy9Gn  浣犲ソ
2  8AgthgcSBZNixtHaWpXyMGjjF59gLCoSFEtMhoDLeNdaPM9LH9uc5VG98vMVkM3nuiAHA2JwmTqchiWR3vEA2asSBNJfZpA  濂?

# Action History
- Created by: maogo | 2019-01-08T16:51:48+00:00
- Closed at: 2019-01-08T18:30:37+00:00
