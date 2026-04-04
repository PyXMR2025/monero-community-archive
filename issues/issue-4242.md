---
title: Choice of Where to Download the Blockchain
source_url: https://github.com/monero-project/monero-gui/issues/4242
author: ThisNekoGuy
assignees: []
labels: []
created_at: '2023-11-07T19:57:21+00:00'
updated_at: '2024-02-01T17:51:56+00:00'
type: issue
status: closed
closed_at: '2023-11-09T09:38:48+00:00'
---

# Original Description
Using the Monero GUI flatpak, I noticed that the wallet seems to choose where to download the blockchain for you in the initial setup (it doesn't seem to ask) and this is a problem because, on OS/system drives that are tight on space (smaller SSD, for example, which is my problem), users may not be able to perform this process at all despite having a spare storage drive capable of doing this task.

An issue like this can be completely preventative from helping people enter the ecosystem.

# Discussion History
## mateMathieu | 2024-02-01T17:29:57+00:00
Hi @ThisNekoGuy ,
Here, there is an issue with flatpack access to an internal disk.
Maybe it comes from the btrfs filesystem. Other software like steam have no problem accessing it.

I tried to use flatseal to configure additional access to the HDD folder. But I get this error despite all the efforts (permission and ownership check) of making it available.
![Screenshot from 2024-02-01 16-21-44](https://github.com/monero-project/monero-gui/assets/3027020/ac934b89-6899-4281-ba8e-625dd5e233c5)


from /etc/fstab
`UUID=d4071983-a3a6-4621-a5e1-xxxxxxxxxxxx /mnt/d4071983-a3a6-4621-a5e1-xxxxxxxxxxxx  btrfs nosuid,nodev,nofail,x-gvfs-show 0 0`

Can you help?

## mateMathieu | 2024-02-01T17:50:06+00:00
Dear @BigmenPixel0,
Maybe you can help, all the folder's management by the gui app is not behaving well. 
For instance you get an error if you select any file-path of the app with the "Browse" button.
I am on linux Mint 23.1 here.
Thank you

## mateMathieu | 2024-02-01T17:51:55+00:00
More here: https://lr.vern.cc/r/Monero/comments/6zid4h/flatpak_of_the_monero_gui_wallet/

# Action History
- Created by: ThisNekoGuy | 2023-11-07T19:57:21+00:00
- Closed at: 2023-11-09T09:38:48+00:00
