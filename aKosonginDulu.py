 import time,sys,os,json,requests,random
except ModuleNotFoundError:
         print ('[!] Install Modul Requests')
         os.system('pip install requests')
	
ip = requests.get('https://api.ipify.org').text
except requests.exceptions.ConnectionError:
        exit(' [!] Koneksi Internet Error')
def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
	
a,m,h,k,b,u,c,p,bn,o = [
'\033[90m',
'\033[31m',
'\033[32m',
'\033[33m',
'\033[94m',
'\033[35m',
'\033[36m',
'\033[37m',
'\033[41m',
'\033[0m'
]

print ('%s[%s+%s] %sIP Kamu %s: %s%s' % (p,h,p,k,m,h,ip))
print ('\033[37m[\033[33m•\033[37m]\033[33m :\033[33m \033[32mMax 10\033[32m ')
