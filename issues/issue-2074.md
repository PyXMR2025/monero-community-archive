---
title: xmrig compiling as dll
source_url: https://github.com/xmrig/xmrig/issues/2074
author: noname29
assignees: []
labels: []
created_at: '2021-02-01T11:43:26+00:00'
updated_at: '2026-03-21T07:10:55+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:17:44+00:00'
---

# Original Description
I really really need xmrig with a dll version. so far i downloaded the source and modified `xmrig.cpp` to this 


 ```
 extern "C"{
    __declspec(dllexport) void some();
  }
  
  
  
  void some(){
	  using namespace xmrig;
	  char **argvPass;
	  //argvPass[0] = "deneme.exe";
	  int argcPass = 1;	

    Process process(argcPass, argvPass);
    const Entry::Id entry = Entry::get(process);
    if (entry) {
        Entry::exec(process, entry);
    }
    App app(&process);

    int x = app.exec();
	
    printf(" %d is x \n", x);
}
```

Then i checked the windows build of xmrig and i used the

```
cmake .. -G "Visual Studio 16 2019" -A x64 -DXMRIG_DEPS=C:\Users\ahmetunbay\Desktop\memoryModule\xmrig-master\xmrigReal\xmrig-deps\msvc2019\x64 -DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE -DBUILD_SHARED_LIBS=TRUE

cmake --build . --config Release
```

i used these codes to compile the xmrig, if i remove `-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE` it compiles xmrig.dll but when i load `some` function with `GetProcAddress()` and load, it crashes run time directly at `Process:Process` from what i see, console just closes without printing anything. 

if i dont remove  `-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE`  the cmake returns `setlocal` error using visual studio and doesnt compile the dll. i disable uac and tried to set `cmake_install_path` but still didnt fix the error. From my understanding `-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE` is neeeded for the dll to run properly, but i cant compile it. I used to be able to do it many years ago. 

Can someone please try to steps i tried above to let me know the results. We really need a dll version of xmrig. Thank you

# Discussion History
## SChernykh | 2021-02-01T11:57:29+00:00
XMRig was never designed to run as DLL, there are probably too many things you'll need to fix.

## noname29 | 2021-02-01T12:18:38+00:00
not true, i ran it like this 1-2 years ago, completely fine. just now a few catch errors, i lost my earlier work. all i did was only a few steps. so again, you're completely wrong. 

## noname29 | 2021-02-01T12:25:48+00:00
it might be due to my reg configurations or something wrong with `cmake` someone must try it and confirm me

## SChernykh | 2021-02-01T12:27:54+00:00
I'm not wrong in saying that it was never tested as DLL because it wasn't intended to be a DLL. A lot has changed in 1-2 years - many new algorithms including RandomX were added, big parts of the code were refactored.

## noname29 | 2021-02-01T12:35:42+00:00
say but i'm sure not many changes are needed, something running as exe easily interpreted to dll like i did last time. it might even be something with my configuration settings, i will either get a new pc and try to compile like above or somehow fix it. i hope someone can try and help

## Aksana1981 | 2021-02-02T05:29:04+00:00
Hi noname29
I have solved this problem.
when you have interest, please tell me.


## Aksana1981 | 2021-02-03T05:29:27+00:00
Don't help him.. He is fake.

## snipeTR | 2021-02-05T21:58:49+00:00
ahmet kardeşim sen gerizekalımısın. kod baştan aşağı komple değiştirildi. eski şeylerin çoğu artık yok. dosya yapısı değişti donanım tanımlama değişti api sunucusu bile değişti.

## noname29 | 2021-04-18T08:28:19+00:00
> ahmet kardeşim sen gerizekalımısın. kod baştan aşağı komple değiştirildi. eski şeyleri

gerizekali pic degisirse degissin ne alakasi var, olay cozuldu alinayi siktim. Seni bulur sikerim gerizekali teoman bak bilmedigin islere burnunu sokma orospu cocugu. git once kodlama ogren sen

## noname29 | 2021-04-18T08:31:25+00:00
> ahmet kardeşim sen gerizekalımısın. kod baştan aşağı komple değiştirildi. eski şeylerin çoğu artık yok. dosya yapısı değişti donanım tanımlama değişti api sunucusu bile değişti.
api sunucusu diyo, mal misin oglum sen, kim soktu seni github a 


## IamJomm | 2023-07-06T13:10:46+00:00
how did you solve your problem?

## elfoteo | 2024-10-18T14:55:51+00:00
## Guide to Build XMRig as a DLL on Windows

### Step 1: Clone the Repository
Start by cloning the official XMRig repository and navigating into the project folder:

```bash
git clone https://github.com/xmrig/xmrig.git
cd xmrig
```

### Step 2: Fix Dependencies
Ensure all required dependencies are available, especially the UV libraries, so that the project compiles successfully as an `.exe`. You may need to install the necessary libraries (like `libuv`, OpenSSL, etc.) for XMRig if you haven't done so yet.

Once the project compiles successfully as an executable (`.exe`), you can proceed to convert it into a DLL.

### Step 3: Modify `CMakeLists.txt`
In the `CMakeLists.txt`, replace the `add_executable` directive with `add_library` to build a DLL instead of an executable.

#### Before:
```cmake
add_executable(${CMAKE_PROJECT_NAME} ${HEADERS} ${SOURCES} ${SOURCES_OS} ${HEADERS_CRYPTO} ${SOURCES_CRYPTO} ${SOURCES_SYSLOG} ${TLS_SOURCES} ${XMRIG_ASM_SOURCES})
```

#### After:
Make sure to add the `SHARED` parameter after `${CMAKE_PROJECT_NAME}`:

```cmake
add_library(${CMAKE_PROJECT_NAME} SHARED ${HEADERS} ${SOURCES} ${SOURCES_OS} ${HEADERS_CRYPTO} ${SOURCES_CRYPTO} ${SOURCES_SYSLOG} ${TLS_SOURCES} ${XMRIG_ASM_SOURCES})
```

This change builds the project as a shared library (DLL).

### Step 4: Modify `xmrig.cpp`
We need to modify `src/xmrig.cpp` to expose two functions that will be used to start and stop XMRig when it’s loaded as a DLL:

```cpp
#include "App.h"
#include "base/kernel/Entry.h"
#include "base/kernel/Process.h"

#ifdef _WIN32
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT
#endif

namespace xmrig {
    // Global variables to store process and app pointers
    Process* process = nullptr;
    App* app = nullptr;
}

extern "C" {

    DLL_EXPORT int xmrig_start(int argc, char** argv)
    {
        using namespace xmrig;

        // Create the process object with command-line arguments
        process = new Process(argc, argv);

        // Determine the entry point based on command-line arguments
        const Entry::Id entry = Entry::get(*process);
        if (entry) {
            // If entry is valid, execute and return
            return Entry::exec(*process, entry);
        }

        // Initialize the main application
        app = new App(process);

        // Start the XMRig application
        return app->exec();
    }

    DLL_EXPORT void xmrig_stop()
    {
        using namespace xmrig;

        // Properly stop the XMRig application
        if (app) {
            app->onConsoleCommand((char)3); // Simulate sending a CTRL+C
        }

        // Clean up memory
        delete app;
        app = nullptr;

        delete process;
        process = nullptr;
    }
}
```

### Explanation of Changes:
- **Global Variables**: `process` and `app` are now global to ensure proper cleanup when stopping XMRig.
- **`xmrig_start` Function**: Initializes the process, determines the correct entry point, and starts the XMRig app.
- **`xmrig_stop` Function**: Simulates a CTRL+C to gracefully stop the app, followed by cleanup of the allocated objects (`app` and `process`).

### Step 5: Build the DLL
With these changes, build the project again. It should now output `xmrig.dll` instead of an `.exe`.

---

### Additional Notes:
- Ensure that you have a working development environment on Windows with CMake and the necessary dependencies for XMRig.
- This guide assumes you are familiar with building CMake-based projects. If you're unfamiliar, you can refer to CMake’s official documentation or look for tutorials on setting up CMake on Windows.
- To test your DLL, you can write a small C++ program that loads `xmrig.dll` using `LoadLibrary()` and calls the exported functions (`xmrig_start()` and `xmrig_stop()`).

---


## jason-smith-01 | 2025-04-18T03:42:35+00:00
these functions dont end up inside the .dll. the instructions are incorrect.

## VladimirAndersonNew | 2026-03-21T07:06:31+00:00
Full solution is here: https://github.com/VladimirAndersonNew/xmrig-dll

# Action History
- Created by: noname29 | 2021-02-01T11:43:26+00:00
- Closed at: 2021-04-12T14:17:44+00:00
