---
title: Privacy policy doesn't exist
source_url: https://github.com/monero-project/monero-site/issues/606
author: wgx
assignees: []
labels: []
created_at: '2018-02-18T13:35:13+00:00'
updated_at: '2020-04-07T09:36:27+00:00'
type: issue
status: closed
closed_at: '2020-04-07T09:36:27+00:00'
---

# Original Description
The link to privacy policy on the legal page doesn't go anywhere. As the beginning of GDPR looms, would be good to get the Monero privacy policy sorted. 👍 

# Discussion History
## mattcode55 | 2018-02-18T17:34:42+00:00
The privacy policy is at the bottom of the [legal page](https://getmonero.org/legal/). The old pages were removed a while ago https://github.com/monero-project/monero-site/pull/455#issuecomment-339360972.

Where did you find a link to one of the old pages?

## wgx | 2018-02-18T18:08:45+00:00
@mattcode55 The legal page doesn't have a privacy policy on it, it instead has a paragraph which links to a non-existent page (with an #anchor). Please go and look: https://getmonero.org/legal/

## rehrar | 2018-02-18T18:17:32+00:00
Yes, it does not link to a different page, it links to a different part of the same page. Scroll the bottom of the Legal page and you will see a Copyright segment and a Privacy Policy segment after the long Terms of Service section. 

Everything is as it should be. 

## SamsungGalaxyPlayer | 2018-02-18T18:22:35+00:00
@rehrar with the current version of the site, I only see the copyright section. Not the privacy policy section.

![capture](https://user-images.githubusercontent.com/12520755/36355274-5ff4d59a-14a6-11e8-9758-0135b06331c8.PNG)

## rehrar | 2018-02-18T18:23:56+00:00
Check on mobile? Checking desktop. 

## SamsungGalaxyPlayer | 2018-02-18T18:26:16+00:00
@rehrar yes, I see it on mobile right now.

## rehrar | 2018-02-18T18:27:06+00:00
Will fix. 

## mattcode55 | 2018-02-18T18:27:24+00:00
I can see it on desktop just fine ![Screenshot](http://www.enlightenment.org/ss/e-5a89c56abe74c0.27184876.jpg)

## SamsungGalaxyPlayer | 2018-02-18T18:28:33+00:00
@mattcode55 weird, I reset my cache right before viewing it :/

## rehrar | 2018-02-18T18:29:30+00:00
It's too private for some to be able to see. 

## mattcode55 | 2018-02-18T18:30:14+00:00
[I just archived the site on archive.is and I can see it there](http://archive.is/aUBrq) so it isn't a caching thing, it also is there when I use my phone. Very spooky.

## rehrar | 2018-02-19T21:14:31+00:00
After a good amount of testing, I simply cannot reproduce the Privacy Policy not appearing. @wgx can you share your OS and browser? Try on another computer as well. Still the same problem? Mobile?

## wgx | 2018-02-20T09:45:23+00:00
Firefox 58, MacOS 10.13

<img width="1128" alt="screen shot 2018-02-20 at 09 44 43" src="https://user-images.githubusercontent.com/930099/36417041-c293ecd6-1622-11e8-8dd6-e9436a2706b9.png">


## wgx | 2018-02-20T09:46:07+00:00
@rehrar if I view source, I can see the policy is in the markup but a CSS rule is likely preventing it being shown for some reason. 

## erciccione | 2018-06-25T10:22:39+00:00
Is this issue still relevant?

## wgx | 2018-06-25T12:45:42+00:00
Still not fixed for me - no privacy policy visible in firefox

## erciccione | 2018-06-25T12:51:31+00:00
I can see it properly on Linux with Firefox 60.0.2 64-bit. Anybody else able to test this on MacOS?

## erciccione | 2020-04-07T09:36:27+00:00
This issue is old and was discussed and closed on gitlab. Please reopen if you feel it's still relevant.

# Action History
- Created by: wgx | 2018-02-18T13:35:13+00:00
- Closed at: 2020-04-07T09:36:27+00:00
