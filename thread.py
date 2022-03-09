import threading
from cryptography.fernet import Fernet
from time import *
import ntplib
import pyotp
key = 'UM_Xip80dCSWhVkGRsxiNwf21ceCjWiWK8JT1OSTiPA='.encode()
t1 = 'gAAAAABiJ6CPVOphNbdsTHUr3nIL3Qigv8d8Zevf8Zh7suhlXBEjgWdfzh7R2XZXI0MoC2MnHf8OWT72QKDPXdakG0ON6JVDjCyz4p_Lj0bP15wZdwvEFA53hqVFr_dbfxXBwVo4-WG8'.encode()
t2 = 'gAAAAABiJ6CP1U4FyroAioxHWN8o7XGChTw57D3GFyvtXvxoF-tJ3grWGA2n4c_moau3ZKTheGfwsCrk1XicysiwhwA0j6EhZ5dVNMkR9sqXFJudd61cu_2x88VXUxgI-b1ivJ-XPTC8'.encode()
t3 = 'gAAAAABiJ-x1GNpfwuX6YZ7xOtp8Bk-Ca39uhdB2DhMETRi3b7cIML-q6Er7s_LTt1w8ZWrPSR-J2RU7dNnwPLIB5CSWE4-TWyZWDr4JPSPPfaM5IK7GtM8tXRkgoQ6YvkUlPLZ8dQPV'

def dc(token: bytes, key:bytes) -> bytes:
    return Fernet(key).decrypt(token)
hotp = pyotp.HOTP('fzxxostsjyndbisi')
intento = ''

my_timer = 0
c = ntplib.NTPClient()
response = c.request('pool.ntp.org')
ts = int(response.tx_time)
s = int(response.tx_time)%10
dif = 12 - ts%10
tseed = 0
print(s)
while s != 2:
    print("sincronizando...")
    sleep(1)
    s = (s + 1)%10
    print(s)
    #print(ts)
    
if(s == 2):
    def countdown():
        global my_timer
        global tseed
        
        my_timer = 10
        tseed = ts%10000 + dif + 10
        print(tseed)
        while my_timer > 1 and not(challenge):
            my_timer = my_timer - 1
            sleep(1)
            if my_timer == 1:
                sleep(0.99)
                my_timer = 10
                print("creando nueva semilla")
                tseed = tseed + 10
                
        print(dc(t1,key))
        print(tseed)
    countdown_thread = threading.Thread(target = countdown)
    countdown_thread.start()
else:
    print("desincronizado ")

challenge = False
while my_timer > 0 and not(challenge):
        paso = hotp.at(tseed)
        print(paso)
        intento = input("codigo: ")
        challenge = hotp.verify(intento,tseed)
        if not(challenge):
            print('Código erroneo, intenta de nuevo')
countdown_thread.join()