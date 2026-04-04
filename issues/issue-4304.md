---
title: 1 million blocks behind after v0.18.3.3 upgrade
source_url: https://github.com/monero-project/monero-gui/issues/4304
author: Hueristic
assignees: []
labels: []
created_at: '2024-04-07T14:25:44+00:00'
updated_at: '2024-04-20T02:19:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Chain was fully synced before upgrade and now it seems to be re-syncing about 1/3rd of the db.

I was on monero-gui-install-win-x64-v0.18.3.2 or v0.18.3.1 before upgrade.

Is this a winblows Gui thing only?

I'm not going to upgrade anything else until this is addressed.

# Discussion History
## selsta | 2024-04-07T14:27:11+00:00
We released v0.18.3.2 about a month ago and have not received a single other report about this.

Can you share the output of "status" and "sync_info" from monerod?

## selsta | 2024-04-07T14:31:25+00:00
You have to enter it without quotes

## Hueristic | 2024-04-07T14:39:26+00:00
>>> status
[4/7/2024 10:36 AM] 2024-04-07 14:32:59.816 I Monero 'Fluorine Fermi' (v0.18.3.3-release) 
Error: Problem fetching info-- rpc_request:

*************************************************************************************************

>>> sync_info
[4/7/2024 10:38 AM] 2024-04-07 14:37:41.346 I Monero 'Fluorine Fermi' (v0.18.3.3-release) 
Height: 3102069, target: 3122172 (99.3561%) 
Downloading at 865 kB/s 
Next needed pruning seed: 7 
13 peers 
Remote Host Peer_ID State Prune_Seed Height DL kB/s, Queued Blocks / MB 
213.7.245.151:18080 117530896a9fdee6 standby 0 3122171 1 kB/s, 20 blocks / 7.82225 MB queued 
198.167.205.140:57020 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued 
188.166.112.13:18080 7f358c18318823ab standby 0 3122172 0 kB/s, 40 blocks / 15.7417 MB queued 
92.193.199.59:18080 9a85923dcec6174c standby 0 3122172 1 kB/s, 20 blocks / 7.77224 MB queued 
47.155.115.238:18080 756c7696938d9545 standby 0 3122172 0 kB/s, 160 blocks / 57.1135 MB queued 
94.130.9.215:18080 285856feee6defbe standby 0 3122171 1 kB/s, 120 blocks / 44.8534 MB queued 
185.220.101.32:18080 505ca1cff5645a5a standby 0 3122171 1 kB/s, 200 blocks / 68.7258 MB queued 
193.138.218.77:18080 b05a67f8aa942bb5 standby 0 3122172 0 kB/s, 40 blocks / 14.8923 MB queued 
188.165.183.122:18080 910c7bd3f97049fd synchronizing 0 3122126 860 kB/s, 0 blocks / 0 MB queued 
47.197.181.187:18080 dc99fdeab5a325f3 standby 0 3122172 0 kB/s, 40 blocks / 15.4055 MB queued 
192.243.60.111:18080 7ad6d0224431442b synchronizing 0 3122172 0 kB/s, 240 blocks / 84.8399 MB queued 
147.91.80.50:18080 ff6a73eeed7326af normal 0 1 0 kB/s, 0 blocks / 0 MB queued 
84.75.29.59:18089 1f698958c08bbf6f standby 0 3122172 1 kB/s, 40 blocks / 15.0211 MB queued 
53 spans, 377.399 MB 
[moooooooooooooooooooooooooooooooooooooooooooooooooooo] 
185.220.101.32:18080 20/185 (3102069 - 3102088, 5759 kB) 2060 kB/s (0.58) 
47.155.115.238:18080 20/185 (3102089 - 3102108, 6614 kB) 1883 kB/s (0.47) 
192.243.60.111:18080 20/185 (3102109 - 3102128, 5514 kB) 4442 kB/s (1) 
209.222.252.29:18380 20/185 (3102129 - 3102148, 5070 kB) 2284 kB/s (0.33) 
192.243.60.111:18080 20/185 (3102149 - 3102168, 5854 kB) 605 kB/s (1) 
185.220.101.32:18080 20/185 (3102169 - 3102188, 6210 kB) 1348 kB/s (0.58) 
47.155.115.238:18080 20/185 (3102189 - 3102208, 5314 kB) 1119 kB/s (0.47) 
209.222.252.29:18380 20/185 (3102209 - 3102228, 6933 kB) 1749 kB/s (0.33) 
174.29.99.236:18080 20/185 (3102229 - 3102248, 5543 kB) 1463 kB/s (0.42) 
209.222.252.29:18380 20/185 (3102249 - 3102268, 7110 kB) 181 kB/s (0.33) 
174.29.99.236:18080 20/185 (3102269 - 3102288, 6968 kB) 233 kB/s (0.42) 
185.220.101.32:18080 20/185 (3102289 - 3102308, 7176 kB) 858 kB/s (0.58) 
192.243.60.111:18080 20/185 (3102309 - 3102328, 7218 kB) 4225 kB/s (1) 
94.130.9.215:18080 20/185 (3102329 - 3102348, 7244 kB) 756 kB/s (0.24) 
47.155.115.238:18080 20/185 (3102349 - 3102368, 7266 kB) 771 kB/s (0.47) 
192.243.60.111:18080 20/185 (3102369 - 3102388, 7260 kB) 1799 kB/s (1) 
192.243.60.111:18080 20/185 (3102389 - 3102408, 7264 kB) 4162 kB/s (1) 
94.130.9.215:18080 20/185 (3102409 - 3102428, 7307 kB) 883 kB/s (0.24) 
47.155.115.238:18080 20/185 (3102429 - 3102448, 7381 kB) 1067 kB/s (0.47) 
185.220.101.32:18080 20/185 (3102449 - 3102468, 7260 kB) 1810 kB/s (0.58) 
192.243.60.111:18080 20/185 (3102469 - 3102488, 7385 kB) 4382 kB/s (1) 
192.243.60.111:18080 20/185 (3102489 - 3102508, 7478 kB) 967 kB/s (1) 
185.220.101.32:18080 20/185 (3102509 - 3102528, 7337 kB) 2054 kB/s (0.58) 
185.220.101.32:18080 20/185 (3102529 - 3102548, 7495 kB) 1877 kB/s (0.58) 
94.130.9.215:18080 20/185 (3102549 - 3102568, 7467 kB) 2092 kB/s (0.24) 
47.155.115.238:18080 20/185 (3102569 - 3102588, 7427 kB) 1436 kB/s (0.47) 
192.243.60.111:18080 20/185 (3102589 - 3102608, 7820 kB) 4908 kB/s (1) 
84.75.29.59:18089 20/185 (3102609 - 3102628, 7106 kB) 401 kB/s (0.13) 
192.243.60.111:18080 20/185 (3102629 - 3102648, 7391 kB) 1973 kB/s (1) 
94.130.9.215:18080 20/185 (3102649 - 3102668, 7502 kB) 1046 kB/s (0.24) 
185.220.101.32:18080 20/185 (3102669 - 3102688, 7653 kB) 1916 kB/s (0.58) 
47.155.115.238:18080 20/185 (3102689 - 3102708, 7596 kB) 1790 kB/s (0.47) 
174.29.99.236:18080 20/185 (3102709 - 3102728, 7468 kB) 1951 kB/s (0.42) 
192.243.60.111:18080 20/185 (3102729 - 3102748, 7050 kB) 4461 kB/s (1) 
185.220.101.32:18080 20/185 (3102749 - 3102768, 5936 kB) 1981 kB/s (0.58) 
174.29.99.236:18080 20/185 (3102769 - 3102788, 6117 kB) 1371 kB/s (0.42) 
94.130.9.215:18080 20/185 (3102789 - 3102808, 7657 kB) 523 kB/s (0.24) 
47.155.115.238:18080 20/185 (3102809 - 3102828, 7693 kB) 1821 kB/s (0.47) 
94.130.9.215:18080 20/185 (3102829 - 3102848, 7673 kB) 688 kB/s (0.24) 
185.220.101.32:18080 20/185 (3102849 - 3102868, 7748 kB) 1896 kB/s (0.58) 
92.193.199.59:18080 20/185 (3102869 - 3102888, 7772 kB) 510 kB/s (0.15) 
193.138.218.77:18080 20/185 (3102889 - 3102908, 6879 kB) 1093 kB/s (0.4) 
47.197.181.187:18080 20/185 (3102909 - 3102928, 7730 kB) 2308 kB/s (0.76) 
188.166.112.13:18080 20/185 (3102929 - 3102948, 7807 kB) 1899 kB/s (0.44) 
213.7.245.151:18080 20/185 (3102949 - 3102968, 7822 kB) 113 kB/s (0.03) 
84.75.29.59:18089 20/185 (3102969 - 3102988, 7914 kB) 480 kB/s (0.13) 
192.243.60.111:18080 20/185 (3102989 - 3103008, 7742 kB) 4167 kB/s (1) 
47.155.115.238:18080 20/185 (3103009 - 3103028, 7818 kB) 1461 kB/s (0.47) 
192.243.60.111:18080 20/185 (3103029 - 3103048, 6860 kB) 2762 kB/s (1) 
47.197.181.187:18080 20/185 (3103049 - 3103068, 7675 kB) 2730 kB/s (0.76) 
185.220.101.32:18080 20/185 (3103069 - 3103088, 6146 kB) 1985 kB/s (0.58) 
188.166.112.13:18080 20/185 (3103089 - 3103108, 7934 kB) 1017 kB/s (0.44) 
193.138.218.77:18080 20/185 (3103109 - 3103128, 8013 kB) 1573 kB/s (0.4)

## selsta | 2024-04-07T14:43:29+00:00
> Height: 3102069, target: 3122172 (99.3561%)

It says 99%. Did you already sync up most of the missing 1/3?

## Hueristic | 2024-04-07T14:45:40+00:00
nope weird huh.

![image](https://github.com/monero-project/monero-gui/assets/6501678/5defab0e-f291-4ac6-a1aa-e279b702861b)


## selsta | 2024-04-07T14:51:05+00:00
It seems you are conflating wallet and daemon sync. The daemon did not lose 1/3 of the progress, it's the wallet that is resyncing.

But something seems wrong, why does the "status" output not work for example? Without it the GUI won't function correctly.

Can you go to Settings -> Info and share

- Wallet mode
- Wallet restore height

Also do you manually start monerod.exe or do you let monero-gui handle the start / stopping?

## Hueristic | 2024-04-07T14:53:02+00:00
No manual intervention.




## selsta | 2024-04-07T14:54:45+00:00
Did you change the wallet restore height? It says 2024731 which is about the 1/3 you are re-syncing.

## Hueristic | 2024-04-07T14:55:18+00:00
That is from when wallet was added a few months ago.

## selsta | 2024-04-07T14:55:21+00:00
Also do you have Node -> Daemon start flags set?

## Hueristic | 2024-04-07T14:55:49+00:00
everything in this gui is default, no flags.

## selsta | 2024-04-07T14:57:29+00:00
When was the last time you had monerod synced up on this Windows PC?

## Hueristic | 2024-04-07T14:59:23+00:00
within the last few weeks.

## Hueristic | 2024-04-07T15:04:47+00:00
I noticed something else weird but would rather not post it here, can you pm me on bitcointalk or we can use irc?

## selsta | 2024-04-07T15:08:45+00:00
you can PM me on IRC (selsta), i don't have a bitcointalk account

## Hueristic | 2024-04-07T15:10:07+00:00
kk

## Kanopola | 2024-04-19T02:16:16+00:00
> Chain was fully synced before upgrade and now it seems to be re-syncing about 1/3rd of the db.
> 
> I was on monero-gui-install-win-x64-v0.18.3.2 or v0.18.3.1 before upgrade.
> 
> Is this a winblows Gui thing only?
> 
> I'm not going to upgrade anything else until this is addressed.

Apparently I'm not the only one who has this problem that arose after the update. I have formatted and returned to version 18.3.1 and it is still the same. I better stop wasting time mining.

Al parecer no soy el único que tiene ese problema que surgió después de la actualización. He formateado y he vuelto a la versión 18.3.1 y sigue igual. Mejor dejo de perder el tiempo minando.

## Hueristic | 2024-04-19T16:05:10+00:00
> Apparently I'm not the only one who has this problem that arose after the update. I have formatted and returned to version 18.3.1 and it is still the same. I better stop wasting time mining.

I've found a work around, you can set wallet restore height to current date.



## selsta | 2024-04-19T22:40:46+00:00
@Kanopola from which version to which version did you upgrade? and can you explain in detail what happened? which operating system are you using?

## Kanopola | 2024-04-20T02:08:25+00:00
> @Kanopola from which version to which version did you upgrade? and can you explain in detail what happened? which operating system are you using?


I think it was from 3.1 to 3.3. I have been updating until after 3.3 the Nodes do not synchronize and everything started to cause problems.

I will try to explain what I have done (I am attaching some screenshots of different events):

1.- I thought it was the Kaspersky antivirus and I deleted it; I also disabled all of Windows Defender, but the problem still persisted.

2.- I tried going back to versions 3.2 and 3.1, but it's still the same.

3.- I have uninstalled the program with Revo Unistaller and I have cleaned the Laptop with everything and registered with Glary Utilities to reinstall everything again, but the problem continued.

4.- Finally I formatted and only with the defender I installed the latest version and the problem continued even though I had given permissions in the firewall for the monero and P2Pool folders and files, and I added the port that it suggests for the Mini.

5.- I have also added them to exclusions and finally I have also disabled all the antivirus functions, but the problem continues.

Now the Nodes take time to synchronize and new ones are added, and also the wallet starts synchronizing from 3 million blocks and I have to wait more than 2 hours until it finishes.

6.- I have removed, cleaned and put on again, and it is still the same.

7.- I have also tried using the current date when I restore the wallet, but it continues to synchronize the wallet and the Nodes.

Sometimes it shows that everything is synchronized, but when I hit it to start, it keeps starting P2Pool and does not show the Hashes it mines or does anything else.

I suggest doing something one click like the "Vertcoin One Click Miner" I'm using as it's great to just boot up and start mining in the Pool without any issues.

Well, I'll wait for a next version with all these new problems corrected, since I don't plan to continue wasting my time with this as it is now.

Details of my Laptop:

Laptop: Dell Precision M4700
Processor: Intel(R) Core(TM) i7-3840QM CPU at 2.80 GHz.
RAM: 32GB
Video card 1: Intel(R) HD Graphics 4000 (integrated)
Video card 2: NVIDIA Quadro K2000M (external)
Operating System: Windows 10 Pro, version 22H2 (comp. 19045.4291)

Greetings!

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

Creo que fue de la 3.1 a la 3.3. He ido actualizando hasta que después de la 3.3 los Nodos no se sincronizan y todo empezó a dar problemas.

Te intentaré explicar lo que he hecho (adjunto algunas capturas de pantallas de diferentes eventos):

1.- Pensé que era el antivirus Kaspersky y lo eliminé; también deshabilité todo de Windows Defender, pero seguía el problema.

2.- Probé volver a las versiones 3.2 y 3.1, pero sigue igual.

3.- He desintalado el programa con Revo Unistaller y he limpiado la Laptop con todo y registro con Glary Utilities para volver a instalar todo de nuevo, pero seguía el problema. 

4.- Finalmente formatee y solo con el defender instalé la última versión y seguía el problema a pesar de que había dado permisos en el cortafuegos para las carpetas y archivos de monero y de P2Pool, y agregué el puerto que sugiere para la Mini.

5.- También los he agregado a exclusiones y finalmente también he deshabilitado todas las funciones del antivirus, pero sigue el problema.

Ahora los Nodos tardan en sincronizar y se van agregando nuevos, y también la billetera se empiezar a sincronizar desde los 3 millones de bloques y debo esperar más de 2 horas hasta que termine.

6.- He vuelto a quitar, limpiar y poner, y sigue igual.

7.- También he probado usar la fecha actual cuando restauro la billetera, pero sigue sincronizando la billetera y los Nodos.

A veces muestra que está todo sincronizado, pero cuando le doy a empezar, se queda iniciando el P2Pool y no muestra a los Hash que mina ni hace más nada.

Sugiero que hagan algo de un solo clic como el "Vertcoin One Click Miner" que estoy usando, ya que, es una maravilla que iniciar solo y empieza a minar en la Pool sin problemas.

Bueno, esperaré una próxima versión con todos estos problemas nuevos corregidos, ya que, no pienso seguir perdiendo el tiempo con esto como está ahora.

Detalles de mi Laptop:

Laptop: Dell Precision M4700
Procesador: Intel(R) Core(TM) i7-3840QM CPU a  2.80 GHz.
RAM: 32GB
Tarjeta de video 1: Intel(R) HD Graphics 4000 (integrada)
Tarjeta de video 2: NVIDIA Quadro K2000M (externa)
Sistema Operativo: Windows 10 Pro, versión 22H2 (comp. 19045.4291)

¡Saludos!

![Screenshot_1](https://github.com/monero-project/monero-gui/assets/56226178/30b543e7-9324-4fc1-ad21-e74965316716)
![Screenshot_3](https://github.com/monero-project/monero-gui/assets/56226178/5c5e2f1d-1c95-4499-8aa2-fb56a25fa938)
![Screenshot_5](https://github.com/monero-project/monero-gui/assets/56226178/59030964-eee1-462a-a4ad-200cc3a6ef5c)


# Action History
- Created by: Hueristic | 2024-04-07T14:25:44+00:00
