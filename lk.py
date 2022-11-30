from pyfiglet import Figlet
import time

print("\t\t\tSelect a language\n\t\t\t-----------------------------\n\t\t\tSelecciona un lenguaje\n\n")
print("\t\t\t[1] Español\n\t\t\t[[2] English")

lang = input(">> ")
if lang=="1":
	f = Figlet(font='small')
	print (f.renderText('calculador de peso'))
	time.sleep(3)

	peso = input("ponga su peso aqui\n>> ")

	print('usted pesa %s kg' %peso)
if lang=="2":
	f = Figlet(font='small')
	print (f.renderText('Weight Calculator'))
	time.sleep(3)

	peso = input("put your weight here\n>> ")

	print('you weigh %s kg' %peso)
