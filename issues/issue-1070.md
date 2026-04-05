---
title: 7700k running half the speed of 4790
source_url: https://github.com/xmrig/xmrig/issues/1070
author: jjziets
assignees: []
labels: []
created_at: '2019-07-23T22:35:17+00:00'
updated_at: '2019-07-24T22:45:12+00:00'
type: issue
status: closed
closed_at: '2019-07-24T22:45:12+00:00'
---

# Original Description
using ubuntu I noticed that 2.99 is half the speed compared to my 4790

![61751938-4c708980-adaa-11e9-80dd-f97947979cfd](https://user-images.githubusercontent.com/19214485/61752726-23052d00-adad-11e9-9a23-a27b8b1636dd.png)


![61752006-89d51700-adaa-11e9-8586-3c6b779427b4](https://user-images.githubusercontent.com/19214485/61752729-24365a00-adad-11e9-8479-18764da5e540.png)


I have tried to reduce the threads but has minimal effect.  Any suggestions 

Distributor ID: Ubuntu
Description:    Ubuntu 16.04.6 LTS
Release:        16.04
Codename:       xenial


# Discussion History
## jjziets | 2019-07-23T22:44:37+00:00
The rig with the 7700k has 16GB ram and the rig with the 4970 has 19gb ram

## jjziets | 2019-07-24T03:57:12+00:00
How do I enable +jit on Ubuntu? 

## jjziets | 2019-07-24T21:25:54+00:00
i just tested stock and it seems to be the same 

![image](https://user-images.githubusercontent.com/19214485/61829973-5bb70c00-ae6a-11e9-9f76-1c31f32d1434.png)



## jjziets | 2019-07-24T22:45:12+00:00
it is the gpu miner that has a high cpu usage on +6gpu rigs. 

![image](https://user-images.githubusercontent.com/19214485/61833707-72169500-ae75-11e9-8a4a-904c1ae25690.png)


# Action History
- Created by: jjziets | 2019-07-23T22:35:17+00:00
- Closed at: 2019-07-24T22:45:12+00:00
