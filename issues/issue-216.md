---
title: 'OSX: Don''t quit whole app'
source_url: https://github.com/monero-project/monero-gui/issues/216
author: sammy007
assignees: []
labels:
- wontfix
created_at: '2016-11-26T17:04:39+00:00'
updated_at: '2019-07-16T17:45:49+00:00'
type: issue
status: closed
closed_at: '2019-07-16T17:45:49+00:00'
---

# Original Description
It's way better to not quite whole application if "x" is clicked in window decoration, just hide window, let it remain running.

# Discussion History
## Jaqueeee | 2016-11-26T17:16:52+00:00
i think most people will get confused if 'X' doesn't quit the app. It would also add a security risk if wallet stays open when user thinks it's closed. 

## sammy007 | 2016-11-26T17:17:44+00:00
Just to make it clear, `Cmd+w` has no effect and it's expected that "close" button will behave like `Cmd+w`. If you need to totally quit app you can use `Cmd+q` to make user experience unobtrusive. Dock space is limited to always `hide` app so it will consume extra space in dock.

All existing wallets behave like this, Hive, Bitcoin-Qt and so forth.

## Jaqueeee | 2016-11-26T23:47:28+00:00
I see. Those shortcuts are mac specific and that behavior is not expected on other platforms. For now the GUI works the same on all platforms but we could add platform independent stuff later on. 

## sammy007 | 2016-11-26T23:48:55+00:00
Yeah prolly with swapping decoration buttons because it's kinda looks not native.

## Jaqueeee | 2016-12-04T16:00:20+00:00
#225 replaces black top bar with native bar. But the exit button still works the same AFAICT.

## ghost | 2016-12-23T16:52:46+00:00
I just want to support this as another mac user. The x button on a mac usually closes the screen rather than the programme. We're a strange breed, but it is what we're used to. 

## jonathancross | 2017-06-06T00:53:36+00:00
> All existing wallets behave like this, Hive, Bitcoin-Qt and so forth.

FWIW: I just tested Electrum and see that clicking the red close button or using `⌘w` or `⌘q` all have the exact same effect -- completely close the application. Picasa too.  KeepassX will quit if the user clicks the close button, but `⌘w` will not hide or close the window.  They are all single-window apps like Monero.

GPG Keychain, Photoshop, act as described above by @sammy007.

Seems to me that this behavior is not all that consistent...



## rex4539 | 2018-01-02T22:05:35+00:00
Any updates on this?

Standard MacOS behavior when clicking the X button is to just close the main window.

Unless my understanding is totally off, implementing this is just connecting the action to `close()`

## selsta | 2019-07-16T17:17:10+00:00
Apps that support multiple windows have this behaviour. monero-gui does not support multiple windows so it closes when clicking on X. This is inline with the e.g. native Notes.app.

We also use Qt instead of AppKit so implementing the requested feature is difficult.

+wontfix

# Action History
- Created by: sammy007 | 2016-11-26T17:04:39+00:00
- Closed at: 2019-07-16T17:45:49+00:00
