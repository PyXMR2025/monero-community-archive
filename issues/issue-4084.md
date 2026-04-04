---
title: Menu shortcut doesn't show up on Tails (.desktop file incorrect?)
source_url: https://github.com/monero-project/monero-gui/issues/4084
author: ghost
assignees: []
labels: []
created_at: '2022-12-17T21:29:49+00:00'
updated_at: '2022-12-18T03:12:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
So the menu shortcut doesn't show up on tails and supposedly it did before > https://xmrguide.org/tails/gui/install/manual

The desktop file was generated in **monero-gui.desktop**`/live/persistence/TailsData_unlocked/dotfiles/.local/share`

### This is what the generated desktop file by the appimage created:

``` [Desktop Entry]
Name=Monero GUI
GenericName=Monero-GUI
X-GNOME-FullName=Monero-GUI
Comment=Monero GUI
Keywords=Monero;
Exec=/home/amnesia/Persistent/Monero GUI/monero-gui-linux-x64-v0.18.1.2/monero-gui-v0.18.1.2/monero-wallet-gui %u
Terminal=false
Type=Application
Icon=monero
Categories=Finance;Network;
MimeType=x-scheme-handler/monero;x-scheme-handler/moneroseed
StartupNotify=true
X-GNOME-Bugzilla-Bugzilla=GNOME
X-GNOME-UsesNotifications=true
StartupWMClass=monero-wallet-gui
```
### This is what default `electrum.desktop` file looks like in tails
``` [Desktop Entry]
Comment=Lightweight Bitcoin Client
Exec=sh -c "PATH=\"\\$HOME/.local/bin:\\$PATH\"; electrum %u"
GenericName[en_US]=Bitcoin Wallet
GenericName=Bitcoin Wallet
Icon=electrum
Name[en_US]=Electrum Bitcoin Wallet
Name=Electrum Bitcoin Wallet
Categories=Finance;Network;
StartupNotify=true
StartupWMClass=electrum
Terminal=false
Type=Application
MimeType=x-scheme-handler/bitcoin;
Actions=Testnet;

[Desktop Action Testnet]
Exec=sh -c "PATH=\"\\$HOME/.local/bin:\\$PATH\"; electrum --testnet %u"
Name=Testnet mode




# Discussion History
## plowsof | 2022-12-18T00:12:35+00:00
you've enabled the Dotfiles feature correct?

*edit - i'm creating a tails bootable usb to verify 

*edit - after following the guide step by step (ensuring to enable dot files) i see Applications -> Monero GUI. Works perfectly.

Only things ive noticed are the guide links to an older version of the GUI and could benefit from updating the link to v18.1.2 / hash. 

## ghost | 2022-12-18T03:12:56+00:00
@plowsof
yes, I have enabled dotfiles on the persistent volume storage. Aswell as verified the GPG signature of the donwload Monero-GUI **v18.1.2**.

>*edit - after following the guide step by step (ensuring to enable dot files) i see Applications -> Monero GUI. Works perfectly.

Thats weird I have been using dotfiles for a longtime. I do have custom dconf settings being persisted as and autorun dotfile that **Disables GNOME Animations** amoung other things like:
``` # Disable All Animations in GNOME
gsettings set org.gnome.desktop.interface enable-animations "false" 
# Disable recently-used files in file manager
gsettings set org.gnome.desktop.privacy remember-recent-files "false"
```
and removing/adding different favorite sidebar apps

``` 
gsettings set org.gnome.shell favorite-apps "['tor-browser.desktop', 'tca.desktop', 'thunderbird.desktop', 'org.keepassxc.KeePassXC.desktop', 'org.kde.kleopatra.desktop', 'org.gnome.Nautilus.desktop', 'org.gnome.gedit.desktop', 'org.gnome.Screenshot.desktop']"  
```
**idk if this is the issue?** Could you tell me if the **monero-gui.desktop** has the same output besides the Exec and **Catagories=** cause I forgot I added `Finance;` before `Network;` in Catagories to see if that fixed the issue but apparently not.

# Action History
- Created by: ghost | 2022-12-17T21:29:49+00:00
