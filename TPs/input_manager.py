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