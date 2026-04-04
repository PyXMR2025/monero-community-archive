---
title: Site testing process & automation
source_url: https://github.com/monero-project/monero-site/issues/731
author: el00ruobuob
assignees: []
labels:
- 💬 discussion
created_at: '2018-05-09T12:48:29+00:00'
updated_at: '2020-04-19T09:57:25+00:00'
type: issue
status: closed
closed_at: '2020-04-19T09:57:24+00:00'
---

# Original Description
This thread is to discuss site testing & automation of this testing.

I have, on behalf of @rehrar, started to test myself the PRs, let's see if we can do better.

Environment (ESXi-absed VMs):
- A dedicated Ubuntu Server 18.04 to run the build on.
- 4 clients:
  - Ubuntu 18.04
  - CentOS 7
  - Windows 7
  - Windows 10

On the server, i made a script to start testing a PR based on it's number:

```bash
#!/bin/bash

if [ -z $1 ]
then
        echo 'Pull Request not specified'
        exit 1
elseif ! [[ $1 =~ ^[0-9]+$ ]]
        echo 'Pull Request should be a number'
        exit 1
fi

dirPR=PR$1
dirExist=`find . -name $dirPR | wc -l`

echo "Getting Pull Request informations"
PRpage=`curl https://github.com/monero-project/monero-site/pull/$1`
PRtitle=`<<<$PRpage grep title | head -1 | sed s/"<title>"//g | sed s/"<\/title>"//g`
echo $PRtitle

if [ $dirExist == "1" ]
then
        echo "Directory exist for Pull Request" $1
        cd $dirPR
        echo "Clearing local changes and fetching again"
        git fetch origin master
        git reset --hard FETCH_HEAD
        git clean -df
        git pull -f --no-edit
        echo "Fetch succeeded"
else
        echo "No directory, getting Pull Request"
        PRsource=`<<<$PRpage grep "class=\"commit-ref" | grep title | tail -1 | sed s/\"/" "/g | awk '{print $3}'`
        repo=`<<<$PRsource sed s/\:/" "/g | awk '{print $1}'`
        branch=`<<<$PRsource sed s/\:/" "/g | awk '{print $2}'`
        echo "Going to fetch" $branch "from repository" $repo
        git clone -b $branch https://github.com/$repo $dirPR
        cd $dirPR
fi

rubyPS=`ps aux | grep ruby | grep -v grep`
rubyRunning=`<<<$rubyPS wc -l`

if [ $rubyRunning == "1" ]
then
        echo "Ruby is already running, killing..."
        rubyPID=`<<<$rubyPS awk '{print $2}'`
        kill -9 $rubyPID
        echo "Killed. Let's Rock'n'Roll!"
else
        echo "Ruby is not here. Let's Rock'n'Roll!"
fi

jekyll serve --host vsrv-ubuntu-getmonero --port 80 -I --detach
local=(`ls _i18n/ | grep -e ^..$ | grep -v en`)
for i in "${local[@]}"
do
        cp -R _i18n/$i/resources/user-guides/png _site/$i/resources/user-guides/
done
echo "Getmonero stagged for Pull Request" $PRtitle
echo "Please connect to getmonero.<my_domain> and try!"

exit 0
```

Which i called this way: ```./gitter.sh #PRnum```

Then, i connect on my 4 VMs to check for all the browsers:

  | Edge | IE 11 | Chrome | Firefox | Opera | Vivaldi
-- | -- | -- | -- | -- | -- | --
Windows 7 | - | OK | OK | OK | OK | OK
Windows 10 | OK | OK | OK | OK | OK | OK
Ubuntu 18.04 | - | - | OK | OK | OK | OK
CentOS 7 | - | - | - | OK | OK | OK

Only Firefox is perfect out of the box.
All others are showing a lot of carriage return around the <language_name> box:
Firefox:
![image](https://user-images.githubusercontent.com/37215310/39815757-667c41e6-5399-11e8-9d13-1df7d702c26e.png)

Others:
![image](https://user-images.githubusercontent.com/37215310/39815781-707c591a-5399-11e8-9756-273cbb6edf24.png)
![image](https://user-images.githubusercontent.com/37215310/39815798-7ce2a0c4-5399-11e8-8f44-0eeda2f9174e.png)

See the language selection item taking all the place:
![image](https://user-images.githubusercontent.com/37215310/39815739-5279e518-5399-11e8-8138-bfb49881f7d3.png)


# Discussion History
## el00ruobuob | 2018-05-09T12:48:44+00:00
About the bot, @mattcode55 it could be great. However it's not always about just the page look and feel, sometimes testing it with a mouse help to discover some glitches (i found links inconsistency on #692 this way). So a human being will always have to test for consistency.
But if you have ideas to impove my testing platform, please share. At the moment, i only have automated the process of creating a new directory based on the PR number, grabbing automatically a new PR or new changes when i ask for, and starting jekyll on my env.
I can share my bash script if you're insterested.

On the client side, it means connecting to the server, checking a (new) logfile to see if build has changed from previous check and what to test, and then push the screenshots as comments. But it will not help my bandwidth... and the glitches that i presume are corrected by @rehrar at each update will be present on the screenshots.

## el00ruobuob | 2018-05-09T13:41:38+00:00
@rehrar is the behaviour i have with all browsers apart from firefox something you already know about?

## el00ruobuob | 2018-05-09T14:42:19+00:00
Could anyone with apropriate rights flag this as +discussion ?

## mattcode55 | 2018-05-09T19:26:44+00:00
>About the bot, @mattcode55 it could be great. However it's not always about just the page look and feel, sometimes testing it with a mouse help to discover some glitches (i found links inconsistency on #692 this way). So a human being will always have to test for consistency.

Yes, that's true. Although I do think a bot would still be useful, it would make it easy to see what a PR did without wading through the diff.

***

+discussion

## el00ruobuob | 2018-05-17T15:36:33+00:00
I have reinstalled ruby in 2.4.1, i don't have any needs to `bundle exec` the `jekyll serve`, however, i still have the strange behaviour on the browsers.

## erciccione | 2020-04-09T08:49:35+00:00
This issue was opened on GitLab for some time (closed now in preparation for the migration) and got 2 additional comments: https://repo.getmonero.org/monero-project/monero-site/-/issues/731

## erciccione | 2020-04-19T09:57:24+00:00
I don't think this is still relevant, especially now that we have CI process. Closing it, but feel free to reopen it if still relevant

# Action History
- Created by: el00ruobuob | 2018-05-09T12:48:29+00:00
- Closed at: 2020-04-19T09:57:24+00:00
