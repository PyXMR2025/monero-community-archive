---
title: keep getting this error -- > no active pools, stop mining
source_url: https://github.com/xmrig/xmrig/issues/3371
author: AbianTang
assignees: []
labels: []
created_at: '2023-12-04T16:43:12+00:00'
updated_at: '2025-06-18T22:31:20+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:31:20+00:00'
---

# Original Description
bug still pressent in version 6.21.0 of xmrig , running on mac m3 pro and windows10

023-12-05 00:36:05.752]  miner    speed 10s/60s/15m 2393.0 2376.3 2611.0 H/s max 2882.0 H/s
[2023-12-05 00:37:04.153]  net      no active pools, stop mining
[2023-12-05 00:37:05.879]  miner    speed 10s/60s/15m 1936.3 2330.4 2597.7 H/s max 2882.0 H/s
[2023-12-05 00:37:11.547]  net      use pool randomxmonero.auto.nicehash.com:443 TLSv1.3 
[2023-12-05 00:37:11.547]  net      fingerprint (SHA-256): ""
[2023-12-05 00:37:11.547]  net      new job from randomxmonero.auto.nicehash.com:443 diff 131076 algo rx/0 height 134443
[2023-12-05 00:38:06.056]  miner    speed 10s/60s/15m 2355.8 2084.8 2548.2 H/s max 2882.0 H/s
[2023-12-05 00:38:32.277]  net      no active pools, stop mining
[2023-12-05 00:38:38.466]  net      use pool randomxmonero.auto.nicehash.com:443 TLSv1.3 198.18.0.145
[2023-12-05 00:38:38.466]  net      fingerprint (SHA-256): "a7bc29017c3d564fdbfd3e984891f"


# Discussion History
## SlavisaBakic | 2023-12-04T21:19:10+00:00
> bug still pressent in version 6.21.0 of xmrig , running on mac m3 pro and windows10
> 
> 023-12-05 00:36:05.752] miner speed 10s/60s/15m 2393.0 2376.3 2611.0 H/s max 2882.0 H/s [2023-12-05 00:37:04.153] net no active pools, stop mining [2023-12-05 00:37:05.879] miner speed 10s/60s/15m 1936.3 2330.4 2597.7 H/s max 2882.0 H/s [2023-12-05 00:37:11.547] net use pool randomxmonero.auto.nicehash.com:443 TLSv1.3 [2023-12-05 00:37:11.547] net fingerprint (SHA-256): "" [2023-12-05 00:37:11.547] net new job from randomxmonero.auto.nicehash.com:443 diff 131076 algo rx/0 height 134443 [2023-12-05 00:38:06.056] miner speed 10s/60s/15m 2355.8 2084.8 2548.2 H/s max 2882.0 H/s [2023-12-05 00:38:32.277] net no active pools, stop mining [2023-12-05 00:38:38.466] net use pool randomxmonero.auto.nicehash.com:443 TLSv1.3 198.18.0.145 [2023-12-05 00:38:38.466] net fingerprint (SHA-256): "a7bc29017c3d564fdbfd3e984891f"

Please ignore spam message above. Please try another mining pool and see if same problem persist. If not, it is issue on NiceHash side.

## geekwilliams | 2023-12-05T08:58:15+00:00
@StelimslimDEV mate your site appears to be down. You sure it's not spam? 

@SlavisaBakic has the best answer. 

## viponedream | 2023-12-09T23:38:39+00:00
same issue,  some pool have this issue, 
the miner should keep longer to wait for notify
the pool still send data, just slower some time.


## koitsu | 2024-01-14T23:12:52+00:00
> same issue, some pool have this issue, the miner should keep longer to wait for notify the pool still send data, just slower some time.

This might be configurable through the currently-undocumented `--daemon-job-timeout` flag (or in JSON config, `daemon-job-timeout` parameter in the `pool` section).  The value is in milliseconds and defaults to 15000 (i.e. 15 seconds).  I will be submitting a PR for the author to update documentation to reflect this flag/parameter.

However, I cannot immediately tell from the XMRig source code whether or not this would apply to the OP's situation, as it's clear more than 15 seconds has transpired between new job + report of "no active pools".  Packet captures would ultimately tell what is going on (and plaintext is preferred for this, as TLS-based connectivity cannot be reviewed for payload request/response behaviours).

## sergik7777 | 2024-02-10T19:28:58+00:00
![Снимок экрана (1)](https://github.com/xmrig/xmrig/assets/159652031/875a7418-b4c4-4d19-86b9-6f9e67fef363)
что за проблема???? и как ее решить???

## sergik7777 | 2024-02-10T19:30:10+00:00
бывало запускался с 10 раза ! сейчас вобще не запускается майнер


## geekwilliams | 2024-02-10T19:50:18+00:00
пожалуйста, удалите stratum+ssl:// и порт (:443) из командной строки и повторите попытку.

## sergik7777 | 2024-02-10T19:56:48+00:00
> пожалуйста, удалите stratum+ssl:// и порт (:443) из командной строки и повторите попытку.

та же беда!

## geekwilliams | 2024-02-10T20:01:07+00:00
Можете ли вы подключиться к rx.unmineable.com с помощью браузера на том же компьютере? Если нет, то у вас проблема с сетью или ваш интернет-провайдер может блокировать домен.

## sergik7777 | 2024-02-10T20:05:29+00:00
> Можете ли вы подключиться к rx.unmineable.com с помощью браузера на том же компьютере? Если нет, то у вас проблема с сетью или ваш интернет-провайдер может блокировать домен.

не заходит на сайт!


## geekwilliams | 2024-02-10T20:07:19+00:00
Попробуйте другой пул и посмотрите, сработает ли он.

## sergik7777 | 2024-02-10T20:07:41+00:00



> Можете ли вы подключиться к rx.unmineable.com с помощью браузера на том же компьютере? Если нет, то у вас проблема с сетью или ваш интернет-провайдер может блокировать домен.

а как обойти блокировку?

## sergik7777 | 2024-02-10T20:17:06+00:00
с другим пулом все также!

> Попробуйте другой пул и посмотрите, сработает ли он.

с другим пулом все также!


## sergik7777 | 2024-02-10T21:13:05+00:00
> Можете ли вы подключиться к rx.unmineable.com с помощью браузера на том же компьютере? Если нет, то у вас проблема с сетью или ваш интернет-провайдер может блокировать домен.

впн установил все запустилось!  благодарю за помощь!

# Action History
- Created by: AbianTang | 2023-12-04T16:43:12+00:00
- Closed at: 2025-06-18T22:31:20+00:00
