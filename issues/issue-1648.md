---
title: Xmrig dev fee is set to 12% after build
source_url: https://github.com/xmrig/xmrig/issues/1648
author: Maz4id
assignees: []
labels: []
created_at: '2020-04-17T17:59:48+00:00'
updated_at: '2020-04-18T09:39:33+00:00'
type: issue
status: closed
closed_at: '2020-04-18T09:39:33+00:00'
---

# Original Description
So I tried to build xmrig with 0 dev fee but after when I run:
./xmrig --donate-level 0 -o pool.supportxmr.com:443 -u mywallet -p worker1 -k --tls
 dev fee is set to 12%
![image](https://user-images.githubusercontent.com/51741745/79599196-c3df0980-80ed-11ea-8369-e3e3619015f5.png)

Here is a video when I compiled the miner: https://youtu.be/MItw760dioo


# Discussion History
## xmrig | 2020-04-17T19:45:39+00:00
It very confusing, it should work as expected even if not specify `--donate-level` option.

Are you sure you virtual machine or hypervisor is not compromised somehow?

1. Please share cloned source code.
2. Don't use `-DBUILD_STATIC=ON` unless you exactly know what you doing.

Thank you.

## Unnameless | 2020-04-17T20:12:57+00:00
There is no reason to change the max dev fee. Only the min. Build it so without any flags and try again using a config file

## ghost | 2020-04-18T00:00:53+00:00
> So I tried to build xmrig with 0 dev fee but after when I run:
> ./xmrig --donate-level 0 -o pool.supportxmr.com:443 -u mywallet -p worker1 -k --tls
> dev fee is set to 12%
> ![image](https://user-images.githubusercontent.com/51741745/79599196-c3df0980-80ed-11ea-8369-e3e3619015f5.png)
> 
> Here is a video when I compiled the miner: https://youtu.be/MItw760dioo

If you forked it through github, then go to src folder and edit the donation file, then head to the bottom, then change the max donation = 5% any percent you want, then the min donation = 0% if you don't want to donate the dev through xmrig, you can donate dev through his wallet. After you edited it save it. Clone your forked repository to your computer and start building it with gcc or msvc. After you build it, head to the website xmrig.com then go to the wizard and set your config, after that download your config to your computer. Open your config.json through notepad then change the donate level to 0, and save it, then put it on the folder where your custom xmrig sit. Then right click on the xmrig.exe then send it to desktop(create shortcut). Go to your desktop and right click the xmrig.exe shortcut, don't add any command lines just head through advance then allow the app to run administrator then apply then save. Finally run the app

## Maz4id | 2020-04-18T09:39:33+00:00
> It very confusing, it should work as expected even if not specify `--donate-level` option.
> 
> Are you sure you virtual machine or hypervisor is not compromised somehow?
> 
> 1. Please share cloned source code.
> 2. Don't use `-DBUILD_STATIC=ON` unless you exactly know what you doing.
> 
> Thank you.

I know what I'm doing, actually was from my VPS, I don't know what but I tried on another machine and now works perfectly, thanks for the help.

# Action History
- Created by: Maz4id | 2020-04-17T17:59:48+00:00
- Closed at: 2020-04-18T09:39:33+00:00
