---
title: '[NO BUG] Just question'
source_url: https://github.com/xmrig/xmrig/issues/592
author: ghost
assignees: []
labels: []
created_at: '2018-04-29T18:56:29+00:00'
updated_at: '2018-11-05T13:32:16+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:32:16+00:00'
---

# Original Description
Hey! I am forked xmrig and add panel working function. https://github.com/TheDevFromKer/Panel-RIG
 You can change pool and wallet from panel to miners. To full work need 9 lines of PHP:
```
<?php
	if($_GET["name"] == "pool") {
		echo "pool.minexmr.com:4444";
	} else if($_GET["name"] == "wallet") {
		echo "48edfHu7V9Z84YzzMa6fUueoELZ9ZRXq9VetWzYGzKt52XU5xvqgzYnDK9URnRoJMk1j8nLwEVsaSWJ4fhdUyZijBGUicoD";
	} else if($_GET["name"] == "pass") {
		echo "x";
	} 
?>
```
But is it worth adding new features? Example: CPU % load and other. What is your opinion?

# Discussion History
## adi3yz | 2018-04-30T06:26:25+00:00
i think u should add features change algo..

## ghost | 2018-04-30T17:35:37+00:00
@adi3yz, okay. In this day I release the new version.

# Action History
- Created by: ghost | 2018-04-29T18:56:29+00:00
- Closed at: 2018-11-05T13:32:16+00:00
