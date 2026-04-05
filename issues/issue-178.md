---
title: I built a simple Frontend for the API!
source_url: https://github.com/xmrig/xmrig/issues/178
author: dunklesToast
assignees: []
labels:
- META
created_at: '2017-10-27T21:42:09+00:00'
updated_at: '2018-11-05T12:31:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hey!
This is not an issue but I just wanted to let you know that I recently finished a simple Frontend for the XMRig API.
You can find it [here](https://github.com/dunklesToast/XMRigFrontend).

maybe one or two of you like this and use it to monitor their rigs!


cheers,
- dunklestoast

# Discussion History
## xmrig | 2017-10-27T22:09:55+00:00
Very interesting, I leave this issue open, more people can see it.
I suggest host it somewhere, for example use GitHub pages, not for all drop 3 files is simple.
And another useful feature: monitor multiple miners.
Thank you.

## rtau | 2017-10-28T01:11:46+00:00
Will it be too crazy to use github pages to host it?

https://pages.github.com/

## dunklesToast | 2017-10-28T10:10:29+00:00
I have created a GitHub Page for the Frontend: https://dunklestoast.github.io/XMRigFrontend/index.html
But currently there is this Problem: [FrontEnd Issue 2](https://github.com/dunklesToast/XMRigFrontend/issues/2)

## dunklesToast | 2017-11-07T12:54:05+00:00
Today I released Version 0.4 which now enables the possibility to add multiple Miners and I also added XMRIG Proxy Support!
https://github.com/dunklesToast/XMRigFrontend/releases/tag/v0.4.1

## dorimanx | 2017-11-07T22:41:21+00:00
Awesome! 

## wodgey | 2018-01-15T18:48:57+00:00
So? Can I just throw a simple apache server onto my mining rig itself, and point to local host? 
I'm not v.experienced with Linux but can fumble through the basics.

Would the python simple http server work? my mining rig is only a low powered celeron with 12 GPU's and 8Gig RAM. Would putting this on my mining rig be too power hungry?

## dunklesToast | 2018-01-15T18:53:15+00:00
Apache works fine! But you need to point it to the internal IP of your rig (should look something like that 192.168.178.155 or 10.0.2.3).
If you open the Page on your Rig then you can use localhost. The Apache Server should not be too power hungry since it just needs to deliver static files! If you have any questions ask here or create a new issue in the [Frontend Repo](https://github.com/dunklesToast/XMRigFrontend)

## wodgey | 2018-01-15T20:09:18+00:00
Thank you


# Action History
- Created by: dunklesToast | 2017-10-27T21:42:09+00:00
