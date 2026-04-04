---
title: 'Vulnerability Report (2) : Weak Ciphers Enabled'
source_url: https://github.com/monero-project/meta/issues/335
author: raza5402
assignees: []
labels: []
created_at: '2019-04-27T11:23:35+00:00'
updated_at: '2019-06-29T12:02:36+00:00'
type: issue
status: closed
closed_at: '2019-04-27T15:20:56+00:00'
---

# Original Description
Hi team,

This time i founded this vulnerability in your website : https://ww.getmonero.org
![weak cipers github](https://user-images.githubusercontent.com/49895674/56849034-32570600-68a4-11e9-92e1-5df69cb6f265.png)

Vulnerability Details:-

I detected that weak ciphers are enabled during secure communication (SSL).
You should allow only strong ciphers on your web server to protect secure communication with your visitors.

Impact:

Attackers might decry-pt SSL traffic between your server and your visitors.

POC link : https://www.ssllabs.com/ssltest/analyze.html?d=ww.getmonero.org&s=104.24.27.115&latest


Remedy:

Configure your web server to disallow using weak ciphers. 

I hope that you will fix this issue as soon as possible. Looking forward to hearing from you. Thank you

Sincerely,
Ali Raza

# Discussion History
## fluffypony | 2019-04-27T15:20:56+00:00
No.

## raza5402 | 2019-04-27T15:27:22+00:00
Now why you rejected this please let me know

## raza5402 | 2019-06-29T12:02:36+00:00
HI team,
please update me

On Sat, 27 Apr 2019 at 20:20, Riccardo Spagni <notifications@github.com>
wrote:

> No.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/meta/issues/335#issuecomment-487294643>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AL4VR6Q4WIIHFT2U3FE666DPSRVNXANCNFSM4HI4AKXQ>
> .
>


# Action History
- Created by: raza5402 | 2019-04-27T11:23:35+00:00
- Closed at: 2019-04-27T15:20:56+00:00
