import ntplib
from time import *
import pyotp
hotp = pyotp.HOTP('fzxxostsjyndbisi')

# creamos una variable c para inicializar el objeto ntplib
c = ntplib.NTPClient()

#  Solicitamos al servidor pool.ntp.org que nos envié el tiempo actual y 
#  el valor se guardará en la variable response
response = c.request('pool.ntp.org')
# response.tx_time nos dará el tiempo epoch del servidor en el momento solicitado
# este valor no se actualiza automáticamente y solo tendrá el valor al momento de la llamada
print(response.tx_time)
epoch = int(response.tx_time)

semilla = 0
cambio = 10
if epoch%10 == 2:
    while True:
        #print('semilla generada')
        semilla = epoch%10000 + cambio
        #print(semilla)
        print(hotp.at(semilla))
        cambio = cambio +10
        sleep(9.9)
    

# Este es el valor que deberás actualizar cada 10 segundos para que se actualice basado en las reestricciones dadas


# Esta instrucción nos generará un codigo unico de 6 digitos que deberemos poner en thread.py.
# Recuerda que en threar.py el valor esperado cambiará cada 10 segundos, por lo que tu programa
# deberá generar un nuevo código cada 10 segundos y ese codigo deberá estar basado en una semilla nueva
# generada de igual forma cada 10 segundos
#print(hotp.at(semilla))