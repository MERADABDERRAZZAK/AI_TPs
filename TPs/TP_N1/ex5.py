def max_sum(list_of_lists):
    return max(list_of_lists, key=sum)

def max_len(list_of_lists):
    return max(list_of_lists, key=len)

def max_first(list_of_lists):
    return max(list_of_lists, key=lambda x: x[0])

def max_last(list_of_lists):
    return max(list_of_lists, key=lambda x: x[-1])

def get_number(message):
    while True:
        try:
            number = input(message)
            if number.upper() == "END":
                return "END"
            if number.upper() == "EXIT":
                return "EXIT"
            return float(number) 
        except ValueError:
            print("خطأ! يرجى إدخال عدد صحيح أو عشري .")

print()
print("=" * 50 + "TP N1 Ex5" + "=" * 50)

L = []
Ls = []
number = "Start"
print("املأ الليست , للانتقال لملأ الليست الفرعية التالية أدخل end") 
print("لايقاف الملأ أدخل exit") 
while True:

    if number.upper() == "EXIT":
        break 
    while True:    
        number = get_number("أدخل عدد: ")
        if str(number).upper() == "END" or str(number).upper() =="EXIT":
            break   
        Ls.append(number)

    if Ls:
        L.append(Ls)
        Ls = []
    

print(f"المصفوفة الأساسية: {L}\n")
print(f"الأكبر مجموعاً (max_sum):   {max_sum(L)}")
print(f"الأطول (max_len):          {max_len(L)}")
print(f"الأكبر أول عنصر (max_first): {max_first(L)}")
print(f"الأكبر آخر عنصر (max_last):  {max_last(L)}")

print("=" * 100)
print()