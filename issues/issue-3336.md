---
title: Getting only one file.
source_url: https://github.com/xmrig/xmrig/issues/3336
author: ghost
assignees: []
labels: []
created_at: '2023-09-21T14:57:04+00:00'
updated_at: '2025-06-18T22:20:52+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:20:52+00:00'
---

# Original Description
If i download your file and open the ZIP in finder it open some folder and when i open the folder i get only one file. 

When i was looking to some tutorials i saw 3 files, and in 2 of them you make some changes and those 2 files i do not have.

My computer is Mac running on Intel 5.

I did everithinng like in tutorial and do it like 8 times to be sure.

Thank you for help. Maybe im doing somethinng wrong.

<img width="523" alt="Snímek obrazovky 2023-09-21 v 16 38 07" src="https://github.com/xmrig/xmrig/assets/145689703/7a15976d-40a5-435b-bf28-36871f483479">
<img width="415" alt="Snímek obrazovky 2023-09-21 v 16 41 07" src="https://github.com/xmrig/xmrig/assets/145689703/feea5d9b-0706-4a01-9b2c-5cf5d5b6418e">
<img width="632" alt="Snímek obrazovky 2023-09-21 v 16 42 42" src="https://github.com/xmrig/xmrig/assets/145689703/e42fa523-8d42-4bc1-bfa4-cb2867785692">
<img width="732" alt="Snímek obrazovky 2023-09-21 v 16 44 29" src="https://github.com/xmrig/xmrig/assets/145689703/112d041a-4921-4bdf-8a31-a592887bfb77">
<img width="719" alt="Snímek obrazovky 2023-09-21 v 16 45 46" src="https://github.com/xmrig/xmrig/assets/145689703/9196ec54-d8d5-4988-8a7d-fc4df623d01f">
<img width="1440" alt="Snímek obrazovky 2023-09-21 v 16 51 56" src="https://github.com/xmrig/xmrig/assets/145689703/8e245842-5387-42cc-832f-9927a6415298">
<img width="648" alt="Snímek obrazovky 2023-09-21 v 16 52 49" src="https://github.com/xmrig/xmrig/assets/145689703/eebeef57-4516-44d9-b370-22b4ec4f14e0">



# Discussion History
## SChernykh | 2023-09-21T16:19:51+00:00
This must be antivirus triggering - they don't like any mining software. Try to add the download folder to antivirus exceptions, then download xmrig again.

## ghost | 2023-09-21T18:26:06+00:00
> This must be antivirus triggering - they don't like any mining software. Try to add the download folder to antivirus exceptions, then download xmrig again.

Hello, thank you for your answer. I just open my antivirus and I saw that he blocked that 2 files everytime i download them. He put them to quarantine, beacue they contain **Trojan** viruses. **_Do you think that is save to open them?_**

## SChernykh | 2023-09-21T18:32:15+00:00
You can download [SHA256SUMS](https://github.com/xmrig/xmrig/releases/download/v6.20.0/SHA256SUMS) and double check that the archive you downloaded has the correct SHA256. If it's correct, you shouldn't worry. Antiviruses always say "Trojan/Malware/Miner" or something like this about XMRig, and even just Monero wallet software.

## ghost | 2023-09-22T06:51:47+00:00
Thank you very much, I just download the SHA256SUMS, but Im not really sure what should I compare. 

I see it like this now:

<img width="1358" alt="Snímek obrazovky 2023-09-22 v 8 49 10" src="https://github.com/xmrig/xmrig/assets/145689703/42ea5acc-d6f6-4f21-ac92-25972694b978">


## SChernykh | 2023-09-22T06:53:34+00:00
You should compare the sha256 of .tar.gz archive that you downloaded. Don't unpack it, check sha256 first.

## ghost | 2023-09-22T11:38:44+00:00
> You should compare the sha256 of .tar.gz archive that you downloaded. Don't unpack it, check sha256 first.

Maybe im little bit dumb, but **what** on the sha256 should i check? (code, size, name)

# Action History
- Created by: ghost | 2023-09-21T14:57:04+00:00
- Closed at: 2025-06-18T22:20:52+00:00
