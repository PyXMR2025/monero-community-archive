---
title: getmonero.org/how-to-ccs Has strangely broken link
source_url: https://github.com/monero-project/monero-site/issues/2015
author: dginovker
assignees: []
labels: []
created_at: '2022-08-10T06:48:25+00:00'
updated_at: '2022-09-17T09:35:56+00:00'
type: issue
status: closed
closed_at: '2022-09-17T09:35:55+00:00'
---

# Original Description
If you visit https://ccs.getmonero.org/how-to-ccs/ and click the link under "[What is the CCS and What Are Its Rules and Expectations](https://ccs.getmonero.org/what-is-ccs)", you get getmonero.org on port 8080 like this:

```
https://ccs.getmonero.org:8080/what-is-ccs/
```
![image](https://user-images.githubusercontent.com/32943174/183833837-9c766da4-fbf3-427e-9267-8ced15f74f0c.png)


# Discussion History
## apertamono | 2022-08-10T20:35:22+00:00
The CCS is in a separate repository on Gitlab. [This error was reported and dismissed there](https://repo.getmonero.org/monero-project/ccs-front/-/issues/2). I think there's a slash missing at the end of the link. Might have been dismissed because it does work in the local preview there.

## plowsof | 2022-09-16T19:23:32+00:00
Thanks for raising the issue, had a quick look, it is indeed a missing slash at the end. A PR must be made to the CCS-front end repository on gitlab (not here)

https://repo.getmonero.org/monero-project/ccs-front/-/tree/master/how-to-ccs (easy fix but, my account isn't able to fork the repo)

edit* made a PR here (gitlab says +220 / -220 after adding "/" (?) https://repo.getmonero.org/monero-project/ccs-front/-/merge_requests/36

## erciccione | 2022-09-17T09:35:55+00:00
Closing this issue as it's unrelated to this repository. Please use the merge request on gitlab for further discussion.

# Action History
- Created by: dginovker | 2022-08-10T06:48:25+00:00
- Closed at: 2022-09-17T09:35:55+00:00
