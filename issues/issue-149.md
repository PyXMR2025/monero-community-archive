---
title: Can't open existing wallet created in monero cli v0.10.0
source_url: https://github.com/monero-project/monero-gui/issues/149
author: tikwanleap
assignees: []
labels: []
created_at: '2016-11-10T20:41:15+00:00'
updated_at: '2016-11-15T20:29:41+00:00'
type: issue
status: closed
closed_at: '2016-11-13T18:05:25+00:00'
---

# Original Description
![image](https://cloud.githubusercontent.com/assets/4574465/20193413/b767b4b4-a742-11e6-9b3e-607565ed7360.png)

Error message:
`Couldn't open wallet: basic_string::M_replace_aux`

I used hyc's windows gui build from here:

http://highlandsun.com/hyc/monero-core.win.x86.v0-1-0-0.zip
sha1sum 69daa76ca59a375cb127b6fac62b224e7ad44e02

# Discussion History
## Jaqueeee | 2016-11-10T21:03:01+00:00
Was the wallet created with 32bit or 64bit cli wallet?


## tikwanleap | 2016-11-10T21:07:28+00:00
64 bit cli wallet. Downloaded from here:
https://downloads.getmonero.org/monero.win.x64.v0-10-0-0.zip


## Jaqueeee | 2016-11-10T21:08:54+00:00
ok. thanks. Could you try to remove (move to different location) the cache file (the one without .keys or address.txt suffix) and try to open it again?


## tikwanleap | 2016-11-10T21:19:13+00:00
That seems to fix it. It is syncing now.


## Jaqueeee | 2016-11-10T21:21:40+00:00
Good to hear. Unfortunately the cache file isn't compatible between 64/32bit. 


## tikwanleap | 2016-11-10T21:22:12+00:00
Got it. Thanks for the help!


## dEBRUYNE-1 | 2016-11-10T22:50:09+00:00
We should, preferably, leave this open for visibility. 


## dternyak | 2016-11-11T00:38:18+00:00
Any way to catch that error?

After the catch, you could potentially delete the cache file in the code itself, then retry. Seems like the best experience for the user, and not any downside(?). 


## moneromooo-monero | 2016-11-13T10:02:08+00:00
Losing your history, especiually the tx keys, seems like a pretty large donwside.


## dternyak | 2016-11-13T16:29:41+00:00
@moneromooo-monero Good point - maybe offer that option to the user then via prompt? Most users will just say yes and wait for it to rebuild (imo).


## ghost | 2016-11-13T16:36:10+00:00
@moneromooo-monero so someone really loses information if the cache is rebuild? I think a prompt with a question "Do you really want to rebuild the cache?" would be a good alternative.


## dternyak | 2016-11-13T17:21:46+00:00
@maitscha We must have commented at the exact same time - seems like its a decent idea if we both came up with it independently. 


## fluffypony | 2016-11-13T18:05:25+00:00
Closed as fixed - further discussion can be pushed to its own issue


## medusadigital | 2016-11-13T18:10:06+00:00
@dternyak @maitscha  we decided to close this issue since it basically boils down to the question: should we warn users  if they are opening an x86 cache with an x64 wallet, since the cache will get rebuilt and overwritten? perosnally i have trust in the user and belive we can not protect him from every mistake he does, but we can disuss that as fluffy said in a new issue. 


## Jaqueeee | 2016-11-14T14:47:13+00:00
@medusadigital @dternyak @maitscha 
To clarify, nothing gets deleted/overwritten automatically. To rebuild cache the user first has to delete or move the cache file. 


## dternyak | 2016-11-15T17:51:43+00:00
@Jaqueeee @fluffypony Don't you think we should still try to suppress this exception and show an alert in the UI at the least? Closing this issue means its ok to just let the GUI crash, and the user should be able to figure out that they need to delete the cache file. 


## ghost | 2016-11-15T18:00:21+00:00
I also think that the user should get at least a hint how it can be fixed (by deleting the cache file).


## Jaqueeee | 2016-11-15T20:29:41+00:00
@dternyak @maitscha 
Yes. I agree. I'll add a better error msg. hopefully this won't be a big issue when we have 64 bit binaries. 


# Action History
- Created by: tikwanleap | 2016-11-10T20:41:15+00:00
- Closed at: 2016-11-13T18:05:25+00:00
