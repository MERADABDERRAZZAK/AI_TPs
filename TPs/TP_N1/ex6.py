# ==================================================
# دالة الأدوات المساعدة (Utils)
# ==================================================

def get_input(message, allow_tuple=False):
    """
    دالة شاملة لإدارة الإدخال:
    - تدعم الأرقام (int/float)
    - تدعم النصوص (END/EXIT)
    - تدعم إدخال التوبل إذا تم تفعيل allow_tuple (مثل: 1,2)
    """
    while True:
        user_input = input(message).strip()
        
        # التعامل مع أوامر الخروج والتوقف
        if user_input.upper() in ["END", "EXIT"]:
            return user_input.upper()
        
        # إذا كنا نتوقع إدخال توبل (للتمرين السادس)
        if allow_tuple and "," in user_input:
            try:
                # تحويل النص "1,2" إلى توبل من أرقام (1.0, 2.0)
                return tuple(float(x) for x in user_input.split(","))
            except ValueError:
                print("خطأ! لإدخال توبل استخدم الصيغة: رقم,رقم (مثال: 5,10)")
                continue

        # محاولة التحويل لرقم عادي
        try:
            return float(user_input)
        except ValueError:
            # إذا فشل التحويل وكان النص عادياً (مثل التمرين 4) نعيده كنص
            return user_input

# ==================================================
# حلول التمارين (Logic)
# ==================================================

def tuples_to_dict(L):
    """حل التمرين 6: تحويل قائمة توبل إلى قاموس مفاتيحُه هي الفهارس"""
    return {i: t for i, t in enumerate(L)}

# ==================================================
# البرنامج الرئيسي (Main Execution)
# ==================================================

print()
print("=" * 50 + "TP N1 Ex6" + "=" * 50)
print("تشغيل التمرين السادس: تحويل قائمة توبل إلى قاموس")
print("=" * 50)

list_of_tuples = []

print("تعليمات:")
print("- أدخل الأرقام بصيغة (رقم,رقم) لإنشاء توبل، مثال: 1,2")
print("- أدخل 'END' لإنهاء القائمة وعرض النتيجة")

while True:
    entry = get_input("أدخل توبل (مثلاً 5,10): ", allow_tuple=True)
    
    if entry == "END" or entry == "EXIT":
        break
    
    if isinstance(entry, tuple):
        list_of_tuples.append(entry)
    else:
        print("تنبيه: سيتم إضافة المدخل كعنصر وحيد لأنه ليس توبل.")
        list_of_tuples.append(entry)

# عرض النتيجة النهائية
if list_of_tuples:
    result = tuples_to_dict(list_of_tuples)
    print(f"\nالقائمة التي أدخلتها: {list_of_tuples}")
    print(f"القاموس الناتج (الفهرس كـ Key):")
    print(result)
else:
    print("\nلم يتم إدخال أي بيانات.")

print("=" * 100)