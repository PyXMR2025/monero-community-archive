---
title: 'Feature request : Ship a genuine AppImage in the download'
source_url: https://github.com/monero-project/monero-gui/issues/3703
author: cassepipe
assignees: []
labels: []
created_at: '2021-09-17T08:05:15+00:00'
updated_at: '2021-09-30T14:02:23+00:00'
type: issue
status: closed
closed_at: '2021-09-18T13:47:46+00:00'
---

# Original Description
It's all in the title. The current AppImage you find in the Linux download folder is just a hack to start the executable from a graphical session apparently.
Would you be willing to ship a genuine AppImage?

Thanks for all the great work 

# Discussion History
## selsta | 2021-09-17T13:22:19+00:00
What would be the advantages?

## cassepipe | 2021-09-17T13:48:15+00:00
Linux desktop integration made possible with tools like AppImageLauncher
(Then we don't have a `monero-gui-vxxxx` directory hanging out on the desktop or in the home directory)

## selsta | 2021-09-17T13:51:35+00:00
Did you install the desktop entry on first start? https://wiki.archlinux.org/title/desktop_entries

## cassepipe | 2021-09-17T16:16:29+00:00
No I did not., thanks for pointing out to documentation. 

AppImages and Flatpak are becoming more and more common to distribute software on Linux especially when the software needs to be kept up to date. I thought it would be a worthwhile addition.
Especially as there no other way to know that the AppImage is not a standard AppImage without searching into the repo issues
which is confusing for non advanced Linux users.

Now if you tell me there no willingness for that to happen or that is poses technical issues, I'll just close this.

## selsta | 2021-09-17T16:19:31+00:00
FWIW I think Monero GUI is available as a Flatpak. Is that good enough?

## cassepipe | 2021-09-18T13:47:46+00:00
I did not know that. There wasn't any last time I checked. 
I looked it's only two months old and there is no mention of it neither on getmonero.org nor the Github's Readme 
(Can I trust it then ?)

It is not for me to judge if that's good enough or not, I am just making humble suggestions.
Thanks for your replies.

NB : You asked what are the advantages of Appimages, I think it is better worded [there](https://docs.appimage.org/introduction/advantages.html#advantages-for-application-authors ). (Now if you actually meant advantages *over* flatpaks I have no idea)

## q7nm | 2021-09-30T14:01:57+00:00
> I did not know that. There wasn't any last time I checked. I looked it's only two months old and there is no mention of it neither on getmonero.org nor the Github's Readme (Can I trust it then ?)


Hi. You can look at the manifest of org.getmonero.Monero and make sure that there are no bad functions inside.


# Action History
- Created by: cassepipe | 2021-09-17T08:05:15+00:00
- Closed at: 2021-09-18T13:47:46+00:00
