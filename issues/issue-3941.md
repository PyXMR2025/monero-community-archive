---
title: Cannot change blockchain location
source_url: https://github.com/monero-project/monero-gui/issues/3941
author: CountCypher
assignees: []
labels: []
created_at: '2022-06-07T15:31:04+00:00'
updated_at: '2022-06-16T14:46:49+00:00'
type: issue
status: closed
closed_at: '2022-06-16T14:45:20+00:00'
---

# Original Description
I'm using Monero GUI Wallet 0.17.3.2 in Advanced mode (Local node) on Fedora 35. I would like to change the blockchain location to another drive in my PC, because my system partition is running out of space.

To achieve this, I did the following:
1. Waited until wallet and daemon are synchronized
2. Stopped daemon under "Settings" > "Node"
3. Closed wallet and exited Monero GUI
4. Started Monero GUI again and chose "Use custom settings"
5. Changed the blockchain location by using the file picker dialogue

...and now I receive this warning:

![moneroGUI_warning](https://user-images.githubusercontent.com/54265000/172419396-24a067c1-2246-4a85-8e4d-df033f8b8647.png)

This is odd, because the drive (a NTFS drive at mount point "/mnt/9412e124-079b-498a-93b5-91a46394cb13") has ~127 GB free:

```
martin on linux-pc in /mnt/9412e124-079b-498a-93b5-91a46394cb13🔒 
❯ df -h
Dateisystem    Größe Benutzt Verf. Verw% Eingehängt auf
devtmpfs        4,0M       0  4,0M    0% /dev
tmpfs           5,9G    1,5M  5,9G    1% /dev/shm
tmpfs           2,4G    2,1M  2,4G    1% /run
/dev/sda4       107G     96G  5,6G   95% /
tmpfs           5,9G    3,5M  5,9G    1% /tmp
/dev/sdb2       295G    153G  127G   55% /mnt/9412e124-079b-498a-93b5-91a46394cb13
/dev/sdb1       632G    513G  119G   82% /mnt/01D324F9D6684290
tmpfs           1,2G    2,8M  1,2G    1% /run/user/1000
```

If I dismiss the warning, the new location is taken over:

![moneroGUI_Node_settings_cropped](https://user-images.githubusercontent.com/54265000/172420346-e98ca9ae-9756-4b55-8036-bff7d9e78a8c.png)

If I now start the daemon, I get continuous errors that the daemon cannot be connected to:

```
[07.06.22 17:04] 2022-06-07 15:04:37.428 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[07.06.22 17:09] 2022-06-07 15:09:34.201 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[07.06.22 17:09] 2022-06-07 15:09:40.061 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[07.06.22 17:09] 2022-06-07 15:09:44.628 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Error: Couldn't connect to daemon: 127.0.0.1:18081
```

It might be that it's a permission problem, but I don't see a difference between the original folder...

```
martin on linux-pc in .var/app/org.getmonero.Monero 
❯ ls -la .bitmonero/
insgesamt 36468
drwxr-xr-x. 3 martin martin     4096 16. Nov 2021  .
drwxr-xr-x. 7 martin martin     4096 16. Nov 2021  ..
-rw-r--r--. 1 martin martin 33315985  7. Jun 17:11 bitmonero.log
drwxr-xr-x. 2 martin martin     4096  7. Jun 16:37 lmdb
-rw-r--r--. 1 martin martin  3858402  7. Jun 17:09 monero-wallet-gui.log
-rw-r--r--. 1 martin martin   147263  7. Jun 17:00 p2pstate.bin
```

...and the new location:

```
martin on linux-pc in /mnt/9412e124-079b-498a-93b5-91a46394cb13🔒 
❯ ls -la monero/
insgesamt 20
drwxr-xr-x. 3 martin martin 4096  7. Jun 17:09 .
drwxr-xr-x. 8 root   root   4096 30. Mai 12:01 ..
-rw-------. 1 martin martin 5319  7. Jun 17:09 bitmonero.log
drwx------. 2 martin martin 4096  7. Jun 17:09 lmdb
```

What I find strange is that Monero GUI takes over this path as new location:
`/run/user/1000/doc/7d3be5a0/monero`
Could it be that the program believes that there's only 1.2GB free on that drive because the path points to tmpfs (according to `df -h` output above)? I'm not familiar enough with how this works in detail unfortunately. :frowning_face:  Is there any way to tell Monero GUI the "correct" location? Or is it a permissions issue? Any help highly appreciated, thanks in advance. 


# Discussion History
## selsta | 2022-06-07T17:59:32+00:00
Can you try starting monerod manually with `--data-dir` flag and see what kind of error messages you get, or if it works?

## CountCypher | 2022-06-07T18:25:41+00:00
Sorry for asking such a basic thing, but were can I find the monerod CLI program? I've installed Monero GUI as flatpak and I can't find monerod neither in the binaries path nor in `.var/app/org.getmonero.Monero` and its subfolders.

EDIT: I've found it. It's located in `/var/lib/flatpak/app/org.getmonero.Monero/x86_64/stable/26ca152e0772bca75346779c0712ae8ecf93452f3542cf255c42c0862c2fb0a6/files/bin/`. Not very obvious. :wink: 
But I have trouble executing the binary:

```
martin on linux-pc in 26ca152e0772bca75346779c0712ae8ecf93452f3542cf255c42c0862c2fb0a6/files/bin🔒 
❯ ./monerod --help
./monerod: error while loading shared libraries: libboost_chrono.so.1.79.0: cannot open shared object file: No such file or directory

```

## q7nm | 2022-06-08T11:16:24+00:00
Hello! Try this:
```
flatpak override --user --filesystem=/mnt/9412e124-079b-498a-93b5-91a46394cb13 org.getmonero.Monero
```

## q7nm | 2022-06-08T11:32:08+00:00
> Sorry for asking such a basic thing, but were can I find the monerod CLI program? I've installed Monero GUI as flatpak and I can't find monerod neither in the binaries path nor in `.var/app/org.getmonero.Monero` and its subfolders.
> 
> EDIT: I've found it. It's located in `/var/lib/flatpak/app/org.getmonero.Monero/x86_64/stable/26ca152e0772bca75346779c0712ae8ecf93452f3542cf255c42c0862c2fb0a6/files/bin/`. Not very obvious. wink But I have trouble executing the binary:
> 
> ```
> martin on linux-pc in 26ca152e0772bca75346779c0712ae8ecf93452f3542cf255c42c0862c2fb0a6/files/bin🔒 
> ❯ ./monerod --help
> ./monerod: error while loading shared libraries: libboost_chrono.so.1.79.0: cannot open shared object file: No such file or directory
> ```

You can run `monerod` like this:
```
flatpak run --command=monerod org.getmonero.Monero
```

OR:
```
flatpak run --command=bash org.getmonero.Monero
```
And run something in the sandbox.

## selsta | 2022-06-08T11:35:33+00:00
@BigmenPixel0 does setting a custom blockchain location usually work with monero-gui installed via flatpak?

## q7nm | 2022-06-08T11:37:25+00:00
> @BigmenPixel0 does setting a custom blockchain location usually work with monero-gui installed via flatpak?

It should, but you must manually allow access to the required directory.

## selsta | 2022-06-08T11:39:11+00:00
Ok, then ignore my suggestion with running monerod manually @CountCypher. I didn't know that it was a flatpak sandboxing (?) related issue.

## CountCypher | 2022-06-08T11:57:58+00:00
> Hello! Try this:
> 
> ```
> flatpak override --user --filesystem=/mnt/9412e124-079b-498a-93b5-91a46394cb13 org.getmonero.Monero
> ```

Thanks @BigmenPixel0, that did the trick as it seems. Node is synchronizing right now in the new location. :smile: 
One more question: Was this a "one time command" to add the drive to flatpak sandboxing or do I need to repeat this command, for example after every reboot, before I start Monero GUI?


## q7nm | 2022-06-08T12:00:30+00:00
> > Hello! Try this:
> > ```
> > flatpak override --user --filesystem=/mnt/9412e124-079b-498a-93b5-91a46394cb13 org.getmonero.Monero
> > ```
> 
> Thanks @BigmenPixel0, that did the trick as it seems. Node is synchronizing right now in the new location. smile One more question: Was this a "one time command" to add the drive to flatpak sandboxing or do I need to repeat this command, for example after every reboot, before I start Monero GUI?

Once is enough. (you have already entered this command, no more)

## CountCypher | 2022-06-14T13:27:27+00:00
An update on the local node synchronization progress:
The daemon has been running now for more than 60 hours. While the process seemed to run quite quickly in the beginning, it seemed to get slower and slower once it passed the 80%. That is, it took almost 12 hours to go from 98.6% to 98.8%:

```
>>> status
[12.06.22 11:01] 2022-06-12 09:01:16.439 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Height: 2276136/2644065 (86.1%) on mainnet, not mining, net hash 1.93 GH/s, v14, 10(out)+0(in) connections, uptime 0d 17h 59m 54s
>>> status
[12.06.22 12:25] 2022-06-12 10:25:46.129 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Height: 2320728/2644108 (87.8%) on mainnet, not mining, net hash 2.21 GH/s, v14, 12(out)+0(in) connections, uptime 0d 19h 24m 24s
>>> status
[12.06.22 15:34] 2022-06-12 13:34:46.301 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Height: 2377164/2644194 (89.9%) on mainnet, not mining, net hash 2.36 GH/s, v14, 13(out)+0(in) connections, uptime 0d 22h 33m 25s
>>> status
[12.06.22 17:14] 2022-06-12 15:14:09.720 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Height: 2411964/2644244 (91.2%) on mainnet, not mining, net hash 2.40 GH/s, v14, 13(out)+0(in) connections, uptime 1d 0h 12m 50s
>>> status
[12.06.22 21:05] 2022-06-12 19:05:29.876 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Height: 2466496/2644359 (93.3%) on mainnet, not mining, net hash 2.73 GH/s, v14, 12(out)+0(in) connections, uptime 1d 4h 4m 10s
>>> status
[13.06.22 07:06] 2022-06-13 05:06:08.354 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Height: 2543556/2644635 (96.2%) on mainnet, not mining, net hash 3.28 GH/s, v14, 12(out)+0(in) connections, uptime 1d 14h 4m 51s
>>> status
[13.06.22 18:35] 2022-06-13 16:33:43.202 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Height: 2608836/2644992 (98.6%) on mainnet, not mining, net hash 3.07 GH/s, v14, 13(out)+0(in) connections, uptime 2d 1h 33m 54s
>>> status
[14.06.22 06:23] 2022-06-14 04:20:20.734 I Monero 'Oxygen Orion' (v0.17.3.2-unknown)
Height: 2614876/2645329 (98.8%) on mainnet, not mining, net hash 3.02 GH/s, v14, 12(out)+0(in) connections, uptime 2d 13h 21m 39s
```
![monerod_status](https://user-images.githubusercontent.com/54265000/173587898-c2843aed-c702-4d44-a6d4-7eaa794cef66.png)

Is that normal?
Btw, the blockchain location is on a HDD, not a SSD, but I'm still wondering why it is taking _that_ long to create a local node. I'd love to have my own local node, but I wasn't expecting this long waiting time.

## CountCypher | 2022-06-16T14:45:20+00:00
After I had the PC running for days, the local node finally reached 100% sync. :smile: I only use the wallet once in a while, so every time I open it, it needs a _very_ long time for initial sync with the local node on my HDD. I'm afraid, my hardware specs are just not fit for the task. :wink: So I'll switch to a remote node for the time being, because this takes only seconds to sync. But still, I'm thinking about switching to running my own node on a VPS instead. 
Thanks a lot for your help earlier, I learned a lot. :smile: Closing this issue now.

## selsta | 2022-06-16T14:46:24+00:00
Sorry, forgot to reply. The issue is the HDD. Having an SSD significantly speeds up sync and tx generation.

# Action History
- Created by: CountCypher | 2022-06-07T15:31:04+00:00
- Closed at: 2022-06-16T14:45:20+00:00
