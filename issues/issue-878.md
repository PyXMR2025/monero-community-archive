---
title: Adding Quickfacts to Press-kit section
source_url: https://github.com/monero-project/monero-site/issues/878
author: lh1008
assignees: []
labels: []
created_at: '2018-09-07T23:33:34+00:00'
updated_at: '2020-04-07T09:45:48+00:00'
type: issue
status: closed
closed_at: '2020-04-07T09:45:48+00:00'
---

# Original Description
Hi,

I have been working on adding the [Quick-Facts Sheet](http://www.monerooutreach.org/pubs/2018/QuickFacts/QuickFacts.pdf) to the getmonero.org/press-kit section, and I already added some new elements and style. 
I took the library style, to begin with (took me a while to learn how to work inside the website, so sorry for those who have been waiting for this a long time ago). We haven' t decided yet the final design, but I make this issue because @el00ruobuob volunteered to help me set it up and would be glad to have him join this quest.

@el00ruobuob the branch I have been working on is the [press-kit](https://github.com/lh1008/monero-site/tree/presskit). 

Thank you! :)


  

# Discussion History
## el00ruobuob | 2018-09-08T05:54:31+00:00
At first site I can see a mismatch between yml and md files.
The yml is no construct the same way liquid is calling the tags.
I go deeper in in later today.

## el00ruobuob | 2018-09-08T16:30:33+00:00
I wasn't woke up when i read the code this morning.
So following our discussion on Wire, i think you could do the following changes to always point to the up to date file:

*  on `presskit/_i18n/en.yml`:
   * replace `file: "QuickFacts.pdf"` with `url: "http://monerooutreach.org/pubs/2018/QuickFacts/QuickFacts.pdf"`  
* on `presskit/press-kit/index.md`:
   * replace `<a href="{{ site.baseurl_root }}/press-kit/{{ publication.file }}">` with `<a href="{{ publication.url }}">`

# Action History
- Created by: lh1008 | 2018-09-07T23:33:34+00:00
- Closed at: 2020-04-07T09:45:48+00:00
