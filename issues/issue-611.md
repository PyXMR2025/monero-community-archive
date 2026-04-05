---
title: Add StartUp XMRIG
source_url: https://github.com/xmrig/xmrig/issues/611
author: LearnMiner
assignees: []
labels: []
created_at: '2018-05-06T19:53:45+00:00'
updated_at: '2018-06-17T18:08:50+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:08:50+00:00'
---

# Original Description
How can i add StartUp XMRIG in Regedit? I tried 

void Startup(TCHAR* path) {
	HKEY hKey = NULL;
	RegOpenKey(HKEY_CURRENT_USER, L"Software\\Microsoft\\Windows\\CurrentVersion\\Run", &hKey);
	RegSetValueEx(hKey, L"xmrig miner", 0, REG_SZ, (PBYTE)path, lstrlen(path) * sizeof(TCHAR) + 1);
	RegCloseKey(hKey);
}

But when i compile and open exe no add in regedit :(

# Discussion History
## snipeTR | 2018-05-06T21:27:09+00:00
your bestard hacker (lamer)

# Action History
- Created by: LearnMiner | 2018-05-06T19:53:45+00:00
- Closed at: 2018-06-17T18:08:50+00:00
