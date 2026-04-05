---
title: How to download the latest xmrig binary from github automatically
source_url: https://github.com/xmrig/xmrig/issues/3071
author: toxicroadkill
assignees: []
labels: []
created_at: '2022-06-15T00:45:46+00:00'
updated_at: '2022-06-16T21:43:12+00:00'
type: issue
status: closed
closed_at: '2022-06-16T21:43:12+00:00'
---

# Original Description
not really a issue with xmrig, but with downloading it.

i run a rather large mining farm, and have the miners setup to update the os (debian) on a weekly basis, and do a reboot

is there a way to pull the latest binary xmrig from github

in the install script it does

wget https://github.com/xmrig/xmrig/releases/download/v6.17.0/xmrig-6.17.0-linux-static-x64.tar.gz

I would just like to pull the most recent binary without having to change the filename all the time, and then incorporate this into the update script that runs weekly..

wget https://github.com/xmrig/xmrig/releases/download/linux-static-x64.tar.gz <-- something like this..specify which type of binary i want, and be able to just download the latest version without worrying about what the version number is?

is this possible with github?


# Discussion History
## Spudz76 | 2022-06-15T04:24:25+00:00
```
wget -q https://github.com/$(wget -qO- https://github.com/xmrig/xmrig/releases/latest | grep -o /xmrig/xmrig/releases/download/v.*/xmrig-.*-linux-static-x64.tar.gz)
```

## toxicroadkill | 2022-06-15T04:34:08+00:00
wow, what a great answer, never thought of doing it that way

thank you very much



> On Jun 14, 2022, at 11:24 PM, Tony Butler ***@***.***> wrote:
> 
> 
> wget -q https://github.com/$(wget -qO- https://github.com/xmrig/xmrig/releases/latest | grep -o /xmrig/xmrig/releases/download/v.*/xmrig-.*-linux-static-x64.tar.gz)
> —
> Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/3071#issuecomment-1155969596>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/ASD5O3YQA3ENME5TM5ZE2BDVPFLIHANCNFSM5YZQGSIQ>.
> You are receiving this because you authored the thread.
> 



## JacksonChen666 | 2022-06-16T20:05:59+00:00
@toxicroadkill you may close this issue now (and also rename the issue to "How to download the latest xmrig binary from github automatically" for accuracy reasons, just a suggestion)

# Action History
- Created by: toxicroadkill | 2022-06-15T00:45:46+00:00
- Closed at: 2022-06-16T21:43:12+00:00
