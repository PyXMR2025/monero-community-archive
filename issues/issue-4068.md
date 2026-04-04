---
title: '[feature] Add ''Restore from QR'' option to Welcome To Monero wallet menu'
source_url: https://github.com/monero-project/monero-gui/issues/4068
author: CryptoGrampy
assignees: []
labels: []
created_at: '2022-11-13T18:22:33+00:00'
updated_at: '2022-12-12T16:51:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero GUI should support restoring wallets from QR codes containing the Monero restore wallet URI scheme.

I think the best place for this would be on the 'Welcome to Monero' menu as a new menu option.  Adding this feature to the main Monero wallet would allow for much easier onboarding of new users through gift cards, and additionally would make wallet backup/restores much easier to deal with.  

# Discussion History
## plowsof | 2022-12-12T16:45:22+00:00
I've just been testing the webcam features already added to the Monero GUI (selsta helped me set it up / fixed some dependency issues i had). I assumed it was only for the transfer screen , to grab a payment uri and auto fill the recipient/amount fields. I noticed the js function https://github.com/monero-project/monero-gui/blob/master/js/Wizard.js#L3 and went immediately to the 'restore wallet from seed/keys page' and there is an extra 'restore from qr' radio button now - which once clicked brings up the camera feed. after scanning a wallet uri the fields are auto filled. 
restore wallet page:
![Screenshot from 2022-12-12 16-50-22](https://user-images.githubusercontent.com/77655812/207104839-b8691e40-aaf3-4204-8965-ac0e413e445c.png)
transfer page:
![Screenshot from 2022-12-12 16-49-59](https://user-images.githubusercontent.com/77655812/207104913-dc741899-577d-409c-885a-3419fdbb722b.png)



# Action History
- Created by: CryptoGrampy | 2022-11-13T18:22:33+00:00
