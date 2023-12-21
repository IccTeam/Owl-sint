# Ngapain Deck? Mau Recode Ya
# Boleh Recode Tapi Tambahkan Author asli

# [+]-------------------------------------------[+]
#  | Creator : OwlBird05                         |
#  | Github : https://github.com/IccTeam         |
#  | Powered By Intelligence Cyber Community     |
# [+]-------------------------------------------[+]

### !/usr/bin/python3
#VERSION 1.2
#CREATED 2023 BY MR,OWLBIRD05
#CODED BY MR,OWLBIRD05
#CREDITS TO INTELLEGENCE CYBER COMMUNITY LEADER
                                               
try:
                 import time
                 import os
                 import sys
                 import requests
                 import re
                 import json
                 import urllib
                 import colorama
                 import instaloader
                 from time import sleep
                 from datetime import datetime
                 import phonenumbers as pnumb
                 from phonenumbers import parse
                 from phonenumbers import geocoder
                 from phonenumbers import carrier
                 from phonenumbers import timezone
                 from instaloader import instaloader
except ModuleNotFoundError:
                 print (f"Please Install Module First")
                 sys.exit()
### 14 modules

### colors
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[1;93m"
WHITE = "\033[1;97m"
NORMAL = "\033[0;37m"

OKGREEN = '\033[92m'
WARNING = '\033[93m'
YE = '\033[1;33m'
BOLD = '\033[1m'
ENDC = '\033[0m'

CRED2 = "\33[91m"
CBLUE2 = "\33[94m"
ENDC = "\033[0m"

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
### animation
def animation(s):
  for c in s + "\n":
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.0025)
     
### banner
def banner():
            animation (f"""
    {BLUE}░█████╗░░██╗░░░░░░░██╗██╗░░░░░░██████╗██╗███╗░░██╗████████╗   
    ██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██║████╗░██║╚══██╔══╝          
    ██║░░██║░╚██╗████╗██╔╝██║░░░░░╚█████╗░██║██╔██╗██║░░░██║░░░             
    ██║░░██║░░████╔═████║░██║░░░░░░╚═══██╗██║██║╚████║░░░██║░░░               
    ╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██████╔╝██║██║░╚███║░░░██║░░░                  
    ░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░                   
            Version 1.2 - 2023 coded by Mr,OwlBird05

         \033[91m[??] Choose an option:
         \033[91m[\033[93m1\033[91m] \033[1;97mPhone Number Information
         \033[91m[\033[93m2\033[91m] \033[1;97mTrack IP
         \033[91m[\033[93m3\033[91m] \033[1;97mInstagram User Information
         \033[91m[\033[93mA\033[91m] \033[1;97mAbout""")
def start():
      os.system("clear")
      banner()
      chose=input("           \033[94mChoose\033[0m: ")
      if chose == "1": ## MENU 1
        sleep(1)
        print(f"""
        \033[91m[\033[93m1\033[91m] \033[1;97mTrack Number V1
        \033[91m[\033[93m2\033[91m] \033[1;97mTrack Number V2
        \033[91m[\033[93m3\033[91m] \033[1;97mTrack Number V3""")
        V = input(f"      {BLUE}Choose\033[0m: ")
        if V == "1": ### chose 1
                    number = input(f"{WHITE}Enter Number {NORMAL}({GREEN}Without +){WHITE} :{CRED2}➤ ")
                    parsing = parse(number)
                    loc = geocoder.description_for_number(parsing,"id")
                    isp = carrier.name_for_number(parsing,"id")
                    tz = timezone.time_zones_for_number(parsing)
                    ### track number v1
                    print ()
                    sleep(0.1)
                    print(f"{YELLOW}International Format          {NORMAL}:",pnumb.normalize_digits_only(parsing))
                    sleep(0.1)
                    print(f"{YELLOW}National Format               {NORMAL}:",pnumb.national_significant_number(parsing))
                    sleep(0.1)
                    print(f"{YELLOW}Valid Number                  {NORMAL}:",pnumb.is_valid_number(parsing))
                    sleep(0.1)
                    print(f"{YELLOW}Can Be Internatioally Dialled {NORMAL}:",pnumb.can_be_internationally_dialled(parsing))
                    sleep(0.1)
                    print(f"{YELLOW}Location                      {NORMAL}:",loc)
                    sleep(0.1)
                    print(f"{YELLOW}Region Code For Number        {NORMAL}:",pnumb.region_code_for_number(parsing))
                    sleep(0.1)
                    print(f"{YELLOW}Number Type                   {NORMAL}:",pnumb.number_type(parsing))
                    sleep(0.1)
                    print(f"{YELLOW}Is Carrier Specific           {NORMAL}:",pnumb.is_carrier_specific(parsing))
                    sleep(0.1)
                    print(f"{YELLOW}ISP                           {NORMAL}:",isp)
                    sleep(0.1)
                    print(f"{YELLOW}Time Zone                     {NORMAL}:",tz)
                    sleep(0.1)
                    print('\n\033[1;93mWhatsApp Number               \033[0m: wa.me/' + number + ' \n')
                    sleep(0.1)
                    print(f"{YELLOW}Is Number Geographical        {NORMAL}:",pnumb.is_number_geographical(parsing))
                    print("")
                    sleep(1)
                    open = input(f"{WHITE}TYPE 1 To Open Chat Target on WhatsApp or press ENTER to next: ")
                    if open == "1" :
                           sleep(1)
                           print(f"{WHITE}Openned WhatsApp")
                           sleep(1)
                           sleep(1)
                           print(f"{NORMAL}Done")
                           sleep(0.50)
                           os.system('\nxdg-open http://wa.me/' + number + ' \n')
                           sleep(0.30)
                           print("")
                    elif open == "" :
                           print("")
                           sys.exit(1)
                    
                    
                    
####################
#CODED BY OWLBIRD05
#CONTACT ME +6283848301116
#OR YOU CAN DM MY INSTAGRAM @ICCFFICIAL
#NOTE: If you want to recode, don't forget to include the name of the tool developer
#CATATAN: Jika ingin kode ulang, jangan lupa cantumkan nama pengembang alat
####################
                    
                    
                    
        elif V == "2": ### chose 2
                      number = input(f"{WHITE}Enter Number {NORMAL}({GREEN}Without +){WHITE} :{CRED2}➤ ")
                      ### REQUESTS API
                      phe = requests.get("http://apilayer.net/api/validate?access_key=59198d04ba13167bd195d1e9ad73332f&number=" + number )
                      sleep(1)
                      print ()
                      sleep(0.1)
                      ### track number v2
                      print(f"{YELLOW}Valid                 {NORMAL}:{GREEN} " + str(phe.json() ['valid']))
                      sleep(0.1)
                      print(f"{YELLOW}Number                {NORMAL}: " + str(phe.json() ['number']))
                      sleep(0.1)
                      print(f"{YELLOW}Local Format          {NORMAL}: " + str(phe.json() ['local_format']))
                      sleep(0.1)
                      print(f"{YELLOW}International Format  {NORMAL}: " + str(phe.json() ['international_format']))
                      sleep(0.1)
                      print(f"{YELLOW}Country Prefix        {NORMAL}: " + str(phe.json() ['country_prefix']))
                      sleep(0.1)
                      print(f"{YELLOW}Country Code          {NORMAL}: " + str(phe.json() ['country_code']))
                      sleep(0.1)
                      print(f"{YELLOW}Country Name          {NORMAL}: " + str(phe.json() ['country_name']))
                      sleep(0.1)
                      print(f"{YELLOW}Location              {NORMAL}: " + str(phe.json() ['location']))
                      sleep(0.1)
                      print(f"{YELLOW}Carrier               {NORMAL}: " + str(phe.json() ['carrier']))
                      sleep(0.1)
                      print(f"{YELLOW}Line Type             {NORMAL}: " + str(phe.json() ['line_type']))
                      sleep(0.1)
                      print(f"{YELLOW}Success               {NORMAL}:{GREEN} " + str(phe.json() ['valid']))
                      sleep(0.1)
                      print ()
                      print(f"{YELLOW}Success               {NORMAL}:{GREEN} " + str(phe.json() ['valid']))
                      sleep(0.1)
                      print ()

                 
        elif V == "3": ### chose 3
                      try:
                          def phoneGW():
                             User_phone = input(f"{WHITE}Enter Number {NORMAL}({GREEN}EX +62xxx){WHITE} :{CRED2}➤ ")
                             default_region = "ID" #DEFAULT COUNTRY INDONESIA

                             import phonenumbers
                             from phonenumbers import carrier, geocoder, timezone
                             parsed_number = phonenumbers.parse(User_phone, default_region) # VARIABLE PHONENUMBERS
                             region_code = phonenumbers.region_code_for_number(parsed_number)
                             jenis_provider = carrier.name_for_number(parsed_number, "en")
                             location = geocoder.description_for_number(parsed_number, "id")
                             is_valid_number = phonenumbers.is_valid_number(parsed_number)
                             is_possible_number = phonenumbers.is_possible_number(parsed_number)
                             formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                             formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
                             number_type = phonenumbers.number_type(parsed_number)
                             timezone1 = timezone.time_zones_for_number(parsed_number)
                             timezoneF = ', '.join(timezone1)

                             print(f"\n {NORMAL}========== {YELLOW}SHOW INFORMATION PHONE NUMBERS {WHITE}==========")
                             sleep(0.1)
                             print(f"\n {NORMAL}Location             :{YELLOW} {location}")
                             sleep(0.1)
                             print(f" {NORMAL}Region Code          :{YELLOW} {region_code}")
                             sleep(0.1)
                             print(f" {NORMAL}Timezone             :{YELLOW} {timezoneF}")
                             sleep(0.1)
                             print(f" {NORMAL}Operator             :{YELLOW} {jenis_provider}")
                             sleep(0.1)
                             print(f" {NORMAL}Valid number         :{YELLOW} {is_valid_number}")
                             sleep(0.1)
                             print(f" {NORMAL}Possible number      :{YELLOW} {is_possible_number}")
                             sleep(0.1)
                             print(f" {NORMAL}International format :{YELLOW} {formatted_number}")
                             sleep(0.1)
                             print(f" {NORMAL}Mobile format        :{YELLOW} {formatted_number_for_mobile}")
                             sleep(0.1)
                             print(f" {NORMAL}Original number      :{YELLOW} {parsed_number.national_number}")
                             sleep(0.1)
                             print(f" {NORMAL}E.164 format         :{YELLOW} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
                             sleep(0.1)
                             print(f" {NORMAL}Country code         :{YELLOW} {parsed_number.country_code}")
                             sleep(0.1)
                             print(f" {NORMAL}Local number         :{YELLOW} {parsed_number.national_number}")
                             sleep(0.1)
                             if number_type == phonenumbers.PhoneNumberType.MOBILE:
                                 print(f" {NORMAL}Type                 :{YELLOW} This is a mobile number")
                                 print ()
                             elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
                                 print(f" {NORMAL}Type                 :{YELLOW} This is a fixed-line number")
                                 print ()
                             else:
                                 print(f" {NORMAL}Type                 :{YELLOW} This is another type of number")
                                 print ()
                          if __name__ == '__main__':
                              phoneGW()
                      except KeyboardInterrupt:
                          print(f" {NORMAL}[{YE}!{NORMAL}] {YE}PROGRAM STOPPED...")



      elif chose == "2": ## MENU 2

                        try:
                            def IP_Track():
                                           sleep(1)
                                           ip = input(f"{WHITE}\n Enter IP target :{CRED2}➤ ") #INPUT IP ADDRESS
                                           print()
                                           print(f' {NORMAL}============= {YELLOW}SHOW INFORMATION IP ADDRESS {NORMAL}=============')
                                           req_api = requests.get(f"http://ipwho.is/{ip}") #API IPWHOIS.IS
                                           ip_data = json.loads(req_api.text)
                                           time.sleep(2)
                                           print(f"{NORMAL}\n IP target       :{YELLOW}", ip)
                                           sleep(0.1)
                                           print(f"{NORMAL} Type IP         :{YELLOW}", ip_data["type"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Country         :{YELLOW}", ip_data["country"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Country Code    :{YELLOW}", ip_data["country_code"])
                                           sleep(0.1)
                                           print(f"{NORMAL} City            :{YELLOW}", ip_data["city"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Continent       :{YELLOW}", ip_data["continent"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Continent Code  :{YELLOW}", ip_data["continent_code"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Region          :{YELLOW}", ip_data["region"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Region Code     :{YELLOW}", ip_data["region_code"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Latitude        :{YELLOW}", ip_data["latitude"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Longitude       :{YELLOW}", ip_data["longitude"])
                                           sleep(0.1)
                                           lat = int(ip_data['latitude'])
                                           lon = int(ip_data['longitude'])
                                           sleep(0.1)
                                           print(f"{NORMAL} Maps            :{YELLOW}",f"https://www.google.com/maps/@{lat},{lon},8z")
                                           sleep(0.1)
                                           print(f"{NORMAL} EU              :{YELLOW}", ip_data["is_eu"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Postal          :{YELLOW}", ip_data["postal"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Calling Code    :{YELLOW}", ip_data["calling_code"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Capital         :{YELLOW}", ip_data["capital"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Borders         :{YELLOW}", ip_data["borders"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Country Flag    :{YELLOW}", ip_data["flag"]["emoji"])
                                           sleep(0.1)
                                           print(f"{NORMAL} ASN             :{YELLOW}", ip_data["connection"]["asn"])
                                           sleep(0.1)
                                           print(f"{NORMAL} ORG             :{YELLOW}", ip_data["connection"]["org"])
                                           sleep(0.1)
                                           print(f"{NORMAL} ISP             :{YELLOW}", ip_data["connection"]["isp"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Domain          :{YELLOW}", ip_data["connection"]["domain"])
                                           sleep(0.1)
                                           print(f"{NORMAL} ID              :{YELLOW}", ip_data["timezone"]["id"])
                                           sleep(0.1)
                                           print(f"{NORMAL} ABBR            :{YELLOW}", ip_data["timezone"]["abbr"])
                                           sleep(0.1)
                                           print(f"{NORMAL} DST             :{YELLOW}", ip_data["timezone"]["is_dst"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Offset          :{YELLOW}", ip_data["timezone"]["offset"])
                                           sleep(0.1)
                                           print(f"{NORMAL} UTC             :{YELLOW}", ip_data["timezone"]["utc"])
                                           sleep(0.1)
                                           print(f"{NORMAL} Current Time    :{YELLOW}", ip_data["timezone"]["current_time"])
                                           print ()
                                           sleep(0.1)
                            if __name__ == '__main__':
                                IP_Track()
                        except KeyboardInterrupt:
                            print(f" {NORMAL}[{YE}!{NORMAL}] {YE}PROGRAM STOPPED...")


      elif chose == "3":
          def instagram():
            import instaloader, sys
            from instaloader import instaloader
            #2 MODULE

            x = instaloader.Instaloader()

            try:
                      print ()
                      sleep(1)
                      uname = input(f"\033[36mEnter a username \033[0m:{CRED2}➤ \033[36m") #INPUT USER
                      if uname == "":
                                      print("\033[33mUnknown command!")
                                      sys.exit()

                      f = instaloader.Profile.from_username(x.context,uname)

                      print("\033[32mUsername\033[0m :", f.username)
                      print("\033[32mID\033[0m :", f.userid)
                      print("\033[32mNama lengkap\033[0m :", f.full_name)
                      print("\033[32mBiografi\033[0m :", f.biography)
                      print("\033[32mNama kategori bisnis\033[0m :", f.business_category_name)
                      print("\033[32mURL eksternal\033[0m :", f.external_url)
                      print("\033[32mDiikuti orang\033[0m :", f.followed_by_viewer)
                      print("\033[32mMengikuti\033[0m :", f.followees)
                      print("\033[32mPengikut\033[0m :", f.followers)
                      print("\033[32mMengikuti orang\033[0m :", f.follows_viewer)
                      print("\033[32mDiblokir orang\033[0m :", f.blocked_by_viewer)
                      print("\033[32mPernah memblokir orang\033[0m :", f.has_blocked_viewer)
                      print("\033[32mPunya sorotan\033[0m :", f.has_highlight_reels)
                      print("\033[32mPunya cerita publik\033[0m :", f.has_public_story)
                      print("\033[32mTelah meminta orang\033[0m :", f.has_requested_viewer)
                      print("\033[32mDiminta orang\033[0m :", f.requested_by_viewer)
                      print("\033[32mMemiliki cerita yang dapat dilihat\033[0m :", f.has_viewable_story)
                      print("\033[32mIGTV\033[0m :", f.igtvcount)
                      print("\033[32mAkun bisnis\033[0m :", f.is_business_account)
                      print("\033[32mAkun pribadi\033[0m :", f.is_private)
                      print("\033[32mDiverifikasi\033[0m :", f.is_verified)
                      print("\033[32mPostingan\033[0m :", f.mediacount)
                      print("\033[32mURL foto profil\033[0m :", f.profile_pic_url)
                      print ()

            except KeyboardInterrupt:
                      print("\033[33mI understand!")

            except EOFError:
                      print("\033[33mWhy?")
          instagram()

                 
      elif chose == "A" or "a": ## MENU 4
                                     sleep(1)
                                     print(f"""{NORMAL}
The OwlSint tool is a tool for searching phone number information 
And for tracking phone numbers,perhaps only a few countries whose 
Location can be tracked using this tool. This tool was created by 
{GREEN}Mr,OwlBird05 {NORMAL}to help you get phone number information. If you want 
To recode this tool don't forget to include the developer's name to
Credit the coder.

// {WHITE}TRANSLATE TO INDONESIAN{NORMAL}

Alat OwlSint adalah alat untuk mencari informasi nomor telepon 
dan untuk melacak nomor telepon, mungkin hanya beberapa negara 
Yang lokasinya dapat dilacak menggunakan alat ini. Alat ini dibuat 
Oleh {GREEN}Mr,OwlBird05 {NORMAL}untuk membantu Anda mendapatkan informasi nomor 
Telepon. Jika Anda ingin Kode ulang alat ini jangan lupa cantumkan 
Nama pengembang untuk menghargai pembuat kode.

""")

### Start tools
start()
### CODED BY MR,OWLBIRD05 / +6283848301116
