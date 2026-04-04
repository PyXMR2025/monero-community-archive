---
title: Last update Linux issue. Impossible to copy own monero address
source_url: https://github.com/monero-project/monero-gui/issues/3432
author: IMVIX
assignees: []
labels: []
created_at: '2021-04-23T00:20:32+00:00'
updated_at: '2021-05-04T21:03:59+00:00'
type: issue
status: closed
closed_at: '2021-05-04T21:03:45+00:00'
---

# Original Description
I use Monero on Whonix Workstation. There is bug in Monero GUI 0.17.2.1-8444a95 (Qt 5.15.2) for Linux. It's impossible to copy to clipboard the address for receive Monero.

I see only "save as image" after the last update of Monero GUI:

![2](https://user-images.githubusercontent.com/77311926/115799888-ec68a600-a3c8-11eb-9688-31b01fb44bc4.jpg)

Everything was well before this update in older versions:

![1](https://user-images.githubusercontent.com/77311926/115799992-2b96f700-a3c9-11eb-8d02-f2ea8894b6ea.jpg)

Please return this button back or explain how to copy address to clipboard without qr-code.

# Discussion History
## selsta | 2021-04-23T00:22:23+00:00
<img width="623" alt="Screenshot 2021-04-23 at 02 21 51" src="https://user-images.githubusercontent.com/7697454/115800327-ab798d00-a3da-11eb-9f93-76805e743739.png">

See the copy button in the right corner.

## IMVIX | 2021-04-23T00:31:47+00:00
Thank you. There is no visible button in my Whonix-Debian Monero GUI 0.17.2.1-8444a95 (Qt 5.15.2). It's invisible in all themes. 

![1](https://user-images.githubusercontent.com/77311926/115800913-06a38380-a3cb-11eb-939f-9ee83a6fa9f6.jpg)


## selsta | 2021-04-23T00:33:06+00:00
Did you use arch to install the GUI? Did you do start with QMLSCENE_DEVICE=softwarecontext env var?

Also try clicking in the right corner even if no button is visible.

## IMVIX | 2021-04-23T00:48:32+00:00
It was checked in two different ways. 

1) I downloaded new [Whonix XFCE](https://www.whonix.org/wiki/VirtualBox/XFCE) and updated it as usual: `sudo apt-get-update-plus dist-upgrade`

2) I updated my old Whonix with old Monero GUI 0.17.19 (second picture on the topic).

Started from the menu in both cases:

![1](https://user-images.githubusercontent.com/77311926/115801893-584d0d80-a3cd-11eb-9438-23e429cf9498.jpg)


## selsta | 2021-04-23T00:49:52+00:00
It is likely that whonix sets QMLSCENE_DEVICE=softwarecontext automatically.

Anyway, until the next version you will just have to click in the right corner, it will copy the address.

## IMVIX | 2021-04-23T00:51:24+00:00
Ok. Small button works if you click it. But this button is invisible. 

## selsta | 2021-04-23T00:52:21+00:00
> But this button is invisible.

Yes, this is because whonix sets QMLSCENE_DEVICE=softwarecontext env var. It will be fixed in the next version that should be out soon.

## selsta | 2021-05-04T21:03:45+00:00
Closing as the issue is resolved in repo, new release should be out soon.

# Action History
- Created by: IMVIX | 2021-04-23T00:20:32+00:00
- Closed at: 2021-05-04T21:03:45+00:00
