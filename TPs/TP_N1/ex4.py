def extract_by_indices(L1, L2):
    result = []
    n = len(L1)
    
    for idx in L2:

        if -n <= idx < n:
            result.append(L1[idx])
        else:
            result.append(None)
            
    return result

def get_number(message):
    while True:
        try:
            number = input(message)
            if number.upper() == "END":
                return "END"
            return int(number) 
        except ValueError:
            print("خطأ! يرجى إدخال عدد صحيح .")

print()
print("=" * 50 + "TP N1 Ex4" + "=" * 50)


L1 = []
print("املأ الليست 1, لايقاف الحلقة أدخل end") 
while True: 
    item = input("أدخل العنصر: ")
    if item.upper() == "END":
        break   
    L1.append(item)

L2 = []
print("املأ الليست 2, لايقاف الحلقة أدخل end") 
while True: 
    number = get_number("أدخل عدد: ")
    if number == "END":
        break   
    L2.append(number)



print(f"L1: {L1}")
print(f"L2 (Indices): {L2}")
print(f"النتيجة: {extract_by_indices(L1, L2)}")
print("=" * 100)
print()