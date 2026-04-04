---
title: monero wallet keys file signature for photorec
source_url: https://github.com/monero-project/monero/issues/9015
author: jakbin
assignees: []
labels: []
created_at: '2023-10-08T08:55:28+00:00'
updated_at: '2023-10-08T14:22:53+00:00'
type: issue
status: closed
closed_at: '2023-10-08T14:22:53+00:00'
---

# Original Description
I have mistakenly deleted my monero wallet keys file. I try to recover it using photorec but photorec don't have signature for this file type. Please provide monero wallet keys file signature for photorec. So may be i can recover my monero wallet files.

or 

By following photorec documentation, i found this code 
```c
#if !defined(SINGLE_FORMAT) || defined(SINGLE_FORMAT_MONERO_KEYS)
#ifdef HAVE_CONFIG_H
#include <config.h>
#endif
#ifdef HAVE_STRING_H
#include <string.h>
#endif
#include <stdio.h>
#include "types.h"
#include "filegen.h"

/*@ requires valid_register_header_check(file_stat); */
static void register_header_check_MONERO_KEYS(file_stat_t *file_stat);

const file_hint_t file_hint_MONERO_KEYS = {
  .extension = "keys",
  .description = "Monero Wallet Keys File",
  .max_filesize = 3000,
  .recover = 1,
  .enable_by_default = 1,
  .register_header_check = &register_header_check_MONERO_KEYS
};

/*@
  @ requires valid_file_check_param(file_recovery);
  @ ensures  valid_file_check_result(file_recovery);
  @ assigns  *file_recovery_new;
  @*/
static void file_check_MONERO_KEYS(file_recovery_t *file_recovery)
{
  const unsigned char MONERO_KEYS_footer[FOOTER_SIZE] = {
    FOOTER_MAGIC_MONERO_KEYS
  };
  file_search_footer(file_recovery, MONERO_KEYS_footer, sizeof(MONERO_KEYS_footer), FOOTER_EXTRA);
}

/*@
  @ requires valid_header_check_param(buffer, buffer_size, safe_header_only, file_recovery, file_recovery_new);
  @ ensures  valid_header_check_result(\result, file_recovery_new);
  @*/
static int header_check_MONERO_KEYS(const unsigned char *buffer, const unsigned int buffer_size, const unsigned int safe_header_only, const file_recovery_t *file_recovery, file_recovery_t *file_recovery_new)
{
  reset_file_recovery(file_recovery_new);
  file_recovery_new->extension = file_hint_MONERO_KEYS.extension;
  file_recovery_new->file_check = &file_check_MONERO_KEYS;
  return 1;
}

static void register_header_check_MONERO_KEYS(file_stat_t *file_stat)
{
  static const unsigned char MONERO_KEYS_header[HEADER_SIZE] = {
    HEADER_MAGIC_MONERO_KEYS
  };
  register_header_check(HEADER_LOC, MONERO_KEYS_header, sizeof(MONERO_KEYS_header), &header_check_MONERO_KEYS, file_stat);
}
#endif
```

I don't have these tow values for code `FOOTER_MAGIC_MONERO_KEYS` and `HEADER_MAGIC_MONERO_KEYS`.

# Discussion History
# Action History
- Created by: jakbin | 2023-10-08T08:55:28+00:00
- Closed at: 2023-10-08T14:22:53+00:00
