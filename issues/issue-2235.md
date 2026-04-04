---
title: 'plugin request: jekyll-target-blank'
source_url: https://github.com/monero-project/monero-site/issues/2235
author: plowsof
assignees: []
labels:
- 🧰 back end
created_at: '2024-01-31T09:40:44+00:00'
updated_at: '2024-07-18T07:30:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
#2233 (original #2118) hard codes some external links to open in an external window.

jekyll-target-blank 
>Automatically adds a target="_blank" rel="noopener noreferrer" attribute to all external links in Jekyll's content plus several other automation features for the external links. [Read more here](https://keith-mifsud.me/projects/jekyll-target-blank)

https://github.com/keithmifsud/jekyll-target-blank
https://rubygems.org/gems/jekyll-target-blank

uncovered some issues while testing:

We have bad URI's. To confirm , enter `https://matrix.to/#/#monero:monero.social` @ https://0mg.github.io/tools/uri/
- requires #2234
- requires #2237 

It then builds. and after a brief look it seems to work fine. 


# Discussion History
## plowsof | 2024-07-13T12:41:09+00:00
Ignore:
Since 2020, major web browsers have enabled native handling of lazy loading by default.

Adding another which would be useful:
Jekyll-loading-lazy https://github.com/gildesmarais/jekyll-loading-lazy

- we need to move to building site inside a docker container. both these plugins requires certain versions of gems / ruby and you will run into problems. it would remove alot of the friction for contributors also (when we eventually start bumping ruby versions) 

## plowsof | 2024-07-15T17:48:29+00:00
Testing with a docker build/run setup (to support plugins/ruby versions easier), and noticed a bug in the header logo:
```html
 <div class="col-lg-4 col-md-4 col-sm-4 col-xs-4">
   <a href="/%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20"><img src="/img/monero-logo.png" width="500" height="135" alt="Monero Logo" class="monero-logo" loading="lazy"></a>
 </div>
``` 

after some debugging/head scratching/downgrading ruby / removing plugins i confirmed `jekyll-loading-lazy` is the main culprit. new lines.. and spaces being escaped?: in `header.html` i see whats going on:

```liquid
<div class="col-lg-4 col-md-4 col-sm-4 col-xs-4">
  <a href="{% if site.lang == 'en' %}
  
  {{ site.baseurl_root }}/
  
  {% else %}
  
  {{ site.baseurl_root }}/{{site.lang}}
  
  {% endif %}"><img src="/img/monero-logo.png" width="500" height="135" alt="Monero Logo" class="monero-logo"></a>
</div>
```

`jekyll-loading-lazy` does not handle multiple line liquid scripts in the href. a brief search shows liquid templates can avoid adding whitespace/newlines to the html using [whitespace control](https://shopify.github.io/liquid/basics/whitespace/)

not needed as above comment shows most browsers have this enabled since 2020 but this would fix it and seems correct liquid scripting practice:

```liquid
<div class="col-lg-4 col-md-4 col-sm-4 col-xs-4">
  <a href="{% if site.lang == 'en' -%}

  {{ site.baseurl_root }}/
  
  {%- else -%}
  
  {{ site.baseurl_root }}/{{site.lang}}
  
  {%- endif %}"><img src="/img/monero-logo.png" width="500" height="135" alt="Monero Logo" class="monero-logo"></a>
</div>
```

# Action History
- Created by: plowsof | 2024-01-31T09:40:44+00:00
