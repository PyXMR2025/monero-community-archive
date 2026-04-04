---
title: 'Send screen: some help text does not switch colour when switching from dark
  mode to light mode'
source_url: https://github.com/monero-project/monero-gui/issues/3135
author: endorxmr
assignees: []
labels: []
created_at: '2020-10-07T09:24:34+00:00'
updated_at: '2020-10-19T07:10:05+00:00'
type: issue
status: closed
closed_at: '2020-10-19T07:10:05+00:00'
---

# Original Description
In the Send screen, some of the help text for the advanced options (Key images and Offline transaction signing) always stays white, no matter the theme. This makes it unreadable when using a light theme. See attached screenshots.

<img width="509" alt="help-dark" src="https://user-images.githubusercontent.com/28117225/95312710-8d5d9c80-088f-11eb-860c-245361c0df3f.PNG">
<img width="540" alt="help-light" src="https://user-images.githubusercontent.com/28117225/95312719-8f276000-088f-11eb-909c-fce52032dcb9.PNG">



# Discussion History
## endorxmr | 2020-10-07T09:39:39+00:00
Could it be because of these two lines? I'm not familiar with Qt or the GUI code, but if I had to bet, this is where I'd put my money.

https://github.com/monero-project/monero-gui/blob/afc2e846fd280248610ab56eb5e39966f0305d5d/pages/Transfer.qml#L561

https://github.com/monero-project/monero-gui/blob/afc2e846fd280248610ab56eb5e39966f0305d5d/pages/Transfer.qml#L604

## selsta | 2020-10-07T11:01:24+00:00
Thanks for reporting. It was due to helpTextSmall using RichText, see #3136

# Action History
- Created by: endorxmr | 2020-10-07T09:24:34+00:00
- Closed at: 2020-10-19T07:10:05+00:00
