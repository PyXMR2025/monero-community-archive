---
title: '[Feature Request] Uri scheme for Monero Core'
source_url: https://github.com/monero-project/monero-gui/issues/760
author: serhack
assignees: []
labels:
- feature
created_at: '2017-06-06T13:24:02+00:00'
updated_at: '2019-04-30T20:20:17+00:00'
type: issue
status: closed
closed_at: '2019-04-30T20:20:17+00:00'
---

# Original Description
Hello,
I'm developing integrations for Monero. I think I can include in checkout page a button that open monero-gui with address-field precompiled. This should a good idea, then the client can click with a button :)
For this, we need uri scheme support.
I can provide some resources about how to develop this 
Windows : https://msdn.microsoft.com/en-us/library/aa767914(v=vs.85).aspx

# Discussion History
## amiuhle | 2017-06-07T12:42:44+00:00
`monero-wallet-rpc` already generates URIs in the form `monero:<address>?tx_amount=1`:

https://getmonero.org/knowledge-base/developer-guides/wallet-rpc#makeuri

Just pointing this out as it might help you with your integrations, it'll still have to be implemented in GUI clients, of course.

## serhack | 2017-06-10T12:06:39+00:00
@amiuhle Sorry for lately answer. Thanks for resource! 

## dEBRUYNE-1 | 2017-08-09T13:22:13+00:00
+feature

## pazos | 2018-04-25T14:53:51+00:00
I'm working on this and think it is easy to implement for osx/ios, because it is just add a string to Info.plist and the computer will register the application itself. For linux seems easy doable too but we need a desktop file to be able to use xdg-open (MimeType=x-scheme-handler/monero;)

When I have some time to wrap the code together and tested on mac/linux I'll ping you @serhack to find a way to do it without messing too much with m$ registry

# Action History
- Created by: serhack | 2017-06-06T13:24:02+00:00
- Closed at: 2019-04-30T20:20:17+00:00
