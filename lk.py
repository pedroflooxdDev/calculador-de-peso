from pyfiglet import Figlet
import time

f = Figlet(font='small')
print (f.renderText('calculador de peso'))
time.sleep(3)

peso = input("ponga su peso aqui\n>> ")

print('usted pesa %s kg' %peso)
