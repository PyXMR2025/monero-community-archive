---
title: Cpu usage is %66
source_url: https://github.com/xmrig/xmrig/issues/1743
author: MezarKazar
assignees: []
labels:
- question
created_at: '2020-06-23T10:39:37+00:00'
updated_at: '2020-06-23T11:45:01+00:00'
type: issue
status: closed
closed_at: '2020-06-23T11:41:33+00:00'
---

# Original Description
No description

# Discussion History
## xmrig | 2020-06-23T11:02:11+00:00
Please show miner output.
Thank you.

## xmrig | 2020-06-23T11:34:51+00:00
For this kind of CPU using only physical cores is the best strategy, technically this CPUs hash enough L3 cache for extra 20-24 threads with undefined result, likely hashrate will remain about the same, main issue there is no good place for extra threads.

Using all threads (100% CPU usage) definitely reduces hashrate, because this CPUs has not enough cache for it.
Thank you.

## snipeTR | 2020-06-23T11:36:48+00:00
şu anda 1000 dolar aylık gelirin var diğer desteklenen coinlere bir bakmanı tavsiye ederim. umarım yasadışı birşey yapmıyorsundur. çünkü kimliğini birazcık açık etmişsin. sanırım datacenter işletmecisisin. 
sadece fiziksel çekirdek sayısı kadar kullanmanı öneririm. hyper-treading performansı biraz düşürüyor.

## MezarKazar | 2020-06-23T11:45:00+00:00
> şu anda 1000 dolar aylık gelirin var diğer desteklenen coinlere bir bakmanı tavsiye ederim. umarım yasadışı birşey yapmıyorsundur. çünkü kimliğini birazcık açık etmişsin. sanırım datacenter işletmecisisin.
> sadece fiziksel çekirdek sayısı kadar kullanmanı öneririm. hyper-treading performansı biraz düşürüyor.

Selam. Diğer coin olarak öneriniz var mi? Uyari icin tesekkurler mesaji editledim. 

# Action History
- Created by: MezarKazar | 2020-06-23T10:39:37+00:00
- Closed at: 2020-06-23T11:41:33+00:00
