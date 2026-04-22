def get_positive_int(message):
    
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("يرجى إدخال عدد موجب!")
                continue
            return value
        except ValueError:
            print("خطأ! يرجى إدخال رقم صحيح موجب.")

print()
print("=" * 50 + "TP N1 Ex1" + "=" * 50)
n = get_positive_int("أدخل العدد n: ")
a, b = 0, 1

while a < n:
    print(a, end=' ')
    a, b = b, a + b

print("=" * 100)
print()