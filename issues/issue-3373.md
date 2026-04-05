---
title: How to limit the number of CORES of a given CPU in the case of dual X99?
source_url: https://github.com/xmrig/xmrig/issues/3373
author: fil-br
assignees: []
labels: []
created_at: '2023-12-06T14:08:11+00:00'
updated_at: '2025-06-18T22:30:55+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:30:55+00:00'
---

# Original Description
Hello, I'm running XMRIG through hiveos on an X99 dual CPU motherboard with 2x e5 2673v4 with 40 cores and 80 threads in total, however, due to the L2 memory it is only running half of each CPU (CPU1 10c/20t and CPU2 10c/ 20t). Totaling 40 threads with a total of 9.8khs in mining (8gb RAM DDR4 2400Mhz for each CPU). Yesterday, a user told me to limit the number of Threads to 36 threads to increase the hashrate, which worked. Starting to do 11.7Khs. Looking at HIVEOS, one processor continues with 20 threads (average of 260 hours) and others with 16 threads (average of 400 hours). I would like to know if it is possible, within the CPU Configuration, to specify the number of Threads for each CPU, leaving 16 threads for each and what command to do this.

![photo_5154628416912337733_y](https://github.com/xmrig/xmrig/assets/123833820/607c6eb5-6d07-412a-8bdf-41e656effb99)


# Discussion History
## SlavisaBakic | 2023-12-06T17:45:52+00:00
According to this, Xeon E5 2673v4 have 50MiB of L3 cache which means you can mine with 25 threads per CPU.
https://www.cpu-world.com/CPUs/Xeon/Intel-Xeon%20E5-2673%20v4.html

In CPU config on screenshot you have option to set CPU affinity. In your case and assuming you have Hyper-Threading enabled:

`"rx/0":[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78]`

However, you only have one sticks of RAM per CPu and you should have 4 sticks of RAM per CPU because that CPU have quad-channel. If NUMA is disabled in BIOS, enable it so each CPU core can access RAM directly.

Also, I don't know how HiveOS CPU threads number works so you would have to run "lscpu" command to see affinitiy numbers for physical and HT threads. Monitoring in HiveOS also consumes CPU cycles and add CPU overhead which reduce hashrate.

## SlavisaBakic | 2023-12-06T18:09:33+00:00
More explanation for CPU config:
CPU1 - 0-39
CPU2 - 40-79

Even numbers are "physical" while odd numbers are HT ones. Fore example, CPU1 core 1 is "0, 1".

Dual Xeon E5-2673 v4 should reach 15-17k hashrate.

## fil-br | 2023-12-06T18:38:08+00:00
> More explanation for CPU config: CPU1 - 0-39 CPU2 - 40-79
> 
> Even numbers are "physical" while odd numbers are HT ones. Fore example, CPU1 core 1 is "0, 1".
> 
> Dual Xeon E5-2673 v4 should reach 15-17k hashrate.

Hi, I'll see if it's possible to activate HT (hyper-threading) and NUMA. But what would CPU Config look like?
"cpu1": { "rx/0":[0-39] }
"cpu2": { "rx/0":[40-79] }

???

## fil-br | 2023-12-06T18:45:39+00:00
> According to this, Xeon E5 2673v4 have 50MiB of L3 cache which means you can mine with 25 threads per CPU. https://www.cpu-world.com/CPUs/Xeon/Intel-Xeon%20E5-2673%20v4.html
> 
> In CPU config on screenshot you have option to set CPU affinity. In your case and assuming you have Hyper-Threading enabled:
> 
> `"rx/0":[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78]`
> 
> However, you only have one sticks of RAM per CPu and you should have 4 sticks of RAM per CPU because that CPU have quad-channel. If NUMA is disabled in BIOS, enable it so each CPU core can access RAM directly.
> 
> Also, I don't know how HiveOS CPU threads number works so you would have to run "lscpu" command to see affinitiy numbers for physical and HT threads. Monitoring in HiveOS also consumes CPU cycles and add CPU overhead which reduce hashrate.

But I don't think it can run 25t per CPU, since the L2 of this processor is 256kb per core (5120mb total), which is exactly what is needed by XMRIG per core/thread. An Epyc with 512kb per core can use all threads.

## SlavisaBakic | 2023-12-06T18:50:35+00:00
> But I don't think it can run 25t per CPU, since the L2 of this processor is 256kb per core (5120mb total), which is exactly what is needed by XMRIG per core/thread. An Epyc with 512kb per core can use all threads.

That is not correct. 
https://xmrig.com/docs/miner/randomx-optimization-guide#memory-size-requirements

RandomX requires 2MiB of last level cache per thread which is L3 in most cases. L2 cache needs to be 256KiB or higher. EPYCs can mine with all threads because they have a lot of L3 cache (exactly 2MiB L3 per thread or 4 MiB L3 cache per core).


## SlavisaBakic | 2023-12-06T18:55:38+00:00
> > More explanation for CPU config: CPU1 - 0-39 CPU2 - 40-79
> > Even numbers are "physical" while odd numbers are HT ones. Fore example, CPU1 core 1 is "0, 1".
> > Dual Xeon E5-2673 v4 should reach 15-17k hashrate.
> 
> Hi, I'll see if it's possible to activate HT (hyper-threading) and NUMA. But what would CPU Config look like? "cpu1": { "rx/0":[0-39] } "cpu2": { "rx/0":[40-79] }
> 
> ???

I've written it in my first message.

## Spudz76 | 2023-12-06T20:33:20+00:00
would be like 40 threads on the evens, Intel fake cores don't really do much but technically you could include 10 of the odd numbers like Slavisa's example (25 per cpu = 50MB L3) but I don't expect that to be worth as much
```
"rx/0":[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78]
```

## fil-br | 2023-12-07T13:48:58+00:00
> seriam cerca de 40 threads pares, os núcleos falsos da Intel não fazem muito, mas tecnicamente você poderia incluir 10 números ímpares, como o exemplo de Slavisa (25 por CPU = 50 MB L3), mas não espero que valha a pena como muito
> 
> ```
> "rx/0":[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78]
> ```

Hi, I did some tests, see below.

## fil-br | 2023-12-07T13:52:36+00:00
> > > Mais explicações para a configuração da CPU: CPU1 - 0-39 CPU2 - 40-79 
> > > Os números pares são "físicos", enquanto os números ímpares são HT. Por exemplo, o núcleo 1 da CPU1 é "0, 1". 
> > > Dual Xeon E5-2673 v4 deve atingir 15-17k hashrate.
> > 
> > 
> > Olá, vou ver se é possível ativar HT (hyper-threading) e NUMA. Mas como seria a configuração da CPU? "cpu1": { "rx/0":[0-39] } "cpu2": { "rx/0":[40-79] }
> > ???
> 
> Eu escrevi isso na minha primeira mensagem.

Hello,
Sorry, I didn't take L3 into consideration, but your calculations are right, the miner should use 25 threads, instead of the current 20. Could it be due to low RAM?

I did as you said and also did some tests.
In the first image, the test follows as indicated, but the hashrate dropped significantly, reaching 6.5khs.
In the second image, I put 15 colors for each processor, I thought it would improve... it only got worse going to 2.8khs. The third image is a variation (error) of the second, note that I forgot to put a core (13), note that a core there in the middle for 488h/s and increasing the total to 3khs. The fourth image is the best performing configuration, listing 0-35, I have a hash rate of 11.4khs.

Still looking to understand how this miner works and better configuration.

![a](https://github.com/xmrig/xmrig/assets/123833820/1cd8642b-e7fc-436a-9cb7-f0d802cc5a42)
.
.
.
![ex](https://github.com/xmrig/xmrig/assets/123833820/5fb63cda-d0c6-4045-b465-3339ea69a4d6)
.
.
.
![b](https://github.com/xmrig/xmrig/assets/123833820/44c127e0-8e53-4f22-b439-66026ea99e4d)
.
.
.
![c](https://github.com/xmrig/xmrig/assets/123833820/4571c9fd-c980-4dac-83d1-f9c82b1bf438)


## SlavisaBakic | 2023-12-07T13:56:21+00:00
Can you post here XMRig output instead of HiveOS dashboard?

## fil-br | 2023-12-07T14:03:39+00:00
> Can you post here XMRig output instead of HiveOS dashboard?
Could it be this screen? or using each core/thread?

![image](https://github.com/xmrig/xmrig/assets/123833820/ec0705ec-b970-421e-9cc8-f4e296b1187c)


## SlavisaBakic | 2023-12-07T14:14:51+00:00
Is it possible to scroll up and get that log from the start like this?

![image](https://github.com/xmrig/xmrig/assets/31129590/46088e01-e03d-4de7-82d2-6b8ef9262e92)


## fil-br | 2023-12-07T14:18:43+00:00
> Is it possible to scroll up and get that log from the start like this?
> 
> ![image](https://private-user-images.githubusercontent.com/31129590/288785035-46088e01-e03d-4de7-82d2-6b8ef9262e92.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDE5NTg3OTMsIm5iZiI6MTcwMTk1ODQ5MywicGF0aCI6Ii8zMTEyOTU5MC8yODg3ODUwMzUtNDYwODhlMDEtZTAzZC00ZGU3LTgyZDItNmI4ZWY5MjYyZTkyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjA3VDE0MTQ1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ0OWZkNGRjZTQzMDQ3M2JlNzQ4NTUwOGI2MTVmOTdhYjA0MGRiM2IzYTRkZWFhNTgyMTkxMmJmZDIwMzZlYmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.NZgOKb0JbRYKBBxkpfy8eFx4MJLIDzgLVTvFmY4utT4)

ok, I'll try. Below is an extra screen for analysis.
![image](https://github.com/xmrig/xmrig/assets/123833820/2616023c-cd3b-41e4-bdd9-88992456d3e1)


## fil-br | 2023-12-07T14:25:44+00:00
![image](https://github.com/xmrig/xmrig/assets/123833820/18559dd9-bbf4-47dd-8afa-7cb5da4c3b20)


## SlavisaBakic | 2023-12-07T14:43:15+00:00
It shouldn't be 36 threads but 50 threads according to CPU confg.
So it is either lack of RAM sticks and having only one memory channel per CPU or HiveOS.



Maybe you should first test using other OS like Windows Server or Ubuntu. 

Please download Ubuntu 22.04.3 LTS and create bootable USB disk.
https://releases.ubuntu.com/jammy/ubuntu-22.04.3-desktop-amd64.iso

You don't need to isntall it because there is option for trying out live version.
https://www.youtube.com/watch?v=3wofbmwLNUw

When you boot live Ubuntu you can download and run xmrig as root user. Default pool should be donation one so out of the box you should be able to see hashrate.

## fil-br | 2023-12-07T14:49:09+00:00
> It shouldn't be 36 threads but 50 threads according to CPU confg. So it is either lack of RAM sticks and having only one memory channel per CPU or HiveOS.
> 
> Maybe you should first test using other OS like Windows Server or Ubuntu.
> 
> Please download Ubuntu 22.04.3 LTS and create bootable USB disk. https://releases.ubuntu.com/jammy/ubuntu-22.04.3-desktop-amd64.iso
> 
> You don't need to isntall it because there is option for trying out live version. https://www.youtube.com/watch?v=3wofbmwLNUw
> 
> When you boot live Ubuntu you can download and run xmrig as root user. Default pool should be donation one so out of the box you should be able to see hashrate.

It has 36 threads as it is the one that gives the best mining results at the moment. Do you want me to test it with the parameters you indicated? or even without any parameters?

## SlavisaBakic | 2023-12-07T14:53:23+00:00
> It has 36 threads as it is the one that gives the best mining results at the moment. Do you want me to test it with the parameters you indicated? or even without any parameters?

Sory. In that case you will need to have 4 RAM sticks per CPU to utilize all memory channels and test it with more threads.



## fil-br | 2023-12-07T14:58:15+00:00
See in the image below that it is running with 50 threads, but the efficiency drops to 6.5khs

![image](https://github.com/xmrig/xmrig/assets/123833820/9f18b7af-2aa6-4be4-b394-78042f1da350)


## SlavisaBakic | 2023-12-07T15:02:55+00:00
It drops because not all CPU cores have direct access to RAM.

EDIT: You need to utilize all 4 memory channels per CPU.

https://xmrig.com/benchmark/2JVLZ8

## fil-br | 2023-12-07T15:05:13+00:00
> Sory. In that case you will need to have 4 RAM sticks per CPU to utilize all memory channels and test it with more threads.

ok, I have two Samsung, I will provide 6 more sticks with the same capacity and frequency, but from a different brand. It works?

## SlavisaBakic | 2023-12-07T15:06:35+00:00
> > Sory. In that case you will need to have 4 RAM sticks per CPU to utilize all memory channels and test it with more threads.
> 
> ok, I have two Samsung, I will provide 6 more sticks with the same capacity and frequency, but from a different brand. It works?

Only one way to find out. 

## fil-br | 2023-12-07T18:18:16+00:00
> > > Sory. In that case you will need to have 4 RAM sticks per CPU to utilize all memory channels and test it with more threads.
> > 
> > 
> > ok, I have two Samsung, I will provide 6 more sticks with the same capacity and frequency, but from a different brand. It works?
> 
> Only one way to find out.

Will the model MTA16ATF2G64AZ-2G3B1
 Does it work on XEON?, there is someone selling it close to me. It was installed on a server.

## SlavisaBakic | 2023-12-07T19:54:11+00:00
> > > > Sory. In that case you will need to have 4 RAM sticks per CPU to utilize all memory channels and test it with more threads.
> > > 
> > > 
> > > ok, I have two Samsung, I will provide 6 more sticks with the same capacity and frequency, but from a different brand. It works?
> > 
> > 
> > Only one way to find out.
> 
> Will the model MTA16ATF2G64AZ-2G3B1 Does it work on XEON?, there is someone selling it close to me. It was installed on a server.

Those are unregistered DIMMs and I'm afraid they won't work with RDIMMs you already have even if you are able to physically insert them to motherboard.


`M393A1G40DB1-CRC - Samsung 1x 8GB DDR4-2400 RDIMM PC4-19200T-R Single Rank x4 Module 
M393A1G40DB1-CRC0Q - Samsung 8GB DDR4-2400MHz PC4-19200 ECC Registered CL17 288-Pin DIMM 1.2V Single Rank Memory Module`

So basically, you would need 6 additional RDIMM (registered DIMM) DDR4-2400 CL17 ECC single rank. ECC RDIMMs are usually referred as server RAM. Desktop PCs and laptops use UDIMM (unregistered memory) and don't support ECC.

## fil-br | 2023-12-08T17:22:40+00:00
Updating. I added 2x RAM 16gb 2133Mhz. Totaling 48GB. the others I have are 2x 8gb 2400Mhz. However, after several tests I realized that 2 RAM slots are not working. I changed the position processors, but the problem persists. As the board is Chinese (shingsha x99 dual F2), I probably won't find BIOS available to update.

![WhatsApp Image 2023-12-08 at 14 10 01 (1)](https://github.com/xmrig/xmrig/assets/123833820/3c9d214b-40fe-4540-a65d-37700291b36c)
![WhatsApp Image 2023-12-08 at 14 10 01](https://github.com/xmrig/xmrig/assets/123833820/aba9e4da-284d-452c-b578-807c6376d238)

Adding more RAM, there was little difference, I believe that the maximum hashrate will only be obtained with 8 sticks of RAM. I also don't know if it would be of higher MHz and capacity,
![image](https://github.com/xmrig/xmrig/assets/123833820/7240843a-ae5d-471b-8237-d5eaceff63ee)


## Scaneruga | 2024-02-09T20:38:44+00:00
Please help me figure out the settings for 2 e5 2699v3 processors, I can't figure out what values to put here: "rx/0":
Thanks!

# Action History
- Created by: fil-br | 2023-12-06T14:08:11+00:00
- Closed at: 2025-06-18T22:30:55+00:00
