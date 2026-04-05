---
title: Remove xmrig icon
source_url: https://github.com/xmrig/xmrig/issues/1758
author: kiliangui
assignees: []
labels:
- question
created_at: '2020-06-30T14:26:31+00:00'
updated_at: '2020-08-19T00:45:56+00:00'
type: issue
status: closed
closed_at: '2020-08-19T00:45:56+00:00'
---

# Original Description
hello ! I need to remove the xmrig icon . I download "ressournce hacker" and delete the icon folder. the .exe file as no icon but when i run xmrig , the icon is here in my task manager. can you help me to remove xmrig icon ?
![image](https://user-images.githubusercontent.com/67644676/86138165-648a7600-baee-11ea-82d0-6c7bcdba6115.png)


# Discussion History
## snipeTR | 2020-06-30T15:16:32+00:00
dont delete. just clange.
and refresh icon cache.

## kerinlive | 2020-07-14T14:28:00+00:00
Icon and other meta data succesful change in resource hacker. If you want to hide xmrig from taskmanager you may get any system executable file such as explorer.exe, export all resources data from it as *.res file, and next you need to import res file to xmrig.exe. make sure that you select all need resources to change. And check the Overwrite point on popup window when you make selection of resources that you want to import. Resources hacker success do this changes all time with xmrig. Process Name that shows in taskmgr, software vendor, licensing data, and other data of process can be changed in manifest tab in reshack. Try.

## kerinlive | 2020-07-14T14:29:48+00:00
And dont use *.rc resource file. It may not import res data correctly. Only .*res files

# Action History
- Created by: kiliangui | 2020-06-30T14:26:31+00:00
- Closed at: 2020-08-19T00:45:56+00:00
