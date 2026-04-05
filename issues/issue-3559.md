---
title: Can you help with malware version of xmrig ?
source_url: https://github.com/xmrig/xmrig/issues/3559
author: Posoroko
assignees: []
labels:
- av
created_at: '2024-10-07T09:17:14+00:00'
updated_at: '2025-06-16T19:41:14+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:41:14+00:00'
---

# Original Description
Hi all ! 
I understand that your software is legit.  I'm sorry that people are using it in  a bad way. I'm into opensource myself.

I just realized that xmrig is running on my machine.  But I can't find where it's installed.  I found a process called DIHost.exe and when I try to delete it, windows says: "can't delete because it's running in xmrig.exe.

If I open task manager, DIHost.exe shuts down and I can delete it,  but I feel like xmrig is still there, somewhere else.

Can you help me figuring thjis out ? I've ran webdoctor's cureit sac and it identified DIHost.exe as a threat, but it didn't  find xmrig.

It would be nice to create some resource to help people deal with malware versions.  I'd be glad to help putting it together if you guys are up for it.

# Discussion History
## jianmingyong | 2024-11-22T01:13:26+00:00
While Xmrig is not a malware per se, it can be used as a means to be a malware by hiding it in a hidden folder with well known names that you probably wouldn’t notice.

You will probably need to find the main source of the malware, usually hidden in C:/Users/<user>/AppData/Roaming/Dll (which you can’t find as they make the folder system related even hiding when you show hidden folder). By finding the root exe that generates the fake xmrig, you can then remove it easily off your system.

(Also you can get a hint by looking at the startup section in the Task Manager for unusual name like DllHost or something microsoft related. They like to hide them using such names)

# Action History
- Created by: Posoroko | 2024-10-07T09:17:14+00:00
- Closed at: 2025-06-16T19:41:14+00:00
