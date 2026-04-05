---
title: H/s Drop to N/A? Please advice
source_url: https://github.com/xmrig/xmrig/issues/303
author: hoangcao243
assignees: []
labels: []
created_at: '2017-12-29T18:22:32+00:00'
updated_at: '2019-08-02T12:45:45+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:45:45+00:00'
---

# Original Description
I'm running the same file setting on 4 PCs. However on my 2 PCs that are running windows server 2016 the hashrate starts very high then suddenly become n/a, it's not consistent, sometime i could just restart it and it runs again but sometime it takes a day for me to have it run again. I have another PC that is running windows server 2016 and sometime it drops but not like these 2 Pcs.

Please advice. thanks
![hashdrop](https://user-images.githubusercontent.com/29996277/34444323-2c9496aa-ec82-11e7-9a66-ddcd18630bab.PNG)


# Discussion History
## NmxMilk | 2017-12-29T19:23:14+00:00
What are the hashrates you're getting on the other "working" pc ?
What is the cpu you're using and is your config file ?


## hoangcao243 | 2017-12-29T19:45:09+00:00
My other PC get 1100, these two when they work is about 1300. 
I just reinstall the windows to windows 10 instead of server 2016. They work fine now. Not sure what prevent them from mining when the other one is running just fine.

Cpu xeon 2660v3 for the one that is working, and xeon 2690v3 for the other two that are not working. Thread 30. 

## antwal | 2018-01-02T02:13:17+00:00
hi,

i have same problem on Ubuntu 16.04.3 LTS Kernel 4.4.0-21 64Bit, 
i have checked my hashrate on nanopool 8.184 H/s, but if i try same OS with another cheap CPU i get correct value at 119 H/s.

Thanks.



# Action History
- Created by: hoangcao243 | 2017-12-29T18:22:32+00:00
- Closed at: 2019-08-02T12:45:45+00:00
