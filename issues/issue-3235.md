---
title: Why is 0.17.1.4 being hidden by the github API?
source_url: https://github.com/monero-project/monero-gui/issues/3235
author: luckman212
assignees: []
labels: []
created_at: '2020-11-14T19:35:15+00:00'
updated_at: '2020-11-18T10:09:21+00:00'
type: issue
status: closed
closed_at: '2020-11-15T20:38:22+00:00'
---

# Original Description
I am always extra careful with releases of crypto-apps, so I verify GPG hashes and things like that. Anything out of place triggers a red flag for me, which is why I'm asking...

```bash
$ curl -s -o- https://api.github.com/repos/monero-project/monero-gui/releases | jq -r '.[0].tag_name'
v0.17.1.3
```
Yet, there's clearly a non-beta 0.17.1.**4** release shown here: 
https://github.com/monero-project/monero-gui/releases/latest

Anyone know the reason?

# Discussion History
## xiphon | 2020-11-15T20:38:22+00:00
> Why is 0.17.1.4 being hidden by the github API? 

It is not.
```
$ curl -s -o- https://api.github.com/repos/monero-project/monero-gui/releases | jq -r '.[1].tag_name'
v0.17.1.4
```

## luckman212 | 2020-11-17T20:03:05+00:00
Strange, in all other repos I interact with, the first array element `[0]` returned by the API is always the latest release. This one seems inverted... 

## xiphon | 2020-11-18T10:09:21+00:00
You should have used `https://api.github.com/repos/monero-project/monero-gui/releases/latest` endpoint.

```
$ curl -s -o- https://api.github.com/repos/monero-project/monero-gui/releases/latest | jq -r '.tag_name'
v0.17.1.4
```

# Action History
- Created by: luckman212 | 2020-11-14T19:35:15+00:00
- Closed at: 2020-11-15T20:38:22+00:00
