---
title: Pages versionning
source_url: https://github.com/monero-project/monero-site/issues/738
author: el00ruobuob
assignees: []
labels: []
created_at: '2018-05-18T06:44:26+00:00'
updated_at: '2018-07-18T12:45:17+00:00'
type: issue
status: closed
closed_at: '2018-07-18T12:45:17+00:00'
---

# Original Description
Hi everyone,

I wonder if we could use front matter in all pages to track changes and display a disclaimer on the website.
The idea is:
- To warn the readers that the version may be outdated or incomplete
- To help the localization team to do update

For that, i suggest to add:
- On Each File:
```Markdown
---
version.major: 1
version.minor: 0
version.build: 0
---

{% include version_check.html title={{ page.title }} version={{ page.version }} %}
```

- in a version_check.html page:
```Markdown
{% assign templatepage = site.pages | where: 'title', {{ title }} %}
{% for item in templatepage %}
  {% if item.path | slice: 1, 2 == "en" %}
    {% assign templateVersion = item.version %}
  {% endif %}
{% endfor %}

{% if version.major != mainVersion.major %}
  //disclaimer "This page is outdated, do not use it as reference"
{% version.minor != mainVersion.major %}
  //disclaimer "This page is not up to date, but may be used as reference"
{% else %}
  // Nothing
{% endif %}
```

The Major version concerns changes that make the old version unusable (totally outdated - a full rewrite needed), the Minor version is for improvements (like adding updated screenshots, or new options) keeping the old version usable, and build version is for typos and other corrections which are not related to the content that matter.

What do you think of this @rehrar @erciccione 

# Discussion History
## el00ruobuob | 2018-05-24T06:11:25+00:00
The solution such as i'm describing is not working here.
I work on a slightly different one, as a POC on my side now, and the results are so far so good.

Base page version to be handled in the "root" directory-page, where the front-matter is.
```html
---
layout: user-guide
title: "How to solo mine with the GUI"
permalink: /resources/user-guides/solo_mine_GUI.html
mainVersion:
  - "2"
  - "1"
  - "0"
---
```

On the localized md files, an assign and an include would do.
By the way, both version and untranslated "disclaimer" are grouped.
```md
{% assign version = '2.0.0' | split: '.' %}
{% include disclaimer.html translated="true" version=page.version %}
```

And the disclaimer page:
```html
<div class="disclaimer">
  {% if translated != "true" %}
    <p>{% t global.untranslated %} <a class="disclaimer-link" href="https://github.com/monero-project/monero-site/blob/master/README.md">README</a>.</p>
  {% endif %}
  {% if version[0] != page.mainVersion[0] %}
    {% capture link %}{{ site.baseurl_root }}{{ page.url }}{% endcapture %}
    <p>{% t global.outdatedMax %} <a class="disclaimer-link" href="{{ link1 }}" >{% t global.outdatedVersion %}</a>.</p>
  {% elsif version[1] != page.mainVersion[1] %}
    <p>{% t global.outdatedMin %}</p>
  {% endif %}
</div>
```

I need a bit more tune before doing a POC PR, after what i'll see with @rehrar how we could implement it.

Anyway, feedback are welcome regarding the idea itself.

## el00ruobuob | 2018-05-24T09:10:30+00:00
Ping @erciccione @mattcode55 @MaxXor, what do you think about it?

## el00ruobuob | 2018-05-24T10:27:12+00:00
My POC is working.
I will PR it later for everyone to see it.
Disclaimer page is as follows:
```liquid
{% assign disclaimer = "" %}

{% if version[0] != page.mainVersion[0] %}
  {% capture linkEN %}{{ site.baseurl_root }}{{ page.url }}{% endcapture %}
  {% capture disclaimer %}{% t global.outdatedMax %} <a class="disclaimer-link" href="{{ linkEN }}" >{% t global.outdatedVersion %}</a>.{% endcapture %}
{% elsif version[1] != page.mainVersion[1] %}
  {% capture disclaimer %}{% t global.outdatedMin %}{% endcapture %}
{% endif %}

{% if include.translated != "true" %}
  {% if disclaimer != "" %}
    {% capture disclaimer %}<br>{{ disclaimer }}{% endcapture %}
  {% endif %}
  {% capture disclaimer %}{% t global.untranslated %} <a class="disclaimer-link" href="https://github.com/monero-project/monero-site/blob/master/README.md">README</a>.{{ disclaimer }}{% endcapture %}
{% else %}

{% endif %}
{% if disclaimer != "" %}
  <div class="disclaimer">
    <p>{{ disclaimer }}</p>
  </div>
{% endif %}
```

## erciccione | 2018-06-02T12:11:30+00:00
+improvement
+in progress

## el00ruobuob | 2018-07-17T21:27:36+00:00
Solved by merging of #741

## erciccione | 2018-07-18T12:32:05+00:00
@el00ruobuob you can just close a PR if you opened it and it's solved.
btw:

+resolved

# Action History
- Created by: el00ruobuob | 2018-05-18T06:44:26+00:00
- Closed at: 2018-07-18T12:45:17+00:00
