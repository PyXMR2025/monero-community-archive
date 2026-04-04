---
title: Appimage version ?
source_url: https://github.com/monero-project/monero-gui/issues/3699
author: cassepipe
assignees: []
labels: []
created_at: '2021-09-13T09:18:07+00:00'
updated_at: '2021-09-13T09:26:36+00:00'
type: issue
status: closed
closed_at: '2021-09-13T09:26:36+00:00'
---

# Original Description
I am trying to integrate the `monero-wallet.AppImage` contained in the [getmonero.org Linux downlaod](https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.17.2.3.tar.bz2) but AppImageLauncher does not recognize it  as an AppImage. 
I have tried to inspect it but the --apimage-extract option does not exist on it apparently. 
What version of AppImage is this ? How is it built ?
I realize the issue could be coming from AppImageLauncher but since all other AppImages worked fine with it so far I thought there might be something weird about this one.

# Discussion History
## cassepipe | 2021-09-13T09:26:36+00:00
My bad I did not search correctly. The answer is [here]( https://github.com/monero-project/monero-gui/issues/3045#issuecomment-676082064)

Did you consider shipping a genuine AppImage that can be integrated to the desktop ?

# Action History
- Created by: cassepipe | 2021-09-13T09:18:07+00:00
- Closed at: 2021-09-13T09:26:36+00:00
