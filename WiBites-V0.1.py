# Wifi Biter is a dictionary generator program that uses a database of Router Make/Model
# combinations to give the you the exact Characters and Length you need to
# put in to Crunch and generate a dictionary for attacking wireless routers.
#
# Crunch is best utilized with Aircrack-ng by piping the output from Crunch into Aircrack-ng
# and letting it run. Please Note: This is password cracking, it is not like you see in the movies where
# this kind of thing is done in 10 seconds, this will possibly take days or weeks depending on the router.

import time

routers = {
    '2WIRExxx':' Length 10, Charset 0-9',
    '3MobileWiFi':'Length 8, Charset 0-9 a-z',
    '3Wireless-Modem-XXXX':'Length 8. Charset0-9 A-F, The first 4 digits are the same as on the SSID',
    'AOLBB-XXXXXX':'Length 8, Charset 0-9 A-Z',
    'AT###': 'Length 10, Charset 0-9',
    'belkin.xxx':'Length 8, Charset 2-9 a-f',
    'belkin.xxxx':'Length 8, Charset 0-9 A-F',
    'Belkin.XXXX':'Length 8, Charset 0-9 A-F',
    'Belkin_XXXXXX':'Length 8, Charset 0-9 A-F',
    'BigPondXXXXXX':'Length 10, Charset 0-9 A-F',
    'BOLT!SUPER 4G-XXXX':'Length 8, Last 4 Numbers of SSID + 4 Numbers',
    'BTHomeHub(1)-XXXX' : 'Length 10, Charset 0-9 a-f',
    'BTHomeHub(2)-XXXX' : 'Length 10, Charset 2-9 a-f',
    'BTHub3':'Length 10, Charset 2-9 a-f',
    'BTHub4':'Length 10, Charset 2-9 a-f',
    'BTHub5':'Length 10, Charset 2-9 a-f',
    'Digicom_XXXX':'Length 8, Charset 0-9 A-Z',
    'DJAWEB_#####':'Length 10, Charset 0-9',
    'Domino_XXXX':'Length 8, Charset 0-9 A-F',
    'E583x-xxxx':'Length 8, Charset 0-9',
    'E583x-xxxxx':'Length 8, Charset 0-9 A-F',
    'EasyBox-######':'Length 9, Charset 0-9 A-F',
    'EEBrightBox-XXXXXX':' 3 words, with hyphens in-between,Lengths 3-4-5 or any combination.',
    'FrontierXXXX':'Length 10, Charset 0-9',
    'INFINITUM####':'Length 10, Charset 0-9',
    'Linkem_XXXXXX':'Length 8, Charset 0-9',
    'MobileWifi-xxxx':'Length 8, Charset 0-9',
    'MYWIFI(EE)':' MYWIFI plus 4 Numbers',
    'ONOXXXX':'Length 10, Charset 0-9',
    'Orange-0a0aa0':'Length 8, Charset 0-9 a-f',
    'Orange-XXXX':'Length 8, Charset "2345679 ACEF"',
    'PLST':'PLSTWIFI + Last 5 digits of MAC Address',
    'PlusnetWireless-XXXXXX':'Length 10, Charset 0-9 A-F',
    'PLUSNET-XXXXXX':'Length 10, Charset 0-9 a-f',
    'Sitecom_XXXX':'Length 8, Charset 0-9 A-F',
    'SKYXXXXX':'Length 8, Charset A-Z',
    'SpeedTouchXXXXXX':'Length 10, Charset 0-9 a-f',
    'TALKTALK-XXXXXX':'Length 8, Charset 346789 A-Z',
    'TDC-####':'Length 9, Charset 0-9 a-f',
    'Tech_XXXXXXXX':'Lenght 8, Charset A-Z',
    'Technicolor-Router':'Length 10, Charset 0-9 A-F',
    'TelstraXXXXXX':'Length 10, Charset 0-9 A-F',
    'TELUSXXXX':'Length 10, Charset 0-9 a-f',
    'Thomson':'Length 10, Charset 0-9 A-F',
    'Thomson':'Length 10, Charset 0-9 a-f',
    'TIM_PN51T_XXXX':'Length 8, Charset 0-9, WPS PIN is 12345670',
    'TNCAP-XXXX':'Length 10, Charset 0-9 A-F',
    'TNCAPXXXXXX':'Length 10, Charset 0-9 A-F',
    'TP-LINK_######':'Length 8, Charset 0-9 A-F',
    'TRENDnetTEW-123ABC':'Length 11, Charset, First 3 digits in SSID(123 here) + 8 digits',
    'UNITE-XXXX':'Length 8, Charset 0-9',
    'UPCXXXXXXX':'Length 8, Charset A-Z',
    'Verizon MIFIXXXXXXXX':'Length 11, Charset 0-9',
    'virginmediaXXXXXX':'Length 8, Charset a-z (bar iol)',
    'VirginMobileMiFiXXXX XXX':'Length 11, Charset 0-9',
    'VMXXXXXXX-2G':'Length 8, Charset a-z (bar iol)',
    'VMXXXXXXX-5G':'Length 8, Charset a-z (bar iol)',
    'ZyXELXXXXXX':'Length 13/10, Charset 0-9 A-Z/ 0-9 A-F', }



print("Please Note: Not all Wifi Routers will be included, but if it is possible to find the correct CharSet we will add them.")
time.sleep(2)
def mainFuct():
    rName = raw_input("please enter router name: ")


    if rName in routers:
 	      print(routers[rName])
    elif rName == "?":
        print("To use Wifi-Biter enter the Router Name, but where number are in the router name replace them with 'X', For example;")
        print("Instead of 'TNCAP-1586' type 'TNCAP-XXXX'")
    else:
        print("Router is not in our database....")

def loopBack():
    x = 1
    while x == 1:
        mainFuct()

loopBack()

