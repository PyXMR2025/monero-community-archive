---
title: Xmrig Specific thread range optional config
source_url: https://github.com/xmrig/xmrig/issues/2674
author: ghost
assignees: []
labels: []
created_at: '2021-11-07T01:53:03+00:00'
updated_at: '2023-12-04T06:21:17+00:00'
type: issue
status: closed
closed_at: '2023-12-04T06:21:17+00:00'
---

# Original Description
I think for running multiple xmrig proccess on the same computer with multiple threads like 12 threads 6 core ryzen 5 1600x
if running 2 process i can choose thread count 4 and its pretty optimal but i think for increased efficiency

adding a option to specify thread ranges like thread-range=[ 0 1 2 3 ] and then you could run the second script running at the same time on the same computer with an option of thread-range=[ 4 5 6 7 ] and then could potential add an additional very low difficulty coin with a thread-range=[ 8 9 ] etc.. 

also a option which by default is set to false such as 
custom-thread-range: false
if false then it will continue with your default optimizations if true then allows person to customize

potentially if this function was added you would see a major boost in running it on a cpu with 64 threads or 32 threads being as you could specify what thread to attach and run on and specify the amount of power to use using your setup configurations already you have like max-cpu-threshold= etc.. 

but i have been able to push 2000h/s on just the first 4 threads running 2 different scripts so it must already be attaching to other threads but based on the output of 600/hs on each thread in each script file i think it doesn't really have that function so if this could be added then i think the h/s could be pushed even further with this mining software such as lets say i run 2 scripts on the same threads and then i could be pushing about 6 scripts and probably wouldn't see a decline in h/s but i just think this would be really good addition for the advanced miners trying to overclock and especially the watercooling miners with cpu's i have always loved your mining software since 2017 i've been using it and would really love to see this addition i have always ran it on linux os too.

Also i wouldn't mind sharing my config file setup i am using to get the 2000h/s per script with the script files i use to auto start said scripts files with a terminal and array to randomize mining multiple crypto's with the unmineable pool website
running the amd ryzen 5 1600x with a Cryorig H7 quad lumi for cooling the cpu along with open pc

But until this function is added i will probably just be running one at a time and randomizing which one it does but i would greatly appreciate if this option would be added as then i can play around with the configurations to test some different setups i have in mind as the accepted shares per seconds seem to be alot more optimal but in the long run for my randomizing script file i would like to have a function that runs 2 scripts at the same time for the lowest difficulty currencies i have upto about 10 to 12 cryptos i would like to accomplish this with. while i have about 24 to 30 cryptos i have that would randomize and mine 1 at a time mainly trying to increase the amount of cryptos i can mine at a time thus increasing long term profit goals with more outcomes possible

# Discussion History
# Action History
- Created by: ghost | 2021-11-07T01:53:03+00:00
- Closed at: 2023-12-04T06:21:17+00:00
