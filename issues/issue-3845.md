---
title: 'Monero ''Oxygen Orion'' (v0.17.3.0-release)  Error: Couldn''t connect to daemon:
  127.0.0.1:18081'
source_url: https://github.com/monero-project/monero-gui/issues/3845
author: ThomasAn73
assignees: []
labels: []
created_at: '2022-02-27T12:18:51+00:00'
updated_at: '2022-04-29T19:50:21+00:00'
type: issue
status: closed
closed_at: '2022-04-29T19:50:21+00:00'
---

# Original Description
I have a folder exception added to Windows Firewall. The Monero GUI was working fine for about four days. Now I keep getting the daemon connection error and has not been able to connect since.

# Discussion History
## selsta | 2022-02-27T14:19:55+00:00
Do you have a custom blockchain location set?

## ThomasAn73 | 2022-02-27T21:48:52+00:00
Yes. It's on a D: drive. It hasn't been moved or changed. It was installing the chain for the first time and there was a flag to prune the chain from the get go. The drive has a 125Gb capacity and I estimate the pruned chain should top at 45Gb. It had 60,000 transactions left to go, reached 42Gb and now it can't connect. 

## selsta | 2022-02-27T21:58:34+00:00
It sounds like your blockchain is corrupted. That can happen if you unplug the external hard drive during the initial sync. Is it possible that that happened?

## ThomasAn73 | 2022-02-27T22:35:12+00:00
No, nothing changed from the day before to the next. Drive was always connected. I had to stop the Daemon a few times to gain some bandwidth during conference calls, but it always restarted right up. Except now.

## ThomasAn73 | 2022-02-27T22:42:04+00:00
There was one time I had to kill the GUI. If the GUI is closed without first stopping the daemon then it never closes. There is a message saying stopping daemon and it stays there for hours indefinitely. After killing the GUI the daemon was working fine. Stopped, started and the chain kept downloading. That incident was three days before this current event. So, I don't see a connection.

## selsta | 2022-02-27T22:43:44+00:00
Yes, killing the GUI is irrelevant as it's a separate program to the daemon.

## ThomasAn73 | 2022-02-27T22:44:45+00:00
Also, even when it was connecting, it was not staying connected continuously. I thought I could leave it overnight so it finishes, but by morning the daemon was stopped and I had to restart it, but it kept going so I thought it was normal.

## selsta | 2022-02-27T22:47:36+00:00
Do you now how to start the daemon from `cmd`?

Open `cmd`, drag and drop monerod.exe into it and then add `--data-dir`, it should look similar to this:

`.\monerod.exe --data-dir D:\Custom\Blockchain\Path`

Change it to your custom path. Please try to start it manually like this and post the result.

## ThomasAn73 | 2022-02-27T22:54:27+00:00
2022-02-27 22:53:11.926 I Monero 'Oxygen Orion' (v0.17.3.0-release)
2022-02-27 22:53:11.926 I Initializing cryptonote protocol...
2022-02-27 22:53:11.926 I Cryptonote protocol initialized OK
2022-02-27 22:53:11.926 I Initializing core...
2022-02-27 22:53:11.926 I Loading blockchain from folder D:\MoneroBlockchain\lmdb ...
2022-02-27 22:53:11.942 W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2022-02-27 22:53:11.942 E Error opening database: Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2022-02-27 22:53:11.942 I Stopping cryptonote protocol...
2022-02-27 22:53:11.942 I Cryptonote protocol stopped successfully
2022-02-27 22:53:11.942 E Exception in main! Failed to initialize core

## selsta | 2022-02-27T22:55:46+00:00
Yes, looks corrupted.

You can try to add the `--db-salvage` flag in addition to the above command and it might fix itself, but it's not guaranteed.

## ThomasAn73 | 2022-02-27T22:58:44+00:00
No go. 
Delete the DB and restart ? Problem is I don't know what condition caused it, so it could happen again if nothing else changes.

## selsta | 2022-02-27T23:01:50+00:00
I assume it's an external hard drive? Most of the times it's either force shutdown computer during sync or unplugging the hard drive during sync.

You can add `--db-sync-mode safe` to your daemon startup flags, it will result in a slower sync but it should be impossible to corrupt the database.

Basically I would recommend to delete the lmdb folder and do:

`.\monerod.exe --data-dir D:\Custom\Blockchain\Path --db-sync-mode safe`

For the initial sync stay in CMD and don't use the GUI yet.

## ThomasAn73 | 2022-02-27T23:02:56+00:00
Will do. Thank you for the assistance and tips !

## ThomasAn73 | 2022-02-28T00:15:21+00:00
I am noticing the download is rather spotty even-though I have good internet connection. Is this type of behavior normal ? Saying "0 blocks synced in 90 min" ?
![Clipboard-1](https://user-images.githubusercontent.com/3271277/155906257-643ed068-4e4c-4073-a4cd-9b7acb8a9e68.jpg)



## selsta | 2022-02-28T00:19:25+00:00
Looks weird but it seems to sync fine. I would ignore it for now.

## damiendonnelly | 2022-04-29T14:56:32+00:00
The simple solution is to download the Monero CLI wallet as well, unzip it and run (right click, open with Terminal)"monerod".
This will start the Monero Daemon. Then try again from the GUI with the location specified and the start up flags "--db-sync-mode safe"

## selsta | 2022-04-29T19:50:21+00:00
Seems like no new issues showed up, closing.

# Action History
- Created by: ThomasAn73 | 2022-02-27T12:18:51+00:00
- Closed at: 2022-04-29T19:50:21+00:00
