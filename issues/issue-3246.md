---
title: Can't export key images - always 164 bytes output file
source_url: https://github.com/monero-project/monero-gui/issues/3246
author: KarboDuck
assignees: []
labels: []
created_at: '2020-11-25T08:47:24+00:00'
updated_at: '2021-02-16T02:42:46+00:00'
type: issue
status: closed
closed_at: '2021-02-16T02:42:46+00:00'
---

# Original Description
I'm trying to export key images. But I always get a file with size just of 164 bytes.

Tried that using three different wallet files with some balance on them on:
- Laptop #1: Ubuntu 20.10, gui wallet 0.17.1.4
- Laptop #2: Windows 10, gui wallet 0.17.1.4

As mentioned [here](https://github.com/monero-project/monero/issues/7042) "wallet just exports what it's not exported before", and in CLI workaround is to add "all" and use `export_key_images all somefilename `.

In GUI it seems like it's impossible to export key images from scratch.

# Discussion History
## selsta | 2020-11-25T08:48:22+00:00
Would you prefer if the GUI always exports all key images?

## KarboDuck | 2020-11-25T08:53:27+00:00
I'm not sure how it should work. My problem is, I'm trying to "communicate" cold and hot wallet. And because my hot wallet is phisically a new file, I can't update it because cold wallet thinks it's already gave me key images in the past and I have no way to have them again (in the gui).

Sorry if I'm confused how it's all works.

## jonathancross | 2020-12-07T19:21:04+00:00
> Would you prefer if the GUI always exports all key images?

I think this would be preferable.  It may make a larger file, but avoids many situations that might confuse users.

# Action History
- Created by: KarboDuck | 2020-11-25T08:47:24+00:00
- Closed at: 2021-02-16T02:42:46+00:00
