# ==================================================
# دالة الأدوات المساعدة (Logic & Utils)
# ==================================================

def chainage_avant(faits, regles):
    """تنفيذ الاستنتاج للأمام البسيط"""
    modification = True
    while modification:
        modification = False
        for regle in regles:
            conditions = regle[0]
            consequence = regle[1]
            
            # التحقق: هل كل الشروط موجودة؟ وهل النتيجة جديدة؟
            all_met = all(c in faits for c in conditions)
            if all_met and consequence not in faits:
                print(f"استنتاج جديد: إضافة {consequence}")
                faits.append(consequence)
                modification = True
    return faits

# ==================================================
# البرنامج الرئيسي (Main Execution)
# ==================================================
print("\n" + "=" * 20 + " TP N2 Ex3 " + "=" * 20)

# إعداد البيانات
base_faits = [
    'animal a des plumes', 
    'animal a un long cou', 
    'animal a de longues pattes'
]

base_regles = [
    [['animal vole', 'animal pond des oeufs'], 'animal est un oiseau'],
    [['animal a des plumes'], 'animal est un oiseau'],
    [['animal est un oiseau', 'animal a un long cou', 'animal a de longues pattes'], 'animal est une autruche']
]

print(f"الحقائق الأولية: {base_faits}")

# تنفيذ الاستنتاج
resultat = chainage_avant(base_faits, base_regles)

print(f"\nالحقائق النهائية: {resultat}")
print("=" * 50)