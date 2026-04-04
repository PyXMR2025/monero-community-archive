---
title: Check if updates are available
source_url: https://github.com/monero-project/monero-gui/issues/2089
author: sanderfoobar
assignees: []
labels:
- resolved
created_at: '2019-04-16T14:52:39+00:00'
updated_at: '2020-01-17T08:19:04+00:00'
type: issue
status: closed
closed_at: '2020-01-16T02:36:46+00:00'
---

# Original Description
GUI has functionality to check if a newer version of the GUI is available, via DNS. I believe this was disabled some time ago. We should get this functionality working. 

This also has overlap with a yet-to-be-made issue about redesigning all popups/modals.

# Discussion History
## ghost | 2019-04-19T11:42:41+00:00
Wasn’t this deemed a security risk? Big + on UX but

<sub>Sent with <a href="http://githawk.com">GitHawk</a></sub>

## erciccione | 2019-04-19T13:16:15+00:00
> Wasn’t this deemed a security risk? Big + on UX but

Yes, but AFAIK the CLI check for updates, it just doesn't install them. I think something like that could be done for the GUI as well.

## sanderfoobar | 2019-04-21T15:28:57+00:00
Update mechanism leverages DNS to fetch latest version but not auto-download.

## GBKS | 2019-05-25T07:11:27+00:00
Here's a design for this modal, just in case you'd like to have one. Would it be possible to add a link to a summary of what's new in the update?

![monero-new-version-gbks-190525](https://user-images.githubusercontent.com/695901/58366052-fb890580-7ecc-11e9-8db5-e756218143d4.png)

## selsta | 2020-01-16T02:28:59+00:00
@GBKS Can you upload the modal to Zeplin? Looks good.

> We should get this functionality working.

Working again.

+resolved

## GBKS | 2020-01-16T08:44:25+00:00
Sorry, I don't believe I ever uploaded this to Zeplin. I recently moved my design files to Figma, which should allow you to directly inspect the designs from there. If you still want to work with this design, here's the [link to Figma](https://www.figma.com/file/DplJ2DDQfIKiuRvolHX2hN/Monero-GUI?node-id=0%3A41). Let me know if that works for you.

## selsta | 2020-01-16T17:58:46+00:00
Does Figma show the exact measurements like Zeplin does?

## GBKS | 2020-01-16T21:50:28+00:00
Yep, works almost the same way. You can click, hover and command-hover things to see all kinds of spacing. There's also a code panel on the right to see font sizes and other values. But I'm sure there are some small details that are different, let me know if anything is a big issue for you.

## selsta | 2020-01-16T23:11:39+00:00
I had to signup to see all the details, nice, looks like a good Zeplin alternative. I wonder if we should add the link to the README.

## GBKS | 2020-01-17T08:18:11+00:00
We can definitely do that. I published this Figma file as a community file that I can regularly push updates to and people can freely duplicate. If you want to add a link, here's the one to the [public file](https://www.figma.com/c/file/775423808468574409). I'm also planning to update my Github repo where I had the Sketch files to point to Figma. Just seems a little better suited for open-source design collaboration.

## selsta | 2020-01-17T08:19:04+00:00
@GBKS I opened #2726 for it :)

# Action History
- Created by: sanderfoobar | 2019-04-16T14:52:39+00:00
- Closed at: 2020-01-16T02:36:46+00:00
