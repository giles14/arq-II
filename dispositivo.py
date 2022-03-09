import ntplib
from time import *
import pyotp
hotp = pyotp.HOTP('base32secret3232')

# creamos una variable c para inicializar el objeto ntplib
c = ntplib.NTPClient()

#  Solicitamos al servidor pool.ntp.org que nos envié el tiempo actual y 
#  el valor se guardará en la variable response
response = c.request('pool.ntp.org')
# response.tx_time nos dará el tiempo epoch del servidor en el momento solicitado
# este valor no se actualiza automáticamente y solo tendrá el valor al momento de la llamada
response.tx_time

# Este es el valor que deberás actualizar cada 10 segundos para que se actualice basado en las reestricciones dadas
# puedes utilizar la función de tiempo sleep(n) para poner una pausa de n segundos dentro de un loop while
# de esta forma una vez coordinado la primera vez, podrás mostrar cada 10 segundos un nuevo código
semilla = 0

# Esta instrucción nos generará un codigo unico de 6 digitos que deberemos poner en thread.py.
# Recuerda que en threar.py el valor esperado cambiará cada 10 segundos, por lo que tu programa
# deberá generar un nuevo código cada 10 segundos y ese codigo deberá estar basado en una semilla nueva
# generada de igual forma cada 10 segundos
print(hotp.at(semilla))