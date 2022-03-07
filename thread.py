import threading
from time import *
import ntplib
import pyotp

hotp = pyotp.HOTP('base32secret3232')

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
    print(ts)
    
if(s == 2):
    def countdown():
        global my_timer
        global tseed
        
        my_timer = 10
        tseed = ts%10000 + dif + 10
        print(tseed)
        while my_timer > 1:
            my_timer = my_timer - 1
            sleep(1)
            if my_timer == 1:
                print("creando nueva semilla")
                tseed = tseed + 10
                response = c.request('pool.ntp.org')
                print(response.tx_time)
                print(tseed)
                sleep(1)
                my_timer = 10
        print("se acabo el tiempo")
    countdown_thread = threading.Thread(target = countdown)
    countdown_thread.start()
else:
    print("desincronizado ")

actual = 0   
while my_timer > 0:
        actual = actual + 1
        #print(f"hello world {actual}")
        paso = hotp.at(tseed)
        print(paso)
        intento = input("codigo: ")
        print(hotp.verify(intento,tseed))
        sleep(10)
print("Sin tiempo")