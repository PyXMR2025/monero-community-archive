---
title: 'Feature Request: ''list_key_images'' simplewallet JSON RPC method'
source_url: https://github.com/monero-project/monero/issues/694
author: bigreddmachine
assignees: []
labels: []
created_at: '2016-03-02T19:33:26+00:00'
updated_at: '2016-09-25T19:47:16+00:00'
type: issue
status: closed
closed_at: '2016-09-25T19:47:16+00:00'
---

# Original Description
It would be advantageous to have a rpc method for simplewallet that allowed your to issue a command and receive key images for all transaction outputs in your wallet. In the hypothetical case of giving an auditor access to your wallet, you could then give him/her your wallet's view key and the list of key images, allowing the auditor to verify payments that were sent and XMR still in your account.


# Discussion History
## moneromooo-monero | 2016-09-24T16:44:44+00:00
There is a export_key-images and import_key_images command pair now. Do you see a possible use for having them as JSON ? Currently, they export a file with signed key images, which can be used for the auditor case you mention.


## bigreddmachine | 2016-09-25T19:47:16+00:00
Am I right that `export_key_images` and `import_key_images` are both `json_rpc` commands, just that they export/import a file rather than the keys as a json-formatted response?

If that's the case, I think the way you have it is perfect. I don't see a reason to have it respond with the keys in JSON format, or import keys from JSON format, since the whole goal is to export the keys in a way that can easily be shared with someone else. Someone might come up with a specific reason to have then in JSON, but then it's as simple as reading the file and generating a JSON.

I'm going to close this issue. Thanks for your work!


# Action History
- Created by: bigreddmachine | 2016-03-02T19:33:26+00:00
- Closed at: 2016-09-25T19:47:16+00:00
