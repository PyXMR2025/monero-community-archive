---
title: Can't create cold transaction!
source_url: https://github.com/monero-project/monero/issues/9078
author: developergames2d
assignees: []
labels:
- question
- low priority
created_at: '2023-11-28T13:58:47+00:00'
updated_at: '2024-01-02T15:45:57+00:00'
type: issue
status: closed
closed_at: '2024-01-02T15:45:57+00:00'
---

# Original Description
1. I exported exits to file from only-view wallet.
2. I opened the same cold wallet on computer without network and tap on "import exits". But it prints error "Failed to import outputs: Failed to import outputs: Hot wallets cannot import outputs"!

How can I fix it?

# Discussion History
## selsta | 2023-11-28T14:44:52+00:00
Can you follow all the steps in this tutorial? It seems you did something wrong.

https://monerodocs.org/cold-storage/offline-transaction-signing/

## developergames2d | 2023-11-28T15:09:34+00:00
> Can you follow all the steps in this tutorial? It seems you did something wrong.
> 
> https://monerodocs.org/cold-storage/offline-transaction-signing/

Is it necessarily use CLI? I used gui-v0.18.3.1...

## selsta | 2023-11-28T17:16:21+00:00
You can also use the GUI. "Hot wallets cannot import outputs" means that your wallet was at some point connected to a node, meaning it's not a cold wallet anymore but a hot wallet. This can happen if you copy the wallet file.

## developergames2d | 2023-11-28T19:31:09+00:00
> You can also use the GUI. "Hot wallets cannot import outputs" means that your wallet was at some point connected to a node, meaning it's not a cold wallet anymore but a hot wallet. This can happen if you copy the wallet file.

What do I need to do? Delete this wallet and restore it from the SEED without connecting to the network?

## selsta | 2023-11-29T03:13:41+00:00
Generally a cold wallet should have been created on a computer without internet connection in the first place.

If you still want to use this wallet then yes you have to restore from seed without connecting to the internet, but it would be preferable to create a new wallet that was never connected to the internet.

## developergames2d | 2023-11-29T08:59:18+00:00
> Generally a cold wallet should have been created on a computer without internet connection in the first place.
> 
> If you still want to use this wallet then yes you have to restore from seed without connecting to the internet, but it would be preferable to create a new wallet that was never connected to the internet.

I have a new problem: I could to import exits and export keys, but when I launch view-only wallet and connect to remote daemon, the button "import" for keys is non-clickable.
![image](https://github.com/monero-project/monero/assets/106807841/561f7376-3cdd-46ff-b59e-dde23d669f77)

After I try to transfer coins without keys, and it worked...


## developergames2d | 2023-11-29T10:22:50+00:00
Напишу по-русски:
Я вообще не понимаю, зачем нужны ключи. Отправить можно так:
1. Для сгенерированного кошелька взять адрес, private view key и высоту блока.
2. Создать кошелёк только для просмотра с этими параметрами в Monero gui.
3. Во вкладке "Отправить" ввести адрес, сумму и комиссию.
4. Нажать "Оффлайн подпись транзакций"->Создать и сохранить файл "SIGN".
5. На компьютере без сети восстановить сгенерированный кошелёк из SEED или открыть восстановленный.
6. Нажать "Оффлайн подпись транзакций"->Подписать(оффлайн) и выбрать файл "SIGN". В папке должны добавиться файлы "SIGN_signed_keyImages" и "SIGN_signed".
7. Открыть онлайн кошелёк только для просмотра.
8. Во вкладке Отправить нажать "Оффлайн подпись транзакций"->Отправить и выбрать файл "SIGN_signed". Монеты должны отправиться.

Причём после последнего действия мне выскакивает сообщение об ошибке, но монеты все равно отправляются. Я так и не понял, зачем нужен экспорт/импорт выходов и ключей, и зачем эти пункты в инструкции.

## selsta | 2023-11-29T14:47:25+00:00
You have to set your remote node as a trusted daemon to import key images.

## developergames2d | 2023-11-29T17:50:04+00:00
> You have to set your remote node as a trusted daemon to import key images.

This was done: see left-down data on the screenshot, I used remote node.

## selsta | 2023-11-29T17:51:29+00:00
Yes, you are connected to a remote node but the screenshot doesn't show if you marked the remote mode as a trusted node. You can do that in the remote node settings.

## developergames2d | 2023-11-29T17:58:11+00:00
> Yes, you are connected to a remote node but the screenshot doesn't show if you marked the remote mode as a trusted node. You can do that in the remote node settings.

Okay, I'll try later, but I don't understand now why do this if the coins are sent without import/export keys and exits. As I wrote in 9078#issuecomment-1831613572 all works with using only creating sign-file online, signing this file offline and broadcasting signed file to mempool online.

## selsta | 2023-11-29T18:08:58+00:00
Your comment is in Russian, I didn't fully understand it. I think importing key images is only necessary after you sent a transaction, if you only had received transactions then you don't have any key images to import.

# Action History
- Created by: developergames2d | 2023-11-28T13:58:47+00:00
- Closed at: 2024-01-02T15:45:57+00:00
