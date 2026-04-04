---
title: ' E string len count value 10383 goes out of remain storage len 4432'
source_url: https://github.com/monero-project/monero/issues/8664
author: mubali1987
assignees: []
labels: []
created_at: '2022-12-03T15:11:11+00:00'
updated_at: '2022-12-03T20:25:18+00:00'
type: issue
status: closed
closed_at: '2022-12-03T20:25:18+00:00'
---

# Original Description
2022-12-03 14:45:33.096 E string len count value 10383 goes out of remain storage len 4432
2022-12-03 14:45:33.096 E Exception at [portable_storage::load_from_binary], what=string len count value 10383 goes out of remain storage len 4432
2022-12-03 14:45:42.093 E to big string len value in storage: 1397218431845233286
2022-12-03 14:45:42.094 E Exception at [portable_storage::load_from_binary], what=to big string len value in storage: 1397218431845233286
2022-12-03 14:45:48.188 W ge_frombytes_vartime failed at 457
2022-12-03 14:46:08.548 E string len count value 376890643 goes out of remain storage len 3597
2022-12-03 14:46:08.557 E Exception at [portable_storage::load_from_binary], what=string len count value 376890643 goes out of remain storage len 3597
2022-12-03 14:46:13.352 E unknown entry_type code = r
2022-12-03 14:46:13.352 E Exception at [portable_storage::load_from_binary], what=unknown entry_type code = r
2022-12-03 14:46:13.453 E string len count value 11166 goes out of remain storage len 5118
2022-12-03 14:46:13.453 E Exception at [portable_storage::load_from_binary], what=string len count value 11166 goes out of remain storage len 5118
2022-12-03 14:46:28.719 E  attempt to read 224 bytes from buffer with 34 bytes remained
2022-12-03 14:46:28.720 E Exception at [portable_storage::load_from_binary], what= attempt to read 224 bytes from buffer with 34 bytes remained
2022-12-03 14:47:04.450 E string len count value 15861 goes out of remain storage len 5972
2022-12-03 14:47:04.453 E Exception at [portable_storage::load_from_binary], what=string len count value 15861 goes out of remain storage len 5972
2022-12-03 14:47:06.741 E string len count value 14968 goes out of remain storage len 4393
2022-12-03 14:47:06.742 E Exception at [portable_storage::load_from_binary], what=string len count value 14968 goes out of remain storage len 4393
2022-12-03 14:47:19.223 E to big string len value in storage: 2486257080171393218
2022-12-03 14:47:19.234 E Exception at [portable_storage::load_from_binary], what=to big string len value in storage: 2486257080171393218
2022-12-03 14:47:23.104 E unknown entry_type code =
2022-12-03 14:47:23.106 E Exception at [portable_storage::load_from_binary], what=unknown entry_type code =
2022-12-03 14:47:24.464 E string len count value 13270 goes out of remain storage len 2224
2022-12-03 14:47:24.472 E Exception at [portable_storage::load_from_binary], what=string len count value 13270 goes out of remain storage len 2224
2022-12-03 14:49:49.452 E to big string len value in storage: 18014973891449351
2022-12-03 14:49:49.453 E Exception at [portable_storage::load_from_binary], what=to big string len value in storage: 18014973891449351
2022-12-03 14:50:27.894 E to big string len value in storage: 3310076586714118651
2022-12-03 14:50:27.904 E Exception at [portable_storage::load_from_binary], what=to big string len value in storage: 3310076586714118651
2022-12-03 14:50:37.692 E string len count value 13066 goes out of remain storage len 1528
2022-12-03 14:50:37.700 E Exception at [portable_storage::load_from_binary], what=string len count value 13066 goes out of remain storage len 1528
2022-12-03 14:50:41.690 E unknown entry_type code = ?
2022-12-03 14:50:41.691 E Exception at [portable_storage::load_from_binary], what=unknown entry_type code = ?
2022-12-03 14:50:45.489 E string len count value 752194326 goes out of remain storage len 4434
2022-12-03 14:50:45.490 E Exception at [portable_storage::load_from_binary], what=string len count value 752194326 goes out of remain storage len 4434
2022-12-03 14:50:58.167 E string len count value 830325072 goes out of remain storage len 1530
2022-12-03 14:50:58.168 E Exception at [portable_storage::load_from_binary], what=string len count value 830325072 goes out of remain storage len 1530
2022-12-03 14:51:01.117 W ge_frombytes_vartime failed at 454
2022-12-03 14:52:07.611 E string len count value 1041160684 goes out of remain storage len 3751
2022-12-03 14:52:07.612 E Exception at [portable_storage::load_from_binary], what=string len count value 1041160684 goes out of remain storage len 3751
2022-12-03 14:52:12.288 W ge_frombytes_vartime failed at 454

# Discussion History
## selsta | 2022-12-03T15:15:12+00:00
Do you have any issues apart from error / warning messages? it just means someone is sending you invalid data.

## mubali1987 | 2022-12-03T15:18:42+00:00
error 
2022-12-03 14:45:33.096 E string len count value 10383 goes out of remain storage len 4432
2022-12-03 14:45:33.096 E Exception at [portable_storage::load_from_binary], what=string len count value 10383 goes out of remain storage len 4432
2022-12-03 14:45:42.093 E to big string len value in storage: 1397218431845233286
2022-12-03 14:45:42.094 E Exception at [portable_storage::load_from_binary], what=to big string len value in storage: 1397218431845233286
2022-12-03 14:46:08.548 E string len count value 376890643 goes out of remain storage len 3597
2022-12-03 14:46:08.557 E Exception at [portable_storage::load_from_binary], what=string len count value 376890643 goes out of remain storage len 3597
2022-12-03 14:46:13.352 E unknown entry_type code = r
2022-12-03 14:46:13.352 E Exception at [portable_storage::load_from_binary], what=unknown entry_type code = r
2022-12-03 14:46:13.453 E string len count value 11166 goes out of remain storage len 5118
2022-12-03 14:46:13.453 E Exception at [portable_storage::load_from_binary], what=string len count value 11166 goes out of remain storage len 5118
2022-12-03 14:46:28.719 E  attempt to read 224 bytes from buffer with 34 bytes remained
2022-12-03 14:46:28.720 E Exception at [portable_storage::load_from_binary], what= attempt to read 224 bytes from buffer with 34 bytes remained
2022-12-03 14:47:04.450 E string len count value 15861 goes out of remain storage len 5972
2022-12-03 14:47:04.453 E Exception at [portable_storage::load_from_binary], what=string len count value 15861 goes out of remain storage len 5972
2022-12-03 14:47:06.741 E string len count value 14968 goes out of remain storage len 4393
2022-12-03 14:47:06.742 E Exception at [portable_storage::load_from_binary], what=string len count value 14968 goes out of remain storage len 4393
2022-12-03 14:47:19.223 E to big string len value in storage: 2486257080171393218
2022-12-03 14:47:19.234 E Exception at [portable_storage::load_from_binary], what=to big string len value in storage: 2486257080171393218
2022-12-03 14:47:23.104 E unknown entry_type code =
2022-12-03 14:47:23.106 E Exception at [portable_storage::load_from_binary], what=unknown entry_type code =
2022-12-03 14:47:24.464 E string len count value 13270 goes out of remain storage len 2224
2022-12-03 14:47:24.472 E Exception at [portable_storage::load_from_binary], what=string len count value 13270 goes out of remain storage len 2224
2022-12-03 14:49:49.452 E to big string len value in storage: 18014973891449351
2022-12-03 14:49:49.453 E Exception at [portable_storage::load_from_binary], what=to big string len value in storage: 18014973891449351
2022-12-03 14:50:27.894 E to big string len value in storage: 3310076586714118651
2022-12-03 14:50:27.904 E Exception at [portable_storage::load_from_binary], what=to big string len value in storage: 3310076586714118651
2022-12-03 14:50:37.692 E string len count value 13066 goes out of remain storage len 1528
2022-12-03 14:50:37.700 E Exception at [portable_storage::load_from_binary], what=string len count value 13066 goes out of remain storage len 1528
2022-12-03 14:50:41.690 E unknown entry_type code = ?
2022-12-03 14:50:41.691 E Exception at [portable_storage::load_from_binary], what=unknown entry_type code = ?
2022-12-03 14:50:45.489 E string len count value 752194326 goes out of remain storage len 4434
2022-12-03 14:50:45.490 E Exception at [portable_storage::load_from_binary], what=string len count value 752194326 goes out of remain storage len 4434
2022-12-03 14:50:58.167 E string len count value 830325072 goes out of remain storage len 1530
2022-12-03 14:50:58.168 E Exception at [portable_storage::load_from_binary], what=string len count value 830325072 goes out of remain storage len 1530
2022-12-03 14:52:07.611 E string len count value 1041160684 goes out of remain storage len 3751
2022-12-03 14:52:07.612 E Exception at [portable_storage::load_from_binary], what=string len count value 1041160684 goes out of remain storage len 3751
2022-12-03 15:12:03.304 E Failed to parse transaction from blob


## selsta | 2022-12-03T15:24:23+00:00
Same as here: https://github.com/monero-project/monero/issues/8630

Someone is sending your node invalid data and your node correctly ignored it. There are no issues as far as I can see.

# Action History
- Created by: mubali1987 | 2022-12-03T15:11:11+00:00
- Closed at: 2022-12-03T20:25:18+00:00
