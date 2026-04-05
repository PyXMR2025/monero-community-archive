---
title: Xmrig report is running in a VM
source_url: https://github.com/xmrig/xmrig/issues/3658
author: fantas21
assignees: []
labels:
- question
created_at: '2025-05-15T03:58:18+00:00'
updated_at: '2025-06-16T15:07:43+00:00'
type: issue
status: closed
closed_at: '2025-06-16T15:07:43+00:00'
---

# Original Description
**Describe the bug**
Xmrig report is running in VM and don't recognize L3 cache.

**To Reproduce**
run xmrig in 11th Gen Intel(R) Core(TM) i9-11980HK.

**Expected behavior**
Is not a VM, is a genuine intel cpu.

**Required data**
-  
 - XMRig version 6.22.2 MSVC/2019 (built for Windows x86-64, 64 bit)
 - 
    https://github.com/xmrig/xmrig/releases/download/v6.22.2/xmrig-6.22.2-msvc-win64.zip
-   
  - Miner log 
  
[log.txt](https://github.com/user-attachments/files/20219380/log.txt)

  - Config file or command line (without wallets)
  
[config.json](https://github.com/user-attachments/files/20219381/config.json)


 - OS: 
Edición	Windows 11 Pro
Versión	24H2
Instalado el	‎24/‎11/‎2024
Versión del sistema operativo	26100.3915
Experiencia	Paquete de experiencia de características de Windows 1000.26100.83.0



**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2025-05-15T06:17:02+00:00
You have virtualization enabled in BIOS. You need to find the corresponding option and disable it.

# Action History
- Created by: fantas21 | 2025-05-15T03:58:18+00:00
- Closed at: 2025-06-16T15:07:43+00:00
