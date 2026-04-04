---
title: Unable to send txn with fastest tx prio - x41.5 fee
source_url: https://github.com/monero-project/monero-gui/issues/986
author: 1337tester
assignees: []
labels:
- resolved
created_at: '2017-12-04T12:45:28+00:00'
updated_at: '2018-03-17T22:54:16+00:00'
type: issue
status: closed
closed_at: '2018-03-17T22:54:16+00:00'
---

# Original Description
**When choosing fastest transaction priority - x41.5 fee, GUI wallet is unable to send the tx.**

Error message in log - "qrc:///pages/Transfer.qml:338: TypeError: Cannot read property 'priority' of undefined" (after I click "Send")
No warning/error message appears on the GUI level

![cannot_send_41 5x](https://user-images.githubusercontent.com/6553766/33553319-87979e96-d8f8-11e7-9a67-7eb4645f9e4e.jpg)

I was able to send the tx with other parameters (fee, privacy level, payment ID), the x41.5 fee seems to be the cause

**Additional Information:**
I am present on a remote node
Distro - Ubuntu 17.10
GUI version: v0.11.1.0-100-gd9d2050
Embedded Monero version: v0.10.3.1-1136-g9fad4008

# Discussion History
## stoffu | 2017-12-04T14:42:46+00:00
#989

## 1337tester | 2018-01-06T13:24:53+00:00
works on 
GUI version: v0.11.1.0-146-gac509ed
Embedded Monero version: v0.10.3.1-1397-ga529f0a6

Close please

## 1337tester | 2018-03-17T14:49:29+00:00
close please;)

## pazos | 2018-03-17T16:20:27+00:00
+resolved

## dEBRUYNE-1 | 2018-03-17T22:49:07+00:00
+resolved

# Action History
- Created by: 1337tester | 2017-12-04T12:45:28+00:00
- Closed at: 2018-03-17T22:54:16+00:00
