---
title: How to decode the ZMQ data
source_url: https://github.com/monero-project/monero/issues/8233
author: White2001Offl
assignees: []
labels: []
created_at: '2022-04-01T15:51:24+00:00'
updated_at: '2023-08-09T00:07:07+00:00'
type: issue
status: closed
closed_at: '2023-08-09T00:07:06+00:00'
---

# Original Description
Hi, I wanna know how to decode the ZMQ data i.e., `json-full-chain_main` and `json-full-txpool_add`
like to get TXN hash , sender , receiver address and amount 
and the block hash

I searched everywhere but unable to find out
there is not even a docs to do

```
json-full-txpool_add:[{"version":2,"unlock_time":0,"inputs":[{"to_key":{"amount":0,"key_offsets":[43255423,4282010,493445,155113,1101181,463783,979500,31375,13137,1191,7055],"key_image":"8f3ace349087c6949e95c378de7ff7e115018a78fe019814f17f8f7197da1b9a"}},{"to_key":{"amount":0,"key_offsets":[48216780,213697,1871618,72799,222675,99318,795,13510,44345,8939,16938],"key_image":"3fca90f8dc1a70bf33b1a4fc9fae608cc8b4e5cdf5999aa216816d067cd8f43f"}}],"outputs":[{"amount":0,"to_key":{"key":"d09e23385de4edeebb8a79ecad7cd9a87fd44fa38771e9ad50e521234604eb47"}},{"amount":0,"to_key":{"key":"f9742c2fa73bc8dc5ef93439b1a6560b737c4c9481f1d92ebd66e165725c058b"}}],"extra":"017106843e6390069e59090f152a26676138432e63a58a6e90dd74f1c80d1bf9e6020901cc96e76797c1acf3","signatures":[],"ringct":{"type":5,"encrypted":[{"mask":"0000000000000000000000000000000000000000000000000000000000000000","amount":"995335cf02ed9001000000000000000000000000000000000000000000000000"},{"mask":"0000000000000000000000000000000000000000000000000000000000000000","amount":"55c2e8b9937dfe90000000000000000000000000000000000000000000000000"}],"commitments":["ff5adb15899ed7d9f2857358fe52cdf215a5dfe4c663a6bb179775b5cee381f5","ab975cf575ea9495f32f01f90b7a7ddab08cad309c5afd03ca9afe0a8d7c1c21"],"fee":8660000,"prunable":{"range_proofs":[],"bulletproofs":[{"V":["d7f1b5b25ccf5a24864b20c5432b0956629efd31a414f3f96e8865a649adee1f","a00176380f30ba58d8dac8664912dc71b7f04516293b5733f7090c2186ac1ead"],"A":"52078e7ef13c0f79f4255f0d8b24bb0ea946af2963d9b8de13b4f02eb5740ddb","S":"d4e84d424e8ce0ac49b5f3c307d8955e857998c1139d7a34db2a5828d6b650d9","T1":"69149118bb88e4e1ac6fe56b1771429dd143bf28c6165d9c8883f4081648f7e7","T2":"3fb6cf222b8a80c69629774fc81a166563e83d761a19c2c7d52d13188104f533","taux":"4ff18f52ea228c2341ede6353e0bab851139b051da9a6b62f85c9c5a4255100b","mu":"b54063a08d1de8cf00a2da7d6ee530b990b40413da809030ac7f7309022c0808","L":["01a962790c3fdc13c41cf1df1dac213cf4a02aed963733a111d0511ecfa7a847","bcfe51ad18d3508b1d42010f891eba758d7420ee0bc16c105a77e7c85fe005cb","457d1e908a853dd20ae2cab7870989aed25415d8ecd9d426c325e77d2d0d7628","fac5d14bdc27d011ea0e89efc2eb4e8e1f0ed6ccc98f783b6cb144e3e3bd386e","5f3f51deb22207a0f938fb3e6f4274e99736c403a1524425d7eceaaf9dece2b3","b915693b459b828f06bcfdd335f4884bf39301810af8c072eee164f67ef50749","e2414e135a35d5094cfe33fef694583bccb31367d0d412f4ee185ae756bb405d"],"R":["25a2da3ca05ed4cedb6f91e3a8ff86078d40a151a270adace9de197fded09f22","847c8ff7513894ba23ecd4e8c34114f6f526b6de0c0717e3b3ff7505a1205590","2b0dd4eeb839ac1cc3d0bf85acd9975a2eab820df1805671233a344e44df576c","f630155d900f98d65718b21d319cde03314addd60ebc6095210b2aaf08e70240","5f17e3cbfe99bc66d938245ee0efc2871689a0719addc28732b56b3caf24ead5","71c70a902fc40c05d3a99b0b03b1e655fad6def93ce6f493db913c3675672e19","8249bdafaebf68972925a1e947b63713f03202f9802a8b3db25d07cb7eac3c32"],"a":"43bc9c44912ecc1d6cf6f877af6f418d8c63892fb831bc0df958a81424f39205","b":"16ff6429b74f59285405bcea241672e6898528baf15b877e33bd28c5e3e0710d","t":"5a4443f85632b8446b2e48b294e974054769f3116b189c7981a34dcf84769c0a"}],"mlsags":[],"pseudo_outs":["4db5ffbc7f985ef985de99febd3ee0f22e466acc4c8ec40214aa5b6fa2883775","6199e2cf624ad88e5740a43e06fea204ba6879240c64c71e695979de736b6834"]}}}]
```

This is the data I get in ZMQ.

Thanks

# Discussion History
## selsta | 2022-04-02T01:32:40+00:00
ZMQ does have some basic documentation here: https://github.com/monero-project/monero/blob/master/docs/ZMQ.md

Also did you see sech1's reply on IRC?

```
Mar 30 16:35:53 <white2001[m]>	hi guys
Mar 30 16:36:09 <white2001[m]>	can anyone help me to decode the zmq data
Mar 30 16:36:20 <white2001[m]>	I'm searching in internet for 4 days
Mar 30 16:36:40 *	white2001[m] sent a code block: https://libera.ems.host/_matrix/media/r0/download/libera.chat/1a07ce07075bbec89187ceb032a3d548d5bc3bc2
Mar 30 16:37:26 <white2001[m]>	Here is the data I receive from zmq
Mar 30 16:37:26 <white2001[m]>	how can I decode and get txn hash , see amount and get the sender and receive address
Mar 30 17:02:38 <bridgerton[m]>	<sech1> amount, sender and receive address? Sir, this is Monero
Mar 30 17:06:45 <bridgerton[m]>	<sech1> to get txn hash, subscribe to json-minimal-txpool_add
```

## White2001Offl | 2022-04-02T04:20:41+00:00
@selsta yeah, but I wanna get the inputs and output address with amount. Basically I'm trying to build a payment gateway for monero, And the input , output decode from ZMQ makes my work easy. Is there any way?
If not how can I get the inputs and outputs from txn hash. I tried RPC call but I'm failing idk if docs wrong or I am?


## SChernykh | 2022-04-02T07:34:47+00:00
Addresses and amounts are hidden in Monero. For payment gateways to work, you have to use viewkey + 1 subaddress for each payment - then you can see how much and when each of subaddresses received. But it can only be done with RPC calls.

## White2001Offl | 2022-04-02T15:31:32+00:00
@SChernykh which RPC call I've to use?
/get_transactions ?
If so I tried by running `monero-wallet-rpc` by setting port and wallet dir
but when I make a request

```
curl http://127.0.0.1:28088/json_rpc -d '{"jsonrpc": "2.0","id": "0", "method": "'get_transactions'", "params": '"{\"txs_hashes\": [\"c1aad1558a9e2a93b10ec30859afbbb4eb540bb64c0884e82916146ebb8e463c\"]}"'}' -H 'Content-Type: application/json'
{
  "error": {
    "code": -32700,
    "message": "Parse error"
  },
  "id": 0,
  "jsonrpc": "2.0"
}curl: (6) Could not resolve host: 2.0,id
curl: (6) Could not resolve host: 0,
curl: (6) Could not resolve host: method
curl: (6) Could not resolve host: 'get_transactions',
curl: (6) Could not resolve host: params
curl: (3) [globbing] nested brace in column 17
curl: (6) Could not resolve host: application
```

I get this error

## White2001Offl | 2022-04-02T20:12:05+00:00
ok I get it now how all works.
only think i wanna know is how can I decode the out and in address and amount data so that I can verify If the address is received or not and how much it received


## selsta | 2023-08-09T00:07:06+00:00
You can't get the addresses from ZMQ data, please re-read the previous comments.

# Action History
- Created by: White2001Offl | 2022-04-01T15:51:24+00:00
- Closed at: 2023-08-09T00:07:06+00:00
