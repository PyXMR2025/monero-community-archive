---
title: Error while synchronizing stagenet
source_url: https://github.com/monero-project/monero/issues/9890
author: ruben2k1
assignees: []
labels: []
created_at: '2025-04-04T18:57:57+00:00'
updated_at: '2025-04-08T17:18:49+00:00'
type: issue
status: closed
closed_at: '2025-04-08T17:18:47+00:00'
---

# Original Description
I was downloading the stagenet blockchain when suddenly it stopped here and says 0% synchronized. I tried to sync it on the Raspberry but it didn't sync either

[https://i.gyazo.com/d23492ce63b453d67b2f61029d752789.png](https://github.com/monero-project/monero-gui/issues/url)

Also, it keeps coming up “Synchronization started” and that a new candidate block has been returned

[https://i.gyazo.com/563784d19db97baa0284232b4333fe94.png](https://github.com/monero-project/monero-gui/issues/url)

# Discussion History
## selsta | 2025-04-05T12:20:49+00:00
Which monero version are you using? Did both of these syncs happen of the Raspberry Pi? Which exact model and operating system are you using?

## ruben2k1 | 2025-04-05T13:32:28+00:00
I am using version 0.18.3.4-release (Fluorine Fermi) Linux ARM v8, both on the Raspberry and on my PC using the Windows 64 bits binaries

Yes, both on the Raspberry and on my Windows 10 PC this happens

I am using Raspberry Pi 5 8GB RAM with Raspberry Pi OS Lite 64 bits

## nahuhh | 2025-04-05T13:45:08+00:00
What command line flags are you using, if any

and the output of `sync_info`

## ruben2k1 | 2025-04-05T14:24:24+00:00
I'm using this command: monerod --stagenet --enable-dns-blocklist --data-dir D:\xmr\blockchain --add-priority-node=stagenet.xmr-tw.org:38081 --add-priority-node=stagenet.xmr.ditatompel.com:443 --add-priority-node=xmr-lux.boldsuck.org:38081 --add-priority-node=node.monerodevs.org:38089 --add-priority-node=node2.monerodevs.org:38089

Before I used to use only: monerod --stagenet --enable-dns-blocklist --data-dir D:\xmr\blockchain, but I noticed that with the other command I get less “Synchronization started” and “Sync data returned a new top block candidate” message over and over again

Output of sync_info here: [https://i.gyazo.com/cdcfa8212a797807e62612f2292b93c3.png](url)

## ruben2k1 | 2025-04-05T14:27:23+00:00
I don't know why it is getting slower and slower and increasing the days, at the beginning it is fast synchronizing but when it reaches over 7% the problems start

[https://i.gyazo.com/26a4af2d095bdd7f8526494f4504815e.png](url)

## ruben2k1 | 2025-04-05T14:32:01+00:00
I wanted to test with stagenet without spending money on real XMR and integrate XMR into applications

[https://i.gyazo.com/f5d3400acd6f3c8e8e2e488bb8b54f88.png](url)

## nahuhh | 2025-04-05T14:44:46+00:00
Sync_info looks fine.

its probably just slow (?)
are you using hdd or ssd?

## ruben2k1 | 2025-04-05T14:49:03+00:00
I'm using external SSD

## nahuhh | 2025-04-05T14:54:31+00:00
Has sync halted, or just slowed?


If slowed, probably normal. I'm not sure when thr last time stagenet has checkpoints updated (or if stagenet uses checkpoints).

1 block per second w/o checkpoints is "normal" range

## ruben2k1 | 2025-04-05T14:58:37+00:00
In the Raspberry monerod stopped when it had been open for a while, in Windows this does not happen to me

But both are equally slow

[https://i.gyazo.com/63e412fd29a2bfcaee0b525f6db84e96.png](url)

## ruben2k1 | 2025-04-05T15:02:45+00:00
The Raspberry also stopped the synchronization even though monerod did not close, since the night of the previous day it was going through the same block and the next day it had not advanced at all

I would also be grateful if you know how to download the raw blockchain for stagenet, like the mainnet one that is available for download on the Monero website



## nahuhh | 2025-04-05T15:06:44+00:00
> I would also be grateful if you know how to download the raw blockchain for stagenet, 

not available

> like the mainnet one that is available for download on the Monero website

this is being removed



## ruben2k1 | 2025-04-05T15:09:31+00:00
Why is being removed? 

## selsta | 2025-04-05T15:20:57+00:00
> Why is being removed?

It is not recommended, there is no speed benefit because the raw blockchain has to be verified during import anyway and it increases the chance for support requests if something goes wrong or the .raw file is outdated.

## selsta | 2025-04-05T15:22:33+00:00
Can you let the Windows version sync for 24h and report back and what height it is?

## plowsof | 2025-04-05T15:25:23+00:00
the testnet chain is smaller 

>--add-priority-node=stagenet.xmr-tw.org:38081 --add-priority-node=stagenet.xmr.ditatompel.com:443 --add-priority-node=xmr-lux.boldsuck.org:38081 --add-priority-node=node.monerodevs.org:38089 --add-priority-node=node2.monerodevs.org:38089

also i think your ports are wrong for `--add-priority-node`, these look like RPC nodes. you're using 38089 for monerodevs , should be using the p2p port @ 38080 right? 

## ruben2k1 | 2025-04-05T15:31:45+00:00
> Can you let the Windows version sync for 24h and report back and what height it is?

Yes of course

Currently going for height 587547

## ruben2k1 | 2025-04-05T15:34:18+00:00
> the testnet chain is smaller
> 
> > --add-priority-node=stagenet.xmr-tw.org:38081 --add-priority-node=stagenet.xmr.ditatompel.com:443 --add-priority-node=xmr-lux.boldsuck.org:38081 --add-priority-node=node.monerodevs.org:38089 --add-priority-node=node2.monerodevs.org:38089
> 
> also i think your ports are wrong for `--add-priority-node`, these look like RPC nodes. you're using 38089 for monerodevs , should be using the p2p port @ 38080 right?

It looks like it, I will stop the node to make the correction

## ruben2k1 | 2025-04-05T15:43:28+00:00
I see that the slowness is not a bug as such, I think I'll leave it at that

Still I think you should check the errors that occur in the Raspberry (monerod closes after a while, stops synchronizing and does not increase the height - was 10h without doing anything ...)

Thanks for the help

## nahuhh | 2025-04-05T15:50:10+00:00
For rasp pi, i'd also like to see the sync_info

## ruben2k1 | 2025-04-05T15:52:11+00:00
I don't have that anymore, the hard disk I was using in the Raspberry is now using it in Windows to synchronize stagenet (since the Raspberry was giving error and I had been trying for a week)

## ruben2k1 | 2025-04-06T20:18:58+00:00
> Can you let the Windows version sync for 24h and report back and what height it is?

[https://i.gyazo.com/5c47f8fa4b6a37fe9a1a74ec9b93e793.png](url)

## selsta | 2025-04-06T20:20:41+00:00
Yes, this appears way too slow for it to be working correctly.

## ruben2k1 | 2025-04-06T20:32:26+00:00
I don't know what it is due to

## nahuhh | 2025-04-07T00:58:14+00:00
offtopic

moving fwd, can you
A) upload the image directly to github (using the toolbar above/below the comment box) like: ![5c47f8fa4b6a37fe9a1a74ec9b93e793.png](https://github.com/user-attachments/assets/52f9ec5d-e214-40ef-aec8-7f68a0adc7d9)
Or
B) just paste the link w/o the brackets like: https://i.gyazo.com/5c47f8fa4b6a37fe9a1a74ec9b93e793.png

your image links arent clickable as-is. I have to keep copy/pasting them

thx

## nahuhh | 2025-04-07T00:59:35+00:00
> I don't know what it is due to

Are you sure this is syncing to an ssd?

edit:
Also can try
1. Running the v0.18.3.4 binary for 10min, then
2. Run the v0.18.4.0 binary for 10min

any notable difference?

this seems like an issue with
A) really old pc
B) hdd
C) ghosts /s

I'll try sync stagenet for myself

## ruben2k1 | 2025-04-07T01:00:13+00:00
Oh thanks, I didn't know it

## ruben2k1 | 2025-04-07T01:36:59+00:00
Yes, I am using a 2TB external SSD

I have seen today that Monero has been updated and I have changed the binaries to the latest version, but it is still as slow

My PC has i5 4690K 3.5Ghz, NVIDIA GTX 960 and 8GB of RAM

It may seem old and it is, but I use it every day and it runs fast, especially since 2 years ago I changed the HDD hard drive for SSD. I even play video games with it still

## nahuhh | 2025-04-07T03:07:03+00:00
> > Can you let the Windows version sync for 24h and report back and what height it is?
> 
> https://i.gyazo.com/5c47f8fa4b6a37fe9a1a74ec9b93e793.png

@selsta stagenet is being spammed at these blocks (1111273 etc)
https://stagenet.xmrchain.net/page/65720

Taking 5min to sync 7mb (335kb * 20 block sync size) sounds like a problem, but it's about 15 seconds for a block. Maybe normal if assuming an (older) external ssd connected via usb 2.0?

i'm only at block ~145k. Probably 10+hrs away from block 1111NNN. Will know what it looks like when i get there


## ruben2k1 | 2025-04-07T11:46:31+00:00
I'm stuck here

I've left it all night and if you look at the timestamp, no progress has been made

![](https://i.gyazo.com/f161203c01dc02214f89cbcc23fa973a.png)


## nahuhh | 2025-04-07T12:10:50+00:00
sync_info

i passed 1111273 and it took about 30secs to sync 20 blocks

## ruben2k1 | 2025-04-07T12:57:30+00:00
![](https://i.gyazo.com/899822ad247e764b62de2ee4bf69db40.png)


## nahuhh | 2025-04-07T17:23:11+00:00
looks like youre just really struggling to verify larger batches. Youre about 8000 blocks ahead of your prior screenshot.

for the 11hrs downtime in your prior screenshot, did your computer go to sleep?

## selsta | 2025-04-07T17:24:57+00:00
The `sync_info` output also shows it's not a network issue, the blocks are loaded but somehow verify way too slowly. Could you try syncing to an internal SSD for testing purposes?

## ruben2k1 | 2025-04-07T17:26:38+00:00
No, I have deactivated the sleep mode

This is the current status of the process

![](https://i.gyazo.com/2e5b2c81de25d4f6ea62b3d01091cad1.png)


## ruben2k1 | 2025-04-07T17:32:10+00:00
Anyway I am using a remote node with monero-wallet-rpc on stagenet in the meantime, as it takes too long

## ruben2k1 | 2025-04-07T17:40:47+00:00
Here you have it synchronized with my internal SSD

![](https://i.postimg.cc/jdjVXNs4/image.png)


## selsta | 2025-04-07T18:08:01+00:00
Also please update to v0.18.4.0 – it does not necessarily contain fixes for the issue you are experiencing but it can't hurt.

## ruben2k1 | 2025-04-07T18:10:38+00:00
> Also please update to v0.18.4.0 – it does not necessarily contain fixes for the issue you are experiencing but it can't hurt.

I'm already in that version, see in the image above where I run sync_info

## ruben2k1 | 2025-04-08T13:37:31+00:00
Stuck here

![](https://i.gyazo.com/1f1d178afe3e0d9a39b4b83f334584b2.png)

## nahuhh | 2025-04-08T13:57:04+00:00
install and run htop:
```
sudo apt install htop
htop
```

Then
1. Filter htop by pressing `F4`
2. Type `monerod` then enter
3. Take screenshot
i'd like to see 
  - The `S` (status) column
  - The overall cpu and ram usage
4. If there are 2 tabs `Main` and `I/O`, press `tab` and take another screenshot.
  - looking to see if there is any io activity



## ruben2k1 | 2025-04-08T13:58:41+00:00
> install and run htop:
> 
> ```
> sudo apt install htop
> htop
> ```
> 
> Then
> 
> 1. Filter htop by pressing `F4`
> 2. Type `monerod` then enter
> 3. Take screenshot
> 
> i'd like to see the `S` column

I'm on Windows. Htop for Windows?

## nahuhh | 2025-04-08T14:41:58+00:00
> I'm on Windows. Htop for Windows?

Whoops. Forgot. Idk how to check on windows.

Is it still stuck? try to get a `sync_info` from it.

## ruben2k1 | 2025-04-08T14:50:09+00:00
Yes, it is still stuck

I had to run the command twice because it gave an error

![](https://i.gyazo.com/6501f47d0e00593337491fc89339108f.png)

## nahuhh | 2025-04-08T14:57:42+00:00
Its not stuck, just taking 15-25mins to sync 20 blocks. 

each block in those ranges are about 450kb (and grow to about 1.5mb). I think this is just your pc, ssd, or usb connection being slow. 

Copy the bitmonero folder to your internal ssd and try sync it there 

## ruben2k1 | 2025-04-08T17:18:47+00:00
May be due to USB connection

# Action History
- Created by: ruben2k1 | 2025-04-04T18:57:57+00:00
- Closed at: 2025-04-08T17:18:47+00:00
