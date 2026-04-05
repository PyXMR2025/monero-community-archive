---
title: Termux c++ fatal eror
source_url: https://github.com/xmrig/xmrig/issues/1903
author: xerox87
assignees: []
labels: []
created_at: '2020-10-18T12:47:16+00:00'
updated_at: '2021-04-12T14:45:27+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:45:27+00:00'
---

# Original Description

![Screenshot_20201017-153415](https://user-images.githubusercontent.com/73064379/96367894-caa81100-1150-11eb-852e-b585c0a68abc.png)



# Discussion History
## DeadManWalkingTO | 2020-10-20T21:19:14+00:00
You can't build at Termux 

## Saikatsaha1996 | 2020-10-21T08:02:21+00:00
Just use this with out any error...

1) pkg upgrade -y
2) pkg install git cmake libuv clang nano -y
3) git clone --single-branch https://github.com/xmrig/xmrig.git
4) git clone https://github.com/xmrig/xmrig-amd.git (number 4 only for amd gpu in android)
5) cd xmrig
6) mkdir build && cd build
7) cmake .. -DWITH_HTTPD=OFF -DWITH_TLS=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DCMAKE_BUILD_TYPE=Release -DWITH_HWLOC=OFF
8) ls
9) make 
10) cp ../src/config.json config.json
11) nano config.json

11) donate.v2.xmrig.com:3333
12) xmr.pool.minergate.com:45700
13) CONTROL+\ ,donate.v2.xmrig.com:3333, replace with ( your pool address ) , y enter
14) Control +\ , and past   YOUR_WALLET_ADDRESS , replace with ( your user name or wallet address) , y enter, and scroll down and check your all details.. 
15) control + x 
16) y enter
17) enter
18) ./xmrig-notls
19) enjoy...!

## xerox87 | 2020-10-22T07:12:47+00:00
![Screenshot_20201022-091144](https://user-images.githubusercontent.com/73064379/96837436-b6ad2980-1446-11eb-8140-9882c2421597.png)


## xerox87 | 2020-10-22T07:13:00+00:00
Killed? 

## Saikatsaha1996 | 2020-10-22T07:30:33+00:00
Your ram not much
You need to some changes
10) cp ../src/config.json config.json
11) enter
12) nano config.json
13) enter

After that 
Change mode AUTO to light
...

## Saikatsaha1996 | 2020-10-22T07:37:39+00:00
![Screenshot_20201022-130625.png](https://user-images.githubusercontent.com/72664192/96839927-714d2400-1467-11eb-8332-e190b8f0d379.png)


Just change or replace "auto" to "light"

But you not get good hash rate you can get with light max 60 h/s and with auto 400+ h/s..

## xerox87 | 2020-10-22T09:01:36+00:00
Thx 55h/s ☺☺ I'll buy a phone soon, thank you for your advice

## Saikatsaha1996 | 2020-10-22T09:06:41+00:00
> Thx 55h/s ☺☺ I'll buy a phone soon, thank you for your advice

If you can buy samsung new series mobile.. 
Have amd gpu
And you can get good hash rate
But i recommend don't buy mobile for mineing
If you want buy raspberry Pi 3 model 
And make a mineing rig...

## xerox87 | 2020-10-22T10:35:08+00:00
I have raspbery pi 4 95h/s I'll try the pi data version amd whether it will be better h / s some recommendations regarding setting pi 4 so I tried better hash 2.1ghz and gpu 750 and no increase h / s

## Saikatsaha1996 | 2020-10-22T10:39:32+00:00
> I have raspbery pi 4 95h/s I'll try the pi data version amd whether it will be better h / s some recommendations regarding setting pi 4 so I tried better hash 2.1ghz and gpu 750 and no increase h / s

Make a rig raspberry Pi 3 with 10 pieces
You can get 800 h/s
Or make a rig raspberry Pi 0 with pieces
You can get good results..

# Action History
- Created by: xerox87 | 2020-10-18T12:47:16+00:00
- Closed at: 2021-04-12T14:45:27+00:00
