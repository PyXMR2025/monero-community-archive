---
title: -c, --config=FILE option doesn't work
source_url: https://github.com/xmrig/xmrig/issues/46
author: vcambur
assignees: []
labels: []
created_at: '2017-07-25T23:09:49+00:00'
updated_at: '2017-08-17T14:32:15+00:00'
type: issue
status: closed
closed_at: '2017-08-17T14:32:15+00:00'
---

# Original Description
First of all thank you very much for such optimized miner
Do you plan to implement the option in subject ?


# Discussion History
## xmrig | 2017-07-25T23:19:40+00:00
In next release (2.2.0), actually I had plan to restore it in current release, but... delay it again)
Related #26
Thank you.

## xmrig | 2017-07-25T23:36:44+00:00
Config support need rewritten it not just backport from C version, for example now possibly specify multiple --url options, in JSON it need wrap to array and add new option.
Maybe something like:
```json
{
"pools": [
    {
      "url": "pool1:3333",
      "user": "user1",
      "pass": "x",
      "keepalive": true,
      "nicehash": false
    },
    {
      "url": "pool2:5555",
      "user": "user2",
      "pass": "x",
      "keepalive": true,
      "nicehash": false
    }
  ]
}
```

## vcambur | 2017-07-26T08:38:21+00:00
I see
yes this way it looks good

## xmrig | 2017-07-31T15:44:00+00:00
Example config file https://github.com/xmrig/xmrig/blob/dev/src/config.json
Can load multiple config files and combine with command line options.
If no pool specified by command line options will try load config.json from directory with executable.

## vcambur | 2017-08-01T12:48:39+00:00
Thanks, going to try from the dev branch


# Action History
- Created by: vcambur | 2017-07-25T23:09:49+00:00
- Closed at: 2017-08-17T14:32:15+00:00
