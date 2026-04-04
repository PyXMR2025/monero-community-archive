---
title: Window resizing issue when running dual monitors on a PC
source_url: https://github.com/monero-project/monero-gui/issues/3850
author: geonic1
assignees: []
labels: []
created_at: '2022-03-04T20:39:55+00:00'
updated_at: '2022-03-04T21:22:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This bug has existed for a few years, but I'm getting to reporting it now.

Steps to recreate the issue:

1. Run dual monitors
2. Open GUI, turn second monitor off. GUI window will remain properly sized on the main monitor.
3. Turn main monitor off. Turn it back on. GUI will not adjust to the proper resolution and will be unusable. Image:
![image](https://user-images.githubusercontent.com/48529862/156837974-2757b205-dc0c-453a-aded-b8dfded889aa.png)
4. To force it to resize, you either have to turn the second monitor on or remove the second monitor connection from the computer.

My other applications all resize properly when using one or two monitors. The GUI is the one exception.

Happy to provide any other details if necessary.


# Discussion History
## geonic1 | 2022-03-04T20:52:54+00:00
A few more screenshots of the GUI when it gets stuck in this mode.

![image](https://user-images.githubusercontent.com/48529862/156839042-a95f41c9-8b15-469a-97a2-29ad4d2c9e91.png)

![image](https://user-images.githubusercontent.com/48529862/156839919-9d75dc4a-2d3b-46a7-b857-9d1e506cdfee.png)



## selsta | 2022-03-04T20:55:05+00:00
Can you go to Settings -> Interface and turn off custom decorations? I assume it won't fix anything but it might help with some resizing related bugs.

Also HighDPI is handled by the Qt library, it's not much we can influence. We have to update to Qt6 at some point, it might fix some issues.

## geonic1 | 2022-03-04T21:10:01+00:00
Yeah, that didn't fix it. Here it is with custom decorations turned off:

![image](https://user-images.githubusercontent.com/48529862/156842106-feddb136-a680-4dc2-86c9-4aaefc8b84d7.png)




## selsta | 2022-03-04T21:10:48+00:00
What happens if you resize the program during this state?

## geonic1 | 2022-03-04T21:12:43+00:00
Not much. Here it is resized and in full screen.

![image](https://user-images.githubusercontent.com/48529862/156842165-013b6ad1-4f27-4a72-929e-0fe8292662f1.png)
![image](https://user-images.githubusercontent.com/48529862/156842190-f247c14f-ca39-4429-a107-98e9d3f64ee5.png)


## selsta | 2022-03-04T21:21:56+00:00
Seems like a bug in Qt then. We will have to update to Qt6 to see if it fixes the issue.

## geonic1 | 2022-03-04T21:22:39+00:00
Also interesting to note is that, in this condition, what's displayed doesn't match with where the buttons actually are.

https://user-images.githubusercontent.com/48529862/156843294-492a4371-8d6e-4c18-b369-4c89502128e6.mp4




# Action History
- Created by: geonic1 | 2022-03-04T20:39:55+00:00
