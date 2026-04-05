---
title: command file startup deletes values from config.json, ignores other commands
source_url: https://github.com/xmrig/xmrig/issues/3024
author: NVMDSTEVil
assignees: []
labels: []
created_at: '2022-04-17T03:03:49+00:00'
updated_at: '2025-06-28T10:39:48+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:39:48+00:00'
---

# Original Description
**Describe the bug**
Using a .cmd file with an option such as --threads-hint "80" will delete the option from the config.cfg file rather than set the option to the same.  Not all commands (such as user/url) seem to suffer this issue and will be ignored completely.  Also the ability to set options realtime in the config.json file will be lost while xmrig is running due to using a .cmd file to startup if you dont use --config=config.json variable.  Using --config=config.json variable will ignore .cmd line values in the .cmd file!

**To Reproduce**
Create a .cmd startup file with startup values and --config=config.json.

**Expected behavior**
.cmd variables should read from the .cmd startup file, and written to config.json if the variable autosave is true, not deleted from config.json!  Should still be able to set variables in config.json when launching from a .cmd file even without setting --config=config.json.

**Required data**
 - Log does not show anything
 - .cmd line: xmrig.exe --config=config.json --cpu-max-threads-hint 76 -a gr -o stratum+tcp://server -u wallet.name -p x -o stratum+tcp://server -u wallet.name -p x
 - OS:WIN10

**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2022-04-17T06:38:39+00:00
Hints are command line only and are never written to config.json other than by modifying what profiles are generated.

If profiles already exist in config.json, hints are ignored.

And I think it's `--cpu-max-threads-hint` anyway.

When using command line options, do not use a config.json.  When using a config.json, do not use command line options.

## NVMDSTEVil | 2022-04-17T07:52:11+00:00
Yes, I just didnt bother checking that I wrote it right.

Still doesnt change the fact that having a hint deletes it from config.json if autosave is set to true, which then leaves a user confused when they go to config.json to change it and find it non-existant.

## Spudz76 | 2022-04-17T08:19:17+00:00
But there is no sense in having a hint in the config.json

They are hints for first-run.

## NVMDSTEVil | 2022-04-17T09:15:30+00:00
Maybe I need to make this simpler to understand.

This exists in config.json as the file is when extracted:

"max-threads-hint": 100,

It is deleted from config.json if you add it to your .cmd arguments.

If you wish to use it later from within config.json, it is not efficient to delete it from config.json.  Updating the value in config.json from the .cmd argument list would be more efficient and allow editing config.json on-the-fly for testing.

This goes for other items in the config.json as well, I have not bothered to test every single one.

## snipeTR | 2022-04-17T15:18:58+00:00
are you retarded? Is iq below 50? Are you stupid?
You should NOT use config.json when using arguments.
You should NOT use arguments when using config.json.
ANSWER TO THE QUESTION IS NULL

## NVMDSTEVil | 2022-04-17T19:37:24+00:00
Why? To allow real-time changes to XMRIG while it is running.  A very nice feature of XMRIG.

Thumbed down for the condescending attitude.

## Spudz76 | 2022-04-17T20:04:25+00:00
You can real-time change it anyway, either by editing the file and saving it (will be detected and reloaded) or by using the API to PUT a new one.

Nobody gets what you're talking about, maybe your use-case is wacky.  Feels like an X-Y problem.

## NVMDSTEVil | 2022-04-17T20:33:53+00:00
Editing the config.json file and saving it does not allow real-time change if you run from a .cmd/bat without the option --config=config.json, which when used ignores the other commands used in the .cmd/bat.

## Spudz76 | 2022-04-17T20:38:40+00:00
Why the hell are you running it from a cmd / bat

## snipeTR | 2022-04-17T23:05:22+00:00
probably a botnet is trying to run. or an IT employee who uses their company's computers without permission.

## NVMDSTEVil | 2022-04-18T00:39:31+00:00
> Why the hell are you running it from a cmd / bat

Why is the ability to use .cmd/bat files available (and example files provided) if its not an intended use case scenario?

## Spudz76 | 2022-04-18T11:19:11+00:00
It is an option if you do not use config.json at all, which is why it doesn't make one unless you incorrectly force it to do so with the `--config` option

Once a config.json exists, you just run `xmrig` with no args (or the exe directly).  Because it's designed to be used either one way or the other, not both.

And once there is a config.json you edit the file to modify options, with the exception of any autoconfig hints if you're trying to reconfigure thread profiles.

All setup howto's tell you to make a basic config.json with the wizard, and not use command line arguments at all.

Also most command line arguments are overridden by what's in config.json unlike how everything else in the world works.

In general the command line arguments should not be used unless you have a weird use-case where config.json can't work, or you like having all your configuration info readable in the process list.

## NVMDSTEVil | 2022-04-28T17:45:11+00:00
I guess i'll just stay dumbfounded on why you would allow things to be deleted from config.json and create confusion for newer users, seeing as many pools and discord servers suggest using command line as the preferred method.  Exist-and-override should in theory be much simpler but I guess I just subscribe to the old way of doing things where the config file kept all the different config inputs and didnt magically delete them because they also existed somewhere else.

## Spudz76 | 2022-04-28T22:29:42+00:00
Well the reason most pools document the command line method is to be consistent with how most other miner apps work, where they don't take any config file whatsoever.

# Action History
- Created by: NVMDSTEVil | 2022-04-17T03:03:49+00:00
- Closed at: 2025-06-28T10:39:48+00:00
