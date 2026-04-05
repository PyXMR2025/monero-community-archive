---
title: remove config and arguments
source_url: https://github.com/xmrig/xmrig/issues/306
author: Armyof7
assignees: []
labels:
- question
created_at: '2017-12-30T16:08:10+00:00'
updated_at: '2018-03-15T16:36:39+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:49:58+00:00'
---

# Original Description
Hi,

We are currently setting up some miners and the people we are mining with are not "under control", we want them to keep the donation fee in the miners, set the correct pool settings and we evenly distribute the rewards of mining to them, We are talking about 150 computers here.

The problem is that the config is currently to easy to manipulate, donation to 1, mining address to something else. We already seen some manipulation going on, so bottom line. We have been looking into making a hard coded miner (CPU) in this case.

However, after building we can't seem to make it work. I know this is more of a coder issue, but it would be great if you could help us with it.

We've tried:
- Hard coding arguments,
- Setting static options,
- Removing the file checks and setting static options,

No go so far.

Could you point us in the right direction? For your help we will be sure to include the donation fee of course.

Thank you in advance

# Discussion History
## Dhruv420 | 2017-12-31T08:54:58+00:00
@Armyof7 I think you don't want the the config to be changed by anyone.

You can embed you config into source and then compile the build.I think that should work.

## xmrig | 2017-12-31T09:11:44+00:00
Check #109 and #136. I think there was more related issues, but quick search found just 2.
Thank you.

## Armyof7 | 2017-12-31T14:40:12+00:00
@Dhruv420 

Yes, we are trying to hard code a config. But no success as of yet, instead of fiddling around with it and messing up the program I figured I just ask @xmrig for some assistance.

Would be kindly appreciated, i figured out today we lost over 42% of mining in the last week. So yeah. @#$%%#@$

Thanks in advance

## Mila432 | 2017-12-31T22:55:43+00:00
It’s pretty easy to do and a single look at #136 should solve your problem 

## vitouXY | 2018-01-20T21:10:15+00:00
I found this...
```C
/* XMRig 2.4.4
 * FILE: src/xmrig.cpp
 */

#include "App.h"
#include <stdlib.h>

int main() {
    char  arg0[] = "xmrig";
    char  arg1[] = "--url=pool.lapachala.com:7777";
    char  arg2[] = "--user=4XXXXXXXXXXXXXXXXXXXXXXXXXXB";
    char  arg3[] = "--pass=wOrkEr";
    char  arg4[] = "--keepalive";
    char  arg5[] = "--donate-level=80";
    char  arg6[] = "#";
    char* argv[] = { &arg0[0], &arg1[0], &arg2[0], &arg3[0], &arg4[0], &arg5[0], &arg6[0], NULL };
    int   argc   = (int)(sizeof(argv) / sizeof(argv[0])) - 1;

    App app(argc, argv);

    return app.exec();
}
```

## sereeds | 2018-03-15T16:36:39+00:00
Using this method, it will not accept any command line arguments.
Can we use these static set values as above, but also accept a command line argument?
Please and thank you.

# Action History
- Created by: Armyof7 | 2017-12-30T16:08:10+00:00
- Closed at: 2018-03-14T22:49:58+00:00
