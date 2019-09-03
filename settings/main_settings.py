import os
from pathlib import Path

ROOT_DIR = str(Path(__file__).parent.parent)
ROOT_DIR_FORWARD_SLASH_SEPARATOR = ROOT_DIR.replace(os.sep, '/')

IMPLICITLY_WAIT = 20  # default time of waiting for elements before every driver.find_by method

"""
Desired Capabilities are keys and values encoded in a JSON object, sent by Appium clients to the server when
a new automation session is requested. They tell the Appium drivers all kinds of important things about how you want
your test to work. Each Appium client builds capabilities in a way specific to the client's language, but at the end
of the day, they are sent over to Appium as JSON objects.
"""

"""iOS specific"""
IOS_DEV_GROUP = ""  # your Apple developer group
IOS_SIGNING_ID = ""  # your Apple ID
IOS_BUNDLE_ID = ""  # bundle of iOS application
IOS_UDID = ""  # udid of the device
IOS_DRIVER = "XCUITest" # which automation engine to use (XCUITest for iOS)

"""Android specific"""
ANDROID_DRIVER = 'UiAutomator2' # which automation engine to use (UiAutomator2 for Android)

"""Both"""
PLATFORM = ""  # platform of device
DEVICE = ""  # name of the device
APP_PATH = ""  # the absolute local path or remote http URL to a .ipa file (IOS), .app folder (IOS Simulator)
SYSTEM_VERSION = ""  # device system version
NO_RESET = ""  # if False then after session start app will be reinstalled
WAIT_FOR_COMMAND = ""  # in sec, after this time with no command, session terminates
WAIT_FOR_QUIESCENCE = ''  # when False skips UI tests and speeds up building app
SERVER_ADDRESS = "http://localhost:4723/wd/hub"  # Appium server IP

IOS_CAPABILITIES = {
           "xcodeOrgId": IOS_DEV_GROUP,
       "xcodeSigningId": IOS_SIGNING_ID,
         "platformName": PLATFORM,
           "deviceName": DEVICE,
             "bundleID": IOS_BUNDLE_ID,
                  "app": APP_PATH,
       "automationName": IOS_DRIVER,
                 "udid": IOS_UDID,
      "platformVersion": SYSTEM_VERSION,
              "noReset": NO_RESET,
    "newCommandTimeout": WAIT_FOR_COMMAND,
    "waitForQuiescence": WAIT_FOR_QUIESCENCE
    }

ANDROID_CAPABILITIES = {
     "platformName": PLATFORM,
  "platformVersion": SYSTEM_VERSION,
       "deviceName": DEVICE,
              "app": APP_PATH,
   "automationName": ANDROID_DRIVER
}

DESIRED_CAPABILITIES = None   # None by default - should be ANDROID_CAPABILITIES or IOS_CAPABILITIES

