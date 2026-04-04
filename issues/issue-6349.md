---
title: VARIANT1_1 input and output values
source_url: https://github.com/monero-project/monero/issues/6349
author: jeandudey
assignees: []
labels: []
created_at: '2020-02-21T02:40:30+00:00'
updated_at: '2020-02-21T14:40:05+00:00'
type: issue
status: closed
closed_at: '2020-02-21T14:40:05+00:00'
---

# Original Description
I know this is only for `variant = 1` but actually interesting.

`VARIANT1_1` access only the 11th byte of the byte-buffer it gets passed, only that byte is modified, this is used in several places on the code. 

The issue: none, confusion maybe. It just happens for this to be true, i don't know the purpose of the code since it not does much:

```c
    uint8_t long_state = malloc(sizeof(uint8_t) * 12);
    for (int i = 0; i < 255; i++) {
        long_state[11] = i;
        VARIANT1_1(&long_state);
        assert(long_state[11] == i); // This demonstrates that VARIANT1_1 does nothing on that byte
    }
```

That code assumes that a variable `variant = 1` exists in the code.

<details>
  <summary>Small example</summary>

  ```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#include <time.h>

#define VARIANT1_1(p) \
  do if (variant == 1) \
  { \
    const uint8_t tmp = ((const uint8_t*)(p))[11]; \
    static const uint32_t table = 0x75310; \
    const uint8_t index = (((tmp >> 3) & 6) | (tmp & 1)) << 1; \
    ((uint8_t*)(p))[11] = tmp ^ ((table >> index) & 0x30); \
  } while(0)

int main(int argc, char **argv) {
    /* Variant 1 */
    int variant = 1;
    uint8_t *long_state = NULL;
    uint8_t v = 0;

    long_state = malloc(sizeof(uint8_t) * 12);

    for (int i = 0; i < 255; i++) {
        long_state[11] = i;
        VARIANT1_1(&long_state);
        printf("%02x -> %02x\n", i, long_state[11]);
        assert(long_state[11] == i);
    }

    free(long_state);

    return 0;
}
  ```
 
</details>

This can be demonstrated with a small Python example (matches current implementation):

```python
def variant1_1(p):
    tmp = p[11]
    table = 0x75310
    index = (((tmp >> 3) & 6) | (tmp & 1)) << 1
    return tmp ^ ((table >> index) & 0x30)

arr = [0,0,0,0,0,0,0,0,0,0,0,0xCF];
print("not changed: {}".format(variant1_1(arr) == 0xCF))
```

# Discussion History
## moneromooo-monero | 2020-02-21T12:08:10+00:00
I've tried your python example, and it gets modified in 192/256 cases. Also a quick C program shows the value is modified. Maybe I'm misunderstanding what you're saying though.

# Action History
- Created by: jeandudey | 2020-02-21T02:40:30+00:00
- Closed at: 2020-02-21T14:40:05+00:00
