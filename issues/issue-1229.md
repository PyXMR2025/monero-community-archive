---
title: ' syncing Daemon with GUI most of the times GUI gives a false positive "Connected"
  Progress Bar.'
source_url: https://github.com/monero-project/monero-gui/issues/1229
author: juanpc2018
assignees: []
labels: []
created_at: '2018-03-31T12:38:32+00:00'
updated_at: '2018-04-07T14:31:25+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When syncing the Daemon most of the times the GUI gives a false positive "Connected" Progress Bar,
The true way to know if it's truly synced is:
A) press start mining.......
or
B) task manager hard drive activity....

A way to detect HardDrive activity like task manager should combined to give a proper reading.
NOT + AND Gate Logic.
also detecting the true last block independently from another source + Comparator....

# Discussion History
## sanderfoobar | 2018-04-04T05:50:14+00:00
Are you saying the progress bars do not reflect that monerod is syncing/refreshing?

## qubenix | 2018-04-04T14:36:47+00:00
I'm not sure if this is what OP means (if I am wrong then I'll make an issue for this specifically), but I've experienced that the progress bar is either empty or full. Here you can see my blockchain is about 50% sync'd, but progress bar shows empty:

![image](https://user-images.githubusercontent.com/15707061/38314243-fc0cf0f2-37e2-11e8-9ad2-1b08e64a7197.png)

Here, just a little while later in the sync process, my bar shows full:

![image](https://user-images.githubusercontent.com/15707061/38314286-0fe350c6-37e3-11e8-9591-3c6ff7fa242f.png)

@juanpc2018 please confirm if this is what you are experiencing as well.

## juanpc2018 | 2018-04-06T18:49:27+00:00
in Windows8.1x64 shows Connected, but still is Syncing,
GUI Freezes, but resumes Ok.

Shows Blocks Remaining, Shows Connected, but still Syncing, GUI Freezes, but resumes OK,
until is fully connected... Hard Drive does not Move "monerod.exe",
Start Mining Works Ok. etc... 

## stoffu | 2018-04-07T03:49:29+00:00
@qubenix This is fixed in #1243.

## qubenix | 2018-04-07T14:31:25+00:00
Sorry to almost hijack this issue because it seems @juanpc2018 is having some freezing issue instead. My comment is fixed with pr #1243 so I don't think there's a need to open a separate issue.

# Action History
- Created by: juanpc2018 | 2018-03-31T12:38:32+00:00
