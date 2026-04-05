---
title: I can't mine more than 1 time with xmrig
source_url: https://github.com/xmrig/xmrig/issues/2539
author: Cris7015
assignees: []
labels:
- question
created_at: '2021-08-14T01:39:39+00:00'
updated_at: '2022-04-03T14:39:00+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:39:00+00:00'
---

# Original Description
Hello I need help and I have tried to mine with xmrig and minexmr I already have 1 machine running that is mining but at the moment I want to mine with another machine the program starts without problems but it does not register the 2 machines but only 1 that may be I need help I would appreciate it
![Captura de pantalla (464)_LI](https://user-images.githubusercontent.com/76759272/129430662-2b4f96c8-6e4a-4221-ace3-9337ed9e1b92.jpg)
![Screenshot (9)](https://user-images.githubusercontent.com/76759272/129430667-6b0fa72a-b0dd-4594-8a70-38c1004abbb7.png)
The second image that I sample is the second machine that doesn't want to appear on minexmr's mining list, I don't really know if it's their problem, mine, or yours.

# Discussion History
## freakovision | 2021-08-14T10:43:18+00:00
They are mining under the same name. 
Use different rig-id for each worker.
`--rig-id=ID` - ` rig identifier for pool-side statistics`


## Cris7015 | 2021-08-27T18:26:52+00:00
where can i get a rig-id or can it be anyone?

## Cris7015 | 2021-08-27T18:35:47+00:00
Hello I already discovered the error in the user I had to add a. and at that point a name;)

## Spudz76 | 2021-08-27T20:47:16+00:00
Yes some pools take rig-id within the password, when they don't support rig-id itself.

And you just make them up, unique to yourself.

# Action History
- Created by: Cris7015 | 2021-08-14T01:39:39+00:00
- Closed at: 2022-04-03T14:39:00+00:00
