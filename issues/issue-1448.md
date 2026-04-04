---
title: MGs json broken in ringct
source_url: https://github.com/monero-project/monero/issues/1448
author: moneroexamples
assignees: []
labels: []
created_at: '2016-12-14T01:27:17+00:00'
updated_at: '2017-02-13T07:14:07+00:00'
type: issue
status: closed
closed_at: '2016-12-15T15:57:49+00:00'
---

# Original Description
```json
    "MGs": [ {
        "ss": [ [ "fb90b21624c8cadaad85a517b0d5bee92f4cc3e2c44ed464e6bf7770f830e502", "e992b731280092c207fcbe8d168565af0671c9e2be802dada5c6af1ca4e6490b"], [ "9dcfb0e033230069bdc88e4b5b9c9a7779efd929eaccb1b7290107054be39c05", "1b4ec23eeb606145d8e031554fd056a2d3e4ebe5aa69fbac379c2a099da6640b"], [ "f7f98c9f91f0e55404b689e0826e33d4d4bfa33d3464cc4946c07f8283ac9502", "1f9efe9d19fa44ddb442db8dfee4fe07cb71d3081d15719d86eeab7175f61b0a"], [ "708088d68772859e71830fef14976fe72be40df4c696466931a5635690c8160c", "ffa70c367fd282a96b72d4370abc1c3f48a59142b618dffd1dbad7d208332200"], [ "8b5e11baa7672a22ca0db3245b4fda79d3711e036428669fdbc5edbbb37a3807", "9ab07d970d2817e10053327f389971b36ab14bcafb66d28191d1bc1cf9111604"]], 
        "cc": "72372efb964ab4c0cae0800953e34ea9f46f70f1c50d7710e4d8d9bcbe80190b", 
      }{
        "ss": [ [ "ff6dc943d53d3a74d05bdc0c46f1f04231b70594e89365b72e442dc017e3f00e", "a63fcdf5a61eee003ae5c392cf97c6d28c368772d6c423e4d7f21ebbe2123604"], [ "e91f04c23ba9aa1c8f4c434e59c23f3456e1da676c06ace70a9fa463e35b5700", "b3e3442ab3e46e38e88dfb9c28f82a812432b82c7c2ad9b2547aa00516093d0e"], [ "f37e3506c0042bc3cc7cfae604b77c2badee0ad50eb8bde74bb4b80ef3cddd03", "4bb9c5261cfe33a5ea0abcfad95f22ff56502bcc90b7d6de32febe0165fe220d"], [ "7906c9eb3b6aaab6ee6d2cfb297065486d101b684a14c0adaaf093714176bc0d", "6235cc89181f82ded88f2ea4d00ff452de7082866c1001374c2e5820b76f9309"], [ "ffae141920f6443e6175b2f112e355a4803b6217579562341c07b0b18dc9610d", "051aeea8aa5fa6367df7120051fd71c95197e582966624618f511608625d5e0e"]], 
        "cc": "1d54733bdd58ffe8d6f415f035622b9b95e0c3dbd99d6401bc361aa15c9b8e07"
      }]
```

Notice missing comma in `}{`. This breaks json parsers.

# Discussion History
## luigi1111 | 2016-12-15T15:57:48+00:00
Fixed in #1449 

# Action History
- Created by: moneroexamples | 2016-12-14T01:27:17+00:00
- Closed at: 2016-12-15T15:57:49+00:00
