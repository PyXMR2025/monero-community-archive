---
title: Low Hash Rate on Jetson AGX xavier
source_url: https://github.com/xmrig/xmrig/issues/2486
author: upinsbg
assignees: []
labels: []
created_at: '2021-07-19T05:57:02+00:00'
updated_at: '2021-07-20T19:34:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
hi, im  a newbie to mining and i had search over google unable to find suitable answer since i was using  jetson AGX xavier.. which is arm64 architecture...so the sources/fix i could find is limited

since the config file unable to run CPU + GPU together
i switch to command line 
i run 2 terminal
1 for gpu which is this
`./xmrig --donate-level 5 --no-cpu --cuda -o kp.unmineable.com:3333 -u <address> -k -a kawpow`

and another one for CPU which is this: 

however this one cause my xavier laggy
`./xmrig --donate-level 5 -o rx.unmineable.com:13333 -u <address> -k --cpu-priority=5 --cpu-max-threads-hint=80 --cpu-no-yield --hugepage-size=2048 --randomx-1gb-pages --randomx-mode=fast`


so i remove some param and become like this:
```
./xmrig --donate-level 5 -o rx.unmineable.com:13333 -u <address> -k  --cpu-no-yield
--randomx-1gb-pages --randomx-mode=fast
```

and here is the screen shot of what i get
CPU:RandomX
![image](https://user-images.githubusercontent.com/87630891/126103224-55515885-c5f1-48ae-bf53-17953ef1cc78.png)


and here for GPU:kawpow
![image](https://user-images.githubusercontent.com/87630891/126104329-6e26acac-2260-46e7-8ee8-7bc0bc76bff5.png)

....

and if i try to run only with GPU... 
![image](https://user-images.githubusercontent.com/87630891/126109659-af445e33-756c-4f5a-aad7-9b43c7e07b82.png)


![image](https://user-images.githubusercontent.com/87630891/126109700-d9346656-1384-4fdb-aec6-2751103a5c6f.png)

it seems that performance is increase a bit....however it is still far away from its max capability 1377 MHz


it seems to me running GPU only benefit more... as its was 1000 Hz more compared to CPU + GPU

therefore i would like to request the masters here for help... what i would need to do to increase my AGX xavier hash rate?


# Discussion History
## upinsbg | 2021-07-19T05:59:10+00:00
im currently mining shiba at unmineable 
i was wondering if the speed of unmineable affecting my hashrate as well.. but logically it should not.
please enlighten me

also...both CPU and GPU are mining SHiba for the same address.. i guess it should be fine ya?
just.. the worker on kawpaw didnt appear in unmineable

## Spudz76 | 2021-07-19T23:21:39+00:00
1GB hugepages aren't supported at all on arm64 stop bothering with that

Don't use no-yield if you also want it not to lag.

gcc7 sucks use newer

build the bundled deps with `./scripts/build_deps.sh` because the system-provided ones are old and suck too

## Spudz76 | 2021-07-19T23:25:19+00:00
also kawpow at 4295M difficulty that is not autodiff might as well be wasting your time it will never catch accepts

use MoneroOcean if you want to get XMR for other algos, with autodiff like all pools should have, or they suck.  It will also try other coins besides just kawpow which probably isn't the best bang for the GPU watt right now.  Autoswitching pool jumps algos based on prices while you sleep.

## upinsbg | 2021-07-20T18:12:29+00:00
![Screenshot_2021-07-21-01-05-05-391_com brave browser](https://user-images.githubusercontent.com/87630891/126374218-51670003-fb6e-42be-9824-ce7199006778.jpg)

its kinda weird.. the miner or the pool was not running correctly or what.. my stat show it has 0 hash rate for quite sometimes.

cant be sure about it.



## upinsbg | 2021-07-20T18:14:53+00:00
> 1GB hugepages aren't supported at all on arm64 stop bothering with that
> 
> Don't use no-yield if you also want it not to lag.
> 
> gcc7 sucks use newer
> 
> build the bundled deps with `./scripts/build_deps.sh` because the system-provided ones are old and suck too

alright. thanks for your suggestion.. i already down the huge page.. using sysctl vr-hugepages=4.. maybe i should set to 0.

also  i stop using cpu.. seems like focus on gpu have better result.. 
any comment? 


sure i will try that script

## upinsbg | 2021-07-20T18:20:38+00:00
> also kawpow at 4295M difficulty that is not autodiff might as well be wasting your time it will never catch accepts
> 
> use MoneroOcean if you want to get XMR for other algos, with autodiff like all pools should have, or they suck. It will also try other coins besides just kawpow which probably isn't the best bang for the GPU watt right now. Autoswitching pool jumps algos based on prices while you sleep.

one thing weird.. indeed it never show accept when i mining with gpu but it did catch accept on cpu!. however my mining result with gpu was like much2 better than cpu..
so i ignore that.

cant be helped.. the only compatible miner for jetson was xmrig here. and i found this pool unmineable from youtube.

maybe i should try switching the pool.


may enlighten me which pool works best for xmrig?

i try search like ethermine etc.. but those miner are not supported on ARM.. which is a headache working with jetson



## Spudz76 | 2021-07-20T19:32:40+00:00
I use MoneroOcean because it supports a bunch of algos (KawPow included) and pays XMR for everything, and everything is autodiff and works great.

Also the CPU would earn more processing some other coin too.  Setup one "rig" as the CPU by itself, and another copy of xmrig as another "rig" using the GPU only. Then it will build an effective hashrate list of all available and supported algos and pick the best one (max XMR output) for your hardware at any time.

# Action History
- Created by: upinsbg | 2021-07-19T05:57:02+00:00
