---
title: HTML injection in "Receive" tab.
source_url: https://github.com/monero-project/monero-gui/issues/1799
author: serhack
assignees: []
labels: []
created_at: '2018-12-11T18:09:07+00:00'
updated_at: '2018-12-12T19:58:42+00:00'
type: issue
status: closed
closed_at: '2018-12-12T19:58:42+00:00'
---

# Original Description
Version: Monero 0.13.0.4 GUI
Topic: Any users could inject HTML via the Receive page input fields "Set the label of new address" and "Edit the label". 

Steps to reproduce:

- Press "Create a new address" link
- Insert your HTML
- Voilà, your HTML is displayed 

In every security model I see, there's a MUST: parse any inputs from the user. I would like to apply this to Monero GUI too. It seems in some places HTML injection is not possible, but I would like to run more tests.

(However, this is not a security issue).

# Discussion History
## sanderfoobar | 2018-12-12T10:10:14+00:00
Thanks. This is due to how the `textFormat` property of QML Type `Text` defaults to `Text.AutoText` - which  according to the documentation will turn the component into RichText mode depending on the content. 

> If the text format is Text.AutoText the Text item will automatically determine whether the text should be treated as styled text.

Solution is to default them to `textFormat.PlainText` instead and override `RichText` when needed. 

`MoneroComponents.Label`, which internally uses `Text`, is used in a lot of places so Ill check them all and PR a fix.

# Action History
- Created by: serhack | 2018-12-11T18:09:07+00:00
- Closed at: 2018-12-12T19:58:42+00:00
