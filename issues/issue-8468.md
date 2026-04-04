---
title: RockPr64 - Armbian build error
source_url: https://github.com/monero-project/monero/issues/8468
author: dawiepoolman
assignees: []
labels: []
created_at: '2022-07-27T10:01:22+00:00'
updated_at: '2022-07-27T12:19:38+00:00'
type: issue
status: closed
closed_at: '2022-07-27T11:43:47+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/2351212/181220162-dbe993be-3c4f-4c02-894b-89b07959bd37.png)

specs:
![image](https://user-images.githubusercontent.com/2351212/181220304-5a0443bf-2d82-4147-ae45-d1162ee9a8bc.png)

where could I have missed something?

# Discussion History
## dawiepoolman | 2022-07-27T10:04:33+00:00
![image](https://user-images.githubusercontent.com/2351212/181221075-8e8cda82-1f51-4115-a59d-bb530b410833.png)


## dawiepoolman | 2022-07-27T11:14:32+00:00
seems like a rebuild went though.
I will test stability and revert..

## dawiepoolman | 2022-07-27T11:23:38+00:00
nope, 
folder build/release/bin is missing:
![image](https://user-images.githubusercontent.com/2351212/181235299-bd34b97f-a677-4cb8-a645-fae86d51a73f.png)


## hyc | 2022-07-27T11:43:47+00:00
Go into the Linux directory. The default build paths have the OS added to them now.

Most likely you ran out of memory during the first build; if you had used a larger swap it probably would have succeeded. No bug here.

## dawiepoolman | 2022-07-27T12:19:37+00:00
confirmed:
![image](https://user-images.githubusercontent.com/2351212/181245094-ee4275bb-4129-408c-bcd9-d4fd5ceb3da6.png)

Thanks @hyc !

# Action History
- Created by: dawiepoolman | 2022-07-27T10:01:22+00:00
- Closed at: 2022-07-27T11:43:47+00:00
