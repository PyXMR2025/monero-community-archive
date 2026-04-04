---
title: German localizations issue
source_url: https://github.com/monero-project/monero-gui/issues/11
author: mbg033
assignees: []
labels: []
created_at: '2016-09-02T19:14:15+00:00'
updated_at: '2016-09-12T21:29:39+00:00'
type: issue
status: closed
closed_at: '2016-09-12T21:29:39+00:00'
---

# Original Description
@JamesCullum, could you please re-do it with Qt Linguist? Right now it can't be opened with Qt and it breaks the build
https://gyazo.com/4fe97d4c4fd4d924061bb2122cca5d52


# Discussion History
## JamesCullum | 2016-09-02T19:57:51+00:00
The installation of Qt Linguist crashed continously, thats why i had to do it via Notepad++ and asked for verification on the PR. Re-doing it would also be quite exhausting so id rather fix the existing one.

Ironically, i wanted to make sure to not break anything and only used html entities instead of non-english letters. The error comes from the html entitity that i used to replace german special characters, in this specific case, `&uuml;` equals the ü. I think i read somewhere in the Qt docs that this is how language specific characters are supposed to be used.

Can you try replacing the following sequences locally and check if it works then?

```
&uuml; => ü
&Uuml; => Ü
&auml; => ä
&Auml; => Ä
&ouml; => ö
&Ouml; => Ö`
```


## devinjdawson | 2016-09-10T09:30:23+00:00
@JamesCullum which files? 


## JamesCullum | 2016-09-10T10:39:42+00:00
What are you talking about?


## devinjdawson | 2016-09-11T00:10:55+00:00
I get an error "&uuml;" is undefined, when trying to compile the localization files on Ubuntu 16.04. I can't find `uuml` in the source. 


## JamesCullum | 2016-09-11T09:28:11+00:00
Then your tool compiles this code already to the special characters. Open the original files with a text editor and replace it.


## devinjdawson | 2016-09-11T11:14:08+00:00
which files


## JamesCullum | 2016-09-11T14:59:52+00:00
The file of the german translation, which is the only one i edited and the one that gives you the error during compilation?!


## devinjdawson | 2016-09-11T21:15:44+00:00
The files that are mentioned in the error are never created. When I look at the source, the term `uuml` is not present. This is why I do not know which files you are asking me to edit.

This is the exact error I get:

```
monero@monerocomputer:~/monero-core$ -make
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical translations/monero-core_de.ts -qm /home/monero/monero-core/release/bin/translations/monero-core_de.qm
lrelease error: Parse error at translations/monero-core_de.ts:9:41: Entity 'uuml' not declared.
Makefile:412: recipe for target 'release/bin/translations/monero-core_de.qm' failed
make: *** [release/bin/translations/monero-core_de.qm] Error 1
```


## JamesCullum | 2016-09-12T07:12:24+00:00
Are you using the current code? According to [this PR](https://github.com/monero-project/monero-core/pull/14/commits/f2a126790a777c6dce5370921f5461f7627f8e5e) it should be fixed already.


## mbg033 | 2016-09-12T21:29:39+00:00
yep, fixed


# Action History
- Created by: mbg033 | 2016-09-02T19:14:15+00:00
- Closed at: 2016-09-12T21:29:39+00:00
