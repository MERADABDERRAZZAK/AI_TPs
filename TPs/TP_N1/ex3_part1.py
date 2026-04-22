def trier(classeur, valeur):
    if valeur >= 0:
        classeur['positifs'].append(valeur)
    else:
        classeur['négatifs'].append(valeur)
    return classeur

def get_number(message):
    while True:
        try:
            number = input(message)
            if number.upper() == "END":
                return "END"
            return float(number) 
        except ValueError:
            print("خطأ! يرجى إدخال رقم صحيح أو عشري.")

print()
print("=" * 50 + "TP N1 Ex3 Part1" + "=" * 50)


mon_classeur = {'négatifs': [], 'positifs': []}
print("لايقاف الحلقة أدخل end: ")
while True:
    valeur = get_number("أدخل عدد: ")
    if valeur == "END":
        break
    trier(mon_classeur, valeur)
    print(mon_classeur)

print("=" * 100)
print()