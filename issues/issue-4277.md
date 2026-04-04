---
title: 'Monero GUI Wallet: Unable to connect to daemon after upgrading bind9 of Debian
  12'
source_url: https://github.com/monero-project/monero-gui/issues/4277
author: ch9PcB
assignees: []
labels: []
created_at: '2024-02-14T13:29:30+00:00'
updated_at: '2024-02-16T14:04:48+00:00'
type: issue
status: closed
closed_at: '2024-02-16T14:04:48+00:00'
---

# Original Description
My setup:

Debian 12.5, 64-bit, English
Monero GUI Wallet version 0.18.3.1 (Fluorine Fermi)

About twelve hours ago, Monero GUI Wallet's daemon was still able to sync.

However, after applying the security update of bind9 mentioned in [[SECURITY] [DSA 5621-1] bind9 security update](https://lists.debian.org/debian-security-announce/2024/msg00028.html), said daemon has been and still is unable to sync.

Please see the screenshot below.

On behalf of users of Debian 12 (Bookworm), I would appreciate it if @selsta could issue a fix soon. Thanks.


![Unable to connect to daemon after upgrading bind9 of Debian 12](https://github.com/monero-project/monero-gui/assets/24192216/9c8c4b75-f9cf-4b7b-845a-66d67475a866)



# Discussion History
## selsta | 2024-02-15T15:35:52+00:00
Can you share the output of Settings -> Info -> Wallet mode?

Also how did you install monero-gui? Website? Package manager?

I don't see how bind9 is related here.

## ch9PcB | 2024-02-15T21:22:52+00:00
> Can you share the output of Settings -> Info -> Wallet mode?
> 
Settings --> Info --> Wallet mode --> Advanced mode (Local node)

I have been using "Advanced mode (Local node)" since Day 1 of using your software (that was more than two years ago.)

> Also how did you install monero-gui? Website? Package manager?
> 
Debian 12.5 doesn't have a pacakge called monero-gui or Monero GUI Wallet.

Even if it has, I won't install monero-gui using Debian's package manager because packages in the stable repositories are often out-dated.

Below are the steps that I have been taking since two years ago:

1. Download Monero GUI Wallet using this URL: https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.18.3.1.tar.bz2
2. Un-tar it to a directory/folder of my choice
3. In a terminal, I run/launch the program as /home/username/monero/monero-wallet-gui
4. I enter the password when prompted

> I don't see how bind9 is related here.

Why not?

Before I upgraded the Debian's package called bind9 to the latest version, I was using version 1:9.18.19-1~deb12u1 which was released to the public on September 21, 2023.

My device was able to sync the daemon since September 21, 2023.

A few hours later, I upgraded bind9 to the latest version which is 1:9.18.24-1 (Please see Debian's changelog for bind9 by clicking the following link: https://metadata.ftp-master.debian.org/changelogs//main/b/bind9/bind9_9.18.24-1_changelog)

After the upgrade, the daemon failed to sync and the issue persists even at the time of writing this reply.

## selsta | 2024-02-15T21:24:42+00:00
Please share the output of starting monerod manually from terminal.

## ch9PcB | 2024-02-15T21:31:36+00:00
> Please share the output of starting monerod manually from terminal.

```
username@hostname:~/monero$ ./monerod
2024-02-15 21:25:39.298 I Monero 'Fluorine Fermi' (v0.18.3.1-release)
2024-02-15 21:25:39.298 I Initializing cryptonote protocol...
2024-02-15 21:25:39.298 I Cryptonote protocol initialized OK
2024-02-15 21:25:39.298 I Initializing core...
2024-02-15 21:25:39.298 I Loading blockchain from folder /home/username/.bitmonero/lmdb ...
2024-02-15 21:25:39.351 I Loading checkpoints
2024-02-15 21:25:39.351 I Core initialized OK
2024-02-15 21:25:39.351 I Initializing p2p server...
2024-02-15 21:25:39.352 I p2p server initialized OK
2024-02-15 21:25:39.352 I Initializing core RPC server...
2024-02-15 21:25:39.353 I Binding on 127.0.0.1 (IPv4):18081
2024-02-15 21:25:39.858 I core RPC server initialized OK on port: 18081
2024-02-15 21:25:39.868 I Starting core RPC server...
2024-02-15 21:25:39.868 I core RPC server started ok
2024-02-15 21:25:39.869 I Starting p2p net loop...
2024-02-15 21:25:40.870 I 
2024-02-15 21:25:40.870 I **********************************************************************                                                                          
2024-02-15 21:25:40.870 I The daemon will start synchronizing with the network. This may take a long time to complete.                                                    
2024-02-15 21:25:40.870 I                                                            
2024-02-15 21:25:40.870 I You can set the level of process detailization through "set_log <level|categories>" command,                                                    
2024-02-15 21:25:40.870 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).                                  
2024-02-15 21:25:40.870 I                                                            
2024-02-15 21:25:40.870 I Use the "help" command to see the list of available commands.                                                                                   
2024-02-15 21:25:40.870 I Use "help <command>" to see a command's documentation.     
2024-02-15 21:25:40.870 I **********************************************************************                                                                          
2024-02-15 21:25:48.390 I [82.153.138.165:18080 OUT] Sync data returned a new top block candidate: 1 -> 3085052 [Your node is 3085051 blocks (9.8 years) behind] 
2024-02-15 21:25:48.390 I SYNCHRONIZATION started                                                                                                                                                                 
2024-02-15 21:25:50.773 I Synced 101/3085052 (0%, 3084951 left)                                                                                                                                                   
2024-02-15 21:25:51.574 I Synced 201/3085052 (0%, 3084851 left)                                                                                                                                                   
2024-02-15 21:25:52.411 I Synced 301/3085052 (0%, 3084751 left)                                                                                                                                                   
2024-02-15 21:25:52.426 I Synced 401/3085052 (0%, 3084651 left)                                                                                                                                                   
2024-02-15 21:25:52.545 I Synced 501/3085052 (0%, 3084551 left)                                                                                                                                                   
2024-02-15 21:25:52.924 I Synced 601/3085052 (0%, 3084451 left)                                                                                                                                                   
2024-02-15 21:25:52.950 I Synced 701/3085052 (0%, 3084351 left)                                                                                                                                                   
2024-02-15 21:25:53.184 I Synced 801/3085052 (0%, 3084251 left)                                                                                                                                                   
2024-02-15 21:25:53.676 I Synced 901/3085052 (0%, 3084151 left) 
```

Strange.

The daemon is able to sync with your server(s).

[Sorry, I had to stop the daemon's syncing because I have not been able to sync for the past two days and I guess there are many blocks of data for the daemon to sync.]

My question is: Why is the daemon unable to sync when I launch/run monero-wallet-gui in a terminal?

## selsta | 2024-02-15T21:32:51+00:00
Do you usually have a custom blockchain location? If yes you have to try again with `--data-dir /path/to/custom/blockchain` and share the output.

## ch9PcB | 2024-02-15T21:34:50+00:00
> Do you usually have a custom blockchain location? If yes you have to try again with `--data-dir /path/to/custom/blockchain` and share the output.

Yes I do.

## selsta | 2024-02-15T21:35:53+00:00
I suspect your blockchain corrupted somehow. Did you force shutdown your machine around the time you updated bind9?

## ch9PcB | 2024-02-15T21:39:49+00:00
> I suspect your blockchain corrupted somehow. Did you force shutdown your machine around the time you updated bind9?

I can't remember if I forced the shutdown.

Suppose I did.

Can you help me please? Thanks.

## selsta | 2024-02-15T21:43:52+00:00
You have to either delete your blockchain data.mdb file, or restore one from backup if you have one. Then you have to start monero-gui and let it re-sync.

## ch9PcB | 2024-02-15T21:52:10+00:00
> You have to either delete your blockchain data.mdb file, or restore one from backup if you have one. Then you have to start monero-gui and let it re-sync.

Thanks for your advice.

I shall delete my blockchain's data.mdb file AND lock.mdb file as well.

I do weekly backups of my data.mdb file AND lock.mdb file and shall restore them to the usual custom location.

I shall feedback to you if your advice works.

On another topic....

I have this directory/folder called .bitmonero in this location: /home/username/.bitmonero

Said folder contains the following items:

```
lmdb (sub-directory containing data.mdb and lock.mdb)
bitmonero.log
monero-wallet-gui.log
p2pstate.bin
rpc_ssl.crt
rpc_ssl.key
```

Can I delete all of the above sub-directory and files please?

My custom location is in a separate drive called /media/username/.......

Thanks again for your help.



## selsta | 2024-02-15T21:54:23+00:00
> I do weekly backups of my data.mdb file AND lock.mdb file and shall restore them to the usual custom location.

Yes, though the lock.mdb file will be generated by monerod, so you can delete existing data.mdb + lock.mdb and restore your backed up data.mdb file.

> Can I delete all of the above sub-directory and files please?

Yes, it got created after you started monerod without --data-dir flag. You can delete it.

## ch9PcB | 2024-02-15T21:56:45+00:00
> > I do weekly backups of my data.mdb file AND lock.mdb file and shall restore them to the usual custom location.

> Yes, it got created after you started monerod without --data-dir flag. You can delete it.

Thanks for your reply.

I shall go offline now to copy my data.mdb file AND lock.mdb file from my backup to my usual custom location.

I shall feedback here if my issue is resolved (or not).



## ch9PcB | 2024-02-16T01:50:55+00:00
@selsta 

The instructions contained in your advice worked. The daemon on my device could sync.

I found out that data.mdb in my custom location was corrupt not because of a forced shutdown.

The reason is that my external storage contained disk errors and bad clusters and I had to run the following command in a terminal with admin privilege under Microsoft Windows to fix them:

chkdsk /r /f h:

After Microsoft Windows had fixed my external storage, I was then able to delete data.mdb and copy its backup to my custom location.

Next, I booted into Debian 12.5, launched monero-wallet-gui and the daemon could sync.

_Conclusion:_ Disk errors and bad clusters in my external storage where data.mdb is located caused the daemon of Monero GUI Wallet unable to sync. The issue was not due to the upgrading of the Debian package bind9.

## selsta | 2024-02-16T14:04:48+00:00
Closing as your issue is resolved.

# Action History
- Created by: ch9PcB | 2024-02-14T13:29:30+00:00
- Closed at: 2024-02-16T14:04:48+00:00
