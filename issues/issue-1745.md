---
title: Welcome screen blank
source_url: https://github.com/monero-project/monero-gui/issues/1745
author: Premik
assignees: []
labels: []
created_at: '2018-11-19T13:29:55+00:00'
updated_at: '2019-01-29T07:28:58+00:00'
type: issue
status: closed
closed_at: '2019-01-29T07:28:58+00:00'
---

# Original Description
On the welcome screen I can only see the Title and no other controls:

![welcome](https://user-images.githubusercontent.com/842962/48709980-64827e80-ec07-11e8-91ba-9866c265f596.png)

I can close this window using alt+f4 and the wallet terminates. The rest of the wallet app seems to be working normally. But I can only unlock the latest wallet I've used and can't change wallet from gui.

Arch linux, installed `monero-wallet-qt 0.13.0.4-1` from AUR. But I've been facing this bug in several older versions too. Don't remember when it started first.

In the console output there are many WARN messages like this:
```QML QQuickItem: Detected anchors on an item that is managed by a layout. This is undefined behavior; use Layout.alignment instead```
And nothing else. But I'm seeing these all the times also in the main window (which works ok) so probably not related.






# Discussion History
## dEBRUYNE-1 | 2018-11-20T09:24:11+00:00
What happens if you simply hit enter on the welcome screen? 

## Premik | 2018-11-20T09:42:54+00:00
Enter does nothing. I've also tried tab, space, cursor keys and their combinations. Mouse clicks on the white space also does nothing. It is not a redrawing issue. I can resize the window using the bottom right icon and the title still renders correctly in the middle of the window. I think the controls are simply not there.

Maybe there is some issue with enumerating the available languages?

## dEBRUYNE-1 | 2018-11-21T11:36:55+00:00
>Maybe there is some issue with enumerating the available languages?

I suppose. Thanks for your report by the way. A quick "hack" I think you can use to open your desired wallet is to add the desired wallet name to the config file:

https://monero.stackexchange.com/questions/2866/where-are-the-monero-core-configuration-parameters-stored/

Lastly, pinging @skftn to have a look. 

## sanderfoobar | 2018-11-21T19:09:08+00:00
Could you temporarily switch to another DNS provider and restart the GUI? Ruling that one out...

I can try to reproduce in a VM if you ~~give me your Arch version~~. Other system details welcome too.

## Premik | 2018-11-22T09:55:16+00:00
@dEBRUYNE-1 Thanks for the workaround. I could use the montero-wallet-cli as well.

@skftn I changed my  DNS temporally to Google's 8.8.8.8. Made no difference. I've check with Wireshark and the Welcome screen is not making any connections so no surprise.

Arch is a rolling distro so there are no versions. Anything not older than 6 months should do. I run KDE and installed wallet from AUR using `yaourt monero-wallet-qt`. Provided this problem was not reported before I have bad feeling there must be something unique in my setup though.

I tried to open the wallet under a different user profile but the same blank screen.

I think the problem must be in the `wizards\WizardWelcome.qml`. I cloned the latest master branch and compiled with Debug and did `export "QT_LOGGING_RULES=*.debug=true"` in a hope to see more in the console output. Because there are some interesting logs statements in that qml file like: 
```
...
onStatusChanged: {
            if(status === XmlListModel.Ready){
                console.warn("languages availible: ",count);
                if(count < 2){
                    console.log("Skipping language page until more languages are availible")
                    wizard.switchPage(true);
                }
            }
        }
```

 But I've never seen that line (104) printed out. I tried to change it to `console.warn` but still it is not printing this line. So my best guess is this callback method gets never called..


## Premik | 2019-01-29T07:28:55+00:00
I can no longer reproduce this after a system update. Not sure what fixed this. `monero-wallet-qt` and lib is still on `0.13.0.4-1`. Maybe something with qt/kde libraries..

# Action History
- Created by: Premik | 2018-11-19T13:29:55+00:00
- Closed at: 2019-01-29T07:28:58+00:00
