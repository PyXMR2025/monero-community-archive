---
title: '[WIP] Restyle wizards to black-theme'
source_url: https://github.com/monero-project/monero-gui/issues/1513
author: sanderfoobar
assignees: []
labels: []
created_at: '2018-07-17T13:59:42+00:00'
updated_at: '2019-04-10T19:50:41+00:00'
type: issue
status: closed
closed_at: '2019-04-10T19:50:41+00:00'
---

# Original Description
As the title says.

Fixes #746

+enhancement

#### ideas/to-do's

```
< knueffelbund> Is it possible to pick up the language from the OS setting?
< knueffelbund> Just as a default, but it could help some people avoid using this super long  menu.
```

# Discussion History
## sanderfoobar | 2018-07-22T00:51:09+00:00
Language selection screen:

![](https://i.imgur.com/9LJJU3Z.png)
![](https://i.imgur.com/jtg2DU9.png)

The globe rotates slowly. The menu is triggered by pressing 'Languages'.

## ghost | 2018-07-25T06:12:39+00:00
Very nice!

## sanderfoobar | 2018-08-05T21:37:20+00:00
Home screen:

![](https://i.imgur.com/7QXQ14c.png)

## GBKS | 2018-08-06T09:42:37+00:00
![monero-onboarding-type-icons-180806-2](https://user-images.githubusercontent.com/695901/43709387-f9200384-996c-11e8-9981-5d981dee87de.png)

Here's my current exploration for these icons. I'm talking to rehrar and tficharmers about some details (mostly color related), and also running it past some other designers I know to get an outside perspective. All feedback appreciated, as always.

## Leza89 | 2018-10-27T03:15:05+00:00
@ GBKS I like the `Create a new wallet` symbol you came with up since it's more descriptive of the action 
 but I prefer the old style in general tbh.

## GBKS | 2018-10-27T20:58:59+00:00
@Leza89 thanks for the feedback. What do you like better about the old style?

## Leza89 | 2018-10-27T21:15:17+00:00
It doesn't look "modernized" - in general I don't like the new simplified designs. i.e.:

http://d5vf6134d8ffdnfp1qv4rv3l.wpengine.netdna-cdn.com/wp-content/uploads/04a-windows-os-logos.jpg

In chronological order:
1985: Ohgodwhy
1992-1994: too simple and flat
1995-2000: ok-ish
2001-2005: good
2006-2008: nice
2009-2012: nice
current: too simple and flat
(next: Ohgodwhy? ^^)

I guess I don't like the lack of a third color within the icon's borders and the mnemonic seed symbol looks quite similar to ledger and usb sticks. What's that supposed to represent?

Edit: And probably the introduction of a secondary main color

* old: orange; Most active buttons are white or orange, outline is orange, whilst I consider white to be neutral

* your design: orange and blue (and white).. Button outline is white so rather neutral; The descriptive element of the button is an intense blue. When I think of it this is probably the biggest reason - Take your design, invert the colors and tell me what feels more compelling for you:

https://img.picload.org/image/dcacdrww/untitled.png

## bitlamas | 2019-01-09T16:53:25+00:00
I like the language selection screen, but I believe the languages should be shown in alphabetic order.
The home screen looks nice, from the two images shared in the issue I prefer the _first one_. I have a couple things to say about both, but first things first: how are these designs going to work with the discussion ongoing on #1846? If we're going to have a screen between the `Language selection` and the `Setup your wallet` then it would also be nice to have a proposal for this new screen.

Design from @xmrdsc 
I think we could use different icons for `Create a new wallet`. A light bulb always comes up to me as "idea" instead of calling to the action of creation; I personally prefer the plus icon from the second design. Another one that could use a different icon is `Open a wallet from file`, I think it's too similar to the hardware wallet icon. File is usually represented by a _folder_ or a floppy disk. Maybe something like [this](https://image.flaticon.com/icons/svg/148/148957.svg), but with the Monero logo stamp on the paper.
I also think the `Language selection` button on the welcome screen could be bigger, more similar to like what is in the second design.

Design from @GBKS 
The icon for `Restore from keys or mnemonic` really makes me think about [LastPass button](http://blog.ryansjohnson.com/wp-content/uploads/2018/01/lastpass.png). The colors would probably have to be worked on as well, but you already mentioned that yourself so it's good. Same as the first design, I think `Open a wallet from file` should be something other than the USB stick.
I like `Previous / Next` buttons at the end although there's not really a "next" since the user has to click in one of the icons to actually proceed. I think the `Previous` button could also show the title of the previous screen (e.g. `Previous: Select wallet mode`)

## GBKS | 2019-01-14T08:37:44+00:00
[Here's an updated design](https://www.dropbox.com/s/9658ioljjvjhh6d/monero-onboarding-how-to-set-up-gbks-191114.png?dl=0) based on the Reddit and IRC discussions. It uses the new icons in orange as requested, with an updated "Restore from file" icon (folder vs. USB stick).

However, I made them smaller and changed the layout from the horizontal list with big icons, to a vertical list with smaller icons and more text (a layout we already use for node selection). Having more text vs. just a short label makes it easier to explain what each options means, which will hopefully reduce confusion (text in the design is not final, I'd need help getting that perfect).

What do you think?

## sanderfoobar | 2019-01-14T09:28:10+00:00
@GBKS I like it!

Up on zeplin?

## GBKS | 2019-01-14T13:04:18+00:00
@xmrdsc it is now - [see here](https://zpl.io/25qP4jo). Icons should be exportable in 1x (60x60px) and 2x (120x120px).

One more note that I did not adjust the saturation. Since the icons are smaller than in the previous layout, they are visually not as overwhelming. But let me know if there are still any other changes you'd like to see.

## sanderfoobar | 2019-01-18T12:13:11+00:00
Cheers. See #1909 for PR. 

# Action History
- Created by: sanderfoobar | 2018-07-17T13:59:42+00:00
- Closed at: 2019-04-10T19:50:41+00:00
