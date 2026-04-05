---
title: Bug with system account.
source_url: https://github.com/xmrig/xmrig/issues/1456
author: GjBrutello
assignees: []
labels: []
created_at: '2019-12-23T00:29:07+00:00'
updated_at: '2021-04-12T15:07:20+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:07:20+00:00'
---

# Original Description
**Describe the bug**
If xmrig is launched under "system" account then after 1-2 minutes all windows begging to hands.

**To Reproduce**
Create simple windows task with values "Run whether user is logged on or not"

![lags](https://user-images.githubusercontent.com/50217444/71328946-768cca00-2549-11ea-88bf-91d064569a0f.png)

it's other computer in other city.
![bug](https://user-images.githubusercontent.com/50217444/71329042-164a5800-254a-11ea-9a2b-ab9819f25943.png)

**Expected behavior**
the same computer but xmrig is launched under "user" so it works properly.
![good](https://user-images.githubusercontent.com/50217444/71329024-d3888000-2549-11ea-8978-de4f91cade8a.png)

**Additional context**
I wanted to create a windows task or start xmrig as a service with program nssm in order if my computer suddenly reboots then miner is able to start again without the need user login. But now when I log in to the computer after rebooting, all the windows are buggy(glitches) and I have to run a command "taskkill /f xmrig.exe" to disable the miner that works under the systems account. This was tested on about ten different computers with windows server 2008 R2 which are located in different locations(cities,countries) but some of them were worked fine under the system account.


# Discussion History
## APT-ZERO | 2019-12-27T20:48:36+00:00
Enable logs in parameters or config and attach it here

## GjBrutello | 2019-12-29T15:27:20+00:00
> 
> 
> Enable logs in parameters or config and attach it here


Windows hangs but xmrig is still mining.

![glitch](https://user-images.githubusercontent.com/50217444/71558814-48dfdd80-2a81-11ea-8493-4a03ab1a0dbe.png)

--



## GjBrutello | 2019-12-29T16:06:36+00:00
Короче, Здорова,! С наступающим тебя...! :) В общем, такая проблема,  на каждом пятом сервере с windows server 2008, независимо от версии xmrig наблюдаются зависания окон. До форка стояли майнеры 4-ой версии, которые на тот момент уже поддерживали RandomX и в ожидании форка майнили старый алго cn/r без проблем, но после форка на rx/0 многие серваки внезапно заглючили, все окна стали виснуть, я стал разбираться, обновил майнеры на 5-ую версию и понял, что проблема в том, что xmrig запущен как служба, то есть SESSIONAME "service". Если запускать xmrig от любой другой учетки с правами админа, юзера или даже system, но чтобы было SESSIONAME console или rdp-tcp, то все отлично, майнер работает, но получается для запуска майнера приходится логиниться на серваки, а значит в случае перезагрузки компа майнер самостоятельно не запустится. Пробовал много способов - создавал задачу от system учетки и запускал как служба c прогой nssm, даже менял запуск службы с логином и паролем от аминистратора, пытался через runas, но все равно проблема не решается, поскольку получается user "Administrator", а SESSIONNAME "service". В общем, не знаю, что делать, приходится постоянно следить и быть залогиненым на этих глючных серваках, а ведь до форка они около года майнили cn/r без каких либо проблем.

Скрины:
Как видно, если xmrig работает под SESSIONNAME service, то все глючит.
![glitch2](https://user-images.githubusercontent.com/50217444/71558934-83964580-2a82-11ea-9a91-207218be8839.png)

Здесь  SESSIONNAME rdp-tcp#1 поэтому работает должным образом.
![norm](https://user-images.githubusercontent.com/50217444/71559048-b42aaf00-2a83-11ea-8216-0a5e2abbab3b.png)

Здесь запущен от системной учетки с помощью psexec, но SESSIONNAME rdp-tcp#0, поскольку запуск psexec наследуется от пользователя, поэтому майнер тоже работает как надо.
![norm3](https://user-images.githubusercontent.com/50217444/71559329-e558ae80-2a86-11ea-8c14-ee024e89e5bd.png)

Add: Also manually added the accounts "system" and "local service" in the "Lock pages in memory" but nothing has changed.

--
So the issue is SESSIONNAME "service" but it is not exactly.

# Action History
- Created by: GjBrutello | 2019-12-23T00:29:07+00:00
- Closed at: 2021-04-12T15:07:20+00:00
