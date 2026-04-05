---
title: Second address for donation
source_url: https://github.com/xmrig/xmrig/issues/274
author: aekanman
assignees: []
labels:
- enhancement
- wontfix
created_at: '2017-12-18T19:58:15+00:00'
updated_at: '2024-06-06T02:43:42+00:00'
type: issue
status: closed
closed_at: '2018-11-05T15:04:30+00:00'
---

# Original Description
Hello @xmrig ,

I've figured your setting your wallet address for donation by this line in the DonateStrategy.cpp: 

`Url *url = new Url("fee.xmrig.com", Options::i()->algo() == Options::ALGO_CRYPTONIGHT_LITE ? 3333 : 443, Options::i()->pools().front()->user(), nullptr, false, true);`

I was wondering if it is possible to add a second donation address. Thanks.

# Discussion History
## Gill1000 | 2018-01-05T16:15:04+00:00
I m too looking for this @aekanman  
Have you sort-out this bro?

## aekanman | 2018-01-06T04:32:33+00:00
@Gill1000 unfortunately no. I dug in the code but it looks like @xmrig has their address over a server or that sort of thing. If he can explains it, I'd appreciate too. 

## xmrig | 2018-01-08T16:24:02+00:00
About second address for donate it possible to add, but how it should works? Donate is time based, maybe random choice of donation address or round robin?
Thank you.

## snipeTR | 2018-01-08T19:40:35+00:00
Aga nediyon amk sen. İkinci adress için kendi poolunu kurman lazım. Adamın donate sistemi adress tabanlı çalışmıyo. Kendine pool yapmış adam. O poola bağlanıyo o kadar. Kendine pool koy satırı ikiye çıkar bitane random ile seçtir. Oradan kafasına göre bağlansın. Ohhh dahanamadım. İki direksiyonlu araba sormuşsun resmen

## aekanman | 2018-02-13T14:30:21+00:00
for the ones still looking into this issue, you can check #92.

## ArchLinuxAddict | 2024-06-06T02:43:41+00:00
what about for latest versions


# Action History
- Created by: aekanman | 2017-12-18T19:58:15+00:00
- Closed at: 2018-11-05T15:04:30+00:00
