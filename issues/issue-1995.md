---
title: monero-gui transfer too long time
source_url: https://github.com/monero-project/monero-gui/issues/1995
author: vae520283995
assignees: []
labels: []
created_at: '2019-03-07T09:49:45+00:00'
updated_at: '2019-03-30T11:09:19+00:00'
type: issue
status: closed
closed_at: '2019-03-28T08:42:57+00:00'
---

# Original Description
when I transfer always show me creating transaction
Have been waiting for

# Discussion History
## roy500 | 2019-03-07T09:57:43+00:00
me too ! I have the same problem ! 

## vae520283995 | 2019-03-07T10:09:43+00:00
my version is monero-gui-v0.13.0.4

## sanderfoobar | 2019-03-07T13:11:40+00:00
1. How much time does waiting for a transfer take?
2. Please share OS/distro details
3. Please share hardware details (CPU/memory)

## vae520283995 | 2019-03-08T01:32:40+00:00
> 1. How much time does waiting for a transfer take?
> 2. Please share OS/distro details
> 3. Please share hardware details (CPU/memory)

@xmrdc 
hello
1.Sometimes three minutes and sometimes a few seconds
2.win7 64bit 
3.intel i3-8100 3.60GHz  ram 8.00GB
other I can't transfer money continuously. I have to wait for confirmation.

## erciccione | 2019-03-08T12:18:32+00:00
I think the issue experienced here is the time that pass between you hit "send" and when you are asked to confirm. I too noticed in the last versions can take few minutes before receiving the confirmation of the transfer, it wasn't this slow time ago.

FWI i experienced the issue on the CLI, didn't try with the GUI.

@vae520283995 are you using an SSD or a normal hard drive? that could be the key

## MoneroChan | 2019-03-09T03:46:02+00:00
@vae520283995 @roy500

**Solution / Workaround**
To speed up Transaction preparation on v0.13.0.4 and possible 0.14?)
This Solution has been tested to work when preparing a "Cold signing" transaction on a Slow Old HDD, but i think it should also work for normal transactions.

Example Process: 

- Step 1. Prepare a dummy transaction, e.g prepare to send 0.00001 XMR to yourself, but instead of sending funds, Click  'Create TX file.' instead (advanced options if it doesn't appear)

- This will force the GUI to bootstrap sync the transaction preparation process that goes on behind the scenes. Once TX file is created, just save it anywhere and delete it. 

- Your wallet transaction generator is Now in sync with the more recent blocks and can now prepare Transactions much faster from this point (at least for the next 10 minutes or so)

- You can now arrange your time critical transfer / exchange quickly.

- Example use case:  If you are doing a transfer to an XMR>BTC exchange with limited time-out periods, using this workaround reduces the "Preparing transaction" time by about 90% on a 160GB Old Seagate HDD, but only after the first dummy transaction is completed above. 

- So basically, do the Dummy Transaction above, and only then do the actual transfer. Not the other way round.

- Workaround only works for a few minutes. Once more blocks arrive, you may need to repeat this dummy transaction bootstrap.

- Save your own address in your address book so you can create the Dummy TX quickly.

Again, I can confirm this solution works with cold signing transactions on V0.13.0.4, but I haven't tested this with the newer 0.14 release yet.

Maybe one of the Dev's like @luigi1111 can advise why this workaround works? 

Maybe there can be a button to 'bootstrap' the transaction preparation without using this workaround.

Hope this helps.

## sanderfoobar | 2019-03-11T14:52:06+00:00
@vae520283995 I suspect same 'problem' is present in the CLI when creating transactions. Thus, I fear this is not an issue for GUI. Please verify you have the same wait times in the CLI while creating a transaction.

## vae520283995 | 2019-03-12T03:32:55+00:00
> @ vae520283995我怀疑在创建事务时CLI中存在相同的“问题”。因此，我担心这不是GUI的问题。创建事务时，请验证CLI中的等待时间是否相同。

@xmrdsc Yes, I call transfer with moneor-wallet-rpc as well.

## vae520283995 | 2019-03-12T03:33:31+00:00
> @ vae520283995 @ roy500
> 
> **解决方案/解决方法**
> 为了加快v0.13.0.4上的事务准备和可能的0.14？）
> 此解决方案在慢速旧硬盘上准备“冷签名”事务时已经过测试，但我认为它也适用于正常的事务。
> 
> 示例流程：
> 
> * 步骤1.准备虚拟交易，例如准备向自己发送0.00001 XMR，但不要发送资金，请单击“创建TX文件”。相反（高级选项，如果它没有出现）
> * 这将强制GUI引导同步在幕后进行的事务准备过程。创建TX文件后，只需将其保存在任何位置并将其删除即可。
> * 您的钱包交易生成器现在与更新的块同步，现在可以从这一点开始更快地准备交易（至少在接下来的10分钟左右）
> * 您现在可以快速安排您的时间关键转移/交换。
> * 示例用例：如果您正在转移到具有有限超时时间的XMR> BTC交换，则使用此解决方法可将160GB旧希捷硬盘上的“准备事务”时间减少约90％，但仅限于第一个虚拟机交易完成如上。
> * 所以基本上，做上面的虚拟交易，然后才进行实际转移。不是相反。
> * 解决方法仅适用于几分钟。一旦更多块到达，您可能需要重复此虚拟事务引导程序。
> * 将您自己的地址保存在地址簿中，以便快速创建虚拟TX。
> 
> 同样，我可以确认此解决方案适用于V0.13.0.4上的冷签名事务，但我还没有使用较新的0.14版本对此进行测试。
> 
> 也许像@ luigi1111这样的Dev 之一可以建议为什么这个解决方法有效？
> 
> 也许可以有一个按钮来“引导”事务准备而不使用此变通方法。
> 
> 希望这可以帮助。

thanks,i try

## MoneroChan | 2019-03-23T07:22:09+00:00
I can now Confirm my Above solution also works for 0.14. 


## vae520283995 | 2019-03-28T08:42:47+00:00
> 我现在可以确认我的上述解决方案也适用于0.14。

thank you very much

## MoneroChan | 2019-03-30T11:09:19+00:00
@erciccione maybe you can try this trick on CLI? 
See Issue 2045 https://github.com/monero-project/monero-gui/issues/2045  ?
I don't use CLI, so maybe it'll help you out.
i'm thinking the CLI equivalent would be to stop the Password field for the dummy transaction.

# Action History
- Created by: vae520283995 | 2019-03-07T09:49:45+00:00
- Closed at: 2019-03-28T08:42:57+00:00
