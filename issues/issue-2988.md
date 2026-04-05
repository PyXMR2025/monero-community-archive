---
title: error con unmineable CPU
source_url: https://github.com/xmrig/xmrig/issues/2988
author: Nano2400
assignees: []
labels: []
created_at: '2022-03-24T03:56:07+00:00'
updated_at: '2025-06-28T10:42:16+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:42:16+00:00'
---

# Original Description
Buen dia, 
Solicito ayuda con estos errores que no me deja avanzar 

[2022-03-23 22:40:20.049]  net      use pool rx.unmineable.com:3333  139.59.164.251

[2022-03-23 22:40:20.050]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2586347 (37 tx)

[2022-03-23 22:40:20.050]  cpu      use argon2 implementation SSSE3

[2022-03-23 22:40:20.051]  msr      to access MSR registers Administrator privileges required.

[2022-03-23 22:40:20.051]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

[2022-03-23 22:40:20.051]  randomx  init dataset algo rx/0 (4 threads) seed a2d54c5c46912044...

[2022-03-23 22:40:20.071]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (20 ms)


# Discussion History
## Noeleth | 2022-03-31T07:46:47+00:00
En principio deberías ejecutar el programa en modo administrador 

# Action History
- Created by: Nano2400 | 2022-03-24T03:56:07+00:00
- Closed at: 2025-06-28T10:42:16+00:00
