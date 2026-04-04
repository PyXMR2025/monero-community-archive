---
title: GUI can't read user profile located in OneDrive folders (Windows 11)
source_url: https://github.com/monero-project/monero-gui/issues/3762
author: GenericNormie
assignees: []
labels: []
created_at: '2021-11-30T19:23:23+00:00'
updated_at: '2021-11-30T19:24:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero GUI gives me a "Welcome" screen with language/mode selection instead of just asking for the password every time I launch it. 
The main suspect is OneDrive which creates new paths for some default folders and Monero GUI simply can't read .keys file which is being installed there by default. My OS is Windows 11 Home, build 22000.348. 

Steps to reproduce (I did a clean installation of Windows 11): 
- create Windows 11 Installation Media from here https://www.microsoft.com/en-us/software-download/windows11  (I used a simple 8Gb USB drive);
- on the finishing stage of the installation when you set up things like "connect to your MS profile" etc. there will be a screen "Back up your files with OneDrive". Click "Back up my files with OneDrive";
- install Monero GUI, select "advanced mode", recover wallet with seed, finish setting up a profile by creating a password and connecting GUI to your blockchain folder; 
- wait for sync (or don't, idk); 

And that's it. You will get a "Welcome" screen every time you launch a wallet because the path to Monero folder with your profile is not C:\Users\username\Documents   but  C:\Users\username\OneDrive\Documents. 
OneDrive creates a new path for a bunch of default folders like Desktop, Pictures, Apps, etc. 
I resolved it by moving Monero folder with my profile and .keys to my blockchain folder on another HDD.
Uninstalling OneDrive didn't help because nothing changed regarding folders.

Disclaimer: I'm not sure if this issue is a thing on W10 because I didn't have OneDrive installed on it.

# Discussion History
# Action History
- Created by: GenericNormie | 2021-11-30T19:23:23+00:00
