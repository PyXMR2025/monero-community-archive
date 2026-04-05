---
title: Compile issues
source_url: https://github.com/xmrig/xmrig/issues/835
author: Omnividente
assignees: []
labels: []
created_at: '2018-10-22T17:12:42+00:00'
updated_at: '2018-10-22T17:34:08+00:00'
type: issue
status: closed
closed_at: '2018-10-22T17:34:08+00:00'
---

# Original Description
I have problem when a compiling XMRIG
```
Серьезность	Код	Описание	Проект	Файл	Строка	Состояние подавления
Ошибка	LNK1257	эх єфрыюё№ ёючфрЄ№ ъюф	xmrig	C:\xmrig-master\build\LINK	1	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4390	";": обнаружен пустой контролируемый оператор; это правильно?	xmrig	c:\xmrig-master\src\3rdparty\rapidjson\prettywriter.h	225	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4267	=: преобразование из "size_t" в "ULONG"; возможна потеря данных	xmrig	c:\xmrig-master\src\common\net\client.cpp	882	
Предупреждение	C4390	";": обнаружен пустой контролируемый оператор; это правильно?	xmrig	c:\xmrig-master\src\3rdparty\rapidjson\writer.h	448	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4244	аргумент: преобразование "float" в "uint64_t", возможна потеря данных	xmrig	c:\xmrig-master\src\net\strategies\donatestrategy.cpp	74	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4267	=: преобразование из "size_t" в "uint32_t"; возможна потеря данных	xmrig	c:\xmrig-master\src\workers\multiworker.cpp	181	
Предупреждение	C4267	=: преобразование из "size_t" в "uint32_t"; возможна потеря данных	xmrig	c:\xmrig-master\src\workers\multiworker.cpp	184	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4267	return: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\core\config.h	84	
Предупреждение	C4390	";": обнаружен пустой контролируемый оператор; это правильно?	xmrig	c:\xmrig-master\src\3rdparty\rapidjson\prettywriter.h	225	
Предупреждение	C4267	аргумент: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\common\net\tls.cpp	91	
Предупреждение	C4267	аргумент: преобразование из "size_t" в "int"; возможна потеря данных	xmrig	c:\xmrig-master\src\common\net\tls.cpp	111	
Ошибка	C1047	╘рщы юс·хъЄр шыш сшсышюЄхъш "xmrig.dir\Release\NetworkState.obj" с√ы ёючфрэ ё сюыхх ёЄрЁющ тхЁёшхщ ъюьяшы ЄюЁр, ўхь фЁєушх юс·хъЄ√; т√яюыэшЄх чрэютю яюёЄЁюхэшх ёЄрЁ√ї юс·хъЄют ш сшсышюЄхъ	xmrig	C:\xmrig-master\build\LINK	1	

```
[http://fs1.directupload.net/images/181022/holkv54e.png](url)

# Discussion History
# Action History
- Created by: Omnividente | 2018-10-22T17:12:42+00:00
- Closed at: 2018-10-22T17:34:08+00:00
