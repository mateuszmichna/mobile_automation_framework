# Mobile Automation Framework

This framework is designed for all QAs who have possibility to write
automatic tests for mobile devices or emulator. It has some functions like:

``-tap``

``-drag and drop``

``-swipes``

``-send keys to field``

```-clear field```

``-make screenshot``

and built-it test case design.

It is based on [Page Object Pattern](https://selenium-python.readthedocs.io/page-objects.html) design in [Selenium](https://selenium-python.readthedocs.io/index.html).

Using this framework saves time that every tester usually spend on writing his own framework and test case design.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.
Please keep in mind that you have to get access to source code of application that would be tested - it would be build
on your mobile/emulator.
### Prerequisites

1. Before first use of this framework please install:

    [Appium Desktop](https://github.com/appium/appium-desktop)

    [Android Studio](https://developer.android.com/studio) - for Android purposes

    [XCode](https://developer.apple.com/xcode/) - for iOS purposes

2. Add Android SDK to [PATH](https://www.dev2qa.com/how-to-set-android-sdk-path-in-windows-and-mac/) (if Android)

3. Clone your project application's repo.

Setting Appium manuals could be find here:
1. [iOS emulators](http://appium.io/docs/en/drivers/ios-xcuitest-real-devices/)
2. [iOS real devices](http://appium.io/docs/en/drivers/ios-xcuitest-real-devices/)
3. [Android emulators and real devices](http://appium.io/docs/en/drivers/android-uiautomator2/)

### Installing

1. Clone this repository and open it in PyCharm.
2. Install requirements.

### How to use framework
Writing tests has following steps.

Create [desired capabilities](http://appium.io/docs/en/writing-running-appium/caps/) in Appium.
Copy them to main_settings.py

Now:
1. Make session in Appium Desktop to inspect your application like web DOM and copy selectors to 
elements that you're interested in.
2. For every new screen create new .py file in /project/pages/ - default page you can find in project repo.
3. Put selectors there and write functions that are using your elements (ex. taps).
4. Write your test case using unittest.TestCase design in /project/test_cases/. Test case example is included.
Just follow steps in default_test_case.py.

Do not be connected to the device in Appium Desktop while running test cases!

## Authors

* **Mateusz Michna** - feel free to contact

