---
title: 17.3.0 Rollback
source_url: https://github.com/monero-project/monero/issues/8303
author: sweeden-ttu
assignees: []
labels: []
created_at: '2022-04-29T18:27:34+00:00'
updated_at: '2022-05-01T07:12:22+00:00'
type: issue
status: closed
closed_at: '2022-04-30T07:21:52+00:00'
---

# Original Description
Has anyone even ran the test library since v17.2 ? 

I see a lot of commits to the 17.3 branch which ban transaction types and it looks like none of this has even been verified on Main_net yet.

-  missing binaries for major platforms
-  Unit tests don't run
-  multitude of messaging and onion features were added

# Discussion History
## selsta | 2022-04-29T19:48:56+00:00
We constantly run the tests, on every single commit to be exact.

## selsta | 2022-04-30T07:21:52+00:00
Here is an example of tests run on the latest PR: https://github.com/monero-project/monero/runs/6235008179

If you meant something else please reword it. Closing this in the meantime as your question was answered.

## sweeden-ttu | 2022-04-30T11:03:43+00:00
Please stop closing my issues when you have only proven that nothing works except on Ubuntu

## sweeden-ttu | 2022-04-30T11:04:09+00:00
Make build-test 

… Nothing works

## sweeden-ttu | 2022-04-30T11:04:45+00:00
> We constantly run the tests, on every single commit to be exact.

Show me one that isn't Ubuntu

## sweeden-ttu | 2022-04-30T11:06:17+00:00
Please reopen my Issue or stop commenting them on at all. 

Your comments and feedback are completely useless

## selsta | 2022-04-30T11:08:55+00:00
Please check the README: https://github.com/monero-project/monero#on-linux-and-macos

The command is called:

```
make release-test
```

## sweeden-ttu | 2022-04-30T11:16:17+00:00
That's what I just said.

It doesn't work .

you're clearly trying to do 50% ruin takeover of monero.  Where enough idiots, at least 50% adopt an a New version that doesn't work when the  current version already worked ... and it wasn't needed 

## sweeden-ttu | 2022-04-30T11:18:05+00:00
17.2 works Just fine I've traded plenty of monero and products online  for several.   

 there's no reason to upgrade to 17.3 As far as I can tell nothing works

## selsta | 2022-04-30T11:18:48+00:00
No, you said `make build-test`, that's two different commands. Try to read properly.

## sweeden-ttu | 2022-04-30T11:21:18+00:00
make Is a command 

try putting a command line in a command line once in your life

## selsta | 2022-04-30T11:22:35+00:00
`build-test` and `release-test` are two different targets. I would suggest reading this if you don't know what make targets are: https://stackoverflow.com/questions/2270643/what-is-a-make-target

## sweeden-ttu | 2022-04-30T11:25:24+00:00
Return the first principle

TEST

## sweeden-ttu | 2022-04-30T11:25:39+00:00
OK I think it's clear you are paid by the government organization at this point to ruin monero

## sanderfoobar | 2022-04-30T11:39:04+00:00
- this issue has the nonsensical title "17.3.0 Rollback" ... When posting issues, you ought to keep them relevant to the actual issue
- the actual issue does not specify a *specific problem* that needs to be discussed or solved, instead you listed 3 random statements
- you are being rude to a valuable community member

So, if you want *something* fixed, learn how to articulate your problem into something that is comprehensible and post a new github issue.

## plowsof | 2022-04-30T12:32:26+00:00
> OK I think it's clear you are paid by the government organization at this point to ruin monero

If by 'government organization' you mean 'Community Crowdfunding System' then yes, you are correct. see (note the number 5): https://ccs.getmonero.org/proposals/selsta-5.html



## jeffro256 | 2022-04-30T16:38:39+00:00
@web-sharp To run the tests, do `cd build/<OS>/<branch>/release/tests/ && make test`

## sweeden-ttu | 2022-04-30T23:15:03+00:00
![image](https://user-images.githubusercontent.com/63826817/166125619-6c2c87d9-8ac5-4602-b369-245c48dab92b.jpeg)![image](https://user-images.githubusercontent.com/63826817/166125620-bddb3878-dfb8-4138-a8c4-6290f0849161.jpeg)

Here is the promised bounty. 

## sweeden-ttu | 2022-04-30T23:15:53+00:00
> @web-sharp To run the tests, do `cd build/<OS>/<branch>/release/tests/ && make test`

Still doesn't work 

## sweeden-ttu | 2022-04-30T23:16:51+00:00
> > OK I think it's clear you are paid by the government organization at this point to ruin monero
> 
> 
> 
> If by 'government organization' you mean 'Community Crowdfunding System' then yes, you are correct. see (note the number 5): https://ccs.getmonero.org/proposals/selsta-5.html
> 
> 
> 
> 

Rolls eyes.  So no accountability that's aparent!!  Here's two euros for you they matter to me nothing 

## trasherdk | 2022-05-01T07:12:22+00:00
@web-sharp update your github profile :grimacing: 
![image](https://user-images.githubusercontent.com/5003891/166136071-488a2e48-391f-44ce-9f3b-c63002bb8134.png)


# Action History
- Created by: sweeden-ttu | 2022-04-29T18:27:34+00:00
- Closed at: 2022-04-30T07:21:52+00:00
