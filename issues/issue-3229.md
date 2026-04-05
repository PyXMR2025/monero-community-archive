---
title: ETH is going really slowly to the account
source_url: https://github.com/xmrig/xmrig/issues/3229
author: MarcelKite
assignees: []
labels: []
created_at: '2023-03-24T07:49:50+00:00'
updated_at: '2025-06-18T22:44:48+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:44:48+00:00'
---

# Original Description
**Describe the bug**
Some time ago miner was working perfect and now it's really slow.


 OS: macOS Catalina version 10.15.7

![ok](https://user-images.githubusercontent.com/128785973/227456158-0e399e2b-7de2-4e8c-a6d2-b4c46c0ecffe.png)
![config](https://user-images.githubusercontent.com/128785973/227456955-ef9d0576-a6f2-4fda-9290-57d879fe6ad8.png)
![log](https://user-images.githubusercontent.com/128785973/227457268-04dd477a-19cf-4e86-b14d-f93fcbd3f909.png)


# Discussion History
## SChernykh | 2023-03-24T07:55:26+00:00
You don't have huge pages and MSR mod working. Change "wrmsr" to true in config.json, reboot to free RAM and run xmrig as root before any other program.

## MarcelKite | 2023-03-24T08:04:27+00:00
Thx it's working now!!!
![ok](https://user-images.githubusercontent.com/128785973/227460802-b973aad8-9f42-4812-a242-b66a16387c75.png)


## MarcelKite | 2023-03-24T08:05:17+00:00
And I have an question how to use 100% of cpu?


## SChernykh | 2023-03-24T08:06:58+00:00
It's not really working, you still have "11% 128/1168" in yellow. You need to clean up your system and free some more RAM, because XMRig shows 5.1/8.0 GB used when it starts. Also, I still don't see MSR mod working.

## MarcelKite | 2023-03-24T08:46:45+00:00
![ok](https://user-images.githubusercontent.com/128785973/227469675-5f09f44f-743b-4f6e-b86e-ae6a309a4f87.png)


## SChernykh | 2023-03-24T08:59:38+00:00
Oh, I forgot that you're on macOS. MSR mod is only supported on Windows and Linux. You need to fix huge pages (by freeing RAM and removing some apps from autostart) and you're good.

## MarcelKite | 2023-03-24T09:21:13+00:00
OK THX

## MarcelKite | 2023-03-24T09:42:05+00:00
![Zrzut ekranu 2023-03-24 o 09 41 35](https://user-images.githubusercontent.com/128785973/227483900-3caf4b0c-9d81-4ce8-819b-90d4e78eee0a.png)
It works now

# Action History
- Created by: MarcelKite | 2023-03-24T07:49:50+00:00
- Closed at: 2025-06-18T22:44:48+00:00
