nombre = input("INGRESE SU NOMBRE ")
genero = input("INGRESE SU GENERO (M o F) ")
if (genero == "F" and nombre.lower() < 'm') or (genero == "M" and nombre.lower() > 'n'):
    grupo = "A"
else:
    grupo = "B"
print("Tu grupo es " + grupo)