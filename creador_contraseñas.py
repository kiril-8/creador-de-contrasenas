#importes usados
import random

#variables
letras = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM" #o string.ascii_letters que son todas las palabras del alfabeto
numero = "1234567890" #o string_digits que son los numeros de 0 al 9
simbolo = "%$·#€/^*\¡" #o string.punctuation que son los simbolos
resp_corr = ("si", "no")

#cual es la longitud que quieres
long_usu = int(input("Cuantos caracteres quieres para tu contraseña: "))



#preguntar si quiere numeros
while True:
    num_resp = input("¿Quieres numeros en tu contraseña?").lower().strip()
    if num_resp in resp_corr:
        break
    else:
        print("Respuesta incorrecta, escribe si o no")
if num_resp == "si":
    num_resp = True
else:
    num_resp = False

#preguntar si quiere letras
while True:
    let_resp = input("¿Quieres letras en tu contraseña?").lower().strip()
    if let_resp in resp_corr:
        break
    else:
        print("Respuesta incorrecta, escribe si o no")

if let_resp == "si":
    let_resp = True
else:
    let_resp = False
#preguntar si quiere simbolos
while True:
    sim_resp = input("¿Quieres simbolo en tu contraseña?").lower().strip()
    if sim_resp in resp_corr:
        break
    else:
        print("Respuesta incorrecta, escribe si o no")
if sim_resp == "si":
    sim_resp = True
else:
    sim_resp = False

total = ""
if let_resp:
    total += letras
if num_resp:
    total += numero
if sim_resp:
    total += simbolo
if total == "":
    print("No has seleccionado ningun caracter. El programa termina")
    exit

contraseña = ""

for _ in range(long_usu):
    contraseña += random.choice(total)
print("Tu contraseña es", contraseña)