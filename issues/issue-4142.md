---
title: 'monerod.service: Can''t open PID file /home/satoshi/.bitmonero/monerod.pid
  (yet?) after start: No such file or direc'
source_url: https://github.com/monero-project/monero/issues/4142
author: Sologigabit
assignees: []
labels:
- invalid
created_at: '2018-07-16T12:06:57+00:00'
updated_at: '2019-07-10T03:58:04+00:00'
type: issue
status: closed
closed_at: '2018-08-15T11:41:02+00:00'
---

# Original Description
I followed this docu:
https://freedomnode.com/blog/110/how-to-install-and-set-up-full-monero-node-on-linux

I am geting this error:

root@Monero:/home/satoshi/.bitmonero# systemctl monerod.service
Unknown operation monerod.service.
root@Monero:/home/satoshi/.bitmonero# systemctl status monerod.service
* monerod.service - Monero Full Node
   Loaded: loaded (/lib/systemd/system/monerod.service; enabled; vendor preset: enabled)
   Active: failed (Result: timeout) since Mon 2018-07-16 13:56:38 CEST; 39s ago
  Process: 3378 ExecStart=/usr/local/bin/monerod --restricted-rpc --block-sync-size 3 --confirm-external-bind --config-file /home/satoshi/.bitmonero/m

Jul 16 13:55:08 Monero systemd[1]: Starting Monero Full Node...
Jul 16 13:55:09 Monero monerod[3378]: 2018-07-16 11:55:09.710            7f23c10bbbc0        INFO         global        src/daemon/main.cpp:283
Jul 16 13:55:09 Monero monerod[3378]: Forking to background...
Jul 16 13:55:09 Monero systemd[1]: monerod.service: Can't open PID file /home/satoshi/.bitmonero/monerod.pid (yet?) after start: No such file or direc
![pid error monero](https://user-images.githubusercontent.com/35578253/42757771-7992247e-8901-11e8-978a-67e93ea6ae0e.png)

Jul 16 13:56:38 Monero systemd[1]: monerod.service: Start operation timed out. Terminating.
Jul 16 13:56:38 Monero systemd[1]: monerod.service: Failed with result 'timeout'.
Jul 16 13:56:38 Monero systemd[1]: Failed to start Monero Full Node.

root@Monero:/home/satoshi/.bitmonero#


# Discussion History
## moneromooo-monero | 2018-07-16T22:08:02+00:00
That seems to be a problem with the config file.

 Are you using the one from monero or another from somewhere else ?

## Sologigabit | 2018-07-17T09:18:55+00:00
I see thise steps. 
https://freedomnode.com/blog/110/how-to-install-and-set-up-full-monero-node-on-linux

cd /lib/systemd/system
sudo wgethttps://gist.githubusercontent.com/mariodian/b8bb62de8f5aa5466cccb17f280f439e/raw/db0a98573e0a8cc871781d8d43f03437ca159e22/monerod.service 
<https://gist.githubusercontent.com/mariodian/b8bb62de8f5aa5466cccb17f280f439e/raw/89d339eb064065a5f915b5d868f44ddaa3395101/monerod.service>sudo chmod 644 monerod.service

Saludos Cordiales / Kind regards / Mit freundlichen Grüßen / Cordialement / Met vriendelijke groet

Joaquín Ignacio
Administrador de Cuentas / Account Manager

SoloGigabit Carrier Nuetral DataCenter
P.I. Fuente del Jarro
Plaza de Elche 14-15
46988 Paterna, Valencia
España

El 17/07/2018 a las 0:08, moneromooo-monero escribió:
>
> That seems to be a problem with the config file.
>
> Are you using the one from monero or another from somewhere else ?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub 
> <https://github.com/monero-project/monero/issues/4142#issuecomment-405396890>, 
> or mute the thread 
> <https://github.com/notifications/unsubscribe-auth/Ah7hjdZ3m35erZRYNCNyn1wKX3v91zhLks5uHQ7QgaJpZM4VRAtZ>.
>



## Sologigabit | 2018-07-17T09:19:55+00:00
Clone the repository and its submodules:

git clone --recursivehttps://github.com/monero-project/monero cd monero
make -j2 release # -j4 for 4 threads etc

It may take a while to compile depending on your machine.

When finished, copy all the binaries to|/usr/local/bin|:

sudo cp ./build/release/bin/* /usr/local/bin/

*Top 5 Reasons Monero Will Become the Most Widely Used Private and 
Anonymous Cryptocurrency* 
<https://freedomnode.com/blog/85/top-5-reasons-monero-will-become-the-most-widely-used-anonymous-cryptocurrency>


    /*4*/Set up the service

I've written a systemd service that automatically starts the node after 
a reboot or when crashed.

cd /lib/systemd/system
sudo wgethttps://gist.githubusercontent.com/mariodian/b8bb62de8f5aa5466cccb17f280f439e/raw/db0a98573e0a8cc871781d8d43f03437ca159e22/monerod.service 
<https://gist.githubusercontent.com/mariodian/b8bb62de8f5aa5466cccb17f280f439e/raw/89d339eb064065a5f915b5d868f44ddaa3395101/monerod.service>sudo chmod 644 monerod.service

Saludos Cordiales / Kind regards / Mit freundlichen Grüßen / Cordialement / Met vriendelijke groet

Joaquín Ignacio
Administrador de Cuentas / Account Manager

SoloGigabit Carrier Nuetral DataCenter
P.I. Fuente del Jarro
Plaza de Elche 14-15
46988 Paterna, Valencia
España

El 17/07/2018 a las 0:08, moneromooo-monero escribió:
>
> That seems to be a problem with the config file.
>
> Are you using the one from monero or another from somewhere else ?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub 
> <https://github.com/monero-project/monero/issues/4142#issuecomment-405396890>, 
> or mute the thread 
> <https://github.com/notifications/unsubscribe-auth/Ah7hjdZ3m35erZRYNCNyn1wKX3v91zhLks5uHQ7QgaJpZM4VRAtZ>.
>



## moneromooo-monero | 2018-07-17T10:08:38+00:00
Try with the monero config file (utils/systemd/monerod.service).

## Sologigabit | 2018-07-17T11:03:32+00:00
I followed these steps. https://freedomnode.com/blog/110/how-to-install-and-set-up-full-monero-node-on-linux

cd /lib/systemd/system
sudo wget https://gist.githubusercontent.com/mariodian/b8bb62de8f5aa5466cccb17f280f439e/raw/db0a98573e0a8cc871781d8d43f03437ca159e22/monerod.service
sudo chmod 644 monerod.service

Clone the repository and its submodules:

git clone --recursive https://github.com/monero-project/monero
cd monero
make -j2 release # -j4 for 4 threads etc

It may take a while to compile depending on your machine.

When finished, copy all the binaries to /usr/local/bin:

sudo cp ./build/release/bin/* /usr/local/bin/

Top 5 Reasons Monero Will Become the Most Widely Used Private and Anonymous Cryptocurrency
4
 Set up the service

I've written a systemd service that automatically starts the node after a reboot or when crashed.

cd /lib/systemd/system
sudo wget https://gist.githubusercontent.com/mariodian/b8bb62de8f5aa5466cccb17f280f439e/raw/db0a98573e0a8cc871781d8d43f03437ca159e22/monerod.service
sudo chmod 644 monerod.service

## jtgrassie | 2018-07-17T13:43:21+00:00
> root@Monero:/home/satoshi/.bitmonero# systemctl monerod.service
> Unknown operation monerod.service.

For starters you are missing the word `start`. It should be:
```
sudo systemctl start monerod.service
```

## moneromooo-monero | 2018-08-15T11:13:34+00:00
This is a problem with the config file from that location, and no comment after being asked to try to one from the monero tree, closing.

+invalid

## sephethus | 2019-07-10T03:27:24+00:00
I had this same problem and from the same guide, I tried the monerod.service file from the source as suggested above, same problem, same error. There is no pid file in the monero folder. Where is the PID file or where should it be? utils/systemd/monerod.service did not work.

## jtgrassie | 2019-07-10T03:36:04+00:00
@sephethus that guide linked at the top of this thread is wrong. If you used the service file thats actually in this repository, you'd see it specifies a pid file and the correct parameter to create it.

Copy the monerod.service file from this repository to the correct destination (e.g. on Ubuntu this can be either `/etc/systemd/system/` or `/lib/systemd/system/`), then run `sudo systemctl enable monerod` and `sudo systemctl start monerod`. The service file in this repository assumes the user reads it, knows how to used systemd and knows how to create a user/group ("monero" in this case) on their system. The Monero StackExchange is a better place for support, not a this github bug/issue tracker.

# Action History
- Created by: Sologigabit | 2018-07-16T12:06:57+00:00
- Closed at: 2018-08-15T11:41:02+00:00
