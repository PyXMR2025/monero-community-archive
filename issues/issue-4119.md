---
title: SELinux 'has detected a problem' on RHEL 9.1 / Rocky / AlmaLinux
source_url: https://github.com/monero-project/monero-gui/issues/4119
author: David-Else
assignees: []
labels: []
created_at: '2023-02-16T11:20:40+00:00'
updated_at: '2023-02-16T17:22:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have tried the downloading 0.18.1.2 from the main site, and the flatpak from flathub, exact same problem. As soon as it launches i get spammed with flickering never ending SELinux errors, they all look like this:

![Screenshot from 2023-02-16 11-10-42](https://user-images.githubusercontent.com/12832280/219350544-cb1fc11b-1dce-4281-b096-c7ec0a2df4ef.png)

It makes the app unusable, hope it can be fixed, could anyone explain what it is trying to tell me? Thanks!


# Discussion History
## selsta | 2023-02-16T16:28:45+00:00
Please see https://bugzilla.redhat.com/show_bug.cgi?id=2058657#c11

```
setsebool -P selinuxuser_execmod 1
```

Qt uses JIT which gets blocked by SELinux, as far as I can tell there isn't anything we can do on our side.

## David-Else | 2023-02-16T17:08:48+00:00
@selsta Thanks for the feedback! I assume `setsebool -P selinuxuser_execmod 1` is a universal setting, can it be made specific to only monero-gui?

## selsta | 2023-02-16T17:22:04+00:00
I'm unfortunately not familiar with SELinux.

# Action History
- Created by: David-Else | 2023-02-16T11:20:40+00:00
