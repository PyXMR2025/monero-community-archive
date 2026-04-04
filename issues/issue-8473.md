---
title: RockPro64 sync struggles
source_url: https://github.com/monero-project/monero/issues/8473
author: dawiepoolman
assignees: []
labels: []
created_at: '2022-07-29T08:13:37+00:00'
updated_at: '2022-08-23T16:44:00+00:00'
type: issue
status: closed
closed_at: '2022-08-23T16:44:00+00:00'
---

# Original Description
Hi guys

I have a brand new RockPro64 running Arbian on eMMC and writing the data do an NVMe.
I must have tried 10 times already with different degrees of progress (between about 10%-47%) before failure with different errors.

The latest log:

![image](https://user-images.githubusercontent.com/2351212/181713921-16d1b676-2ab6-4be9-977b-3449777cf8f6.png)


popping blocks from the stack does not work:

![image](https://user-images.githubusercontent.com/2351212/181714229-a2378b11-4975-4a1d-a220-3b79d8388936.png)


my drive is not full yet:
![image](https://user-images.githubusercontent.com/2351212/181714383-e8b546fb-ee8d-4d55-8ac6-d1a4b655338f.png)


my monerod.conf file has reasonably settings afaik:
![image](https://user-images.githubusercontent.com/2351212/181714986-821be6de-d1ad-43b9-bc32-5f34e2f9e4b9.png)

Please tell me it cant be hardware related?  It is brand new?
Is there a way to test?



# Discussion History
## dawiepoolman | 2022-07-29T08:19:01+00:00
--db-salvage also fails with same error " Attempt to get block from height 1250892 failed -- block not in db"

![image](https://user-images.githubusercontent.com/2351212/181716142-4dc45545-16f1-4805-9a66-cb35931e1cb6.png)


## dawiepoolman | 2022-07-29T08:26:38+00:00
scan disk shows ok?:
![image](https://user-images.githubusercontent.com/2351212/181717835-4937db30-04dc-476c-879b-e847dedad7f6.png)


## dawiepoolman | 2022-07-29T08:33:12+00:00
restarting sync from scratch again fwiw..

## dawiepoolman | 2022-07-29T08:37:45+00:00
htop during sync:

![image](https://user-images.githubusercontent.com/2351212/181719647-96f47812-840b-448a-8d63-fc3510bb3749.png)


## Gingeropolous | 2022-07-29T12:20:42+00:00
is the nvme brand new? is it USB attached? i don't know what rockpro64 boards look like these days

## selsta | 2022-07-29T12:31:05+00:00
How did you format your SSD? `exfat`, `ext4`, ... ?

Also your regarding your config, 64 out peers and 1024 in peers seems way too much for your system. I would recommend to keep out_peers at the default value.

## dawiepoolman | 2022-07-29T14:07:24+00:00
PCIe card attached
ext4
Brand: crucial
current synch at 27%..

## dawiepoolman | 2022-07-29T14:08:14+00:00
![20220729_160705](https://user-images.githubusercontent.com/2351212/181777954-238d0635-c242-46f2-b662-669793ed32f5.jpg)


## dawiepoolman | 2022-07-29T14:14:59+00:00
ok, I have set the in and out peers to default just in case and restarted the monerod service.

I did notice errors in the log but it seems like it resumed successfully.
![image](https://user-images.githubusercontent.com/2351212/181779178-c30f7498-1cae-4ed8-9596-e604fcaa6d14.png)



## dawiepoolman | 2022-07-29T14:16:43+00:00
running fine so far..:
![image](https://user-images.githubusercontent.com/2351212/181779510-bef230a9-e34b-4959-a14b-952ecb32a8eb.png)


## selsta | 2022-07-29T14:20:17+00:00
From what I know the Rock64 has some stability issues with default memory clock: https://forum.pine64.org/showthread.php?tid=11209&pid=76615#pid76615

I don't know if this also applies to the Pro but it would explain the weird errors you are getting.

## dawiepoolman | 2022-07-29T19:40:51+00:00
different error again:
![image](https://user-images.githubusercontent.com/2351212/181832335-40490fec-ace9-42c1-85d1-30b949752789.png)


## dawiepoolman | 2022-07-29T19:52:56+00:00
pop blocks:
![image](https://user-images.githubusercontent.com/2351212/181833488-74641efd-ca88-4bed-83c9-7ff8056f67cc.png)


after restarting monerod I get the same errors.
Let me restart  the sync from scratch one more time.  Not sure whether is is a NVMe issue or clock issue of RockPro64 as @selsta suggested.  

## dawiepoolman | 2022-07-29T20:01:58+00:00
I have restarted with a new db and new logs but on starting monerod fresh I get very suspicions log entries from the get-go:

![image](https://user-images.githubusercontent.com/2351212/181834891-3a273044-b927-48cc-8792-171ea2ee4477.png)


## selsta | 2022-07-29T20:04:16+00:00
What do you find suspicious?

## hyc | 2022-07-29T20:29:51+00:00
A lot of these single board computers have issues with weak power supplies. I'd look into that first of all.

## dawiepoolman | 2022-07-29T21:27:05+00:00
what I mean by suspicious is the phrases with 'Warning' or 'Error' in the log file in the beginning:  
![image](https://user-images.githubusercontent.com/2351212/181844568-ed2aa458-ad23-426d-b855-403e77230eff.png)

hopefully that is benign or does not apply/mean much in this context.

The power supply looks decent in my opinion.  It has output of 12V and 5Amps and is quite a bulky power supply compared to those of my Raspberry Pis

The re-sync is progressing well so far:
![image](https://user-images.githubusercontent.com/2351212/181845243-2609c5b0-8471-433a-9d08-c8e0b95f9905.png)



## selsta | 2022-07-29T21:28:18+00:00
These are just log categories.

## dawiepoolman | 2022-07-29T21:29:06+00:00
Ok awesome.

This is the power supply..




## dawiepoolman | 2022-07-29T21:32:46+00:00
![Screenshot_20220729-233110_Gallery](https://user-images.githubusercontent.com/2351212/181845837-ddbe6926-9600-497b-99c1-05c98843e638.jpg)


## dawiepoolman | 2022-07-29T21:34:03+00:00
sorry for the massive photo rendering.  I am not shouting  :P

## dawiepoolman | 2022-07-29T21:37:03+00:00
looking stable..
![image](https://user-images.githubusercontent.com/2351212/181846160-13606e5f-19c3-444c-8531-a0c59c4f5d7f.png)

running nice and cool:
![image](https://user-images.githubusercontent.com/2351212/181846300-246ac2d9-e4b4-4e1e-af23-d5b45e00fcef.png)


## dawiepoolman | 2022-07-29T21:40:41+00:00
blockchain growing nicely on NVMe..
![image](https://user-images.githubusercontent.com/2351212/181846687-135c13eb-fd76-4563-8615-8ae67704e6c4.png)


## dawiepoolman | 2022-07-30T05:21:12+00:00
getting there..
![image](https://user-images.githubusercontent.com/2351212/181875972-803f5802-8f35-4e11-96bb-95e473ed77eb.png)


## dawiepoolman | 2022-07-30T05:27:46+00:00
wait.. it seems to be stuck at that last block..

htop shows one processor 100% and stays there:
![image](https://user-images.githubusercontent.com/2351212/181876113-86a006de-38be-4f94-b4ba-4c2d4198c846.png)


df -h
![image](https://user-images.githubusercontent.com/2351212/181876149-a80026d8-6a7d-41ec-8ab5-e76751308d80.png)


log still at block 1089949/2678317
![image](https://user-images.githubusercontent.com/2351212/181876180-7b47ac73-2f9d-4875-be3c-617cdc017bc2.png)



## dawiepoolman | 2022-07-30T05:45:07+00:00
still stuck..
monerod service wont stop graciously.  seems stuck on stop left cmd screen with processor no 6 on 100%:

![image](https://user-images.githubusercontent.com/2351212/181876593-7a0e9214-66f0-4416-aa99-18ed31cb4886.png)


## selsta | 2022-07-30T10:05:59+00:00
The fact that you constantly get a different issue hints at some system instability to me :/ I would try reducing the memory clock as a first step.

## dawiepoolman | 2022-07-30T10:59:07+00:00
I have rebooted and it resumed fine.
I will keep an eye and if it fails again I will try slow the clock speed (seems super technical tbh)
Hopefully it is just the initial sync workload that causes the instability. 
If is indeed the clock speed I would have preferred to rather exchange the unit for another one but logistically from South Africa it is such a shlep.


## dawiepoolman | 2022-07-31T06:34:41+00:00
Ok, it failed another 2 times, the last sync only at 17%

I am afraid @selsta is correct, i.e. the ddr memory clock speed is causing the instability.

From the pine64 forum threads I gather that this file could likekely be the latest custom version to try: rk3328_ddr_400MHz_v1.17.bin

From thread here:
https://forum.pine64.org/showthread.php?tid=11209&page=2

And download git repo here:
https://github.com/rockchip-linux/rkbin/tree/master/bin/rk33

The instructions that I could find here by Johannes:
https://forum.pine64.org/showthread.php?tid=7387&page=2

Question; is it possible to change this file on the eMMC chip that I am booting Arbian from? 
The instructions looks like it will create a brand new boot image that I first might have to flush to a micro SD card (like I did when I first setup the system), boot from the SD and only then write it to the eMMC?

Sounds like a risky process to a not super technical person like myself.

## dawiepoolman | 2022-07-31T06:45:37+00:00
btw, I think this build memory issue I had was related without us  realizing it at the time:
https://github.com/monero-project/monero/issues/8468

## dawiepoolman | 2022-07-31T07:24:08+00:00
That file I mentioned wont work, I see the RockPro uses a Rockchip RK3399 chip, hence the more likely file to use would be 
rk3399_ddr_933MHz_v1.25.bin (or to be very conservative the rk3399_ddr_666MHz_v1.25.bin)

I will make a post on the pine64 forum to confirm as well

## dawiepoolman | 2022-08-02T22:09:20+00:00
I have tried the steps in this thread: https://forum.pine64.org/showthread.php?tid=7387&page=2
i.e. I have taken the files:
https://github.com/rockchip-linux/rkbin/blob/master/bin/rk33/rk3399_ddr_666MHz_v1.25.bin
https://github.com/rockchip-linux/rkbin/blob/master/bin/rk33/rk3399_miniloader_v1.26.bin

maybe I should have taken the  rk3399pro* files?

and I have replaced (or at least I think I did) the files in the latest .iso from Armbian 22.05 Jammy  listed for download on the home page here:
https://www.armbian.com/rockpro64/

I cant seem to find a command to confirm the effective ddr clock speed though:
![image](https://user-images.githubusercontent.com/2351212/182481383-2f1a1abf-a5ef-48e3-97dc-41121ba93917.png)

![image](https://user-images.githubusercontent.com/2351212/182481753-7c80141f-aa8a-4739-bcf0-fbcf3081983a.png)


any other tips would be very much appreciated


## dawiepoolman | 2022-08-02T22:14:26+00:00
![image](https://user-images.githubusercontent.com/2351212/182482474-744cc9cd-885a-4131-808b-0614ff0d645a.png)


monero compiled fine from source but is giving these sync errors again

## selsta | 2022-08-05T21:52:48+00:00
Were you able to confirm the memory clock?

## dawiepoolman | 2022-08-06T17:37:43+00:00
Hi @selsta
I honestly have no idea how to proceed technically. I tried the instructions but it I cant conclude that it did not work because I did not do it right. 
I am at the end of my knowledge when it gets to the re-compilation of an .iso with different .bin files.


## selsta | 2022-08-06T17:40:07+00:00
The pine64 forum will likely be your best resource.

## dawiepoolman | 2022-08-12T15:16:28+00:00
I have asked for a board replacement since the pine64 forum post goes unanswered.  I will keep you guys posted.

## selsta | 2022-08-13T18:43:26+00:00
```
19:59 <garth> Hyc was right about the propensity for these problems via weak power supplies. The time this happened to me was a bad board component, probably memory.
19:59 <garth> Both of these suggestions have been mentioned alreadt
19:59 <garth> Already
```

This user also has a RockPro64.

## dawiepoolman | 2022-08-13T18:50:08+00:00
Thx selsta. The pine64 sales guys suggested I log a ticket with their tech support. I will referece this issue thread to them as well for futher comment.

## dawiepoolman | 2022-08-13T20:42:38+00:00
Whilst I wait on the support ticket feedback, I feel inclined to try and replace the power supply with a better quality just in case.

Would something like this suffice?:

Check this out on takealot: Mean Well GST60A12-P1J AC/DC Power Supply, ITE, 1 Output, 60 W, 12 V, 5 A
https://www.takealot.com/mean-well-gst60a12-p1j-ac-dc-power-supply-ite-1-output-60-w-12-v/PLID71116310

It is more expensive than the SBC though.

## hyc | 2022-08-14T01:56:11+00:00
Is your current power supply one that was originally bundled with the rockpro64? At 60W it should be fine already; you shouldn't need anywhere near 60W unless you've got a couple HDDs plugged in. Could try cleaning the connectors tho, just in case. Also if you have a voltmeter, could check to see if the 12V bus is actually at 12V, or if it's sagging lower. If it's reading less than 12V then yeah, definitely the power supply is inadequate.

## dawiepoolman | 2022-08-14T20:16:37+00:00
This is the multimeter result on the official rockpro64 power supply:

![20220814_201349](https://user-images.githubusercontent.com/2351212/184553273-628098b3-89a7-486f-8b80-a43ca37773c4.jpg)

It looks powerful enough to me i.e.  stable above 12V

The pine64 support guys suggested I ask in the online channels so I asked on their Telegram chat and the admin suggested I rather try the official Debian image for the RockPro64 rather than the Armbian. Apparantly the armbian devs are known for overclocking the system and the pine64 clan is not surprised.

So, I have started the test with debian. I will keep you posted.


## hyc | 2022-08-14T20:36:11+00:00
I actually meant checking the power rails on the RockPro64 while the power supply is plugged in and the rockpro is powered up and running. You should be able to get to it from the expansion connector.

But anyway, testing with the official Debian image sounds like a good idea.

## dawiepoolman | 2022-08-15T06:15:36+00:00
cool stuff.
running stable so far after 6 hours on Debian. sync at 29%:

![image](https://user-images.githubusercontent.com/2351212/184585524-7fc6e0a1-19c2-4a28-843c-ecc18c3fd204.png)


## dawiepoolman | 2022-08-15T10:33:04+00:00
it failed again :-(

![image](https://user-images.githubusercontent.com/2351212/184620401-e91d2298-9f08-4098-ba69-7b686f8922a1.png)

it got to 43% in about 8 hours


## dawiepoolman | 2022-08-15T12:53:21+00:00
The recommendations of the pine64 support are beyond the typical technical user capabilities:

![image](https://user-images.githubusercontent.com/2351212/184637421-4fd2adb8-6751-48f3-b5f9-ec64b235e488.png)

Can someone summarize the steps or point to an example pls?

Has no one in the monero community had to build a custom image before?  Sounds to me like a board issue tbh.

## dawiepoolman | 2022-08-15T15:30:31+00:00
checked for disk errors  on the nvme just in case and it is clean:

![image](https://user-images.githubusercontent.com/2351212/184665691-11a0e818-6b99-43e6-b868-0c5806cf39cc.png)


## dawiepoolman | 2022-08-15T16:31:35+00:00
I retried again with more aggressive config settings and it failed at 5%.

config:

data-dir=/home/cypher/.bitmonero
log-file=/home/cypher/.bitmonero/monero.log
log-level=0
block-sync-size=50
db-sync-mode=safe
enable-dns-blocklist=1
enforce-dns-checkpointing=1
max-concurrency=6
limit-rate-up=1048576
limit-rate-down=1048576
max-log-files=1



2022-08-15 15:47:12.952 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1678    Synced 148494/2690190 (5%, 2541696 left)
cypher@rockpro64:~$ tail -n 100 .bitmonero/monero.log
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /home/cypher/monero/build/monerod(+0x4f976c) [0xaaaaca58976c]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /home/cypher/monero/build/monerod(+0x52660c) [0xaaaaca5b660c]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /home/cypher/monero/build/monerod(+0x3cc18c) [0xaaaaca45c18c]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /home/cypher/monero/build/monerod(+0x3d462c) [0xaaaaca46462c]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /home/cypher/monero/build/monerod(+0x3efd14) [0xaaaaca47fd14]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /home/cypher/monero/build/monerod(+0x38e540) [0xaaaaca41e540]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /home/cypher/monero/build/monerod(+0x391b4c) [0xaaaaca421b4c]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /home/cypher/monero/build/monerod(+0xf1efc) [0xaaaaca181efc]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /home/cypher/monero/build/monerod(+0x3615f8) [0xaaaaca3f15f8]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /home/cypher/monero/build/monerod(+0x3629dc) [0xaaaaca3f29dc]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /home/cypher/monero/build/monerod(+0x1d9094) [0xaaaaca269094]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [16] /home/cypher/monero/build/monerod(+0xc1c7c) [0xaaaaca151c7c]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [17] /home/cypher/monero/build/monerod(+0x2f540c) [0xaaaaca38540c]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [18] /home/cypher/monero/build/monerod(+0x3291a8) [0xaaaaca3b91a8]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [19]  0xb028) [0xffff83c6b028]:_thread.so.1.74.0(+0xb028) [0xffff83c6b028]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [20] /lib/aarch64-linux-gnu/libpthread.so.0(+0x8628) [0xffff8393b628]
2022-08-15 16:04:10.572 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [21] /lib/aarch64-linux-gnu/libc.so.6(+0xd601c) [0xffff8389101c]
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172
2022-08-15 16:04:10.573 [P2P8]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:4502 Error adding block with hash: <d8cd2c3f83b73039e3c607b01d8fd26b20ac4dfdb11a794b6388413148cdec0f> to blockchain, what = Failed to get output amount in db transaction: MDB_CORRUPTED: Located page was wrong type
2022-08-15 16:04:10.573 [P2P8]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: cryptonote::DB_ERROR
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x134) [0xaaaaca100e18]:__cxa_throw+0x134) [0xaaaaca100e18]
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /home/cypher/monero/build/monerod(+0x4fef00) [0xaaaaca58ef00]
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /home/cypher/monero/build/monerod(+0x50bcb0) [0xaaaaca59bcb0]
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /home/cypher/monero/build/monerod(+0x3d6fa8) [0xaaaaca466fa8]
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /home/cypher/monero/build/monerod(+0x406f28) [0xaaaaca496f28]
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /home/cypher/monero/build/monerod(+0x3a67ec) [0xaaaaca4367ec]
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /home/cypher/monero/build/monerod(+0x3cd6c0) [0xaaaaca45d6c0]
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /home/cypher/monero/build/monerod(+0x3d462c) [0xaaaaca46462c]
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /home/cypher/monero/build/monerod(+0x3efd14) [0xaaaaca47fd14]
2022-08-15 16:04:10.573 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /home/cypher/monero/build/monerod(+0x38e540) [0xaaaaca41e540]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /home/cypher/monero/build/monerod(+0x391b4c) [0xaaaaca421b4c]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /home/cypher/monero/build/monerod(+0xf1efc) [0xaaaaca181efc]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /home/cypher/monero/build/monerod(+0x3615f8) [0xaaaaca3f15f8]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /home/cypher/monero/build/monerod(+0x3629dc) [0xaaaaca3f29dc]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /home/cypher/monero/build/monerod(+0x1d9094) [0xaaaaca269094]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [16] /home/cypher/monero/build/monerod(+0xc1c7c) [0xaaaaca151c7c]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [17] /home/cypher/monero/build/monerod(+0x2f540c) [0xaaaaca38540c]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [18] /home/cypher/monero/build/monerod(+0x3291a8) [0xaaaaca3b91a8]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [19]  0xb028) [0xffff83c6b028]:_thread.so.1.74.0(+0xb028) [0xffff83c6b028]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [20] /lib/aarch64-linux-gnu/libpthread.so.0(+0x8628) [0xffff8393b628]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [21] /lib/aarch64-linux-gnu/libc.so.6(+0xd601c) [0xffff8389101c]
2022-08-15 16:04:10.574 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172
2022-08-15 16:04:10.574 [P2P8]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:4748 Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2022-08-15 16:04:12.286 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     [47.55.110.17:18080 OUT] Sync data returned a new top block candidate: 208666 -> 2690204 [Your node is 2481538 blocks (7.9 years) behind]
2022-08-15 16:04:12.286 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     SYNCHRONIZATION started
2022-08-15 16:04:14.167 [P2P5]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   Failed to get output amount in db transaction: MDB_CORRUPTED: Located page was wrong type
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: cryptonote::DB_ERROR
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x134) [0xaaaaca100e18]:__cxa_throw+0x134) [0xaaaaca100e18]
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /home/cypher/monero/build/monerod(+0x4fef00) [0xaaaaca58ef00]
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /home/cypher/monero/build/monerod(+0x50c778) [0xaaaaca59c778]
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /home/cypher/monero/build/monerod(+0x4f90a8) [0xaaaaca5890a8]
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /home/cypher/monero/build/monerod(+0x4f976c) [0xaaaaca58976c]
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /home/cypher/monero/build/monerod(+0x52660c) [0xaaaaca5b660c]
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /home/cypher/monero/build/monerod(+0x3cc18c) [0xaaaaca45c18c]
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /home/cypher/monero/build/monerod(+0x3d462c) [0xaaaaca46462c]
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /home/cypher/monero/build/monerod(+0x3efd14) [0xaaaaca47fd14]
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /home/cypher/monero/build/monerod(+0x38e540) [0xaaaaca41e540]
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /home/cypher/monero/build/monerod(+0x391b4c) [0xaaaaca421b4c]
2022-08-15 16:04:14.167 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /home/cypher/monero/build/monerod(+0xf1efc) [0xaaaaca181efc]
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /home/cypher/monero/build/monerod(+0x3615f8) [0xaaaaca3f15f8]
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /home/cypher/monero/build/monerod(+0x3629dc) [0xaaaaca3f29dc]
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /home/cypher/monero/build/monerod(+0x1d9094) [0xaaaaca269094]
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [16] /home/cypher/monero/build/monerod(+0xc1c7c) [0xaaaaca151c7c]
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [17] /home/cypher/monero/build/monerod(+0x2f540c) [0xaaaaca38540c]
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [18] /home/cypher/monero/build/monerod(+0x3291a8) [0xaaaaca3b91a8]
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [19]  0xb028) [0xffff83c6b028]:_thread.so.1.74.0(+0xb028) [0xffff83c6b028]
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [20] /lib/aarch64-linux-gnu/libpthread.so.0(+0x8628) [0xffff8393b628]
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [21] /lib/aarch64-linux-gnu/libc.so.6(+0xd601c) [0xffff8389101c]
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172
2022-08-15 16:04:14.168 [P2P5]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:4502 Error adding block with hash: <d8cd2c3f83b73039e3c607b01d8fd26b20ac4dfdb11a794b6388413148cdec0f> to blockchain, what = Failed to get output amount in db transaction: MDB_CORRUPTED: Located page was wrong type
2022-08-15 16:04:14.168 [P2P5]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: cryptonote::DB_ERROR
2022-08-15 16:04:14.168 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x134) [0xaaaaca100e18]:__cxa_throw+0x134) [0xaaaaca100e18]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /home/cypher/monero/build/monerod(+0x4fef00) [0xaaaaca58ef00]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /home/cypher/monero/build/monerod(+0x50bcb0) [0xaaaaca59bcb0]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /home/cypher/monero/build/monerod(+0x3d6fa8) [0xaaaaca466fa8]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /home/cypher/monero/build/monerod(+0x406f28) [0xaaaaca496f28]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /home/cypher/monero/build/monerod(+0x3a67ec) [0xaaaaca4367ec]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /home/cypher/monero/build/monerod(+0x3cd6c0) [0xaaaaca45d6c0]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /home/cypher/monero/build/monerod(+0x3d462c) [0xaaaaca46462c]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /home/cypher/monero/build/monerod(+0x3efd14) [0xaaaaca47fd14]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /home/cypher/monero/build/monerod(+0x38e540) [0xaaaaca41e540]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /home/cypher/monero/build/monerod(+0x391b4c) [0xaaaaca421b4c]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /home/cypher/monero/build/monerod(+0xf1efc) [0xaaaaca181efc]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /home/cypher/monero/build/monerod(+0x3615f8) [0xaaaaca3f15f8]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /home/cypher/monero/build/monerod(+0x3629dc) [0xaaaaca3f29dc]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /home/cypher/monero/build/monerod(+0x1d9094) [0xaaaaca269094]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [16] /home/cypher/monero/build/monerod(+0xc1c7c) [0xaaaaca151c7c]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [17] /home/cypher/monero/build/monerod(+0x2f540c) [0xaaaaca38540c]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [18] /home/cypher/monero/build/monerod(+0x3291a8) [0xaaaaca3b91a8]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [19]  0xb028) [0xffff83c6b028]:_thread.so.1.74.0(+0xb028) [0xffff83c6b028]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [20] /lib/aarch64-linux-gnu/libpthread.so.0(+0x8628) [0xffff8393b628]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172      [21] /lib/aarch64-linux-gnu/libc.so.6(+0xd601c) [0xffff8389101c]
2022-08-15 16:04:14.169 [P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:172
2022-08-15 16:04:14.169 [P2P5]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:4748 Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2022-08-15 16:04:14.170 [P2P5]  INFO    global  src/p2p/net_node.inl:291        Host 47.55.110.17 blocked.


## selsta | 2022-08-15T18:06:13+00:00
I would try to get the hardware replaced.

## dawiepoolman | 2022-08-15T18:12:12+00:00
Indeed. I have asked pine64 support for a replacement. The system is unusable. I will let you know their answer since these boards will likely become very popular in the monero community IF proven stable.

## hyc | 2022-08-16T03:09:22+00:00
I've had zero problems with my rockpro64. Had no idea any memory instabilities were a common thing for them.

## dawiepoolman | 2022-08-16T07:06:07+00:00
Ok, while I wait on a reply for a replacement request, I will try and cool the cpu way down:

![20220816_080757](https://user-images.githubusercontent.com/2351212/184813703-626b2942-fee9-4f0a-817d-589d275d57d4.jpg)

It is running at a nice and cool 21 - 22 degrees celsius (previously 55 average)

I have set the config parameters to:

log-level=0
block-sync-size=1
db-sync-mode=safe
enable-dns-blocklist=1
enforce-dns-checkpointing=1
max-concurrency=1
limit-rate-up=1048576
limit-rate-down=1048576
max-log-files=1

Lets see if this would help, at least for the initial sync..

## dawiepoolman | 2022-08-16T09:31:14+00:00
Still running.  Currently at 14% synced at 23 degrees Celsius..

## dawiepoolman | 2022-08-16T20:38:06+00:00
48%...

## selsta | 2022-08-16T20:49:34+00:00
Is this the highest you have reached?

## dawiepoolman | 2022-08-16T21:06:55+00:00
Yes, looking good so far. I have read on some forum that the heat of the cpu and ram chips might affect each other on the rockpro64 so I thought what the hell, lets cool it down as far as possible to see if it makes a difference.
 

## dawiepoolman | 2022-08-17T05:49:03+00:00
alas, it failed at 57%
fubar

## dawiepoolman | 2022-08-17T16:16:25+00:00
pine64 support ticket is going unanswered. seems like they are deflecting the responsibility. 

## dawiepoolman | 2022-08-17T17:30:46+00:00
I think I found something to try..
based on this thread:
https://forum.pine64.org/showthread.php?tid=7387

when I run this in dir:
/sys/class/devfreq/ff9a0000.gpu$
![rockpro64memory](https://user-images.githubusercontent.com/2351212/185203949-92e2ad8c-b74d-4202-9d23-9e7703ff68c9.JPG)

maybe worth fiddling with other permutations e.g. set the 
cur_freq = 400000000 (instead of 500000000)
max_freq = 600000000 (instead of 800000000)
target_freq = 400000000 (instead of 500000000)

wcgw?

## dawiepoolman | 2022-08-17T17:58:31+00:00
ok, I only managed to set the max_freq 

root@rockpro64:/sys/class/devfreq/ff9a0000.gpu# echo 600000000 > max_freq
root@rockpro64:/sys/class/devfreq/ff9a0000.gpu# cat max_freq
600000000

permission is denied at runtime even for root for target_freq and cur_freq

lets see how it goes with at least the max_freq reduced...

## dawiepoolman | 2022-08-17T18:29:13+00:00
checking while running:
![image](https://user-images.githubusercontent.com/2351212/185215584-5dede62d-663c-4948-80c5-d57c9348ce54.png)

it is running super low at cur_freq = 200000000

## dawiepoolman | 2022-08-17T19:13:55+00:00
it failed again.
f@ck!

## osensei | 2022-08-18T00:54:13+00:00
Maybe try syncing to a USB-attached SSD storage and see if it works? (I believe I see a Sandisk portable SSD drive on your desk) 

Just to rule out a problem with the PCIe to M.2 adapter and/or the current SSD drive...

## dawiepoolman | 2022-08-18T06:23:58+00:00
not a bad idea at all. 
-However, I have scanned the nvme for errors and there were none.
-the other SSDs I have connected to running other nodes but I have spare HDDs (that might be slower but at least prove the point)
I will try an HDD and revert.

## dawiepoolman | 2022-08-18T12:08:27+00:00
I just completed another sync attempt to the nvme and also failed at 57% (where it failed last time)
starting the test on the hdd now..

## dawiepoolman | 2022-08-18T14:10:59+00:00
2%

## dawiepoolman | 2022-08-18T14:56:42+00:00
I hope this does not turn out to be true:
![image](https://user-images.githubusercontent.com/2351212/185426437-359817e5-f374-4dbc-88fe-af54fe353075.png)

HDD sync silly slow but maybe it is worth returning the nvme for a replacement as well just to be safe.
I will make a call after the weekend.  If the HDD stays stable with ambitious config settings it might be the nvme that turns out to cause the instability (or both ofc) 

## hyc | 2022-08-18T15:56:43+00:00
> based on this thread:

That thread is for the older Rock64, not for RockPro64. Completely different chip.

> when I run this in dir:
> /sys/class/devfreq/ff9a0000.gpu$

The GPU should have zero impact on anything here.

## dawiepoolman | 2022-08-18T16:48:00+00:00
@hyc, correct, the Rock64 is different but that forum was the closest example that I could find that explains an potential approach to solve the issue for the RockPro64 with a RK3399 chip.
I have since also posted a request on the armbian forum where I mentioned the files that I think are required for a different boot image here:
https://forum.armbian.com/topic/22967-rockpro64-ddr-clock-speed-causing-system-instability/
i.e. files:
rk3399pro_ddr_666MHz_v1.27.bin
rk3399pro_miniloader_v1.26.bin 

in the meantime I have also already submitted a return request for the nvme.  The courier will fetch the nvme card tomorrow. I will then replace the nvme with a better quality Samsung nvme to be extra safe.

I think @osensei  has a good suggestion to test an USB sync (SSD/HDD)  fwiw in the meantime.  

I did not realize that I was looking at the frequencies of the GPU instead of the ddr.  That could explain why the observed cur_freq = 200000000 at runtime (because there are no graphics being rendered in headless server mode?)

Anyways, whilst I wait for the pine64 engineers to have a look at my ticket for a potential board replacement, I might as well replace the nvme.  I do recall that we had stability issues with similar nvme cards at my workplace with the 'crucial' brand.


## dawiepoolman | 2022-08-18T17:17:12+00:00
This does not look good:
![image](https://user-images.githubusercontent.com/2351212/185455687-99c4e19c-9013-42c5-a406-c1be9ebec337.png)


## hyc | 2022-08-18T18:01:36+00:00
At this point the experiment seems pointless. Do a full sync on a PC, then copy the blockchain to the RockPro64 and see if it can stay sync'd without crashing.

## dawiepoolman | 2022-08-18T18:26:13+00:00
that is cheating :P 
..but an option for sure, however the sync experiment will give me better peace of mind that the hardware will be able to handle scaling in the coming years though.  I don't want to leave an underlying weakness in place when I can rather address it right up front.

I don't care about the time the chain takes to sync tbh. I have three other synced rpi3 nodes  already.  I want the expensive hardware to give me peace of mind that it will be stable when I need it to be 5 years from now when we take over the world 


## osensei | 2022-08-18T19:44:25+00:00
> the other SSDs I have connected to running other nodes 

If keeping the other nodes running is not critical, and you have enough available space in any of the other SSDs, I would try them out.

Syncing to HDD is painfully slow for monero, and not very practical (unless you have some fast RAID or SSD-cached hybrid setup)
Also, I'don't think it translates to a similar scenario, because the CPU will spend most of the time in IO wait state.

## dawiepoolman | 2022-08-18T21:18:59+00:00
that is.. an embarrassingly elegant recommendation.  I am too proud to admit I have not considered that.
That would indeed simulate a similar stress test between the cpu <-> ddr

let me get on that..

## dawiepoolman | 2022-08-18T22:10:09+00:00
cool
running on usb connected ssd.. 

## dawiepoolman | 2022-08-18T22:17:57+00:00
so far running stable (resuming from 18% that a previously connected node completed on the SSD)

I still see sporadic entries in the log like this:
![image](https://user-images.githubusercontent.com/2351212/185504789-efa90397-e9dc-4ffc-b30f-88acf8d9cae9.png)

anything to be concerned about?

## selsta | 2022-08-18T22:19:09+00:00
> anything to be concerned about?

AFAIK no. It is just an uncaught exception that gets logged.

## dawiepoolman | 2022-08-18T22:26:38+00:00
awesome thx.

KPIs:
![image](https://user-images.githubusercontent.com/2351212/185505113-38cee448-2e99-441d-b41e-6ad06c7664fb.png)

temp:  37.5 degrees (no fan, just heatsink)

config:
data-dir=/home/cypher/.bitmonero
log-file=/home/cypher/.bitmonero/monero.log
log-level=0
block-sync-size=100
db-sync-mode=safe
enable-dns-blocklist=1
enforce-dns-checkpointing=1
max-concurrency=0
limit-rate-up=1048576
limit-rate-down=1048576
max-log-files=1


## selsta | 2022-08-18T22:30:26+00:00
I would recommend to keep `block-sync-size` at default. And you don't need `enforce-dns-checkpointing`.

## dawiepoolman | 2022-08-18T23:04:35+00:00
thx.  updated!

## dawiepoolman | 2022-08-19T06:01:34+00:00
There it is: RockPro64 is the common denominator:
![image](https://user-images.githubusercontent.com/2351212/185552979-6f356673-13de-4775-aca7-ccab5831b3de.png)



## dawiepoolman | 2022-08-19T06:53:54+00:00
I have ordered a new RockPro64 whilst I wait for the Pine64 engineers to attend to the support ticket.  I dont want to be kept waiting for them to just confirm what we have proven here.

So hopefully soon with a new SBC and higher quality NVMe I can get this setup stable.  Thanks for all the interest, I hope the monero community can benefit from my novice experience.

## osensei | 2022-08-19T12:23:27+00:00
> There it is: RockPro64 is the common denominator: ![image](https://user-images.githubusercontent.com/2351212/185552979-6f356673-13de-4775-aca7-ccab5831b3de.png)

Hmm... I would say "file too large" seems like a "legit" error. 

Are you using ext4 on the USB-attached SSD? Did you check the available space? 
At this moment a pruned db uses 50 GB, while a full db uses 139 GB.

## dawiepoolman | 2022-08-19T12:53:06+00:00
1Tb ext4 filesystem. Recently formatted.  Used to be a BTC node that ran on a RPi3 which I have upgraded to a RPi4 so I had the SSD spare and converted to a xmr node on RPi3 for the lulz.  Nothing wrong with the SSD.
It only had the db on it and nothing else.


 

## osensei | 2022-08-19T13:16:37+00:00
Well, I guess the experiment is over, ha. Maybe close this issue then?

I hope you have better luck with the new RockPro64!



## dawiepoolman | 2022-08-19T13:19:08+00:00
Ok cool thx.  Let's close and I will give update when I receive the new SBC.
Later!

## dawiepoolman | 2022-08-23T06:21:40+00:00
How do you like them apples:?

![image](https://user-images.githubusercontent.com/2351212/186085070-c03bf2e7-586f-4c3a-a64a-8bdb54b4c49e.png)


I will share how I managed to achieve this (on the vulnerable rockpro64 SBC) shortly..

## dawiepoolman | 2022-08-23T15:24:24+00:00
Ok, so I thought that since cpu and memory cycles are in such a harmonious balance these days, maybe one could adjust the cpu clock cycles instead of the memory and then their interdependence will result in the ddr being passed a slower workload than the default (which clearly results in sporadic system overloads, at least in my case)

That is how I came across the topic of cpu governors
this paper here https://www.kernel.org/doc/ols/2006/ols2006v2-pages-223-238.pdf
has these graphs that made me think that maybe 'powersave' would result in lower demand on memory as well:
![image](https://user-images.githubusercontent.com/2351212/186194039-f8495bbe-bd20-4bf5-92d1-6dec3dfbd545.png)

so I changed it and...

resulting cpu speed:
![image](https://user-images.githubusercontent.com/2351212/186189957-28e7c1ed-91b0-4064-ae49-2084cfd7d6c6.png)
 
so it ran quite stable with the cpu threads not utilized fully (at least at first):
![image](https://user-images.githubusercontent.com/2351212/186189503-34ce7b65-e5ca-4730-bc63-a6e658d1b913.png)

temp sensors nice and low:
![image](https://user-images.githubusercontent.com/2351212/186190093-c845c2b9-fcb2-47cf-a2a9-7601e647c8f7.png)

at 52% synced the system got quite busy and the swap file even filled up, but it remained stable:
![image](https://user-images.githubusercontent.com/2351212/186190301-12c9e762-b08f-44a5-9174-87ba84895c3d.png)

the sync took about 48 hours to get to 97%, but the remaining 3% took another 48 hours with a massive workload
![image](https://user-images.githubusercontent.com/2351212/186190595-925d646d-d8af-43ff-b153-8766aeff81ec.png)
I am not sure whether this is a common experience generally since transaction volume in monero has picked up rather dramatically recently and hence blocks are bigger as well as the recent fork which increased ring sizes too.

summary of steps..
check existing available governors:
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_governors
debian for rockpro64 only shipped with options: performance schedutil
current setting for all cpus:
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
schedutil

to add extra governors:
sudo apt install cpufrequtils
now available options are:
conservative powersave ondemand userspace performance schedutil
set to powersave:
sudo nano /etc/default/cpufrequtils
GOVERNOR="powersave"
sudo systemctl restart cpufrequtils
reboot to be sure and confirm it is still set to "powersave":
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

a description of the different governor algorithms are here:
https://forum.xda-developers.com/t/cpu-governors-explained.1663809/

and how to change them as I explained here already is here:
https://dannyda.com/tag/scaling_available_governors/

hopefully this could help those coming after me to get their rockpro64 monero nodes running stable without the worry that future block sizes might corrupt their databases unexpectedly. Many rockpro64 sbc boards might have the same risk as mine but maybe just not as big so this could be a way to make sure it is at least a safety catch.

I would recommend the monero devs to maybe also consider making the default 'block-sync-size' monerod parameter a function of the host hardware and the median transactions within the blocks being synced somehow. I am sure that has been proposed already?

I have since ordered another rockpro64 since reverse logistics was too expensive anyways :P


## selsta | 2022-08-23T16:08:59+00:00
> the sync took about 48 hours to get to 97%, but the remaining 3% took another 48 hours with a massive workload

monerod contains checkpoints so that PoW verification can be skipped for known block hashes. All new blocks that get created after the latest checkpoint take longer to verify, that's usually why the last percentages take a while. And also due to increased usage.

> I would recommend the monero devs to maybe also consider making the default 'block-sync-size' monerod parameter a function of the host hardware and the median transactions within the blocks being synced somehow. I am sure that has been proposed already?

What is the issue with the default value currently? I usually keep it at default, but I also don't have a SBC.

## dawiepoolman | 2022-08-23T16:40:08+00:00
ah, the checkpoints makes sense for the pow verification.  I think even with the powersave governor the rockpro64 did very well i.e. roughly 4 days to sync 

potentially optimizing the workload passed to the hardware may decrease total sync time, however, as proven with the governors, the OS should be able process the loads with the current default parameters. Potentially sending smaller chuncks of work to the hardware just makes intuitive sense to me, at least for the SBC nodes with limited capacity.

anyways, thanks again for the amazing software.  It is fun being part of growing this ecosystem

# Action History
- Created by: dawiepoolman | 2022-07-29T08:13:37+00:00
- Closed at: 2022-08-23T16:44:00+00:00
