---
title: Violación de segmento (`core' generado)
source_url: https://github.com/xmrig/xmrig/issues/1680
author: daqm3d
assignees: []
labels: []
created_at: '2020-05-18T06:19:58+00:00'
updated_at: '2020-08-19T01:21:12+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:21:12+00:00'
---

# Original Description
tengo un problema al ejecutar el compilador , cuando  se ejecuta siempre sale Violación de segmento (`core' generado)

- eh estado probando las configuraciones y diversos factores pero no logro resolver 

- aqui dejo el mensaje que me sale en la consola :

[2020-05-17 21:53:24.242]  net  use pool xmr.pool.minergate.com:45700  88.99.142.163
[2020-05-17 21:53:24.242]  net  new job from xmr.pool.minergate.com:45700 diff 2000 algo rx/0 height 2100818
[2020-05-17 21:53:24.242]  rx   init dataset algo rx/0 (4 threads) seed c703171b2934606a...
[2020-05-17 21:53:24.242]  rx   not enough memory for RandomX dataset
[2020-05-17 21:53:24.243]  rx   failed to allocate RandomX dataset, switching to slow mode (1 ms)
[2020-05-17 21:53:27.502]  rx   dataset ready (3259 ms)
[2020-05-17 21:53:27.502]  cpu  use profile  rx  (2 threads) scratchpad 2048 KB
Violación de segmento (`core' generado)
![Captura de pantalla de 2020-05-17 21-13-29](https://user-images.githubusercontent.com/34916431/82180129-e8c1ca80-98ad-11ea-9d74-850a003a09d9.png)




# Discussion History
## trasherdk | 2020-05-18T15:00:52+00:00
So, what was your question ?

## daqm3d | 2020-05-18T21:30:52+00:00
why it gives this error Violación de segmento (`core' generado)

# Action History
- Created by: daqm3d | 2020-05-18T06:19:58+00:00
- Closed at: 2020-08-19T01:21:12+00:00
