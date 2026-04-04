---
title: ' Newly downloaded wallet prompts wrong version'
source_url: https://github.com/monero-project/monero-gui/issues/2810
author: caozi522
assignees: []
labels: []
created_at: '2020-03-18T21:34:08+00:00'
updated_at: '2020-05-08T13:50:16+00:00'
type: issue
status: closed
closed_at: '2020-05-08T13:50:16+00:00'
---

# Original Description
Connected daemon is not compatible with GUI.Please upgrade or connect to another daemon.

# Discussion History
## selsta | 2020-03-18T21:35:30+00:00
Please click on the two arrows in the bottom left corner to connect to a new node. Wait a minute and see if the message goes away. If not, restart the GUI and try again.

## caozi522 | 2020-03-18T21:39:00+00:00
I have tried many times and it has no effect

## selsta | 2020-03-18T21:54:15+00:00
Can you open main menu, go to “Change wallet mode” and select advanced mode? Then open your wallet, go to Settings -> Node, click on remote node and enter the following:

```
address: node.xmr.to
port: 18081
```

or alternatively

```
address: node.supportxmr.com
port: 18081
```

Does this work?

## caozi522 | 2020-03-18T21:58:31+00:00
> 您可以打开主菜单，转到“更改钱包模式”并选择高级模式吗？然后打开您的钱包，进入设置->节点，单击远程节点并输入以下内容：
> 
> ```
> address: node.xmr.to
> port: 18081
> ```
> 
> 或者
> 
> ```
> address: node.supportxmr.com
> port: 18081
> ```
> 
> 这样行吗？

How to modify the address and port I did not find where to modify
http://chuantu.xyz/t6/725/1584568733x2890212003.jpg

## selsta | 2020-03-18T22:01:08+00:00
<img width="1026" alt="Screenshot 2020-03-18 at 22 59 32" src="https://user-images.githubusercontent.com/7697454/77011522-57e17800-696c-11ea-941e-36ecced5a251.png">


# Action History
- Created by: caozi522 | 2020-03-18T21:34:08+00:00
- Closed at: 2020-05-08T13:50:16+00:00
