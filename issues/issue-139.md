---
title: '"This app can’t run on your PC" when running Debug - Windows 10'
source_url: https://github.com/xmrig/xmrig/issues/139
author: ranbuch
assignees: []
labels: []
created_at: '2017-10-06T09:15:43+00:00'
updated_at: '2018-02-23T21:17:43+00:00'
type: issue
status: closed
closed_at: '2018-02-23T21:17:43+00:00'
---

# Original Description
When I'm trying to run the program in debug `\build\debug\xmrig.exe` I'm getting this message:
![this-app-cant-run](https://user-images.githubusercontent.com/3777546/31271152-add775c8-aa8f-11e7-8cc5-f62558333884.jpg)
In release it seems to work fine tough.

I've tried opening the CMD as Administrator but got the same result.

Any suggestions?

# Discussion History
## xmrig | 2017-10-06T09:21:37+00:00
What operation system did you use 64/32 bit.
Compiler MSYS/msvc (version?).
Where you get libuv from here https://github.com/xmrig/xmrig-deps ? or some place else.


## ranbuch | 2017-10-06T19:41:00+00:00
I use 64 bit with visual studio 2017 and I got my libuv from:
https://github.com/libuv/libuv
This is my Visual Studio info:


```Microsoft Visual Studio Community 2017 
Version 15.3.5
VisualStudio.15.Release/15.3.5+26730.16
Microsoft .NET Framework
Version 4.7.02046

Installed Version: Community

Visual Basic 2017   00369-60000-00001-AA705
Microsoft Visual Basic 2017

Visual C# 2017   00369-60000-00001-AA705
Microsoft Visual C# 2017

Visual C++ 2017   00369-60000-00001-AA705
Microsoft Visual C++ 2017

Visual F# 4.1   00369-60000-00001-AA705
Microsoft Visual F# 4.1

Application Insights Tools for Visual Studio Package   8.8.00712.1
Application Insights Tools for Visual Studio

ASP.NET and Web Tools 2017   15.0.30726.0
ASP.NET and Web Tools 2017

ASP.NET Core Razor Language Services   1.0
Provides languages services for ASP.NET Core Razor.

ASP.NET Template Engine 2017   15.0.30726.0
ASP.NET Template Engine 2017

ASP.NET Web Frameworks and Tools 2017   5.2.50601.0
For additional information, visit https://www.asp.net/

Azure App Service Tools v3.0.0   15.0.30728.0
Azure App Service Tools v3.0.0

Azure Data Lake Node   1.0
This package contains the Data Lake integration nodes for Server Explorer.

Azure Data Lake Tools for Visual Studio   2.2.9000.1
Microsoft Azure Data Lake Tools for Visual Studio

Azure Data Lake Tools for Visual Studio   2.2.9000.1
Microsoft Azure Data Lake Tools for Visual Studio

Common Azure Tools   1.10
Provides common services for use by Azure Mobile Services and Microsoft Azure Tools.

JavaScript Language Service   2.0
JavaScript Language Service

JavaScript Project System   2.0
JavaScript Project System

JavaScript UWP Project System   2.0
JavaScript UWP Project System

Merq   1.1.17-rc (cba4571)
Command Bus, Event Stream and Async Manager for Visual Studio extensions.

Microsoft Azure HDInsight Azure Node   2.2.9000.1
HDInsight Node under Azure Node

Microsoft Azure Hive Query Language Service   2.2.9000.1
Language service for Hive query

Microsoft Azure Stream Analytics Language Service   2.2.9000.1
Language service for Azure Stream Analytics

Microsoft Azure Stream Analytics Node   1.0
Azure Stream Analytics Node under Azure Node

Microsoft Azure Tools   2.9
Microsoft Azure Tools for Microsoft Visual Studio 2017 - v2.9.50719.1

Microsoft Continuous Delivery Tools for Visual Studio   0.3
Simplifying the configuration of continuous build integration and continuous build delivery from within the Visual Studio IDE.

Microsoft JVM Debugger   1.0
Provides support for connecting the Visual Studio debugger to JDWP compatible Java Virtual Machines

Microsoft MI-Based Debugger   1.0
Provides support for connecting Visual Studio to MI compatible debuggers

Microsoft Visual C++ Wizards   1.0
Microsoft Visual C++ Wizards

Microsoft Visual Studio VC Package   1.0
Microsoft Visual Studio VC Package

Mono Debugging for Visual Studio   Mono.Debugging.VisualStudio
Support for debugging Mono processes with Visual Studio.

Node.js Tools   1.0.0.0
Adds support for developing and debugging Node.js apps in Visual Studio

NuGet Package Manager   4.3.1
NuGet Package Manager in Visual Studio. For more information about NuGet, visit http://docs.nuget.org/.

SQL Server Data Tools   15.1.61707.200
Microsoft SQL Server Data Tools

ToolWindowHostedEditor   1.0
Hosting json editor into a tool window

TypeScript   2.3.4.0
TypeScript tools for Visual Studio

Visual Studio Code Debug Adapter Host Package   1.0
Interop layer for hosting Visual Studio Code debug adapters in Visual Studio

Visual Studio Tools for Apache Cordova   15.108.00.01
Visual Studio Tools for Apache Cordova

Visual Studio tools for CMake   1.0
Visual Studio tools for CMake

Visual Studio Tools for Unity   3.3.0.2
Visual Studio Tools for Unity

Visual Studio Tools for Universal Windows Apps   15.0.26730.08
The Visual Studio Tools for Universal Windows apps allow you to build a single universal app experience that can reach every device running Windows 10: phone, tablet, PC, and more. It includes the Microsoft Windows 10 Software Development Kit.

WebJobs Tools v1.0.0   __RESXID_PRODUCTVERSION__
WebJobs Tools v1.0.0

Xamarin   4.7.9.45 (bd7e3753c)
Visual Studio extension to enable development for Xamarin.iOS and Xamarin.Android.

Xamarin.Android SDK   7.4.5.1 (fb018c5)
Xamarin.Android Reference Assemblies and MSBuild support.

Xamarin.iOS and Xamarin.Mac SDK   11.0.0.0 (152b654)
Xamarin.iOS and Xamarin.Mac Reference Assemblies and MSBuild support.

```

## xmrig | 2017-10-07T09:44:34+00:00
Probably you linking with dynamic libuv (dll file required) for debug build.
Thank you.

## 2010phenix | 2017-10-07T22:22:13+00:00
xmrig, ranbuch, maybe is Windows Defender? ;)

# Action History
- Created by: ranbuch | 2017-10-06T09:15:43+00:00
- Closed at: 2018-02-23T21:17:43+00:00
