def get_note(message):
    while True:
        try:
            return float(input(message)) 
        except ValueError:
            print("خطأ! يرجى إدخال رقم صحيح أو عشري.")

print()
print("=" * 50 + "TP N1 Ex2" + "=" * 50)

notes = []

while True:
    val = get_note("أدخل علامة الطالب (أو عدداً سالباً للتوقف): ")
    
    if val < 0:
        print("تم إيقاف إدخال البيانات.")
        break
    
    # إضافة العلامة للقائمة
    notes.append(val)
    
    # حساب البيانات المطلوبة
    count = len(notes)
    highest = max(notes)
    lowest = min(notes)
    average = sum(notes) / count
    
    # عرض النتائج في كل دورة
    print(f"\n--- الإحصائيات الحالية ---")
    print(f"عدد العلامات: {count}")
    print(f"أعلى علامة: {highest}")
    print(f"أدنى علامة: {lowest}")
    print(f"متوسط جميع العلامات)المعدل): {average:.2f}")
    print("=" * 100)
    print()