---
title: Build error
source_url: https://github.com/monero-project/monero-gui/issues/4388
author: Querens
assignees: []
labels: []
created_at: '2024-12-22T15:35:38+00:00'
updated_at: '2024-12-22T22:25:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
/home/querens/Programs/monero-gui/monero/external/miniupnp/miniupnpc/listdevices.c: In function ‘add_device’:                                                                       
/home/querens/Programs/monero-gui/monero/external/miniupnp/miniupnpc/listdevices.c:60:24: error: implicit declaration of function ‘strdup’; did you mean ‘strcmp’? [-Wimplicit-fu   nction-declaration]                                                                                                                                                                 ������������
   60 |         elt->descURL = strdup(dev->descURL);                                                                                                                                
      |                        ^~~~~~                                                                                                                                               
      |                        strcmp                                                                                                                                               
/home/querens/Programs/monero-gui/monero/external/miniupnp/miniupnpc/listdevices.c:60:22: error: assignment to ‘char *’ from ‘int’ makes pointer from integer without a cast [-Wi   nt-conversion]                                                                                                                                                                      ������������
   60 |         elt->descURL = strdup(dev->descURL);                                                                                                                                
      |                      ^                                                                                                                                                      
make[3]: *** [monero/external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/build.make:79: monero/external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/listdevices.c.o] Error 1   
make[2]: *** [CMakeFiles/Makefile2:1574: monero/external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/all] Error 2 
make[2]: *** Waiting for unfinished jobs.... 
```
And some time after
```
make[1]: *** [Makefile:136: all] Error 2
make[1]: Leaving directory '/home/querens/Programs/monero-gui/build/release'
make: *** [Makefile:48: release] Error 2

```

# Discussion History
## selsta | 2024-12-22T22:25:09+00:00
Please see https://github.com/monero-project/monero/issues/9618#issuecomment-2543163149

# Action History
- Created by: Querens | 2024-12-22T15:35:38+00:00
