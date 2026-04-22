# ==================================================
# دالة الأدوات المساعدة (Utils)
# ==================================================
regles = [] # الهيكل: [ [الشروط], النتيجة ]

# ==================================================
# حلول التمارين (Logic)
# ==================================================

def ajouter_regle(conditions, consequence):
    """2. إضافة قاعدة"""
    regles.append([conditions, consequence])

def afficher_regles():
    """1. عرض القواعد"""
    for r in regles:
        print(f"SI {r[0]} ALORS {r[1]}")

def get_conditions(regle):
    """3. إرجاع الشروط"""
    return regle[0]

def get_consequence(regle):
    """4. إرجاع النتيجة"""
    return regle[1]

def fait_satisfait_condition(fait, regle):
    """5. هل الحقيقة تحقق أحد الشروط؟"""
    return fait in regle[0]

def conditions_satisfaites(regle, base_faits):
    """6. هل كل الشروط متوفرة في قاعدة الحقائق؟"""
    for cond in regle[0]:
        if cond not in base_faits:
            return False
    return True

# ==================================================
# البرنامج الرئيسي (Main Execution)
# ==================================================
print("\n" + "=" * 20 + " TP N2 Ex2 " + "=" * 20)
ajouter_regle(['animal a des plumes'], 'animal est un oiseau')
afficher_regles()

# تجربة التحقق (مثال)
test_faits = ['animal a des plumes']
print(f"هل الشروط محققة؟ {conditions_satisfaites(regles[0], test_faits)}")
print("=" * 50)