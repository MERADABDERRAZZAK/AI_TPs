def difference(L1, L2):
    diff1 = [item for item in L1 if item not in L2]
    diff2 = [item for item in L2 if item not in L1]
    return (diff1, diff2)

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

L1, L2 = [], []

print("املأ الليست 1, لايقاف الحلقة أدخل end") 
while True: 
    number = get_number("أدخل عدد: ")
    if number == "END":
        break   
    L1.append(number)

print("املأ الليست 2, لايقاف الحلقة أدخل end")     
while True: 
    number = get_number("أدخل عدد: ")
    if number == "END":
        break   
    L2.append(number)


diff1, diff2 = difference(L1, L2)
print(f"diff1: {diff1}") 
print(f"diff2: {diff2}") 

print("=" * 100)
print()