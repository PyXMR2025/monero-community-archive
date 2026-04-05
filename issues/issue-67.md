---
title: Disabled huge pages support if xmrig is launched from subfolder
source_url: https://github.com/xmrig/xmrig/issues/67
author: YetAnotherRussian
assignees: []
labels:
- bug
created_at: '2017-08-21T15:26:30+00:00'
updated_at: '2019-08-02T12:35:13+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:35:13+00:00'
---

# Original Description
Hi there :) You've just released v2.3.0 where you claim message about huge pages support fix.

I've just tested this one, and Win10 issue isn't fixed (I have never reported this one though :( )

System is Win10, G4600 CPU, 16Gb RAM, huge pages enabled.

Xmrig 1.0.1: available, enabled
Xmrig 2.0.1+: unavailable, disabled

Bat file is exactly the same:

xmrig.exe -o mine.aeon-pool.com:3333 --algo=cryptonight-lite --cpu-affinity 14 --print-time=5 --donate-level=3 -t 3 --av=2 -u qwerty -p x

It's not only message display theme, but the actual hashrate drop. I use msvc compiles, but there're no changes in gcc ones.

P.S. No issues found under Win7 on machines with similar (G4560 + 16Gb RAM) and other (i5-4570 + 32Gb RAM) config.

Thanks.


# Discussion History
## xmrig | 2017-08-21T15:45:05+00:00
There is no changes since version 1.0.0.
If all happen on same machine:
**unavailable** mean you not run miner as administrator, it required to use huge pages.
If you see **available, disabled** it means it fail to allocate huge pages, reboot should help.
Thank you.

## YetAnotherRussian | 2017-08-22T14:03:07+00:00
Lol, I've discovered the issue :) Affect version(s) = 1.0+ That was windows desktop folder. Note that cmd watcher is absent as well.

Take a look at my screen capture.

Note: no malware, no spyware, just .mp4 file.

## xmrig | 2017-08-22T14:19:11+00:00
Please upload video somewhere else, for example attach to comment. To much popups on that site and I don't know how download file from that site.

Mentioned message is just single line fix https://github.com/xmrig/xmrig/commit/beb9af43139312536b2861122689cc5e6de4af93

it regression since version 0.8, you still need run miner as admin and reboot or sign out required.

## YetAnotherRussian | 2017-08-22T14:21:16+00:00
Sorry, that's it. Link removed.

[Screencast 2017-08-22.zip](https://github.com/xmrig/xmrig/files/1242311/Screencast.2017-08-22.zip)

I tried 2.3.0 as well, with reboot also, doesn't help(

Launched 2.3.0 from "root" (C:\) folder to avoid any issues, works OK.


## xmrig | 2017-08-22T15:04:58+00:00
It strange, did you try create directory with only English characters? I tried create directory with Russian characters, all work fine, don't know how path can affect this feature.
Also you disable UAC? I don't see UAC prompt. Maybe it can cause this issue.
Thank you.

## YetAnotherRussian | 2017-08-22T18:05:29+00:00
Russian/English folder name does not make sense. Yes, UAC is fully disabled, but I think it's a "must have" for any rig :-D It's disabled through control panel native setting, not through any hacks (incl. registry tweaks or any tweaking software that may uninstall system components etc.). I'm using legit OEM win version, so no "custom builds", hacks or somethin.

No issues with other mining software that uses huge pages though :-/

## Unse | 2017-12-05T17:41:34+00:00
Прошу прощения, для лучшего понимания я буду на русском писать.

Шэф!
У меня примерно такая же беда, решил не открывать новый топик.
Есть 4 пк, в том числе даже с одинаковыми цпу, везде win 10 x64 pro.
На двух пк - свежеустановленная, на других - тоже самое, только установлено на год раньше. 
Но все обновлены до одинаковых версий.

На своем старом пк я просто прописал своего пользователя в политиках блокировки страниц и запускаю xmrig БЕЗ прав администратор (вообще батником), при этом UAC включен, но все работает. xmrig пишет: "HUGE PAGES: available, enabled'.
И на втором пк тоже самое. Все перепроверил - без админа, с уаком, юзер в политиках, страницы доступны.

А вот на других двух, где винду только только установил - ну никак. И разные версии пробовал начиная с 2.4.0.
Пользователь ( Все, Пользователь, Пользователи, Администраторы, Гости, короче на самом деле кого я туда только не добавлял) в политиках добавлен. 
Но! Если запускать НЕ ОТ администратора - страницы красные, недоступны, неактивированы.
Если от администратора - то доступны и активированы.

Системы хоть и в разное время устанавливалиьс из одного образа, цпу идентичные, памяти везде больше 12 гиг, настройки одинаковые.
Единственное различие между старыми и новыми - на старых я ВРУЧНУЮ прописывал пользователя в политиках блокировки страниц. (Т.к. тогда еще на xmr-stack сидел).
На обоих новых - я просто решил запустить с правами админа xmrig, чтобы он сам прописал пользователя. 

## Unse | 2017-12-05T17:54:58+00:00
В общем я нашел ГДЕ проблема, но не знаю кто виноват =)

На обоих новых пк имя пользователя было "user".
Хохмы ради я сделал нового пользователя "tester", удалил всех из политик, по новой, чтоб наверняка, добавил в Блокировку Страниц двух пользователей: "user" и "tester".
Перезагрузился, зашел под "user"ом - страницы не доступны без админских прав.
Вышел, зашел под "tester"ом - страницы ДОСТУПНЫ БЕЗ админских прав.
Но виновата винда или хмринг - не знаю, извините.

upd: виновата скорее все таки винда.  Потому что xmr-stack ведет себя аналогично абсолютно. Под "user" без админских прав не пользует страницы, под другим - пользует.

P.S. наверное надо было другую ветку все таки делать. Извиняюсь.

# Action History
- Created by: YetAnotherRussian | 2017-08-21T15:26:30+00:00
- Closed at: 2019-08-02T12:35:13+00:00
