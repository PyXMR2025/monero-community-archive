---
title: 'Put extra field in the protocol: enforce sorted TLV format (with restricted
  tags)'
source_url: https://github.com/monero-project/research-lab/issues/61
author: UkoeHB
assignees: []
labels: []
created_at: '2020-01-30T23:53:31+00:00'
updated_at: '2020-04-17T17:45:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero transactions have an extra field that is not verified (see this [stackexchange question](https://monero.stackexchange.com/questions/11888/complete-extra-field-structure-standard-interpretation) for all the details I could figure out about how it is actually used). So long as it's in the right part of the transaction structure, and does not force a tx outside the maximum tx weight, any kind of data may reside inside it. Moreover, there are no clear standards about how to implement those fields for tx construction.

A heuristics-based analysis of transactions' extra fields reveals a lot of so-called 'anonymity puddles', which are essentially fingerprints of different implementation methods. [Pools](https://usercontent.irccloud-cdn.com/file/g2Ms1LsZ/image.png) which use different size extra nonces to keep track of miners, and the sub-field sorting method ([1](https://moneroblocks.info/api/get_transaction_data/c9f438fbbcd2a2014f5be316c3870dd48e38b915811f0c13c4f98f8512c096d3) vs [2](https://moneroblocks.info/api/get_transaction_data/d2ad39f56fef490fd9e162c456ae82b0cf0176e13e2aa52bd417f3bfaedf99b1); standard implementation sorts using `sort_tx_extra()`), are clear examples. Thanks to [Noncesense Research Lab](https://noncesense-research-lab.github.io/) researchers Isthmus and N3ptune for their work investigating this problem.

It's important that the extra field remain open ended to maintain flexibility in the face of an unknown future. It's also important, in line with the Monero Project's interest in fungibility and privacy, that users only lose privacy because they choose to (opt-out privacy), and not because there is no clear anonymity pool. This proposal aims to retain the extra field's flexibility while also creating an environment for straightforward implementation consensus.

1. Interpret the extra field as a series of bytes with little endian order, index 0 to n-1 where n is the number of bytes in the field.
2. The bytes must comply with TLV ([Type-Length-Value](https://www.dialogic.com/webhelp/csp1010/8.4.1_ipn3/exsapi_quickref_tlv_-_introduction_to_tlvs.htm)) format. In essence, the first byte read is a type (if the byte equals 255, add the next byte to the type, and so on; this permits an arbitrary number of types), the second byte is a length (interpreted as a varint, so there may be multiple bytes to the length), and the third byte is the first byte of the value (the number of these value-bytes is equal to the length). The next byte after a value ends is interpreted as a type, and so on. If the final extra field byte isn't the final byte of a value, assuming the field was strictly parsed using these rules, then the transaction will be rejected.
3. The types must be sorted. This may require the most updates to in-the-wild implementations.
4. When implemented, reserve a set of types for the 'official protocol'. This accommodates current uses of the field, and potential future wide-scale uses of the field. These reserved types may have special rules, such as current types 0x01 (single public key, usually the transaction public key; no length since all pub keys are 32 bytes), 0x02 (extra nonce, used by miners in an arbitrary fashion that should be standardized, and for non-coinbase tx often contains an internal no-length type 0x01 for an 8-byte encrypted payment ID), and 0x04 (additional public keys, the length byte is instead the 'number of pub keys', and actual length is num_keys x 32). These public keys can be enforced by requiring that 8*key != I (I is identity, e.g. 0; 8 is the elliptic curve cofactor), and recording them in the field originally as (1/8) x key. It's a more controversial suggestion that doesn't align with industry-level usage of the format, but does allow shoehorning in historical use of the field.

# Discussion History
## UkoeHB | 2020-02-12T19:06:30+00:00
UPDATE

Here are some additional, minor thoughts, I had.
1. Reserve the first 32 tags for protocol-specific tags. This means all tags `0x0#`, and `0x1#` belong to the protocol.
2. Ban use of padding bytes `0x00` outside of fields.
3. Put encrypted payment IDs in type field `0x05` with non-declared length 8 (no length byte).
4. Mandate non-declared extra nonce length 32 (no more subfields, just `0x02` then 32 bytes similar to the public key tag `0x01`). Unencrypted payment IDs can still be supported by implementations that really want to, assuming minor changes to parsing.

## UkoeHB | 2020-02-12T23:00:40+00:00
Pseudo code for verifying a transaction has sorted TLV format.
[enforced_sorted_TLV_extrafield_pseudocode.txt](https://github.com/monero-project/research-lab/files/4494485/enforced_sorted_TLV_extrafield_pseudocode.txt)



UPDATE: added sorting, made check_extra_tags_found() O(N).
UPDATE2: fixed indexing. Note that to extend types and lengths beyond 254 I do a simple sum, but there may be more utility to encode them as varints.
UPDATE3: moved getting a value's length to a new function
UPDATE4: simplified code around getting types and lengths
UPDATE5: start extraIndex at -1
```
//Pseudocode for verifying enforced sorted TLV format in extra field


//---------------------------------------------------------------------------------
//cryptonote_config.h

#define HF_VERSION_BEGIN_ENFORCING_EXTRA_FIELD	13


//---------------------------------------------------------------------------------
//tx_extra_enforced.h

#define EXTRA_TAG_PADDING					0x00
#define EXTRA_TAG_TX_PUBLIC_KEY				0x01
#define EXTRA_TAG_EXTRA_NONCE				0x02
#define EXTRA_TAG_ADDITIONAL_PUBLIC_KEYS	0x04
#define EXTRA_TAG_ENCRYPTED_PAYMENT_ID		0x05

#define EXTRA_TAG_FIRST_UNRESTRICTED		0x20

//---------------------------------------------------------------------------------
//validate_protocol_expectations.cpp


namespace validate_consensus_protocol
{
	namespace transactions
	{
		function bool check_tx_semantic(transaction tx)
		{
			int current_hf_version{get_hf_version()};

			...

			//at one point the field was not enforced in any way, so there was no need to validate it
			if (current_hf_version >= HF_VERSION_BEGIN_ENFORCING_EXTRA_FIELD) then
				if !(extra_field::extra_field_format_is_valid(tx, current_hf_version)) then
					return false;

			...

			return true;
		}

		namespace extra_field
		{
			function bool check_extra_tags_found(unsigned intVector tags_found, transaction tx, int hf_version)
			{
				if (hf_version >= HF_VERSION_BEGIN_ENFORCING_EXTRA_FIELD) then
				{
					unsigned int num_outs{tx.num_outs};
					unsigned intVector count_tags[EXTRA_TAG_FIRST_UNRESTRICTED]; //initialize to all 0s

					for (int tags_foundIndex; tags_foundIndex = 0 to size(tags_found) - 1)
					{
						if (tags_found[tags_foundIndex] < EXTRA_TAG_FIRST_UNRESTRICTED) then
							count_tags[tags_found[tags_foundIndex]] += 1;
					}

					//should only be one lone tx public key
					if (count_tags[EXTRA_TAG_TX_PUBLIC_KEY] > 1) then
						return false;

					//should only be one lone extra nonce
					if (count_tags[EXTRA_TAG_EXTRA_NONCE] > 1) then
						return false;

					//should only be one lone extra tx public keys
					if (count_tags[EXTRA_TAG_ADDITIONAL_PUBLIC_KEYS] > 1) then
						return false;

					//should only be one lone encrypted payment ID
					if (count_tags[EXTRA_TAG_ENCRYPTED_PAYMENT_ID] > 1) then
						return false;
					else if (num_outs == 2) then
						//encrypted payment ID expected
						if !(count_tags[EXTRA_TAG_ENCRYPTED_PAYMENT_ID] == 1) then
							return false;
				}

				return true;
			}

			//get value/length and number of its bytes; if a byte is 255 then we add the next byte to it, and so on
			function unsigned int get_extra_field_value_or_length(const int &extraIndex, const byteVector &extra_field, unsigned int &num_bytes, const unsigned int& field_size)
			{
				unsigned int add_length{1};	//1 by default to force the while loop to start
				unsigned int value_length{0};

				//the '+ 1' is because we begin by looking at the byte next to our initial extra index
				while ((value_length % 255 == 0) && (add_length != 0) && (extraIndex + num_bytes + 1 < field_size))
				{
					num_bytes += 1;

					add_length = extra_field[extraIndex + num_bytes];
					value_length += add_length;
				}

				return value_length;
			}


			//all the rules around different restricted extra field types are here; return false for disallowed types or behaviors
			//updates extraIndex to land on the last byte of a value's field
			function bool pass_over_extra_field_value_length(int &extraIndex, unsigned int test_type, byteVector extra_field, unsigned int field_size, int hf_version)
			{
				if (hf_version >= HF_VERSION_BEGIN_ENFORCING_EXTRA_FIELD)
				{
					unsigned int type_length{0};
					unsigned int num_length_bytes{0};

					type_length = get_extra_field_value_or_length(extraIndex, extra_field, num_length_bytes, field_size);

					if (test_type < EXTRA_TAG_FIRST_UNRESTRICTED) then
					{
						switch(test_type)
						{
							case EXTRA_TAG_PADDING

								//padding bytes disallowed
								return false;
							
							case EXTRA_TAG_TX_PUBLIC_KEY

								if (num_length_bytes == 0) then
									return false;

								//the transaction public key is 32 bytes, and has no length byte
								extraIndex += 32;

							case EXTRA_TAG_EXTRA_NONCE

								if (num_length_bytes == 0) then
									return false;

								//the extra nonce is 32 bytes, and has no length byte
								extraIndex += 32;

							case EXTRA_TAG_ADDITIONAL_PUBLIC_KEYS

								if (num_length_bytes == 0) then
									return false;

								//the additional public keys is 32 bytes per key, and length is number of keys
								extraIndex += (32*type_length + num_length_bytes);

							case EXTRA_TAG_ENCRYPTED_PAYMENT_ID

								if (num_length_bytes == 0) then
									return false;

								//the encrypted payment ID is 8 bytes, and has no length byte
								extraIndex += 8;

							case else

								//other restricted tags disallowed
								return false;
						}
					}
					else
					{
						if (num_length_bytes == 0) then
							return false;

						//straightforward TLV is expected for all non-restricted types
						//+num_length_bytes moves index to position of last length byte, then value length moves to last byte of value
						extraIndex += (type_length + num_length_bytes);
					}
				}

				return true;
			}


			//enforced sorted TLV format
			function bool extra_field_format_is_valid(transaction tx, int hf_version)
			{
				if (hf_version >= HF_VERSION_BEGIN_ENFORCING_EXTRA_FIELD) then
				{
					byteVector extra_field{tx.extra};
					int extraIndex{-1};
					unsigned int field_size{size(extra_field)};
					unsigned intVector tags_found;
					unsigned int temp_type{0};
					unsigned int num_type_bytes{0};
					unsigned int prev_type{0};

					//loop ends when we land on the last byte (or go past the field size)
					while (extraIndex < field_size - 1)
					{
						//get type
						temp_type = get_extra_field_value_or_length(extraIndex, extra_field, num_type_bytes, field_size);

						//move extra index to last byte of the type
						extraIndex += num_type_bytes;

						//types should be in ascending order, duplicates are allowed at this stage
						if (temp_type < prev_type) then
							return false;

						//get length, and skip to the end of this type's value field; it returns false due to invalid types or when a length byte is expected but not found
						if !(pass_over_extra_field_value_length(extraIndex, temp_type, extra_field, field_size, hf_version)) then
							return false;

						tags_found.push_back(temp_type);

						//move on to the next type
						prev_type = temp_type;
					}

					//in case we have requirements around which tags should be in the field
					if !check_extra_tags_found(tags_found, tx, hf_version) then
						return false;

					//these only line up when TLV format is obeyed, i.e. when the last byte of the last type field is the last byte of the extra field
					return extraIndex == (field_size - 1);
				}

				return true;
			}
		}
	}
}
//---------------------------------------------------------------------------------
```

## Mitchellpkt | 2020-04-01T17:12:21+00:00
Here's what we've observed in practice, recently:

<img width="951" alt="image" src="https://user-images.githubusercontent.com/21246742/78165574-c14f9500-7408-11ea-8ae5-7d695b4321d3.png">

# Action History
- Created by: UkoeHB | 2020-01-30T23:53:31+00:00
