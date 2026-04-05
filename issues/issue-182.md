---
title: WINE Problem?
source_url: https://github.com/xmrig/xmrig/issues/182
author: shift-reality
assignees: []
labels:
- invalid
created_at: '2017-10-29T18:11:46+00:00'
updated_at: '2017-10-29T21:51:03+00:00'
type: issue
status: closed
closed_at: '2017-10-29T21:51:03+00:00'
---

# Original Description
* VERSIONS:     XMRig/2.4.2 libuv/1.14.1 gcc/6.3.0
 * HUGE PAGES:   unavailable, disabled
 * CPU:          AMD FX(tm)-8350 Eight-Core Processor            (1) -x64 AES-NI
 * CPU L2/L3:    8.0 MB/8.0 MB
 * THREADS:      2, cryptonight, av=1, donate=15%
 * POOL #1:      xmr-usa.dwarfpool.com:8050
 * COMMANDS:     hashrate, pause, resume
err:ntdll:RtlpWaitForCriticalSection section 0x7bcdc380 "loader.c: loader_section" wait timed out in thread 004d, blocked by 004b, retrying (60 sec)
err:ntdll:RtlpWaitForCriticalSection section 0x7bcdc380 "loader.c: loader_section" wait timed out in thread 004c, blocked by 004b, retrying (60 sec)
err:ntdll:RtlpWaitForCriticalSection section 0x7bcdc380 "loader.c: loader_section" wait timed out in thread 004e, blocked by 004b, retrying (60 sec)
err:ntdll:RtlpWaitForCriticalSection section 0x7bcdc380 "loader.c: loader_section" wait timed out in thread 004f, blocked by 004b, retrying (60 sec)
err:ntdll:RtlpWaitForCriticalSection section 0x7bcdc380 "loader.c: loader_section" wait timed out in thread 0051, blocked by 004b, retrying (60 sec)
err:ntdll:RtlpWaitForCriticalSection section 0x7bcdc380 "loader.c: loader_section" wait timed out in thread 0050, blocked by 004b, retrying (60 sec)
err:ntdll:RtlpWaitForCriticalSection section 0x7bcdc380 "loader.c: loader_section" wait timed out in thread 0052, blocked by 004b, retrying (60 sec)
err:ntdll:RtlpWaitForCriticalSection section 0x7bcdc380 "loader.c: loader_section" wait timed out in thread 0053, blocked by 004b, retrying (60 sec)
[2017-10-29 20:10:01] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-10-29 20:10:11] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-10-29 20:10:21] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-10-29 20:10:31] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-10-29 20:10:41] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s


# Discussion History
## MineMoneroPRO | 2017-10-29T18:13:19+00:00
Лютый изврат.

## shift-reality | 2017-10-29T18:29:59+00:00
конечно изврат, просто билд сделал на линуксе
Нужно как-то проверить, в винде такой ошибки нет, но и нет ниодного сообщения о принятой шаре(Такие должны быть?)

## MineMoneroPRO | 2017-10-29T18:31:48+00:00
Слишком низкий хешрейт для сложности на дварфе. Майнер просто не успевает найти шару.

Попробуйте на пуле с вар. диффом.

## shift-reality | 2017-10-29T18:40:16+00:00
Подскажите, пожалуйста такой пул... я новичек
сейчас получается 86 мх/с ( в винде все работает нормально )
и в винде 2 раза таки появилось accepted!)

Может еще вкурсе, почему на mingw была проблема с std::this_thread (я закинул какой-то патч, mingw-std-threads, и заинклудил в воркерах... вроде работает...) как-то можно обойтись без такого костыля?) если нет, то ничего ли он не сломает?) Т.к. кроссплатформенно ли, может в вине из-за него ошибки?

Туда-же: может знаете как собрать ехе с меньшим размером(сейчас 1.5мб)

## MineMoneroPRO | 2017-10-29T19:28:35+00:00
Такой пул уже был прописан в конфиге по умолчанию.
Так же весь список существующих пулов можно увидеть здесь: moneropools.com

Зачем Вы вообще кушаете кактус? https://github.com/xmrig/xmrig/releases

## shift-reality | 2017-10-29T20:03:03+00:00
Спасибо

# Action History
- Created by: shift-reality | 2017-10-29T18:11:46+00:00
- Closed at: 2017-10-29T21:51:03+00:00
