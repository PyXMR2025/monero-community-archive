---
title: source contains non-free font files
source_url: https://github.com/monero-project/monero-gui/issues/1463
author: jonassmedegaard
assignees: []
labels: []
created_at: '2018-06-17T11:57:34+00:00'
updated_at: '2018-07-17T21:35:21+00:00'
type: issue
status: closed
closed_at: '2018-07-17T21:35:21+00:00'
---

# Original Description
The font files <fonts/*.otf> are copyright Apple and lack a free license.

Please either get Apple to license the fonts with a Free license, or replace with a freely licensed font.

# Discussion History
## pazos | 2018-06-18T15:36:48+00:00
Good catch @jonassmedegaard! I didn't notice that SFUI were san francisco fonts. Not sure if we are using those outside osx/ios bundles (against apple  license). Anyways we can replace those completely with good quality fonts like [roboto](https://github.com/google/roboto/blob/master/LICENSE)

## pazos | 2018-06-21T00:46:54+00:00
and to anwser myself, yes we are using the fonts in all the platforms: https://github.com/monero-project/monero-gui/blob/master/components/Style.qml#L6-L9

Roboto doesn't look nice on our qml interface so I think I will try Ubuntu fonts instead

## jonassmedegaard | 2018-06-21T05:59:12+00:00
Quoting Martín Fernández (2018-06-21 02:46:58)
> and to anwser myself, yes we are using the fonts in all the platforms: 
> https://github.com/monero-project/monero-gui/blob/master/components/Style.qml#L6-L9
> 
> Roboto doesn't look nice on our qml interface so I think I will try Ubuntu fonts instead

Please reconsider: Ubuntu font is non-free according to Debian: 
https://en.wikipedia.org/wiki/Ubuntu_(typeface)#Ubuntu_Font_Licence
https://alioth-lists.debian.net/pipermail/pkg-fonts-devel/2011-April/006515.html


 - Jonas

-- 
 * Jonas Smedegaard - idealist & Internet-arkitekt
 * Tlf.: +45 40843136  Website: http://dr.jones.dk/

 [x] quote me freely  [ ] ask before reusing  [ ] keep private


## pazos | 2018-06-21T16:31:43+00:00
fair point, I guess. Reverting to Roboto, which is Apache licensed font. Doesn't look that bad, but maybe @skftn would like to give a feedback.

## sanderfoobar | 2018-07-17T07:11:29+00:00
@jonassmedegaard Thanks for the headsup!
@pazos I'm trying out some [Apache licenced fonts](https://github.com/jenskutilek/free-fonts). will PR when I have something. I'm targeting the 13.0 release for this change of fonts.

# Action History
- Created by: jonassmedegaard | 2018-06-17T11:57:34+00:00
- Closed at: 2018-07-17T21:35:21+00:00
