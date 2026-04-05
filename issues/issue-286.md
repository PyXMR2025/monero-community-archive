---
title: Is there any way to write a code in source code to make miner run automatically
  ?
source_url: https://github.com/xmrig/xmrig/issues/286
author: a7adidy
assignees: []
labels: []
created_at: '2017-12-23T01:57:50+00:00'
updated_at: '2018-11-05T12:33:17+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:33:17+00:00'
---

# Original Description
Is there any way to write a code in source code to run miner automaticly at start up !? Please help me  

# Discussion History
## BigMichi1 | 2017-12-23T08:37:47+00:00
easiest way is with crontab

all files will be in '/home/user/xmrig/'

`@reboot cd /home/user/xmrig/ && /home/user/xmrig/xmrig`

## Dhruv420 | 2017-12-23T12:01:45+00:00
You can try creating a service for xmrig.exe-(It will automatically start whenever you log in to you windows)
**## Step 1-**
To run an app as a service, you’re going to need a small, third-party utility. There are several out there, but my favorite is SrvStart.
To get started, head over to the download page (http://www.rozanski.org.uk/software) and download SRVSTART. The download contains just four files (two DLL and two EXE files). There’s no installer; instead, copy these to your computer’s C:\Windows folder these to your main Windows folder to “install” SrvStart.


![image](https://user-images.githubusercontent.com/25684786/34319245-03df1d08-e803-11e7-8df6-cbf76832fc1b.png)

**## Step Two: Create a Configuration File for the New Service-**
Next, you’ll want to create a configuration file that SrvStart will read to create the service. 
Fire up Notepad and create your configuration file using the format below.


![ddd](https://user-images.githubusercontent.com/25684786/34319278-db0474ea-e803-11e7-973f-4fade301b39f.PNG)




For me it looks like this-


![dddd](https://user-images.githubusercontent.com/25684786/34319300-3dde2a98-e804-11e7-9051-66737d84b352.PNG)


Save the new configuration file wherever you like, and replace the .txt extension with a .ini extension. Make note of the file name, since we’ll need it in the next step. For ease of typing at the Command Prompt, I suggest saving this file temporarily right on your E: drive.


**## Step Three: Use the Command Prompt to Create the New Service-**

Open Command Prompt by right-clicking the Start menu (or pressing Windows+X), choosing “Command Prompt (Admin)”, and then clicking Yes to allow it to run with administrative privileges.

![image](https://user-images.githubusercontent.com/25684786/34319310-a0f933ca-e804-11e7-9e87-d31b6bbbbaba.png)

At the Command Prompt, use the following syntax to create the new service:

![nn](https://user-images.githubusercontent.com/25684786/34319327-39ffe1ea-e805-11e7-9b3a-008a11f86a32.PNG)

For me it looks like-

![nnn](https://user-images.githubusercontent.com/25684786/34319348-f31a1574-e805-11e7-86df-7ff121468e07.PNG)
Press ENTER-

![jj](https://user-images.githubusercontent.com/25684786/34319354-166abea2-e806-11e7-88b7-991c9a8283e6.PNG)

When you run the command, you should receive a SUCCESS message if everything goes well.

You have successfully created your service-

![ii](https://user-images.githubusercontent.com/25684786/34319374-d6a20f2c-e806-11e7-8943-e8b27248ec66.PNG)

In case it shows status as stopped just right click and select start and you are good to go.

HOPE THIS HELPS :)


## a7adidy | 2017-12-23T19:01:51+00:00
i want to write a code in source code to make the miner run at start up ! is that possible ?

## Zelecktor | 2017-12-24T23:20:41+00:00
@Dhruv420
Amazing tutorial! great job.

I have a few questions, i hope you can help me.
I just want to do it on windows 7. I need some help in creating the new service on the command  prompt.

This will run the program even if no user log on the machine?. For example if i turn on the computer, enter in the stand by windows and no user logs in.

And the last thing. I want to make like an easy "install setup" to install xmrig (just put the compiled files in C:/program files/xmrig (or wherever) but also make the service to start the program automatically (if someone turns off the computer) just in case when it turns on again, it start mining again (even if no user logs in) just in the stand by

## Dhruv420 | 2017-12-26T07:38:11+00:00
@Zelecktor 
I think you necessarily need to log in for the service to trigger up,but i have a solution for your problem you can use **autologon**,what it basically does is that it automatically logs in a specific user  as the name suggests. (**This setting is recommended only for cases in which the computer is physically secured and steps have been taken to make sure that untrusted users cannot remotely access the registry**.)

## **To use Registry Editor to turn on automatic logon, follow these steps:**
1) Click Start, and then click Run.
2)In the Open box, type Regedt32.exe, and then press Enter.
3)Locate the following subkey in the registry:
**HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon**
4)Double-click the DefaultUserName entry, type your user name, and then click OK.
5)Double-click the DefaultPassword entry, type your password, and then click OK.

**In Case there is no default password it must be added. To add the value, follow these steps:**
1)On the Edit menu, click New, and then point to String Value.
2)Type DefaultPassword, and then press Enter.
3)Double-click DefaultPassword.
4)In the Edit String dialog, type your password and then click OK.

**Now back to step 6-**
6)On the Edit menu, click New, and then point to String Value.
7)Type AutoAdminLogon, and then press Enter.
8)Double-click AutoAdminLogon.
9)In the Edit String dialog box, type 1 and then click OK.
10)Exit Registry Editor.
11)Click Start, click Shutdown.
12)Click OK to turn off your computer.
13)Restart your computer. You can now log on automatically.

**To bypass the AutoAdminLogon process and to log on as a different user, press and hold the Shift key after you log off or after Windows restarts.**

**For your problem regarding creating new service in cmd-**
You just need to follow the simple syntax-
![image](https://user-images.githubusercontent.com/25684786/34350387-8bce4f64-ea3c-11e7-99f3-c654fa7af070.png)

**For Example my .ini configuration file is in E named dd drive I will write the command in format-**
![bb](https://user-images.githubusercontent.com/25684786/34350596-a156aab0-ea3d-11e7-9140-7e8018b5537e.PNG)

Hope this will Help :)



## Dhruv420 | 2017-12-26T07:47:06+00:00
@Zelecktor
As far as i know there are many guides on the Internet to make a compiled setup.You can follow any one of those :)

## Zelecktor | 2017-12-26T15:02:20+00:00
@Dhruv420 Thanks very much for your guide. I'll try but the thing is that i can't leave logged a sesion.
The computer what i want to do it, is used by many people (each one with their own username and pass, but as user privileges). Im the admin, so most part of the day the computer is turned on but always in stand by, on the night we turn off (mostly) but at 8:00am we turn it on leaving it in stand by, just to leave it ready if someone needs to use it.
Just a waste of CPU if we leave there turned on all day without use it. Also tested with 2 threat and uses about 14-17% of CPU (about 150-170h/s), witch means that it doesnt affect any user and for what is used for (usually webpages, excel, SAP and printing)

## Dhruv420 | 2017-12-26T15:15:06+00:00
@Zelecktor Hmm..i got a clear picture of your situation now.Once you log in to the admin account  the services are activated.Then you are free to sign out and keep the computer on lock screen for others to join in.I think the miner should work fine then.

## Zelecktor | 2017-12-26T15:31:48+00:00
@Dhruv420 yeah thats easy, even its not nessesary do it as a service, just using shell:startup and works with every user (using background function), already tested, but i cant be logging every day, mostly if i want to do it with others computers.
Run it in stand by is one solution

## Dhruv420 | 2017-12-26T15:45:21+00:00
@Zelecktor shell startup won't start the application on lock screen either.

## Zelecktor | 2017-12-26T16:07:44+00:00
@Dhruv420 nope, an user must log in first to make it work, then when he/she leaves is the problem. if the sesion is closed it stop mining, if the user "lock" sesion the miner and all programs of that sesion remains running.

But you got what i want to do, just try to run xmrig when windows start on the stand by (or lock window). Prety sure there is a method, like add as a windows esential program



## Dhruv420 | 2017-12-26T16:14:27+00:00
@Zelecktor hmm...as of now I have no method in my knowledge that will do the task as you intend.But I sure will do some research,after all I am a learner too.

## Zelecktor | 2017-12-26T17:39:40+00:00
@Dhruv420 thanks very much! yeah im sure it will be usefull to many people. Yeah i saw on your first line

> You can try creating a service for xmrig.exe-(It will automatically start whenever you log in to you windows)

I said, yeah! thats what i need, no users log in = mining on the stand by windows (also mining all time if the PC is turned on, if an user logs in and logs out). But it didnt worked as i spected, I just re-booted, enter on the stand by but i didnt see any worker on my dashboard, but when i enter as an normal user or admin, then start mining.

## Dhruv420 | 2017-12-26T19:58:44+00:00
@Zelecktor
Happy to help :)

# Action History
- Created by: a7adidy | 2017-12-23T01:57:50+00:00
- Closed at: 2018-11-05T12:33:17+00:00
