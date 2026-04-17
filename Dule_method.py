import os, time, random, sys, requests, uuid

# Colors
G = '\033[1;92m' 
Y = '\033[1;93m' 
W = '\033[1;97m' 
S = '\033[1;96m' 
R = '\033[1;91m'

# --- KEY APPROVAL SYSTEM (UPDATED) ---
def approval():
    os.system('clear')
    # ইউজার ডিভাইসের আইডি দিয়ে একটি পারমানেন্ট কী বানানো হচ্ছে
    try:
        # টার্মাক্স বা লিনাক্সে ইউজার আইডি নেওয়া
        device_id = os.getlogin()
    except:
        # যদি কোনো কারণে login না পাওয়া যায় তবে র্যান্ডম না করে ফিক্সড রাখার চেষ্টা
        device_id = "USER"

    # একটি ইউনিক কী যা ইউজারের ফোনে সবসময় একই থাকবে
    key = f"SHAHIN-VIP-{device_id.upper()}-{uuid.getnode()}"
    
    # আপনার দেওয়া গিটহাব লিঙ্ক
    approval_url = "https://raw.githubusercontent.com/w8Shahin/Approval-control/refs/heads/main/Keys.txt"
    
    print(f"{G} [•] WELCOME TO SHAHIN VIP TOOL")
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    try:
        # গিটহাব থেকে ফাইলটি পড়া হচ্ছে
        active_keys = requests.get(approval_url).text
        
        if key in active_keys:
            print(f" {G}[√] STATUS : APPROVED ACCESS")
            print(f" {W}[•] WELCOME SHAHIN BIN AHMED USER")
            print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            time.sleep(2)
            Main() # এপ্রুভ থাকলে মেইন মেনুতে যাবে
        else:
            # যদি এপ্রুভ না থাকে তবে এখানে কী (Key) দেখাবে
            print(f" {R}[×] STATUS : NOT APPROVED")
            line()
            print(f" {W}[•] YOUR KEY : {G}{key}")
            line()
            print(f" {Y}[!] এই কী (Key) টি কপি করে এডমিনকে পাঠান।")
            print(f" {W}[•] এডমিন যখন এটি গিটহাবে অ্যাড করবে, তখন টুল চলবে।")
            print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            input(f" {G}[ENTER] করলে হোয়াটসঅ্যাপে মেসেজ যাবে...")
            
            # হোয়াটসঅ্যাপে অটো মেসেজ পাঠানোর অপশন
            whatsapp_msg = f"https://wa.me/+8801XXXXXXXXX?text=Assalamu%20Alaikum%20Admin,%20Please%20Approve%20My%20Key:%20{key}"
            os.system(f'termux-open-url "{whatsapp_msg}"')
            sys.exit() # কী দেখানোর পর কোড বন্ধ হবে
            
    except Exception as e:
        print(f" {R}[!] নেটওয়ার্ক সমস্যা বা গিটহাব লিঙ্ক ভুল!")
        print(f" {W}[•] Error: {e}")
        sys.exit()

def line():
    print(f"{W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# [নিচে আপনার বাকি মেইন মেনু এবং ক্লোনিং কোড থাকবে]
