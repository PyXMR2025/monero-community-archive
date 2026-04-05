---
title: Random "Aborted" / "Segmentation Fault" / "Bus error" messages and miner stops
source_url: https://github.com/xmrig/xmrig/issues/1803
author: offmarte
assignees: []
labels: []
created_at: '2020-08-07T19:22:49+00:00'
updated_at: '2020-08-10T17:01:41+00:00'
type: issue
status: closed
closed_at: '2020-08-10T17:01:41+00:00'
---

# Original Description
I'm getting these messages after mining for some time
![image](https://user-images.githubusercontent.com/62944284/89680372-335d4c80-d8c9-11ea-83b7-ea8518824816.png)
![image](https://user-images.githubusercontent.com/62944284/89680421-496b0d00-d8c9-11ea-898d-f02c5bc84d27.png)
![image](https://user-images.githubusercontent.com/62944284/89681038-8552a200-d8ca-11ea-903e-81e4f269b9e5.png)


I'm mining on cpu only. My PC:
- ryzen 5 1600 stock clocks
- 24gb 2666mhz ram
- ubuntu 20.04

I built xmrig from source. First I thought it could be debugging stuff happening, so i compiled with the `-DCMAKE_BUILD_TYPE=Release` tag, but no luck here.

Miner startup screen:
![image](https://user-images.githubusercontent.com/62944284/89680808-16754900-d8ca-11ea-86d9-c454fecdb2c0.png)


# Discussion History
## Lonnegan | 2020-08-07T22:52:19+00:00
There are two versions of the Ryzen 5 1600. The original Ryzen 5 1600 "Summit Ridge", introduced in mid 2017, and the new Ryzen 5 1600 "Pinnacle Ridge", introduced only in late 2019 as a cheaper version of the Ryzen 5 2600. Which one is yours?

The very early devices of the "Summit Ridge" had problems with segment faults in Linux. It was so heavy, that AMD offered to replace them :o
https://www.extremetech.com/computing/254750-amd-replaces-ryzen-cpus-users-affected-rare-linux-bug

Perhaps your system is affected by this?

## offmarte | 2020-08-08T00:12:22+00:00
Thanks Lonnegan, I'm going to investigate that. I have the first gen ryzen 5 1600, not the AF

## SChernykh | 2020-08-08T09:00:09+00:00
@codedracula4ec You could try to disable Opcache in BIOS. First gen Ryzens have this problem sometimes.

## offmarte | 2020-08-10T15:08:05+00:00
@SChernykh I didn't find that option in my b350 tomahawk arctic bios.
@Lonnegan my ryzen is one of the latest 1st gen ryzen lot, so it might be some other problem

**EDIT:** I updated the bios to the latest non beta and now there is opcache control in "cpu features". I just ran kill-ryzen.sh and it's working as it should, but the problem still persists on xmrig

## offmarte | 2020-08-10T17:01:16+00:00
Fixed! Thank you guys @SChernykh  @Lonnegan 
I built xmrig with opcache disabled and now it's working for 1 hour long in full speed without any crashes

# Action History
- Created by: offmarte | 2020-08-07T19:22:49+00:00
- Closed at: 2020-08-10T17:01:41+00:00
