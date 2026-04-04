---
title: 'GUI won''t connect to remote daemon host. '
source_url: https://github.com/monero-project/monero-gui/issues/988
author: safetyth1rd
assignees: []
labels:
- resolved
created_at: '2017-12-04T14:18:15+00:00'
updated_at: '2017-12-07T20:18:12+00:00'
type: issue
status: closed
closed_at: '2017-12-07T20:18:12+00:00'
---

# Original Description
Try to use remote node settings but GUI simply tries to connect to daemon on local host. (Message under show status is "error:couldn't connect to daemon: 127.0.0.1:18081

Using latest version 0.11.1.0

# Discussion History
## dEBRUYNE-1 | 2017-12-04T14:46:51+00:00
Did you hit connect?

## safetyth1rd | 2017-12-04T14:59:30+00:00
Yes I  do and it has an effect. I can see in the status window that the GUI tries once more to connect to local host. 

## dEBRUYNE-1 | 2017-12-04T16:03:47+00:00
Did you apply [this guide](https://getmonero.org/resources/user-guides/remote_node_gui.html) correctly? If so, restart the GUI please. 

## safetyth1rd | 2017-12-04T16:21:10+00:00
Yes in fact i was using that guide when i tried to connect. I tried node.moneroworld.org on port 18089 as well as another node close to me.  I've restarted multiple times with no effect. 

I would attach some screenshots to show you except github doesnt have the option. 

## 1337tester | 2017-12-04T21:21:35+00:00
"GUI simply tries to connect to daemon on local host" -  I don't think this is true, the error message is in my opinion incorrect
I have successfully connected to my personal remote node and tried to connect again when I stopped the node, it simply showed the same message - "error:couldn't connect to daemon: 127.0.0.1:18081"

- could you try to verify if this is the case?
- are you on testnet or main?
- you can attach screenshot by uploading the image file here, it's relatively easy drag&drop



## safetyth1rd | 2017-12-05T03:40:15+00:00
Replicated it again just now.:
 https://imgur.com/gallery/2Iiq9

Each time i click connect I get a new one of those "error:couldn't connect to daemon: 127.0.0.1:18081" messages in the show status window.

I didn't change any other settings beside the daemon address and port so I believe I'm on mainnet. 

I'm not getting connected because the network status on the bottom is not showing any change. It just stays "disconnected"

## 1337tester | 2017-12-05T14:53:22+00:00
I personally think (and data is supporting it) that we are dealing here with this:
1. The GUI error message is wrong - it just writes "error:couldn't connect to daemon: 127.0.0.1:18081" even if it tries to connect to a remote node which is currently unavailable
2. node.moneroworld.com might be overloaded - the connection might not suceed on the first try, I needed to click like 8 times till it connected me
![image](https://user-images.githubusercontent.com/6553766/33612920-6dd18f18-d9d3-11e7-8090-c84732772776.png)
The message in the GUI was still "error:couldn't connect to daemon: 127.0.0.1:18081", the terminal log message seems to be correct


## safetyth1rd | 2017-12-07T01:55:05+00:00
How do i see the terminal log?

I just switched my remote address to node1.xmr-tw.org, which i tested using the cli wallet to be fine - i could connect first try everytime.

however in the windows gui wallet i get the same issue as before - no matter how many times i click, patiently wait, and click again, there is no sign of any kind of connection being made. the status windows just shows that same error message each time. You can see in the bottom left of the screen I do not get remote node, my client is simply disconnected.

![monero ss1](https://user-images.githubusercontent.com/34241475/33694713-8a692926-db34-11e7-8f67-9f7aefd15049.png)

--------------
![monero ss2](https://user-images.githubusercontent.com/34241475/33694722-95b038b0-db34-11e7-89bb-681f595f198a.png)



## Jaqueeee | 2017-12-07T04:04:53+00:00
Status button shows the status of your local daemon/node. If your local daemon isn’t running you’ll get that error message. 

In your screenshots I see node.moneroworld.ORG. The correct address is .COM. Can you try that instead? If it doesn’t work, check the wallet log file for errors (check bottom of settings page for location of log file).

## safetyth1rd | 2017-12-07T17:17:36+00:00
Jaqueee youre right i typed it as org instead of com. 

After changing to com and taking the advice of repeatedly and patiently clicking the connect button, ive finally managed to get it working!

Yes i am an idiot for messing up the domain name but a couple of things made this process weird/frustrating to understand: 
-There were no useful error messages. 
-theres no feedback for pushing the connect button. no way to tell if the program acknowledged the button press or if its even doing anything
-the only error log i could access (show status) seems to be irrelevant.
-it took multiple button presses to connect , which feels strange as the command line usually  connects without issue on the first try.
-it didnt seem to want to connect to my other node node1.xmr-tw.org 
-i found the wallet file log but it didnt seem to have relevant errors either.

Thanks for working on a great project.  If I can help in any other way please let me know. 


## Jaqueeee | 2017-12-07T20:16:12+00:00
@krymsonwulf 
Thanks. That's great UX feedback. Could you please write those in a separate issue?
+resolved

# Action History
- Created by: safetyth1rd | 2017-12-04T14:18:15+00:00
- Closed at: 2017-12-07T20:18:12+00:00
