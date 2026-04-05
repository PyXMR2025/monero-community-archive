---
title: xmrig does not run properly on MacOS High Sierra, ignoring many options, running
  sluggishly.
source_url: https://github.com/xmrig/xmrig/issues/752
author: shrewdacumen
assignees: []
labels:
- review later
created_at: '2018-09-12T18:56:05+00:00'
updated_at: '2021-04-12T15:57:52+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:57:52+00:00'
---

# Original Description
This happens on MacOS.
./xmrig -c some.file.json  --> produces an error if I removed config.json file.

However, bizarrely enough, making config.json into existence solves the problem.
cp some.file.json config.json
./xmrig --> run without problem.

xmrig does not recognize multi-cores on MacOS High Sierra.
Thus it runs sluggishly using 1-core only. (Intel i7 process felt useless with xmrig on MacOS)
And xmrig tends to ignore any command line arguments specified.

Topping it all off, "7-year-old-Macbook air" is much faster (2-3 times) than "latest Macbook Pro Retina" in terms of Hashrate with xmrig:  Something seriously wrong in it is going on!!!
(most of MacOS natively programs runs 5-15 times faster on Macbook Pro Retina than on 7-year-old Macbook Air.)

Both Macbook does not heat up much -> CPU are scarcely busy. (all CPU cores are idle but 1 core.)
Activity Monitor shows this.  Up to the point that even fans are not running.

<img width="1159" alt="speed comparison between" src="https://user-images.githubusercontent.com/684684/45455095-e7c3b780-b720-11e8-99ab-1216c09f2a22.png">


**

> And the following 2 my comments has more issues on top of this!!!

**

# Discussion History
## shrewdacumen | 2018-09-12T18:57:14+00:00
![screen shot 2018-09-13 at 3 56 27 am](https://user-images.githubusercontent.com/684684/45446895-1170e480-b709-11e8-980a-b5172433d32a.png)


## shrewdacumen | 2018-09-12T19:06:27+00:00
and if I specify "cpu-affinity": 0x00000f
xmrig exit with an error, while "cpu-affinity": null give no error.


![1 pro2015-sungwook local xmrig build vim 2018-09-13 04-00-12](https://user-images.githubusercontent.com/684684/45447379-58aba500-b70a-11e8-86fd-04f523182d96.png)
![2 pro2015-sungwook local xmrig build vim 2018-09-13 04-01-30](https://user-images.githubusercontent.com/684684/45447380-59443b80-b70a-11e8-8a28-b2b261bf717e.png)
![3 screen shot 2018-09-13 at 3 59 16 am](https://user-images.githubusercontent.com/684684/45447382-59443b80-b70a-11e8-82fe-10ffa96b7bb5.png)


## xmrig | 2018-09-13T09:29:17+00:00
1. `./xmrig -c some.file.json` work fine for me, please provide all possible information, what exactly error, etc.
2. `cn-heavy` required 4 MB of CPU cache per thread, but i5-5287U has only 3 MB, so 1 thread looks OK.
3. If you want change threads count, use option `threads`, for example `"threads": 2,`. `0x00000f` is invalid syntax for JSON, workaround is use decimal number `15` or string `"0x00000f"`.

## shrewdacumen | 2018-09-13T09:42:13+00:00
> `./xmrig -c some.file.json` work fine for me, please provide all possible information, what exactly error, etc.
> `cn-heavy` required 4 MB of CPU cache per thread, but i5-5287U has only 3 MB, so 1 thread looks OK.
> If you want change threads count, use option `threads`, for example `"threads": 2,`. `0x00000f` is invalid syntax for JSON, workaround is use decimal number `15` or string `"0x00000f"`.

./xmrig -c some.file.json --> seems to work at first
But if you remove 'config.json' (default json file) and then run './xmrig -c some.file.json' in the terminal of Mac,
It will return you an error which happened on my end.
xmrig tried to find 'config.json, neglecting command line option "-c some.file.json" and then will give you an error message.

And as I mentioned above, 7 year old Macbook air(Intel i5) runs more than 2 times faster than new Macbook Pro (intel i7) that will give you the hint that ./xmrig is not optimized for MacOS for sure.

Thanks

## dunklesToast | 2018-09-15T23:24:36+00:00
Since this issue already contains macOS bugs, I’ll add one:

The background parameter seems to be broken with High Sierra 

## dhniels | 2018-11-29T15:33:28+00:00
Seems to be broken in Mojave as well.

# Action History
- Created by: shrewdacumen | 2018-09-12T18:56:05+00:00
- Closed at: 2021-04-12T15:57:52+00:00
