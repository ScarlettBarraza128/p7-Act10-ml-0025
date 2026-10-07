# Emily Barraza NC = 0025

# ==========================================
# 1. IF - CONDICIÓN
# ==========================================
print("+-+-+-+-+-+-+-+ 1. IF - CONDICIÓN +-+-+-+-+-+-+-+-+-")
edad = 20

if edad >= 18:
    print("Eres mayor de edad")


# ==========================================
# 2. IF + ELIF - VARIAS CONDICIONES
# ==========================================
print("+-+-+-+-+-+-+-+ 2. IF + ELIF - VARIAS CONDICIONES +-+-+-+-+-+-+-+-+-")
calificacion = 8

if calificacion >= 9:
    print("Excelente")
elif calificacion >= 6:
    print("Aprobado")


# ==========================================
# 3. IF + ELSE - SI NO SE CUMPLE
# ==========================================
print("+-+-+-+-+-+-+-+ 3- IF + ELSE - SI NO CUMPLE +-+-+-+-+-+-+-+-+-")
edad = 16

if edad >= 18:
    print("Puedes entrar")
else:
    print("No puedes entrar")


# ==========================================
# 4. FOR - CICLO FOR
# ==========================================
print("+-+-+-+-+-+-+-+ 4. FOR - CICLO FOR +-+-+-+-+-+-+-+-+-")
frutas = ["manzana", "pera", "naranja"]

for fruta in frutas:
    print(fruta)


# ==========================================
# 5. WHILE - CICLO WHILE
# ==========================================
print("+-+-+-+-+-+-+-+ 5. WHILE - CICLO WHILE +-+-+-+-+-+-+-+-+-")
numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1
print("Emily Barraza NC = 0025")