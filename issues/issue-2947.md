---
title: Can i increase my Hashrate?
source_url: https://github.com/xmrig/xmrig/issues/2947
author: Noeleth
assignees: []
labels: []
created_at: '2022-02-28T05:56:39+00:00'
updated_at: '2022-04-04T05:35:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

Hello good day. I am new to mining, and I wanted to know if it is possible to increase my hasrate. I currently have a lenovo ideapad laptop with intel i7 6700HQ 2.6 ghz. windows 10. As you can see in the images, I work with the unmineable console, which in turn works with xmrig. I am mining with cpu as you can see, in the image I put my work with unmineable 1673h. but I have had peaks of 3000, 4000 or 5000 for a few minutes, if you see my cpu is at 50%, I have also worked with the xmrig program separately and it also gives me around 1700hs. I have tried the windows setup guide for xmrig. I also attach photos of my json file, if someone can help me increase my hashrate to at least 3500 4000, I would appreciate it, I know that my cpu can work a little more than 50% even reach 70 or 80%... . thank you very much to all.
![B2FC0943-84C3-4C7D-83A5-74986D0EB14B](https://user-images.githubusercontent.com/100553798/155931557-0322ed70-f7aa-443d-87e3-66d730ba3173.jpeg)
![14B9E2B6-DD97-450B-A891-D80F949787CE](https://user-images.githubusercontent.com/100553798/155931573-00def04f-76b2-4076-8653-32891bedf67c.jpeg)
![71923AD0-96AB-4F21-BA7A-827DD960E27B](https://user-images.githubusercontent.com/100553798/155931587-42c48a44-e3b7-4743-81da-a1b57c6cb3aa.jpeg)
![EA06B785-D2AE-4400-A7C6-D68A867F6C34](https://user-images.githubusercontent.com/100553798/155931596-ebc48922-286f-4ba8-bd8d-12e646d38f4f.jpeg)
![1D2726CB-42C9-48D5-8AE6-2FADBC7C045B](https://user-images.githubusercontent.com/100553798/155931608-f2070a9a-e8ff-4e3f-845c-5a23a27e64c9.jpeg)
![AB225EF2-3183-4064-BBF3-96582E703056](https://user-images.githubusercontent.com/100553798/155931618-4be3caa3-201b-4189-bbf5-d48cf3d6221c.jpeg)
![3DCDBCEB-0873-4D89-A13E-80B1FFAA902C](https://user-images.githubusercontent.com/100553798/155931624-6b61eec7-16b8-4ffd-abf1-01837bf97752.jpeg)

![FA49A717-D47E-457D-920D-CCBD10B7434D](https://user-images.githubusercontent.com/100553798/155952795-b993f94b-5564-4063-8e85-f70f75b439f6.png)



# Discussion History
## Spudz76 | 2022-02-28T12:29:29+00:00
Your peaks are luck, if you let xmrig run a while the graph should look the same.

Your CPU has 6MB of L3 which means 6/2=3 threads regardless if there are four cores.  HyperThreads on Intel are useless in RandomX because the secondary thread is not wired separately to cache and memory so it just slows the real-core, so 50% is maximum anyway even if you had 16MB of cache it would only run the four real cores.

You would make more XMR using MoneroOcean and some other algorithms that don't need what RandomX needs.  Most of my Intels run astrobwt and earn much more than they would with rx/0.  And you can run GPUs then into the same XMR payout buffer.

## Spudz76 | 2022-02-28T12:33:25+00:00
Oh also with their fixed job difficulty of 100001 you will have terrible luck variance because 100001/30=3333H/s while you only have enough hashrate for 1780*30=53400 difficulty.  So some rounds can miss work.

Either set custom diff if possible (I don't know if Unmineable supports that) or ideally switch to a pool with autodiff.

## Noeleth | 2022-02-28T12:50:34+00:00
I dont know pools with autodiff, im going to investigate if unmineable support custom dif. 

## Spudz76 | 2022-02-28T13:35:59+00:00
Looks like you can put `+53400` on the end of your wallet string, if it will allow diff that low (might ignore it).

## BobbieX | 2022-04-03T23:19:29+00:00
I use an AMD 5800H CPU for mining but only get about 2200h. Seems only 3 of 16 threads are working by default Xmrig setting. How can I improve it?
![image](https://user-images.githubusercontent.com/101654375/161453151-fbc3c166-fbcb-4d49-a750-5ac0b53ec3a5.png)
![image](https://user-images.githubusercontent.com/101654375/161453186-e71a4ebc-538f-49ad-9b72-78ca1cc92c76.png)


## SChernykh | 2022-04-04T05:35:56+00:00
It should be 8 threads for Ryzen 5800H. Edit config.json and remove the `cpu` section there. If you use the command line, remove `-t 3` or `--threads 3` from it.

# Action History
- Created by: Noeleth | 2022-02-28T05:56:39+00:00
