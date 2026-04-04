---
title: Stealth Address Generation yielding 95 characters instead of 64
source_url: https://github.com/monero-project/monero/issues/5950
author: DrewGlinsman
assignees: []
labels:
- invalid
created_at: '2019-10-01T23:03:01+00:00'
updated_at: '2019-10-29T20:17:39+00:00'
type: issue
status: closed
closed_at: '2019-10-29T20:17:39+00:00'
---

# Original Description
Hey all, I've been trying to follow the Mastering Monero tutorial to generate a stealth address from code in C++ but my result is 95 characters when I think the actual stealth address is only supposed to be 64. 

Below is my code:
`    std::string str_spend_key = "omitted";

    cryptonote::network_type nettype = cryptonote::MAINNET;
    crypto::public_key public_spend_key;

    cryptonote::blobdata blob;
    epee::string_tools::parse_hexstr_to_binbuff(str_spend_key, blob);

    crypto::secret_key sc = *reinterpret_cast<const crypto::secret_key*>(blob.data());

    std::cout << "Private Spend Key : " << sc << std::endl;

    crypto::secret_key_to_public_key(sc, public_spend_key);

    std::cout << "Public Spend Key: " << public_spend_key << std::endl;

    std::string str_view_key = "omitted";

    cryptonote::blobdata blob2;
    epee::string_tools::parse_hexstr_to_binbuff(str_view_key, blob2);

    crypto::secret_key vc = *reinterpret_cast<const crypto::secret_key*>(blob2.data());

    std::cout << "Private View Key: " << vc << std::endl;

    crypto::public_key public_view_key;
    crypto::secret_key_to_public_key(vc, public_view_key);

    std::cout << "Public View Key: " << public_view_key << std::endl;

    cryptonote::account_public_address address {public_spend_key, public_view_key};

    std::string public_address;

    public_address = cryptonote::get_account_address_as_str(nettype, false, address);

    std::cout << "Denari Address: " << public_address << std::endl;

    account_base base;

    account_public_address p_address;

    base.create_from_keys(p_address, sc, vc);

    transaction tx_genesis;

    construct_miner_tx(0, 0, 0, 0, 0, base.get_keys().m_account_address, tx_genesis);

    std::string str_tx_key = "75d9a862861a421263263bdc0bd6305e0f65dc9dc9dd492d4b3fe756b0c5e302";
    cryptonote::blobdata blobtx;
    epee::string_tools::parse_hexstr_to_binbuff(str_tx_key, blobtx);

    crypto::secret_key txKey = *reinterpret_cast<const crypto::secret_key*>(blobtx.data());

    crypto::key_derivation derivation;

    generate_key_derivation(public_view_key, txKey, derivation);

    crypto::ec_scalar scalar;

    size_t index = 01;

    derivation_to_scalar(derivation, index, scalar);
    
    std::string strAddress = base.get_public_address_str(nettype);

    std::cout << "Stealth Address: " << strAddress << std::endl;`

Running the following code gives me the stealth address: 5MEVMzHpoxT15hYavW8cKy15s6q2GTJGP111111111111111111111113zdxkuGQ7q11eLBGTjcVkjfSVYv31gRM15JAgwa

# Discussion History
## moneromooo-monero | 2019-10-01T23:37:10+00:00
What is a stealth address ?

Anyway, 95 characters is the normal length of a Monero standard address expressed in base 58. The 11...11 string above hints that there's a lot of 0s in the underlying data being encoded, which is usually a mistake upstream.


## SomaticFanatic | 2019-10-07T13:49:39+00:00

Just FYI. We don’t have stealth addresses. We have subaddresses. 

## moneromooo-monero | 2019-10-07T20:58:59+00:00
Subaddresses are 95 characters long, so if that's what you're trying to build, it matches :)

## moneromooo-monero | 2019-10-10T12:46:59+00:00
If no further info, I'll close this soon.

## binaryFate | 2019-10-12T13:12:00+00:00
I think what @DrewGlinsman is trying to do, and means by "stealth address" is to generate a one-time destination. Hence the code involving a transaction key, calling `generate_key_derivation`, etc.

I do not see how it could work given that the last two lines are not using any of the previous results.

Anyway the confusion seems to be that an address should be used as the destination of an output. This is not the case, you do not need to involve any sort of address-formating code on the one-time-destination (which is just a public key).

## moneromooo-monero | 2019-10-24T18:01:47+00:00
ping for more info before I close.

## jonathancross | 2019-10-29T19:34:23+00:00
Seems safe to close.
This question is probably more appropriate for [monero.stackexchange.com](https://monero.stackexchange.com/) or IRC.

## moneromooo-monero | 2019-10-29T20:09:34+00:00
+invalid

# Action History
- Created by: DrewGlinsman | 2019-10-01T23:03:01+00:00
- Closed at: 2019-10-29T20:17:39+00:00
